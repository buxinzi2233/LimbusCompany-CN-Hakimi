#!/usr/bin/env python3
"""Restore source structure without replacing existing Chinese translations.

Only source-delta files are written. Missing translations are filled from the
pinned official release when available, otherwise retained as source text so
the audit reports them explicitly. This is preparation, not translation.
"""

import argparse
import json
from pathlib import Path
from diff_extractor import Json, IDENTITY_FIELDS, HANGUL_REGEX, read_resource, normalized_path


def identity(value: Json, index: int) -> str:
    if isinstance(value, dict):
        for field in ('id', 'key', 'level', 'index'):
            if field in value:
                return f'{field}={value[field]}'
    return str(index)


def reconcile(source: Json, current: Json, official: Json, field: str) -> Json:
    if isinstance(source, dict):
        target = current if isinstance(current, dict) else {}
        reference = official if isinstance(official, dict) else {}
        return {**target, **{k: reconcile(v, target.get(k), reference.get(k), k) for k, v in source.items()}}
    if isinstance(source, list):
        target_list = current if isinstance(current, list) else []
        official_list = official if isinstance(official, list) else []
        target = {identity(v, i): v for i, v in enumerate(target_list)}
        reference = {identity(v, i): v for i, v in enumerate(official_list)}
        source_ids = {identity(v, i) for i, v in enumerate(source)}
        return [reconcile(v, target.get(identity(v, i)), reference.get(identity(v, i)), field)
                for i, v in enumerate(source)] + [v for i, v in enumerate(target_list) if identity(v, i) not in source_ids]
    if field in IDENTITY_FIELDS or not isinstance(source, str):
        return source
    if isinstance(current, str) and not HANGUL_REGEX.search(current) and (current.strip() or not source.strip()):
        return current
    if isinstance(official, str) and not HANGUL_REGEX.search(official) and (official.strip() or not source.strip()):
        return official
    return source if current is None else current


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, required=True)
    parser.add_argument('--baseline-dir', type=Path, required=True)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--official', type=Path, required=True)
    args = parser.parse_args()
    changed: list[str] = []
    for source_path in sorted(args.source_dir.rglob('*.json')):
        relative = normalized_path(source_path, args.source_dir)
        source = read_resource(source_path)
        baseline_path = args.baseline_dir / relative
        if baseline_path.is_file() and source == read_resource(baseline_path):
            continue
        if not source.get('dataList'):
            continue
        current_path = args.target / relative
        official_path = args.official / relative
        current = read_resource(current_path) if current_path.is_file() else None
        official = read_resource(official_path) if official_path.is_file() else None
        merged = reconcile(source, current, official, '')
        if merged != current:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            current_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            changed.append(str(relative))
    print(json.dumps({'restored_files': changed}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
