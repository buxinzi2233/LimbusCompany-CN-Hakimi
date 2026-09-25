#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Game localization switcher for Limbus Company.

Supported states:
  - baseline: Official 零协会 baseline (chapters 1~9 localized, new season untranslated)
  - hakimi:   Our new season Hakimi localization (full a1c10p1 + polish)
  - vanilla:  Completely clean unmodded game (Lang folder disabled)
  - status:   Display current game localization state
"""

import argparse
import os
import shutil
import sys
import json

GAME_DATA = '/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data'
LANG_DIR = os.path.join(GAME_DATA, 'Lang')
LANG_DISABLED = os.path.join(GAME_DATA, 'Lang.disabled')
WORKSPACE = '/home/buxinzi/Documents/巴士汉化-哈基米版'
HAKIMI_BACKUP = os.path.join(WORKSPACE, 'backups/game-lang-hakimi-new-snapshot')
BASELINE_REF = os.path.join(WORKSPACE, 'references/LLC-2026090501/LimbusCompany_Data/Lang/LLC_zh-CN')
FONT_SRC = os.path.join(WORKSPACE, 'workspace/LLC_zh-CN/Font')


def get_status() -> str:
    if os.path.isdir(LANG_DISABLED) and not os.path.exists(LANG_DIR):
        return 'vanilla (Lang disabled)'
    if not os.path.exists(LANG_DIR):
        return 'vanilla (No Lang directory)'
    llc_dir = os.path.join(LANG_DIR, 'LLC_zh-CN')
    if not os.path.exists(llc_dir):
        return 'custom (Lang exists but LLC_zh-CN missing)'
    s1000 = os.path.join(llc_dir, 'StoryData/S1000B.json')
    if os.path.exists(s1000):
        return 'hakimi (New season a1c10p1 localization active)'
    return 'baseline (Official 零协会 baseline active)'


def switch_to_vanilla():
    if os.path.exists(LANG_DIR):
        if os.path.exists(LANG_DISABLED):
            shutil.rmtree(LANG_DISABLED)
        shutil.move(LANG_DIR, LANG_DISABLED)
        print('Switched to VANILLA: Lang moved to Lang.disabled')
    elif os.path.exists(LANG_DISABLED):
        print('Already in VANILLA: Lang is disabled.')
    else:
        print('Already in VANILLA: No Lang directory found.')


def switch_to_baseline():
    if os.path.exists(LANG_DISABLED) and not os.path.exists(LANG_DIR):
        os.rename(LANG_DISABLED, LANG_DIR)
    if os.path.exists(LANG_DIR):
        shutil.rmtree(LANG_DIR)
    os.makedirs(LANG_DIR, exist_ok=True)
    temp_llc = os.path.join(LANG_DIR, 'LLC_zh-CN')
    shutil.copytree(BASELINE_REF, temp_llc)
    shutil.copytree(FONT_SRC, os.path.join(temp_llc, 'Font'))
    config_data = {
        'lang': 'LLC_zh-CN',
        'titleFont': '',
        'contextFont': '',
        'samplingPointSize': 78,
        'padding': 5
    }
    with open(os.path.join(LANG_DIR, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('Switched to BASELINE: Official 零协会 baseline restored.')


def switch_to_hakimi():
    if os.path.exists(LANG_DISABLED) and not os.path.exists(LANG_DIR):
        os.rename(LANG_DISABLED, LANG_DIR)
    if os.path.exists(LANG_DIR):
        shutil.rmtree(LANG_DIR)
    os.makedirs(LANG_DIR, exist_ok=True)
    target_llc = os.path.join(LANG_DIR, 'LLC_zh-CN')
    shutil.copytree(os.path.join(WORKSPACE, 'workspace/LLC_zh-CN'), target_llc)
    config_data = {
        'lang': 'LLC_zh-CN',
        'titleFont': '',
        'contextFont': '',
        'samplingPointSize': 78,
        'padding': 5
    }
    with open(os.path.join(LANG_DIR, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    if os.path.exists(HAKIMI_BACKUP):
        shutil.rmtree(HAKIMI_BACKUP)
    shutil.copytree(LANG_DIR, HAKIMI_BACKUP)
    print('Switched to HAKIMI: New season Hakimi localization deployed from workspace.')


def main():
    parser = argparse.ArgumentParser(description='Manage game localization state')
    parser.add_argument('action', choices=['status', 'baseline', 'hakimi', 'vanilla'],
                        help='Action to perform')
    args = parser.parse_args()

    if args.action == 'status':
        print(f'Current state: {get_status()}')
    elif args.action == 'baseline':
        switch_to_baseline()
        print(f'Current state: {get_status()}')
    elif args.action == 'hakimi':
        switch_to_hakimi()
        print(f'Current state: {get_status()}')
    elif args.action == 'vanilla':
        switch_to_vanilla()
        print(f'Current state: {get_status()}')


if __name__ == '__main__':
    main()
