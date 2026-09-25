"""Filesystem integration checks for pinned and explicitly selected Korean sources."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from tools.source_snapshot import resolve_source_directory


def write_snapshot(root: Path) -> Path:
    """Create an actual snapshot directory and a hash-locked manifest on disk."""
    source = root / 'snapshot'
    source.mkdir()
    resource = source / 'Example.json'
    resource.write_text('{"dataList": []}\n', encoding='utf-8')
    manifest = root / 'source-sha256.tsv'
    manifest.write_text(f'{hashlib.sha256(resource.read_bytes()).hexdigest()}\tExample.json\n',
                        encoding='utf-8')
    references = root / 'references'
    references.mkdir()
    (references / 'source-snapshot.json').write_text(json.dumps({
        'version': 'filesystem-test',
        'source_dir': 'snapshot',
        'sha256_manifest': manifest.name,
        'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
    }), encoding='utf-8')
    return source


class TestSourceSnapshot(unittest.TestCase):
    def test_valid_manifest_resolves_existing_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = write_snapshot(root)
            self.assertEqual(Path(resolve_source_directory(None, root)), source)

    def test_missing_snapshot_fails_without_steam_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = write_snapshot(root)
            (source / 'Example.json').unlink()
            source.rmdir()
            with self.assertRaisesRegex(FileNotFoundError, 'Pinned Korean snapshot.*unavailable'):
                resolve_source_directory(None, root)

    def test_incorrect_manifest_hash_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_snapshot(root)
            (root / 'source-sha256.tsv').write_text('changed manifest\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Source manifest hash mismatch.*expected=.*actual='):
                resolve_source_directory(None, root)

    def test_explicit_source_does_not_require_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'explicit'
            source.mkdir()
            (source / 'Example.json').write_text('{"dataList": []}\n', encoding='utf-8')
            self.assertFalse((root / 'references/source-snapshot.json').exists())
            self.assertEqual(Path(resolve_source_directory(str(source), root)), source)

    def test_missing_explicit_source_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaisesRegex(FileNotFoundError, 'Korean source directory does not exist'):
                resolve_source_directory(str(root / 'absent'), root)


if __name__ == '__main__':
    unittest.main()
