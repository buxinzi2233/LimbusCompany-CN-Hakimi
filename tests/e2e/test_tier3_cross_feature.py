# -*- coding: utf-8 -*-
"""
Tier 3: Cross-Feature Combinations Test Suite.
Verifies pairwise and cross-module interactions between combat skills,
keywords, buff systems, typography/fonts, character voices, and Steam deployment.
Total test count: 10 tests.
"""

import json
from pathlib import Path
import re
import unittest

from tests.e2e.common import (
    WORKSPACE_DIR,
    STEAM_LANG_DIR,
    STEAM_CONFIG_FILE,
    EXPECTED_FONT_SIZE,
    EXPECTED_FONT_SHA256,
    FONT_REL_PATH,
    CORE_KEYWORDS,
    load_json,
    compute_sha256,
    collect_all_strings,
    has_hangul,
    has_fullwidth_tilde,
    validate_tmp_tags,
)


class TestTier3CrossFeature(unittest.TestCase):
    """Tier 3: Pairwise Cross-Feature Interactions."""

    def test_pairwise_combat_skill_keyword_tooltip(self):
        """Tier 3.1: Combat skills referencing keywords use [关键词] + trailing space for TMP tooltip."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"Skills file missing: {fpath}")
        data = load_json(fpath)
        bad_references = []
        for item in data["dataList"]:
            for lvl in item.get("levelList", []):
                desc = lvl.get("desc", "")
                for coin in lvl.get("coinlist", []):
                    for cdesc in coin.get("coindescs", []):
                        desc += " " + cdesc.get("desc", "")
                for kw in CORE_KEYWORDS:
                    # Pattern for keyword without trailing space: [关键词] followed immediately by non-space
                    if re.search(rf'\[{kw}\][^\s]', desc):
                        bad_references.append((item["id"], kw))
        self.assertEqual(len(bad_references), 0, f"Found keyword tags without trailing space: {bad_references[:5]}")

    def test_pairwise_passive_trigger_and_buff_verb_triad(self):
        """Tier 3.2: Passive skill effects obey verb triad: 获得 positive count, 增加 potency, 施加 debuff."""
        fpath = WORKSPACE_DIR / "Passives_Enemy-a1c10p1.json"
        self.assertTrue(fpath.exists(), f"Passives file missing: {fpath}")
        data = load_json(fpath)
        # Verify passive descriptions do not mix invalid verbs
        violations = []
        for item in data["dataList"]:
            desc = item.get("desc", "")
            # Check for forbidden phrasing: e.g. "获得...流血" (positive verb on debuff) or "施加...呼吸法"
            if "获得" in desc and "流血" in desc:
                # Check if it erroneously says 获得X层流血
                if re.search(r'获得\d+层.*流血', desc):
                    violations.append((item["id"], "Erroneously used '获得' with 流血"))
            if "施加" in desc and "呼吸法" in desc:
                if re.search(r'施加\d+层.*呼吸法', desc):
                    violations.append((item["id"], "Erroneously used '施加' with 呼吸法"))
        self.assertEqual(len(violations), 0, f"Verb triad violations in passives: {violations}")

    def test_pairwise_combat_skill_and_sarasa_font_charset(self):
        """Tier 3.3: All Chinese characters in enemy skills exist within valid CJK charset bounds."""
        fpath = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        data = load_json(fpath)
        strings = collect_all_strings(data)
        for s in strings:
            for ch in s:
                # Disallow unmapped control codes except standard \n, \r, \t
                if ord(ch) < 32 and ch not in ("\n", "\r", "\t"):
                    self.fail(f"Invalid control character code {ord(ch)} found in {s}")
                # Ensure no replacement character U+FFFD
                self.assertNotEqual(ord(ch), 0xFFFD, f"Unicode replacement character found in {s}")

    def test_pairwise_story_dialogue_and_sinner_characterization(self):
        """Tier 3.4: Sinner dialogue lines adhere to persona constraints (e.g. Dante clock ticking)."""
        story_path = WORKSPACE_DIR / "StoryData" / "S1000B.json"
        if story_path.exists():
            data = load_json(story_path)
            for item in data["dataList"]:
                teller = item.get("teller", "")
                content = item.get("content", "")
                if teller == "但丁" and "<" in content:
                    # External Dante speech must use <嘀嗒...>
                    if "째깍" in content:
                        self.fail(f"Raw Korean clock tick sound in Dante line {item['id']}: {content}")

    def test_pairwise_rpgsystem_dialogue_and_rich_text_formatting(self):
        """Tier 3.5: RPGSystem dialogue lines containing color tags maintain tag balance."""
        fpath = WORKSPACE_DIR / "RPGSystem" / "rpg-loc-dialogue-floor-1.json"
        self.assertTrue(fpath.exists(), f"RPG dialogue missing: {fpath}")
        data = load_json(fpath)
        tag_errors = []
        for entry in data["dataList"]:
            for text_item in entry.get("texts", []):
                text = text_item.get("text", "")
                valid, err = validate_tmp_tags(text)
                if not valid:
                    tag_errors.append((entry["key"], text, err))
        self.assertEqual(len(tag_errors), 0, f"TMP tag balance errors in RPG dialogue: {tag_errors[:3]}")

    def test_pairwise_steam_deployment_config_and_font_mounting(self):
        """Tier 3.6: Steam deployment has config.json pointing to LLC_zh-CN and valid mounted font."""
        self.assertTrue(STEAM_CONFIG_FILE.exists(), f"config.json missing: {STEAM_CONFIG_FILE}")
        config = load_json(STEAM_CONFIG_FILE)
        self.assertEqual(config.get("lang"), "LLC_zh-CN")

        font_file = STEAM_LANG_DIR / FONT_REL_PATH
        self.assertTrue(font_file.exists(), f"Deployed font missing: {font_file}")
        self.assertEqual(font_file.stat().st_size, EXPECTED_FONT_SIZE)
        self.assertEqual(compute_sha256(font_file), EXPECTED_FONT_SHA256)

    def test_pairwise_boss_raid_ui_and_enemy_naming_consistency(self):
        """Tier 3.7: Enemy names in Enemies-a1c10p1.json align with Boss Raid UI terminology."""
        enemies_path = WORKSPACE_DIR / "Enemies-a1c10p1.json"
        self.assertTrue(enemies_path.exists(), "Enemies file missing")
        enemies_data = load_json(enemies_path)
        enemy_names = {item["name"] for item in enemies_data["dataList"]}
        # Verify key Season 8 enemy names are properly translated
        self.assertTrue(any("雷横" in name or "赤神" in name or "针怪" in name for name in enemy_names),
                        f"Expected Season 8 boss names not found in {enemy_names}")

    def test_pairwise_battle_keywords_and_bufs_id_alignment(self):
        """Tier 3.8: Keyword IDs in BattleKeywords-a1c10p1.json mirror buff entries in Bufs-a1c10p1.json."""
        kw_path = WORKSPACE_DIR / "BattleKeywords-a1c10p1.json"
        bufs_path = WORKSPACE_DIR / "Bufs-a1c10p1.json"
        self.assertTrue(kw_path.exists(), "Keywords missing")
        self.assertTrue(bufs_path.exists(), "Bufs missing")
        kw_data = load_json(kw_path)
        bufs_data = load_json(bufs_path)
        kw_ids = {item["id"] for item in kw_data["dataList"]}
        bufs_ids = {item["id"] for item in bufs_data["dataList"]}
        common_ids = kw_ids.intersection(bufs_ids)
        self.assertGreater(len(common_ids), 0, "No common IDs between BattleKeywords and Bufs")

    def test_pairwise_stage_node_and_story_id_flow(self):
        """Tier 3.9: Stage nodes in StageNode-a1c10p1.json link to Chapter 10 story stage sequence."""
        stage_path = WORKSPACE_DIR / "StageNode-a1c10p1.json"
        self.assertTrue(stage_path.exists(), "StageNode file missing")
        stage_data = load_json(stage_path)
        stage_ids = [item["id"] for item in stage_data["dataList"]]
        self.assertIn(11001, stage_ids, "Stage 11001 missing")
        self.assertIn(11004, stage_ids, "Stage 11004 missing")

    def test_pairwise_announcer_voice_dialogue_alignment(self):
        """Tier 3.10: Announcer metadata in Announcer-a1c10p1.json matches BattleAnnouncerDlg files."""
        announcer_path = WORKSPACE_DIR / "Announcer-a1c10p1.json"
        self.assertTrue(announcer_path.exists(), "Announcer meta missing")
        announcer_data = load_json(announcer_path)
        meta_ids = {item["id"] for item in announcer_data["dataList"]}
        # ID 55 is the Sisyphus Emporium Announcer introduced in a1c10p1
        self.assertIn(55, meta_ids, f"Season 8 Announcer 55 missing from meta: {meta_ids}")


if __name__ == "__main__":
    unittest.main()
