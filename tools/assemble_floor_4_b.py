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

sys.path.insert(0, '.')
from tools.floor_4_b_dict_part1 import translations as t1
from tools.floor_4_b_dict_part2 import translations as t2
from tools.floor_4_b_dict_part3 import translations as t3
from tools.floor_4_b_dict_part4 import translations as t4

all_translations = {}
all_translations.update(t1)
all_translations.update(t2)
all_translations.update(t3)
all_translations.update(t4)

speaker_map = {
    '도로테아': '多萝西娅',
    '포레그': '四脚人',
    '원레그': '单脚人',
    '살갗 소파': '人皮沙发',
    '등굽은 조명': '驼背落地灯',
    '뼛걸이': '骨衣架',
    '박제된 가죽 커튼': '剥制皮窗帘',
    '행복한 옷장': '快乐衣橱',
    '쌍둥이 램프': '双子台灯',
    '빨간 방석 스툴': '红色软凳',
    '느긋한 가죽 침대': '舒服的皮床',
    '르누아르 가방관 디자이너': '黑派箱包馆设计师',
    '르루주 가방관 디자이너': '红派箱包馆设计师',
    '르네': '勒内',
    '디자이너의 걸작': '设计师的杰作',
    '돈키호테': '堂吉诃德',
    '홍루': '鸿璐',
    '뫼르소': '默尔索',
    '단테': '但丁',
    '뿌이': '普伊',
    '쁘우이': '普呜伊',
    '쁘…': '普……',
    '죽어가는 르누아르': '濒死的黑派',
    '???': '？？？'
}

src_file = 'backups/part2-scope-20260924/source-kr/RPGSystem/rpg-loc-dialogue-floor-4-b.json'
tgt_file = 'workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-4-b.json'

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
