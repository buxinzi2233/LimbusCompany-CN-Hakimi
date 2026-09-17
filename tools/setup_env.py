#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 1: Environment and Base Localization Setup Tool
遵循月亮计划原生自定义语言接口规范及都市零协会发布标准。
"""

import os
import shutil
import sys

GAME_DIR = "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company"
GAME_LANG_DIR = os.path.join(GAME_DIR, "LimbusCompany_Data", "Lang", "LLC_zh-CN")
REPO_SRC_DIR = "/tmp/llc_repo/LLC_zh-CN"
REPO_FONT_SRC = "/tmp/llc_repo/Fonts/ChineseFont.ttf"

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKSPACE_LLC = os.path.join(PROJECT_ROOT, "workspace", "LLC_zh-CN")
WORKSPACE_FONT = os.path.join(WORKSPACE_LLC, "Font", "Context", "ChineseFont.ttf")

def setup():
    print("=" * 60)
    print("【阶段 1】初始化本地汉化环境与基准包同步")
    print("=" * 60)

    if not os.path.exists(GAME_DIR):
        print(f"[ERROR] 游戏目录未找到: {GAME_DIR}")
        sys.exit(1)
    print(f"[OK] 发现游戏安装目录: {GAME_DIR}")

    # 1. 拷贝仓库 JSON 资源到 workspace
    if os.path.exists(REPO_SRC_DIR):
        print(f"[INFO] 正在从基准仓库 {REPO_SRC_DIR} 同步文件至工作空间...")
        for item in os.listdir(REPO_SRC_DIR):
            s = os.path.join(REPO_SRC_DIR, item)
            d = os.path.join(WORKSPACE_LLC, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print(f"[OK] 工作空间 JSON 资源同步完成。")
    else:
        print(f"[ERROR] 基准仓库不存在: {REPO_SRC_DIR}")
        sys.exit(1)

    # 2. 拷贝字体到 workspace/LLC_zh-CN/Font/Context/ChineseFont.ttf
    os.makedirs(os.path.dirname(WORKSPACE_FONT), exist_ok=True)
    if os.path.exists(REPO_FONT_SRC):
        print(f"[INFO] 正在同步字体文件至工作空间: {WORKSPACE_FONT}")
        shutil.copy2(REPO_FONT_SRC, WORKSPACE_FONT)
        print(f"[OK] 字体文件同步完成 (大小: {os.path.getsize(WORKSPACE_FONT)} 字节)")
    else:
        print(f"[ERROR] 字体文件未找到: {REPO_FONT_SRC}")
        sys.exit(1)

    # 3. 部署至游戏目录 Lang/LLC_zh-CN
    print(f"[INFO] 正在向游戏本地目录部署汉化包: {GAME_LANG_DIR}")
    os.makedirs(os.path.dirname(GAME_LANG_DIR), exist_ok=True)
    if os.path.exists(GAME_LANG_DIR):
        shutil.rmtree(GAME_LANG_DIR)
    shutil.copytree(WORKSPACE_LLC, GAME_LANG_DIR)
    print(f"[OK] 游戏本地目录部署完成！")

    # 4. 校验结构
    font_in_game = os.path.join(GAME_LANG_DIR, "Font", "Context", "ChineseFont.ttf")
    if os.path.exists(font_in_game) and os.path.getsize(font_in_game) > 10 * 1024 * 1024:
        print(f"[SUCCESS] 阶段 1 验证通过！游戏原生多语言接口已就绪。")
        print(f"  - 汉化根路径: {GAME_LANG_DIR}")
        print(f"  - 字体路径:   {font_in_game}")
        print(f"  - 语言标识:   LLC_zh-CN (启动游戏后可在标题界面切换)")
    else:
        print(f"[FAILED] 字体文件校验失败！")
        sys.exit(1)

if __name__ == "__main__":
    setup()
