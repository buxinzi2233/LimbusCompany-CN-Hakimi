#!/usr/bin/env python3
import json
import os

WORKSPACE_DIR = "workspace/LLC_zh-CN"

with open("backups/part2-scope-20260924/source-kr/Skills_Abnormality-a1c10p2.json", encoding="utf-8-sig") as f:
    kr_data = json.load(f)["dataList"]

# Define translations for all 59 skills
trans = {
    # 1503: 往昔之海的黑线
    150301: {
        "levelList": [{
            "level": 1,
            "name": "还给我……",
            "desc": "若目标装备了守备技能，则造成的伤害量-90%\n自身每有1层[HeavyBlackYarn] ，拼点威力+1\n[WhenUse] 目标的[TangleBlackYarn] 每有5层，基础威力+1(最多+2)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "}
                ]}
            ]
        }]
    },
    150302: {
        "levelList": [{
            "level": 1,
            "name": "交出来……",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n自身每有1层[HeavyBlackYarn] ，拼点威力+1\n[WhenUse] 主要目标的[TangleBlackYarn] 每有3层，拼点威力+1(最多+8)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[TangleBlackYarn] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若目标的<color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn] 在15以上，则使目标陷入混乱状态</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    150303: {
        "levelList": [{
            "level": 1,
            "name": "别夺走……",
            "desc": "自身每有1层[HeavyBlackYarn] ，拼点威力+1\n[WhenUse] 主要目标的[TangleBlackYarn] 每有5层，基础威力+1(最多+2)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[TangleBlackYarn] "}
                ]}
            ]
        }]
    },
    150304: {
        "levelList": [{
            "level": 1,
            "name": "错综缠结",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n自身每有1层[HeavyBlackYarn] ，拼点威力+1\n[WhenUse] 目标的[TangleBlackYarn] 每有3层，拼点威力+1(最多+8)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加4次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若目标的<color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn] 在15以上，则使目标陷入混乱状态</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    150305: {
        "levelList": [{
            "level": 1,
            "name": "古旧之物的挣扎",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n自身的[HeavyBlackYarn] 每有1层，拼点威力-1\n[WhenUse] 主要目标的[TangleBlackYarn] 每有3层，基础威力+1(最多+3)\n[WhenUse] 若主要目标的[TangleBlackYarn] 在15以上，则基础威力+3",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[TangleBlackYarn] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若目标的<color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn] 在15以上，则使目标陷入混乱状态</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    150306: {
        "levelList": [{
            "level": 1,
            "name": "纠缠",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n自身的[HeavyBlackYarn] 每有1层，拼点威力-1\n[WhenUse] 主要目标的[TangleBlackYarn] 每有3层，基础威力+1(最多+3)\n[WhenUse] 若主要目标的[TangleBlackYarn] 在15以上，则基础威力+3",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 对目标施加5层[TangleBlackYarn] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5层[TangleBlackYarn] "}
                ]}
            ]
        }]
    },
    150307: {
        "levelList": [{
            "level": 1,
            "name": "无底深渊之口",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n[StartBattle] 目标的[TangleBlackYarn] 每有2层，基础威力+1，造成的伤害量+10%",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加5层[TangleBlackYarn] "},
                    {"desc": "[DefeatDuelAttack] 消除目标的<color=#ff6000><mark=#ff000040><b><u>10层[TangleBlackYarn] </u></b></mark></color>"},
                    {"desc": "[OnSucceedAttack] 若目标处于<color=#ff6000><mark=#ff000040><b><u>混乱状态</u></b></mark></color>或目标的<color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn] 在20以上</u></b></mark></color>，则重复投掷该硬币(每个技能最多1次)"},
                    {"desc": "[ReUseOnSucceedAttack] 造成等同于<color=#ff6000><mark=#ff000040><b><u>目标体力上限150%的固定伤害</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    150308: {
        "levelList": [{
            "level": 1,
            "name": "冲洗",
            "desc": "[DuelCounter] \n[WhenUse] 目标的[TangleBlackYarn] 每有2层，基础威力+1\n[WinDuel] 消除目标的<color=#ff6000><mark=#ff000040><b><u>所有[TangleBlackYarn] </u></b></mark></color>，并消除使用该技能的部位的所有[SickBlackYarn] \n[DefeatDuel] 消除目标的<color=#ff6000><mark=#ff000040><b><u>所有[TangleBlackYarn] </u></b></mark></color>，并使使用该技能的部位的[SickBlackYarn] 减少一半(向上取整)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "},
                    {"desc": "[OnSucceedAttack] 下回合对目标施加3层[Binding] "}
                ]}
            ]
        }]
    },

    # 1501: 阿尔菈乌涅 (Alriune)
    150101: {
        "levelList": [{
            "level": 1,
            "name": "春之诞生",
            "desc": "[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>目标的理智值-5</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Sinking] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"}
                ]}
            ]
        }]
    },
    150102: {
        "levelList": [{
            "level": 1,
            "name": "秋之迟暮",
            "desc": "[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>目标的理智值-5</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2点[Sinking] "}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}]}
            ]
        }]
    },
    150103: {
        "levelList": [{
            "level": 1,
            "name": "渴望成为人类的玩偶",
            "desc": "[WhenUse] 目标的[Vibration] 强度与[Sinking] 强度之和每有3点，最终威力+1(最多+2)\n[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>目标的理智值-10</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 造成等同于目标[Sinking] 强度的理智伤害"}]}
            ]
        }]
    },
    150104: {
        "levelList": [{
            "level": 1,
            "name": "渴望成为玩偶的人类",
            "desc": "[WideAreaRampage] \n[WhenUse] 主要目标的[Vibration] 强度与[Sinking] 强度之和每有3点，最终威力+1(最多+2)\n[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>所有目标的理智值-10</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5层[AlriuneSillage] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5层[AlriuneSillage] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "该硬币命中所有攻击目标"},
                    {"desc": "[OnSucceedAttack] 对目标施加1点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150105: {
        "levelList": [{
            "level": 1,
            "name": "散发宜人香气的月桂冠",
            "desc": "<color=#ff6000><mark color=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n该技能不造成伤害，且不触发目标的[Sinking] \n[EndSkill] 对<color=#ff6000><mark color=#ff000040><b><u>目标施加[FlowerLaurelWreath] (每回合最多1次)</u></b></mark></color>",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的理智值恢复20点"}
                ]}
            ]
        }]
    },
    150106: {
        "levelList": [{
            "level": 1,
            "name": "怀揣归于尘土的夙愿",
            "desc": "[WhenUse] 主要目标的[Vibration] 强度与[Sinking] 强度之和每有3点，最终威力+1(最多+8)\n[WhenUse] 若<color=#ff6000><mark color=#ff000040><b><u>主要目标没有[FlowerLaurelWreath] ，则最终威力+5</u></b></mark></color>\n[DefeatDuel]\n- 伤害量减少80%\n- 该技能造成的伤害不会使目标陷入混乱\n- 不触发目标的[Sinking] \n\n[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>所有目标的理智值-10</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外\n[EndSkillAll] 将自身的[AlriunePetal] 重置为0",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加等同于目标[AlriuneSillage] 强度的[Vibration] 强度(分别生效)"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加等同于目标[AlriuneSillage] 强度的[Sinking] 强度(分别生效)"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150107: {
        "levelList": [{
            "level": 1,
            "name": "与所有欲生之物同归墓穴",
            "desc": "[CantDuel] [CantChangeTarget] \n该技能不触发目标的守备技能\n若目标不处于恐慌或侵蚀状态，则取消攻击",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 造成等同于目标体力上限120%的固定伤害"}]}
            ]
        }]
    },
    150108: {
        "levelList": [{
            "level": 1,
            "name": "当所有人内心的欲望都被花朵所取代……",
            "desc": "无论速度如何皆可与该技能拼点\n该技能不造成伤害\n[EndSkill] 使<color=#ff6000><mark color=#ff000040><b><u>目标的理智值-25</u></b></mark></color>\n- 持有[FlowerLaurelWreath] 的目标除外",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加10点沉沦 "}
                ]}
            ]
        }]
    },

    # 1502: 泥土所生者
    150201: {
        "levelList": [{
            "level": 1,
            "name": "花簇",
            "desc": "该技能造成的伤害固定为0点",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加1层[AlriuneSillage] "}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加1层[AlriuneSillage] "}]}
            ]
        }]
    },
    150202: {
        "levelList": [{
            "level": 1,
            "name": "心之龟裂",
            "desc": "该技能造成的伤害固定为0点\n[WhenUse] 目标的负面效果强度之和每有3点，最终威力+1(最多+2)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加4点[Sinking] "},
                    {"desc": "[OnSucceedAttack] 对目标施加4点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 下回合对目标施加1层[Vulnerable] "}
                ]}
            ]
        }]
    },
    150203: {
        "levelList": [{
            "level": 1,
            "name": "缠绕而至的绝望",
            "desc": "该技能造成的伤害固定为0点\n[WhenUse] 目标的负面效果层数之和每有3层，最终威力+1(最多+3)\n[DefeatDuel]\n- 不触发目标的[Sinking] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>造成等同于目标[Sinking] 强度的理智伤害</u></b></mark></color>"}
                ]}
            ]
        }]
    },

    # 1519: 腻子 (Mastic)
    151901: {
        "levelList": [{
            "level": 1,
            "name": "启动",
            "desc": "[StartBattle] \n<color=#ff6000><mark color=#ff000040><b><u>- 获得自身体力上限30%的护盾</u></b></mark></color>\n- 自身的[ChargeKhaki] 次数恢复至最大值\n- 下回合获得1层[SpreadingDye] ",
            "coinlist": [{"coindescs": []}]
        }]
    },
    151902: {
        "levelList": [{
            "level": 1,
            "name": "穿线",
            "desc": "自身的[ChargeKhaki] 强度每有2点，拼点威力+1(最多+3)\n[WhenUse] 下回合获得1层[Agility] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>下回合对目标施加1层[Binding] </u></b></mark></color>"}
                ]}
            ]
        }]
    },
    151903: {
        "levelList": [{
            "level": 1,
            "name": "锁式线迹",
            "desc": "自身的速度高于目标时，造成的伤害量+20%\n自身的[ChargeKhaki] 强度每有2点，硬币威力+1(最多+2)\n[WhenUse] 消耗4次[ChargeKhaki] 次数，硬币威力+2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>自身的速度高于目标或自身体力低于50%时，</u></b></mark></color>\n- 所有硬币变为[SuperCoin] \n- 造成的伤害量增加(与目标的速度差 × 15)%[TabExplain] (最多40%)\n<color=#ff6000><mark color=#ff000040><b><u>[DefeatDuel] 下回合获得1层[Binding] </u></b></mark></color>",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加4层[Laceration] "}]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加1层[ThreadDye] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1层[ThreadDye] "},
                    {"desc": "[OnSucceedAttack] 若该硬币为[SuperCoin] ，<color=#ff6000><mark color=#ff000040><b><u>自身的[ChargeKhaki] 次数增加4次</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    151904: {
        "levelList": [{
            "level": 1,
            "name": "平缝",
            "desc": "自身的速度高于目标时，造成的伤害量+20%\n自身的[ChargeKhaki] 强度每有2点，硬币威力+1(最多+2)\n[WhenUse] 消耗4次[ChargeKhaki] 次数，硬币威力+2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>自身的速度高于目标或自身体力低于50%时，</u></b></mark></color>\n- 所有硬币变为[SuperCoin] \n- 造成的伤害量增加(与目标的速度差 × 15)%[TabExplain] (最多40%)\n[WinDuel] 下回合获得1层[Agility] ",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加3次"}]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加1层[ThreadDye] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1层[ThreadDye] "},
                    {"desc": "[OnSucceedAttack] 若该硬币为[SuperCoin] ，<color=#ff6000><mark color=#ff000040><b><u>自身的[ChargeKhaki] 次数增加4次</u></b></mark></color>"}
                ]}
            ]
        }]
    },
    151905: {
        "levelList": [{
            "level": 1,
            "name": "三针彩虹包缝",
            "desc": "[WideAreaRampage] \n无论速度如何皆可与该技能拼点\n自身的[ChargeKhaki] 强度每有2点，最终威力+1(最多+3)\n[WhenUse] 消耗全部自身[ChargeKhaki] 次数，每消耗1次[ChargeKhaki] 次数，造成的伤害量+5%\n[WhenUse] 主要目标的[Laceration] 强度与[Laceration] 次数之和每有3点，硬币威力+1(最多+3)\n[DefeatDuel]\n- 获得10层[AttackDmgDown] 与4层[Paralysis] \n- 该技能造成的伤害不会使目标陷入混乱\n[EndSkillAll] <color=#ff6000><mark color=#ff000040><b><u>结束本回合</u></b></mark></color>",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 使目标的[Laceration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 使目标的[Laceration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 使目标的[Laceration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "该硬币命中所有攻击目标"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发1次目标的[Laceration] (使[Laceration] 次数减少1次)"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 下回合对目标施加3层[ThreadDye] "},
                    {"desc": "[OnSucceedAttack] 对持有[Inactible] 效果的目标生效以下效果"},
                    {"desc": "- 下回合使其陷入混乱状态"},
                    {"desc": "- 造成等同于该硬币最终伤害量20%的色欲伤害"}
                ]}
            ]
        }]
    },

    # 1495: 修补师阿内特 (Alterationist Annette)
    149501: {
        "levelList": [{
            "level": 1,
            "name": "修剪",
            "desc": "自身的[FinishedFabric] 20以上时，基础威力+1\n自身的[FinishedFabric] 40以上时，基础威力+2\n[WhenUse] 自身的[ChargeKhaki] 强度每有2点，硬币威力+1(最多+2)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeKhaki] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[ScissorsMark] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeKhaki] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[ScissorsMark] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加3层[ScissorsMark] "},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 下回合获得1层[FinishedFabric] </u></b></mark></color>"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若自身的[ChargeKhaki] 次数在12以上，则消耗4次[ChargeKhaki] 次数触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    149502: {
        "levelList": [{
            "level": 1,
            "name": "裁剪",
            "desc": "自身的[FinishedFabric] 20以上时，基础威力+1\n自身的[FinishedFabric] 40以上时，基础威力+2\n[WhenUse] 自身的[ChargeKhaki] 强度每有2点，硬币威力+1(最多+2)\n[WhenUse] 消耗4次自身的[ChargeKhaki] 次数，最终威力+2",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeKhaki] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[ScissorsMark] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeKhaki] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[ScissorsMark] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[ScissorsMark] "},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 下回合获得1层[FinishedFabric] </u></b></mark></color>"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若自身的[ChargeKhaki] 次数在12以上，则消耗4次[ChargeKhaki] 次数触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    149503: {
        "levelList": [{
            "level": 1,
            "name": "固定，随后依样裁剪",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n[WhenUse]\n- 若自身的[ChargeKhaki] 次数在10以上，则消耗10次[ChargeKhaki] 次数，硬币威力+2\n· 消耗最多20次自身剩余的[ChargeKhaki] 次数，每消耗1次数值，造成的伤害量+1%(最多20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- 自身的[FinishedFabric] 减少3层\n- 伤害量-75%\n- 获得4层[Paralysis] </u></b></mark></color>\n- 该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 自身的[ChargeKhaki] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加4点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 使目标的[Vibration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5层[ScissorsMark] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 下回合获得3层[FinishedFabric] </u></b></mark></color>"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    149504: {
        "levelList": [{
            "level": 1,
            "name": "斜向裁剪",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>无论速度如何皆可与该技能拼点</u></b></mark></color>\n[WhenUse]\n- 攻击加权值增加等同于[LargeTailoringShears] 数值的数值(最多3)\n- 若自身的[ChargeKhaki] 次数在10以上，则消耗10次[ChargeKhaki] 次数，硬币威力+2\n- 消耗最多20次自身剩余的[ChargeKhaki] 次数，每消耗1次数值，造成的伤害量+1%(最多20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- 自身的[FinishedFabric] 减少3层\n- 伤害量-90%\n- 获得4层[Paralysis] </u></b></mark></color>\n- 该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 若为主要目标，对目标施加5层[ScissorsMark] "},
                    {"desc": "[OnSucceedAttack] 触发1次[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 下回合获得1层[FinishedFabric] </u></b></mark></color>"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 若为主要目标，触发2次[VibrationExplosion] 。使目标的[Vibration] 次数减少2次"}
                ]}
            ]
        }]
    },
    149505: {
        "levelList": [{
            "level": 1,
            "name": "打版",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget] \n以[TailoringTarget] 为目标</u></b></mark></color>",
            "coinlist": [
                {"coindescs": [{"desc": "[SuperCoin] "}]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[OnSucceedAttack] 对目标施加9层[ScissorsMark] </u></b></mark></color>"}
                ]}
            ]
        }]
    },
    149506: {
        "levelList": [{
            "level": 1,
            "name": "链式包缝(Surfil à la chaîne)",
            "desc": "<color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget] \n以[TailoringTarget] 为目标</u></b></mark></color>\n自身的[LargeTailoringShears] 每有1层，\n最终威力+1，造成的伤害量+20%(分别最多3，60%)\n自身的[ChargeKhaki] 强度每有1点，\n造成的伤害量+4%(最多20%)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 目标罪人若\n- 装备了守备技能，则获得4层[Paralysis] 且该技能造成的伤害不会使目标陷入混乱\n- 未装备守备技能，则下回合获得10层[FinishedFabric] </u></b></mark></color>\n[EndSkill]\n- <color=#ff6000><mark=#ff000040><b><u>若进行了拼点，</u></b></mark></color>对目标施加等同于该罪人技能最终拼点威力一半的[DamagedFabric] (最多20)\n<color=#ff6000><mark=#ff000040><b><u>- 消耗目标的所有[ScissorsMark] </u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[EndBattle] 下回合获得1层[LargeTailoringShears] </u></b></mark></color>",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}
                ]},
                {"coindescs": [{"desc": "[SuperCoin] "}]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 触发1次[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发2次[VibrationExplosion] 。使目标的[Vibration] 次数减少2次"}
                ]}
            ]
        }]
    },

    # 1506: 黑派品牌经理 (Brand Manager)
    150601: {
        "levelList": [{
            "level": 1,
            "name": "定钉于此",
            "desc": "[WhenUse] 自身的[ChargeNoir] 强度每有3点，硬币威力+1(最多+3)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加5次"},
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加5次"},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "}
                ]}
            ]
        }]
    },
    150602: {
        "levelList": [{
            "level": 1,
            "name": "生钉吧",
            "desc": "[WhenUse] 自身的[ChargeNoir] 强度每有3点，硬币威力+1(最多+3)\n[DefeatDuel] 伤害量减少80%，且该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150603: {
        "levelList": [{
            "level": 1,
            "name": "敲击",
            "desc": "[WhenUse] 自身的[ChargeNoir] 强度每有3点，硬币威力+1(最多+3)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "}
                ]}
            ]
        }]
    },
    150604: {
        "levelList": [{
            "level": 1,
            "name": "默示",
            "desc": "[WinDuel] 使目标的[Vibration] 次数增加3次\n[WinDuel] 触发[VibrationExplosion] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Vulnerable] "},
                    {"desc": "<color=#ff6000><mark=#ff000040><b><u>[DefeatDuelAttack] 对目标施加1层[NoirShieldPiece] </u></b></mark></color>"}
                ]}
            ]
        }]
    },
    150605: {
        "levelList": [{
            "level": 1,
            "name": "宣示保存神域",
            "desc": "无论速度如何皆可与该技能拼点。使用该技能前不会陷入混乱\n\n[StartBattle] 敌方单位每装备1个守备技能，拼点威力-2(最多-10)\n\n[WhenUse] 主要目标若<color=#ff6000><mark=#ff000040><b><u>没有[NoirShieldPiece] ，该技能最终威力+5</u></b></mark></color>\n[WhenUse] 消耗所有自身的[ChargeNoir] 次数\n- 每消耗3次，最终威力+1\n- 造成的伤害量+(消耗值 × 5)%\n<color=#ff6000><mark=#ff000040><b><u>- 获得1层[NoirField] </u></b></mark></color>\n[DefeatDuel] 伤害量减少80%，且该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 若目标持有[NoirShieldPiece] ，"},
                    {"desc": "- 受到该硬币造成的最终伤害量-95%"},
                    {"desc": "- 该硬币造成的伤害不会使目标陷入混乱"},
                    {"desc": "- 消除目标的[NoirShieldPiece] ，对目标施加2层[VibrationResonance] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发3次[VibrationExplosion] 。使目标的[Vibration] 次数减少3次"},
                    {"desc": "[OnSucceedAttack] 造成等同于该硬币最终伤害量的混乱损伤"}
                ]}
            ]
        }]
    },
    150606: {
        "levelList": [{
            "level": 1,
            "name": "启示",
            "desc": "使用该技能前不会陷入混乱\n<color=#ff6000><mark=#ff000040><b><u>[StartBattle] 获得999层[NoirShieldUp] </u></b></mark></color>",
            "coinlist": []
        }]
    },
    150607: {
        "levelList": [{
            "level": 1,
            "name": "立约",
            "desc": "[SupportEnemy] \n\n[EndSkill] 若目标为友方单位，使其获得6层[AttackUp] \n[EndSkill] 目标友方单位发动随机攻击技能\n\n[DefeatDuel] 获得1层[Vulnerable] \n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] 自身的[NoirShieldUp] 减少150层</u></b></mark></color>",
            "coinlist": []
        }]
    },
    150608: {
        "levelList": [{
            "level": 1,
            "name": "截断诞生。",
            "desc": "无论速度如何皆可与该技能拼点。使用该技能前不会陷入混乱\n[WhenUse] 自身的[NoirShieldUp] 每有100层，最终威力+1\n[WhenUse] 若目标持有[NoirShieldPiece] ，拼点威力-5\n[DefeatDuel] 该技能造成的伤害量-80%，且该技能造成的伤害不会使目标陷入混乱\n[EndSkill] 结束本回合",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加2层[NoirNail] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 自身的[NoirShieldUp] 每有200层，追加触发1次[VibrationExplosion] (最多4次)"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发3次[VibrationExplosion] 。"}
                ]}
            ]
        }]
    },
    150609: {
        "levelList": [{
            "level": 1,
            "name": "连番敲打，截断诞生！",
            "desc": "无论速度如何皆可与该技能拼点。使用该技能前不会陷入混乱\n\n[WhenUse] 消耗所有自身的[ChargeNoir] 次数\n- 每消耗3次，最终威力+1\n- 造成的伤害量+(消耗值 × 5)%\n\n[WhenUse] 若主要目标持有[NoirShieldPiece] ，拼点威力-5\n[WhenUse] 若主要目标没有[NoirShieldPiece] ，该技能最终威力+5\n[DefeatDuel] 该技能造成的伤害量-80%，且该技能造成的伤害不会使目标陷入混乱\n[EndSkill] 结束本回合",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加1层[NoirNail] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加2层[NoirNail] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 若目标持有[NoirShieldPiece] ，"},
                    {"desc": "- 受到该硬币造成的最终伤害量-95%"},
                    {"desc": "- 该硬币造成的伤害不会使目标陷入混乱"},
                    {"desc": "- 消除目标的[NoirShieldPiece] ，对目标施加2层[VibrationResonance] "},
                    {"desc": "[OnSucceedAttack] 对目标施加5点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150610: {
        "levelList": [{
            "level": 1,
            "name": "信徒们，回应召唤吧",
            "desc": "[StartBattle] 下回合召唤5名黑派友方单位(除自身外的场上友方单位数量无法超过5名)\n[DefeatDuel] 伤害量减少80%，且该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}
                ]}
            ]
        }]
    },

    # 1504: 法兰绒 (Flannel)
    150401: {
        "levelList": [{
            "level": 1,
            "name": "购买记录呢？",
            "desc": "造成的伤害量+(自身护盾数值)%(最多20%)\n[WhenUse] 自身的[ChargeNoir] 次数增加2次",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}]}
            ]
        }]
    },
    150402: {
        "levelList": [{
            "level": 1,
            "name": "购买资格是？",
            "desc": "[WhenUse] 自身的[ChargeNoir] 次数与目标的[Vibration] 之和每有6点，硬币威力+1(最多+2)\n[WhenUse] 自身的[ChargeNoir] 次数增加3次\n[WinDuel] 自身的[ChargeNoir] 次数增加2次\n[WhenUse] 若自身的[ChargeNoir] 强度在3以上，最后一枚硬币变为[SuperCoin] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}
                ]}
            ]
        }]
    },
    150403: {
        "levelList": [{
            "level": 1,
            "name": "压花[法兰绒]",
            "desc": "造成的伤害量+(自身护盾数值)%(最多50%)\n[WhenUse] 目标的[Vibration] 每有6点，最终威力+1(最多+2)\n[WhenUse] 消耗自身最多15次[ChargeNoir] 次数，\n获得相当于体力上限(消耗的[ChargeNoir] 次数 × 2)%的维持至下回合的护盾\n[WhenUse] 若消耗了10次以上自身的[ChargeNoir] 次数，硬币威力+2，所有硬币变为[SuperCoin] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 自身的[ChargeNoir] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加2次"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 转换为[VibrationCollapse] [Switch_Vibration] "},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次\n- 自身的[ChargeNoir] 强度每有2点，追加触发1次该效果(最多2次)"}
                ]}
            ]
        }]
    },
    150404: {
        "levelList": [{
            "level": 1,
            "name": "面料强化",
            "desc": "对友方单位使用。对友方单位造成的伤害量固定为0\n[WhenUse] 目标的[Vibration] 每有4点，最终威力+2(最多+6)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 本回合与下回合获得3层[DefenseUp] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Charge] 次数增加等同于自身[ChargeNoir] 次数的数值\n- 若目标的[Charge] 次数达到上限，下回合使其获得3层[DefenseUp] 与5层[NoirBindArmor] "}
                ]}
            ]
        }]
    },
    150405: {
        "levelList": [{
            "level": 1,
            "name": "为了保全",
            "desc": "对友方单位使用。对友方单位造成的伤害量固定为0\n[WhenUse] 目标的[Vibration] 每有4点，最终威力+2(最多+6)\n[WhenUse] 若自身的[ChargeNoir] 强度在3以上，所有硬币变为[SuperCoin] \n[WhenUse] 若自身的[ChargeNoir] 次数低于10次，获得[ChargeNoir] 次数使其达到10次，每获得2次数值，获得1层[Vulnerable] \n[DefeatDuel] 消耗自身一半的[ChargeNoir] 次数\n[EndSkill] 消耗自身全部[ChargeNoir] 次数",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 本回合与下回合获得2层[DefenseUp] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Charge] 次数增加等同于自身[ChargeNoir] 次数的数值\n- 若目标的[ChargeNoir] 次数达到上限，下回合使其获得3层[DefenseUp] 与5层[NoirBindArmor] "}
                ]}
            ]
        }]
    },

    # 1505: 黑派时装屋 (Maison)
    150501: {
        "levelList": [{
            "level": 1,
            "name": "你的标价是？",
            "desc": "[WhenUse] 自身的[ChargeNoir] 次数增加2次",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}]}
            ]
        }]
    },
    150502: {
        "levelList": [{
            "level": 1,
            "name": "真是破绽百出呢",
            "desc": "[WhenUse] 自身的[ChargeNoir] 次数与目标的[Vibration] 之和每有6点，硬币威力+1(最多+2)\n[WhenUse] 自身的[ChargeNoir] 次数增加3次\n[WinDuel] 自身的[ChargeNoir] 次数增加2次\n[WhenUse] 若自身的[ChargeNoir] 强度在3以上，最后一枚硬币变为[SuperCoin] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 自身的[ChargeNoir] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150503: {
        "levelList": [{
            "level": 1,
            "name": "压花[毛毡]",
            "desc": "造成的伤害量+(自身护盾数值)%(最多50%)\n[WhenUse] 目标的[Vibration] 每有6点，最终威力+1(最多+2)\n[WhenUse] 消耗自身最多15次[ChargeNoir] 次数，\n获得相当于体力上限(消耗的[ChargeNoir] 次数 × 2)%的维持至下回合的护盾\n[WhenUse] 若消耗了10次以上自身的[ChargeNoir] 次数，硬币威力+2，所有硬币变为[SuperCoin] ",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加1点[Vibration] "},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 对目标施加1点[Vibration] "}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 转换为[VibrationCollapse] [Switch_Vibration] "},
                    {"desc": "[OnSucceedAttack] 若消耗了10次以上[ChargeNoir] 次数，触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "[UnBrokenCoinOnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },
    150504: {
        "levelList": [{
            "level": 1,
            "name": "压花[回响]",
            "desc": "持有护盾期间受到敌人攻击时，对敌人造成等同于(自身[ChargeNoir] 强度 × [NoirBindArmor] 数值)的伤害\n[WhenUse] [ChargeNoir] 次数增加3次",
            "coinlist": []
        }]
    },

    # 1488: 控制者 (Controller)
    148801: {
        "levelList": [{
            "level": 1,
            "name": "剥皮",
            "desc": "",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加3次"}
                ]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "}
                ]}
            ]
        }]
    },
    148802: {
        "levelList": [{
            "level": 1,
            "name": "去肉",
            "desc": "场上<color=#ff6000><mark=#ff000040><b><u>每存在1名存活的被鞣制的囚犯，造成的伤害量+10%</u></b></mark></color>\n[DefeatDuel] 该技能造成的伤害量-80%，且该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加2次"},
                    {"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加2次"}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Laceration] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 下回合对目标施加2层[Vulnerable] "}
                ]}
            ]
        }]
    },
    148803: {
        "levelList": [{
            "level": 1,
            "name": "脑油鞣制",
            "desc": "无法变更目标\n该技能优先指定体力最低的友方单位为目标\n\n若未攻击指定的目标，则取消技能",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 若目标为友方单位，生效以下效果\n- 将目标重新塞回后背\n- 自身恢复体力上限1%的体力\n- 理智值恢复20点\n- 本回合与下回合获得2层[AttackDmgUp] "}
                ]}
            ]
        }]
    },
    148804: {
        "levelList": [{
            "level": 1,
            "name": "片皮",
            "desc": "[EndBattle] 下回合最多召唤2名被鞣制的囚犯，并施加[B3FreshMob] \n\n- 场上存活的被鞣制的囚犯无法超过6名\n- 每召唤1名被鞣制的囚犯，消耗体力上限0.5%的体力\n- <color=#ff6000><mark=#ff000040><b><u>满足以下条件时停用该效果</u></b></mark></color>\n· 使用该技能的槽位被2个以上攻击技能指定为主要目标\n· 场上存活的被鞣制的囚犯在6名以上",
            "coinlist": [{"coindescs": [{"desc": "[SuperCoin] "}]}]
        }]
    },
    148805: {
        "levelList": [{
            "level": 1,
            "name": "强力片皮",
            "desc": "[EndBattle] 下回合最多召唤4名被鞣制的囚犯，并施加[B3FreshMob] \n- 场上存活的被鞣制的囚犯无法超过6名\n- 每召唤1名被鞣制的囚犯，消耗体力上限0.5%的体力\n\n[StartBattle] 下回合使所有友方单位获得1层[AttackDmgUp] ",
            "coinlist": [{"coindescs": [{"desc": "[SuperCoin] "}]}]
        }]
    },
    148806: {
        "levelList": [{
            "level": 1,
            "name": "原罪脑油转鼓",
            "desc": "场上<color=#ff6000><mark=#ff000040><b><u>每存在1名存活的被鞣制的囚犯，造成的伤害量+10%</u></b></mark></color>\n[StartBattle] 使除自身外的所有友方单位获得2层[Enhancement] \n[WhenUse] 若自身当前体力低于体力上限50%，场上每存在1名被鞣制的囚犯，最终威力+1\n[DefeatDuel] 该技能造成的伤害量-80%，且该技能造成的伤害不会使目标陷入混乱",
            "coinlist": [
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "}
                ]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 对目标施加3层[Burst] "}
                ]}
            ]
        }]
    },
    148807: {
        "levelList": [{
            "level": 1,
            "name": "惩戒·打磨·收尾",
            "desc": "[CantDuel] \n该技能不触发守备技能(包括可拼点守备)\n\n[EndSkill] 命令3名随机被鞣制的囚犯对目标使用随机技能(未陷入混乱的友方单位优先)",
            "coinlist": [
                {"coindescs": [
                    {"desc": "造成的伤害量+100%"},
                    {"desc": "[OnSucceedAttack] 对目标施加10点[Vibration] "},
                    {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                    {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                ]}
            ]
        }]
    },

    # 1491: 被鞣制的囚犯
    149101: {
        "levelList": [{
            "level": 1,
            "name": "泼洒脑油",
            "desc": "",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2层[Burst] "}]},
                {"coindescs": [{"desc": "[OnSucceedAttack] 下回合对目标施加2层[Reduction] "}]}
            ]
        }]
    },
    149102: {
        "levelList": [{
            "level": 1,
            "name": "涂抹脑油",
            "desc": "",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Burst] 次数增加2次"}]},
                {"coindescs": [
                    {"desc": "[OnSucceedAttack] 下回合对目标施加5层[DefenseDown] "},
                    {"desc": "[OnSucceedAttack] 下回合对目标施加2层[Paralysis] "}
                ]}
            ]
        }]
    },
    149103: {
        "levelList": [{
            "level": 1,
            "name": "赎罪压花",
            "desc": "",
            "coinlist": [
                {"coindescs": [{"desc": "[OnSucceedAttack] 恢复控制者部位及本体体力上限1%的体力"}]},
                {"coindescs": [
                    {"desc": "[SuperCoin] "},
                    {"desc": "[OnSucceedAttack] 恢复控制者部位及本体体力上限1%的体力"}
                ]}
            ]
        }]
    }
}

out_data = {"dataList": []}
for item in kr_data:
    sid = item["id"]
    t = trans.get(sid, {})
    new_item = {"id": sid, "levelList": []}
    for lv_idx, lv in enumerate(item["levelList"]):
        t_lv = t.get("levelList", [{}])[lv_idx] if lv_idx < len(t.get("levelList", [])) else {}
        new_lv = {
            "level": lv["level"],
            "name": t_lv.get("name", lv.get("name", "")),
            "desc": t_lv.get("desc", lv.get("desc", ""))
        }
        if "abName" in lv:
            new_lv["abName"] = t_lv.get("abName", lv["abName"])
            
        coinlist = []
        for c_idx, c in enumerate(lv.get("coinlist", [])):
            t_c = t_lv.get("coinlist", [{}])[c_idx] if c_idx < len(t_lv.get("coinlist", [])) else {}
            new_c = {}
            if "coindescs" in c:
                new_c["coindescs"] = []
                for cd_idx, cd in enumerate(c["coindescs"]):
                    t_cd = t_c.get("coindescs", [{}])[cd_idx] if cd_idx < len(t_c.get("coindescs", [])) else {}
                    new_c["coindescs"].append({
                        "desc": t_cd.get("desc", cd.get("desc", ""))
                    })
            coinlist.append(new_c)
        new_lv["coinlist"] = coinlist
        new_item["levelList"].append(new_lv)
    out_data["dataList"].append(new_item)

out_path = os.path.join(WORKSPACE_DIR, "Skills_Abnormality-a1c10p2.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Skills_Abnormality-a1c10p2.json: written {len(out_data['dataList'])} skills.")
