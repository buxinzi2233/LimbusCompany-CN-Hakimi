"""Static JSON integration coverage for traversal and localized keyword checks."""

import json
from pathlib import Path
import tempfile
import unittest

from tools.keyword_names import load_keyword_names
from tools.linter import LintConfig, Linter, traverse_json_strings


class TestCompleteTraversal(unittest.TestCase):
    """Exercise real resource files without service mocks."""

    def test_array_strings_and_duplicate_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "Passives.json"
            target.write_text('{"dataList":[{"id":-1,"desc":["한글"]},{"id":-1,"desc":["한국어"]}]}', encoding="utf-8")
            values = list(traverse_json_strings(json.loads(target.read_text()), "", {}))
            paths = [path for path, _, _ in values]
            self.assertEqual(paths, ["dataList[id=-1,position=0].desc[0]", "dataList[id=-1,position=1].desc[0]"])
            report = Linter(LintConfig(target=str(target), source_dir=str(root), rules="L08", check_korean=True)).run()
            self.assertEqual(report.error_count, 2)
            self.assertEqual({issue.json_path for issue in report.issues}, set(paths))
            source = root / "source"
            source.mkdir()
            (source / target.name).write_text('{"dataList":[{"id":-1,"desc":["{0}"]},{"id":-1,"desc":["{1}"]}]}', encoding="utf-8")
            target.write_text('{"dataList":[{"id":-1,"desc":["{0}"]},{"id":-1,"desc":["{0}"]}]}', encoding="utf-8")
            parity = Linter(LintConfig(target=str(target), source_dir=str(source), rules="L03")).run()
            self.assertEqual(len(parity.issues), 2)
            self.assertEqual({issue.json_path for issue in parity.issues}, {"dataList[id=-1,position=1].desc[0]"})

    def test_dictionary_keywords_and_titles(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "BattleKeywords-test.json").write_text('{"dataList":[{"id":"Ledger","name":"写进账簿","extra":true}]}', encoding="utf-8")
            (root / "Bufs-test.json").write_text('{"dataList":[{"id":"TremorBurst","name":"震颤 引爆"}]}', encoding="utf-8")
            target = root / "Passives.json"
            target.write_text(json.dumps({"dataList": [
                {"id": 1, "desc": "[写进账簿]"},
                {"id": 2, "desc": "[写进账簿]次数"},
                {"id": 3, "desc": "[写进账簿]\t"},
                {"id": 4, "desc": "[写进账簿]。"},
                {"id": 5, "desc": "[写进账簿] "},
                {"id": 6, "desc": "[命中时]造成伤害；[第2阶段专属]；写进账簿次数；震颤强度"},
                {"id": 7, "desc": "[Ledger]"},
                {"id": 8, "desc": "[震颤 引爆]"},
                {"id": 9, "desc": "[写进账簿]\n"},
                {"id": 10, "desc": "[写进账簿]　"},
            ]}, ensure_ascii=False), encoding="utf-8")
            for workers in (1, 2):
                report = Linter(LintConfig(target=str(root), source_dir=str(root), rules="L04", workers=workers)).run()
                self.assertEqual(report.error_count, 8)
                self.assertEqual({issue.json_path for issue in report.issues}, {f"dataList[id={i}].desc" for i in (1, 2, 3, 4, 7, 8, 9, 10)})
            report = Linter(LintConfig(target=str(target), source_dir=str(root), rules="L04")).run()
            self.assertEqual(report.error_count, 8)

    def test_negative_status_prefixes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "Passives.json"
            target.write_text('{"dataList":[{"id":1,"desc":"获得2层破裂守护 "},{"id":2,"desc":"获得2层震颤同步 "},{"id":3,"desc":"获得2层破裂 "},{"id":4,"desc":"获得2层震颤 "}]}', encoding="utf-8")
            report = Linter(LintConfig(target=str(target), source_dir=str(root), rules="L06")).run()
            self.assertEqual(report.error_count, 2)
            self.assertEqual({issue.json_path for issue in report.issues}, {"dataList[id=3].desc", "dataList[id=4].desc"})

    def test_dictionary_schema_errors_are_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            dictionary = root / "Bufs-test.json"
            for raw in ('{}', '{"dataList":[{}]}', '{"dataList":[{"name":42}]}'):
                dictionary.write_text(raw, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Keyword resource requires"):
                    load_keyword_names(root)
            dictionary.write_text('{', encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                load_keyword_names(root)

    def test_real_workspace_dictionary(self) -> None:
        project = Path(__file__).resolve().parents[1]
        workspace = project / "workspace/LLC_zh-CN"
        names = load_keyword_names(workspace)
        self.assertIn("写进账簿", names)
        self.assertNotIn("命中时", names)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for filename in ("BattleKeywords-BossRaid.json", "Bufs-BossRaid.json"):
                (root / filename).write_bytes((workspace / filename).read_bytes())
            target = root / "Passives.json"
            target.write_text('{"dataList":[{"id":1,"desc":"对目标施加2层[写进账簿]"}]}', encoding="utf-8")
            report = Linter(LintConfig(target=str(target), source_dir=str(root), rules="L04")).run()
            self.assertEqual(report.error_count, 1)
            self.assertIn("[写进账簿]", report.issues[0].message)


if __name__ == "__main__":
    unittest.main()
