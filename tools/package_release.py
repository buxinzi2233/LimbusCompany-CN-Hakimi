#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automation tool for packaging Limbus Company localization releases.
Generates two distinct distribution bundles:
1. Full Edition (完整版): Complete localization including Canto 10 story & RPG exploration.
2. Combat-Only Edition (仅战斗辅助版): Only combat mechanics & battle UI, omitting provisional
   Canto 10 story/exploration to allow game fallback to native text while players wait for LLC.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import zipfile

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WORKSPACE = PROJECT_ROOT / "workspace" / "LLC_zh-CN"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "dist"
FONT_RELATIVE = Path("Font/Context/ChineseFont.ttf")
EXPECTED_FONT_SHA256 = "a56a06f1af27726bc5def015b61deecbbdf5ae6d954a91b1131d8a17290def35"

# Story & dialogue files to exclude in Combat-Only edition
CANTO10_STORY_PATTERN = re.compile(r"^(S10[0-9]{2}[A-Z]|S999[1-9][A-Z]|P10[0-9]{3})\.json$")
CANTO10_VOICE_PATTERN = re.compile(r"^Voice_.*_10[0-9]{3}\.json$")

CONFIG_JSON_CONTENT = {
    "lang": "LLC_zh-CN",
    "titleFont": "",
    "contextFont": "",
    "samplingPointSize": 78,
    "padding": 5
}

LICENSE_TEXT = """Copyright (c) 2024 to now Localize Limbus Company & Community Contributors

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit.
- NonCommercial — You may not use the material for commercial purposes.
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
"""


def compute_sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compute_file_sha256(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def should_exclude_for_combat_only(rel_path: Path) -> bool:
    """Determine if a file should be excluded from the combat-only distribution."""
    parts = rel_path.parts
    filename = parts[-1]

    # Exclude Canto 10 story files (S1000B~S1062B, S9991B, P10416, etc.)
    if len(parts) == 2 and parts[0] == "StoryData":
        if CANTO10_STORY_PATTERN.match(filename):
            return True

    # Exclude RPG system story dialogue and narration (keep RPG UI and items/mechanics)
    if len(parts) == 2 and parts[0] == "RPGSystem":
        if filename.startswith("rpg-loc-dialogue-") or filename.startswith("rpg-loc-narration-"):
            return True

    # Exclude Canto 10 personality identity voice lines
    if len(parts) == 2 and parts[0] == "PersonalityVoiceDlg":
        if CANTO10_VOICE_PATTERN.match(filename):
            return True

    return False


def build_package(workspace: Path, output_zip: Path, version: str, edition: str) -> dict:
    """Build a distribution zip file following the game's native directory structure."""
    is_combat_only = (edition == "combat-only")
    prefix = "LimbusCompany_Data/Lang/LLC_zh-CN"

    output_zip.parent.mkdir(parents=True, exist_ok=True)
    if output_zip.exists():
        output_zip.unlink()

    included_count = 0
    excluded_count = 0

    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        # 1. Add LimbusCompany_Data/Lang/config.json
        config_data = json.dumps(CONFIG_JSON_CONTENT, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
        zf.writestr("LimbusCompany_Data/Lang/config.json", config_data)

        # 2. Add Info/LICENSE and Info/version.json
        version_info = {
            "version": version,
            "edition": edition,
            "notice": f"边狱公司汉化-哈基米版 ({'仅战斗辅助版' if is_combat_only else '完整汉化版'})",
            "canto10_story_included": not is_combat_only
        }
        zf.writestr(f"{prefix}/Info/LICENSE", LICENSE_TEXT.strip().encode("utf-8") + b"\n")
        zf.writestr(f"{prefix}/Info/version.json", json.dumps(version_info, ensure_ascii=False, indent=2).encode("utf-8") + b"\n")

        # 3. Add workspace files
        for p in sorted(workspace.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(workspace)

            if is_combat_only and should_exclude_for_combat_only(rel):
                excluded_count += 1
                continue

            archive_path = f"{prefix}/{rel.as_posix()}"
            zf.write(p, archive_path)
            included_count += 1

    file_size = output_zip.stat().st_size
    sha256 = compute_file_sha256(output_zip)

    return {
        "output_file": str(output_zip),
        "edition": edition,
        "included_files": included_count,
        "excluded_files": excluded_count,
        "size_bytes": file_size,
        "sha256": sha256
    }


def verify_package(zip_path: Path, edition: str) -> dict:
    """Verify the internal structure, font integrity, and JSON validity of a package."""
    is_combat_only = (edition == "combat-only")
    prefix = "LimbusCompany_Data/Lang/LLC_zh-CN"

    results = {
        "passed": True,
        "errors": [],
        "checked_files": 0,
        "json_valid_files": 0,
        "has_font": False,
        "has_config": False,
        "has_info": False,
        "canto10_story_files": 0,
        "canto10_combat_files": 0
    }

    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = set(zf.namelist())

        # Verify config.json
        if "LimbusCompany_Data/Lang/config.json" in namelist:
            results["has_config"] = True
            try:
                cfg = json.loads(zf.read("LimbusCompany_Data/Lang/config.json").decode("utf-8"))
                if cfg.get("lang") != "LLC_zh-CN":
                    results["errors"].append("config.json lang property is not 'LLC_zh-CN'")
            except Exception as e:
                results["errors"].append(f"config.json invalid: {e}")
        else:
            results["errors"].append("Missing LimbusCompany_Data/Lang/config.json")

        # Verify ChineseFont.ttf
        font_entry = f"{prefix}/Font/Context/ChineseFont.ttf"
        if font_entry in namelist:
            results["has_font"] = True
            font_bytes = zf.read(font_entry)
            font_sha = compute_sha256(font_bytes)
            if font_sha != EXPECTED_FONT_SHA256:
                results["errors"].append(f"Font SHA-256 mismatch: got {font_sha}, expected {EXPECTED_FONT_SHA256}")
        else:
            results["errors"].append(f"Missing font at {font_entry}")

        # Verify all JSON files and check edition contents
        for name in sorted(namelist):
            results["checked_files"] += 1
            if not name.startswith(prefix + "/"):
                continue

            rel_subpath = name[len(prefix) + 1:]

            # Check Canto 10 story files
            if rel_subpath.startswith("StoryData/"):
                fname = os.path.basename(rel_subpath)
                if CANTO10_STORY_PATTERN.match(fname):
                    results["canto10_story_files"] += 1

            # Check Canto 10 combat mechanics
            if any(k in rel_subpath for k in ["Skills_Enemy-a1c10p1", "Skills_Abnormality-a1c10p1",
                                             "Passives_Enemy-a1c10p1", "Passives_Abnormality-a1c10p1",
                                             "BattleKeywords-a1c10p1", "Bufs-a1c10p1", "Enemies-a1c10p1"]):
                results["canto10_combat_files"] += 1

            # Validate JSON
            if name.endswith(".json"):
                try:
                    data = zf.read(name)
                    json.loads(data.decode("utf-8-sig"))
                    results["json_valid_files"] += 1
                except Exception as e:
                    results["errors"].append(f"Invalid JSON in {name}: {e}")

        # Verify Edition specifics
        if is_combat_only:
            if results["canto10_story_files"] > 0:
                results["errors"].append(f"Combat-only edition must have 0 Canto 10 story files, found {results['canto10_story_files']}")
            if results["canto10_combat_files"] < 7:
                results["errors"].append(f"Combat-only edition missing key Canto 10 combat files: found {results['canto10_combat_files']}")
        else:
            if results["canto10_story_files"] < 20:
                results["errors"].append(f"Full edition missing Canto 10 story files, found only {results['canto10_story_files']}")
            if results["canto10_combat_files"] < 7:
                results["errors"].append(f"Full edition missing Canto 10 combat files: found {results['canto10_combat_files']}")

    if results["errors"]:
        results["passed"] = False

    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE,
                        help=f"Path to LLC_zh-CN workspace (default: {DEFAULT_WORKSPACE})")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                        help=f"Output directory for distribution archives (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--version", type=str, default="2026.09.18",
                        help="Version identifier (default: 2026.09.18)")
    parser.add_argument("--verify-only", action="store_true",
                        help="Only verify existing archives without rebuilding")
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    output_dir = args.output_dir.resolve()
    version = args.version

    if not (workspace / FONT_RELATIVE).is_file():
        print(f"[ERROR] Font missing in workspace: {workspace / FONT_RELATIVE}", file=sys.stderr)
        return 1

    full_zip = output_dir / f"LLC_zh-CN-Full-v{version}.zip"
    combat_zip = output_dir / f"LLC_zh-CN-CombatOnly-v{version}.zip"

    print("=" * 65)
    print("【边狱公司汉化-哈基米版】发布安装包自动化构建与校验系统")
    print(f"版本: v{version}")
    print(f"工作区: {workspace}")
    print(f"输出目录: {output_dir}")
    print("=" * 65)

    if not args.verify_only:
        print(f"\n[1/4] 正在构建【完整版】(Full Edition)...")
        res_full = build_package(workspace, full_zip, version, "full")
        print(f"  - 文件数: 包含 {res_full['included_files']} 个文件")
        print(f"  - 大小:   {res_full['size_bytes'] / (1024 * 1024):.2f} MB")
        print(f"  - SHA256: {res_full['sha256']}")

        print(f"\n[2/4] 正在构建【仅战斗辅助版】(Combat-Only Edition)...")
        res_combat = build_package(workspace, combat_zip, version, "combat-only")
        print(f"  - 文件数: 包含 {res_combat['included_files']} 个文件 (已排除 {res_combat['excluded_files']} 个第10章临时剧情/对话文件)")
        print(f"  - 大小:   {res_combat['size_bytes'] / (1024 * 1024):.2f} MB")
        print(f"  - SHA256: {res_combat['sha256']}")

        # Write SHA256SUMS.txt
        sums_file = output_dir / "SHA256SUMS.txt"
        sums_content = f"{res_full['sha256']}  {full_zip.name}\n{res_combat['sha256']}  {combat_zip.name}\n"
        sums_file.write_text(sums_content, encoding="utf-8")
        print(f"\n[3/4] 已生成校验清单: {sums_file}")

    print(f"\n[4/4] 正在对分发包执行严格完整性验证...")
    v_full = verify_package(full_zip, "full")
    v_combat = verify_package(combat_zip, "combat-only")

    all_passed = True
    print(f"  - 【完整版】验证: {'PASSED' if v_full['passed'] else 'FAILED'}")
    if not v_full['passed']:
        all_passed = False
        for err in v_full['errors']:
            print(f"    [FAIL] {err}")
    else:
        print(f"    (检查文件 {v_full['checked_files']} 个，有效 JSON {v_full['json_valid_files']} 个，含第10章剧情 {v_full['canto10_story_files']} 个)")

    print(f"  - 【仅战斗辅助版】验证: {'PASSED' if v_combat['passed'] else 'FAILED'}")
    if not v_combat['passed']:
        all_passed = False
        for err in v_combat['errors']:
            print(f"    [FAIL] {err}")
    else:
        print(f"    (检查文件 {v_combat['checked_files']} 个，有效 JSON {v_combat['json_valid_files']} 个，第10章临时剧情 0 个，保留战斗机制 {v_combat['canto10_combat_files']} 项)")

    if all_passed:
        print("\n" + "=" * 65)
        print(" [SUCCESS] 全部双版本安装包构建与校验 100% 成功！")
        print(f" 完整版路径:     {full_zip}")
        print(f" 仅战斗辅助版:   {combat_zip}")
        print("=" * 65)
        return 0
    else:
        print("\n [ERROR] 分发包完整性校验失败，请检查报错！", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
