#!/usr/bin/env python3
import json
import os

WORKSPACE_DIR = "workspace/LLC_zh-CN"

with open("backups/part2-scope-20260924/source-kr/Passives_Abnormality-a1c10p2.json", encoding="utf-8-sig") as f:
    kr_data = json.load(f)["dataList"]

# Define translations for all 43 passives
trans = {
    150301: {
        "name": "悲哭不绝",
        "desc": "舞台开始时，以恐慌状态开始战斗\n\n处于恐慌状态时，生效以下效果\n- <color=#ff6000><mark color=#ff000040><b><u>将所有攻击的目标指定为普伊</color></mark></b></u>\n- 使用技能时，若主要目标为普伊，则拼点威力、基础威力增加[TabExplain] \n- 战斗开始时，技能的所有硬币变为[SuperCoin] ",
        "flavor": "属于旧物之子嗣已然绝迹。"
    },
    150302: {
        "name": "缠结的黑线",
        "desc": "通过技能、士气低落及恐慌效果对敌方单位施加[TangleBlackYarn] \n※[TangleBlackYarn] 可<color=#ff6000><mark color=#ff000040><b><u>通过使用守备技能或特定技能减少</color></mark></b></u>\\n\n受到攻击时触发以下效果\n- 受到攻击时获得1层[SickBlackYarn] \n- 若受到攻击的技能为<color=#ff6000><mark color=#ff000040><b><u>斩击属性</color></mark></b></u>，额外获得1层[SickBlackYarn] \n- 受到<color=#ff6000><mark color=#ff000040><b><u>攻击加权值在5以上</color></mark></b></u>的技能攻击时，下回合获得[HeavyBlackYarn] (每回合最多1次)",
        "flavor": "这具身躯上缠绕着的黑线此前并不存在。侥幸在时代更迭之时，黑线缠绕于这古老旧物的身躯之上，正因为这由丝线包裹的身体，才得以在百货公司的时代中苟活下来。而那黑线，如今正被解开。"
    },
    150303: {
        "name": "没入旧日之海",
        "desc": "部位陷入<color=#ff6000><mark color=#ff000040><b><u>混乱状态</color></mark></b></u>时，使其他部位的<color=#ff6000><mark color=#ff000040><b><u>混乱阈值各减少1个并结束回合</color></mark></b></u>\n此后下回合所有部位获得[HideBlackYarn] \n\n若因<color=#ff6000><mark color=#ff000040><b><u>受到攻击使[HideBlackYarn] 消减</color></mark></b></u>，\n- 获得10层[SickBlackYarn] \n- 若获得的[SickBlackYarn] 超过上限，则本回合与下回合获得3层[Vulnerable] \n\n回合结束时，若[HideBlackYarn] 消减，\n- 获得(7 - 剩余强度)层[SickBlackYarn] \n- 下回合获得1层[AngryBlackYarn] ",
        "flavor": "没入那曾经理所当然且自由自在地游曳其中、如今却已消逝的旧日之海的怀抱之中。"
    },
    150304: {
        "name": "尚未干涸的水迹",
        "desc": "因[Combustion] 、[Laceration] 、[Vibration] 、[Burst] 、[Sinking] 受到的体力、理智值、混乱损伤伤害量-50%\n\n恐慌类型不发生变化，回合结束时若处于恐慌状态，则理智值变为0点",
        "flavor": "西西弗水族馆虽然已经消失，但这具身躯上，依然残留着当时微弱的、尚未化为丝线的水迹。"
    },
    150101: {
        "name": "泥塑人偶",
        "desc": "舞台开始时恢复全部体力\n\n本体与部位均不受到[Combustion] 与[Laceration] 的伤害",
        "flavor": "宛如陶瓷般的肌肤，源自泥土。"
    },
    150102: {
        "name": "永不凋零的花",
        "desc": "战斗开始时获得1层[AlriunePetal] \n\n自身陷入混乱时，\n- 下回合获得2层[Vulnerable] \n- 使罪人及协助者的理智值恢复20点\n- 从混乱状态恢复的回合开始时，将[AlriunePetal] 重置为1层\n\n回合开始时，若未持有[FlowerLaurelWreath] 的敌方单位不存在，则<color=#ff6000><mark color=#ff000040><b><u>装备“散发宜人香气的月桂冠”</color></mark></b></u>\n- 若已装备“怀揣归于尘土的夙愿”，则在下回合装备\n\n受到<color=#ff6000><mark color=#ff000040><b><u>未持有[FlowerLaurelWreath] 效果的敌方单位技能攻击时受到的伤害量-50%</color></mark></b></u>\n受到<color=#ff6000><mark color=#ff000040><b><u>持有[FlowerLaurelWreath] 效果的敌方单位技能攻击时受到的伤害量+150%</color></mark></b></u>",
        "flavor": "花朵会凋零。随后再度绽放。"
    },
    150103: {
        "name": "立春",
        "desc": "敌方单位陷入混乱时，对目标造成20点理智伤害\n\n回合开始时，<color=#ff6000><mark color=#ff000040><b><u>若存在处于恐慌或侵蚀状态的目标，则对该目标使用“与所有欲生之物同归墓穴”</color></mark></b></u>(每回合最多2次，按速度较慢的目标顺序使用，协助者除外)\n\n若该目标因该技能阵亡，则下回合生成1名泥土所生者\n- 战斗中泥土所生者达到4名时，不再生成",
        "flavor": "待到春来，自当绽放"
    },
    150201: {
        "name": "源自泥土",
        "desc": "不受到[Combustion] 与[Laceration] 的伤害\n\n<color=#ff6000><mark color=#ff000040><b><u>因[Vibration] 受到的混乱伤害+100%</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>自身陷入混乱时阵亡</color></mark></b></u>",
        "flavor": "重归尘土"
    },
    151901: {
        "name": "超高速SPM",
        "desc": "自身攻击目标的<color=#ff6000><mark color=#ff000040><b><u>速度低于自身时，拼点威力+3</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>使用消耗[ChargeKhaki] 次数的技能的回合结束时，若自身的[ChargeKhaki] 次数在11以上，</color></mark></b></u>使用强力技能\n\n自身的体力在50%以下时，使用强力技能(每场战斗最多1次)",
        "summary": "目标的速度低于自身时，拼点威力增加",
        "flavor": "姐姐可以达到10000 SPM呢"
    },
    151902: {
        "name": "钉刺缝线",
        "desc": "对处于混乱或无法行动状态的目标造成的伤害+40%",
        "flavor": "没有什么比缝合静止不动之物更加轻而易举的了"
    },
    151903: {
        "name": "彩色缝线",
        "desc": "若自身带有[SpreadingDye] ，自身技能命中的目标获得1层[StickyDye] \n\n对带有[ThreadDye] 的目标生效以下效果\n- 通过技能施加的[Laceration] 强度与次数增加等同于[ThreadDye] 强度的数值\n- 通过上述效果施加[StickyDye] 时，对除被施加目标外随机1名持有[ThreadDye] 的敌方单位施加1层[StickyDye] \n\n自身技能的目标持有[Inactible] 时，不施加[ThreadDye] ",
        "flavor": "姐姐缝合布料的同时，我来为它染上颜色。"
    },
    151904: {
        "name": "调节针距调节器",
        "desc": "舞台开始时恢复最大体力，理智值恢复45点\n\n战斗中累计消耗10次自身[ChargeKhaki] 次数时，获得1层[ChargeKhaki] 强度"
    },
    149501: {
        "name": "修补",
        "desc": "回合开始时，对上一回合中对自身<color=#ff6000><mark=#ff000040><b><u>造成最多伤害的罪人</color></mark></b></u>\n<color=#ff6000><mark=#ff000040><b><u>施加1层[TailoringTarget] </color></mark></b></u>并使用“打版”\n- 若带有[TailoringTarget] 的罪人<color=#ff6000><mark=#ff000040><b><u>持有9层[ScissorsMark] </color></mark></b></u>，\n则“打版”改为<color=#ff6000><mark=#ff000040><b><u>“链式包缝(Surfil à la chaîne)”</color></mark></b></u>发动\n\n每次受到罪人攻击时\n- 对该罪人施加1层[ScissorsMark] (每名罪人每回合最多5层)\n- 自身的[ChargeKhaki] 次数增加1次(每名罪人每回合最多5次)\n\n<color=#ff6000><mark=#ff000040><b><u>每次受到持有[TailoringTarget] 的罪人的攻击技能攻击时\n获得3层[ResultEnhancement] (每回合最多9层)</b></u></mark></color>",
        "flavor": "人们常说，衣服是通过修补得以完整的。只要不是量身定制的衣裳，就必须通过修补使其契合自身。\n\n而这绝不仅仅局限于衣物。唯有将从外界获取的事物同样进行修补并披在身上，方能称心如意地活着。"
    },
    149503: {
        "name": "裁剪",
        "desc": "舞台开始时或解除混乱状态后的回合开始时，\n获得30层[FinishedFabric] \n\n生效[PanicChangeLock] 效果，\n回合结束时若处于恐慌状态，则理智值变为30点\n\n回合开始时，\n- 获得自身<color=#ff6000><mark=#ff000040><b><u>体力上限([FinishedFabric] 数值)%的护盾</color></mark></b></u>(最多30%)\n- 恢复等同于[FinishedFabric] 数值的理智值",
        "flavor": "裁剪是根据版型将面料裁开。如果说修补是让衣物迁就人的过程，那么裁剪就是让面料迁就衣物的过程。\n\n因此对于面料而言，裁剪便等同于修补。一旦被剪开的面料，便保留着那一特性，作为修补师所预期的唯一一件衣裳而被钉死。"
    },
    149504: {
        "name": "剪切不息",
        "desc": "修补师阿内特\n- <color=#ff6000><mark=#ff000040><b><u>每次受到罪人攻击时，受到自身体力上限0.8%的混乱伤害</color></mark></b></u>\n\n<color=#ff6000><mark=#ff000040><b><u>陷入混乱状态时，\n失去所有自身的护盾、[FinishedFabric] 与[LargeTailoringShears] ，并获得3层[Vulnerable] </color></mark></b></u>\n\n回合开始时若自身的体力在60%以下，\n- 每损失20%体力，获得1层[ResultEnhancement] 与1层[SlashDamageUp] (分别最多3层)\n- “修剪”的最后一枚硬币与“裁剪”的第二枚硬币变为[SuperCoin] ",
        "flavor": "以修补为价值所构筑的身躯，为了无休止地修补与裁剪而永不停歇剪切。\n\n哪怕身躯正在破碎，修补与裁剪也决不能被截断。虽做着截断之事，自身却无论如何也无法断绝。"
    },
    149505: {
        "name": "漂流惯性",
        "desc": "战斗中累计消耗10次自身的[ChargeKhaki] 次数时，\n获得1层[ChargeKhaki] 强度\n\n自身的[ChargeKhaki] 强度在3/5以上时，\n自身的[ChargeKhaki] 次数上限+5/+10",
        "flavor": "顺应着百货公司的时代所造就的价值而漂流，被卷入那股惯性之中，惯性越是强盛，漂流便越是难以停止。"
    },
    150601: {
        "name": "保全",
        "desc": "战斗中累计消耗10次自身的[ChargeNoir] 次数时，获得1层[ChargeNoir] 强度\n[ChargeNoir] 次数上限+10"
    },
    150602: {
        "name": "应许之槌",
        "desc": "自身的攻击命中或自身受到攻击时，自身的[ChargeNoir] 次数增加1次",
        "flavor": "铁锤将钉子钉下。这柄铁锤所敲打的唯有钉子。挨锤子打的便是钉子。事情便是如此约定的。"
    },
    150603: {
        "name": "阵型保全",
        "desc": "黑派所属友方单位的等级大幅提升\n\n场上每有1名存活的黑派所属友方单位，所有黑派所属友方单位受到的伤害量-5%\n黑派所属友方单位阵亡时，本次战斗中所有黑派所属友方单位获得1层[NoirSquareCollapse] (包括新登场的单位)",
        "flavor": "各守其位执行职务，那些身姿汇聚一处化作单一的阵型，那阵型便成为用以保全整体的图样，故而，在各自的岗位上恪尽职守吧。"
    },
    150401: {
        "name": "黑派面料",
        "desc": "舞台首次登场时，获得5层[NoirBindArmor] \n\n回合开始时，获得自身体力上限([NoirBindArmor] 数值)%的护盾\n\n陷入混乱状态时失去所有[NoirBindArmor] ，\n回合开始时解除混乱状态后，获得5层[NoirBindArmor] ",
        "flavor": "黑派面料如铠甲般坚挺而固定的廓形，能够修饰顾客的体态。"
    },
    150402: {
        "name": "保全",
        "desc": "战斗中累计消耗自身的[ChargeNoir] 次数时，触发以下效果\n- 每次消耗3次时，获得1层[NoirBindArmor] \n- 每次消耗10次时，获得1层[ChargeNoir] 强度\n\n自身的[ChargeNoir] 强度在3以上时，自身的[ChargeNoir] 次数上限+5",
        "flavor": "凝聚力量，使其固定。有时不作改变比做出改变需要更大的力量。"
    },
    150403: {
        "name": "品质保全",
        "desc": "[ChargeNoir] 次数在10以上时，使用强力技能",
        "flavor": "为了品质必须履行质检程序，在此过程中保全决不能被破坏。"
    },
    150404: {
        "name": "面料密度差距",
        "desc": "[ChargeNoir] 强度在3/5以上时，[Vibration] 强度施加量增加1/2点\n\n使用技能时，若防御等级高于目标，防御等级每相差1级，造成的伤害量+3%(最多30%)\n- 防御等级高出5级以上时，基础威力+1",
        "flavor": "黑派将碾压比自身面料更加松软的事物。"
    },
    150501: {
        "name": "黑派面料",
        "desc": "舞台首次登场时，获得5层[NoirBindArmor] \n\n回合开始时，获得自身体力上限([NoirBindArmor] 数值)%的护盾\n\n陷入混乱状态时失去所有[NoirBindArmor] ，\n回合开始时解除混乱状态后，获得5层[NoirBindArmor] ",
        "flavor": "黑派面料如铠甲般坚挺而固定的廓形，能够修饰顾客的体态。"
    },
    150502: {
        "name": "保全",
        "desc": "战斗中累计消耗自身的[ChargeNoir] 次数时，触发以下效果\n- 每次消耗3次时，获得1层[NoirBindArmor] \n- 每次消耗10次时，获得1层[ChargeNoir] 强度\n\n自身的[ChargeNoir] 强度在3以上时，自身的[ChargeNoir] 次数上限+5",
        "flavor": "凝聚力量，使其固定。有时不作改变比做出改变需要更大的力量。"
    },
    150503: {
        "name": "验品保全",
        "desc": "[ChargeNoir] 次数在10以上时，使用强力技能",
        "flavor": "为了品质必须履行质检程序，在此过程中保全决不能被破坏。"
    },
    150504: {
        "name": "面料密度差距",
        "desc": "[ChargeNoir] 强度在3/5以上时，[Vibration] 强度施加量增加1/2点\n\n使用攻击技能时，若防御等级高于目标，防御等级每相差1级，造成的伤害量+3%(最多30%)\n- 防御等级高出5级以上时，基础威力+1",
        "flavor": "黑派将碾压比自身面料更加松软的事物。"
    },
    148801: {
        "name": "原罪生皮供应",
        "desc": "回合开始时，若场上存在的被鞣制的囚犯在2名以下，生成额外槽位\n回合结束时，<color=#ff6000><mark=#ff000040><b><u>场上每存在1名被鞣制的囚犯</u></b></mark></color>，下回合获得1层[AttackDmgUp] ",
        "flavor": "撕下罪人的皮，刮去附着的罪恶，借此供应皮革。"
    },
    148802: {
        "name": "准备重新鞣制",
        "desc": "若场上存在除自身外当前体力低于体力上限80%的友方单位，生成额外槽位",
        "flavor": "再度被罪恶沾污的皮革将被回收至制革厂，重新进行鞣制。"
    },
    148803: {
        "name": "原罪皮革制革厂全负荷运转",
        "desc": "自身的本体体力低于体力上限50%时，结束回合且行动模式发生改变，包括自身在内的所有友方单位在本次战斗中获得[RestrictFailed] ",
        "flavor": "皮革需求暴增。生皮供应困难。原罪皮革曾经是连看都不看一眼的皮革种类，但在某个季度的契机下需求暴增，价格水涨船高。从前无疑是被廉价抛售或直接废弃的皮革。而如今连原罪皮革表面的瑕疵也被包装为情怀与格调供人消费。"
    },
    148804: {
        "name": "制革厂规则",
        "desc": "从第2回合起，每回合开始时对随机3名敌方单位随机施加以下效果之一\n- [RestrictMob] \n- [RestrictBoss] \n- [RestrictTier1] \n- [RestrictDef] \n\n违反规则时，施加1层[RestrictDenied] ",
        "flavor": "区分肉块与皮革，是在严苛的鞣制程序与规则之下被划分开来的。"
    },
    149101: {
        "name": "被鞣制的囚犯",
        "desc": "阵亡时，本次战斗中控制者的防御等级永久降低1级"
    },
    150604: {
        "name": "战斗续行",
        "desc": "舞台开始时，以体力80%、理智值45的状态开始"
    },
    151001: {
        "name": "开始缝合",
        "desc": "回合开始时，对随机2名敌方单位施加[NiddleExpected] "
    },
    151002: {
        "name": "纯手工",
        "desc": "场上每有1根针，技能最终威力+1",
        "flavor": "手工缝制的生命线在于熟练工匠的数量。"
    },
    151003: {
        "name": "哪怕捂住耳朵也能看到的客诉",
        "desc": "每3的倍数回合听见蚕茧的啼哭声\n进入第2阶段时蚕茧的啼哭声每回合持续\n\n听见蚕茧啼哭声的回合免疫无法行动状态\n\n越过混乱阈值后，下回合获得2层[Vulnerable] ",
        "flavor": "从茧中传来了声音。\n“低于80支双股的面料根本不算面料。”“扣眼怎么不是横向的？”\n“是用老式织机织的天竺棉吗？”“赤耳的布边颜色怎么不是红色的？”\n“这个没做防缩水加工处理啊。”“低于Super 150的就是廉价面料吧”\n“Super数只是纱线粗细？纤维直径和支数是两码事，这你都不知道吗。”\n“当然会用Union Special缝纫机来锁底边对吧？”“这是原牛吗？啊，是赤耳单宁吗？”\n“仔细一看针脚太均匀了。用机器了吧？”“不是纯手工缝制就根本不算全定制。”\n“啊这扣眼不是米兰眼啊。”“支数得超过200才算衬衫面料吧。”\n“啊，外面能看见明线啊。”“看到两条明线了。不合格。”\n“缝头包边处理怎么搞成这样。”“至少得超过3 Ply才行吧”"
    },
    149604: {
        "name": "炽烈照耀的阳光",
        "desc": "受阳光影响等级提升的状态\n\n舞台开始时，获得[GoldenLeatherEnhance] ",
        "flavor": "对于倾听阳光温度者，阳光听起来愈发炽烈、耀眼而强烈。"
    },
    148805: {
        "name": "战斗续行",
        "desc": "舞台开始时，以体力90%、理智值45的状态开始"
    },
    148305: {
        "name": "炽烈照耀的阳光",
        "desc": "受炽烈照耀的阳光影响等级提升的状态\n\n舞台开始时，获得2层[ChargeNoir] 强度与15次[ChargeNoir] 次数\n\n舞台开始时以理智值30开始，获得1000点非挥发性护盾",
        "flavor": "对于倾听阳光温度者，阳光听起来愈发炽烈、耀眼而强烈。"
    },
    1590001: {
        "name": "炽烈照耀的阳光",
        "desc": "受阳光影响等级提升的状态",
        "flavor": "对于倾听阳光温度者，阳光听起来愈发炽烈、耀眼而强烈。"
    },
    149608: {
        "name": "哪怕捂住耳朵也能看到的客诉",
        "desc": "蚕茧的啼哭声每回合持续\n免疫无法行动状态"
    },
    151101: {
        "name": "炽烈照耀的阳光",
        "desc": "受炽烈照耀的阳光影响等级提升的状态\n舞台开始时，获得[SapsareeGold] ",
        "flavor": "对于倾听阳光温度者，阳光听起来愈发炽烈、耀眼而强烈。"
    },
    151201: {
        "name": "炽烈照耀的阳光",
        "desc": "受炽烈照耀的阳光影响等级提升的状态\n舞台开始时恢复全部体力，获得[GoldenManager] ",
        "flavor": "对于倾听阳光温度者，阳光听起来愈发炽烈、耀眼而强烈。"
    }
}

out_data = {"dataList": []}
for item in kr_data:
    pid = item["id"]
    t = trans.get(pid, {})
    new_item = {"id": pid}
    for k in ["name", "desc", "summary", "flavor"]:
        if k in t:
            new_item[k] = t[k]
        elif k in item:
            new_item[k] = item[k]
    out_data["dataList"].append(new_item)

out_path = os.path.join(WORKSPACE_DIR, "Passives_Abnormality-a1c10p2.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Passives_Abnormality-a1c10p2.json: written {len(out_data['dataList'])} passives.")
