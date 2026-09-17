#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate and generate UI, System, Items, Announcer, StageNode for Season 8 (a1c10p1)
严格遵循零协会命名存档、符号规范（半角~、六点省略号、全角双引号“”）与技术架构。
"""

import json
import os

WORKSPACE_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN"

def save_json(fname, datalist):
    p = os.path.join(WORKSPACE_DIR, fname)
    with open(p, "w", encoding="utf-8") as fp:
        json.dump({"dataList": datalist}, fp, ensure_ascii=False, indent=2)
    print(f"[{fname}] 已生成并写入: {len(datalist)} 条。")

# 1. Announcer-a1c10p1.json
announcers = [
    {"id": 55, "name": "西西弗斯百货公司广播"},
    {"id": 56, "name": "??"},
    {"id": 57, "name": "??"}
]

# 2. BattlePass-a1c10.json
battlepass = [
    {"id": "battlepass_season_8", "content": "刺点"},
    {"id": "battle_pass_season_8_product_package_with_limbus_desc_summary", "content": "◆ 第8赛季 边狱通行证\n◆ 购买后立即提升10级通行证等级\n◆ 人格特殊强化礼券 VI\n◆ 边狱礼包特别横幅"},
    {"id": "battle_pass_season_8_product_package_without_limbus_desc_summary", "content": "◆ 购买后立即提升10级通行证等级\n◆ 人格特殊强化礼券 VI\n◆ 边狱礼包特别横幅"},
    {"id": "until_season_8_start", "content": "- 至第9赛季更新前"},
    {"id": "until_season_8_end_on_shop", "content": "至第9赛季更新\n前"}
]

# 3. StageNode-a1c10p1.json
stagenodes = [
    {"id": 11001, "title": "审判"},
    {"id": 11002, "title": "法庭"},
    {"id": 11003, "title": "计划"},
    {"id": 11004, "title": "西西弗斯百货公司"}
]

# 4. UnitKeyword-a1c10p1.json
unitkeywords = [
    {"id": "UnitKeyword_SISYPHE", "content": "西西弗斯"},
    {"id": "UnitKeyword_LE_NOIR", "content": "雷诺阿"},
    {"id": "UnitKeyword_LE_ROUGE", "content": "勒鲁日"}
]

# 5. MainUIText-a1c10p1.json
mainui = [
    {"id": "main_ui_rpg_battle_defeated_title", "content": "战斗失败"},
    {"id": "main_ui_rpg_battle_defeated_desc", "content": "<color=#990000>所有罪人均已阵亡。</color>\n请选择后续操作。"},
    {"id": "main_ui_rpg_retry", "content": "重新挑战"},
    {"id": "main_ui_rpg_retry_desc", "content": "从头重新开始该场战斗"},
    {"id": "main_ui_rpg_accept_defeat", "content": "放弃"},
    {"id": "main_ui_rpg_accept_defeat_desc", "content": "返回至最后保存状态的泉水处"},
    {"id": "ContinueConfirm_Desc_Rpg_Stage", "content": "在10-4关卡中，即便战斗中使用继续挑战功能，\n最终通关时仍将被记录为EX通关。\n\n但使用继续挑战后，<color=#990000>若未进行重新挑战、未失败且未放弃并获得胜利保存进度</color>，\n<color=#990000>即便中途放弃10-4关卡，继续挑战消耗的道具也不会返还。</color>\n此外，消耗的狂气不支持退款。"},
    {"id": "formation_ego_resource_popup_current_owned_desc", "content": "当前持有的E.G.O资源数量。"},
    {"id": "formation_ego_resource_popup_current_owned", "content": "持有E.G.O资源"},
    {"id": "9128_chapter_notice_button_title", "content": "章节注意事项"},
    {"id": "9128_chapter_notice_popup_title", "content": "当前正在游玩的章节是<color=#3246AB>[第{0}章 {1}]</color>。"},
    {"id": "9128_chapter_notice_enter_title", "content": "确定要进入<color=#3246AB>[第{0}章 {1}]</color>吗？"},
    {"id": "9128_chapter_notice_popup_desc", "content": "◆ 即使尚未通关先前章节，<color=#ff6000><mark color=#ff000040><b><u>亦可直接游玩主线剧情第10章</color></mark></b></u>。\n◆ 文本中包含<color=#ff6000><mark color=#ff000040><b><u>第9.5章为止的剧透内容</color></mark></b></u>。\n◆ 通关第10章时，若先前章节未通关，则镜牢、镜折铁道、采掘、邪影战斗等<color=#ff6000><mark color=#ff000040><b><u>需要通关先前章节方可解锁的内容将无法游玩。</color></mark></b></u>为游玩全部内容，请达成相应解锁条件。\n◆ 以通关第10章为解锁条件的内容(预计后续更新)，请<color=#ff6000><mark color=#ff000040><b><u>通关第10章与9.5-26关卡</color></mark></b></u>。\n◆ 游玩第10章时，<color=#ff6000><mark color=#ff000040><b><u>将提供默尔索的部分助战人格</color></mark></b></u>。(助战人格与E.G.O适用同步/虚假解析第4阶段。)\n◆ 游玩第10章时，<color=#ff6000><mark color=#ff000040><b><u>所有友方人格提供同步第3阶段支援</color></mark></b></u>。E.G.O不会额外补正虚假解析等级。"}
]

# 6. BattleResultHint-a1c10p1.json
hints = [
    {"id": "battleTip_11006_1", "content": "利纳莫比布尔会以固定周期在更衣室内外反复进出。"},
    {"id": "battleTip_11006_2", "content": "在利纳莫比布尔进入更衣室时对其发起攻击，其攻击性将会提升。"},
    {"id": "battleTip_11008_1", "content": "副厨师长击杀目标时会获得“碎块料理食材”，并在回合结束时吞食以叠加“吃饱饱充满力气”。\n该层数叠加越高，其强力技能“这是本店招牌”的速度便越快、威力越强。"},
    {"id": "battleTip_11008_2", "content": "副厨师长还会将自身的皮制钱包当作料理食材，因此仅保护罪人并无法阻止其烹饪。"},
    {"id": "battleTip_11008_3", "content": "若副厨师长在某回合未击杀任何人，则会叠加“肚子空空饿扁了”。\n数值达到3时将会释放另一种强力技能，因此适时放任其烹饪一次也是应对策略。"},
    {"id": "battleTip_11010_1", "content": "面对楼层经理的特定技能时，建议不要使用攻击技能。"},
    {"id": "battleTip_11010_2", "content": "当“戒备心”达到10层时，楼层经理将释放强力技能。\n请注意避免叠加戒备心，或在特定技能中拼点失败以消除戒备心。"},
    {"id": "battleTip_11010_3", "content": "若自身带有“感谢倾听”，短时间内暂停攻击也是一种可行手段。"},
    {"id": "battleTip_11011_1", "content": "赤神[未生]的生命线极具威胁，建议优先破坏。"},
    {"id": "battleTip_11011_2", "content": "应对赤神[未生]的强力技能时，应指派高体力的友方罪人迎击。"},
    {"id": "battleTip_11011_3", "content": "当“洗礼[赤]”叠加时，建议使用守备技能将其消除。叠加至上限时将受到巨额流血 伤害，且阵亡时将生成敌对单位“赤神[未生]被撕扯的血肉”。"},
    {"id": "battleTip_11016_1", "content": "在针钉数值较高的状态下，若被技能“故意把粗线挑针扎得这么显眼吗？！那就让你好好扎个够！”命中，将陷入标本状态并受到巨额伤害。"},
    {"id": "battleTip_11016_2", "content": "在缝纫之王释放强力技能的回合，若针群依然存活，可能会遭受严重伤害。"}
]

# 7. UserTicket 系列
userticket_bg = [
    {"id": 80, "name": "???", "desc": "第8赛季 刺点 免费奖励达到70级时获得"},
    {"id": 81, "name": "???", "desc": "第8赛季 刺点 边狱通行证奖励达到70级时获得"},
    {"id": 82, "name": "???", "desc": "第8赛季 刺点 特别礼包购买时获得"}
]

# 8. IAPProduct-a1c10.json
iapproducts = [
    {"id": 607, "name": "第8赛季开赛狂气礼包", "desc": "每赛季重置的商品，可获得以下道具：\n\n· 付费狂气 x 1300"},
    {"id": 608, "name": "第8赛季定居支援物资", "desc": "在第8赛季“刺点”期间可购买，可获得以下道具：\n\n· 付费狂气 x 5040\n· 提取10次礼券 x 3\n· 人格训练礼券 IV x 90\n· 人格训练礼券 III x 40\n· 纺砣 x 80\n· 第8赛季自我碎片自选箱 x 40"},
    {"id": 162, "name": "每周狂气礼包", "desc": "每周重置的商品，可获得以下道具：\n\n· 人格训练礼券 IV x 60\n· 人格训练礼券 III x 30"},
    {"id": 163, "name": "每月狂气礼包 I", "desc": "每月重置的商品，可获得以下道具：\n\n· 人格训练礼券 IV x 140\n· 人格训练礼券 III x 40"},
    {"id": 164, "name": "每月狂气礼包 II", "desc": "每月重置的商品，可获得以下道具：\n\n· 人格训练礼券 IV x 270\n· 人格训练礼券 III x 40"},
    {"id": 165, "name": "每月狂气礼包 III", "desc": "每月重置的商品，可获得以下道具：\n\n· 人格训练礼券 IV x 500\n· 人格训练礼券 III x 170"},
    {"id": 109, "name": "每月成长支援礼包 I", "desc": "每月重置的商品，可获得以下道具：\n\n· 付费狂气 x 1690\n· 提取10次礼券 x 2\n· 人格训练礼券 IV x 60\n· 人格训练礼券 III x 30"},
    {"id": 504, "name": "特别提取礼包", "desc": "「新人格特定提取 高定时装::雷诺阿鞋履馆 良秀 · 高定时装::勒鲁日精品店 以实玛利」上线纪念商品，可获得以下道具：\n\n· 提取10次礼券 x 4"},
    {"id": 505, "name": "人格养成礼包", "desc": "「新人格特定提取 高定时装::雷诺阿鞋履馆 良秀 · 高定时装::勒鲁日精品店 以实玛利」上线纪念商品，可获得以下道具：\n\n· 跃迁模块 - 人格同步 x 1\n· 人格训练礼券 IV x 90\n· 人格训练礼券 III x 40"}
]

# 9. Items-a1c10p1.json
items = [
    {
        "id": 111,
        "name": "第8赛季 - 3星人格出目提取礼券",
        "desc": "可进行10次提取，其中必定出现属于第8赛季的3星人格。",
        "flavor": "提取礼券上方印有某种特殊标识的特殊物品。能够确定性地提取存在于稀薄可能性世界中的人格。纸张正在剧烈摇晃并跳动着。"
    },
    {
        "id": 112,
        "name": "第8赛季 - 保证获得当季人格抽取券",
        "desc": "可进行10次提取，其中必定出现属于第8赛季的人格。",
        "flavor": "提取礼券上方印有某种特殊标识的特殊物品。能够确定性地提取存在于稀薄可能性世界中的人格。纸张正在剧烈摇晃并跳动着。"
    },
    {
        "id": 105,
        "name": "第8赛季自我碎片自选箱",
        "desc": "打开后可获得自选罪人的第8赛季自我碎片1~3个。",
        "flavor": "能够自选罪人自我碎片的箱子。紧闭的缝隙中正溢出柔和的光芒。"
    },
    {
        "id": 106,
        "name": "第8赛季自我碎片随机箱",
        "desc": "打开后可随机获得某位罪人的第8赛季自我碎片1~3个。",
        "flavor": "随机装有某位罪人自我碎片的箱子。表面刻有复杂的几何图案。"
    }
]

# 加上 12 罪人的第 8 赛季自我碎片
sinner_names = [
    (10108, "李箱"), (10208, "浮士德"), (10308, "堂吉诃德"), (10408, "良秀"),
    (10508, "默尔索"), (10608, "鸿璐"), (10708, "希斯克利夫"), (10808, "以实玛利"),
    (10908, "罗佳"), (11008, "辛克莱"), (11108, "奥提斯"), (11208, "格里高尔")
]
for sid, sname in sinner_names:
    items.append({
        "id": sid,
        "name": f"第8赛季 {sname}自我碎片",
        "desc": f"在自动售货机中购买{sname}的人格、E.G.O或纺砣时使用。",
        "flavor": "罪人们的某一天以碎片的形式显现之物。碎片漂浮着。\n可能性若不紧握在手中，便仅仅只是漂浮的可能性。"
    })

items.append({
    "id": 12008,
    "name": "第8赛季 同步·虚假解析专用碎片 (通用)",
    "desc": "对所有罪人人格进行同步、E.G.O进行虚假解析时可以使用。",
    "flavor": "在进行人格同步、E.G.O虚假解析时，无论罪人是谁均可通用的碎片。\n但无论收集多少此种碎片，也无法用于提取人格或E.G.O。\n“该碎片是对无所不能的金枝研究的一环，可以填补进任何镜子的心象或世界中。您问提取？那当然不行。能够填补任意世界，便等同于无法从头构建起任何一个世界。 - LCA镜世界观测部门首席研究员”"
})

def main():
    print("开始生成第8赛季 UI、系统、物品与公告汉化文件...")
    save_json("Announcer-a1c10p1.json", announcers)
    save_json("BattlePass-a1c10.json", battlepass)
    save_json("StageNode-a1c10p1.json", stagenodes)
    save_json("UnitKeyword-a1c10p1.json", unitkeywords)
    save_json("MainUIText-a1c10p1.json", mainui)
    save_json("BattleResultHint-a1c10p1.json", hints)
    save_json("UserTicket-EGOBg-a1c10p1.json", userticket_bg)
    save_json("UserTicket-L-a1c10p1.json", userticket_bg)
    save_json("UserTicket-R-a1c10p1.json", userticket_bg)
    save_json("IAPProduct-a1c10.json", iapproducts)
    save_json("Items-a1c10p1.json", items)
    print("第8赛季基础 UI 与系统文件生成完毕！")

if __name__ == "__main__":
    main()
