#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests/test_linter.py: 都市零协会静态质检工具（tools/linter.py）全量单元测试套件
全面覆盖 8 项质检规则正反向用例、CLI 选项、自动修复模式与边缘边界。
运行指令: python3 -m unittest discover -s tests -p "test_*.py"
"""

import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import time
import unittest

# Ensure project root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.linter import (
    Severity,
    Issue,
    LintIssue,
    Linter,
    LintConfig,
    LintReport,
    check_json_syntax,
    check_fullwidth_tilde,
    fix_fullwidth_tilde,
    check_placeholders,
    extract_placeholders,
    check_unclosed_braces,
    check_tmp_tags,
    check_verb_triad,
    check_keyword_trailing_space,
    fix_keyword_trailing_space,
    check_typography,
    check_korean_residue,
    has_fullwidth_tilde,
    has_hangul,
    build_cli_parser,
    lint_file,
    run_linter,
)


class TestRuleL01_JsonSyntax(unittest.TestCase):
    """Rule 1 (L01, FATAL): JSON validity, UTF-8/BOM decoding, and schema integrity."""

    def test_valid_json(self):
        content = '{"dataList": [{"id": 101, "desc": "正常文本"}]}'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNotNone(data)
        self.assertEqual(len(issues), 0)

    def test_invalid_json_syntax(self):
        content = '{"dataList": [{"id": 101, "desc": "未闭合字符串}'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNone(data)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("JSON", issues[0].message)

    def test_utf8_bom_handling(self):
        content_with_bom = '\ufeff{"dataList": [{"id": 102, "desc": "BOM文本"}]}'
        data, issues = check_json_syntax(content_with_bom, "test_bom.json")
        self.assertIsNotNone(data)
        self.assertEqual(len(issues), 0)

    def test_root_not_dict(self):
        content = '[{"id": 101, "desc": "列表根对象"}]'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNone(data)
        self.assertTrue(any("JSON Object" in i.message for i in issues))

    def test_missing_datalist(self):
        content = '{"items": [{"id": 101}]}'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNone(data)
        self.assertTrue(any("dataList" in i.message for i in issues))

    def test_datalist_not_list(self):
        content = '{"dataList": "not_a_list"}'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNone(data)
        self.assertTrue(any("Array" in i.message for i in issues))

    def test_sub_structure_types(self):
        content = '{"dataList": [{"id": 1, "levelList": "invalid_str"}]}'
        data, issues = check_json_syntax(content, "test.json")
        self.assertIsNotNone(data)
        self.assertTrue(any("levelList 必须为 list" in i.message for i in issues))


class TestRuleL02_FullWidthTilde(unittest.TestCase):
    """Rule 2 (L02, FATAL): Zero full-width tilde and wave dash with line/col tracking and auto-fix."""

    def test_valid_halfwidth_tilde(self):
        text = "拼点威力 1~3，等等我~"
        issues = check_fullwidth_tilde(text, "test.json")
        self.assertEqual(len(issues), 0)
        self.assertFalse(has_fullwidth_tilde(text))

    def test_invalid_fullwidth_tilde(self):
        text = "拼点威力 1～3，等等我～"
        issues = check_fullwidth_tilde(text, "test.json")
        self.assertEqual(len(issues), 2)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("全角波浪号", issues[0].message)
        self.assertTrue(has_fullwidth_tilde(text))

    def test_wave_dash_detection(self):
        text = "波浪线测试: 1〜5"
        issues = check_fullwidth_tilde(text, "test.json")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)

    def test_fix_fullwidth_tilde(self):
        text = "1～3 与 4〜6"
        fixed, count = fix_fullwidth_tilde(text)
        self.assertEqual(count, 2)
        self.assertEqual(fixed, "1~3 与 4~6")
        self.assertFalse(has_fullwidth_tilde(fixed))

    def test_line_col_coordinates(self):
        text = "第一行\n第二行包含～全角波浪号"
        issues = check_fullwidth_tilde(text, "test.json")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].line, 2)
        self.assertEqual(issues[0].col, 6)


class TestRuleL03_PlaceholderParity(unittest.TestCase):
    """Rule 3 (L03, FATAL/ERROR): 1:1 placeholder match with broken-brace detection."""

    def test_matching_placeholders(self):
        zh_text = "消耗{0}点道具，同步至{1}阶段"
        kr_text = "{0}개 소모하여 {1}단계로 동기화"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1001")
        self.assertEqual(len(issues), 0)

    def test_reordered_placeholders_valid(self):
        zh_text = "为{1}槽位注入{0}点能量"
        kr_text = "{0} 에너지를 {1} 슬롯에 주입"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1002")
        self.assertEqual(len(issues), 0)

    def test_formatted_placeholder(self):
        zh_text = "获得{0:F1}%伤害加成"
        kr_text = "{0:F1}% 피해량 증가"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1003")
        self.assertEqual(len(issues), 0)

    def test_named_placeholder(self):
        zh_text = "在{Slot}号槽位恢复{hpAmount}点生命值"
        kr_text = "{Slot} 슬롯에서 {hpAmount} 체력 회복"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1004")
        self.assertEqual(len(issues), 0)

    def test_missing_placeholder(self):
        zh_text = "消耗{0}点道具，同步阶段已完成"
        kr_text = "{0}개 소모하여 {1}단계로 동기화"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1005")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("遗漏占位符", issues[0].message)

    def test_extra_placeholder(self):
        zh_text = "消耗{0}点道具，多余{2}"
        kr_text = "{0}개 소모"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1006")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("多余/错改占位符", issues[0].message)

    def test_count_mismatch(self):
        zh_text = "获得{0}点，再次获得{0}点"
        kr_text = "{0}개 획득"
        issues = check_placeholders(zh_text, kr_text, "test.json", item_id="1007")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.ERROR)
        self.assertIn("占位符出现频次不守恒", issues[0].message)

    def test_unclosed_brace(self):
        zh_text = "消耗{0 点道具"
        issues = check_placeholders(zh_text, None, "test.json", item_id="1008")
        self.assertTrue(any(i.severity == Severity.FATAL for i in issues))
        self.assertTrue(check_unclosed_braces(zh_text))

    def test_extract_placeholders(self):
        text = "消耗{0}点资源，在{Slot}号槽位对{1}生效，加成{2:F1}"
        phs = extract_placeholders(text)
        self.assertEqual(phs, ["0", "Slot", "1", "2:F1"])


class TestRuleL04_TmpTagBalance(unittest.TestCase):
    """Rule 5 (L05, FATAL): Unity TMP stack-based parser with LIFO nesting validation."""

    def test_valid_nested_tags(self):
        text = "<b><color=#ff0000>红色粗体</color></b>与<i>斜体</i>"
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 0)

    def test_unclosed_tag(self):
        text = "<b>未闭合粗体文本"
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("未闭合", issues[0].message)

    def test_mismatched_crossed_tags(self):
        text = "<b><color=#ff0000>交叉嵌套</b></color>"
        issues = check_tmp_tags(text, "test.json")
        self.assertGreaterEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("嵌套错乱", issues[0].message)

    def test_extra_closing_tag(self):
        text = "孤立闭标签</color>"
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)
        self.assertIn("多余闭标签", issues[0].message)

    def test_void_tags_sprite_ignored(self):
        text = '获得<sprite name="Laceration">流血效果'
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 0)

    def test_dialogue_brackets_ignored(self):
        text = "但丁发出声音：<嘀嗒，嘀嗒……>，装备<E.G.O>"
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 0)

    def test_case_insensitive_tags(self):
        text = "<COLOR=#ff0000><B>文本</B></COLOR>"
        issues = check_tmp_tags(text, "test.json")
        self.assertEqual(len(issues), 0)


class TestRuleL05_VerbTriad(unittest.TestCase):
    """Rule 6 (L06, ERROR): Verb triad enforcement (获得 / 施加 / 增加 / 减少 / 消耗)."""

    def test_valid_verbs(self):
        text = "自身获得2层[呼吸法] 次数。对目标施加3层[流血] 次数。使震颤 强度增加2点。消耗5点[充能] 。"
        issues = check_verb_triad(text, "Skills_Enemy.json")
        self.assertEqual(len(issues), 0)

    def test_buff_with_wrong_verb(self):
        text = "自身对友方施加2层呼吸法次数"
        issues = check_verb_triad(text, "Skills_Enemy.json")
        self.assertTrue(any(i.severity == Severity.ERROR for i in issues))
        self.assertTrue(any("正面状态层数动词违规" in i.message for i in issues))

    def test_debuff_with_wrong_verb(self):
        text = "对目标获得3层流血次数"
        issues = check_verb_triad(text, "Skills_Enemy.json")
        self.assertTrue(any(i.severity == Severity.ERROR for i in issues))
        self.assertTrue(any("负面状态层数动词违规" in i.message for i in issues))

    def test_potency_with_wrong_verb(self):
        text = "使目标的震颤强度提升2点"
        issues = check_verb_triad(text, "Skills_Enemy.json")
        self.assertTrue(any(i.severity == Severity.ERROR for i in issues))
        self.assertTrue(any("状态强度上升动词违规" in i.message for i in issues))

    def test_decay_with_wrong_verb(self):
        text = "自身的充能层数降低3点"
        issues = check_verb_triad(text, "Skills_Enemy.json")
        self.assertTrue(any(i.severity == Severity.ERROR for i in issues))
        self.assertTrue(any("状态衰减动词违规" in i.message for i in issues))

    def test_potency_amount_noun_exception(self):
        text = "呼吸法 强度获得量+1，流血 施加量+1"
        issues = check_verb_triad(text, "BattleKeywords.json")
        self.assertEqual(len(issues), 0)

    def test_storydata_exemption(self):
        text = "哪怕对敌方施加呼吸法，我也不在乎"
        issues = check_verb_triad(text, "StoryData/S1001.json")
        self.assertEqual(len(issues), 0)


class TestRuleL06_KeywordTrailingSpace(unittest.TestCase):
    """Rule 4 (L04, ERROR): Keyword trailing space with negative lookahead for [{0}]."""

    def test_valid_keyword_space(self):
        text = "自身获得2层[呼吸法] 次数，使目标震颤 强度增加。"
        issues = check_keyword_trailing_space(text, "test.json")
        self.assertEqual(len(issues), 0)

    def test_missing_keyword_space_bracketed(self):
        text = "自身获得2层[呼吸法]次数"
        issues = check_keyword_trailing_space(text, "test.json")
        self.assertTrue(len(issues) >= 1)
        self.assertEqual(issues[0].severity, Severity.ERROR)

    def test_missing_keyword_space_core(self):
        text = "使目标震颤强度增加"
        issues = check_keyword_trailing_space(text, "test.json")
        self.assertTrue(len(issues) >= 1)
        self.assertEqual(issues[0].severity, Severity.ERROR)

    def test_placeholder_in_brackets_exception(self):
        text = "罪人[{0}]参战，以及[{Slot}]状态"
        issues = check_keyword_trailing_space(text, "test.json")
        self.assertEqual(len(issues), 0)

    def test_multiple_spaces_after_keyword(self):
        text = "获得[呼吸法]   次数"
        issues = check_keyword_trailing_space(text, "test.json")
        self.assertTrue(len(issues) >= 1)
        self.assertTrue(any("多个空格" in i.message for i in issues))

    def test_fix_keyword_trailing_space(self):
        bad_text = "自身获得2层[呼吸法]次数，使目标震颤强度增加。"
        fixed, count = fix_keyword_trailing_space(bad_text)
        self.assertGreaterEqual(count, 2)
        self.assertIn("[呼吸法] 次数", fixed)
        self.assertIn("震颤 强度", fixed)


class TestRuleL07_Typography(unittest.TestCase):
    """Rule 7 (L07, WARN): Typography (……, “”, ——) with TMP tag stripping and Morse whitelist."""

    def test_valid_typography(self):
        text = "他说：“这并不合理……全凭管理者大人的指示。”——随后拔出了刀。"
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertEqual(len(issues), 0)

    def test_invalid_ascii_ellipsis(self):
        text = "原来是这样...我不理解..."
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("省略号" in i.message for i in issues))

    def test_invalid_circle_ellipsis(self):
        text = "真的吗。。。我不信"
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("省略号" in i.message for i in issues))

    def test_isolated_single_ellipsis_in_story(self):
        text = "静静等待…"
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("单三点省略号" in i.message for i in issues))

    def test_fullwidth_minus(self):
        text = "声音拉长－断开了"
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("全角减号" in i.message for i in issues))

    def test_double_hyphen(self):
        text = "声音拉长--断开了"
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("双横杠" in i.message for i in issues))

    def test_straight_quotes(self):
        text = '他说: "很好。"'
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertTrue(any("英文半角双引号" in i.message for i in issues))

    def test_quotes_in_tmp_tags_safe(self):
        text = '<sprite name="Laceration">全角“正常对话”'
        issues = check_typography(text, "StoryData/S1001.json")
        self.assertEqual(len(issues), 0)

    def test_morse_code_whitelist(self):
        text = "-- ... -.-"
        issues = check_typography(text, "Skills_Enemy-a1c5p2.json")
        self.assertEqual(len(issues), 0)


class TestRuleL08_KoreanResidue(unittest.TestCase):
    """Rule 8 (L08, FATAL/ERROR): Korean residue scan with absolute whitelist for 'model'."""

    def test_pure_chinese_pass(self):
        text = "全中文正常翻译内容"
        issues = check_korean_residue(text, "test.json", enabled=True)
        self.assertEqual(len(issues), 0)
        self.assertFalse(has_hangul(text))

    def test_korean_residue_detected(self):
        text = "对目标施加 3层 출혈 效果"
        issues = check_korean_residue(text, "test.json", enabled=True)
        self.assertEqual(len(issues), 1)
        self.assertIn("韩文残留", issues[0].message)
        self.assertTrue(has_hangul(text))

    def test_model_key_whitelisted(self):
        text = "이스마엘"
        issues = check_korean_residue(text, "StoryData/1D101A.json", key_name="model", enabled=True)
        self.assertEqual(len(issues), 0)

    def test_scenario_model_codes_id_whitelisted(self):
        text = "엄지아비피"
        issues = check_korean_residue(
            text,
            "ScenarioModelCodes-AutoCreated.json",
            key_name="id",
            enabled=True
        )
        self.assertEqual(len(issues), 0)

    def test_developer_comment_whitelisted(self):
        text = "//효과연출1"
        issues = check_korean_residue(text, "StoryData/3D309I2.json", enabled=True)
        self.assertEqual(len(issues), 0)

    def test_disabled_by_default(self):
        text = "对目标施加 출혈 效果"
        issues = check_korean_residue(text, "test.json", enabled=False)
        self.assertEqual(len(issues), 0)

    def test_season8_fatal_severity(self):
        text = "신규 스킬"
        issues = check_korean_residue(text, "Skills_Enemy-a1c10p1.json", enabled=True)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, Severity.FATAL)


class TestLinterCliAndIntegration(unittest.TestCase):
    """Tests CLI parameters, read-only guarantees, auto-fix, and report generation."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.target_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_only_by_default(self):
        file_path = self.target_dir / "sample.json"
        raw_content = '{"dataList": [{"id": 1, "desc": "错误波浪号～"}]}'
        file_path.write_text(raw_content, encoding="utf-8")

        config = LintConfig(target=str(file_path), fix=False)
        linter = Linter(config)
        report = linter.run()

        self.assertEqual(report.fatal_count, 1)
        self.assertEqual(file_path.read_text(encoding="utf-8"), raw_content)
        self.assertFalse(report.passed)
        self.assertEqual(report.exit_code, 1)

    def test_fix_mode_modifies_safely(self):
        file_path = self.target_dir / "sample_fix.json"
        raw_content = '{"dataList": [{"id": 1, "desc": "错误波浪号～"}]}'
        file_path.write_text(raw_content, encoding="utf-8")

        config = LintConfig(target=str(file_path), fix=True)
        linter = Linter(config)
        report = linter.run()

        self.assertEqual(report.total_fixed_files, 1)
        updated_content = file_path.read_text(encoding="utf-8")
        self.assertIn("~", updated_content)
        self.assertNotIn("～", updated_content)

    def test_exit_code_zero_on_clean(self):
        file_path = self.target_dir / "clean.json"
        raw_content = '{"dataList": [{"id": 1, "desc": "完全正常的文本~"}]}'
        file_path.write_text(raw_content, encoding="utf-8")

        config = LintConfig(target=str(file_path), fix=False)
        linter = Linter(config)
        report = linter.run()

        self.assertEqual(report.fatal_count, 0)
        self.assertEqual(report.error_count, 0)
        self.assertTrue(report.passed)
        self.assertEqual(report.exit_code, 0)

    def test_strict_mode_fails_on_warn(self):
        file_path = self.target_dir / "warn.json"
        raw_content = '{"dataList": [{"id": 1, "desc": "有连打点号...测试"}]}'
        file_path.write_text(raw_content, encoding="utf-8")

        # Non-strict allows warnings to pass
        config_non_strict = LintConfig(target=str(file_path), strict=False)
        report_non_strict = Linter(config_non_strict).run()
        self.assertEqual(report_non_strict.warn_count, 1)
        self.assertTrue(report_non_strict.passed)
        self.assertEqual(report_non_strict.exit_code, 0)

        # Strict rejects warnings
        config_strict = LintConfig(target=str(file_path), strict=True)
        report_strict = Linter(config_strict).run()
        self.assertEqual(report_strict.warn_count, 1)
        self.assertFalse(report_strict.passed)
        self.assertEqual(report_strict.exit_code, 1)

    def test_json_report_generation(self):
        file_path = self.target_dir / "sample.json"
        report_file = self.target_dir / "report.json"
        file_path.write_text('{"dataList": [{"id": 1, "desc": "测试"}]}', encoding="utf-8")

        config = LintConfig(target=str(file_path), json_report=str(report_file))
        linter = Linter(config)
        report = linter.run()

        self.assertTrue(report_file.exists())
        report_data = json.loads(report_file.read_text(encoding="utf-8"))
        self.assertIn("summary", report_data)
        self.assertEqual(report_data["summary"]["total_scanned_files"], 1)

    def test_rules_filter_flag(self):
        file_path = self.target_dir / "filter.json"
        # Has tilde (L02) and unclosed tag (L05)
        raw_content = '{"dataList": [{"id": 1, "desc": "全角波浪号～ <b>未闭合"}]}'
        file_path.write_text(raw_content, encoding="utf-8")

        # Run only L02 (tilde)
        config_l02 = LintConfig(target=str(file_path), rules=["L02"])
        report_l02 = Linter(config_l02).run()
        self.assertEqual(len(report_l02.issues), 1)
        self.assertEqual(report_l02.issues[0].rule, "L02_FULLWIDTH_TILDE")

        # Run only L05 (TMP tags)
        config_l05 = LintConfig(target=str(file_path), rules=["L05"])
        report_l05 = Linter(config_l05).run()
        self.assertEqual(len(report_l05.issues), 1)
        self.assertEqual(report_l05.issues[0].rule, "L05_TMP_TAGS")


class TestPerformanceAndEdgeCases(unittest.TestCase):
    """Tests edge cases, empty structures, legacy compatibility, and multiprocessing."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.target_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_empty_file_and_empty_datalist(self):
        file_path = self.target_dir / "empty.json"
        file_path.write_text('{"dataList": []}', encoding="utf-8")

        config = LintConfig(target=str(file_path))
        linter = Linter(config)
        report = linter.run()

        self.assertEqual(report.total_scanned_files, 1)
        self.assertEqual(len(report.issues), 0)
        self.assertTrue(report.passed)

    def test_legacy_lint_file_wrapper(self):
        file_path = self.target_dir / "legacy.json"
        file_path.write_text('{"dataList": [{"id": 1, "desc": "波浪号～"}]}', encoding="utf-8")

        errors, warnings = lint_file(str(file_path))
        self.assertEqual(len(errors), 1)
        self.assertIn("全角波浪号", errors[0])

    def test_large_text_performance(self):
        file_path = self.target_dir / "large.json"
        entries = [{"id": i, "desc": f"条目 {i}: 正常战斗文本 [呼吸法] 次数增加~"} for i in range(500)]
        content = json.dumps({"dataList": entries}, ensure_ascii=False)
        file_path.write_text(content, encoding="utf-8")

        start = time.time()
        config = LintConfig(target=str(file_path))
        report = Linter(config).run()
        elapsed = time.time() - start

        self.assertTrue(report.passed)
        self.assertLess(elapsed, 2.0)

    def test_cli_parser_defaults(self):
        parser = build_cli_parser()
        args = parser.parse_args([])
        self.assertEqual(args.target, "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN")
        self.assertFalse(args.fix)
        self.assertFalse(args.check_korean)
        self.assertFalse(args.strict)
        self.assertEqual(args.workers, 0)


if __name__ == "__main__":
    unittest.main()
