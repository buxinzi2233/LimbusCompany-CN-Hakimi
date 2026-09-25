#!/usr/bin/env python3
import json
import os

WORKSPACE_DIR = "workspace/LLC_zh-CN"

def merge_passives():
    path = os.path.join(WORKSPACE_DIR, "Passives.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # filter out existing 10917 IDs to re-apply clean
    data["dataList"] = [x for x in data["dataList"] if x["id"] not in [1091701, 1091702, 1091721]]
    
    new_entries = [
        {
            "id": 1091701,
            "name": "修补室的花剪声",
            "desc": "回合结束时，下回合获得等同于自身[ChargeKhaki] 次数的护盾\n自身[ChargeKhaki] 强度在2/3/5以上时，基础技能最终威力+1/+2/+3",
            "summary": "基础技能最终威力增加[TabExplain] "
        },
        {
            "id": 1091702,
            "name": "漂流惯性",
            "desc": "战斗中累计消耗10次自身[ChargeKhaki] 次数时，获得1层[ChargeKhaki] 强度\n\n除自身外持有[NoirScissorShield] 的友方单位攻击结束时，对目标发动“打版”(每回合最多1次)\n- [BeforeUse] 若发动目标的[NoirScissorAlly] 在2层以上，则改为发动“裁剪”(每回合最多1次)",
            "summary": "发动追加攻击"
        },
        {
            "id": 1091721,
            "name": "一把剪刀",
            "desc": "速度最快的1名友方单位的基础斩击技能伤害量+10% ",
            "summary": "额外斩击伤害",
            "flavor": "将所有剪刀中最钟爱的一把，赠予你。"
        }
    ]
    
    data["dataList"].extend(new_entries)
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Passives.json: updated entries")

def merge_passive_ego():
    path = os.path.join(WORKSPACE_DIR, "Passive_Ego.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["dataList"] = [x for x in data["dataList"] if x["id"] not in [2061011, 2091011]]
    
    new_entries = [
        {
            "id": 2061011,
            "name": "无人受伤的都市",
            "desc": "[Charge] 次数上限+5\n\n消耗[Charge] 次数或特殊[Charge] 的技能3(E.G.O技能除外)造成的伤害量+10%\n\n回合结束时，若本回合未受到伤害，则理智值恢复4点\n- 若自身持有2个以上减算硬币基础攻击技能，则改为理智值减少4点(该效果不会使理智值低于-40)"
        },
        {
            "id": 2091011,
            "name": "分裂的触觉",
            "desc": "获得[Breath] 强度或次数时，自身的[Breath] 次数增加1次(每回合最多2次)\n\n若自身为[PersonalityBreath] 或[PersonalityVibration] ，基础攻击加权值为1或[WideAreaRampage] 的基础技能造成的伤害量+10%\n\n攻击结束时，若目标处于混乱状态或已阵亡，则下回合将相当于目标持有的[Vibration] 强度1/3分配施加给其他随机敌方单位(向上取整，若是集中战斗，则判定为部位)\n- 该效果不与E.G.O饰品“镜反射触觉联觉”的效果叠加触发"
        }
    ]
    
    data["dataList"].extend(new_entries)
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Passive_Ego.json: updated entries")

def merge_skills_personality_09():
    path = os.path.join(WORKSPACE_DIR, "Skills_personality-09.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["dataList"] = [x for x in data["dataList"] if not (1091700 <= x["id"] < 1091800)]
    
    new_skills = [
        {
            "id": 1091701,
            "levelList": [
                {
                    "level": 1,
                    "name": "精修(Retouche)",
                    "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[EndSkill] 若目标为友方单位，则使其获得3次[Charge] ，获得1层[AttackUp] \n[EndSkill] 若目标为友方单位，则触发以下效果(每回合最多1次)\n- 使其获得自身体力上限5%的护盾(至少为1)\n- 使其获得1层[NoirScissorShield] \n- 若目标为[PersonalityCharge] ，则使其获得1层[Enhancement] ",
                    "coinlist": [{"coindescs": []}]
                },
                {
                    "level": 2,
                    "name": "精修(Retouche)",
                    "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[EndSkill] 若目标为友方单位，则使其获得<style=\"highlight\">4次</style>[Charge] ，获得1层[AttackUp] \n[EndSkill] 若目标为友方单位，则触发以下效果(每回合最多1次)\n- 使其获得自身体力上限5%的护盾(至少为1)\n- 使其获得1层[NoirScissorShield] \n- 若目标为[PersonalityCharge] ，则使其获得1层[Enhancement] <style=\"highlight\"></style>",
                    "coinlist": [{"coindescs": []}]
                },
                {
                    "level": 4,
                    "name": "精修(Retouche)",
                    "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[EndSkill] 若目标为友方单位，则使其获得4次[Charge] ，获得1层[AttackUp] \n[EndSkill] 若目标为友方单位，则触发以下效果<style=\"highlight\">(每回合最多2次)</style>\n- 使其获得自身体力上限<style=\"highlight\">10%</style>的护盾(至少为1)\n- 使其获得1层[NoirScissorShield] \n- 若目标为[PersonalityCharge] ，则使其获得2层[Enhancement] ",
                    "coinlist": [{"coindescs": []}]
                }
            ]
        },
        {
            "id": 1091702,
            "levelList": [
                {
                    "level": 1,
                    "name": "固定，随后依样裁剪",
                    "desc": "[StartBattle] 使除自身外编队顺序最靠前的1名友方单位(充能 人格优先)获得2层[AttackUp] ，并使其获得自身体力上限5%的护盾(至少为1，每回合最多1次)\n- 若目标为[PersonalityCharge] ，则使其额外获得1层[AttackUp] ，额外获得自身体力上限5%的护盾\n\n[WhenUse] 若目标的[Vibration] 强度在6以上，则硬币威力+1\n[WhenUse] 消耗5次自身的[ChargeKhakiAlly] 次数，使最终威力+2",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[ChargeKhakiAlly] 次数增加6次"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加2次"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}]}
                    ]
                },
                {
                    "level": 2,
                    "name": "固定，随后依样裁剪",
                    "desc": "[StartBattle] 使<style=\"highlight\">自身以及</style>除自身外编队顺序最靠前的1名友方单位(充能 人格优先)获得2层[AttackUp] ，并使其获得自身体力上限5%的护盾(至少为1，每回合最多1次)\n- 若目标为[PersonalityCharge] ，则使其额外获得1层[AttackUp] ，额外获得自身体力上限5%的护盾\n\n[WhenUse] 若目标的[Vibration] 强度在6以上，则硬币威力+1\n[WhenUse] 消耗5次自身的[ChargeKhakiAlly] 次数，使最终威力+2",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[ChargeKhakiAlly] 次数增加6次<style=\"highlight\"></style>"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加2次<style=\"highlight\"></style>"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次<style=\"highlight\"></style>"}]}
                    ]
                },
                {
                    "level": 4,
                    "name": "固定，随后依样裁剪",
                    "desc": "[StartBattle] 使自身以及除自身外编队顺序最靠前的1名友方单位(充能 人格优先)、<style=\"highlight\">当前体力比例最低的1名友方单位</style>获得2层[AttackUp] ，并使其获得自身体力上限5%的护盾(至少为1，每回合最多1次)\n- 若目标为[PersonalityCharge] ，则使其额外获得1层[AttackUp] ，额外获得自身体力上限5%的护盾\n\n<style=\"highlight\">[WhenUse] 目标的[Vibration] 强度每有6点，硬币威力+1(最多+2)</style>\n[WhenUse] 消耗5次自身的[ChargeKhakiAlly] 次数，使最终威力+2",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[ChargeKhakiAlly] 次数增加6次<style=\"highlight\"></style>"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加2次<style=\"highlight\"></style>"}]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次<style=\"highlight\"></style>"},
                            {"desc": "[OnSucceedAttack] 对目标施加1层[AmberResistDown] (每回合最多1次)<style=\"highlight\"></style>"}
                        ]}
                    ]
                }
            ]
        },
        {
            "id": 1091703,
            "levelList": [
                {
                    "level": 3,
                    "name": "斜向裁剪",
                    "desc": "自身每有1层[NoirScissorCut] ，造成的伤害量+15%(最多30%)\n\n[StartBattle] 使除自身外编队顺序最靠前的1名友方单位(充能 人格优先)、当前体力比例最低的1名友方单位获得1层[NoirScissorShield] ，并使其获得自身体力上限5%的护盾(至少为1，每回合最多1次)\n\n[WhenUse] 若目标的[Vibration] 强度在6以上，则硬币威力+1\n[WhenUse] 自身的[ChargeKhakiAlly] 强度每有3点，最终威力+1(最多+2)\n[WhenUse] 消耗5次自身的[ChargeKhakiAlly] 次数，使最终威力+2\n\n[EndSkill] 自身的[ChargeKhakiAlly] 次数增加5次",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"},
                            {"desc": "[OnSucceedAttack] 对目标施加1层[NoirScissorAlly] "}
                        ]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}
                        ]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加1层[NoirScissorAlly] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                            {"desc": "[OnSucceedAttack] 若自身的[ChargeKhakiAlly] 次数在5以上，则消耗5次触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                },
                {
                    "level": 4,
                    "name": "斜向裁剪",
                    "desc": "自身每有1层[NoirScissorCut] ，造成的伤害量<style=\"highlight\">+30%(最多60%)</style>\n\n[StartBattle] 使自身以及除自身外编队顺序最靠前的1名友方单位(充能 人格优先)、当前体力比例最低的1名友方单位获得1层[NoirScissorShield] ，并使其获得自身体力上限<style=\"highlight\">10%</style>的护盾(至少为1，每回合最多1次)\n\n<style=\"highlight\">[WhenUse] 目标的[Vibration] 强度每有6点，硬币威力+1(最多+2)</style>\n[WhenUse] 自身的[ChargeKhakiAlly] 强度每有3点，最终威力+1(最多+2)\n[WhenUse] 消耗5次自身的[ChargeKhakiAlly] 次数，使最终威力+2\n\n[EndSkill] 自身的[ChargeKhakiAlly] 次数增加5次",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加3次"},
                            {"desc": "[OnSucceedAttack] 对目标施加1层[NoirScissorAlly] "}
                        ]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}
                        ]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加1层[NoirScissorAlly] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"},
                            {"desc": "[OnSucceedAttack] 若自身的[ChargeKhakiAlly] 次数在5以上，则消耗5次触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                }
            ]
        },
        {
            "id": 1091704,
            "levelList": [
                {
                    "level": 1,
                    "name": "修剪",
                    "desc": "[DuelCounter] \n[StartBattle] 自身的[ChargeKhakiAlly] 次数增加5次(每回合最多2次)\n[StartBattle] 使自身以及除自身外当前体力比例最低的2名友方单位获得自身体力上限5%的护盾(至少为1，每回合最多1次)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}]}
                    ]
                },
                {
                    "level": 4,
                    "name": "修剪",
                    "desc": "[DuelCounter] \n[StartBattle] 自身的[ChargeKhakiAlly] 次数增加5次(每回合最多2次)\n[StartBattle] 使自身以及除自身外当前体力比例最低的2名友方单位获得自身体力上限<style=\"highlight\">10%</style>的护盾(至少为1，每回合最多1次)\n\n<style=\"highlight\">[WhenUse] 自身的[ChargeKhakiAlly] 次数每有5次，拼点威力+1(最多+4)</style>",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}]}
                    ]
                }
            ]
        },
        {
            "id": 1091705,
            "levelList": [
                {
                    "level": 1,
                    "name": "打版",
                    "desc": "[CantDuel] \n[WhenUse] 自身的[ChargeKhakiAlly] 次数增加3次",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 若自身的[ChargeKhakiAlly] 强度在3以上，则重复投掷该硬币(每个技能最多1次)"},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 对目标施加1层[NoirScissorAlly] "}
                        ]}
                    ]
                }
            ]
        },
        {
            "id": 1091706,
            "levelList": [
                {
                    "level": 1,
                    "name": "裁剪",
                    "desc": "[CantDuel] \n[WhenUse] 自身的[ChargeKhakiAlly] 强度每有3点，最终威力+1(最多+2)\n[WhenUse] 自身的[ChargeKhakiAlly] 次数增加5次\n\n[EndSkill] 消耗目标的2层[NoirScissorAlly] \n[EndSkill] 自身获得1层[NoirScissorCut] ",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}]}
                    ]
                }
            ]
        }
    ]
    
    data["dataList"].extend(new_skills)
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Skills_personality-09.json: updated skills")

def merge_skills_ego_personality_06():
    path = os.path.join(WORKSPACE_DIR, "Skills_Ego_Personality-06.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["dataList"] = [x for x in data["dataList"] if x["id"] not in [2061011, 2061021]]
    
    new_skills = [
        {
            "id": 2061011,
            "levelList": [
                {
                    "level": 1,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "[BeforeAttack] 自身的[Charge] 次数增加1次\n[BeforeAttack] 消耗自身最多6次[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得5层[ChargeForceField] (最多5名，向下取整)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}]},
                        {}
                    ]
                },
                {
                    "level": 3,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "<style=\"highlight\">[WhenUse] 自身的[Charge] 强度每有1点，<noparse>拼点威力增加</noparse>1点(最多2点)</style>\n[BeforeAttack] 自身的[Charge] 次数增加<style=\"highlight\">3次</style>\n[BeforeAttack] 消耗自身最多<style=\"highlight\">8次</style>[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得5层[ChargeForceField] (最多<style=\"highlight\">6名</style>，向下取整)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}]},
                        {"coindescs": [{"desc": "<style=\"highlight\">[OnSucceedAttack] 对目标施加1层[PhotoElectricity] </style>"}]}
                    ]
                },
                {
                    "level": 4,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "[WhenUse] 自身的[Charge] 强度每有1点，<noparse>拼点威力增加</noparse>1点(最多<style=\"highlight\">3点</style>)\n[BeforeAttack] 自身的[Charge] 次数增加<style=\"highlight\">5次</style>\n[BeforeAttack] 消耗自身最多<style=\"highlight\">10次</style>[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得5层[ChargeForceField] (最多<style=\"highlight\">7名</style>，向下取整)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">2层</style>[PhotoElectricity] "}]}
                    ]
                }
            ]
        },
        {
            "id": 2061021,
            "levelList": [
                {
                    "level": 1,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "[CantIdentify] \n随机指定目标\n对带有护盾的目标造成的伤害量+15%\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-6(最多-12)\n[BeforeAttack] 自身的[Charge] 次数增加3次\n[BeforeAttack] 消耗自身最多6次[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得7层[ChargeForceField] (最多5名，向下取整)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnStartCoin] 消耗自身最多10次[Charge] 次数，使该硬币的<noparse>最终威力增加</noparse>消耗的数值"}
                        ]}]
                },
                {
                    "level": 3,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "[CantIdentify] \n随机指定目标\n对带有护盾的目标造成的伤害量+<style=\"highlight\">20</style>%\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-6(最多-12)\n<style=\"highlight\">[BeforeAttack] 自身的[Charge] 强度每有1点，<noparse>最终威力增加</noparse>1点(最多2点)</style>\n[BeforeAttack] 自身的[Charge] 次数增加<style=\"highlight\">4次</style>\n[BeforeAttack] 消耗自身最多<style=\"highlight\">8次</style>[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得7层[ChargeForceField] (最多<style=\"highlight\">6名</style>，向下取整)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnStartCoin] 消耗自身最多10次[Charge] 次数，使该硬币的<noparse>最终威力增加</noparse>消耗的数值"},
                            {"desc": "<style=\"highlight\">[OnSucceedAttack] 对目标施加1层[PhotoElectricity] </style>"}
                        ]}]
                },
                {
                    "level": 4,
                    "name": "宣告拒绝",
                    "abName": "梅特罗波拉利斯的居民",
                    "desc": "[CantIdentify] \n随机指定目标\n对带有护盾的目标造成的伤害量+<style=\"highlight\">25</style>%\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-6(最多-12)\n[BeforeAttack] 自身的[Charge] 强度每有1点，<noparse>最终威力增加</noparse>1点(最多<style=\"highlight\">3点</style>)\n[BeforeAttack] 自身的[Charge] 次数增加<style=\"highlight\">5次</style>\n[BeforeAttack] 消耗自身最多<style=\"highlight\">10次</style>[Charge] 次数，使自身以及除自身外的(1 + 消耗的[Charge] 次数/2)名随机友方单位获得7层[ChargeForceField] (最多<style=\"highlight\">7名</style>，向下取整)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 自身的[Charge] 次数增加2次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnStartCoin] 消耗自身最多10次[Charge] 次数，使该硬币的<noparse>最终威力增加</noparse>消耗的数值"},
                            {"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">2层</style>[PhotoElectricity] "}
                        ]}]
                }
            ]
        }
    ]
    
    data["dataList"].extend(new_skills)
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Skills_Ego_Personality-06.json: updated skills")

def merge_skills_ego_personality_09():
    path = os.path.join(WORKSPACE_DIR, "Skills_Ego_Personality-09.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["dataList"] = [x for x in data["dataList"] if x["id"] not in [2091011, 2091021]]
    
    new_skills = [
        {
            "id": 2091011,
            "levelList": [
                {
                    "level": 1,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多+2)\n[BeforeAttack] 自身获得(2 + 最大共鸣数)点[Breath] (最多8点)\n[BeforeAttack] 自身的[Breath] 次数增加2次\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加2点[Vibration] "}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"}]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加2层[AttackDown] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                },
                {
                    "level": 3,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多<style=\"highlight\">+3</style>)\n[BeforeAttack] 自身获得(<style=\"highlight\">3</style> + 最大共鸣数)点[Breath] (最多8点)\n[BeforeAttack] 自身的[Breath] 次数增加<style=\"highlight\">3次</style>\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">3点</style>[Vibration] "}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加<style=\"highlight\">2次</style>"}]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加2层[AttackDown] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                },
                {
                    "level": 4,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多<style=\"highlight\">+4</style>)\n[BeforeAttack] 自身获得(<style=\"highlight\">4</style> + 最大共鸣数)点[Breath] (最多8点)\n[BeforeAttack] 自身的[Breath] 次数增加<style=\"highlight\">4次</style>\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [{"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">4点</style>[Vibration] "}]},
                        {"coindescs": [{"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加<style=\"highlight\">3次</style>"}]},
                        {"coindescs": [
                            {"desc": "[OnSucceedAttack] 对目标施加2层[AttackDown] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                }
            ]
        },
        {
            "id": 2091021,
            "levelList": [
                {
                    "level": 1,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "[CantIdentify] \n随机指定目标\n自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多+2)\n[BeforeAttack] 自身获得(2 + 最大共鸣数)点[Breath] (最多10点)\n[BeforeAttack] 自身的[Breath] 次数增加2次\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-4(最多-12)\n[BeforeAttack] 若自身的[Breath] 次数在10以上，则消耗4次自身的[Breath] 次数，对主要目标造成的暴击伤害量+20%\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 对目标施加3点[Vibration] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 对目标施加3层[AttackDown] "},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]}
                    ]
                },
                {
                    "level": 3,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "[CantIdentify] \n随机指定目标\n自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多<style=\"highlight\">+3</style>)\n[BeforeAttack] 自身获得(<style=\"highlight\">3</style> + 最大共鸣数)点[Breath] (最多10点)\n[BeforeAttack] 自身的[Breath] 次数增加<style=\"highlight\">3次</style>\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-4(最多-12)\n[BeforeAttack] 若自身的[Breath] 次数在10以上，则消耗4次自身的[Breath] 次数，对主要目标造成的暴击伤害量+<style=\"highlight\">30</style>%\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">4点</style>[Vibration] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "<style=\"highlight\">[OnSucceedAttack] 使目标的[Vibration] 次数增加1次</style>"},
                            {"desc": "[OnSucceedAttack] 对目标施加3层[AttackDown] <style=\"highlight\"></style>"},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次<style=\"highlight\"></style>"}
                        ]}
                    ]
                },
                {
                    "level": 4,
                    "name": "镜反射触觉",
                    "abName": "迷失之心",
                    "desc": "[CantIdentify] \n随机指定目标\n自身的[Breath] 强度与主要目标的[Vibration] 强度之和每有6点，拼点威力+1(最多<style=\"highlight\">+4</style>)\n[BeforeAttack] 自身获得(<style=\"highlight\">4</style> + 最大共鸣数)点[Breath] (最多10点)\n[BeforeAttack] 自身的[Breath] 次数增加<style=\"highlight\">4次</style>\n[BeforeAttack] 每有1枚被破坏的硬币，基础威力-4(最多-12)\n[BeforeAttack] 若自身的[Breath] 次数在10以上，则消耗4次自身的[Breath] 次数，对主要目标造成的暴击伤害量+<style=\"highlight\">40</style>%\n[EndSkill] 对攻击目标中的随机敌方单位分配施加(1 + 最大共鸣数)层[EmpathicDistressAlly] ，每次1层(最多5层)",
                    "coinlist": [
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 对目标施加<style=\"highlight\">5点</style>[Vibration] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加1次"},
                            {"desc": "[OnSucceedAttack] 若目标的[Vibration] 次数在4以上，则触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次"}
                        ]},
                        {"coindescs": [
                            {"desc": "[SuperCoin] "},
                            {"desc": "[OnSucceedAttack] 使目标的[Vibration] 次数增加<style=\"highlight\">2次</style>"},
                            {"desc": "[OnSucceedAttack] 对目标施加3层[AttackDown] <style=\"highlight\"></style>"},
                            {"desc": "[OnSucceedAttack] 触发[VibrationExplosion] 。使目标的[Vibration] 次数减少1次<style=\"highlight\"></style>"}
                        ]}
                    ]
                }
            ]
        }
    ]
    
    data["dataList"].extend(new_skills)
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Skills_Ego_Personality-09.json: updated skills")

if __name__ == "__main__":
    merge_passives()
    merge_passive_ego()
    merge_skills_personality_09()
    merge_skills_ego_personality_06()
    merge_skills_ego_personality_09()
