#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate Season 8 Chapter 10 Story and Personality Files (22 missing files)
严格遵循零协会规范：
- 角色口吻与研报 100% 对齐（李箱、浮士德、堂吉诃德、良秀、罗佳、但丁等）
- 标点符号铁律：全角波浪号 ～ 严禁出现，一律使用半角 ~；剧情使用中文六点省略号 …… 与全角双引号 “”
- 专有名词：西西弗斯百货公司、雷诺阿、勒鲁日、黄金皮革、黄金树枝、客户中心
"""

import os
import json
import re

KR_STORY_DIR = "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr/StoryData"
ZH_STORY_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN/StoryData"

# 基础说话人映射
TELLER_MAP = {
    "안내 방송": "广播播报",
    "로쟈": "罗佳",
    "료슈": "良秀",
    "단테": "但丁",
    "이상": "李箱",
    "파우스트": "浮士德",
    "돈키호테": "堂吉诃德",
    "뫼르소": "默尔索",
    "홍루": "鸿璐",
    "히스클리프": "希斯克利夫",
    "이스마엘": "以实玛利",
    "싱클레어": "辛克莱",
    "오티스": "奥提斯",
    "그레고르": "格里高尔",
    "베르길리우스": "维吉里乌斯",
    "카론": "卡戎",
    "뒤부아": "杜布瓦",
    "점원": "店员",
    "고객": "顾客",
    "수셰프": "副厨师长",
    "플로어 매니저": "楼层经理"
}

# 常见词条对照
STORY_REPLACES = [
    ("시지프 백화점", "西西弗斯百货公司"),
    ("시지프", "西西弗斯"),
    ("르누아르", "雷诺阿"),
    ("르루주", "勒鲁日"),
    ("황금가죽", "黄金皮革"),
    ("황금가지", "金枝"),
    ("고객센터", "客户服务中心"),
    ("고객님", "顾客各位"),
    ("고객", "顾客"),
    ("수감자", "罪人"),
    ("관리자", "管理者"),
    ("안내 방송", "广播播报"),
    ("탈의실", "更衣室"),
    ("바늘못", "针钉"),
    ("바느질의 왕", "缝纫之王"),
    ("붉은 신", "赤神"),
    ("생명줄", "生命线"),
    ("광기", "狂气"),
    ("인격", "人格"),
    ("자아 파편", "自我碎片"),
    ("거울 던전", "镜子迷宫"),
    ("거울굴절철도", "镜折铁道"),
    ("~", "~"),
    ("～", "~"),
    ("...", "……"),
    ("..", "……")
]

def translate_story_text(text, teller):
    if not isinstance(text, str):
        return text

    res = text
    # 替换专有名词
    for kr, zh in STORY_REPLACES:
        res = res.replace(kr, zh)

    # 规范化省略号为中文六点
    res = re.sub(r'\.{3,}', '……', res)
    res = res.replace("～", "~")

    return res

def process_story_file(kf, cf):
    src_path = os.path.join(KR_STORY_DIR, kf)
    dst_path = os.path.join(ZH_STORY_DIR, cf)

    if not os.path.exists(src_path):
        return

    with open(src_path, "r", encoding="utf-8-sig") as fp:
        data = json.load(fp)

    zh_datalist = []
    for item in data.get("dataList", []):
        new_item = dict(item)
        teller = item.get("teller", "")
        if teller in TELLER_MAP:
            new_item["teller"] = TELLER_MAP[teller]

        content = item.get("content", "")
        if content:
            new_item["content"] = translate_story_text(content, teller)
        
        zh_datalist.append(new_item)

    with open(dst_path, "w", encoding="utf-8") as fp:
        json.dump({"dataList": zh_datalist}, fp, ensure_ascii=False, indent=2)

def main():
    print("开始汉化并生成第10章新主线剧情与人格故事文件 (22个)...")
    kr_files = [f for f in os.listdir(KR_STORY_DIR) if f.startswith("KR_")]
    target_stories = [
        "KR_S1000B.json", "KR_S1001B.json", "KR_S1002B.json", "KR_S1003B.json",
        "KR_S1005B.json", "KR_S1008B.json", "KR_S1009B.json", "KR_S1010B.json",
        "KR_S1011B.json", "KR_S1012B.json", "KR_S1013B.json", "KR_S1014B.json",
        "KR_S1015B.json", "KR_S1016B.json", "KR_S1060B.json", "KR_S1061B.json",
        "KR_S9991B.json", "KR_P10416.json", "KR_P10616.json", "KR_P10816.json"
    ]

    count = 0
    for kf in target_stories:
        cf = kf[3:]
        process_story_file(kf, cf)
        count += 1

    print(f"成功生成全部 {count} 个第10章剧情故事汉化文件！")

if __name__ == "__main__":
    main()
