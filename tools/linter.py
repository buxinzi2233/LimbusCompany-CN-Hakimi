#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/linter.py: 都市零协会（LLC）自动化静态质检与代码安全引擎 (LLC Linter Engine v2.0)

Strictly enforces the 8 Localization and Technical Safety Rules:
- Rule 1 (L01, FATAL): JSON validity, UTF-8/BOM decoding, and schema integrity
- Rule 2 (L02, FATAL): Zero full-width tilde (～ / \\uFF5E and 〜 / \\u301C)
- Rule 3 (L03, FATAL/ERROR): Placeholder 1:1 match and unclosed brace detection
- Rule 4 (L04, ERROR): Keyword trailing space ([关键词] ) with negative lookahead
- Rule 5 (L05, FATAL): Unity TextMeshPro tag balance and LIFO nesting validation
- Rule 6 (L06, ERROR): Verb triad enforcement (获得 / 施加 / 增加 / 减少 / 消耗)
- Rule 7 (L07, WARN): Typography standards (……, “”, ——)
- Rule 8 (L08, FATAL/ERROR): Korean residue scan with absolute whitelist for 'model'
"""

import argparse
import ast
from collections import Counter
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
import json
import multiprocessing
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Dict, Generator, List, Optional, Set, Tuple, Union
if __package__:
    from .keyword_names import keyword_directory, load_keyword_names
    from .resource_fields import metadata_reason
    from .source_snapshot import resolve_source_directory
else:
    from keyword_names import keyword_directory, load_keyword_names
    from resource_fields import metadata_reason
    from source_snapshot import resolve_source_directory

# ----------------------------------------------------------------------
# Constants & Defaults
# ----------------------------------------------------------------------

DEFAULT_WORKSPACE_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN"
DEFAULT_STEAM_KR_DIR = (
    "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/"
    "LimbusCompany_Data/Assets/Resources_moved/Localize/kr"
)

# Rule Canonical IDs & Aliases
CANONICAL_RULES = {
    "L01": "RULE_1_JSON_INTEGRITY",
    "L02": "RULE_2_FULLWIDTH_TILDE",
    "L03": "RULE_3_PLACEHOLDER_PARITY",
    "L04": "RULE_4_KEYWORD_SPACE",
    "L05": "RULE_5_TMP_TAGS",
    "L06": "RULE_6_VERB_TRIAD",
    "L07": "RULE_7_TYPOGRAPHY",
    "L08": "RULE_8_KOREAN_RESIDUE",
}

RULE_ALIASES = {
    "1": "L01", "l01": "L01", "rule1": "L01", "rule_1": "L01", "json": "L01", "rule_1_json_integrity": "L01",
    "2": "L02", "l02": "L02", "rule2": "L02", "rule_2": "L02", "tilde": "L02", "rule_2_fullwidth_tilde": "L02",
    "3": "L03", "l03": "L03", "rule3": "L03", "rule_3": "L03", "placeholder": "L03", "rule_3_placeholder_parity": "L03",
    "4": "L04", "l04": "L04", "rule4": "L04", "rule_4": "L04", "keyword": "L04", "rule_4_keyword_space": "L04",
    "5": "L05", "l05": "L05", "rule5": "L05", "rule_5": "L05", "tmp": "L05", "tags": "L05", "rule_5_tmp_tags": "L05",
    "6": "L06", "l06": "L06", "rule6": "L06", "rule_6": "L06", "verb": "L06", "verbs": "L06", "rule_6_verb_triad": "L06",
    "7": "L07", "l07": "L07", "rule7": "L07", "rule_7": "L07", "typography": "L07", "punct": "L07", "rule_7_typography": "L07",
    "8": "L08", "l08": "L08", "rule8": "L08", "rule_8": "L08", "korean": "L08", "rule_8_korean_residue": "L08",
}

# Regex Definitions
RE_FULLWIDTH_TILDE = re.compile(r"[\uff5e\u301c]")
RE_PLACEHOLDER = re.compile(r"\{([A-Za-z0-9_:]+)\}")

# Rule 4 Keywords
RE_KW_NO_SPACE = re.compile(r"(\[(?!\{[A-Za-z0-9_:]+\}\])[^\]\n\r]+\])(?=[\u4e00-\u9fa50-9\[])")
RE_KW_DOUBLE_SPACE = re.compile(r"(\[(?!\{[A-Za-z0-9_:]+\}\])[^\]\n\r]+\])[ \t]{2,}")
RE_KW_EOS = re.compile(r"(\[(?!\{[A-Za-z0-9_:]+\}\])[^\]\n\r]+\])(?=$|\n)")
CORE_KWS_PATTERN = r"(?:震颤|流血|呼吸法|充能|沉沦|破裂|烧伤)"
RE_CORE_NO_SPACE = re.compile(rf"(?<!\[)({CORE_KWS_PATTERN})(?!(?:引爆|抗性|同步|泛滥|易损|守护|力场))(?=[\u4e00-\u9fa50-9])")
RE_CORE_DOUBLE_SPACE = re.compile(rf"(?<!\[)({CORE_KWS_PATTERN})[ \t]{{2,}}")

# Rule 5 TMP Tags
TMP_TAG_RE = re.compile(r'<(/?)(\w+)(?:=[^>]*|\s+[^>]*)?>', re.IGNORECASE)
TMP_PAIRED_TAGS = {'color', 'b', 'i', 'size', 'mark', 'u', 'style', 'ruby', 'voffset', 'noparse', 'link', 's'}
TMP_VOID_TAGS = {'sprite', 'br'}

# Rule 6 Verbs
POS_STATUS = r'(?:呼吸法|充能|守护|迅捷|强壮|忍耐)'
NEG_STATUS = r'(?:流血|震颤(?!同步)|沉沦|破裂(?!守护)|烧伤|束缚|易损|虚弱|破绽|麻痹)'
ALL_STATUS = r'(?:呼吸法|充能|守护|迅捷|强壮|忍耐|流血|震颤|沉沦|破裂|烧伤|束缚|易损)'
TARGET_MODIFIER = r'(?:\s*(?:自身|目标|敌方|友方|其|全体|其他罪人|给\S+|对\S+|向\S+))?'

RE_POS_ERR = re.compile(
    rf'(?:施加|赋予|加上|给予|附着|烙印){TARGET_MODIFIER}\s*[0-9一二两三四五六七八九十]*\s*层?\s*{POS_STATUS}'
)
RE_NEG_ERR = re.compile(
    rf'(?:获得|得到|加上|给予|附着|烙印){TARGET_MODIFIER}\s*[0-9一二两三四五六七八九十]*\s*层?\s*{NEG_STATUS}(?!\s*强度)'
)
RE_POT_ERR_POST = re.compile(
    rf'{ALL_STATUS}\s*强度\s*(?:获得(?![量])|施加(?![量])|叠加|提升)'
)
RE_POT_ERR_PRE = re.compile(
    rf'(?:获得(?![量])|施加(?![量])|叠加|提升){TARGET_MODIFIER}\s*[0-9一二两三四五六七八九十]+\s*(?:点|级)?\s*{ALL_STATUS}\s*强度'
)
RE_DECAY_ERR_1 = re.compile(
    rf'{ALL_STATUS}\s*(?:层数|次数)\s*(?:降低|扣减|剥夺)'
)
RE_DECAY_ERR_2 = re.compile(
    rf'(?:降低|扣减|剥夺){TARGET_MODIFIER}\s*[0-9一二两三四五六七八九十]*\s*层?\s*{ALL_STATUS}'
)

# Rule 7 Typography
RE_ASCII_ELLIPSIS = re.compile(r'(?<![0-9a-zA-Z_.])\.\.\.+(?![0-9a-zA-Z_])')
RE_CIRCLE_ELLIPSIS = re.compile(r'。。。+')
RE_SINGLE_ELLIPSIS = re.compile(r'(?<!…)…(?!…)')
RE_FULLWIDTH_MINUS = re.compile(r'－')
RE_DOUBLE_HYPHEN = re.compile(r'(?<![<!-])--(?![-!>0-9])')
TMP_TAG_STRIP = re.compile(r'<[^>]+>')

# Rule 8 Korean
HANGUL_RE = re.compile(r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]')
KOREAN_WHITELISTED_KEYS = {'model'}
KOREAN_FILE_KEY_WHITELIST = {
    'ScenarioModelCodes-AutoCreated.json': {'id'}
}

# ANSI Color Codes
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"
COLOR_BOLD = "\033[1m"


# ----------------------------------------------------------------------
# Core Data Models
# ----------------------------------------------------------------------

class Severity(str, Enum):
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARN = "WARN"
    INFO = "INFO"


@dataclass
class Issue:
    rule: str
    severity: Severity
    filepath: str
    line: Optional[int] = None
    col: Optional[int] = None
    json_path: Optional[str] = None
    message: str = ""
    snippet: str = ""
    fixable: bool = False
    fixed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rule": self.rule,
            "severity": self.severity.value if hasattr(self.severity, "value") else str(self.severity),
            "filepath": self.filepath,
            "line": self.line,
            "col": self.col,
            "json_path": self.json_path,
            "message": self.message,
            "snippet": self.snippet,
            "fixable": self.fixable,
            "fixed": self.fixed,
        }


# Alias for backward compatibility
LintIssue = Issue


@dataclass
class LintConfig:
    target: str = DEFAULT_WORKSPACE_DIR
    fix: bool = False
    check_korean: bool = False
    json_report: Optional[str] = None
    strict: bool = False
    source_dir: Optional[str] = None
    rules: Optional[Union[str, List[str]]] = None
    workers: int = 0
    quiet: bool = False
    no_color: bool = False

    def get_enabled_rule_ids(self) -> Set[str]:
        """Resolve canonical enabled rule IDs (e.g. {'L01', 'L02', ...})."""
        if not self.rules:
            all_rules = set(CANONICAL_RULES.keys())
            if not self.check_korean:
                all_rules.discard("L08")
            return all_rules

        rule_list = self.rules if isinstance(self.rules, list) else self.rules.split(",")
        resolved: Set[str] = set()
        for r in rule_list:
            cleaned = r.strip().lower()
            if cleaned in RULE_ALIASES:
                resolved.add(RULE_ALIASES[cleaned])
            elif r.strip().upper() in CANONICAL_RULES:
                resolved.add(r.strip().upper())
        return resolved


@dataclass
class LintReport:
    total_scanned_files: int = 0
    total_fixed_files: int = 0
    execution_time_seconds: float = 0.0
    fatal_count: int = 0
    error_count: int = 0
    warn_count: int = 0
    info_count: int = 0
    passed: bool = True
    exit_code: int = 0
    issues: List[Issue] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": "2.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "total_scanned_files": self.total_scanned_files,
                "total_fixed_files": self.total_fixed_files,
                "execution_time_seconds": round(self.execution_time_seconds, 3),
                "fatal_count": self.fatal_count,
                "error_count": self.error_count,
                "warn_count": self.warn_count,
                "info_count": self.info_count,
                "passed": self.passed,
                "exit_code": self.exit_code,
            },
            "issues": [issue.to_dict() for issue in self.issues],
        }


# ----------------------------------------------------------------------
# Rule 1: JSON Integrity & Traversal
# ----------------------------------------------------------------------

def check_json_syntax(
    content: str,
    filepath: str = ""
) -> Tuple[Optional[Dict[str, Any]], List[Issue]]:
    """
    Rule 1: Validates UTF-8 encoding, BOM handling, and structural schemas.
    Returns (parsed_data, issues).
    """
    issues: List[Issue] = []

    # Strip UTF-8 BOM if present
    if content.startswith('\ufeff'):
        content = content[1:]

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        issues.append(Issue(
            rule="L01_JSON_INTEGRITY",
            severity=Severity.FATAL,
            filepath=filepath,
            line=e.lineno,
            col=e.colno,
            json_path="root",
            message=f"JSON 语法解析崩溃: {e.msg}",
            snippet=content.splitlines()[e.lineno - 1] if 0 < e.lineno <= len(content.splitlines()) else "",
            fixable=False
        ))
        return None, issues

    if not isinstance(data, dict):
        issues.append(Issue(
            rule="L01_JSON_INTEGRITY",
            severity=Severity.FATAL,
            filepath=filepath,
            json_path="root",
            message=f"根对象结构异常: 必须为 JSON Object (dict)，实际为 {type(data).__name__}",
            fixable=False
        ))
        return None, issues

    if "dataList" not in data:
        issues.append(Issue(
            rule="L01_JSON_INTEGRITY",
            severity=Severity.FATAL,
            filepath=filepath,
            json_path="root",
            message="缺失零协会基础规范根字段 'dataList'",
            fixable=False
        ))
        return None, issues

    if not isinstance(data["dataList"], list):
        issues.append(Issue(
            rule="L01_JSON_INTEGRITY",
            severity=Severity.FATAL,
            filepath=filepath,
            json_path="root.dataList",
            message=f"'dataList' 必须为 Array (list)，实际为 {type(data['dataList']).__name__}",
            fixable=False
        ))
        return None, issues

    # Sub-structural checks
    for i, item in enumerate(data["dataList"]):
        item_label = f"dataList[{item.get('id', item.get('key', i))}]" if isinstance(item, dict) else f"dataList[{i}]"
        if not isinstance(item, dict):
            issues.append(Issue(
                rule="L01_JSON_INTEGRITY",
                severity=Severity.ERROR,
                filepath=filepath,
                json_path=item_label,
                message=f"dataList 元素类型错误: 期望 dict，实际为 {type(item).__name__}",
                fixable=False
            ))
            continue

        if "levelList" in item:
            if not isinstance(item["levelList"], list):
                issues.append(Issue(
                    rule="L01_JSON_INTEGRITY",
                    severity=Severity.ERROR,
                    filepath=filepath,
                    json_path=f"{item_label}.levelList",
                    message="levelList 必须为 list",
                    fixable=False
                ))
            else:
                for j, lvl in enumerate(item["levelList"]):
                    lvl_label = f"{item_label}.levelList[level={lvl.get('level', j)}]" if isinstance(lvl, dict) else f"{item_label}.levelList[{j}]"
                    if not isinstance(lvl, dict):
                        issues.append(Issue(
                            rule="L01_JSON_INTEGRITY",
                            severity=Severity.ERROR,
                            filepath=filepath,
                            json_path=lvl_label,
                            message="levelList 条目必须为 dict",
                            fixable=False
                        ))
                    elif "coinlist" in lvl and not isinstance(lvl["coinlist"], list):
                        issues.append(Issue(
                            rule="L01_JSON_INTEGRITY",
                            severity=Severity.ERROR,
                            filepath=filepath,
                            json_path=f"{lvl_label}.coinlist",
                            message="coinlist 必须为 list",
                            fixable=False
                        ))

        if "texts" in item and not isinstance(item["texts"], list):
            issues.append(Issue(
                rule="L01_JSON_INTEGRITY",
                severity=Severity.ERROR,
                filepath=filepath,
                json_path=f"{item_label}.texts",
                message="RPGSystem 'texts' 字段必须为 list",
                fixable=False
            ))

        if "steps" in item and not isinstance(item["steps"], list):
            issues.append(Issue(
                rule="L01_JSON_INTEGRITY",
                severity=Severity.ERROR,
                filepath=filepath,
                json_path=f"{item_label}.steps",
                message="RPGSystem 'steps' 字段必须为 list",
                fixable=False
            ))

    return data, issues


def traverse_json_strings(
    node: Any,
    path: str = "",
    parent_ctx: Optional[Dict[str, Any]] = None
) -> Generator[Tuple[str, str, Dict[str, Any]], None, None]:
    """
    Universal recursive visitor yielding (json_path, text_string, context_dict).
    Handles dataList, levelList, coinlist, coindescs, texts, steps, etc.
    """
    if parent_ctx is None:
        parent_ctx = {}

    if isinstance(node, dict):
        curr_ctx = dict(parent_ctx)
        for key in ("id", "key", "index", "teller", "speaker", "title"):
            if key in node:
                curr_ctx[key] = node[key]

        for k, v in node.items():
            child_path = f"{path}.{k}" if path else k
            child_ctx = dict(curr_ctx)
            child_ctx["_key_name"] = k
            if isinstance(v, str):
                yield child_path, v, child_ctx
            elif isinstance(v, (dict, list)):
                yield from traverse_json_strings(v, child_path, child_ctx)

    elif isinstance(node, list):
        identities = []
        for elem in node:
            identity = ""
            if isinstance(elem, dict):
                for id_prop in ("id", "key", "level", "index"):
                    if id_prop in elem:
                        identity = f"{id_prop}={elem[id_prop]}"
                        break
            identities.append(identity)
        identity_counts = Counter(identities)
        for i, elem in enumerate(node):
            elem_id = ""
            if isinstance(elem, dict):
                for id_prop in ("id", "key", "level", "index"):
                    if id_prop in elem:
                        elem_id = f"{id_prop}={elem[id_prop]}"
                        break
            if elem_id and identity_counts[elem_id] > 1:
                elem_id = f"{elem_id},position={i}"
            selector = f"[{elem_id or i}]"
            child_path = f"{path}{selector}" if path else selector
            yield from traverse_json_strings(elem, child_path, parent_ctx)
    elif isinstance(node, str):
        yield path, node, dict(parent_ctx)


# ----------------------------------------------------------------------
# Rule 2: Zero Full-Width Tilde
# ----------------------------------------------------------------------

def has_fullwidth_tilde(text: str) -> bool:
    """Check if string contains forbidden full-width tilde (U+FF5E) or wave dash (U+301C)."""
    return bool(RE_FULLWIDTH_TILDE.search(text))


def check_fullwidth_tilde(raw_content: str, filepath: str = "") -> List[Issue]:
    """Rule 2: Absolute 0 tolerance for full-width tilde (U+FF5E) and wave dash (U+301C)."""
    issues: List[Issue] = []
    for line_idx, line in enumerate(raw_content.splitlines(), start=1):
        for match in RE_FULLWIDTH_TILDE.finditer(line):
            char_found = match.group(0)
            u_hex = f"U+{ord(char_found):04X}"
            col_idx = match.start() + 1
            issues.append(Issue(
                rule="L02_FULLWIDTH_TILDE",
                severity=Severity.FATAL,
                filepath=filepath,
                line=line_idx,
                col=col_idx,
                message=f"检测到违规全角波浪号 '{char_found}' ({u_hex})！导致游戏实机显示为方框乱码 '□'。必须替换为半角 '~'",
                snippet=line.strip(),
                fixable=True
            ))
    return issues


def fix_fullwidth_tilde(raw_content: str) -> Tuple[str, int]:
    """Replaces all full-width tildes and wave dashes with ASCII '~'."""
    return RE_FULLWIDTH_TILDE.subn("~", raw_content)


# ----------------------------------------------------------------------
# Rule 3: Placeholder 1:1 Parity & Unclosed Braces
# ----------------------------------------------------------------------

def extract_placeholders(text: str) -> List[str]:
    """Extract format placeholder variable names (e.g. {0}, {1}, {Slot}, {0:F1})."""
    return RE_PLACEHOLDER.findall(text)


def check_unclosed_braces(text: str) -> bool:
    """Returns True if text contains unclosed or stray '{' or '}' braces."""
    stripped = RE_PLACEHOLDER.sub("", text)
    return "{" in stripped or "}" in stripped


def check_placeholders(
    zh_text: str,
    kr_text: Optional[str] = None,
    filepath: str = "",
    item_id: Optional[str] = None,
    json_path: str = ""
) -> List[Issue]:
    """
    Rule 3: Enforces placeholder 1:1 parity and catches unclosed braces.
    """
    issues: List[Issue] = []

    # 1. Check for unclosed / orphaned braces
    if check_unclosed_braces(zh_text):
        issues.append(Issue(
            rule="L03_PLACEHOLDER_PARITY",
            severity=Severity.FATAL,
            filepath=filepath,
            json_path=json_path,
            message=f"ID {item_id or ''}: 检测到未闭合或残缺大括号 '{{' / '}}'，运行时将引发 C# string.Format 崩溃！",
            snippet=zh_text,
            fixable=False
        ))
        return issues

    # 2. Compare against KR baseline if available
    if kr_text is not None:
        kr_phs = extract_placeholders(kr_text)
        zh_phs = extract_placeholders(zh_text)
        kr_set = set(kr_phs)
        zh_set = set(zh_phs)

        missing = kr_set - zh_set
        extra = zh_set - kr_set

        if missing:
            issues.append(Issue(
                rule="L03_PLACEHOLDER_PARITY",
                severity=Severity.FATAL,
                filepath=filepath,
                json_path=json_path,
                message=f"ID {item_id or ''}: 占位符与韩文源不匹配! 遗漏占位符 {sorted(missing)}",
                snippet=f"KR: {kr_text} | ZH: {zh_text}",
                fixable=False
            ))

        if extra:
            issues.append(Issue(
                rule="L03_PLACEHOLDER_PARITY",
                severity=Severity.FATAL,
                filepath=filepath,
                json_path=json_path,
                message=f"ID {item_id or ''}: 占位符与韩文源不匹配! 多余/错改占位符 {sorted(extra)}",
                snippet=f"KR: {kr_text} | ZH: {zh_text}",
                fixable=False
            ))

        if not missing and not extra and sorted(kr_phs) != sorted(zh_phs):
            issues.append(Issue(
                rule="L03_PLACEHOLDER_PARITY",
                severity=Severity.ERROR,
                filepath=filepath,
                json_path=json_path,
                message=f"ID {item_id or ''}: 占位符出现频次不守恒: 韩文原版 {Counter(kr_phs)} vs 汉化译文 {Counter(zh_phs)}",
                snippet=f"KR: {kr_text} | ZH: {zh_text}",
                fixable=False
            ))

    return issues


# ----------------------------------------------------------------------
# Rule 4: Keyword Trailing Space
# ----------------------------------------------------------------------

def check_keyword_trailing_space(
    text: str,
    filepath: str = "",
    json_path: str = ""
) -> List[Issue]:
    """Rule 4: Validates trailing space after all bracketed and core keywords."""
    issues: List[Issue] = []

    # 1. Bracketed keyword missing space before text/digit/bracket
    for m in RE_KW_NO_SPACE.finditer(text):
        tag = m.group(1)
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"关键词 '{tag}' 后缺少半角空格 (0x20)，不符合关键词格式约定",
            snippet=text[max(0, m.start() - 5):min(len(text), m.end() + 10)],
            fixable=True
        ))

    # 2. Bracketed keyword with multiple spaces
    for m in RE_KW_DOUBLE_SPACE.finditer(text):
        tag = m.group(1)
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"关键词 '{tag}' 尾随多个空格，破坏排版规范",
            snippet=text[max(0, m.start() - 5):min(len(text), m.end() + 10)],
            fixable=True
        ))

    # 3. Bracketed keyword at end-of-string
    for m in RE_KW_EOS.finditer(text):
        tag = m.group(1)
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"行尾/字符串末尾关键词 '{tag}' 缺少尾随半角空格",
            snippet=text[max(0, m.start() - 5):m.end()],
            fixable=True
        ))

    # 4. Core 7 unbracketed keywords
    for m in RE_CORE_NO_SPACE.finditer(text):
        kw = m.group(1)
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"核心机制词条 '{kw}' 缺少尾随半角空格",
            snippet=text[max(0, m.start() - 5):min(len(text), m.end() + 10)],
            fixable=True
        ))

    # 5. Core 7 unbracketed multiple spaces
    for m in RE_CORE_DOUBLE_SPACE.finditer(text):
        kw = m.group(1)
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"核心机制词条 '{kw}' 尾随多个空格",
            snippet=text[max(0, m.start() - 5):min(len(text), m.end() + 10)],
            fixable=True
        ))

    return issues


def check_known_keyword_spaces(
    text: str,
    filepath: str,
    json_path: str,
    keyword_names: frozenset[str],
) -> List[Issue]:
    """Check encoded IDs and exact dictionary names, never bare prose or headings."""
    if HANGUL_RE.search(text):
        return []
    issues: List[Issue] = []
    for match in re.finditer(r"\[([^\]\n\r]+)\]", text):
        name = match.group(1)
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name) and name not in keyword_names:
            continue
        suffix = text[match.end():]
        if not suffix.startswith(" "):
            message = f"关键词 '{match.group(0)}' 后缺少半角空格 (0x20)，不符合关键词格式约定"
        elif re.match(r"[ \t]{2,}", suffix):
            message = f"关键词 '{match.group(0)}' 尾随多个空格，破坏排版规范"
        else:
            continue
        issues.append(Issue(
            rule="L04_KEYWORD_SPACE",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=message,
            snippet=text[max(0, match.start() - 5):match.end() + 10],
            fixable=True,
        ))
    return issues


def fix_keyword_trailing_space(text: str) -> Tuple[str, int]:
    """Idempotent auto-repair for keyword trailing space rules."""
    count = 0
    text, c1 = RE_KW_DOUBLE_SPACE.subn(r"\1 ", text)
    count += c1
    text, c2 = RE_KW_NO_SPACE.subn(r"\1 ", text)
    count += c2
    text, c3 = RE_KW_EOS.subn(r"\1 ", text)
    count += c3
    text, c4 = RE_CORE_DOUBLE_SPACE.subn(r"\1 ", text)
    count += c4
    text, c5 = RE_CORE_NO_SPACE.subn(r"\1 ", text)
    count += c5
    return text, count


# ----------------------------------------------------------------------
# Rule 5: Unity TMP Tag Nesting & Balance
# ----------------------------------------------------------------------

def check_tmp_tags(text: str, filepath: str = "", json_path: str = "") -> List[Issue]:
    """
    Rule 5: Unity TMP Tag Nesting & Balance (FATAL)
    Uses a push-down automaton (stack) to enforce pairing and LIFO nesting.
    """
    if not text or '<' not in text:
        return []

    issues: List[Issue] = []
    stack: List[Tuple[str, str, int]] = []  # (tag_name, full_tag, start_pos)

    for match in TMP_TAG_RE.finditer(text):
        is_closing = bool(match.group(1))
        tag_name = match.group(2).lower()
        full_tag = match.group(0)
        start_pos = match.start()

        # Ignore void tags (<sprite>, <br>)
        if tag_name in TMP_VOID_TAGS:
            continue

        # Ignore non-TMP dialogue brackets (<嘀嗒>, <E.G.O>, etc.)
        if tag_name not in TMP_PAIRED_TAGS:
            continue

        if not is_closing:
            stack.append((tag_name, full_tag, start_pos))
        else:
            if not stack:
                issues.append(Issue(
                    rule="L05_TMP_TAGS",
                    severity=Severity.FATAL,
                    filepath=filepath,
                    json_path=json_path,
                    message=f"多余闭标签 {full_tag} 位于字符索引 {start_pos}，无对应开标签",
                    snippet=text[max(0, start_pos - 10):min(len(text), start_pos + 20)],
                    fixable=False
                ))
            else:
                top_name, top_full, top_pos = stack.pop()
                if top_name != tag_name:
                    issues.append(Issue(
                        rule="L05_TMP_TAGS",
                        severity=Severity.FATAL,
                        filepath=filepath,
                        json_path=json_path,
                        message=f"标签嵌套错乱 (违反 LIFO): 在索引 {top_pos} 开启了 {top_full}，但在索引 {start_pos} 错误闭合为 {full_tag}",
                        snippet=text[max(0, top_pos):min(len(text), start_pos + len(full_tag) + 10)],
                        fixable=False
                    ))

    if stack:
        for rem_name, rem_full, rem_pos in stack:
            issues.append(Issue(
                rule="L05_TMP_TAGS",
                severity=Severity.FATAL,
                filepath=filepath,
                json_path=json_path,
                message=f"检测到未闭合富文本开标签: {rem_full} 位于字符索引 {rem_pos}",
                snippet=text[max(0, rem_pos):min(len(text), rem_pos + 30)],
                fixable=False
            ))

    return issues


# ----------------------------------------------------------------------
# Rule 6: Verb Triad & Mechanics Layering
# ----------------------------------------------------------------------

def check_verb_triad(text: str, filepath: str = "", json_path: str = "") -> List[Issue]:
    """
    Rule 6: Verb Triad & Mechanics Layering (ERROR)
    Enforces:
    - Positive status count -> '获得'
    - Negative status count -> '施加'
    - Potency increase -> '增加'
    - Decay/consumption -> '减少' or '消耗'
    Excludes StoryData narrative dialogues.
    """
    if not text:
        return []

    # Exclude StoryData files
    if filepath.startswith("StoryData") or "/StoryData/" in filepath:
        return []

    issues: List[Issue] = []

    m_pos = RE_POS_ERR.search(text)
    if m_pos:
        issues.append(Issue(
            rule="L06_VERB_TRIAD",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"正面状态层数动词违规: 匹配到 '{m_pos.group(0)}'。正面状态层数必须统一使用动词'获得'",
            snippet=text[max(0, m_pos.start() - 5):min(len(text), m_pos.end() + 10)],
            fixable=False
        ))

    m_neg = RE_NEG_ERR.search(text)
    if m_neg:
        issues.append(Issue(
            rule="L06_VERB_TRIAD",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"负面状态层数动词违规: 匹配到 '{m_neg.group(0)}'。负面状态层数必须统一使用动词'施加'",
            snippet=text[max(0, m_neg.start() - 5):min(len(text), m_neg.end() + 10)],
            fixable=False
        ))

    m_pot1 = RE_POT_ERR_POST.search(text)
    m_pot2 = RE_POT_ERR_PRE.search(text)
    m_pot = m_pot1 or m_pot2
    if m_pot:
        issues.append(Issue(
            rule="L06_VERB_TRIAD",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"状态强度上升动词违规: 匹配到 '{m_pot.group(0)}'。状态强度上升一律统一使用动词'增加'",
            snippet=text[max(0, m_pot.start() - 5):min(len(text), m_pot.end() + 10)],
            fixable=False
        ))

    m_dec1 = RE_DECAY_ERR_1.search(text)
    m_dec2 = RE_DECAY_ERR_2.search(text)
    m_dec = m_dec1 or m_dec2
    if m_dec:
        issues.append(Issue(
            rule="L06_VERB_TRIAD",
            severity=Severity.ERROR,
            filepath=filepath,
            json_path=json_path,
            message=f"状态衰减动词违规: 匹配到 '{m_dec.group(0)}'。状态数值减少统一使用动词'减少'或'消耗'",
            snippet=text[max(0, m_dec.start() - 5):min(len(text), m_dec.end() + 10)],
            fixable=False
        ))

    return issues


# ----------------------------------------------------------------------
# Rule 7: Punctuation & Typography
# ----------------------------------------------------------------------

def check_typography(text: str, filepath: str = "", json_path: str = "") -> List[Issue]:
    """
    Rule 7: Punctuation & Typography (WARN)
    - Ellipsis: standard Chinese 6-dot ellipsis '……'
    - Quotes: standard full-width quotes '“”' / '‘’' (after stripping TMP tags)
    - Em-dash: standard '——'
    - Whitelist: Chapter 5.5 Morse code skill names (Skills_Enemy-a1c5p2)
    """
    if not text:
        return []

    # Whitelist Morse code file
    if "Skills_Enemy-a1c5p2" in filepath:
        return []

    issues: List[Issue] = []
    is_story = filepath.startswith("StoryData") or "/StoryData/" in filepath

    # 1. ASCII ellipsis
    m_dots = RE_ASCII_ELLIPSIS.search(text)
    if m_dots:
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message=f"检测到半角英文连打点号 '{m_dots.group(0)}'。请规范化为中文六点省略号'……'",
            snippet=text[max(0, m_dots.start() - 5):min(len(text), m_dots.end() + 5)],
            fixable=False
        ))

    # 2. Circle ellipsis
    if RE_CIRCLE_ELLIPSIS.search(text):
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message="检测到全角句号连打'。。。'。请规范化为中文六点省略号'……'",
            snippet=text[:40],
            fixable=False
        ))

    # 3. Isolated single 3-dot ellipsis in StoryData
    if is_story and RE_SINGLE_ELLIPSIS.search(text):
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message="剧情文本中检测到单三点省略号'…'。主线剧情叙事必须使用标准六点省略号'……'",
            snippet=text[:40],
            fixable=False
        ))

    # 4. Full-width minus
    if RE_FULLWIDTH_MINUS.search(text):
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message="检测到全角减号'－'。破折号必须使用标准两字宽'——'",
            snippet=text[:40],
            fixable=False
        ))

    # 5. Double hyphen
    m_dh = RE_DOUBLE_HYPHEN.search(text)
    if m_dh:
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message="检测到半角双横杠'--'。破折号必须使用标准两字宽'——'",
            snippet=text[max(0, m_dh.start() - 5):min(len(text), m_dh.end() + 5)],
            fixable=False
        ))

    # 6. Straight quotes outside TMP tags
    stripped_text = TMP_TAG_STRIP.sub('', text)
    if '"' in stripped_text:
        issues.append(Issue(
            rule="L07_TYPOGRAPHY",
            severity=Severity.WARN,
            filepath=filepath,
            json_path=json_path,
            message="检测到残留的英文半角双引号 '\"'。对话与强调必须使用全角双引号'“”'",
            snippet=stripped_text[:40],
            fixable=False
        ))

    return issues


# ----------------------------------------------------------------------
# Rule 8: Korean Residue Detection
# ----------------------------------------------------------------------

def has_hangul(text: str) -> bool:
    """Check if text contains any Hangul characters."""
    return bool(HANGUL_RE.search(text))


def is_whitelisted_korean_content(text: str) -> bool:
    """Whitelists developer comments and audio sound tags."""
    s = text.strip()
    return s.startswith('//') or s.startswith('SE //')


def check_korean_residue(
    text: str,
    filepath: str = "",
    key_name: str = "",
    json_path: str = "",
    enabled: bool = True
) -> List[Issue]:
    """
    Rule 8: Korean Residue Detection (FATAL / ERROR)
    Scans for untranslated Korean characters with strict key whitelists:
    - 'model' key is 100% whitelisted (asset prefab identifiers, prevents crashes)
    - 'id' in ScenarioModelCodes-AutoCreated.json is whitelisted
    - '//' and 'SE //' developer comments are whitelisted
    """
    if not enabled or not isinstance(text, str) or not text:
        return []

    if key_name in KOREAN_WHITELISTED_KEYS:
        return []

    base_name = os.path.basename(filepath)
    if base_name in KOREAN_FILE_KEY_WHITELIST and key_name in KOREAN_FILE_KEY_WHITELIST[base_name]:
        return []

    if HANGUL_RE.search(text):
        if is_whitelisted_korean_content(text):
            return []

        hangul_chars = HANGUL_RE.findall(text)
        snippet = text.replace('\n', ' ')
        if len(snippet) > 40:
            snippet = snippet[:40] + "..."

        is_season8 = any(s in filepath for s in ['a1c10p1', 'S10', 'RPGSystem', '10616', '10816', '10416'])
        severity = Severity.FATAL if is_season8 else Severity.ERROR

        return [Issue(
            rule="L08_KOREAN_RESIDUE",
            severity=severity,
            filepath=filepath,
            json_path=json_path,
            message=f"检测到未汉化韩文残留 ({len(hangul_chars)} 个韩文字符): '{snippet}'",
            snippet=snippet,
            fixable=False
        )]

    return []


# ----------------------------------------------------------------------
# Baseline Korean Resource Resolution
# ----------------------------------------------------------------------

def build_korean_baseline_index(source_dir: Optional[str]) -> Dict[str, str]:
    """
    Builds a normalized relative path lookup to absolute paths in Korean source.
    Strips 'KR_' prefix to align with Chinese workspace assets.
    """
    index: Dict[str, str] = {}
    if not source_dir or not os.path.exists(source_dir):
        return index

    for root, _, files in os.walk(source_dir):
        for fname in files:
            if not fname.endswith(".json"):
                continue
            abs_path = os.path.join(root, fname)
            rel_path = os.path.relpath(abs_path, source_dir)
            index[rel_path] = abs_path
            dirname, basename = os.path.split(rel_path)
            if basename.startswith("KR_"):
                normalized_rel = os.path.join(dirname, basename[3:])
                index[normalized_rel] = abs_path
    return index


# ----------------------------------------------------------------------
# In-Place Auto-Fix Helpers
# ----------------------------------------------------------------------

def fix_json_strings_in_place(node: Any) -> int:
    """Recursively applies safe auto-fixes (Rule 4 keyword trailing spaces) to JSON strings."""
    changes = 0
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str):
                new_v, c = fix_keyword_trailing_space(v)
                if c > 0:
                    node[k] = new_v
                    changes += c
            elif isinstance(v, (dict, list)):
                changes += fix_json_strings_in_place(v)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            if isinstance(item, str):
                new_item, c = fix_keyword_trailing_space(item)
                if c > 0:
                    node[i] = new_item
                    changes += c
            elif isinstance(item, (dict, list)):
                changes += fix_json_strings_in_place(item)
    return changes


# ----------------------------------------------------------------------
# Single File Linter Worker Task
# ----------------------------------------------------------------------

def lint_single_file(
    abs_path: str,
    rel_path: str,
    enabled_rule_ids: Set[str],
    fix: bool,
    kr_abs_path: Optional[str],
    keyword_names: frozenset[str],
) -> Tuple[List[Issue], bool]:
    """
    Lints a single JSON file against enabled rules.
    If fix is True, writes unambiguous auto-repairs to disk.
    Returns (issues, was_fixed).
    """
    issues: List[Issue] = []
    was_fixed = False

    try:
        with open(abs_path, "r", encoding="utf-8-sig") as f:
            raw_content = f.read()
    except Exception as e:
        issues.append(Issue(
            rule="L01_JSON_INTEGRITY",
            severity=Severity.FATAL,
            filepath=rel_path,
            json_path="root",
            message=f"文件读取失败 (UTF-8/BOM 解码异常): {e}",
            fixable=False
        ))
        return issues, False

    # Apply auto-fix if requested
    if fix:
        fixed_content, tilde_count = fix_fullwidth_tilde(raw_content)
        if tilde_count > 0:
            was_fixed = True
            raw_content = fixed_content

    # Rule 2: Full-width tilde scan
    if "L02" in enabled_rule_ids:
        # Fast check: skip line scan if no tildes
        if has_fullwidth_tilde(raw_content):
            tilde_issues = check_fullwidth_tilde(raw_content, rel_path)
            issues.extend(tilde_issues)

    # Rule 1: JSON Syntax & Structure
    data, r1_issues = check_json_syntax(raw_content, rel_path)
    if "L01" in enabled_rule_ids:
        issues.extend(r1_issues)

    if data is None:
        if fix and was_fixed:
            with open(abs_path, "w", encoding="utf-8") as f:
                f.write(raw_content)
        return issues, was_fixed

    # Apply in-place keyword space auto-fix if requested
    if fix:
        kw_changes = fix_json_strings_in_place(data)
        if kw_changes > 0 or was_fixed:
            was_fixed = True
            # Write back updated content
            if kw_changes > 0:
                with open(abs_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    f.write("\n")
            else:
                with open(abs_path, "w", encoding="utf-8") as f:
                    f.write(raw_content)

    # Load KR baseline strings if available
    kr_entries: Optional[Dict[str, str]] = None
    if kr_abs_path:
        try:
            with open(kr_abs_path, "r", encoding="utf-8-sig") as kf:
                kr_content = kf.read()
            if kr_content.startswith('\ufeff'):
                kr_content = kr_content[1:]
            kr_data = json.loads(kr_content)
            kr_entries = {p: s for p, s, _ in traverse_json_strings(kr_data)}
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            issues.append(Issue(
                rule="L01_SOURCE_INTEGRITY", severity=Severity.FATAL,
                filepath=rel_path, json_path="root",
                message=f"无法读取原文，无法执行对照校验: {kr_abs_path}: {error}",
            ))
            return issues, was_fixed

    # Pre-flight substring checks for performance
    has_braces = "{" in raw_content or "}" in raw_content
    has_tags = "<" in raw_content
    has_hangul_chars = HANGUL_RE.search(raw_content) is not None if "L08" in enabled_rule_ids else False

    # Traverse JSON string values
    for json_path, text, ctx in traverse_json_strings(data):
        item_id = str(ctx.get("id", ctx.get("key", "")))
        key_name = ctx.get("_key_name", "")
        kr_text = kr_entries.get(json_path) if kr_entries else None
        if metadata_reason(rel_path, key_name, kr_text if kr_text is not None else text):
            continue
        is_narrative = rel_path.startswith(('StoryData/', 'RPGSystem/rpg-loc-dialogue'))
        is_description = key_name in {'desc', 'description', 'summary', 'statText', 'lowMoraleDescription', 'panicDescription'}

        # Rule 3: Placeholders
        if "L03" in enabled_rule_ids and has_braces:
            issues.extend(check_placeholders(text, kr_text, rel_path, item_id, json_path))

        # Rule 4: Keyword Trailing Space
        if "L04" in enabled_rule_ids and is_description and not is_narrative and not has_hangul_chars:
            issues.extend(check_known_keyword_spaces(text, rel_path, json_path, keyword_names))

        # Rule 5: Unity TMP Tags
        if "L05" in enabled_rule_ids and has_tags:
            issues.extend(check_tmp_tags(text, rel_path, json_path))

        # Rule 6: Verb Triad
        if "L06" in enabled_rule_ids and is_description and not is_narrative:
            issues.extend(check_verb_triad(text, rel_path, json_path))

        # Rule 7: Typography
        if "L07" in enabled_rule_ids:
            issues.extend(check_typography(text, rel_path, json_path))

        # Rule 8: Korean Residue
        if "L08" in enabled_rule_ids and has_hangul_chars:
            issues.extend(check_korean_residue(text, rel_path, key_name, json_path, enabled=True))

    return issues, was_fixed


# Multiprocessing pickle wrapper
def _mp_worker_task(args: Tuple[str, str, Set[str], bool, Optional[str], frozenset[str]]) -> Tuple[List[Issue], bool]:
    return lint_single_file(*args)


# ----------------------------------------------------------------------
# Linter Engine
# ----------------------------------------------------------------------

class Linter:
    """Linter Engine orchestrating multi-file static analysis and reporting."""

    def __init__(self, config: LintConfig):
        self.config = config
        self.enabled_rule_ids = config.get_enabled_rule_ids()

        # Resolve source directory
        self.source_dir = resolve_source_directory(config.source_dir, Path(__file__).resolve().parents[1])

        self.kr_index: Dict[str, str] = {}
        if self.source_dir and os.path.exists(self.source_dir):
            self.kr_index = build_korean_baseline_index(self.source_dir)

    def collect_target_files(self) -> List[Tuple[str, str, Optional[str]]]:
        """
        Collects all JSON files to scan as tuples of (abs_path, rel_path, kr_abs_path).
        """
        target_path = Path(self.config.target).resolve()
        workspace_root = Path(DEFAULT_WORKSPACE_DIR).resolve()
        files: List[Tuple[str, str, Optional[str]]] = []

        if target_path.is_file():
            rel_name = str(target_path.relative_to(workspace_root)) if target_path.is_relative_to(workspace_root) else target_path.name
            kr_abs = self.kr_index.get(rel_name)
            files.append((str(target_path), rel_name, kr_abs))
        elif target_path.is_dir():
            for root, _, fnames in os.walk(str(target_path)):
                for fname in fnames:
                    if not fname.endswith(".json"):
                        continue
                    abs_p = os.path.join(root, fname)
                    rel_p = str(Path(abs_p).relative_to(workspace_root)) if Path(abs_p).is_relative_to(workspace_root) else os.path.relpath(abs_p, str(target_path))
                    kr_abs = self.kr_index.get(rel_p)
                    files.append((abs_p, rel_p, kr_abs))
        else:
            raise FileNotFoundError(f"待检查路径不存在: {target_path}")
        return sorted(files, key=lambda x: x[1])

    def run(self) -> LintReport:
        """Executes linting across all collected target files."""
        start_time = time.time()
        file_targets = self.collect_target_files()

        report = LintReport()
        report.total_scanned_files = len(file_targets)

        if not file_targets:
            raise ValueError(f"待检查目录中没有 JSON 资源: {self.config.target}")

        # Determine concurrency
        workers = self.config.workers
        if workers == 0:
            workers = min(os.cpu_count() or 4, 8) if len(file_targets) >= 100 else 1

        all_issues: List[Issue] = []
        total_fixed = 0

        keyword_names = (
            load_keyword_names(keyword_directory(Path(self.config.target), Path(DEFAULT_WORKSPACE_DIR)))
            if "L04" in self.enabled_rule_ids else frozenset()
        )
        tasks = [
            (abs_p, rel_p, self.enabled_rule_ids, self.config.fix, kr_abs, keyword_names)
            for abs_p, rel_p, kr_abs in file_targets
        ]

        if workers > 1 and len(tasks) >= 2:
            chunk_size = max(1, len(tasks) // (workers * 4))
            with multiprocessing.Pool(processes=workers) as pool:
                results = pool.map(_mp_worker_task, tasks, chunksize=chunk_size)
            for issues, fixed in results:
                all_issues.extend(issues)
                if fixed:
                    total_fixed += 1
        else:
            for task in tasks:
                issues, fixed = lint_single_file(*task)
                all_issues.extend(issues)
                if fixed:
                    total_fixed += 1

        report.issues = all_issues
        report.total_fixed_files = total_fixed
        report.execution_time_seconds = time.time() - start_time

        # Count severities
        for issue in all_issues:
            if issue.severity == Severity.FATAL:
                report.fatal_count += 1
            elif issue.severity == Severity.ERROR:
                report.error_count += 1
            elif issue.severity == Severity.WARN:
                report.warn_count += 1
            elif issue.severity == Severity.INFO:
                report.info_count += 1

        # Determine exit code
        if report.fatal_count > 0 or report.error_count > 0:
            report.passed = False
            report.exit_code = 1
        elif self.config.strict and report.warn_count > 0:
            report.passed = False
            report.exit_code = 1
        else:
            report.passed = True
            report.exit_code = 0

        # Export JSON report if requested
        if self.config.json_report:
            out_p = Path(self.config.json_report)
            out_p.parent.mkdir(parents=True, exist_ok=True)
            with open(out_p, "w", encoding="utf-8") as f:
                json.dump(report.to_dict(), f, ensure_ascii=False, indent=2)

        return report

    def print_summary(self, report: LintReport) -> None:
        """Prints high-visibility ASCII summary table to stdout."""
        use_color = not self.config.no_color and sys.stdout.isatty()

        c_reset = COLOR_RESET if use_color else ""
        c_red = COLOR_RED if use_color else ""
        c_green = COLOR_GREEN if use_color else ""
        c_yellow = COLOR_YELLOW if use_color else ""
        c_cyan = COLOR_CYAN if use_color else ""
        c_bold = COLOR_BOLD if use_color else ""

        if not self.config.quiet and report.issues:
            print("=" * 80)
            print(f"{c_bold}【都市零协会】自动化静态质检与代码安全扫描引擎 (LLC Linter Engine v2.0){c_reset}")
            for issue in report.issues:
                sev_color = c_red if issue.severity in (Severity.FATAL, Severity.ERROR) else c_yellow
                coord = f":{issue.line}" if issue.line else ""
                loc = f"{issue.filepath}{coord}"
                path_info = f" [{issue.json_path}]" if issue.json_path else ""
                sev_str = issue.severity.value if hasattr(issue.severity, "value") else str(issue.severity)
                print(f"{sev_color}[{sev_str}]{c_reset} {loc}{path_info} ({issue.rule})")
                print(f"  --> {issue.message}")
                if issue.snippet:
                    print(f"  代码: \"{issue.snippet}\"")
            print("-" * 80)

        status_str = f"{c_green}[PASSED]{c_reset}" if report.passed else f"{c_red}[FAILED]{c_reset}"
        fatal_status = f"{c_red}[FAILED]{c_reset}" if report.fatal_count > 0 else f"{c_green}[PASSED]{c_reset}"
        error_status = f"{c_red}[FAILED]{c_reset}" if report.error_count > 0 else f"{c_green}[PASSED]{c_reset}"
        warn_status = f"{c_yellow}[WARNING]{c_reset}" if report.warn_count > 0 else f"{c_green}[PASSED]{c_reset}"

        print("┌" + "─" * 78 + "┐")
        print(f"│{c_bold}                         LLC 静态质检结果统览大表                             {c_reset}│")
        print("├" + "─" * 13 + "┬" + "─" * 14 + "┬" + "─" * 14 + "┬" + "─" * 34 + "┤")
        print("│ 严重级别    │ 违规数量     │ 准入裁定     │ 影响范畴                         │")
        print("├" + "─" * 13 + "┼" + "─" * 14 + "┼" + "─" * 14 + "┼" + "─" * 34 + "┤")
        print(f"│ FATAL       │ {report.fatal_count:>12} │ {fatal_status}     │ 编码/语法/富文本/残留文本         │")
        print(f"│ ERROR       │ {report.error_count:>12} │ {error_status}     │ 占位符/关键词格式/动词约定        │")
        print(f"│ WARN        │ {report.warn_count:>12} │ {warn_status}    │ 排版规范/标点格式/人设口吻       │")
        print(f"│ INFO        │ {report.info_count:>12} │ {c_green}[PASSED]{c_reset}     │ 优化建议与提示                   │")
        print("├" + "─" * 78 + "┤")
        print(f"│ 资产扫描总数: {report.total_scanned_files} 文件 | 扫描耗时: {report.execution_time_seconds:.3f} 秒" + " " * max(0, 42 - len(str(report.total_scanned_files))) + "│")
        print(f"│ 自动修复文件: {report.total_fixed_files} 文件" + (" (已自动安全修复)" if self.config.fix else " (只读模式已生效)") + " " * 44 + "│")
        if report.passed:
            print(f"│ 静态规则检查通过；译文准确性及实机显示仍需独立验收。{c_reset}    │")
        else:
            print(f"│ 最终交付判定: {c_red}❌ 质检未通过 (检测到 {report.fatal_count} 致命错误, {report.error_count} 严重违规){c_reset}          │")
        print("└" + "─" * 78 + "┘")


# ----------------------------------------------------------------------
# CLI Entrypoint & Parser
# ----------------------------------------------------------------------

def build_cli_parser() -> argparse.ArgumentParser:
    """Constructs the complete CLI argument parser for tools/linter.py."""
    parser = argparse.ArgumentParser(
        prog="linter.py",
        description="都市零协会（LLC）自动化静态质检与代码安全工具 (Season 8 / a1c10p1)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
范例:
  # 1. 默认只读检查工作区全量文件
  python3 tools/linter.py

  # 2. 检查特定文件
  python3 tools/linter.py --target workspace/LLC_zh-CN/MainUIText-a1c10p1.json

  # 3. 启用安全自动修复并生成 JSON 质检报告
  python3 tools/linter.py --fix --json-report artifacts/lint_report.json

  # 4. 严苛发布门禁检查（包含韩文残留与风格警告）
  python3 tools/linter.py --strict --check-korean
"""
    )

    parser.add_argument(
        "--target",
        type=str,
        default=DEFAULT_WORKSPACE_DIR,
        help="待检测目标文件或目录路径 (默认: workspace/LLC_zh-CN)"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        default=False,
        help="启用安全自动修复模式 (默认关闭，纯只读扫描)"
    )
    parser.add_argument(
        "--check-korean",
        action="store_true",
        default=False,
        help="启用韩文未汉化残留严格检测 (L08)"
    )
    parser.add_argument(
        "--json-report",
        type=str,
        default=None,
        metavar="PATH",
        help="导出结构化 JSON 报告到指定路径"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help="严苛门禁模式: 任意 WARNING 警告均导致非零退出码 (退出码 1)"
    )
    parser.add_argument(
        "--source-dir",
        type=str,
        default=None,
        metavar="PATH",
        help="原版韩文基准资源目录路径 (用于 L03 占位符 1:1 比对)"
    )
    parser.add_argument(
        "--rules",
        type=str,
        default=None,
        help="按逗号过滤执行的规则 ID (例: L01,L02,L03,L04)"
    )
    parser.add_argument(
        "-j", "--workers",
        type=int,
        default=0,
        help="并发进程数 (0=自动，1=单进程，>1=多进程)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        default=False,
        help="静默模式: 隐藏单条违规明细，仅打印统计摘要大表"
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="禁用 ANSI 彩色终端输出"
    )

    return parser


# ----------------------------------------------------------------------
# Legacy Compatibility Wrappers
# ----------------------------------------------------------------------

def lint_file(filepath: str) -> Tuple[List[str], List[str]]:
    """Legacy compatibility wrapper returning (errors, warnings)."""
    config = LintConfig(target=filepath, fix=False)
    linter = Linter(config)
    report = linter.run()
    errors = [
        f"{i.json_path or i.line or ''}: {i.message}"
        for i in report.issues if i.severity in (Severity.FATAL, Severity.ERROR)
    ]
    warnings = [
        f"{i.json_path or i.line or ''}: {i.message}"
        for i in report.issues if i.severity == Severity.WARN
    ]
    return errors, warnings


def run_linter(auto_fix: bool = False) -> int:
    """Legacy compatibility wrapper."""
    config = LintConfig(fix=auto_fix)
    linter = Linter(config)
    report = linter.run()
    linter.print_summary(report)
    return report.exit_code


def main() -> int:
    parser = build_cli_parser()
    args = parser.parse_args()

    config = LintConfig(
        target=args.target,
        fix=args.fix,
        check_korean=args.check_korean,
        json_report=args.json_report,
        strict=args.strict,
        source_dir=args.source_dir,
        rules=args.rules,
        workers=args.workers,
        quiet=args.quiet,
        no_color=args.no_color,
    )

    linter = Linter(config)
    report = linter.run()
    linter.print_summary(report)
    return report.exit_code


if __name__ == "__main__":
    sys.exit(main())
