# -*- coding: utf-8 -*-
"""
Tier 4: Real-World Application Scenarios Test Suite.
Checks resources used by gameplay flows; does not launch or control the game:
1. Sisyphus Department Store multi-floor dungeon exploration simulation.
2. Season 8 Boss Raid combat and mechanics flow (Leiheng / Red God).
3. Full Main Story Chapter 10 reading and scene transition flow.
4. Native Steam deployment files and font/config integrity check.
5. End-to-End game session asset pipeline (Title -> Pass -> Stage -> Battle -> Results).
Total test count: 5 tests.
"""

import json
from pathlib import Path
import unittest

from tests.e2e.common import (
    WORKSPACE_DIR,
    KR_BASE_DIR,
    STEAM_LANG_DIR,
    STEAM_CONFIG_FILE,
    EXPECTED_FONT_SIZE,
    EXPECTED_FONT_SHA256,
    FONT_REL_PATH,
    load_json,
    compute_sha256,
    collect_all_strings,
    has_hangul,
    has_fullwidth_tilde,
)


class TestTier4RealWorld(unittest.TestCase):
    """Tier 4: Real-World End-to-End Application Scenarios."""

    def test_scenario_sisyphus_dept_store_floor_simulation(self):
        """Tier 4.1: Sisyphus Department Store floor exploration simulation (Floors 1-4, B1, B2)."""
        rpg_dir = WORKSPACE_DIR / "RPGSystem"
        self.assertTrue(rpg_dir.exists(), f"RPGSystem directory missing: {rpg_dir}")

        floors = ["floor-1", "floor-2", "floor-3", "floor-4", "floor-b1", "floor-b2"]
        floor_coverage = {}

        for floor in floors:
            diag_file = rpg_dir / f"rpg-loc-dialogue-{floor}.json"
            quest_file = rpg_dir / f"rpg-loc-quest-{floor}.json"
            npc_file = rpg_dir / f"rpg-loc-npc-{floor}.json"

            self.assertTrue(diag_file.exists(), f"Dialogue missing for {floor}: {diag_file}")
            self.assertTrue(quest_file.exists(), f"Quest missing for {floor}: {quest_file}")
            self.assertTrue(npc_file.exists(), f"NPCs missing for {floor}: {npc_file}")

            diag_data = load_json(diag_file)
            quest_data = load_json(quest_file)
            npc_data = load_json(npc_file)

            floor_coverage[floor] = {
                "dialogues": len(diag_data.get("dataList", [])),
                "quests": len(quest_data.get("dataList", [])),
                "npcs": len(npc_data.get("dataList", [])),
            }
            # Verify each floor has substantive content
            self.assertGreater(floor_coverage[floor]["dialogues"], 0, f"No dialogues on {floor}")
            self.assertGreater(floor_coverage[floor]["quests"], 0, f"No quests on {floor}")

        # Ensure all 6 floors successfully linked
        self.assertEqual(len(floor_coverage), 6)

    def test_scenario_boss_raid_combat_flow(self):
        """Tier 4.2: Boss raid battle execution flow: UI -> Enemies -> Skills -> Passives -> Panic -> Speech."""
        # Phase 1: Boss Raid UI
        raid_ui_path = WORKSPACE_DIR / "BossRaidUI-4.json"
        self.assertTrue(raid_ui_path.exists(), "BossRaidUI-4.json missing")
        raid_ui = load_json(raid_ui_path)
        self.assertGreater(len(raid_ui.get("dataList", [])), 0)

        # Phase 2: Boss enemy data
        enemies_path = WORKSPACE_DIR / "Enemies-a1c10p1.json"
        self.assertTrue(enemies_path.exists(), "Enemies-a1c10p1.json missing")
        enemies_data = load_json(enemies_path)
        enemy_ids = {item["id"] for item in enemies_data.get("dataList", [])}

        # Phase 3: Boss combat skills
        skills_path = WORKSPACE_DIR / "Skills_Enemy-a1c10p1.json"
        self.assertTrue(skills_path.exists(), "Skills_Enemy-a1c10p1.json missing")
        skills_data = load_json(skills_path)
        self.assertGreater(len(skills_data.get("dataList", [])), 0)

        # Phase 4: Combat passives
        passives_path = WORKSPACE_DIR / "Passives_Enemy-a1c10p1.json"
        self.assertTrue(passives_path.exists(), "Passives_Enemy-a1c10p1.json missing")
        passives_data = load_json(passives_path)
        self.assertGreater(len(passives_data.get("dataList", [])), 0)

        # Phase 5: Panic information
        panic_path = WORKSPACE_DIR / "PanicInfo-a1c10p1.json"
        self.assertTrue(panic_path.exists(), "PanicInfo-a1c10p1.json missing")
        panic_data = load_json(panic_path)
        self.assertGreater(len(panic_data.get("dataList", [])), 0)

        # Phase 6: Mid-battle dialogue speech bubbles
        speech_path = WORKSPACE_DIR / "BattleSpeechBubbleDlg-a1c10p1.json"
        self.assertTrue(speech_path.exists(), "BattleSpeechBubbleDlg-a1c10p1.json missing")
        speech_data = load_json(speech_path)
        self.assertGreater(len(speech_data.get("dataList", [])), 0)

    def test_scenario_full_story_chapter10_reading_flow(self):
        """Tier 4.3: Full Chapter 10 story reading flow: S1000B through S1062B sequential walk."""
        story_dir = WORKSPACE_DIR / "StoryData"
        chapter10_sequence = [
            "S1000B.json", "S1001B.json", "S1002B.json", "S1003B.json", "S1004B.json",
            "S1005B.json", "S1008B.json", "S1009B.json", "S1010B.json", "S1011B.json",
            "S1012B.json", "S1013B.json", "S1014B.json", "S1015B.json", "S1016B.json",
            "S1060B.json", "S1061B.json", "S1062B.json", "S9991B.json"
        ]

        total_lines_read = 0
        for story_file in chapter10_sequence:
            fpath = story_dir / story_file
            self.assertTrue(fpath.exists(), f"Story node missing in sequence: {story_file}")
            data = load_json(fpath)
            items = data.get("dataList", [])
            self.assertGreater(len(items), 0, f"Story node is empty: {story_file}")

            # Preserve actual source IDs, including intentional gaps and entries without an ID.
            story_entries = [item for item in items if "id" in item]
            ids = [item["id"] for item in story_entries]
            source = load_json(KR_BASE_DIR / "StoryData" / f"KR_{story_file}")
            source_ids = [item["id"] for item in source["dataList"] if "id" in item]
            self.assertEqual(ids, source_ids, f"Story IDs differ from source in {story_file}")

            # Verify no full-width tilde in story lines
            for item in story_entries:
                content = item.get("content", "")
                self.assertFalse(has_fullwidth_tilde(content), f"Forbidden tilde in {story_file}:{item['id']}")

            total_lines_read += len(story_entries)

        self.assertGreaterEqual(total_lines_read, 1100, f"Total story lines read {total_lines_read} below expectation")

    def test_scenario_steam_deployment_and_mod_loading_sanity(self):
        """Tier 4.4: Check deployed config, font bytes and assets without launching the game."""
        # 1. Config loading
        self.assertTrue(STEAM_CONFIG_FILE.exists(), "Game unable to find Lang/config.json")
        config = load_json(STEAM_CONFIG_FILE)
        self.assertEqual(config.get("lang"), "LLC_zh-CN")

        # 2. Mod language directory exists
        self.assertTrue(STEAM_LANG_DIR.exists(), "Game unable to resolve mod localization directory")

        # 3. Font asset present and byte-accurate; runtime mounting is unverified
        font_path = STEAM_LANG_DIR / FONT_REL_PATH
        self.assertTrue(font_path.exists(), "TextMeshPro font ChineseFont.ttf missing in Steam directory")
        self.assertEqual(font_path.stat().st_size, EXPECTED_FONT_SIZE)
        self.assertEqual(compute_sha256(font_path), EXPECTED_FONT_SHA256)

        # 4. Critical UI files loadable from Steam mod path
        critical_ui_files = ["MainUIText-a1c10p1.json", "BattlePass-a1c10.json", "Enemies-a1c10p1.json"]
        for fname in critical_ui_files:
            mod_file = STEAM_LANG_DIR / fname
            self.assertTrue(mod_file.exists(), f"Critical mod file missing from Steam deploy: {fname}")
            data = load_json(mod_file)
            self.assertIn("dataList", data)

    def test_scenario_end_to_end_game_session_asset_pipeline(self):
        """Tier 4.5: Complete session asset pipeline: Title UI -> BattlePass -> Stage -> Announcer -> Items -> Results."""
        session_files = [
            ("MainUIText-a1c10p1.json", "Title / System UI"),
            ("BattlePass-a1c10.json", "Season 8 Battle Pass"),
            ("StageNode-a1c10p1.json", "Chapter 10 Stage Map"),
            ("Announcer-a1c10p1.json", "Combat Announcers"),
            ("Items-a1c10p1.json", "Rewards & Inventory"),
            ("BattleResultHint-a1c10p1.json", "Post-battle hints"),
        ]

        for fname, desc in session_files:
            fpath = WORKSPACE_DIR / fname
            self.assertTrue(fpath.exists(), f"Session step failed, missing {desc}: {fname}")
            data = load_json(fpath)
            self.assertIn("dataList", data, f"Malformed dataList in {desc}: {fname}")
            self.assertGreater(len(data["dataList"]), 0, f"Empty dataList in {desc}: {fname}")


if __name__ == "__main__":
    unittest.main()
