# -*- coding: utf-8 -*-
"""
Common utilities and constants for Limbus Company Season 8 E2E tests.
"""

import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any, Dict, List, Set, Tuple

# Path Constants
PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_DIR = PROJECT_ROOT / "workspace" / "LLC_zh-CN"
TOOLS_DIR = PROJECT_ROOT / "tools"

STEAM_GAME_DIR = Path("/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company")
STEAM_DATA_DIR = STEAM_GAME_DIR / "LimbusCompany_Data"
STEAM_LANG_DIR = STEAM_DATA_DIR / "Lang" / "LLC_zh-CN"
STEAM_CONFIG_FILE = STEAM_DATA_DIR / "Lang" / "config.json"
KR_BASE_DIR = STEAM_DATA_DIR / "Assets" / "Resources_moved" / "Localize" / "kr"

# Font Specifications
EXPECTED_FONT_SIZE = 23870096
EXPECTED_FONT_SHA256 = "a56a06f1af27726bc5def015b61deecbbdf5ae6d954a91b1131d8a17290def35"
FONT_REL_PATH = Path("Font") / "Context" / "ChineseFont.ttf"

# Regular Expressions
HANGUL_REGEX = re.compile(r'[\uac00-\ud7a3]')
FULLWIDTH_TILDE_REGEX = re.compile(r'～')
PLACEHOLDER_REGEX = re.compile(r'\{([0-9a-zA-Z_]+)\}')
TMP_TAG_REGEX = re.compile(r'<(/?[a-zA-Z0-9]+)(?:=[^>]+)?>')

# Core Battle Keywords requiring trailing space
CORE_KEYWORDS = ["震颤", "流血", "呼吸法", "充能", "沉沦", "破裂", "烧伤"]


def load_json(filepath: Path) -> Any:
    """Load JSON from a file with strict UTF-8 decoding."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def collect_all_strings(obj: Any) -> List[str]:
    """Recursively collect all string values from a nested JSON data structure."""
    strings = []
    if isinstance(obj, str):
        strings.append(obj)
    elif isinstance(obj, dict):
        for val in obj.values():
            strings.extend(collect_all_strings(val))
    elif isinstance(obj, list):
        for item in obj:
            strings.extend(collect_all_strings(item))
    return strings


def has_hangul(text: str) -> bool:
    """Check if a string contains any Korean Hangul syllables."""
    return bool(HANGUL_REGEX.search(text))


def find_hangul_instances(text: str) -> List[str]:
    """Find all Hangul character sequences in a string."""
    return HANGUL_REGEX.findall(text)


def has_fullwidth_tilde(text: str) -> bool:
    """Check if a string contains the forbidden full-width tilde '～'."""
    return "～" in text


def extract_placeholders(text: str) -> List[str]:
    """Extract format placeholder variable names (e.g. {0}, {1}, {Slot})."""
    return PLACEHOLDER_REGEX.findall(text)


def validate_tmp_tags(text: str) -> Tuple[bool, str]:
    """
    Validate Unity TextMeshPro tag balance using a LIFO stack.
    Returns (is_valid, error_message).
    """
    stack: List[str] = []
    paired_tags = {"color", "b", "i", "size", "mark", "u"}

    for match in TMP_TAG_REGEX.finditer(text):
        raw_tag = match.group(1).lower()
        if not raw_tag.startswith("/"):
            if raw_tag in paired_tags:
                stack.append(raw_tag)
        else:
            closing_tag = raw_tag[1:]
            if closing_tag in paired_tags:
                if not stack:
                    return False, f"Unmatched closing tag </{closing_tag}> with empty stack"
                last_tag = stack.pop()
                if last_tag != closing_tag:
                    return False, f"Mismatched tag: expected </{last_tag}>, got </{closing_tag}>"

    if stack:
        return False, f"Unclosed tags at end of string: {stack}"
    return True, ""
