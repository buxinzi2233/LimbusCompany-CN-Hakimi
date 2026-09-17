"""Integration checks using the installed client and the complete real package."""

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from tools.deploy_mod import deploy
from tools.diff_extractor import GAME_KR_DIR, PROJECT_ROOT, ZH_DIR, audit
from tools.linter import Linter, LintConfig
from tools.verify_release import hashes, verify


class TestReleaseIntegrity(unittest.TestCase):
    def test_source_delta_has_all_fields_and_translations(self):
        result = audit(GAME_KR_DIR, PROJECT_ROOT / 'references/baseline-KR', ZH_DIR)
        problems = [(f['path'], c['path'], c['problems'])
                    for f in result['files'] for c in f['changes'] if c['problems']]
        self.assertEqual(problems, [], str(problems[:20]))
        self.assertEqual(result['summary']['missing_files'], 0)

    def test_rpg_single_file_uses_its_real_source(self):
        target = ZH_DIR / 'RPGSystem/rpg-loc-ui-common-a1c10p1.json'
        scan = Linter(LintConfig(target=str(target), source_dir=str(GAME_KR_DIR)))
        files = scan.collect_target_files()
        self.assertEqual(len(files), 1)
        self.assertEqual(Path(files[0][2]), GAME_KR_DIR / 'RPGSystem/KR_rpg-loc-ui-common-a1c10p1.json')
        self.assertTrue(scan.run().passed)

    def test_real_package_deployment_and_stale_report_rejection(self):
        result = verify(ZH_DIR, GAME_KR_DIR, PROJECT_ROOT / 'references/baseline-KR',
                        PROJECT_ROOT / 'references/baseline-zh-CN')
        self.assertTrue(result['passed'], str(result['summary']))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            lang = root / 'Lang'
            lang.mkdir()
            (lang / 'config.json').write_text('{"lang":"EN","preserve_setting":true}\n')
            report = root / 'report.json'
            report.write_text(json.dumps(result))
            receipt = deploy(ZH_DIR, GAME_KR_DIR, lang, report, root / 'backup')
            self.assertEqual(hashes(lang / 'LLC_zh-CN'), result['workspace_sha256'])
            self.assertEqual(sorted(p.name for p in lang.iterdir() if p.is_dir()), ['LLC_zh-CN'])
            self.assertEqual(json.loads((lang / 'config.json').read_text()),
                             {'lang': 'LLC_zh-CN', 'preserve_setting': True})
            self.assertEqual(json.loads((root / 'backup/config.json').read_text())['lang'], 'EN')
            self.assertEqual(receipt['status'], 'files_verified_runtime_not_verified')
            copied = root / 'edited-workspace'
            shutil.copytree(ZH_DIR, copied)
            (copied / 'MainUIText-a1c10p1.json').write_text('{}\n')
            deployed = hashes(lang / 'LLC_zh-CN')
            with self.assertRaisesRegex(ValueError, 'Workspace changed'):
                deploy(copied, GAME_KR_DIR, lang, report, root / 'rejected-backup')
            self.assertEqual(hashes(lang / 'LLC_zh-CN'), deployed)
            self.assertFalse((root / 'rejected-backup').exists())
            shutil.copy2(ZH_DIR / 'MainUIText-a1c10p1.json', copied / 'MainUIText-a1c10p1.json')
            items = copied / 'Items-a1c10p1.json'
            original_items = items.read_bytes()
            content = json.loads(original_items)
            content_with_extra = {**content, 'dataList': [*content['dataList'],
                                  {'id': 'unrequested-resource', 'name': 'Unexpected resource'}]}
            items.write_text(json.dumps(content_with_extra))
            extra = audit(GAME_KR_DIR, PROJECT_ROOT / 'references/baseline-KR', copied)
            self.assertTrue(any('unexpected_field' in change['problems']
                                for file in extra['files'] for change in file['changes']))
            items.write_bytes(original_items)
            (copied / 'AbEvents-a1c8p2.json').unlink()
            removed = verify(copied, GAME_KR_DIR, PROJECT_ROOT / 'references/baseline-KR',
                             PROJECT_ROOT / 'references/baseline-zh-CN')
            self.assertFalse(removed['passed'])
            self.assertTrue(any(f['rule'] == 'BASELINE_FILE_MISSING' for f in removed['introduced_findings']))


if __name__ == '__main__':
    unittest.main()
