#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase C: Game Update Watcher & Readiness Tool
监控 Steam 本地《边狱公司》客户端下载/更新状态，捕获最新版本资源落地时间戳与文件变动。
"""

import os
import sys
import time
import json

GAME_DIR = "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company"
LOCALIZE_KR_DIR = os.path.join(GAME_DIR, "LimbusCompany_Data", "Assets", "Resources_moved", "Localize", "kr")
SNAPSHOT_FILE = "/home/buxinzi/Documents/巴士汉化-哈基米版/tools/game_version_snapshot.json"

def get_dir_state(target_dir):
    state = {}
    if not os.path.exists(target_dir):
        return state
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, target_dir)
            try:
                st = os.stat(p)
                state[rel] = {
                    "mtime": st.st_mtime,
                    "size": st.st_size
                }
            except Exception:
                pass
    return state

def create_snapshot():
    print("=" * 70)
    print("【模块 C】创建本地游戏客户端资源版本快照...")
    print("=" * 70)

    if not os.path.exists(GAME_DIR):
        print(f"[ERROR] 找不到游戏目录: {GAME_DIR}")
        sys.exit(1)

    print(f"正在扫描韩文资源目录: {LOCALIZE_KR_DIR}")
    kr_state = get_dir_state(LOCALIZE_KR_DIR)

    snapshot_data = {
        "timestamp": time.time(),
        "human_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "game_dir": GAME_DIR,
        "total_kr_files": len(kr_state),
        "files": kr_state
    }

    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, ensure_ascii=False, indent=2)

    print(f"[OK] 版本基线快照已创建！")
    print(f"  - 记录时间:     {snapshot_data['human_time']}")
    print(f"  - 韩文文件总数: {snapshot_data['total_kr_files']} 个")
    print(f"  - 快照存储路径: {SNAPSHOT_FILE}")
    print("=" * 70)

def check_update():
    print("=" * 70)
    print("【模块 C】比对最新下载状态与版本快照...")
    print("=" * 70)

    if not os.path.exists(SNAPSHOT_FILE):
        print("[WARN] 未找到历史快照，正在自动创建基线快照...")
        create_snapshot()
        return

    with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
        old_snap = json.load(f)

    current_state = get_dir_state(LOCALIZE_KR_DIR)
    old_files = old_snap.get("files", {})

    new_files = []
    modified_files = []
    deleted_files = []

    for fpath, meta in current_state.items():
        if fpath not in old_files:
            new_files.append(fpath)
        else:
            if meta["mtime"] > old_files[fpath]["mtime"] or meta["size"] != old_files[fpath]["size"]:
                modified_files.append(fpath)

    for fpath in old_files:
        if fpath not in current_state:
            deleted_files.append(fpath)

    print(f"基准快照时间: {old_snap.get('human_time')}")
    print(f"当前文件总数: {len(current_state)} 个 (基准: {len(old_files)} 个)")
    print(f"  - 新增文件: {len(new_files)} 个")
    print(f"  - 变更文件: {len(modified_files)} 个")
    print(f"  - 减少文件: {len(deleted_files)} 个")

    if new_files or modified_files:
        print("\n[DETECTED] 检测到客户端已下载新数据！变动重点如下:")
        for nf in (new_files + modified_files)[:15]:
            print(f"  -> {nf}")
        print("\n提示：客户端下载就绪！可以立即触发 tools/diff_extractor.py 进行新赛季差分提取！")
    else:
        print("\n[STATUS] 本地文件与基线快照一致，当前暂未检测到 Steam 写入新版本文件（正在等待下载落盘完成）。")

    print("=" * 70)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        check_update()
    else:
        create_snapshot()
