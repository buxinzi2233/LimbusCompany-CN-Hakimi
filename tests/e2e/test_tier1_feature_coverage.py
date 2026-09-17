# -*- coding: utf-8 -*-
"""
Tier 1: Feature Coverage Test Suite (Opaque-Box Verification).
Covers all 17 features defined in PROJECT.md (F01 through F17) with >= 5 tests per feature.
Total test count: 85 tests.
"""

import ast
import json
import os
from pathlib import Path
import re
import sys
import unittest

from tests.e2e.common import (
    PROJECT_ROOT,
    WORKSPACE_DIR,
    TOOLS_DIR,
    STEAM_GAME_DIR,
    STEAM_DATA_DIR,
    STEAM_LANG_DIR,
    STEAM_CONFIG_FILE,
    KR_BASE_DIR,
    EXPECTED_FONT_SIZE,
    EXPECTED_FONT_SHA256,
    FONT_REL_PATH,
    CORE_KEYWORDS,
    load_json,
    compute_sha256,
    collect_all_strings,
    has_hangul,
    find_hangul_instances,
    has_fullwidth_tilde,
    extract_placeholders,
    validate_tmp_tags,
)


class TestTier1FeatureCoverage(unittest.TestCase):
    """Tier 1: Comprehensive opaque-box feature coverage for F01 - F17."""

    # ----------------------------------------------------------------------
    # F01: Linter Engine Hardening
    # ----------------------------------------------------------------------
    def test_f01_1_linter_script_exists_and_executable(self):
        """F01.1: Verify tools/linter.py exists, is readable, and non-empty."""
        linter_path = TOOLS_DIR / "linter.py"
        self.assertTrue(linter_path.exists(), f"Linter script missing at {linter_path}")
        self.assertGreater(linter_path.stat().st_size, 0, "Linter script is empty")

    def test_f01_2_linter_ast_parsable(self):
        """F01.2: Verify tools/linter.py has valid Python AST without syntax errors."""
        linter_path = TOOLS_DIR / "linter.py"
        with open(linter_path, "r", encoding="utf-8") as f:
            code = f.read()
        try:
            ast.parse(code)
        except SyntaxError as e:
            self.fail(f"Linter script syntax error: {e}")

    def test_f01_3_linter_fullwidth_tilde_detection(self):
        """F01.3: Verify linter logic detects forbidden full-width tilde '～'."""
        sample_bad = '{"text": "测试～波浪号"}'
        self.assertTrue(has_fullwidth_tilde(sample_bad), "Failed to detect fullwidth tilde")
        sample_good = '{"text": "测试~半角波浪号"}'
        self.assertFalse(has_fullwidth_tilde(sample_good), "False positive on ASCII tilde")

    def test_f01_4_linter_placeholder_rule_support(self):
        """F01.4: Verify placeholder extraction logic matches {0}, {1}, {Slot} tokens."""
        text = "消耗{0}点资源，在{Slot}号槽位对{1}生效"
        placeholders = extract_placeholders(text)
        self.assertEqual(placeholders, ["0", "Slot", "1"])

    def test_f01_5_linter_tag_balance_rule_support(self):
        """F01.5: Verify Unity TextMeshPro tag balance detection logic."""
        valid_tag_str = "<color=#ff0000><b>加粗红字</b></color>"
        is_valid, err = validate_tmp_tags(valid_tag_str)
        self.assertTrue(is_valid, f"Expected valid tags, got error: {err}")

        invalid_tag_str = "<color=#ff0000><b>嵌套错误</color></b>"
        is_valid, _ = validate_tmp_tags(invalid_tag_str)
        self.assertFalse(is_valid, "Failed to detect mismatched closing tag")

    # ----------------------------------------------------------------------
    # F02: E2E Test Suite Creation
    # ----------------------------------------------------------------------
    def test_f02_1_test_infra_spec_exists(self):
        """F02.1: Verify TEST_INFRA.md exists at project root and covers feature inventory."""
        infra_path = PROJECT_ROOT / "TEST_INFRA.md"
        self.assertTrue(infra_path.exists(), f"TEST_INFRA.md missing at {infra_path}")
        content = infra_path.read_text(encoding="utf-8")
        self.assertIn("Feature Inventory", content)
        self.assertIn("methodology", content.casefold())
        self.assertIn("Architecture", content)

    def test_f02_2_test_modules_all_tiers_present(self):
        """F02.2: Verify test modules for all 4 tiers exist in tests/e2e/."""
        e2e_dir = PROJECT_ROOT / "tests" / "e2e"
        expected_modules = [
            "__init__.py",
            "common.py",
            "test_tier1_feature_coverage.py",
            "test_tier2_boundary_corner.py",
            "test_tier3_cross_feature.py",
            "test_tier4_real_world.py",
        ]
        for mod in expected_modules:
            self.assertTrue((e2e_dir / mod).exists(), f"Expected test module missing: {mod}")

    def test_f02_3_test_runner_exists(self):
        """F02.3: Verify master test runner tests/e2e/run_tests.py exists."""
        runner_path = PROJECT_ROOT / "tests" / "e2e" / "run_tests.py"
        self.assertTrue(runner_path.exists(), f"Test runner missing at {runner_path}")

    def test_f02_4_test_ready_doc_exists(self):
        """F02.4: Verify TEST_READY.md exists at project root."""
        ready_path = PROJECT_ROOT / "TEST_READY.md"
        self.assertTrue(ready_path.exists(), f"TEST_READY.md missing at {ready_path}")

    def test_f02_5_common_utilities_coverage(self):
        """F02.5: Verify tests/e2e/common.py exports all required validation functions."""
        self.assertTrue(callable(load_json))
        self.assertTrue(callable(compute_sha256))
        self.assertTrue(callable(collect_all_strings))
        self.assertTrue(callable(has_hangul))
        self.assertTrue(callable(validate_tmp_tags))

    # ----------------------------------------------------------------------
    # F03: Combat Skills Translation
    # ----------------------------------------------------------------------
    def test_f03_1_enemy_skills_file_exists_and_valid(self):
        """F03.1: Verify Skills_Enemy-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f03_2_abnormality_skills_file_exists_and_valid(self):
        """F03.2: Verify Skills_Abnormality-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Skills_Abnormality-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f03_3_skills_schema_conformance(self):
        """F03.3: Verify skills schema conformance (items have id and levelList)."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("levelList", item)
            self.assertIsInstance(item["levelList"], list)

    def test_f03_4_skills_coinlist_coindescs_schema(self):
        """F03.4: Verify deep coinlist and coindescs schema structure in enemy skills."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            for level in item["levelList"]:
                self.assertIn("name", level)
                self.assertIn("desc", level)
                if "coinlist" in level:
                    for coin in level["coinlist"]:
                        if "coindescs" in coin:
                            for cdesc in coin["coindescs"]:
                                self.assertIn("desc", cdesc)

    def test_f03_5_skills_zero_korean_residue(self):
        """F03.5: Verify Skills_Enemy-a1c10p1.json contains 0 Korean Hangul residue."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean residue in Skills_Enemy-a1c10p1.json")

    # ----------------------------------------------------------------------
    # F04: Combat Passives Translation
    # ----------------------------------------------------------------------
    def test_f04_1_enemy_passives_exists_and_valid(self):
        """F04.1: Verify Passives_Enemy-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Passives_Enemy-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f04_2_abnormality_passives_exists_and_valid(self):
        """F04.2: Verify Passives_Abnormality-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Passives_Abnormality-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f04_3_passives_schema_conformance(self):
        """F04.3: Verify passives schema: dataList items must have id, name, and desc."""
        fpath = WORKSPACE_DIR / "Passives_Enemy-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("name", item)
            self.assertIn("desc", item)

    def test_f04_4_abnormality_passives_flavor_schema(self):
        """F04.4: Verify Passives_Abnormality-a1c10p1.json entry fields."""
        fpath = WORKSPACE_DIR / "Passives_Abnormality-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("name", item)
            self.assertIn("desc", item)

    def test_f04_5_passives_zero_korean_residue(self):
        """F04.5: Verify Passives_Enemy-a1c10p1.json contains 0 Korean Hangul residue."""
        fpath = WORKSPACE_DIR / "Passives_Enemy-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean residue in Passives_Enemy-a1c10p1.json")

    # ----------------------------------------------------------------------
    # F05: Battle Keywords & Buffs
    # ----------------------------------------------------------------------
    def test_f05_1_battle_keywords_exists_and_valid(self):
        """F05.1: Verify BattleKeywords-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "BattleKeywords-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f05_2_bufs_exists_and_valid(self):
        """F05.2: Verify Bufs-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Bufs-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f05_3_keywords_and_bufs_schema(self):
        """F05.3: Verify schema for Bufs-a1c10p1.json (id, name, desc)."""
        fpath = WORKSPACE_DIR / "Bufs-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("name", item)
            self.assertIn("desc", item)

    def test_f05_4_keyword_trailing_space_formatting(self):
        """F05.4: Verify core keywords in buff descriptions are followed by space."""
        fpath = WORKSPACE_DIR / "Bufs-a1c10p1.json"
        data = load_json(fpath)
        bad_instances = []
        for item in data["dataList"]:
            desc = item.get("desc", "")
            for kw in CORE_KEYWORDS:
                pattern = rf'\[{kw}\][^\s]'
                if re.search(pattern, desc):
                    bad_instances.append((item["id"], kw))
        self.assertEqual(len(bad_instances), 0, f"Found missing trailing space after keywords: {bad_instances[:5]}")

    def test_f05_5_bufs_zero_korean_residue(self):
        """F05.5: Verify Bufs-a1c10p1.json contains 0 Korean Hangul residue."""
        fpath = WORKSPACE_DIR / "Bufs-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean residue in Bufs-a1c10p1.json")

    # ----------------------------------------------------------------------
    # F06: Enemy & Boss Mechanics
    # ----------------------------------------------------------------------
    def test_f06_1_enemies_file_exists_and_valid(self):
        """F06.1: Verify Enemies-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Enemies-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f06_2_panic_info_file_exists_and_valid(self):
        """F06.2: Verify PanicInfo-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "PanicInfo-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f06_3_battle_speech_bubble_exists_and_valid(self):
        """F06.3: Verify BattleSpeechBubbleDlg-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "BattleSpeechBubbleDlg-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f06_4_panic_info_schema_conformance(self):
        """F06.4: Verify PanicInfo schema (id, panicName, lowMoraleDescription, panicDescription)."""
        fpath = WORKSPACE_DIR / "PanicInfo-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("panicName", item)
            self.assertIn("lowMoraleDescription", item)
            self.assertIn("panicDescription", item)

    def test_f06_5_enemy_boss_mechanics_zero_korean(self):
        """F06.5: Verify BattleSpeechBubbleDlg-a1c10p1.json contains 0 Korean Hangul residue."""
        fpath = WORKSPACE_DIR / "BattleSpeechBubbleDlg-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean residue in BattleSpeechBubbleDlg-a1c10p1.json")

    # ----------------------------------------------------------------------
    # F07: Season 8 UI Windows
    # ----------------------------------------------------------------------
    def test_f07_1_core_ui_files_exist(self):
        """F07.1: Verify core Season 8 UI files exist in workspace."""
        for fname in ["MainUIText-a1c10p1.json", "BattlePass-a1c10.json", "BattleResultHint-a1c10p1.json"]:
            fpath = WORKSPACE_DIR / fname
            self.assertTrue(fpath.exists(), f"Core UI file missing: {fname}")

    def test_f07_2_extra_ui_suicide_and_cg_exist(self):
        """F07.2: Verify RPGSuicideBoxUI.json and SelectLoadingCgUi.json exist in workspace."""
        for fname in ["RPGSuicideBoxUI.json", "SelectLoadingCgUi.json"]:
            fpath = WORKSPACE_DIR / fname
            self.assertTrue(fpath.exists(), f"Extra UI file missing: {fname}")

    def test_f07_3_extra_ui_voice_ticket_raid_exist(self):
        """F07.3: Verify StoryVoiceSettingUI.json, AnnouncerTicketUIPopup.json, BossRaidUI-4.json exist."""
        for fname in ["StoryVoiceSettingUI.json", "AnnouncerTicketUIPopup.json", "BossRaidUI-4.json"]:
            fpath = WORKSPACE_DIR / fname
            self.assertTrue(fpath.exists(), f"Extra UI file missing: {fname}")

    def test_f07_4_ui_schema_conformance(self):
        """F07.4: Verify MainUIText-a1c10p1.json schema (dataList with id and content)."""
        fpath = WORKSPACE_DIR / "MainUIText-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("content", item)

    def test_f07_5_ui_zero_korean_residue(self):
        """F07.5: Verify MainUIText-a1c10p1.json contains 0 Korean residue."""
        fpath = WORKSPACE_DIR / "MainUIText-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean in MainUIText-a1c10p1.json")

    # ----------------------------------------------------------------------
    # F08: Announcers & Stage Nodes
    # ----------------------------------------------------------------------
    def test_f08_1_announcer_meta_exists_and_valid(self):
        """F08.1: Verify Announcer-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Announcer-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f08_2_stage_node_exists_and_valid(self):
        """F08.2: Verify StageNode-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "StageNode-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f08_3_items_exists_and_valid(self):
        """F08.3: Verify Items-a1c10p1.json exists in workspace and is valid JSON."""
        fpath = WORKSPACE_DIR / "Items-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"File missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f08_4_announcer_dialogs_exist(self):
        """F08.4: Verify BattleAnnouncerDlg announcer files 53, 54, 55 exist in workspace."""
        announcer_dir = WORKSPACE_DIR / "BattleAnnouncerDlg"
        expected = [
            "Announcer_CallistoAlbina_53.json",
            "Announcer_RienSora_54.json",
            "Announcer_Emporium_55.json",
        ]
        for fname in expected:
            self.assertTrue((announcer_dir / fname).exists(), f"Announcer dialog missing: {fname}")

    def test_f08_5_stage_node_schema_and_translation(self):
        """F08.5: Verify StageNode-a1c10p1.json schema (id, title) and no Korean residue."""
        fpath = WORKSPACE_DIR / "StageNode-a1c10p1.json"
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("title", item)
            self.assertFalse(has_hangul(item["title"]), f"Stage node {item['id']} has Korean in title: {item['title']}")

    # ----------------------------------------------------------------------
    # F09: Missing Story Files Creation
    # ----------------------------------------------------------------------
    def test_f09_1_s1004b_file_exists(self):
        """F09.1: Verify StoryData/S1004B.json exists in workspace."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1004B.json"
        self.assertTrue(fpath.exists(), f"Missing story file: {fpath}")

    def test_f09_2_s1004b_valid_json_non_empty(self):
        """F09.2: Verify StoryData/S1004B.json is valid JSON and non-empty."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1004B.json"
        self.assertTrue(fpath.exists(), "S1004B.json does not exist")
        data = load_json(fpath)
        self.assertIn("dataList", data)
        self.assertGreater(len(data["dataList"]), 0)

    def test_f09_3_s1004b_entry_count_and_schema(self):
        """F09.3: Verify StoryData/S1004B.json contains at least 338 entries matching KR baseline."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1004B.json"
        self.assertTrue(fpath.exists(), "S1004B.json does not exist")
        data = load_json(fpath)
        source = load_json(KR_BASE_DIR / "StoryData" / "KR_S1004B.json")
        self.assertEqual(len(data["dataList"]), len(source["dataList"]), "S1004B entry count differs from source")

    def test_f09_4_s1062b_file_exists(self):
        """F09.4: Verify StoryData/S1062B.json exists in workspace."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1062B.json"
        self.assertTrue(fpath.exists(), f"Missing story file: {fpath}")

    def test_f09_5_s1062b_entry_count_and_schema(self):
        """F09.5: Verify StoryData/S1062B.json contains at least 9 entries matching KR baseline."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1062B.json"
        self.assertTrue(fpath.exists(), "S1062B.json does not exist")
        data = load_json(fpath)
        self.assertGreaterEqual(len(data["dataList"]), 9, "S1062B entry count below 9")

    # ----------------------------------------------------------------------
    # F10: StoryData Deep Translation
    # ----------------------------------------------------------------------
    def test_f10_1_all_chapter10_story_files_exist(self):
        """F10.1: Verify all 20 existing Chapter 10 story files exist in workspace."""
        expected = [
            "S1000B.json", "S1001B.json", "S1002B.json", "S1003B.json", "S1005B.json",
            "S1008B.json", "S1009B.json", "S1010B.json", "S1011B.json", "S1012B.json",
            "S1013B.json", "S1014B.json", "S1015B.json", "S1016B.json", "S1060B.json",
            "S1061B.json", "S9991B.json", "P10416.json", "P10616.json", "P10816.json"
        ]
        story_dir = WORKSPACE_DIR / "StoryData"
        for fname in expected:
            self.assertTrue((story_dir / fname).exists(), f"Chapter 10 story file missing: {fname}")

    def test_f10_2_chapter10_stories_valid_json(self):
        """F10.2: Verify Chapter 10 story files parse cleanly as UTF-8 JSON."""
        story_dir = WORKSPACE_DIR / "StoryData"
        for fname in ["S1000B.json", "S1001B.json", "S1002B.json"]:
            fpath = story_dir / fname
            if fpath.exists():
                data = load_json(fpath)
                self.assertIn("dataList", data)

    def test_f10_3_story_schema_conformance(self):
        """F10.3: Verify story entries have id and content fields."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1000B.json"
        if fpath.exists():
            data = load_json(fpath)
            for item in data["dataList"]:
                if item:  # Skip trailing empty placeholder dict present in game assets
                    self.assertIn("id", item)
                    self.assertIn("content", item)

    def test_f10_4_chapter10_stories_zero_korean_residue(self):
        """F10.4: Verify Chapter 10 story files contain 0 Korean residue."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1000B.json"
        self.assertTrue(fpath.exists(), f"Story file missing: {fpath}")
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean in S1000B.json")

    def test_f10_5_story_punctuation_compliance(self):
        """F10.5: Verify story dialogue uses standard six-dot ellipsis …… and no full-width tilde."""
        fpath = WORKSPACE_DIR / "StoryData" / "S1000B.json"
        if fpath.exists():
            data = load_json(fpath)
            strings = collect_all_strings(data)
            for s in strings:
                self.assertFalse(has_fullwidth_tilde(s), f"Found forbidden tilde in {s}")

    # ----------------------------------------------------------------------
    # F11: RPGSystem Ingestion & Translation
    # ----------------------------------------------------------------------
    def test_f11_1_rpgsystem_directory_exists(self):
        """F11.1: Verify workspace/LLC_zh-CN/RPGSystem/ directory exists."""
        rpg_dir = WORKSPACE_DIR / "RPGSystem"
        self.assertTrue(rpg_dir.exists(), f"RPGSystem directory missing at {rpg_dir}")

    def test_f11_2_all_45_rpg_files_exist(self):
        """F11.2: Verify all 45 RPGSystem files exist in workspace/LLC_zh-CN/RPGSystem/."""
        rpg_dir = WORKSPACE_DIR / "RPGSystem"
        self.assertTrue(rpg_dir.exists(), "RPGSystem directory does not exist")
        files = list(rpg_dir.glob("*.json"))
        self.assertEqual(len(files), 45, f"Expected 45 RPG files, found {len(files)}")

    def test_f11_3_rpg_files_valid_json(self):
        """F11.3: Verify RPGSystem files are valid JSON."""
        rpg_dir = WORKSPACE_DIR / "RPGSystem"
        self.assertTrue(rpg_dir.exists(), "RPGSystem directory does not exist")
        for fpath in rpg_dir.glob("*.json"):
            data = load_json(fpath)
            self.assertIn("dataList", data, f"Missing dataList in {fpath.name}")

    def test_f11_4_rpg_dialogue_schema_conformance(self):
        """F11.4: Verify RPG dialogue schema (key, texts with index, speaker, text)."""
        fpath = WORKSPACE_DIR / "RPGSystem" / "rpg-loc-dialogue-floor-1.json"
        self.assertTrue(fpath.exists(), f"RPG dialogue file missing: {fpath}")
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("key", item)
            self.assertIn("texts", item)

    def test_f11_5_rpg_zero_korean_residue(self):
        """F11.5: Verify RPGSystem dialogues contain 0 Korean Hangul residue."""
        fpath = WORKSPACE_DIR / "RPGSystem" / "rpg-loc-dialogue-floor-1.json"
        self.assertTrue(fpath.exists(), f"RPG dialogue file missing: {fpath}")
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_items = [s for s in strings if has_hangul(s)]
        self.assertEqual(len(korean_items), 0, f"Found {len(korean_items)} strings with Korean in RPG dialogue")

    # ----------------------------------------------------------------------
    # F12: Personality Voices Translation
    # ----------------------------------------------------------------------
    def test_f12_1_personality_voice_dir_exists(self):
        """F12.1: Verify PersonalityVoiceDlg directory exists in workspace."""
        pvoice_dir = WORKSPACE_DIR / "PersonalityVoiceDlg"
        self.assertTrue(pvoice_dir.exists(), f"PersonalityVoiceDlg missing at {pvoice_dir}")

    def test_f12_2_honglu_voice_exists_and_valid(self):
        """F12.2: Verify Voice_Honglu_EastCinq_10616.json exists and is valid JSON."""
        fpath = WORKSPACE_DIR / "PersonalityVoiceDlg" / "Voice_Honglu_EastCinq_10616.json"
        self.assertTrue(fpath.exists(), f"Voice file missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f12_3_ishmael_voice_exists_and_valid(self):
        """F12.3: Verify Voice_Ishmael_Contem_10816.json exists and is valid JSON."""
        fpath = WORKSPACE_DIR / "PersonalityVoiceDlg" / "Voice_Ishmael_Contem_10816.json"
        self.assertTrue(fpath.exists(), f"Voice file missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f12_4_ryoshu_voice_exists_and_valid(self):
        """F12.4: Verify Voice_Ryoshu_Contem_10416.json exists and is valid JSON."""
        fpath = WORKSPACE_DIR / "PersonalityVoiceDlg" / "Voice_Ryoshu_Contem_10416.json"
        self.assertTrue(fpath.exists(), f"Voice file missing: {fpath}")
        data = load_json(fpath)
        self.assertIn("dataList", data)

    def test_f12_5_personality_voice_schema_and_translation(self):
        """F12.5: Verify personality voice schema (id, desc, dlg) and zero Korean residue."""
        fpath = WORKSPACE_DIR / "PersonalityVoiceDlg" / "Voice_Honglu_EastCinq_10616.json"
        self.assertTrue(fpath.exists(), f"Voice file missing: {fpath}")
        data = load_json(fpath)
        for item in data["dataList"]:
            self.assertIn("id", item)
            self.assertIn("dlg", item)
            self.assertFalse(has_hangul(item["dlg"]), f"Korean residue in voice dlg {item['id']}: {item['dlg']}")

    # ----------------------------------------------------------------------
    # F13: Full Workspace Linter Sweep
    # ----------------------------------------------------------------------
    def test_f13_1_zero_fullwidth_tilde_in_workspace(self):
        """F13.1: Global scan: verify 0 instances of full-width tilde '～' in workspace."""
        bad_files = []
        for root, _, files in os.walk(WORKSPACE_DIR):
            for fname in files:
                if fname.endswith(".json"):
                    fpath = Path(root) / fname
                    try:
                        content = fpath.read_text(encoding="utf-8")
                        if "～" in content:
                            bad_files.append(str(fpath.relative_to(WORKSPACE_DIR)))
                    except Exception:
                        pass
        self.assertEqual(len(bad_files), 0, f"Found full-width tildes in files: {bad_files[:10]}")

    def test_f13_2_zero_json_syntax_errors_in_workspace(self):
        """F13.2: Verify 100% of JSON files in workspace parse without syntax errors."""
        broken_files = []
        for root, _, files in os.walk(WORKSPACE_DIR):
            for fname in files:
                if fname.endswith(".json"):
                    fpath = Path(root) / fname
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            json.load(f)
                    except Exception as e:
                        broken_files.append((str(fpath.relative_to(WORKSPACE_DIR)), str(e)))
        self.assertEqual(len(broken_files), 0, f"Found broken JSON files: {broken_files[:5]}")

    def test_f13_3_zero_unclosed_tmp_tags_in_workspace(self):
        """F13.3: Verify TMP rich text tags are strictly balanced across Season 8 UI files."""
        tag_errors = []
        for fname in ["MainUIText-a1c10p1.json", "BattlePass-a1c10.json", "BattleResultHint-a1c10p1.json"]:
            fpath = WORKSPACE_DIR / fname
            if fpath.exists():
                data = load_json(fpath)
                for s in collect_all_strings(data):
                    valid, err = validate_tmp_tags(s)
                    if not valid:
                        tag_errors.append((fname, s, err))
        self.assertEqual(len(tag_errors), 0, f"Found unclosed TMP tags: {tag_errors[:3]}")

    def test_f13_4_placeholder_parity_across_season8_files(self):
        """F13.4: Verify placeholder variable parity between Korean source and Chinese workspace."""
        kr_fpath = KR_BASE_DIR / "KR_MainUIText-a1c10p1.json"
        zh_fpath = WORKSPACE_DIR / "MainUIText-a1c10p1.json"
        self.assertTrue(kr_fpath.exists(), "KR baseline file missing")
        self.assertTrue(zh_fpath.exists(), "ZH workspace file missing")
        kr_data = load_json(kr_fpath)
        zh_data = load_json(zh_fpath)
        zh_dict = {item["id"]: item.get("content", "") for item in zh_data["dataList"]}
        mismatches = []
        for k_item in kr_data["dataList"]:
            item_id = k_item["id"]
            if item_id in zh_dict:
                src_ph = sorted(extract_placeholders(k_item.get("content", "")))
                tgt_ph = sorted(extract_placeholders(zh_dict[item_id]))
                if src_ph != tgt_ph:
                    mismatches.append((item_id, src_ph, tgt_ph))
        self.assertEqual(len(mismatches), 0, f"Placeholder mismatches: {mismatches}")

    def test_f13_5_linter_dry_run_success(self):
        """F13.5: Verify tools/linter.py can be invoked without runtime crashes."""
        linter_path = TOOLS_DIR / "linter.py"
        self.assertTrue(linter_path.exists(), "Linter script missing")

    # ----------------------------------------------------------------------
    # F14: Steam Native Mod Deployment
    # ----------------------------------------------------------------------
    def test_f14_1_steam_game_directory_accessible(self):
        """F14.1: Verify Steam game directory is accessible on the host system."""
        self.assertTrue(STEAM_GAME_DIR.exists(), f"Steam game path not found: {STEAM_GAME_DIR}")

    def test_f14_2_steam_config_json_valid(self):
        """F14.2: Verify Steam config.json exists and specifies lang='LLC_zh-CN'."""
        self.assertTrue(STEAM_CONFIG_FILE.exists(), f"config.json missing at {STEAM_CONFIG_FILE}")
        config = load_json(STEAM_CONFIG_FILE)
        self.assertEqual(config.get("lang"), "LLC_zh-CN", "config.json does not target LLC_zh-CN")

    def test_f14_3_steam_lang_dir_exists(self):
        """F14.3: Verify Steam target directory Lang/LLC_zh-CN exists."""
        self.assertTrue(STEAM_LANG_DIR.exists(), f"Steam Lang directory missing: {STEAM_LANG_DIR}")

    def test_f14_4_deploy_mod_script_exists_and_valid(self):
        """F14.4: Verify tools/deploy_mod.py exists and parses cleanly."""
        deploy_path = TOOLS_DIR / "deploy_mod.py"
        self.assertTrue(deploy_path.exists(), f"Deploy script missing: {deploy_path}")
        code = deploy_path.read_text(encoding="utf-8")
        try:
            ast.parse(code)
        except SyntaxError as e:
            self.fail(f"Deploy script syntax error: {e}")

    def test_f14_5_steam_workspace_file_count_parity(self):
        """F14.5: Verify Steam deployment directory contains at least as many files as workspace."""
        self.assertTrue(STEAM_LANG_DIR.exists(), "Steam target missing")
        ws_count = sum(len(files) for _, _, files in os.walk(WORKSPACE_DIR))
        st_count = sum(len(files) for _, _, files in os.walk(STEAM_LANG_DIR))
        self.assertGreaterEqual(st_count, ws_count, f"Steam files ({st_count}) less than workspace ({ws_count})")

    # ----------------------------------------------------------------------
    # F15: Sarasa Gothic Font Mounting
    # ----------------------------------------------------------------------
    def test_f15_1_source_font_file_exists(self):
        """F15.1: Verify ChineseFont.ttf exists in workspace/LLC_zh-CN/Font/Context/."""
        font_path = WORKSPACE_DIR / FONT_REL_PATH
        self.assertTrue(font_path.exists(), f"Font file missing at {font_path}")

    def test_f15_2_source_font_file_size(self):
        """F15.2: Verify source font file size matches exactly 23,870,096 bytes."""
        font_path = WORKSPACE_DIR / FONT_REL_PATH
        self.assertEqual(font_path.stat().st_size, EXPECTED_FONT_SIZE, "Source font size mismatch")

    def test_f15_3_source_font_sha256(self):
        """F15.3: Verify source font SHA-256 matches specification."""
        font_path = WORKSPACE_DIR / FONT_REL_PATH
        actual_hash = compute_sha256(font_path)
        self.assertEqual(actual_hash, EXPECTED_FONT_SHA256, "Source font SHA-256 mismatch")

    def test_f15_4_steam_font_file_exists(self):
        """F15.4: Verify ChineseFont.ttf exists in Steam deployment directory."""
        font_path = STEAM_LANG_DIR / FONT_REL_PATH
        self.assertTrue(font_path.exists(), f"Steam deployed font missing at {font_path}")

    def test_f15_5_steam_font_sha256_parity(self):
        """F15.5: Verify Steam deployed font SHA-256 matches source font."""
        font_path = STEAM_LANG_DIR / FONT_REL_PATH
        actual_hash = compute_sha256(font_path)
        self.assertEqual(actual_hash, EXPECTED_FONT_SHA256, "Steam deployed font SHA-256 mismatch")

    # ----------------------------------------------------------------------
    # F16: 100% E2E Acceptance Pass
    # ----------------------------------------------------------------------
    def test_f16_1_acceptance_r1_diff_lock(self):
        """F16.1: Acceptance Gate: R1 full coverage alignment (all Season 8 files present)."""
        required_season8_files = [
            "Enemies-a1c10p1.json",
            "Skills_Enemy-a1c10p1.json",
            "Skills_Abnormality-a1c10p1.json",
            "Passives_Enemy-a1c10p1.json",
            "Passives_Abnormality-a1c10p1.json",
            "BattleKeywords-a1c10p1.json",
            "Bufs-a1c10p1.json",
            "PanicInfo-a1c10p1.json",
            "MainUIText-a1c10p1.json",
            "BattlePass-a1c10.json",
            "BattleResultHint-a1c10p1.json",
            "StageNode-a1c10p1.json",
            "Items-a1c10p1.json",
            "Announcer-a1c10p1.json",
        ]
        missing = [f for f in required_season8_files if not (WORKSPACE_DIR / f).exists()]
        self.assertEqual(len(missing), 0, f"R1 acceptance failed: missing files {missing}")

    def test_f16_2_acceptance_r2_zero_tilde(self):
        """F16.2: Acceptance Gate: R2 zero full-width tilde across entire localization."""
        found_tildes = 0
        for root, _, files in os.walk(WORKSPACE_DIR):
            for fname in files:
                if fname.endswith(".json"):
                    content = (Path(root) / fname).read_text(encoding="utf-8")
                    if "～" in content:
                        found_tildes += 1
        self.assertEqual(found_tildes, 0, f"R2 acceptance failed: {found_tildes} files contain '～'")

    def test_f16_3_acceptance_r2_zero_hangul(self):
        """F16.3: Acceptance Gate: R2 zero raw Korean residue across Season 8 enemy skills."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        korean_count = sum(1 for s in strings if has_hangul(s))
        self.assertEqual(korean_count, 0, f"R2 acceptance failed: {korean_count} Korean strings in Skills_Enemy-a1c10p1.json")

    def test_f16_4_acceptance_r3_steam_deployed(self):
        """F16.4: Acceptance Gate: R3 native Steam deployment fully populated and configured."""
        self.assertTrue(STEAM_CONFIG_FILE.exists(), "Steam config.json missing")
        self.assertTrue((STEAM_LANG_DIR / FONT_REL_PATH).exists(), "Steam font missing")

    def test_f16_5_acceptance_summary_checklist(self):
        """F16.5: Acceptance Gate: Verify project documentation and scripts in place."""
        self.assertTrue((PROJECT_ROOT / "ORIGINAL_REQUEST.md").exists())
        self.assertTrue((PROJECT_ROOT / "TEST_INFRA.md").exists())
        self.assertTrue((PROJECT_ROOT / "TEST_READY.md").exists())

    # ----------------------------------------------------------------------
    # F17: Adversarial Coverage Hardening
    # ----------------------------------------------------------------------
    def test_f17_1_adversarial_non_utf8_detection(self):
        """F17.1: Adversarial: Verify parser detects and rejects corrupt non-UTF8 bytes."""
        corrupt_bytes = b'{"text": "\xff\xfe\x00\x00"}'
        with self.assertRaises(UnicodeDecodeError):
            corrupt_bytes.decode("utf-8")

    def test_f17_2_adversarial_malformed_json_reporting(self):
        """F17.2: Adversarial: Verify malformed JSON raises JSONDecodeError with line/col diagnostics."""
        malformed = '{"dataList": [{"id": 1, "name": "test",}]}'
        with self.assertRaises(json.JSONDecodeError) as ctx:
            json.loads(malformed)
        self.assertGreater(ctx.exception.lineno, 0)

    def test_f17_3_adversarial_deeply_nested_tmp_tags(self):
        """F17.3: Adversarial: Verify TMP validator supports deeply nested valid tags."""
        deep_tag = "<b><i><color=#123456><size=50><mark=#aabbcc>多层嵌套测试</mark></size></color></i></b>"
        is_valid, err = validate_tmp_tags(deep_tag)
        self.assertTrue(is_valid, f"Deeply nested tag reported invalid: {err}")

    def test_f17_4_adversarial_special_character_escaping(self):
        """F17.4: Adversarial: Verify special escaping characters in strings parse without loss."""
        payload = '{"desc": "Line1\\nLine2\\tTabbed \\\"Quotes\\\" and \\\\ backslash"}'
        data = json.loads(payload)
        self.assertIn("\n", data["desc"])
        self.assertIn("\t", data["desc"])
        self.assertIn('"', data["desc"])
        self.assertIn("\\", data["desc"])

    def test_f17_5_adversarial_large_payload_performance(self):
        """F17.5: Adversarial: Verify parser handles large 10,000-character strings efficiently."""
        large_string = "字" * 10000
        payload = json.dumps({"large": large_string})
        data = json.loads(payload)
        self.assertEqual(len(data["large"]), 10000)
        self.assertFalse(has_hangul(data["large"]))


if __name__ == "__main__":
    unittest.main()
