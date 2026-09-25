# -*- coding: utf-8 -*-
import json, os, subprocess, sys

speaker_map = {
    "": "",
    "???": "???",
    "뫼르소": "默尔索",
    "리나모비블": "不可动摇者",
    "플라넬": "法兰绒",
    "투피스": "两件套",
    "오티스": "奥提斯",
    "단테": "但丁",
    "싱클레어": "辛克莱",
    "3층 플로어 매니저": "3F 楼层经理",
    "살갗 소파": "人皮沙发",
    "펠트": "毛毡",
    "수선사 아네트": "修补师阿内特",
}

import floor_3_b_part1 as p1
import floor_3_b_part2 as p2
import floor_3_b_part3 as p3
import floor_3_b_fix as fx

all_translations = {}
all_translations.update(p1.translations)
all_translations.update(p2.translations)
all_translations.update(p3.translations)
all_translations.update(fx.fixes)

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

with open('backups/part2-scope-20260924/source-kr/RPGSystem/rpg-loc-dialogue-floor-3-b.json', 'r', encoding='utf-8') as f:
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
        
        zh_text = all_translations.get((sp_kr, text_kr))
        if zh_text is None:
            zh_text = all_translations.get(('', text_kr))
            
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
    for m in missing[:10]:
        print(' ', m)
    sys.exit(1)

out_path = 'workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-3-b.json'
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
