#!/usr/bin/env python3
"""Deploy only a verified, unchanged localization snapshot with retained backups.

Files are copied and verified in a sibling staging directory before activation.
The previous language directory is retained beside it, and a separate backup
contains the previous assets and language config. Failures raise with their
original cause; a successful file deployment is not an in-game rendering claim.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

if __package__:
    from .verify_release import hashes
else:
    from verify_release import hashes

FONT_SHA256 = 'a56a06f1af27726bc5def015b61deecbbdf5ae6d954a91b1131d8a17290def35'
FONT_RELATIVE = Path('Font/Context/ChineseFont.ttf')


def deploy(workspace: Path, source: Path, lang_dir: Path, report_path: Path, backup: Path) -> dict[str, str]:
    report = json.loads(report_path.read_text(encoding='utf-8'))
    if not isinstance(report, dict) or report.get('passed') is not True:
        raise ValueError(f'Release verification did not pass: {report_path}')
    expected = hashes(workspace)
    if report.get('workspace_sha256') != expected:
        raise ValueError(f'Workspace changed since verification; regenerate {report_path}')
    if report.get('source_sha256') != hashes(source):
        raise ValueError(f'Client source changed since verification; regenerate {report_path}')
    font = workspace / FONT_RELATIVE
    if not font.is_file() or hashlib.sha256(font.read_bytes()).hexdigest() != FONT_SHA256:
        raise ValueError(f'Unexpected or missing Sarasa font: {font}')
    if not lang_dir.is_dir():
        raise NotADirectoryError(f'Game language directory does not exist: {lang_dir}')
    destination = lang_dir / 'LLC_zh-CN'
    if destination.is_symlink():
        raise ValueError(f'Refusing to replace a linked language directory: {destination}')
    config_path = lang_dir / 'config.json'
    config = json.loads(config_path.read_text(encoding='utf-8-sig')) if config_path.exists() else {}
    if not isinstance(config, dict):
        raise ValueError(f'Language config must be an object: {config_path}')
    updated_config = {**config, 'lang': 'LLC_zh-CN'}
    backup.mkdir(parents=True, exist_ok=False)
    if destination.exists():
        shutil.copytree(destination, backup / 'LLC_zh-CN')
        if hashes(destination) != hashes(backup / 'LLC_zh-CN'):
            raise OSError(f'Backup hash mismatch: {backup}')
    if config_path.exists():
        shutil.copy2(config_path, backup / 'config.json')
    staging = Path(tempfile.mkdtemp(prefix='.LLC-verified-', dir=lang_dir.parent))
    shutil.copytree(workspace, staging / 'LLC_zh-CN')
    if hashes(staging / 'LLC_zh-CN') != expected or hashes(workspace) != expected:
        raise OSError(f'Staged copy differs or source was modified; staging retained at {staging}')
    (staging / 'config.json').write_text(json.dumps(updated_config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if report['source_sha256'] != hashes(source):
        raise ValueError(f'Client source changed while staging; regenerate {report_path}; staging retained at {staging}')
    retained = staging / 'previous-LLC_zh-CN'
    if destination.exists():
        os.replace(destination, retained)
    os.replace(staging / 'LLC_zh-CN', destination)
    os.replace(staging / 'config.json', config_path)
    if hashes(destination) != expected:
        raise OSError(f'Deployed hash mismatch: {destination}; backup retained at {backup}')
    if json.loads(config_path.read_text(encoding='utf-8')) != updated_config:
        raise OSError(f'Deployed language config mismatch: {config_path}; backup retained at {backup}')
    receipt = {'destination': str(destination), 'backup': str(backup), 'previous_copy': str(retained),
               'verification_report': str(report_path), 'verified_file_count': str(len(expected)),
               'status': 'files_verified_runtime_not_verified'}
    (backup / 'deployment-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--lang-dir', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--backup', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(deploy(args.workspace.resolve(), args.source.resolve(), args.lang_dir.resolve(),
                           args.report.resolve(), args.backup.resolve()), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
