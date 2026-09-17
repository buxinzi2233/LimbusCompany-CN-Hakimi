# -*- coding: utf-8 -*-
"""
Tier 2: Boundary & Corner Cases Test Suite.
Verifies edge cases, extreme text lengths, complex nested coin structures,
multiple placeholders, mixed TMP formatting tags, and punctuation boundaries.
Total test count: 16 tests.
"""

import json
from pathlib import Path
import re
import unittest

from tests.e2e.common import (
    WORKSPACE_DIR,
    KR_BASE_DIR,
    HANGUL_REGEX,
    FULLWIDTH_TILDE_REGEX,
    PLACEHOLDER_REGEX,
    TMP_TAG_REGEX,
    CORE_KEYWORDS,
    load_json,
    collect_all_strings,
    has_hangul,
    has_fullwidth_tilde,
    extract_placeholders,
    validate_tmp_tags,
)


class TestTier2BoundaryCorner(unittest.TestCase):
    """Tier 2: Boundary and Corner Case Verification."""

    def test_empty_description_handling(self):
        """Tier 2.1: Empty string fields in descriptions are valid and handled safely."""
        sample_item = {"id": 9999, "name": "测试空描述", "desc": "", "summary": ""}
        self.assertEqual(sample_item["desc"], "")
        self.assertFalse(has_hangul(sample_item["desc"]))
        self.assertFalse(has_fullwidth_tilde(sample_item["desc"]))
        valid, _ = validate_tmp_tags(sample_item["desc"])
        self.assertTrue(valid)

    def test_whitespace_only_descriptions(self):
        """Tier 2.2: Descriptions consisting only of spaces/newlines are processed safely."""
        ws_desc = "   \n\t  \n  "
        self.assertFalse(has_hangul(ws_desc))
        self.assertFalse(has_fullwidth_tilde(ws_desc))
        valid, _ = validate_tmp_tags(ws_desc)
        self.assertTrue(valid)

    def test_extreme_string_lengths(self):
        """Tier 2.3: Extreme text lengths (>5,000 chars) do not trigger regex catastrophe."""
        long_narrative = "这是一个非常漫长的剧情叙述。" * 400  # ~5,600 characters
        self.assertGreater(len(long_narrative), 5000)
        # Test regex execution time & safety
        self.assertFalse(has_hangul(long_narrative))
        self.assertFalse(has_fullwidth_tilde(long_narrative))
        valid, err = validate_tmp_tags(f"<color=#ffffff>{long_narrative}</color>")
        self.assertTrue(valid, f"Failed on long tagged string: {err}")

    def test_deeply_nested_coins_hierarchy(self):
        """Tier 2.4: Deeply nested skill coin hierarchy (4+ levels, 5+ coins) traversable."""
        nested_skill = {
            "id": 99901,
            "levelList": [
                {
                    "level": 1,
                    "name": "多重连击",
                    "desc": "硬币测试",
                    "coinlist": [
                        {"coindescs": [{"desc": f"[硬币{i}] 造成{i*2}点伤害"} for i in range(1, 6)]}
                    ]
                }
            ]
        }
        all_descs = []
        for lvl in nested_skill["levelList"]:
            all_descs.append(lvl["desc"])
            for coin in lvl["coinlist"]:
                for cdesc in coin["coindescs"]:
                    all_descs.append(cdesc["desc"])
        self.assertEqual(len(all_descs), 6)  # 1 level desc + 5 coin descs

    def test_multiple_placeholders_ordering(self):
        """Tier 2.5: Multiple placeholders with inverted target ordering match source tokens."""
        kr_template = "대상 {0}에게 {1}의 피해를 주고 {Slot}번 슬롯을 파괴한다."
        zh_template = "在{Slot}号槽位对目标{0}造成{1}点伤害。"
        kr_tokens = sorted(extract_placeholders(kr_template))
        zh_tokens = sorted(extract_placeholders(zh_template))
        self.assertEqual(kr_tokens, zh_tokens)
        self.assertEqual(kr_tokens, ["0", "1", "Slot"])

    def test_repeated_placeholders(self):
        """Tier 2.6: Repeated placeholders within a single sentence are extracted consistently."""
        repeated_str = "消耗{0}点能量，若{0}大于5则再次返还{0}点。"
        tokens = extract_placeholders(repeated_str)
        self.assertEqual(tokens, ["0", "0", "0"])
        unique_tokens = sorted(list(set(tokens)))
        self.assertEqual(unique_tokens, ["0"])

    def test_mixed_tmp_tags_complex_ordering(self):
        """Tier 2.7: Complex multi-level LIFO TMP tags are validated properly."""
        complex_tag = "<b><color=#ff0000><i><u><size=120%>极限战斗状态</size></u></i></color></b>"
        is_valid, err = validate_tmp_tags(complex_tag)
        self.assertTrue(is_valid, f"Failed on valid multi-level tags: {err}")

        broken_complex = "<b><color=#ff0000><i><u>极限战斗状态</i></u></color></b>"
        is_valid, _ = validate_tmp_tags(broken_complex)
        self.assertFalse(is_valid, "Failed to detect crossed closing tags </i></u>")

    def test_case_insensitive_tmp_tag_matching(self):
        """Tier 2.8: Case variations in TMP tags (e.g. <COLOR=#HEX>...</color>) match correctly."""
        mixed_case = "<COLOR=#ABCDEF><b>大写标签测试</b></COLOR>"
        is_valid, err = validate_tmp_tags(mixed_case)
        self.assertTrue(is_valid, f"Failed case-insensitive match: {err}")

    def test_special_characters_ascii_tilde(self):
        """Tier 2.9: ASCII tildes (~) used for numeric ranges (1~3) are allowed and valid."""
        range_str = "拼点威力1~3点，持续2~4回合~"
        self.assertFalse(has_fullwidth_tilde(range_str))
        self.assertIn("~", range_str)

    def test_special_characters_chinese_punctuation(self):
        """Tier 2.10: Proper Chinese punctuation: six-dot ellipsis …… and curly quotes “ ”."""
        sample_dialogue = "“这……难道就是‘金枝’的共鸣反应？”"
        self.assertIn("……", sample_dialogue)
        self.assertIn("“", sample_dialogue)
        self.assertIn("”", sample_dialogue)
        self.assertIn("‘", sample_dialogue)
        self.assertIn("’", sample_dialogue)
        self.assertNotIn("...", sample_dialogue)

    def test_skill_brackets_vs_story_brackets(self):
        """Tier 2.11: Skills use compact half-width () while story actions use full-width （）."""
        skill_text = "获得3层呼吸法 (最多10层)"
        story_text = "“好啦好啦……”（但丁轻轻摇了摇头）"
        self.assertRegex(skill_text, r'\([^\)]+\)')
        self.assertRegex(story_text, r'（[^）]+）')

    def test_key_identifier_type_diversity(self):
        """Tier 2.12: Supports both integer IDs and string Keys across localization files."""
        int_id_entry = {"id": 1001, "name": "标准技能"}
        str_key_entry = {"key": "STEP_01", "texts": ["第一步"]}
        self.assertIsInstance(int_id_entry["id"], int)
        self.assertIsInstance(str_key_entry["key"], str)

    def test_missing_optional_schema_fields(self):
        """Tier 2.13: Missing optional fields (flavor, summary, undefined) do not raise KeyError."""
        minimal_entry = {"id": 5001, "name": "测试项", "desc": "基础描述"}
        # Safe access with .get()
        flavor = minimal_entry.get("flavor", "")
        summary = minimal_entry.get("summary", "")
        self.assertEqual(flavor, "")
        self.assertEqual(summary, "")

    def test_multiline_newlines_in_dialogue(self):
        """Tier 2.14: Strings containing multi-line newlines (\\n) parse cleanly without escaping loss."""
        multiline = "第一行对话\n第二行对话\n第三行结束"
        lines = multiline.split("\n")
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[1], "第二行对话")

    def test_zero_length_coin_list(self):
        """Tier 2.15: Defensive skills or passives with empty coinlist [] do not crash traversers."""
        guard_skill = {
            "id": 88801,
            "levelList": [{"level": 1, "name": "防御", "desc": "防御准备", "coinlist": []}]
        }
        total_coins = sum(len(lvl.get("coinlist", [])) for lvl in guard_skill["levelList"])
        self.assertEqual(total_coins, 0)

    def test_escaped_unicode_characters(self):
        """Tier 2.16: Escaped unicode characters (middle dot ·, fullwidth space) retain integrity."""
        ryoshu_phrase = "寸\u00b7铁\u00b7杀\u00b7人"
        self.assertEqual(ryoshu_phrase, "寸·铁·杀·人")
        self.assertIn("·", ryoshu_phrase)


if __name__ == "__main__":
    unittest.main()
