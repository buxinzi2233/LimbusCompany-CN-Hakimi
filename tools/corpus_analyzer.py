#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced In-Game Corpus Analyzer for Limbus Company
基于真实游戏资产逆向，联合检测 teller、title 与 model (立绘模型标签)，
全面覆盖 921 篇主线剧情与 186 个人格语音对话文件。
"""

import os
import json
import re
from collections import Counter

STORY_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN/StoryData"
VOICE_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN/PersonalityVoiceDlg"
OUTPUT_CORPUS_JSON = "/home/buxinzi/Documents/巴士汉化-哈基米版/tools/corpus_stats.json"

CHARACTER_SPECS = {
    "李箱": {
        "models": ["이상", "yisang", "YiSang"],
        "tellers": ["李箱"],
        "voice_prefix": ["voice_yisang"]
    },
    "浮士德": {
        "models": ["파우스트", "faust", "Faust"],
        "tellers": ["浮士德"],
        "voice_prefix": ["voice_faust"]
    },
    "堂吉诃德": {
        "models": ["돈키호테", "donquixote", "DonQuixote"],
        "tellers": ["堂吉诃德", "桑丘"],
        "voice_prefix": ["voice_donquixote"]
    },
    "良秀": {
        "models": ["료슈", "ryoshu", "Ryoshu"],
        "tellers": ["良秀"],
        "voice_prefix": ["voice_ryoshu"]
    },
    "默尔索": {
        "models": ["뫼르소", "meursault", "Meursault"],
        "tellers": ["默尔索"],
        "voice_prefix": ["voice_meursault"]
    },
    "鸿璐": {
        "models": ["홍루", "honglu", "HongLu"],
        "tellers": ["鸿璐", "鸿潞"],
        "voice_prefix": ["voice_honglu"]
    },
    "希斯克利夫": {
        "models": ["히스클리프", "heathcliff", "Heathcliff"],
        "tellers": ["希斯克利夫"],
        "voice_prefix": ["voice_heathcliff"]
    },
    "以实玛利": {
        "models": ["이스마엘", "ishmael", "Ishmael"],
        "tellers": ["以实玛利"],
        "voice_prefix": ["voice_ishmael"]
    },
    "罗佳": {
        "models": ["로쟈", "rodion", "Rodion", "rodya"],
        "tellers": ["罗佳"],
        "voice_prefix": ["voice_rodion"]
    },
    "辛克莱": {
        "models": ["싱클레어", "sinclair", "Sinclair"],
        "tellers": ["辛克莱"],
        "voice_prefix": ["voice_sinclair"]
    },
    "奥提斯": {
        "models": ["오티스", "outis", "Outis"],
        "tellers": ["奥提斯"],
        "voice_prefix": ["voice_outis"]
    },
    "格里高尔": {
        "models": ["그레고르", "gregor", "Gregor"],
        "tellers": ["格里高尔"],
        "voice_prefix": ["voice_gregor"]
    },
    "但丁": {
        "models": ["단테", "dante", "Dante"],
        "tellers": ["但丁", "管理者"],
        "voice_prefix": ["voice_dante"]
    },
    "维吉里乌斯": {
        "models": ["베르길리우스", "vergilius", "Vergilius"],
        "tellers": ["维吉里乌斯", "向导"],
        "voice_prefix": ["voice_vergilius"]
    },
    "卡戎": {
        "models": ["카론", "charon", "Charon"],
        "tellers": ["卡戎"],
        "voice_prefix": ["voice_charon"]
    }
}

def analyze():
    print("=" * 70)
    print("【模块 A】启动高精度实机语料全量逆向分析 (Model + Teller 联合判定)...")
    print("=" * 70)

    stats = {
        name: {
            "story_line_count": 0,
            "voice_line_count": 0,
            "sample_lines": [],
            "keywords": Counter(),
            "pronouns": Counter(),
            "endings": Counter()
        }
        for name in CHARACTER_SPECS
    }

    # 1. 扫描剧情
    story_files = [f for f in os.listdir(STORY_DIR) if f.endswith(".json")]
    for sf in story_files:
        p = os.path.join(STORY_DIR, sf)
        try:
            with open(p, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except Exception:
            continue

        for entry in data.get("dataList", []):
            teller = str(entry.get("teller", "") or entry.get("title", "") or "")
            model = str(entry.get("model", "") or "")
            content = str(entry.get("content", "") or "")
            dialog_id = entry.get("id", "")

            if not content.strip():
                continue

            matched = None
            for char_name, spec in CHARACTER_SPECS.items():
                if any(t in teller for t in spec["tellers"]) or any(m.lower() in model.lower() for m in spec["models"]):
                    matched = char_name
                    break

            if matched:
                st = stats[matched]
                st["story_line_count"] += 1
                if len(st["sample_lines"]) < 8:
                    st["sample_lines"].append({
                        "source": f"StoryData/{sf}",
                        "id": dialog_id,
                        "teller": teller if teller else f"[{model}]",
                        "text": content
                    })

                # 收集结尾符号
                tail = content.strip()[-1:]
                if tail in ["。", "！", "？", "~", "…"]:
                    st["endings"][tail] += 1

                # 收集标志代词与口吻
                for p_check in ["我", "吾", "浮士德", "本官", "下官", "老子", "经理兄", "管理者", "老爷", "钟表头", "布隆布隆", "女士", "先生", "小姐", "姐姐我", "大叔"]:
                    if p_check in content:
                        st["pronouns"][p_check] += 1

    # 2. 扫描人格语音
    if os.path.exists(VOICE_DIR):
        voice_files = [f for f in os.listdir(VOICE_DIR) if f.endswith(".json")]
        for vf in voice_files:
            p = os.path.join(VOICE_DIR, vf)
            try:
                with open(p, "r", encoding="utf-8-sig") as f:
                    data = json.load(f)
            except Exception:
                continue

            matched = None
            for char_name, spec in CHARACTER_SPECS.items():
                if any(pfx in vf.lower() for pfx in spec["voice_prefix"]):
                    matched = char_name
                    break

            if matched:
                st = stats[matched]
                for entry in data.get("dataList", []):
                    desc = entry.get("desc", "") or entry.get("dlg", "")
                    if not desc:
                        continue
                    st["voice_line_count"] += 1
                    if len(st["sample_lines"]) < 12:
                        st["sample_lines"].append({
                            "source": f"PersonalityVoiceDlg/{vf}",
                            "id": entry.get("id", ""),
                            "teller": f"{matched}人格",
                            "text": desc
                        })

    print("\n高精度实机语料全景统计:")
    output_data = {}
    for name, data in stats.items():
        total_lines = data["story_line_count"] + data["voice_line_count"]
        top_p = dict(data["pronouns"].most_common(4))
        top_e = dict(data["endings"].most_common(3))
        print(f"  - [{name:^6}] 剧情台词: {data['story_line_count']:>5} 句 | 人格台词: {data['voice_line_count']:>4} 句 | 总计: {total_lines:>5} 句 | 标志代词: {top_p} | 标点分布: {top_e}")
        output_data[name] = {
            "total_lines": total_lines,
            "story_line_count": data["story_line_count"],
            "voice_line_count": data["voice_line_count"],
            "top_pronouns": top_p,
            "top_endings": top_e,
            "sample_lines": data["sample_lines"]
        }

    with open(OUTPUT_CORPUS_JSON, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n[OK] 完整实机语料库统计已保存至: {OUTPUT_CORPUS_JSON}")
    print("=" * 70)

if __name__ == "__main__":
    analyze()
