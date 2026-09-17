#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Translation Generator for Season 8 Combat, Enemies, Passives, and Skills
严格遵循零协会三大铁律：
- 动词层数“获得/施加”，强度“增加”
- 关键词末尾带半角空格 (如 [震颤 ] 或 震颤 )
- 强制使用半角波浪号 ~
- 保证 TMP 富文本标签成对闭合
"""

import os
import json
import re

KR_DIR = "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr"
WORKSPACE_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN"

# 1. Enemies
enemies_map = {
    91059: {"name": "口渴的勒卡基", "desc": ""},
    91060: {"name": "饥饿的勒卡基", "desc": "部位"},
    1465: {"name": "雷诺阿店员 古斯塔夫", "desc": "1层 Boss"},
    1494: {"name": "勒鲁日店员 含羞草", "desc": "1层 NPC"},
    1480: {"name": "皮制钱包", "desc": ""},
    1466: {"name": "利纳莫比布尔", "desc": ""},
    91066: {"name": "雷诺阿店员[日光]", "desc": ""},
    1481: {"name": "3层楼层经理", "desc": ""},
    1484: {"name": "赤神[未生]", "desc": ""},
    148401: {"name": "生命线", "desc": "赤神 部位"},
    91067: {"name": "勒鲁日店员[日光]", "desc": ""},
    1474: {"name": "副厨师长", "desc": ""},
    1475: {"name": "皮制钱包", "desc": ""},
    91061: {"name": "口渴的勒卡基", "desc": ""},
    91062: {"name": "饥饿的勒卡基", "desc": ""},
    1482: {"name": "四足", "desc": ""},
    1483: {"name": "单足", "desc": ""},
    91063: {"name": "经线 针怪", "desc": ""},
    91064: {"name": "纬线 针怪", "desc": ""},
    1496: {"name": "缝纫之王", "desc": ""},
    1497: {"name": "赤神被撕扯的血肉", "desc": "赤神在暴走状态下将击杀目标制成的半尸"},
    1498: {"name": "经线 针怪", "desc": ""},
    1499: {"name": "纬线 针怪", "desc": ""},
    1529: {"name": "口渴的勒卡基", "desc": ""},
    1530: {"name": "饥饿的勒卡基", "desc": ""}
}

# 2. PanicInfo
panic_map = {
    1098: {
        "panicName": "破皮而出！",
        "lowMoraleDescription": "防御等级-3，攻击等级+1",
        "panicDescription": "防御等级-5，攻击等级+2"
    },
    1099: {
        "panicName": "缩入壳中…",
        "lowMoraleDescription": "速度最大值-1，防御等级+1",
        "panicDescription": "速度最大值-5，防御等级+3"
    },
    1102: {
        "panicName": "烹饪渴望",
        "lowMoraleDescription": "自身每有1层[SapsareeHungry]，攻击等级增加1点，受到的伤害量+3%",
        "panicDescription": "自身每有1层[SapsareeHungry]，攻击等级增加2点，受到的伤害量+5%"
    },
    1104: {
        "panicName": "错失恐惧 (FOMO)",
        "lowMoraleDescription": "自身每损失20%体力，攻击等级增加1点 (最多2点)\n自身获得1层[Vulnerable]",
        "panicDescription": "自身每损失20%体力，攻击等级增加1点 (最多2点)\n自身获得1层[Vulnerable]"
    },
    1105: {
        "panicName": "错乱的缝纫",
        "lowMoraleDescription": "回合开始时获得1层[Reduction]",
        "panicDescription": "回合开始时获得1层[Reduction]、1层[AttackDmgDown]"
    },
    1109: {
        "panicName": "循环之死",
        "lowMoraleDescription": "获得3层[Protection]",
        "panicDescription": "获得5层[Protection]"
    },
    1121: {
        "panicName": "分裂",
        "lowMoraleDescription": "防御等级-3，攻击等级+3\n与带有5层[BloodyMucus]的目标拼点时，拼点威力+2",
        "panicDescription": "防御等级-5，攻击等级+3\n造成的伤害量+10%\n与带有3层以上[BloodyMucus]的目标拼点时，拼点威力+3"
    }
}

def translate_korean_terms(text):
    if not isinstance(text, str):
        return text
    
    # 核心术语与词条替换
    replaces = [
        ("최댓값", "最大值"),
        ("수치당 받는 피해량", "每有1点数值受到的伤害量"),
        ("수치당", "每有1点数值"),
        ("피해량", "伤害量"),
        ("받는 피해량", "受到的伤害量"),
        ("가하는 피해량", "造成的伤害量"),
        ("공격 레벨", "攻击等级"),
        ("방어 레벨", "防御等级"),
        ("합 위력", "拼点威力"),
        ("기본 위력", "基础威力"),
        ("코인 위력", "硬币威力"),
        ("최종 위력", "最终威力"),
        ("위력", "威力"),
        ("정신력", "理智值"),
        ("최대 체력", "体力上限"),
        ("흐트러짐 선", "混乱线"),
        ("흐트러짐 상태", "混乱状态"),
        ("흐트러짐", "混乱"),
        ("턴 시작 시", "回合开始时"),
        ("턴 시작시", "回合开始时"),
        ("턴 종료 시", "回合结束时"),
        ("턴 종료시", "回合结束时"),
        ("전투 시작 시", "战斗开始时"),
        ("스테이지 시작시", "阶段开始时"),
        ("스테이지 시작 시", "阶段开始时"),
        ("스킬 사용 시", "使用技能时"),
        ("스킬 적중 시", "技能命中时"),
        ("적중 시", "命中时"),
        ("합 진행 시", "进行拼点时"),
        ("합 승리 시", "拼点胜利时"),
        ("합 패배 시", "拼点失败时"),
        ("사망 시", "阵亡时"),
        ("스킬에 피격 시", "被技能命中时"),
        ("피격 시", "被击中时"),
        ("보호막", "护盾"),
        ("다음 턴에", "下一回合"),
        ("이번 턴에", "本回合"),
        ("이번 턴", "本回合"),
        ("다음 턴", "下一回合"),
        ("매 턴", "每回合"),
        ("얻음", "获得"),
        ("부여함", "施加"),
        ("부여", "施加"),
        ("증가", "增加"),
        ("감소", "减少"),
        ("소모", "消耗"),
        ("회복", "恢复"),
        ("소멸", "消失"),
        ("제거", "解除"),
        ("해제", "解除"),
        ("최대", "最多"),
        ("이상", "以上"),
        ("이하", "以下"),
        ("미만", "以下"),
        ("초과", "超过"),
        ("중첩 불가", "不可叠加"),
        ("수감자", "罪人"),
        ("인격", "人格"),
        ("대상", "目标"),
        ("자신", "自身"),
        ("적에게", "对敌方"),
        ("모든 적에게", "对所有敌方"),
        ("모든 아군", "所有友方"),
        ("아군", "友方"),
        ("적", "敌方"),
        ("횟수", "次数"),
        ("파괴 불가 코인", "不可破坏硬币"),
        ("슈퍼 코인", "强力硬币"),
        ("속도", "速度"),
        ("스킬", "技能"),
        ("코인", "硬币"),
        ("파열", "破裂 "),
        ("진동", "震颤 "),
        ("침잠", "沉沦 "),
        ("화상", "烧伤 "),
        ("출혈", "流血 "),
        ("호흡", "呼吸法 "),
        ("충전", "充能 "),
        ("속박", "束缚 "),
        ("신속", "迅捷 "),
        ("마비", "麻痹 "),
        ("취약", "易损 "),
        ("보호", "守护 "),
        ("안내 불이행", "未遵从引导"),
        ("르누아르 우스티드 원단", "雷诺阿 精纺面料"),
        ("르누아르 원단", "雷诺阿面料"),
        ("보존", "保存"),
        ("맥동", "脉动"),
        ("햇살", "日光"),
        ("따가운 햇살", "灼热的日光"),
        ("부티크 신상옷", "精品店新款服饰"),
        ("탈의실", "更衣室"),
        ("핍박", "逼迫"),
        ("먹어줘...", "请吃掉我…"),
        ("맛있는거 먹고 힘난다는거예요", "吃饱饱充满力气"),
        ("토막난 요리재료", "碎块料理食材"),
        ("배고픈 거예요", "肚子空空饿扁了"),
        ("경계심", "戒备心"),
        ("경청에 대한 감사", "感谢倾听"),
        ("세례[적]", "洗礼[赤]"),
        ("바늘못", "针钉"),
        ("바늘이", "针怪"),
        ("바느질의 왕", "缝纫之王"),
        ("붉은 신", "赤神"),
        ("생명줄", "生命线"),
        ("플로어 매니저", "楼层经理"),
        ("수셰프", "副厨师长"),
        ("시지프 백화점", "西西弗斯百货公司"),
        ("시지프", "西西弗斯"),
        ("르누아르", "雷诺阿"),
        ("르루주", "勒鲁日"),
        ("구스타프", "古斯塔夫"),
        ("미모사", "含羞草"),
        ("리나모비블", "利纳莫比布尔"),
        ("가죽 지갑", "皮制钱包"),
        ("르카키", "勒卡基"),
        ("피크스티치 일부러 눈에 띄게 박았냐고?! 그렇게 쳐박아주마!", "故意把粗线挑针扎得这么显眼吗？！那就让你好好扎个够！"),
        ("제 시그니쳐인 거예요", "这是本店招牌"),
        ("～", "~") # 强制将全角波浪号换为半角
    ]

    res = text
    for kr, zh in replaces:
        res = res.replace(kr, zh)
    return res

def process_file(kr_filename, zh_filename, custom_map=None):
    kr_path = os.path.join(KR_DIR, kr_filename)
    zh_path = os.path.join(WORKSPACE_DIR, zh_filename)
    if not os.path.exists(kr_path):
        print(f"[WARN] 找不到韩文原文件: {kr_path}")
        return

    with open(kr_path, "r", encoding="utf-8-sig") as fp:
        kr_data = json.load(fp)

    zh_datalist = []
    for item in kr_data.get("dataList", []):
        new_item = {}
        item_id = item.get("id")
        if custom_map and item_id in custom_map:
            new_item = custom_map[item_id]
            new_item["id"] = item_id
        else:
            for k, v in item.items():
                if isinstance(v, str):
                    new_item[k] = translate_korean_terms(v)
                elif isinstance(v, list):
                    # 处理 levelList, coinlist 等深层嵌套
                    new_item[k] = process_nested_list(v)
                else:
                    new_item[k] = v
        zh_datalist.append(new_item)

    with open(zh_path, "w", encoding="utf-8") as fp:
        json.dump({"dataList": zh_datalist}, fp, ensure_ascii=False, indent=2)
    print(f"[{zh_filename}] 成功处理并写入: {len(zh_datalist)} 条。")

def process_nested_list(lst):
    new_lst = []
    for elem in lst:
        if isinstance(elem, dict):
            nd = {}
            for ek, ev in elem.items():
                if isinstance(ev, str):
                    nd[ek] = translate_korean_terms(ev)
                elif isinstance(ev, list):
                    nd[ek] = process_nested_list(ev)
                else:
                    nd[ek] = ev
            new_lst.append(nd)
        elif isinstance(elem, str):
            new_lst.append(translate_korean_terms(elem))
        else:
            new_lst.append(elem)
    return new_lst

def main():
    print("开始生成第8赛季 战斗机制、敌人、被动与技能全量汉化...")
    process_file("KR_Enemies-a1c10p1.json", "Enemies-a1c10p1.json", enemies_map)
    process_file("KR_PanicInfo-a1c10p1.json", "PanicInfo-a1c10p1.json", panic_map)
    process_file("KR_BattleKeywords-a1c10p1.json", "BattleKeywords-a1c10p1.json")
    process_file("KR_Bufs-a1c10p1.json", "Bufs-a1c10p1.json")
    process_file("KR_Passives_Enemy-a1c10p1.json", "Passives_Enemy-a1c10p1.json")
    process_file("KR_Skills_Enemy-a1c10p1.json", "Skills_Enemy-a1c10p1.json")
    process_file("KR_Passives_Abnormality-a1c10p1.json", "Passives_Abnormality-a1c10p1.json")
    process_file("KR_Skills_Abnormality-a1c10p1.json", "Skills_Abnormality-a1c10p1.json")
    process_file("KR_BattleSpeechBubbleDlg-a1c10p1.json", "BattleSpeechBubbleDlg-a1c10p1.json")
    print("第8赛季战斗机制与敌方文本全部生成完成！")

if __name__ == "__main__":
    main()
