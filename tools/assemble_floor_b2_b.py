# -*- coding: utf-8 -*-
import json, os, subprocess, sys

speaker_map = {
    "": "",
    "네이키드": "裸体",
    "탐욕스런 바늘이": "贪婪的针族",
    "바늘이 노동자2": "针族工人2",
    "오티스": "奥提斯",
    "고치": "茧",
    "르누아르 간부": "黑派干部",
    "뫼르소": "默尔索",
    "바늘이 노동자": "针族工人",
    "싱클레어": "辛克莱",
    "퍼티": "油灰",
    "뿌이": "普伊",
    "팔레트": "调色板",
    "바느질의 왕": "裁缝之王",
    "소란스러운 바늘이": "喧闹的针族",
    "료슈": "良秀",
    "줄 선 바늘이": "排队的针族",
    "시끄러운 바늘이": "吵闹的针族",
    "일하는 바늘이": "工作的针族",
    "르누아르 경비원": "黑派警卫",
    "지하 2층 플로어 매니저": "B2F 楼层经理",
    "단테": "但丁",
    "르누아르 스태프 매니저": "黑派员工经理",
}

import b2_b_trans as p1
import b2_b_trans_part2 as p2
import b2_b_trans_part3 as p3

all_translations = {}
all_translations.update(p1.translations)
all_translations.update(p2.translations)
all_translations.update(p3.translations)

# Load global memory for pre-existing matched lines
global_memory = {}
def walk_and_load(zh_root, kr_root):
    for root, dirs, files in os.walk(zh_root):
        for f in files:
            if not f.endswith('.json'): continue
            zh_file = os.path.join(root, f)
            rel_path = os.path.relpath(zh_file, zh_root)
            kr_file = os.path.join(kr_root, rel_path)
            if not os.path.exists(kr_file): continue
            try:
                with open(zh_file, 'r', encoding='utf-8') as fz, open(kr_file, 'r', encoding='utf-8') as fk:
                    zd = json.load(fz)
                    kd = json.load(fk)
                if isinstance(zd, dict) and 'dataList' in zd and isinstance(kd, dict) and 'dataList' in kd:
                    for zk_item, kr_item in zip(zd['dataList'], kd['dataList']):
                        if 'texts' in zk_item and 'texts' in kr_item:
                            for tz, tk in zip(zk_item['texts'], kr_item['texts']):
                                if 'text' in tk and 'text' in tz and tk['text'] and tz['text']:
                                    global_memory[(tk.get('speaker', ''), tk['text'])] = (tz.get('speaker', ''), tz['text'])
                                    global_memory[('', tk['text'])] = (tz.get('speaker', ''), tz['text'])
            except:
                pass
walk_and_load('workspace/LLC_zh-CN', 'backups/part2-scope-20260924/source-kr')

with open('backups/part2-scope-20260924/source-kr/RPGSystem/rpg-loc-dialogue-floor-b2-b.json', 'r', encoding='utf-8') as f:
    kr_data = json.load(f)

zh_dataList = []
missing = []

for item in kr_data.get('dataList', []):
    key = item['key']
    zh_texts = []
    for d in item.get('texts', []):
        idx = d.get('index')
        sp_kr = d.get('speaker', '')
        text_kr = d.get('text', '')
        
        # 1. check all_translations
        zh_text = all_translations.get((sp_kr, text_kr))
        if zh_text is None:
            zh_text = all_translations.get(('', text_kr))
            
        # 2. check global_memory
        if zh_text is None:
            if (sp_kr, text_kr) in global_memory:
                zh_text = global_memory[(sp_kr, text_kr)][1]
            elif ('', text_kr) in global_memory:
                zh_text = global_memory[('', text_kr)][1]
                
        if zh_text is None:
            missing.append((key, sp_kr, text_kr))
            zh_text = text_kr
            
        entry = {'index': idx, 'text': zh_text}
        if sp_kr:
            entry['speaker'] = speaker_map.get(sp_kr, sp_kr)
        zh_texts.append(entry)
    zh_dataList.append({'key': key, 'texts': zh_texts})

if missing:
    print(f'MISSING {len(missing)} translations:')
    for m in missing:
        print(' ', m)
    sys.exit(1)

out_path = 'workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-b2-b.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({'dataList': zh_dataList}, f, ensure_ascii=False, indent=2)

print(f'Successfully generated {out_path}!')
res = subprocess.run(['python3', 'tools/linter.py', '--target', out_path, '--source-dir', 'backups/part2-scope-20260924/source-kr', '--check-korean'], capture_output=True, text=True)
print(res.stdout)
if res.returncode != 0:
    print(res.stderr)
    sys.exit(res.returncode)
else:
    print('PASS 0 ERRORS!')
