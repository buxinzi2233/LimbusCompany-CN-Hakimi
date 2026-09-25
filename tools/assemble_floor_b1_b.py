# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

# Build global memory from workspace/LLC_zh-CN
global_mem_exact = {}
global_mem_text = {}

for fpath in glob.glob('workspace/LLC_zh-CN/**/*.json', recursive=True):
    try:
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        continue
    kr_path = fpath.replace('workspace/LLC_zh-CN/', 'backups/part2-scope-20260924/source-kr/')
    try:
        with open(kr_path, encoding='utf-8') as f:
            kr_data = json.load(f)
    except Exception:
        continue
    if isinstance(data, dict) and 'dataList' in data and isinstance(kr_data, dict) and 'dataList' in kr_data:
        for k_item, z_item in zip(kr_data['dataList'], data['dataList']):
            if 'texts' in k_item and 'texts' in z_item:
                for kt, zt in zip(k_item['texts'], z_item['texts']):
                    ks = kt.get('speaker', '')
                    ktx = kt.get('text', '')
                    ztx = zt.get('text', '')
                    if ktx and ztx:
                        global_mem_exact[(ks, ktx)] = ztx
                        global_mem_text[ktx] = ztx

from tools.floor_b1_b_dict_part1 import translations as t1
from tools.floor_b1_b_dict_part2 import translations as t2
from tools.floor_b1_b_dict_part3 import translations as t3

all_translations = {}
all_translations.update(t1)
all_translations.update(t2)
all_translations.update(t3)

extra_dict = {
    ('단테', '<…….>'): '<……>',
    ('수셰프', '…?'): '……？',
    ('뿌이', '…….'): '……',
    ('뫼르소', '그래.'): '好。',
    ('부셰', '…….'): '……',
    ('파우스트', '그럴지도요.'): '或许如此。',
    ('파우스트', '…?'): '……？',
    ('뫼르소', '…그렇군요.'): '……原来如此。',
    ('부셰', '…?'): '……？',
    ('단테', '<음…>'): '<唔……>',
    ('수셰프', '킁킁…'): '嗅嗅……',
    ('수셰프', '…!'): '……！',
    ('뿌이', '…왜?'): '……为什么？',
    ('뫼르소', '예.'): '是。',
}
all_translations.update(extra_dict)

speaker_map = {
    '배고픈 르카키': '饥饿的褐派',
    '수셰프': '副主厨',
    '낚시꾼': '渔夫',
    '르루주 운반자': '红派搬运工',
    '뫼르소': '默尔索',
    '파우스트': '浮士德',
    '르누아르 운반자': '黑派搬运工',
    '그레고르': '格里高尔',
    '부셰': '屠夫',
    '뿌이': '普伊',
    '???': '？？？',
    '목마른 르카키': '干渴的褐派',
    '단테': '但丁'
}

src_file = 'backups/part2-scope-20260924/source-kr/RPGSystem/rpg-loc-dialogue-floor-b1-b.json'
tgt_file = 'workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-b1-b.json'

with open(src_file, 'r', encoding='utf-8') as f:
    kr_data = json.load(f)

zh_data = {'dataList': []}

untranslated = []

for item in kr_data['dataList']:
    new_item = {'key': item['key'], 'texts': []}
    for t in item['texts']:
        new_t = {'index': t['index']}
        ks = t.get('speaker', '')
        ktx = t.get('text', '')
        
        # Translate speaker
        if 'speaker' in t:
            if ks in speaker_map:
                new_t['speaker'] = speaker_map[ks]
            else:
                new_t['speaker'] = ks
        
        # Translate text
        zh_text = None
        key = (ks, ktx)
        if key in all_translations:
            zh_text = all_translations[key]
        elif key in global_mem_exact:
            zh_text = global_mem_exact[key]
        elif ktx in global_mem_text:
            zh_text = global_mem_text[ktx]
        
        if zh_text is None:
            untranslated.append((item['key'], ks, ktx))
            zh_text = ktx
        
        new_t['text'] = zh_text
        new_item['texts'].append(new_t)
    zh_data['dataList'].append(new_item)

if untranslated:
    print(f'ERROR: {len(untranslated)} texts untranslated!')
    for u in untranslated:
        print(u)
    sys.exit(1)

os.makedirs(os.path.dirname(tgt_file), exist_ok=True)
with open(tgt_file, 'w', encoding='utf-8') as f:
    json.dump(zh_data, f, ensure_ascii=False, indent=2)

print(f'Successfully assembled {tgt_file} with {len(zh_data["dataList"])} items.')
