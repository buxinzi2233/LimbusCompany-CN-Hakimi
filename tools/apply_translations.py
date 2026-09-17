#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 4: Apply High-Fidelity Translations
将主模型精翻的增量条目合并回汉化工程 workspace/LLC_zh-CN/
严格遵循零协会三大铁律：
- 动词层数“获得/施加”，强度“增加”
- 关键词末尾带半角空格
- 强制使用半角波浪号 ~
- 占位符格式严格对齐
"""

import json
import os

WORKSPACE_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN"

def update_json_file(filename, new_items, key_field="id"):
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if not os.path.exists(filepath):
        data = {"dataList": []}
    else:
        with open(filepath, "r", encoding="utf-8-sig") as f:
            data = json.load(f)

    existing_map = {}
    for i, item in enumerate(data.get("dataList", [])):
        if isinstance(item, dict) and key_field in item:
            existing_map[item[key_field]] = i

    added = 0
    updated = 0
    for n_item in new_items:
        k = n_item[key_field]
        if k in existing_map:
            data["dataList"][existing_map[k]].update(n_item)
            updated += 1
        else:
            data["dataList"].append(n_item)
            added += 1

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[{filename}] 注入完成: 新增 {added} 条, 更新 {updated} 条。")

# ==================== 1. BattleKeywords.json ====================
keywords_patch = [
    {
        "id": "DianxueHongLu",
        "name": "点穴 - 鸿潞",
        "desc": "- 最大值：3\n- 施加点穴的角色根据目标(或部位)的点穴数值获得以下效果：\n· 1层：拼点威力+1\n· 2层：基础威力+1\n· 3层：拼点威力+1，基础威力+1\n- 施加该效果的角色若对其他目标(或部位)施加点穴，则原效果消失\n- 被其他角色施加点穴时，效果将被替换 (保留数值)",
        "summary": "",
        "undefined": "-"
    },
    {
        "id": "DuelSousTemoinsEast",
        "name": "见证决斗 - 东部五协会",
        "desc": "- 最大值：3\n- 攻击等级+(数值)\n- 数值达到2以上时，基础技能的呼吸法 强度获得量+1\n- 数值达到3以上时，基础技能的呼吸法 次数获得量+1",
        "summary": "",
        "undefined": "-"
    },
    {
        "id": "SingBulletSupport",
        "name": "(拇指辛克莱子弹补给接收目标特效)"
    },
    {
        "id": "ATL_Agility",
        "summary": "仅供展示"
    },
    {
        "id": "ATL_Breath",
        "summary": "仅供展示"
    },
    {
        "id": "ATL_Target",
        "summary": "仅供展示"
    }
]

# ==================== 2. BattleKeywords-BossRaid.json & Bufs-BossRaid.json ====================
bossraid_keywords_bufs_patch = [
    {
        "id": "FavorBuffLeiheng",
        "name": "邪影 [插翅虎]",
        "desc": "- 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基础防御等级+8 (不可叠加)\n- 产生<color=#f8c200>罪孽共鸣</color>时，获得1个该属性的E.G.O资源、1个持有量最少的随机E.G.O资源 (每回合最多2次)\n- E.G.O技能的伤害量+50%\n- 人格技能中施加<color=#f8c200>破裂 </color>或属于<color=#f8c200>暴食</color>属性的攻击技能伤害量+25% (若为E.G.O技能，则改为伤害量+100%)\n- 人格与敌方进行拼点时，主要目标每带有2层<color=#f8c200>束缚 </color>，拼点威力+1 (最多+2)",
        "summary": ""
    },
    {
        "id": "FavorBuffLeihengTwo",
        "name": "邪影 [天退星]",
        "desc": "- 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基础防御等级+15 (不可叠加)\n- 产生<color=#f8c200>罪孽共鸣</color>时，获得1个该属性的E.G.O资源、2个持有量最少的随机E.G.O资源 (每回合最多2次)\n- E.G.O技能的伤害量+50%\n- 人格技能中施加<color=#f8c200>烧伤 </color>、<color=#f8c200>特殊烧伤</color>或属于<color=#f8c200>愤怒</color>属性的攻击技能伤害量+25% (若为E.G.O技能，则改为伤害量+100%)",
        "summary": ""
    },
    {
        "id": "FavorBuffLeihengHard",
        "name": "苦难",
        "desc": "- <color=#ff0000>体力上限</color>+80%\n- 理智值不会降低至0以下\n- 对带有<color=#ff0000>猎物</color>的目标造成的伤害量+50% (目标装备守备技能时，该效果不生效)，受到的伤害量-50%\n- 使用爆碎斩 [爆碎斬]时，若<color=#ff0000>虎豹弹达到3枚以上</color>，则伤害量+100%",
        "summary": "困难难度苦难"
    },
    {
        "id": "FavorBuffLeihengHardTwo",
        "name": "苦难",
        "desc": "- <color=#ff0000>体力上限</color>+80%\n- 理智值不会降低至0以下\n- 对带有<color=#ff0000>猎物</color>的目标造成的伤害量+50% (目标装备守备技能时，该效果不生效)，受到的伤害量-50%\n- 使用爆碎斩 [爆碎斬]时，若<color=#ff0000>虎豹弹达到3枚以上</color>，则伤害量+100%\n- [2阶段专用效果]\n· 使用技能时，若<color=#ff0000>主要目标带有猎物</color>，则<color=#ff0000>基础威力增加5点且伤害量+200%</color> (目标装备守备技能时，该效果不生效)，该技能的所有硬币变为<color=#ff0000>不可破坏硬币</color>\n· 与带有<color=#ff0000>猎物</color>的目标拼点失败时，自身获得1层<color=#ff0000>切斩 [切斬]</color>",
        "summary": "困难难度苦难"
    },
    {
        "id": "FavorBuffLeiheng1stPhaseForUI",
        "name": "邪影 [插翅虎]",
        "desc": "- 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基础防御等级+8 (不可叠加)\n- 产生<color=#f8c200>罪孽共鸣</color>时，获得1个该属性的E.G.O资源、1个持有量最少的随机E.G.O资源 (每回合最多2次)\n- E.G.O技能的伤害量+50%\n- 人格技能中施加<color=#f8c200>破裂 </color>或属于<color=#f8c200>暴食</color>属性的攻击技能伤害量+25% (若为E.G.O技能，则改为伤害量+100%)\n- 人格与敌方进行拼点时，主要目标每带有2层<color=#f8c200>束缚 </color>，拼点威力+1 (最多+2)"
    },
    {
        "id": "FavorBuffLeiheng2ndPhaseForUI",
        "name": "邪影 [天退星]",
        "desc": "- 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基础防御等级+15 (不可叠加)\n- 产生<color=#f8c200>罪孽共鸣</color>时，获得1个该属性的E.G.O资源、2个持有量最少的随机E.G.O资源 (每回合最多2次)\n- E.G.O技能的伤害量+50%\n- 人格技能中施加<color=#f8c200>烧伤 </color>、<color=#f8c200>特殊烧伤</color>或属于<color=#f8c200>愤怒</color>属性的攻击技能伤害量+25% (若为E.G.O技能，则改为伤害量+100%)"
    },
    {
        "id": "FavorBuffLeihengHardForUI",
        "name": "苦难",
        "desc": "- <color=#ff0000>体力上限</color>+80%\n- 理智值不会降低至0以下\n- 对带有<color=#ff0000>猎物</color>的目标造成的伤害量+50% (目标装备守备技能时，该效果不生效)，受到的伤害量-50%\n- 使用爆碎斩 [爆碎斬]时，若<color=#ff0000>虎豹弹达到3枚以上</color>，则伤害量+100%\n- [2阶段专用效果]\n· 使用技能时，若<color=#ff0000>主要目标带有猎物</color>，则<color=#ff0000>基础威力增加5点且伤害量+200%</color> (目标装备守备技能时，该效果不生效)，该技能的所有硬币变为<color=#ff0000>不可破坏硬币</color>\n· 与带有<color=#ff0000>猎物</color>的目标拼点失败时，自身获得1层<color=#ff0000>切斩 [切斬]</color>"
    },
    {
        "id": "HugeIrritationReflectrial",
        "name": "心 - 天退星[天退星]",
        "desc": "- 回合开始时，每损失15%体力，自身获得1层伤害量增加与1层威力增加 (各最多5层)\n- 通过技能对敌方施加的震颤 强度施加量+3，震颤 次数增加量+1\n- 若自身的速度比目标高出3点以上，则造成的伤害量+(与目标的速度差 x 5)% (最多40%)\n- “二连斩-暴”、“三连击-暴”的最后一枚硬币变为不可破坏硬币",
        "summary": ""
    },
    {
        "id": "Prey_leiheng",
        "name": "猎物",
        "desc": "- 与敌方进行拼点时，拼点威力-5\n- 战斗开始时，\n· 若装备了攻击技能，则使用攻击技能对雷横造成的伤害量降低50%\n· 若装备了守备技能，则受到雷横攻击的伤害量降低75%\n- 带有该效果的状态下与雷横拼点胜利时，获得3个持有量最少的E.G.O资源\n- 回合结束时解除，并使自身恢复10点理智值",
        "summary": ""
    }
]

# ==================== 3. Passives-BossRaid.json ====================
passives_bossraid_patch = [
    {
        "id": 501911,
        "name": "邪影战斗",
        "desc": "与同一目标的拼点次数达到10次以上时，\n拼点威力根据当前 (拼点次数/10)随机增加或减少 (最多10点)\n\n[Combustion]、[Laceration]、[Vibration]、[Burst]、[Sinking]的强度最多可叠加至30点，\n次数最多可叠加至10次\n\n以第一编队入场时，阶段开始时：\n- 自身与战场上的所有罪人理智值变为30\n(若为减算硬币人格，则适用为-30)\n- 全属性E.G.O资源+3\n\n被动“天退星”效果触发时，\n回合结束，并在下一回合切换为第2阶段\n- 持有的状态效果不会因阶段切换而重置\n\n以第二、第三编队入场时，阶段开始时：\n根据当前体力百分比，按顺序视作以下被动已触发过：\n- 高于85%：装填<noparse>虎豹弹</noparse>\n- 85%以下：装填<noparse>虎豹弹</noparse>、雷横\n- 66%以下：装填<noparse>虎豹弹</noparse>、雷横、天退星\n- 50%以下：装填<noparse>虎豹弹</noparse>、雷横、天退星、韶智 天退星 雷横"
    },
    {
        "id": 501901,
        "name": "拇指干部 卡波 IIII",
        "desc": "受到[Combustion]、[Laceration]、[Vibration]、[Burst]、[Sinking]的伤害量-30%\n\n投掷消耗[BulletPropellant]的硬币时，即使没有[BulletPropellant]，也不会取消攻击；作为替代，该硬币命中时施加[Combustion]、增加[Combustion]次数的效果不生效\n\n进行拼点时，使目标的[Vibration]次数增加(1 + 拼点次数/3)次\n(最多3次，对单个目标每回合最多生效3次)"
    },
    {
        "id": 501902,
        "name": "东部十剑",
        "desc": "战斗阶段开始时，以及行动循环切换的回合开始时：\n- 自身获得1层[Bothersome]\n- 自身每损失10%体力，恢复5点理智值 (最多40点)\n\n适用[PanicChangeLock]效果，\n回合结束时若处于恐慌状态，则理智值变为45"
    },
    {
        "id": 501903,
        "name": "选定猎物",
        "desc": "回合开始时，<color=#ff6000><mark=#ff000040><b><u>对上一回合对自己造成伤害最多的罪人施加1层[Prey_leiheng]</u></b></mark></color>\n\n雷横攻击带有[Prey_leiheng]的罪人，且攻击结束时若目标：\n- 陷入混乱，则所有罪人理智值减少10点，并在本回合与下一回合获得1层[ParryingResultDown] (每回合最多1次)\n- 死亡，则上述效果额外触发1次"
    },
    {
        "id": 501904,
        "name": "天退星刀 [天退星刀]",
        "desc": "<color=#ff6000><mark=#ff000040><b><u>单方面攻击命中时</u></b></mark></color>伤害量增加30%，并在下一回合施加1层[Vulnerable]\n\n消耗[BulletPropellant]命中的技能硬币伤害量增加20%，并在下一回合施加2层[DefenseDown]\n\n<color=#ff6000><mark=#ff000040><b><u>若目标装备了守备技能，则上述效果不生效</u></b></mark></color>"
    },
    {
        "id": 501912,
        "name": "天退星刀 过热",
        "desc": "若使用了强力攻击(“快刀乱麻”、“超绝猛虎杀击乱斩”)，则在下一回合根据本次战斗中使用强力攻击的次数获得对应层数的[Complacency] (最多5层)"
    },
    {
        "id": 501910,
        "name": "插翅虎 [揷翅虎]",
        "desc": "战斗开始时，<color=#ff6000><mark=#ff000040><b><u>成比例于自身的速度</u></b></mark></color>：\n- 恢复等同于该数值的理智值。若理智值低于0，则恢复数值翻倍\n- 获得(数值/3)层[SlashDamageUp] (最多5层)\n\n战斗开始时，<color=#ff6000><mark=#ff000040><b><u>若自身带有3层以上的[Binding]，则上述效果不触发，</u></b></mark></color>并获得等同于自身所带[Binding]数值层数的[DefenseDown] (最多9层)"
    },
    {
        "id": 501905,
        "name": "虎豹弹 装填",
        "desc": "首回合结束时，装填[BulletPropellant]，并在下一回合切换行动循环\n- 若处于混乱状态，则解除混乱"
    },
    {
        "id": 501906,
        "name": "雷横 [雷橫]",
        "desc": "回合结束时若体力降至85%以下，或在第2回合结束时，下一回合切换行动循环：\n- 使用强力攻击(“快刀乱麻”)，且每隔3回合循环重复。使用该技能的回合速度最小值与最大值+10\n- 该回合开始时，自身获得25层[BattleSense]\n- 若处于混乱状态，则解除混乱"
    },
    {
        "id": 501907,
        "name": "天退星 [天退星]",
        "desc": "战斗中若体力降至66%以下，则在下一回合切换阶段并变更行动循环：\n- 该回合开始时，获得1层[Irritation]\n- 该回合开始时，获得18枚[BulletPropellantSpecial]并立即装填\n· 若[BulletPropellantSpecial]全部消耗完毕，则该效果转变为[BulletPropellant]，并在下一回合召唤2名严格的拇指索尔达托以补给[BulletPropellantSpecial]\n- 若处于混乱状态，则解除混乱"
    },
    {
        "id": 501908,
        "name": "韶智 天退星 雷横",
        "desc": "回合结束时若体力降至50%以下，则下一回合变更行动循环：\n- 强力攻击“快刀乱麻”变更为“超绝猛虎杀击乱斩”。使用该技能的回合速度最小值与最大值+15\n- [BattleSense]变更为[RestoredBattleSense]\n- [Irritation]变更为[HugeIrritation]\n- 若处于混乱状态，则解除混乱"
    },
    {
        "id": 502001,
        "name": "猛虎豹弹 支援",
        "desc": "回合开始时，自身获得3层[Vulnerable]\n回合结束时，向雷横支援[BulletPropellantSpecial]。\n\n阵亡时，下一回合使雷横获得1层[Vulnerable]"
    }
]

# ==================== 4. Skills_Abnormality-BossRaid.json ====================
skills_bossraid_patch = [
    {
        "id": 501901,
        "levelList": [{"level": 1, "name": "二连斩", "desc": "目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+2)", "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttack] 施加2层[Vibration]"}]}, {"coindescs": [{"desc": "[OnSucceedAttack] 施加3层[Vibration]"}]}]}]
    },
    {
        "id": 501902,
        "levelList": [{"level": 1, "name": "三连击", "desc": "目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+2)", "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration]次数增加2次"}]}, {"coindescs": [{"desc": "[OnSucceedAttack] 施加1层[Vibration]，使目标的[Vibration]次数增加2次"}]}, {"coindescs": [{"desc": "[OnSucceedAttack] 触发[VibrationExplosion]。使目标的[Vibration]次数减少1次"}]}]}]
    },
    {
        "id": 501903,
        "levelList": [{"level": 1, "name": "二连斩-暴[爆]", "desc": "目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+4)\n[DefeatDuel] 自身的[BulletPropellant]减少1枚", "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttack] 施加3层[Vibration]"}]}, {"coindescs": [{"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]，使目标的[Combustion]次数增加2次"}, {"desc": "[OnSucceedAttack] 施加3层[Vibration]，使目标的[Vibration]次数增加2次"}]}]}]
    },
    {
        "id": 501904,
        "levelList": [{"level": 1, "name": "三连击-暴[爆]", "desc": "目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+4)\n[DefeatDuel] 自身的[BulletPropellant]减少1枚", "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration]次数增加2次"}]}, {"coindescs": [{"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]，使目标的[Combustion]次数增加2次"}, {"desc": "[OnSucceedAttack] 施加2层[Vibration]，使目标的[Vibration]次数增加2次"}]}, {"coindescs": [{"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]，使目标的[Combustion]次数增加2次"}, {"desc": "[UnBrokenCoinOnSucceedAttack] 触发2次[VibrationExplosion]。使目标的[Vibration]次数减少2次"}]}]}]
    },
    {
        "id": 501905,
        "levelList": [{"level": 1, "name": "爆碎斩 [爆碎斬]", "desc": "优先以带有[Prey_leiheng]的目标为指定对象\n<color=#ff6000><mark=#ff000040><b><u>不论速度高低均可与该技能进行拼点</u></b></mark></color>\n目标的[Combustion]与[Vibration]之和每有6点，硬币威力+1 (最多+3)\n[DefeatDuel] 自身理智值减少10点", "coinlist": [{"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]"}, {"desc": "[OnSucceedAttack] 施加3层[Vibration]"}, {"desc": "[UnBrokenCoinOnSucceedAttack] 施加4层[Vibration]，使目标的[Vibration]次数增加4次"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 使目标的[Combustion]次数增加3次"}, {"desc": "[OnSucceedAttack] 使目标的[Vibration]次数增加3次"}, {"desc": "[UnBrokenCoinOnSucceedAttack] 转化为[VibrationIgnition]的[Switch_Vibration]"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "<color=#ff6000><mark=#ff000040><b><u>若通过该硬币效果消耗了[BulletPropellant]，则伤害量+50%</u></b></mark></color>"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]，使目标的[Combustion]次数增加3次"}, {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> 触发2次[VibrationExplosion]。使目标的[Vibration]次数减少2次"}]}]}]
    },
    {
        "id": 501906,
        "levelList": [{"level": 1, "name": "快刀乱麻 [快刀亂麻]", "desc": "优先以带有[Prey_leiheng]的目标为指定对象\n<color=#ff6000><mark=#ff000040><b><u>不论速度高低均可与该技能进行拼点，且在使用该技能前不会陷入混乱状态</u></b></mark></color>\n[WhenUse] 消耗全部[BattleSense]。消耗的数值每有：\n- 达到10点以上：每10点使攻击加权值+1 (最多+2)\n- 达到25点：主要目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+5)\n[DefeatDuel] 自身获得1层[Paralysis]\n[DefeatDuel] 造成的伤害量降低80%且该技能造成的伤害无法使目标混乱，<color=#ff6000><mark=#ff000040><b><u>施加的[Combustion]强度与次数、[Vibration]强度与次数的施加量减半</u></b></mark></color> (因其他效果增加的数值除外)\n[EndSkill] [FullReload] (每回合最多1次)\n- 若带有[BulletPropellantSpecial]，则改为[ReloadKeepAmmo] (每回合最多1次)\n[EndSkill] 结束本回合行动", "coinlist": [{"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "消耗全部[BulletPropellant]"}, {"desc": "[OnSucceedAttack] 施加等同于消耗[BulletPropellant]数量的[Combustion]、增加[Combustion]次数、施加[Vibration]、增加[Vibration]次数"}, {"desc": "[UnBrokenCoinOnSucceedAttack] 转化为[VibrationIgnition]的[Switch_Vibration]"}, {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> 触发3次[VibrationExplosion]。使目标的[Vibration]次数减少3次"}]}]}]
    },
    {
        "id": 501907,
        "levelList": [{"level": 1, "name": "超绝猛虎杀击乱斩 [超絕猛虎殺擊亂斬]", "desc": "优先以带有[Prey_leiheng]的目标为指定对象\n<color=#ff6000><mark=#ff000040><b><u>不论速度高低均可与该技能进行拼点，且在使用该技能前不会陷入混乱状态</u></b></mark></color>\n[WhenUse] 消耗全部[BattleSense]。消耗的数值每有：\n- 达到10点以上：每10点使攻击加权值+1 (最多+4)\n- 达到25点以上：主要目标的[Combustion]与[Vibration]之和每有4点，最终威力+1 (最多+6)\n- 达到50点：硬币威力+1，伤害量+50%\n[DefeatDuel] 自身获得6层[Paralysis]\n[DefeatDuel] 造成的伤害量降低80%且该技能造成的伤害无法使目标混乱，<color=#ff6000><mark=#ff000040><b><u>施加的[Combustion]强度与次数、[Vibration]强度与次数的施加量减半</u></b></mark></color> (因其他效果增加的数值除外)\n[EndSkill] [FullReload] (每回合最多1次)\n- 若带有[BulletPropellantSpecial]，则改为[ReloadKeepAmmo] (每回合最多1次)\n[EndSkill] 结束本回合行动", "coinlist": [{"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加6层[Combustion]"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 使目标的[Combustion]次数增加6次"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加6层[Vibration]"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 使目标的[Vibration]次数增加6次"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[UnBrokenCoinOnSucceedAttack] 转化为[VibrationIgnition]的[Switch_Vibration]"}]}, {"coindescs": [{"desc": "[SuperCoin]"}, {"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack]</u></b></mark></color> 触发5次[VibrationExplosion]。使目标的[Vibration]次数减少5次"}]}]}]
    },
    {
        "id": 501908,
        "levelList": [{"level": 1, "name": "天退星刀 装填", "desc": "[DuelCounter]\n[DefeatDuel] 自身的[BulletPropellant]减少1枚\n[EndBattle] [FullReload] (每回合最多1次)\n- 若带有[BulletPropellantSpecial]，则改为[ReloadKeepAmmo] (每回合最多1次)", "coinlist": [{"coindescs": [{"desc": "[OnSucceedAttack] 施加2层[Vibration]"}]}, {"coindescs": [{"desc": "[BulletPropellant] 消耗1枚"}, {"desc": "[OnSucceedAttack] 施加3层[Combustion]"}, {"desc": "[OnSucceedAttack] 使目标的[Vibration]次数增加3次"}]}]}]
    },
    {
        "id": 502001,
        "levelList": [{"level": 1, "name": "猛虎豹弹 支援", "desc": "[EndBattle] 使雷横获得6枚[BulletPropellantSpecial]\n[EndBattle] [DisengageCombat]", "coinlist": [{}]}]
    }
]

def main():
    print("开始执行精翻条目合并...")
    update_json_file("BattleKeywords.json", keywords_patch)
    update_json_file("BattleKeywords-BossRaid.json", bossraid_keywords_bufs_patch)
    update_json_file("Bufs-BossRaid.json", bossraid_keywords_bufs_patch)
    update_json_file("Passives-BossRaid.json", passives_bossraid_patch)
    update_json_file("Skills_Abnormality-BossRaid.json", skills_bossraid_patch)
    print("全部精翻条目已成功合并至 workspace/LLC_zh-CN/！")

if __name__ == "__main__":
    main()
