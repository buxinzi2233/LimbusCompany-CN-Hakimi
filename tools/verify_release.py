#!/usr/bin/env python3
"""Verify the full package and distinguish untouched legacy findings from regressions.

Every JSON is parsed and scanned. A legacy finding is excluded from the delta
release gate only when its exact Chinese field AND its source field are unchanged
from the frozen baseline. Structural JSON/encoding and forbidden-tilde errors are
never excluded. Raw inherited findings remain in the report. This gate does not
claim that translation quality or in-game rendering has been verified.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import TypedDict, cast

if __package__:
    from .diff_extractor import audit, Json
    from .linter import Linter, LintConfig, traverse_json_strings
else:
    from diff_extractor import audit, Json
    from linter import Linter, LintConfig, traverse_json_strings


class Finding(TypedDict):
    file: str
    path: str
    rule: str
    severity: str
    message: str


class Verification(TypedDict):
    passed: bool
    gate_scope: str
    runtime_verified: bool
    summary: dict[str, int]
    workspace_sha256: dict[str, str]
    source_sha256: dict[str, str]
    introduced_findings: list[Finding]
    inherited_findings: list[Finding]
    coverage_problems: list[dict[str, Json]]


def hashes(root: Path) -> dict[str, str]:
    if not root.is_dir():
        raise NotADirectoryError(f'Cannot hash missing directory: {root}')
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}


def string_fields(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    value = json.loads(path.read_text(encoding='utf-8-sig'))
    return {p: s for p, s, _ in traverse_json_strings(value)}


def source_path(root: Path, relative: str) -> Path:
    plain = root / relative
    prefixed = plain.with_name('KR_' + plain.name)
    matches = [p for p in (plain, prefixed) if p.is_file()]
    if len(matches) > 1:
        raise ValueError(f'Ambiguous source files for {relative}: {matches}')
    return matches[0] if matches else plain


def verify(workspace: Path, source: Path, baseline_kr: Path, baseline_zh: Path) -> Verification:
    before = hashes(workspace)
    original = hashes(source)
    coverage = audit(source, baseline_kr, workspace)
    scan = Linter(LintConfig(target=str(workspace), fix=False, check_korean=True,
                            json_report=None, strict=True, source_dir=str(source),
                            rules=None, workers=1, quiet=True, no_color=True)).run()
    introduced: list[Finding] = []
    inherited: list[Finding] = []
    for file in coverage['files']:
        if file['missing_file']:
            introduced.append({'file': file['path'], 'path': '', 'rule': 'SOURCE_FILE_MISSING',
                               'severity': 'FATAL', 'message': 'A new or changed source resource is missing.'})
    for old_file in sorted(baseline_zh.rglob('*.json')):
        relative = str(old_file.relative_to(baseline_zh))
        target = workspace / relative
        if not target.is_file():
            introduced.append({'file': relative, 'path': '', 'rule': 'BASELINE_FILE_MISSING',
                               'severity': 'FATAL', 'message': 'An existing baseline resource was removed.'})
            continue
        original_fields = string_fields(old_file)
        current_fields = string_fields(target)
        old_source = string_fields(baseline_kr / relative)
        current_source = string_fields(source_path(source, relative))
        for path in original_fields.keys() - current_fields.keys():
            if path in old_source and path not in current_source:
                continue
            introduced.append({'file': relative, 'path': path, 'rule': 'BASELINE_FIELD_MISSING',
                               'severity': 'FATAL', 'message': 'An existing field was removed without a source removal.'})
    cache: dict[str, tuple[dict[str, str], dict[str, str], dict[str, str], dict[str, str]]] = {}
    for issue in scan.issues:
        relative = issue.filepath
        if relative not in cache:
            cache[relative] = (string_fields(workspace / relative), string_fields(baseline_zh / relative),
                               string_fields(source_path(source, relative)), string_fields(baseline_kr / relative))
        current_zh, old_zh, current_kr, old_kr = cache[relative]
        path = issue.json_path or ''
        legacy = (not issue.rule.startswith(('L01', 'L02')) and path in current_zh and path in old_zh
                  and current_zh[path] == old_zh[path] and current_kr.get(path) == old_kr.get(path))
        finding: Finding = {'file': relative, 'path': path, 'rule': issue.rule,
                            'severity': issue.severity.value, 'message': issue.message}
        (inherited if legacy else introduced).append(finding)
    problems = [cast(dict[str, Json], {'file': f['path'], **c})
                for f in coverage['files'] for c in f['changes'] if c['problems']]
    stable = before == hashes(workspace) and original == hashes(source)
    if not stable:
        introduced.append({'file': str(workspace), 'path': '', 'rule': 'CONCURRENT_WRITE', 'severity': 'FATAL',
                           'message': 'Resources changed during verification; rerun after all writers finish.'})
    blockers = [f for f in introduced if f['severity'] in {'FATAL', 'ERROR', 'WARN'}]
    return {'passed': not blockers and not problems,
            'gate_scope': 'Current source delta and modified target fields; inherited findings remain unresolved.',
            'runtime_verified': False,
            'summary': {'scanned_files': scan.total_scanned_files, 'delta_files': coverage['summary']['delta_files'],
                        'introduced_blockers': len(blockers), 'inherited_findings': len(inherited),
                        'coverage_problems': len(problems),
                        **{f'introduced_{k}': v for k, v in Counter(f['rule'] for f in introduced).items()}},
            'workspace_sha256': before, 'source_sha256': original,
            'introduced_findings': introduced, 'inherited_findings': inherited, 'coverage_problems': problems}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--baseline-kr', type=Path, required=True)
    parser.add_argument('--baseline-zh', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.workspace.resolve(), args.source.resolve(), args.baseline_kr.resolve(), args.baseline_zh.resolve())
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result['summary'], ensure_ascii=False, indent=2))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
