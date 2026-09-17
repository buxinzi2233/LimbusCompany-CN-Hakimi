#!/usr/bin/env python3
"""Audit every source resource against the frozen KR baseline and Chinese output.

Stable selectors preserve id/key/level/index identity in nested arrays. Reports
retain missing fields, untranslated text and source changes requiring review.
The audit never modifies localization resources.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from typing import Iterator, TypedDict, cast
if __package__:
    from .resource_fields import IDENTITY_FIELDS, metadata_reason
else:
    from resource_fields import IDENTITY_FIELDS, metadata_reason

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GAME_KR_DIR = Path('/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr')
ZH_DIR = PROJECT_ROOT / 'workspace/LLC_zh-CN'
OUTPUT_DIFF = PROJECT_ROOT / 'tools/diff_new_season.json'
type Json = str | int | float | bool | None | list[Json] | dict[str, Json]
type Scalar = str | int | float | bool | None
HANGUL_REGEX = re.compile(r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]')
PLACEHOLDERS = re.compile(r'(?<!\{)\{([A-Za-z0-9_:]+)\}(?!\})')
KEYWORD_REFERENCES = re.compile(r'\[([A-Za-z][A-Za-z0-9_]*)\]')


class FieldChange(TypedDict):
    path: str
    field: str
    source: Scalar
    translation: Scalar
    previous_source: Scalar
    problems: list[str]


class FileChange(TypedDict):
    path: str
    source_path: str
    new_source_file: bool
    missing_file: bool
    changes: list[FieldChange]


class AuditReport(TypedDict):
    source_dir: str
    baseline_dir: str
    target_dir: str
    summary: dict[str, int]
    files: list[FileChange]


def read_resource(path: Path) -> dict[str, Json]:
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict) or (data and not isinstance(data.get('dataList'), list)):
        raise ValueError(f'Expected object with dataList array: {path}')
    return cast(dict[str, Json], data)


def leaves(node: Json, path: str, field: str) -> Iterator[tuple[str, str, Scalar]]:
    if isinstance(node, dict):
        for key, value in node.items():
            yield from leaves(value, f'{path}.{key}' if path else key, key)
    elif isinstance(node, list):
        selectors: set[str] = set()
        for index, value in enumerate(node):
            selector = str(index)
            if isinstance(value, dict):
                for key in ('id', 'key', 'level', 'index'):
                    if key in value:
                        selector = f'{key}={value[key]}'
                        break
            if selector in selectors:
                raise ValueError(f'Duplicate array identity at {path}[{selector}]')
            selectors.add(selector)
            yield from leaves(value, f'{path}[{selector}]', field)
    else:
        yield path, field, node


def normalized_path(path: Path, root: Path) -> Path:
    relative = path.relative_to(root)
    return relative.with_name(relative.name.removeprefix('KR_'))


def compare_file(source: Path, baseline: Path, target: Path, relative: Path) -> FileChange:
    current = list(leaves(read_resource(source), '', ''))
    previous = {p: v for p, _, v in leaves(read_resource(baseline), '', '')} if baseline.is_file() else {}
    translated = {p: v for p, _, v in leaves(read_resource(target), '', '')} if target.is_file() else {}
    changes: list[FieldChange] = []
    for path, field, value in current:
        changed = path not in previous or previous[path] != value
        zh = translated.get(path)
        intact = (path in translated and type(zh) is type(value)
                  and (isinstance(value, str) and field not in IDENTITY_FIELDS or zh == value))
        if not changed and intact:
            continue
        problems: list[str] = []
        if path not in translated:
            problems.append('missing_field')
        elif field in IDENTITY_FIELDS:
            if zh != value:
                problems.append('modified_identity')
        elif isinstance(value, str):
            if not isinstance(zh, str):
                problems.append('wrong_type')
            else:
                if value.strip() and not zh.strip():
                    problems.append('empty_translation')
                if HANGUL_REGEX.search(zh) and not metadata_reason(str(relative), field, value):
                    problems.append('korean_text')
                if Counter(PLACEHOLDERS.findall(value)) != Counter(PLACEHOLDERS.findall(zh)):
                    problems.append('placeholder_mismatch')
                if set(KEYWORD_REFERENCES.findall(value)) - set(KEYWORD_REFERENCES.findall(zh)):
                    problems.append('missing_keyword_reference')
        elif type(zh) is not type(value) or zh != value:
            problems.append('modified_structure')
        changes.append({'path': path, 'field': field, 'source': value,
                        'translation': zh, 'previous_source': previous.get(path), 'problems': problems})
    if not baseline.is_file():
        source_paths = {p for p, _, _ in current}
        for path in sorted(translated.keys() - source_paths):
            changes.append({'path': path, 'field': path.rsplit('.', 1)[-1], 'source': None,
                            'translation': translated[path], 'previous_source': None,
                            'problems': ['unexpected_field']})
    return {'path': str(relative), 'source_path': str(source),
            'new_source_file': not baseline.is_file(), 'missing_file': not target.is_file(), 'changes': changes}


def audit(source_dir: Path, baseline_dir: Path, target_dir: Path) -> AuditReport:
    for directory in (source_dir, baseline_dir, target_dir):
        if not directory.is_dir():
            raise FileNotFoundError(f'Resource directory does not exist: {directory}')
    files: list[FileChange] = []
    scanned = 0
    for source in sorted(source_dir.rglob('*.json')):
        scanned += 1
        relative = normalized_path(source, source_dir)
        baseline = baseline_dir / relative
        if baseline.is_file() and read_resource(source) == read_resource(baseline):
            continue
        result = compare_file(source, baseline_dir / relative, target_dir / relative, relative)
        if result['changes'] or result['new_source_file']:
            files.append(result)
    problems = Counter(p for f in files for c in f['changes'] for p in c['problems'])
    return {'source_dir': str(source_dir), 'baseline_dir': str(baseline_dir), 'target_dir': str(target_dir),
            'summary': {'scanned_files': scanned, 'delta_files': len(files),
                        'new_source_files': sum(f['new_source_file'] for f in files),
                        'missing_files': sum(f['missing_file'] for f in files),
                        'changed_fields': sum(len(f['changes']) for f in files), **dict(problems)}, 'files': files}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=GAME_KR_DIR)
    parser.add_argument('--baseline-dir', type=Path, default=PROJECT_ROOT / 'references/baseline-KR')
    parser.add_argument('--target', type=Path, default=ZH_DIR)
    parser.add_argument('--output', type=Path, default=OUTPUT_DIFF)
    args = parser.parse_args()
    report = audit(args.source_dir, args.baseline_dir, args.target)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report['summary'], ensure_ascii=False, indent=2))
    return int(any(c['problems'] for f in report['files'] for c in f['changes']))


if __name__ == '__main__':
    raise SystemExit(main())
