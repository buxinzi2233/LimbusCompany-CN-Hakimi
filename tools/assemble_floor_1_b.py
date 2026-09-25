# -*- coding: utf-8 -*-
import json, os, subprocess, sys

speaker_map = {
    "": "",
    "그레고르": "格里高尔",
    "크로머": "克罗默",
    "절박한 고객": "迫切的顾客",
    "돈키호테": "唐吉诃德",
    "파우스트": "浮士德",
    "뿌이": "普伊",
    "로쟈": "罗佳",
    "궁핍한 고객": "困窘的顾客",
    "퀼리안": "奎利安",
    "뫼르소": "默尔索",
    "히스클리프": "希斯克利夫",
    "구경 중인 고객": "围观的顾客",
    "미모사": "含羞草",
    "???": "???",
    "단테": "但丁",
    "이스마엘": "以实玛利",
    "이상": "李箱",
    "홍루": "鸿芦",
    "구스타프": "古斯塔夫",
    "가죽 장갑": "真皮手套",
    "뒤부아": "杜布瓦",
    "오티스": "奥提斯",
    "료슈": "良秀",
    "시술 받는 고객": "手术中的顾客",
    "초조한 고객": "焦急的顾客"
}

import floor_1_b_dict as d1

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

with open('backups/part2-scope-20260924/source-kr/RPGSystem/rpg-loc-dialogue-floor-1-b.json', 'r', encoding='utf-8') as f:
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
        
        # 1. check floor_1_b_dict
        zh_text = d1.translations.get((sp_kr, text_kr))
        if zh_text is None:
            zh_text = d1.translations.get(('', text_kr))
            
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
    for m in missing[:10]:
        print(' ', m)
    sys.exit(1)

out_path = 'workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-1-b.json'
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
