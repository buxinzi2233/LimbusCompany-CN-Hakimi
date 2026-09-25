#!/usr/bin/env python3
import json
import os

WORKSPACE_DIR = "workspace/LLC_zh-CN"

passives_assist = {
  "dataList": [
    {
      "id": 40004101,
      "name": "小小的赤红之神",
      "desc": "获得[Charge] 效果时，改为获得[ChargeRouge] \n\n舞台开始时，获得1层[ChargeRouge] 强度\n\n回合开始时，若自身的[ChargeRouge] 强度在2以上，则使自身的[ChargeRouge] 次数增加(自身的[ChargeRouge] 强度 × 2)次",
      "summary": "获得[ChargeRouge] ",
      "flavor": "虽尚且稚嫩，但无疑拥有着神格。"
    },
    {
      "id": 40004102,
      "name": "搏动的本性",
      "desc": "战斗中每次触发[Laceration] 效果时，使自身的[ChargeRouge] 次数增加1次",
      "summary": "[ChargeRouge] 次数增加",
      "flavor": "为什么每次看到血，我的心脏就跳个不停呢……？"
    },
    {
      "id": 40004103,
      "name": "旅程",
      "desc": "根据自身的[ChargeRouge] 强度，获得以下全部效果\n- 1：自身每有1次[ChargeRouge] 次数，造成的伤害量+2%(最多20%)，使目标的体力恢复量+10%(最多100%，向下取整)\n- 2：自身的[ChargeRouge] 强度每有2点，基础威力+1\n- 3：回合开始时，若自身没有[GourmandiseAlly] 效果且自身的[ChargeRouge] 次数在15以上，则消耗所有[ChargeRouge] 次数，获得3层[GourmandiseAlly] \n- 4：技能槽位+1\n- 5：舞台开始时，获得3层[GourmandiseAlly] 并对所有敌方单位施加3层[BloodyMucusAlly] ",
      "summary": "根据自身的[ChargeRouge] 强度获得强化",
      "flavor": "望着他们的背影，一步一步地去了解这个世界、这间百货公司。以及关于自己的事情。"
    },
    {
      "id": 40004104,
      "name": "援手",
      "desc": "战斗中友方单位陷入混乱状态时，对该友方单位使用“握住我的手”(每回合最多2次)"
    },
    {
      "id": 40004105,
      "name": "难以自控的身躯",
      "desc": "若自身带有[GourmandiseAlly] 效果，则获得以下效果\n- 恢复相当于造成伤害量20%的体力\n- 使用技能时，自身的[Laceration] 次数增加3次\n- 技能命中时，对自身施加1层[Laceration] ",
      "summary": "对自身施加[Laceration] ",
      "flavor": "手脚与一切都如此陌生，但自深处萌发的微弱悸动，却逐渐化作难以遏制的狂暴搏动。"
    },
    {
      "id": 40004107,
      "name": "皮质缝合钉",
      "desc": "通过攻击技能未击杀敌人时，对该敌人使用“让我来结束这一切吧……”(每回合最多1次)",
      "flavor": "他们说，为了缝合皮革，需要的不仅是尖锐，更需要粗壮结实的钉子。如果那样还穿不透的话，就再来一次……！"
    },
    {
      "id": 40004108,
      "name": "偏离命运",
      "desc": "该单位阵亡时战斗败北",
      "flavor": "即使走错路也是可以的，但逆流而行或偏离正道，是被“那件东西”所禁止的。"
    },
    {
      "id": 40004202,
      "name": "偏离命运",
      "desc": "该单位阵亡时战斗败北",
      "flavor": "即使走错路也是可以的，但逆流而行或偏离正道，是被“那件东西”所禁止的。"
    },
    {
      "id": 40004203,
      "name": "粘滞卑贱(le Visqueux-Abject)",
      "desc": "该单位仅承受将自身指定为主要目标的技能伤害，不承受其他伤害\n\n首次登场于战斗时，在战场生成[BuffetField] \n\n回合开始时，对[BuffetField] 范围内的目标生效以下效果\n- 友方单位(包括自身)\n· 恢复体力上限5%的体力\n· [Charge] 次数增加4次\n· 获得1层[Protection] \n· 若目标友方单位属于红派，则获得2层[Enhancement] \n· E.G.O技能伤害量+50%\n\n- 敌方单位\n· 施加3层[AttackDown] \n· 施加3层[DefenseDown] \n· 施加2层[BloodyMucusAlly] ",
      "flavor": "赤红之神摄取着眼前之物，不断摄取。其结果便是黏膜质地带的蔓延展开。那是摄取的结果。自自身流出，却令自身与非自身之边界逐渐模糊的卑贱与粘稠。在这之上，属于我的事物在搏动，不属于我的事物在融化。因为边界之外的一切，皆令人恐惧。"
    },
    {
      "id": 40004204,
      "name": "幼年终结(La Fin de l'enfance)",
      "desc": "舞台开始时，获得5层[ChargeRouge] 强度\n\n回合结束时，若自身的[ChargeRouge] 次数在15以上，则装备技能“恶心(la nausée)”\n每回合开始时，获得20点[Aggro] ",
      "flavor": "有谁能规定童年何时终结呢？赤红的孩子通过旅程成长了。以为通过旅程的经验可以成为某种存在，以为自己正在成为那样的存在，但那个过程却戛然而止。童年并非能够自行宣告终结之物。现实突如其来地从外部强行闯入，带着强制与急躁下达了通告。已经结束了。"
    }
  ]
}

skills_assist = {
  "dataList": [
    {
      "id": 40004101,
      "levelList": [
        {
          "level": 1,
          "name": "赤红之钉",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，基础威力+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "赤红之钉",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，基础威力+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"}
              ]
            },
            {
              "coindescs": [
                {"desc": "若目标没有理智值，则造成的伤害量+50%"},
                {"desc": "[OnSucceedAttack] 使目标的理智值减少10点"}
              ]
            }
          ]
        },
        {
          "level": 3,
          "name": "赤红之钉",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，基础威力+1(最多+2)\n[WhenUse] 若理智值高于目标或目标没有理智值，则硬币威力+1",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"}
              ]
            },
            {
              "coindescs": [
                {"desc": "若目标没有理智值，则造成的伤害量+50%"},
                {"desc": "[OnSucceedAttack] 使目标的理智值减少10点"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004102,
      "levelList": [
        {
          "level": 1,
          "name": "走开",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，硬币威力+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加2次"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "走开",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，硬币威力+1(最多+2)\n[WhenUse] 自身的[ChargeRouge] 强度每有2点，攻击加权值+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加2次"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"}
              ]
            }
          ]
        },
        {
          "level": 3,
          "name": "走开",
          "desc": "[WhenUse] 目标的[Laceration] 强度每有4点，硬币威力+1(最多+2)\n[WhenUse] 自身的[ChargeRouge] 强度每有2点，攻击加权值+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加2次"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 自身的[ChargeRouge] 强度每有2点，对目标施加1层[BloodyMucusAlly] (最多2层)"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004103,
      "levelList": [
        {
          "level": 1,
          "name": "加油",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标获得1层[ParryingResultUp] "},
                {"desc": "[EndCoin] 自身的[ChargeRouge] 强度每有1点，使目标获得1层[AttackUp] (最多5层)"}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "加油",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 自身的[ChargeRouge] 强度每有2点，攻击加权值+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标获得1层[ParryingResultUp] "},
                {"desc": "[EndCoin] 自身的[ChargeRouge] 强度每有1点，使目标获得1层[AttackUp] (最多5层)"}
              ]
            }
          ]
        },
        {
          "level": 3,
          "name": "加油",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 自身的[ChargeRouge] 强度每有2点，攻击加权值+1(最多+2)\n[EndSkill] 若自身带有[GourmandiseAlly] 效果且自身的[ChargeRouge] 次数在10以上，则消耗最多10次[ChargeRouge] 次数，使命中的所有目标获得1层[SkillPowerUp] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标获得1层[ParryingResultUp] "},
                {"desc": "[EndCoin] 自身的[ChargeRouge] 强度每有1点，使目标获得1层[AttackUp] (最多5层)"}
              ]
            }
          ]
        },
        {
          "level": 4,
          "name": "加油",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 自身的[ChargeRouge] 强度每有2点，攻击加权值+1(最多+2)\n[EndSkill] 若自身带有[GourmandiseAlly] 效果且自身的[ChargeRouge] 次数在10以上，则消耗最多10次[ChargeRouge] 次数，使命中的所有目标获得1层[SkillPowerUp] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标获得1层[SkillPowerUp] "},
                {"desc": "[EndCoin] 自身的[ChargeRouge] 强度每有1点，使目标在本回合与下回合获得1层[AttackUp] (最多5层)"}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004104,
      "levelList": [
        {
          "level": 1,
          "name": "不要痛",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标恢复(该技能最终威力 × 2)点体力\n- 若目标属于红派，则改为使其体力减少，并使自身恢复等量体力(该效果不会使其陷入混乱或体力降至1点以下)"}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "不要痛",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 若自身的[ChargeRouge] 强度在3以上，则攻击加权值+2",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标恢复(该技能最终威力 × 2)点体力\n- 若目标属于红派，则改为使其体力减少，并使自身恢复等量体力(该效果不会使其陷入混乱或体力降至1点以下)"}
              ]
            },
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标的理智值恢复该技能最终威力的数值\n- 若理智值为最大值，则随机解除1个可解除的负面状态"}
              ]
            }
          ]
        },
        {
          "level": 3,
          "name": "不要痛",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 若自身的[ChargeRouge] 强度在3以上，则攻击加权值+4",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标恢复(该技能最终威力 × 2)点体力\n- 额外使目标恢复相当于目标体力上限(自身的[ChargeRouge] 强度 × 2)%的体力\n- 若目标属于红派，则改为使其体力减少，并使自身恢复等量体力(该效果不会使其陷入混乱或体力降至1点以下)"}
              ]
            },
            {
              "coindescs": [
                {"desc": "[EndCoin] 使目标的理智值恢复该技能最终威力的数值\n- 额外使目标的理智值恢复(自身的[ChargeRouge] 强度 × 3)点\n- 若理智值为最大值，则随机解除1个可解除的负面状态"}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004105,
      "levelList": [
        {
          "level": 1,
          "name": "握住我的手",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] \n\n[WhenUse] 下回合获得5层[Binding] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 解除目标的混乱状态"},
                {"desc": "[EndCoin] 使目标恢复等同于该技能最终威力的体力"}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "握住我的手",
          "desc": "[CantDuel] \n[CantChangeTarget] \n[SupportAlly] ",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[EndCoin] 解除目标的混乱状态"},
                {"desc": "[EndCoin] 使目标恢复等同于该技能最终威力的体力"},
                {"desc": "[EndCoin] 下回合使目标获得目标体力上限50%的护盾"}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004106,
      "levelList": [
        {
          "level": 1,
          "name": "红钉洗礼",
          "desc": "[WhenUse] 若自身的[ChargeRouge] 次数在10以上，则消耗最多10次[ChargeRouge] 次数，攻击加权值+2，硬币威力+2",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加2次"}
              ]
            }
          ]
        },
        {
          "level": 2,
          "name": "红钉洗礼",
          "desc": "[WhenUse] 若自身的[ChargeRouge] 次数在10以上，则消耗最多10次[ChargeRouge] 次数，攻击加权值+2，硬币威力+2\n[WhenUse] 目标的[Laceration] 强度每有4点，基础威力+1(最多+2)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加3次"}
              ]
            }
          ]
        },
        {
          "level": 3,
          "name": "红钉洗礼",
          "desc": "[WhenUse] 若自身的[ChargeRouge] 次数在10以上，则消耗最多10次[ChargeRouge] 次数，攻击加权值+2，硬币威力+2\n[WhenUse] 目标的[Laceration] 强度每有4点，基础威力+1(最多+2)\n[WhenUse] 若自身的[ChargeRouge] 强度在5以上，则生效以下效果\n- 攻击加权值+2\n- 硬币威力+(自身的[ChargeRouge] 强度 - 3)",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 对目标施加2层[Laceration] "},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            },
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 对目标施加1层[BloodyMucusAlly] "},
                {"desc": "[OnSucceedAttack] 使目标的[Laceration] 次数增加3次"},
                {"desc": "[OnSucceedAttack] 对目标施加1层[BuffetGold] "}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004107,
      "levelList": [
        {
          "level": 1,
          "name": "让我来结束这一切吧……",
          "desc": "[CantDuel] \n目标的已损失体力每有1%，造成的伤害量+0.5%(最多30%)\n[WhenUse] 若自身带有[GourmandiseAlly] 效果，则攻击加权值+1",
          "coinlist": [
            {
              "coindescs": [
                {"desc": "[OnSucceedAttack] 下回合对目标施加1层[Binding] "},
                {"desc": "[OnSucceedAttack] 若自身带有[GourmandiseAlly] 效果，则重复投掷该硬币(最多1次)"}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004201,
      "levelList": [
        {
          "level": 1,
          "name": "恶心(la nausée)",
          "desc": "[StartBattle] 消耗所有自身的[ChargeRouge] 次数，使包括自身在内的全体友方单位恢复体力上限([ChargeRouge] 次数消耗值)%的体力",
          "flavor": "在成长为神的过程中必然经历的感觉。有人表现为眩晕，有人表现为作呕，有人表现为痉挛，有人表现为欺瞒，而有人则表现为抗拒。世间的一切都令人目眩、恐惧而混乱。为了忍耐这一切，为了守护自身尚未模糊的界线中的所有物，他试图吐出任何事物来守护自己。",
          "coinlist": [
            {
              "coindescs": [
                {"desc": ""}
              ]
            }
          ]
        }
      ]
    },
    {
      "id": 40004202,
      "levelList": [
        {
          "level": 1,
          "name": "红洞(le Trou rouge)",
          "desc": "[StartBattle] 使自身获得4次[ChargeRouge] 次数",
          "flavor": "这是一个红色的洞。虽闭合着，但它却如同深穴一般渴望着以无尽的饥渴将洞口填满。正如同所被寄予的厚望那般，正如同就这样被诞生出来的那般。",
          "coinlist": [
            {
              "coindescs": [
                {"desc": ""}
              ]
            }
          ]
        }
      ]
    }
  ]
}

with open(os.path.join(WORKSPACE_DIR, "Passives_Assist-a1c10p2.json"), "w", encoding="utf-8") as f:
    json.dump(passives_assist, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("Passives_Assist-a1c10p2.json written successfully.")

with open(os.path.join(WORKSPACE_DIR, "Skills_Assist-a1c10p2.json"), "w", encoding="utf-8") as f:
    json.dump(skills_assist, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("Skills_Assist-a1c10p2.json written successfully.")
