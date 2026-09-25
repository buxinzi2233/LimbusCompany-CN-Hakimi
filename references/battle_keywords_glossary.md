# 《边狱公司》战斗词条 ID 与译名速查

> **使用方式**：内部 ID 不等于官方英文显示名；本表用于定位译名，省略号结尾的说明是截断摘要，不能据此翻译触发条件或数值限制，完整内容读取同 ID 的 JSON。
>
> **来源分层**：既有译名索引保留历史 `baseline-zh-CN` 来源；S8 条目已对齐零协会 `2026092102`，展示当前工作区的中文词条与本地格式化结果，版本边界见[更新调研](../docs/reports/zeroasso-update-research.md)。
>
> **本工作区约定（AGENTS.md，不代表所有上游格式）**：
> 1. **严禁残留英文标识符**：技能、被动、状态机制描述中，**一律禁止**出现 `[ChargeNoir]`、`[Vulnerable]`、`[Laceration]` 等英文 ID，必须替换为对应中文名（例：`[保存] `、`[易损] `、`[流血] `）。
> 2. **后置半角空格**：所有方括号词条后必须紧跟一个半角空格，即 `[关键词] `（本地格式要求；具体悬浮窗行为仍需实机验证）。
> 3. **动词三元法则**：正面状态用 **获得**，负面状态用 **施加**，强度/数值变化用 **增加/减少**，层数消耗用 **消耗/降低**。

---

未经定位的 `Disruption`、`PlusCoinBoost`、`PlusCoinDrop` 不作为已验证别名；实际加算硬币词条请查本索引的 `PlusCoinValueUp` / `PlusCoinValueDown`。

## 1. 核心高频战斗机制速查表 (Core Status Effects)

| 英文 ID | 中文规范译名 | 机制分类 | 典型用语范例 |
| :--- | :--- | :--- | :--- |
| `Laceration` | **流血** | 负面持续伤害 | `对目标施加{0}层[流血] ；使目标的[流血] 强度增加{0}` |
| `Burst` | **破裂** | 受攻击时附加固定伤害 | `对目标施加{0}层[破裂] ；使目标的[破裂] 强度增加{0}` |
| `Sinking` | **沉沦** | 负面精神削减 | `对目标施加{0}层[沉沦] ；使目标的[沉沦] 强度增加{0}` |
| `Vibration` | **震颤** | 负面混乱爆发 | `对目标施加{0}层[震颤] ；触发[震颤引爆] ` |
| `Combustion` | **烧伤** | 负面回合固伤 | `对目标施加{0}层[烧伤] ；使目标的[烧伤] 强度增加{0}` |
| `Breath` | **呼吸法** | 正面暴击增益 | `自身获得{0}层[呼吸法] ；使自身的[呼吸法] 强度增加{0}` |
| `Charge` | **充能** | 核心特殊资源 | `自身获得{0}层[充能] ；消耗{0}层[充能] ` |
| `Enhancement` | **强壮** | 正面威力增益 | `自身获得{0}层[强壮] ` |
| `Reduction` | **虚弱** | 负面威力减益 | `对目标施加{0}层[虚弱] ` |
| `Vulnerable` | **易损** | 负面承伤增加 | `对目标施加{0}层[易损] ` |
| `Protection` | **守护** | 正面承伤减少 | `自身获得{0}层[守护] ` |
| `Agility` | **迅捷** | 正面速度提升 | `自身获得{0}层[迅捷] ` |
| `Binding` | **束缚** | 负面速度降低 | `对目标施加{0}层[束缚] ` |
| `Paralysis` | **麻痹** | 负面硬币减益 | `对目标施加{0}层[麻痹] ` |
| `ParryingResultUp` | **拼点威力提升** | 正面拼点增益 | `使自身获得1层[拼点威力提升] ` |
| `AttackUp` | **攻击等级提升** | 基础数值增益 | `使自身的攻击等级增加{0}` |
| `AttackDown` | **攻击等级降低** | 基础数值减益 | `使目标的攻击等级减少{0}` |
| `DefenseUp` | **防御等级提升** | 基础数值增益 | `使自身的防御等级增加{0}` |
| `DefenseDown` | **防御等级降低** | 基础数值减益 | `使目标的防御等级减少{0}` |

同名不等于同机制：[基准 BattleKeywords.json](baseline-zh-CN/BattleKeywords.json) 中 `Bleeding` 按当前体力比例扣血后层数减半，`Laceration` 在攻击硬币判定时按强度造成固定伤害后减1层；`Burn` 回合末伤害后层数减半，`Combustion` 回合末按强度伤害后减1层。按原文 ID 查对应条目，不把这两组键当作可互换别名。

---

## 2. 第十章 a1c10p1 已译词条

本表对应默尔索主线“被凝视者”的 [BattleKeywords-a1c10p1.json](../workspace/LLC_zh-CN/BattleKeywords-a1c10p1.json) 中57项当前译名，涉及红派（Rouge）与黑派（Noir）；不是整个赛季全部内容的收录承诺。以下“来源文件”列注明本次参考版本，具体数值、条件与风味文本请回到同 ID 完整记录。

| 英文标识符 (ID) | 中文规范译名 | 来源文件 | 机制说明概要 |
| :--- | :--- | :--- | :--- |
| `BloodyMucus` | **洗礼（赤红）** | LLC 2026092102／本地格式化 | - 最大值：5 - 自身每带有3级流血 强度，使自身增加1级攻击等级(最多3级) - 若本效果层数为最大值，则使自身受到的流血 伤害变为2倍且不会因流…… |
| `BuffetFailed` | **虚脱** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，最小与最大速度值-1 - 回合开始时，对自身施加1层易损  - 回合结束时，本效果层数减少1层 (适用于所有部位…… |
| `BuffetSick` | **痛苦之袋** | LLC 2026092102／本地格式化 | - 最大值：30 - 回合结束时，若狂暴 效果解除，则解除本效果，每减少5层，下回合对自身施加1层易损  |
| `ChargeNoir` | **保存** | LLC 2026092102／本地格式化 | - 特殊充能 - 最大层数：20 - 本效果强度与层数的增减同样受普通充能 影响 - 回合结束时，本效果的层数减少1层 |
| `ChargeRouge` | **搏动** | LLC 2026092102／本地格式化 | - 特殊充能 - 最大层数：20 - 本效果强度与层数的增减同样受普通充能 影响 - 回合结束时，本效果的层数减少1层 |
| `DeterioratingBody` | **求生本能** | LLC 2026092102／本地格式化 | - 最大值：5 - 体力不会低于1点 - 受到攻击时，本效果层数减少1层(每个技能最多2次) - 回合结束时，本效果层数减少1层；本效果解除时，自身阵…… |
| `EarlyBuffet_LowMorale` | **分裂** | LLC 2026092102／本地格式化 | - 士气低落 - 防御等级-3 - 攻击等级+3 - 与带有的洗礼（赤红） 层数为5层的目标进行拼点时，使自身的拼点威力+2 |
| `EarlyBuffet_Panic` | **分裂** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 防御等级-5 - 攻击等级+3 - 造成的伤害+10% - 与带有的洗礼（赤红） 层数不低于3层的目标进行拼点时，使自身的拼点威力+…… |
| `Gourmandise` | **狂暴** | LLC 2026092102／本地格式化 | - 基础值：3 - 自身每带有3级流血 强度，使自身造成的伤害+5%(最多+30%) - 所有部位不会陷入混乱，受到来自流血 的伤害-75% - 回合…… |
| `HorribleEat` | **重复播放的重复** | LLC 2026092102／本地格式化 | - 最大值：15 - 使自身增加相当于本效果层数的攻击等级 |
| `HorribleTerror` | **可怕的重复播放** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合开始时，若自身处于E.G.O侵蚀状态，则使自身本回合对所有目标造成的伤害-50% - 回合结束时，自身受到现存体力50%的体力…… |
| `HowlingCocoon` | **茧的悲鸣-微弱** | LLC 2026092102／本地格式化 | - 偶尔，会听见茧的悲鸣。 - 技能的最终威力+2 |
| `HowlingCocoonTwo` | **茧的悲鸣-恶性** | LLC 2026092102／本地格式化 | - 茧的悲鸣不会停下。 - 技能的最终威力+3 |
| `HungryPeople_LowMorale` | **错失恐惧症** | LLC 2026092102／本地格式化 | - 士气低落 - 自身每失去20%体力，攻击等级+1(最多+2) - 对自身施加1层易损  |
| `HungryPeople_Panic` | **错失恐惧症** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 自身每失去20%体力，攻击等级+1(最多+2) - 对自身施加1层易损  |
| `LaNoir_LowMorale` | **回到壳中……** | LLC 2026092102／本地格式化 | - 士气低落 最大速度值-1 防御等级+1 |
| `LaNoir_Panic` | **回到壳中……** | LLC 2026092102／本地格式化 | - 陷入恐慌 最大速度值-5 防御等级+3 |
| `LaRouge_LowMorale` | **从皮里出去！** | LLC 2026092102／本地格式化 | - 士气低落 防御等级-3 攻击等级+1 |
| `LaRouge_Panic` | **从皮里出去！** | LLC 2026092102／本地格式化 | - 陷入恐慌 防御等级-5 攻击等级+2 |
| `MeursaultBuffet` | **嵌钉者** | LLC 2026092102／本地格式化 | - 本场战斗中，自身使用技能时，获得2个对应属性的E.G.O资源(每回合最多2次) - 回合开始时，若有其他友方单位在场，则本回合自身不会因受到伤害阵…… |
| `NiddleExpected` | **刺舌之针** | LLC 2026092102／本地格式化 | - 自身装备守备技能时  - 使自身的针钉 层数减少1层  - 解除本效果  - 回合结束时，对自身施加3层针钉 ，随后解除本效果 |
| `NiddlePin` | **针钉** | LLC 2026092102／本地格式化 | - 特殊流血 - 受到突刺伤害时，对自身施加1层流血 并使本效果层数减少1层 - 回合结束时，使自身增加1级流血 强度并使本效果层数减少1层 |
| `NiddlePinned` | **标本化** | LLC 2026092102／本地格式化 | - 最大值：2  - 受到攻击时，对自身施加1层流血 (每回合最多3次) - 带有本效果时，自身无法行动  - 回合结束时，失去15点体力，并使自身的…… |
| `NoirBindArmor` | **黑派 精纺面料** | LLC 2026092102／本地格式化 | - 最大值：15 - 每带有5层本效果，最大速度值-1，攻击等级+1，防御等级+1 - 回合结束时，本效果的层数减少1层 |
| `NoirNoComply` | **违反规定** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，受到的伤害+5% |
| `NoirSuit` | **黑派 华达呢大衣** | LLC 2026092102／本地格式化 | - 最大值：100 - 回合开始时，每带有20层本效果，使自身获得1层防御等级提升 (最多4层) - 自身通过技能或被动效果消耗或获得保存 层数时，获…… |
| `Nutrition` | **夺来的某物。** | LLC 2026092102／本地格式化 | - 最大值：5 - 回合结束时，下回合使自身获得(本效果层数×2)层搏动 ，随后解除本效果 - 若本效果解除时层数为最大值，则下回合使自身所有部位获得…… |
| `Realisation` | **织纹觉醒** | LLC 2026092102／本地格式化 | - 最大值：100 - 回合开始时，每带有10层本效果，使自身恢复5点理智值 - 回合开始时，每带有20层本效果，使自身获得1层攻击等级提升 与1层防…… |
| `ReliefSense` | **感谢聆听** | LLC 2026092102／本地格式化 | - 最大值：3 - 回合开始时，本效果层数增加1层，并使自身恢复10点理智值 - 使自身技能对本关卡头目造成的伤害+(本效果层数×50)%，该技能攻击…… |
| `RisingMadnessNoir` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层…… |
| `RisingMadnessNoir2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 …… |
| `RisingMadnessRouge` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层…… |
| `RisingMadnessRouge2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 …… |
| `RisingMadnessSisyphe` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层易…… |
| `RisingMadnessSisyphe2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 并…… |
| `RougeThreeCocoon` | **更衣室** | LLC 2026092102／本地格式化 | - 最大值：3 - 不会受到体力伤害 - 受到攻击时，触发以下效果(每回合最多20次)  · 使自身获得1层搏动  · 使自身获得1层伤害强化  · …… |
| `RougeThreeCocoonHit` | **迫害** | LLC 2026092102／本地格式化 | - 最大值：20 |
| `RougeThreeCocoonShield` | **信仰** | LLC 2026092102／本地格式化 | - 回合开始时，获得相当于本效果层数的护盾 - 护盾减少时，本效果层数减少 |
| `RougeThreeNormal` | **精品店新品** | LLC 2026092102／本地格式化 | - 最大值：20  使用技能时，消耗自身体力上限1%的体力并使该技能造成的伤害+(消耗的体力)% |
| `SapsareeCooking` | **切碎的食材** | LLC 2026092102／本地格式化 | - 最大值：5 - 回合结束时解除 |
| `SapsareeHungry` | **我说我肚子饿了噢** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，使自身增加1级攻击等级 - 若本效果层数为3层，则使自身造成的伤害+50% - 副主厨使用技能“啊！我说吃饭时间…… |
| `SapsareeShield` | **吃吧……** | LLC 2026092102／本地格式化 | - 副主厨将受到来自敌方单位的单方面攻击时，消耗1层并使该敌方单位的目标改为自身，随后使用援护防御专用技能 - 多个友方单位带有援护防御 时，层数最高…… |
| `SapsareeSpices` | **火辣辣酱** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，使自身减少1级攻击等级 |
| `SapsareeYammi` | **我说吃好喝好，精神百倍噢** | LLC 2026092102／本地格式化 | - 最大值：5 - 每带有1层本效果，使自身增加1级攻击等级 - 回合开始时，自身每带有1层“我说我肚子饿了噢”，使本效果的层数减少1层 |
| `Sapsaree_LowMorale` | **烹饪欲望** | LLC 2026092102／本地格式化 | - 士气低落 - 自身每带有1层“我说我肚子饿了噢”，使自身攻击等级+1，受到的伤害+3% |
| `Sapsaree_Panic` | **烹饪欲望** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 自身每带有1层“我说我肚子饿了噢”，使自身攻击等级+2，受到的伤害+5% |
| `SavePlacenta` | **自我保护** | LLC 2026092102／本地格式化 | - 命脉将受到来自敌方单位的单方面攻击时，消耗1层并使该敌方单位的目标改为自身，随后使用援护防御专用技能 - 回合结束时解除 |
| `SisyphusAmber` | **琥珀** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 |
| `SisyphusAmethyst` | **紫水晶** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 |
| `SisyphusEmerald` | **祖母绿** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusGold` | **黄金** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusRuby` | **红宝石** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusTopaz` | **托帕石** | LLC 2026092102／本地格式化 | - 无效果 |
| `UnresolvedFeelings` | **多层拼布** | LLC 2026092102／本地格式化 | - 最大值：30 - 使自身增加相当于本效果层数的防御等级 - 受到带有“感谢聆听”的目标攻击时，使本效果层数减少相当于“感谢聆听”层数(每回合每名人…… |
| `Wariness` | **戒心** | LLC 2026092102／本地格式化 | - 最大值：10 - 使自身减少相当于本效果层数的攻击等级，增加相当于本效果层数的防御等级 - 若自身拼点失败，则使本效果层数减少3层 |
| `WeakWithering_LowMorale` | **胡乱缝纫** | LLC 2026092102／本地格式化 | - 士气低落 - 回合开始时，对自身施加1层攻击等级降低  |
| `WeakWithering_Panic` | **胡乱缝纫** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 回合开始时，对自身施加1层攻击等级降低 与1层伤害弱化  |

---

## 3. 全量词条与状态字母检索索引 (A-Z Complete Index, 共 1860 条)

以下收录官方零协会基准与当前工作区全部词条的 English ID -> 中文规范译名映射，按字母顺序排列以供快速检索：

| 英文 ID | 中文规范译名 | 归属来源 | 机制说明摘录 |
| :--- | :--- | :--- | :--- |
| `A1c971a` | **喷涌的暴怒** | LLC 基准 (BattleKeywords-a1c9114.json) | 每回合开始时，使自身增加相当于回合数的烧伤 强度 |
| `A1c971b` | **蔓延的忧郁** | LLC 基准 (BattleKeywords-a1c9114.json) | 回合结束时，若本效果层数为1层，则对体力最低的敌方单位造成相当于自身现存体力的伤害，随后自身阵亡 回... |
| `A1c971c` | **不息的暴食** | LLC 基准 (BattleKeywords-a1c9114.json) | 回合开始时，每经过2回合，使自身获得1层体力恢复提升 (最多5层) 回合开始时，自身每恢复10点体力... |
| `A1c971d` | **吐出的呼吸** | LLC 基准 (BattleKeywords-a1c9114.json) | 自身获得呼吸法 时，额外增加3级呼吸法 强度或额外获得2层呼吸法 |
| `A1c971e` | **伤中之伤** | LLC 基准 (BattleKeywords-a1c9114.json) | 命中时，额外使目标增加2级流血 强度或额外对目标施加1层流血 |
| `A1c971f` | **慵懒的怠惰** | LLC 基准 (BattleKeywords-a1c9114.json) | 回合结束时本效果的层数减少1层 层数为0时EX通关条件失败 |
| `AStrokeOfDeath` | **绝命** | LLC 基准 (BattleKeywords.json) | - 使自身增加2级攻击等级 - 使自身的最终威力+1 - 回合结束时解除本效果 |
| `ATL_Agility` | **再快点！** | LLC 基准 (BattleKeywords.json) | 获得2层迅捷 |
| `ATL_Breath` | **再准点！** | LLC 基准 (BattleKeywords.json) | 增加3级呼吸法 强度 |
| `ATL_EndureCombustion` | **烧伤抗性** | LLC 基准 (BattleKeywords.json) | 受到由烧伤 导致的伤害时，使其数值降低10%(最多10层) |
| `ATL_EndureLaceration` | **流血抗性** | LLC 基准 (BattleKeywords.json) | 受到由流血 导致的伤害时，使其数值降低10%(最多10层) |
| `ATL_Target` | **拿下他！** | LLC 基准 (BattleKeywords.json) | 统一攻击同一个敌方单位。 |
| `AaCePaBa` | **强迫** | LLC 基准 (BattleKeywords-a1c5p1.json) | 关卡开始时，初始理智值为-25点。回合开始时，若理智值低于0点，则使自身获得3层强壮 。 |
| `AaCePbBa` | **苍白的噪音** | LLC 基准 (BattleKeywords-a1c5p2.json) | 理智值减少效率 +2。 带有本效果时，若自身的理智值不高于-45点，则下回合对自身施加噪音恐慌 。 ... |
| `AaCePbBb` | **噪音恐慌** | LLC 基准 (BattleKeywords-a1c5p2.json) | 该单位所有硬币的朝向都必定是反面。 下回合解除本效果 |
| `AaCePbBc` | **不洁** | LLC 基准 (BattleKeywords-a1c5p2.json) | - 士气低落 - 对自身施加1层易损 。该单位拼点失败时，使目标失去2点理智值。 |
| `AaCePbBd` | **不洁** | LLC 基准 (BattleKeywords-a1c5p2.json) | - 陷入恐慌 - 对自身施加2层易损 。该单位拼点失败时，使目标失去5点理智值。 |
| `AaCePbBe` | **报复** | LLC 基准 (BattleKeywords-a1c5p2.json) | - 士气低落 - 回合开始时，使自身获得1层强壮 并对自身施加3层防御等级降低 ，基于上回合受到的伤... |
| `AaCePbBf` | **报复** | LLC 基准 (BattleKeywords-a1c5p2.json) | - 陷入恐慌 - 回合开始时，使自身获得2层强壮 并对自身施加6层防御等级降低 ，基于上回合受到的伤... |
| `AaCePbBg` | **怨恨** | LLC 基准 (BattleKeywords-ycgd.json) | 回合开始时使自身获得2层伤害强化 ，并对自身施加3层防御等级降低 |
| `AaCePbBh` | **怨恨** | LLC 基准 (BattleKeywords-ycgd.json) | 回合开始时使自身获得1层强壮 ，并对自身施加5层防御等级降低 |
| `AaCePbBi` | **大哥的试炼** | LLC 基准 (BattleKeywords-a1c5p2.json) | 回合结束时，本效果的层数减少1层 带有本效果时，受到的技能伤害与震颤引爆 造成的混乱阈值前移量变为3... |
| `AaCePcBa` | **标识** | LLC 基准 (BattleKeywords-a1c5p3.json) | 优先成为攻击指定目标。 受到攻击时，使自身获得的烧伤 强度与对自身施加的烧伤 层数变为2倍 |
| `AaCePcBb` | **荧光灯碎片** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合开始时，使自身增加3级呼吸法 强度并使自身获得2层呼吸法 |
| `AaCePcBc` | **盲目** | LLC 基准 (BattleKeywords-a1c5p3.json) | 层数不低于3层时陷入混乱。 |
| `AaCePcBe` | **苍白恐慌** | LLC 基准 (BattleKeywords-a1c5p3.json) | 理智值减少效率 +2 |
| `AaCePcBf` | **苍白恐慌** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合结束时，对自身施加2层束缚 。 自身所有硬币的朝向都必定是反面。 |
| `AaCePcBg` | **幼虫** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合结束时，将幼虫 转移给现存体力最高的1名友方单位。 回合开始时，使自身失去等同于层数的理智值。 |
| `AaCePcBh` | **绿色黏液** | LLC 基准 (BattleKeywords-a1c5p3.json) | 每当本效果的层数减少时，下回合生成绿色黏液 |
| `AaCePcBi` | **粗重喘息** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合结束时，使自身失去5层呼吸法  造成与受到的伤害+50% |
| `AaCePcBj` | **猎物标记** | LLC 基准 (BattleKeywords-a1c5p3.json) | 成为全体裴廓德号船员的攻击目标 受到来自裴廓德号船员的伤害+50% |
| `AaCePcBk` | **捆缚** | LLC 基准 (BattleKeywords-a1c5p3.json) | 若施加给带有捕获 的目标，则使目标陷入混乱。此效果对已陷入混乱的目标无效。 |
| `AaCePcBl` | **捕获** | LLC 基准 (BattleKeywords-a1c5p3.json) | 若施加给带有捆缚 的目标，则使目标陷入混乱。此效果对已陷入混乱的目标无效。 |
| `AaCePcBn` | **不可抗拒的命令** | LLC 基准 (BattleKeywords-a1c5p3.json) | 使用技能时，失去现存体力10%的体力。技能最终威力+1 命中时，使亚哈恢复8点理智值，并使自身与亚哈... |
| `AaCePcBo` | **比普的自我** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合开始时，每带有1层本效果，使自身恢复3点理智值。 闪避失败时或使用技能“负罪感的重量”时减少本效... |
| `AaCePcBp` | **斯达巴克的自我** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合开始时，每带有5层本效果，使自身获得1层守护 。 与带有猎物标记 的目标拼点失败摧毁硬币时减少本... |
| `AaCePcBq` | **魁魁格的自我** | LLC 基准 (BattleKeywords-a1c5p3.json) | 回合结束时，若自身带有护盾，增加本效果层数 回合结束时，若自身未带有护盾或使用技能：褪色的忏悔时，减... |
| `AaCePcBr` | **援护护盾** | LLC 基准 (BattleKeywords-a1c5p3.json) | 受到伤害时，根据伤害量相应减少本效果层数。 回合结束时本效果不会解除。 回合结束时，若本效果层数为0... |
| `AaCePcBs` | **援护防御** | LLC 基准 (BattleKeywords-a1c5p3.json) | 将以亚哈为攻击目标的技能，目标转移为自身的行动槽。 带有本效果的角色自身行动槽的行动槽容量为无限。 |
| `AaCePcBt` | **援护攻击** | LLC 基准 (BattleKeywords-a1c5p3.json) | 亚哈的攻击技能结束时，对亚哈攻击的目标进行一次单方面攻击。 此时使用的攻击技能与“听从命令…”具有相... |
| `AaCeSeBa` | **嚯！嚯！嚯！** | LLC 基准 (BattleKeywords-a1c951.json) | 回合结束时，下回合使自身获得(自身的呼吸法 强度/5)层呼吸法 。 充能 层数为0时解除本效果。 |
| `AaCeSeBb` | **我要把你做成礼物！** | LLC 基准 (BattleKeywords-a1c951.json) | 每回合使自身增加3级呼吸法 强度。 回合结束时，每个造成伤害的攻击技能恢复3点理智值。 |
| `AaCfPaBa` | **丧失** | LLC 基准 (Bufs-a1c6p1.json) | 回合结束时，若自身的理智值不低于-15点，则使自身失去10点理智值。 受到攻击时，使自身失去2点理智... |
| `AaCfPaBa_Alt1` | **无尽的丧失** | LLC 基准 (Bufs.json) | 回合开始时，使自身恢复5点理智值 受到攻击时，失去3点理智值并在下回合使自身获得2层攻击等级提升 (... |
| `AaCfPaBa_Alt2` | **斩首希斯克利夫** | LLC 基准 (Bufs.json) | 回合开始时，使自身恢复10点理智值 受到攻击时，下回合使自身获得2层攻击等级提升 (每回合最多3次)... |
| `AaCfPbBa` | **爆发的忧郁** | LLC 基准 (BattleKeywords-a1c6p2.json) | - 忧郁抗性+0.3 - 其他罪孽抗性-0.5 - 受到攻击时，对攻击者造成3点理智伤害，对自身施加... |
| `AaCfPbBb` | **爆发的嫉妒** | LLC 基准 (BattleKeywords-a1c6p2.json) | - 嫉妒抗性+0.3 - 其他罪孽抗性-0.5 - 受到攻击时，使攻击者获得1层攻击等级提升 并使其... |
| `AaCfPbBc` | **爆发的暴怒** | LLC 基准 (BattleKeywords-a1c6p2.json) | - 暴怒抗性+0.3 - 其他罪孽抗性-0.5 - 受到攻击时，下回合使自身获得1层攻击等级提升 并... |
| `AaCfPbBd` | **深切的丧失感** | LLC 基准 (BattleKeywords-a1c6p2.json) | 回合开始时，使自身的速度值-5，对自身施加5层防御等级降低 |
| `AaCfPbBe` | **猎物标识** | LLC 基准 (BattleKeywords-a1c6p2.json) | - 若本回合未受到伤害，则攻击后对自身施加1层自卑感 并解除本效果 - 最大值：1 |
| `AaCfPbBf` | **自卑感** | LLC 基准 (BattleKeywords-a1c6p2.json) | - 每次受到伤害时，受到伤害量(20%*层数)的固定伤害 - 最大值：5 |
| `AaCfPbBg` | **凌乱的绘画** | LLC 基准 (Bufs-a1c6p2.json) | - 士气低落 - 使自身获得1层强壮 并对自身施加1层易损 |
| `AaCfPbBh` | **凌乱的绘画** | LLC 基准 (Bufs-a1c6p2.json) | - 陷入恐慌 - 使自身获得1层加算硬币强化 并对自身施加3层易损 |
| `AaCfPbBi` | **憎恶** | LLC 基准 (Bufs-a1c6p2.json) | - 士气低落 - 拼点胜利时，下回合使自身获得1层攻击等级提升 (每回合最多3次) 拼点失败时，使自... |
| `AaCfPbBj` | **憎恶** | LLC 基准 (Bufs-a1c6p2.json) | - 陷入恐慌 - 拼点胜利时，本回合与下回合使自身获得1层攻击等级提升 (每回合最多3次) 拼点失败... |
| `AaCfPcBa` | **觉悟** | LLC 基准 (Bufs-a1c6p3.json) | 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最多3次) 回合开始时，若自身的理智值低于0点... |
| `AaCfPcBa_Alt1` | **宣泄的暴怒** | LLC 基准 (Bufs.json) | 回合结束时，使自身恢复10点理智值 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最多3次)... |
| `AaCfPcBa_Alt2` | **斩首希斯克利夫** | LLC 基准 (Bufs.json) | 回合结束时，使自身恢复10点理智值 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最多3次)... |
| `AaCfPcBa_Alt3` | **爱与憎** | LLC 基准 (Bufs.json) | 回合结束时，使自身恢复15点理智值 攻击命中时，下回合使自身获得1层迅捷 与1层攻击等级提升 (每回... |
| `AaCfPcBa_Alt4` | **褪色的约定** | LLC 基准 (Bufs.json) | 回合结束时，使自身恢复15点理智值 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最多3次)... |
| `AaCfPcBa_Alt5` | **褪色的约定** | LLC 基准 (Bufs.json) | 回合结束时，使自身恢复15点理智值 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最多3次)... |
| `AaCfPcBb` | **管家的标记** | LLC 基准 (BattleKeywords-a1c6p3.json) | 使特定攻击技能的攻击容量增加 |
| `AaCfPcBc` | **束缚法** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 最大值：3 - 回合结束时，对自身施加1层本效果 - 回合结束时，下回合对自身施加相当于本效果层... |
| `AaCfPcBe` | **深切的丧失感** | LLC 基准 (BattleKeywords-a1c6p3.json) | 攻击结束后，对目标造成5点理智伤害。 |
| `AaCfPcBf` | **未能释怀的怅惘** | LLC 基准 (BattleKeywords-a1c6p3.json) | 在特定条件下，回合结束时，若本效果的层数不低于3层，则下回合所有部位陷入混乱。 对锁链部位施加3层易... |
| `AaCfPcBg` | **泄愤对象** | LLC 基准 (BattleKeywords-a1c6p3.json) | 成为心被撕碎的希斯克利夫的指定目标。 自身阵亡时，对其他人格施加本效果。 |
| `AaCfPcBh` | **充满痛苦的暴怒** | LLC 基准 (BattleKeywords-a1c6p3.json) | 攻击者带有爆发的暴怒 时，受到的伤害+100% |
| `AaCfPcBi` | **高温装置** | LLC 基准 (BattleKeywords-a1c6p3.json) | 回合结束时，根据本效果层数受到固定伤害并解除本效果 |
| `AaCfPcBiv2` | **高温装置** | LLC 基准 (BattleKeywords-a1c9p3.json) | 回合结束时，受到自身体力上限(本效果层数×0.5)%的固定伤害并解除本效果 |
| `AaCfPcBm` | **苦痛之雷** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 拼点胜利时，对目标施加撕碎的心 并造成7点体力伤害 - 拼点失败时或单方面攻击后，对自身施加撕碎... |
| `AaCfPcBn` | **撕碎的心** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 所有罪孽属性抗性增加(层数×0.2) - 若本效果层数为3层，则使自身陷入混乱。 |
| `AaCfPcBo` | **觉悟** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 回合结束时，使自身恢复10点理智值 - 受到攻击时，下回合使自身获得1层攻击等级提升 (每回合最... |
| `AaCfPcBp` | **靠近的勇气** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 回合结束时，使自身恢复10点理智值 - 每回合使自身获得3层强壮 与5层守护  - 受到攻击时，... |
| `AaCfPcBq` | **被撕碎的心** | LLC 基准 (BattleKeywords-a1c6p3.json) | - 最大速度值+2 - 每回合使自身获得3层伤害强化 并对自身施加3层易损  - 若主要攻击目标为希... |
| `AaCfPcBr` | **愿她…在苦痛中醒来！** | LLC 基准 (BattleKeywords-a1c6p3.json) | 与带有苦痛之雷 的目标拼点时，拼点威力-6 |
| `AaCfPcBs` | **别妨碍我** | LLC 基准 (BattleKeywords-a1c6p3.json) | 剩余的护盾点数 |
| `AbyssalVitality` | **深海的生命力** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 最大值：100 - 特定技能使用时消耗 - 消耗本效果时，使自身恢复相当于消耗量的理智值 |
| `AccelBullet` | **加速弹** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 特殊弹药 - 特定技能使用时消耗 |
| `Acclamation_LowMorale` | **山庄的回响** | LLC 基准 (Bufs-a1c6p1.json) | - 士气低落 - 使自身的拼点威力-1，正面命中时造成的伤害+10% |
| `Acclamation_Panic` | **山庄的回响** | LLC 基准 (Bufs-a1c6p1.json) | - 陷入恐慌 - 使自身的拼点威力-2，使自身获得1层伤害强化 |
| `AccumulatedPast` | **累积的过去** | LLC 基准 (BattleKeywords_Refraction2.json) | 显示折射轨道累计回合数。 回合结束时，层数+1。 躯干部位被破坏时，消耗所有层数。 |
| `AccumulatedPastMirror` | **累积的过去** | LLC 基准 (BattleKeywords_Mirror4.json) | 回合结束时，层数+11。 躯干部位被破坏时，消耗所有层数。 |
| `AccumulatedPastSinner` | **累积的过去** | LLC 基准 (BattleKeywords-tkt-re.json) | - 最大值：12 - 回合开始时，本效果层数每有3层，使自身获得1层拼点威力提升 与1层攻击等级提升 |
| `ActivatedEgoPassive` | **E.G.O被动技能** | LLC 基准 (BattleKeywords.json) | 激活的E.G.O被动技能 |
| `AengduNewArm` | **鬼怪之臂** | LLC 基准 (BattleKeywords-exme.json) | - 基础攻击等级+4 - 基础防御等级+4 - 受到的伤害-20% - 使用技能时，下回合使自身获得... |
| `AengduNewArmIshmael` | **鬼怪之臂** | LLC 基准 (BattleKeywords.json) | - 受到的伤害-15% - 使用技能时，下回合使自身获得1层迅捷 (每回合最多2次) - 战斗结束时... |
| `Aengdu_Lowmorale` | **怨恨** | LLC 基准 (BattleKeywords-exme.json) | - 回合开始时，使自身获得1层强壮 并对自身施加1层破绽  - 回合结束时，下回合使自身获得2层迅捷 |
| `Aengdu_Panic` | **怨恨** | LLC 基准 (BattleKeywords-exme.json) | - 回合开始时，使自身获得2层强壮 并对自身施加2层破绽  - 回合结束时，下回合使自身获得2层迅捷 |
| `AffectionTeddy` | **依恋** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：9 - 攻击者攻击带有本效果的目标时，根据本效果的层数使攻击者获得相应层数的拼点威力提升... |
| `AgainstMyWill_LowMorale` | **“杀、杀…杀了我…”** | LLC 基准 (BattleKeywords-a1c9p3.json) | 回合开始时，对自身施加8层拼点威力降低 与5层威力降低 |
| `AgainstMyWill_Panic` | **“杀、杀…杀了我…”** | LLC 基准 (BattleKeywords-a1c9p3.json) | 回合开始时，对自身施加10层拼点威力降低 与5层威力降低 |
| `Aggressive` | **本能** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果的层数不低于4层，则进入进攻状态。 |
| `AggressiveBokgak` | **本能** | LLC 基准 (BattleKeywords-Refraction1BokGak.json) | 最大值：5 回合结束时，若本效果的层数不低于4层，则进入进攻状态。 |
| `Aggro` | **挑衅值** | LLC 基准 (BattleKeywords.json) | 在集中遭遇战中，挑衅值越高的行动槽受到敌方单位攻击的概率越高。 |
| `Agility` | **迅捷** | LLC 基准 (BattleKeywords.json) | 一回合内速度值增加等同于本效果层数的数值。 |
| `AimForTheGoal` | **瞄准目标** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 若自身未带有狙击姿势 ，则解除本效果 |
| `AlcoholKimPersonal` | **追悼酒** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 回合开始时，每带有1层本效果，使自身增加1级呼吸法 强度 · 剑契组 头领 默尔... |
| `AllSetForShooting` | **射击准备完毕** | LLC 基准 (BattleKeywords-walpu5.json) | - 行动槽+1 - 将该人格的一个1技能替换为3技能 - 基础攻击技能每消耗1发弹药 ，使其造成的伤... |
| `AlriuneEGOThey` | **余香** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 自身受到沉沦 伤害时，对自身施加1层本效果 - 受到震颤引爆 时，随机对除自身... |
| `AlriuneEGOWe` | **花瓣** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每带有10层本效果，使自身攻击等级+1 - 每回合最多获得15层本效果 |
| `AmberDamageDown` | **怠惰伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低怠惰技能造成的伤害。(最多10层) |
| `AmberDamageUp` | **怠惰伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高怠惰技能造成的伤害。(最多10层) |
| `AmberResistDown` | **怠惰抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的怠惰抗性增加(每层0.1) |
| `AmberResistUp` | **怠惰抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的怠惰抗性减少(每层0.1) |
| `AmberResultDown` | **怠惰威力降低** | LLC 基准 (Bufs.json) | 本回合内怠惰技能的最终威力-{0} |
| `AmberResultUp` | **怠惰威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内，怠惰属性技能的最终威力根据本层数相应增加 |
| `AmberTakeDamageDown` | **怠惰守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自怠惰技能的伤害。(最多10层) |
| `AmberTakeDamageUp` | **怠惰易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自怠惰技能的伤害。(最多10层) |
| `Anger` | **暴怒** | LLC 基准 (BattleKeywords.json) | 发动特定技能所需的资源。发动特定技能时消耗。 |
| `Anger_LowMorale` | **愤怒** | LLC 基准 (Bufs.json) | - 士气低落 - 回合开始时，获得1层伤害强化 并施加2层易损 。 |
| `Anger_Panic` | **愤怒** | LLC 基准 (Bufs.json) | - 陷入恐慌 - 回合开始时，获得2层伤害强化 并施加5层易损 。 |
| `AntiSheepGround` | **对羊接地插头** | LLC 基准 (BattleKeywords_Refraction4.json) | - 最多1层 - 带有本效果的单位与“拒绝接地”技能拼点胜利时，对目标施加1层连接的插头  - 目标... |
| `ArcanaQueenOfHate` | **魔法阿卡纳** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：3 - 自身基础攻击技能造成的伤害+(本效果层数×5)%  - 回合结束时，若本效果层数... |
| `AreaAtk` | **群体攻击** | LLC 基准 (BattleKeywords.json) | 同时攻击不低于2名敌方单位。 |
| `ArrowInTheEyeFau` | **刺入之矢** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 回合开始时，使自身增加相当于本效果层数的流血 强度 - 使自身减少相当于本效果层... |
| `ArrowShiFau` | **箭矢-死** | LLC 基准 (BattleKeywords.json) | - 最小值：0 - 最大值：4 - 特定技能使用时消耗的箭矢 |
| `ArtifactBeeSting` | **穿刺标枪[胡蜂针]** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 斩击抗性+1，怠惰抗性+1 - 回合结束时，下回合对自身施加4层束缚  - 攻击命中时，使自身增... |
| `Assemble` | **狂信** | LLC 基准 (BattleKeywords.json) | 一回合内，攻击带有尖钉 的目标时，技能的最终威力提升等同于本效果层数的数值。(拼点时同样生效) |
| `AssemblePersonality` | **狂信** | LLC 基准 (BattleKeywords.json) | 一回合内，攻击带有尖钉 的目标时，技能的最终威力提升等同于本效果层数的数值。(拼点时同样生效) |
| `AttackDmgDown` | **伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少技能造成的伤害。(最多10层) |
| `AttackDmgUp` | **伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加技能造成的伤害。(最多10层) |
| `AttackDmgUp_Weak` | **脆弱攻击伤害强化** | LLC 基准 (BattleKeywords.json) | 以目标抗性为脆弱的攻击造成的伤害+(本效果层数)% |
| `AttackDown` | **攻击等级降低** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少攻击等级。 |
| `AttackLevelAdder` | **攻击等级 +** | LLC 基准 (BattleKeywords.json) | 一回合内根据本效果的层数来增加攻击等级。 |
| `AttackUp` | **攻击等级提升** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加攻击等级。 |
| `AzureDamageDown` | **忧郁伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低忧郁技能造成的伤害。(最多10层) |
| `AzureDamageUp` | **忧郁伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高忧郁技能造成的伤害。(最多10层) |
| `AzureResistDown` | **忧郁抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的忧郁抗性增加(每层0.1) |
| `AzureResistUp` | **忧郁抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的忧郁抗性减少(每层0.1) |
| `AzureResultDown` | **忧郁威力降低** | LLC 基准 (Bufs.json) | 本回合内忧郁技能的最终威力-{0} |
| `AzureResultUp` | **忧郁威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高忧郁技能的最终威力 |
| `AzureTakeDamageDown` | **忧郁守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自忧郁技能的伤害。(最多10层) |
| `AzureTakeDamageUp` | **忧郁易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自忧郁技能的伤害。(最多10层) |
| `BabayagaTimeLimit` | **迫近的芭芭雅嘎** | LLC 基准 (BattleKeywords.json) |  |
| `BackstreetsNight_LowMorale` | **后巷深宵** | LLC 基准 (BattleKeywords-a1c9116.json) | 回合开始时，使自身获得1层强壮 与1层体力恢复提升 并对自身施加1层易损 |
| `BackstreetsNight_Panic` | **后巷深宵** | LLC 基准 (BattleKeywords-a1c9116.json) | 回合开始时，使自身获得2层强壮 ，2层体力恢复提升 并对自身施加1层易损 |
| `BandageOfTheBoundKing` | **受缚之王的绷带** | LLC 基准 (BattleKeywords_Refraction4.json) | 阵亡时，使全体敌方单位增加2级沉沦 强度并对其施加1层沉沦  对击杀自身的目标施加受缚之王的绷带 。... |
| `BattleSense` | **底力** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：25 - 特定技能使用时消耗，该回合结束时，使自身恢复相当于消耗量的理智值 - 每次进行... |
| `BattlefieldHorse` | **号令** | LLC 基准 (BattleKeywords.json) | - 使自身的拼点威力+1，防御等级+2 - 回合结束时解除本效果 |
| `BearClawWound` | **被撕裂的色彩[红色]** | LLC 基准 (BattleKeywords-twth.json) | - 最大值：9 - 受到攻击时，每带有3层本效果，使自身增加1级流血 强度(每回合最多1次) - 回... |
| `BearClawWoundAlly` | **被撕裂的色彩[红色]** | LLC 基准 (BattleKeywords.json) | - 最大值：9 - 受到攻击时，每带有3层本效果，使自身增加1级流血 强度(每回合最多1次) - 回... |
| `BeastEyesAlly` | **过热** | LLC 基准 (BattleKeywords.json) | - 自身获得猛虎标弹 时，解除本效果 - 使自身的最小与最大速度值+2 - 基础攻击技能的拼点威力-... |
| `BeastEyes_LowMorale` | **猛兽本能-士气低落** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 对现存体力比例高于自身的目标造成的伤害+(体力比例之差/2)%(最多+10%) - 回合开始时，... |
| `BeastEyes_Panic` | **猛兽本能-陷入恐慌** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 对现存体力比例高于自身的目标造成的伤害+(体力比例之差)%(最多+25%) - 回合开始时，使自... |
| `BeeSting` | **穿刺标枪[蜂针]** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 斩击抗性+0.2，怠惰抗性+0.2 - 回合结束时，下回合对自身施加2层束缚  - 攻击命中时，... |
| `BeingGolden` | **金光** | LLC 基准 (BattleKeywords.json) | 回合开始时，每带有1层本效果则恢复10点体力。 |
| `BestWelfareTeamCaptain` | **福利部队长** | LLC 基准 (BattleKeywords-walpu8.json) | - 行动槽+1，将该人格的一个1技能替换为3技能 - 自身技能增加的烧伤 、流血 、破裂 、沉沦 与... |
| `BestWelfareTeamMember` | **福利部优秀员工** | LLC 基准 (BattleKeywords-walpu6.json) | - 自身技能增加的烧伤 、流血 、破裂 、沉沦 与震颤 强度额外+1级(特殊异常状态同样适用) - ... |
| `BigWelcome` | **盛情款待** | LLC 基准 (BattleKeywords_Refraction4.json) | 攻击结束后，若目标陷入混乱或击杀目标，则获得1个傲慢E.G.O资源与随机1个其他E.G.O资源(每回... |
| `Binding` | **束缚** | LLC 基准 (BattleKeywords.json) | 一回合内速度值减少等同于本效果层数的数值。 |
| `BirdCage` | **炙热鸟笼** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 若自身带有烧伤 ，则每层本效果使自身的暴怒抗性+0.1(本效果不会使暴怒抗性超过... |
| `BitOfEmotion` | **情感共享** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 攻击命中敌方单位时，以(50/硬币数)%的概率获得使用的技能对应属性的1个E.G.O资源 - 友... |
| `BlackCloud` | **黑云** | LLC 基准 (BattleKeywords.json) | 最大值：1 本回合使自身使用的基础攻击技能的所有硬币转化为不可摧毁的硬币，该技能结束前自身不会因受到... |
| `BlackCloudBlade` | **黑云刀** | LLC 基准 (BattleKeywords.json) | 最大值：1 使自身的斩击威力+1 斩击技能命中时，使目标增加1级流血 强度 |
| `BlackNightmare` | **指令成瘾** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 增加的沉沦 强度与施加的沉沦 层数额外+2 - 回合结束时解除本效果，并对自身施加(本回合拼点失... |
| `BlackNightmareYisang` | **指令成瘾** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+5 - 使“Furioso-Replica”获得以下效果 · 命中时，使目标增... |
| `BlackTearsAlly` | **深泪** | LLC 基准 (BattleKeywords-walpu6.json) | - 特殊充能(固定强度) - 特定技能发动附加效果所需的资源 - 最大值：20 |
| `BladeResultUpTier1` | **本国剑-传授洗法** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高1技能的最终威力 |
| `BladeResultUpTier2` | **本国剑-传授刺法** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高2技能的最终威力 |
| `BladelineagePride` | **杀手本位** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 每带有1层本效果，使自身增加1级攻击等级 - 斩击技能攻击命中时，使自身增加1级... |
| `Blame_LowMorale` | **迁怒** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 回合开始时，使自身获得2层强壮 并对自身施加2层易损 。 |
| `Blame_Panic` | **迁怒** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 回合开始时，随机友方单位失去20点理智值 |
| `Blandishment` | **理所应当的信念** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最小与最大速度值+1 - 攻击等级+2，防御等级+2 - 令自身基础技能增加的呼吸法 强度额外+... |
| `BlandishmentShinEnemyDelete` | **心-???** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最小与最大速度值+1 - 攻击等级+2，防御等级+2 - 令自身技能增加的呼吸法 强度与获得的呼... |
| `Blandishment_Enemy` | **理所应当的信念** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最小与最大速度值+1 - 攻击等级+3，防御等级+3 - 令自身技能增加的呼吸法 强度额外+1级 |
| `Blandishment_Shin` | **心-代行** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最小与最大速度值+2 - 攻击等级+1，防御等级+1 - 令自身基础技能增加的呼吸法 强度与获得... |
| `Blandishment_Shin_Enemy` | **心-空** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最小与最大速度值+1 - 攻击等级+2，防御等级+2 - 令自身技能增加的呼吸法 强度与获得的呼... |
| `Bleeding` | **流血** | LLC 基准 (BattleKeywords.json) | 进行攻击时，受到(现存体力×本效果层数)%的固定伤害，随后使本效果的层数减半。 |
| `BlessingAlly` | **加护** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，自身每带有8点理智值，使自身获得1层守护之剑(最多5层) - 拼点结束时，使目标增加... |
| `BlessingOfIndexPrescriptAlly` | **指令加护** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 每带有3层本效果，攻击等级+1 - 最大值：9 |
| `BlessingOfIndexPrescriptEnemy` | **指令加护** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 每带有3层本效果，攻击等级+1 - 最大值：9 |
| `BlindFaith_LowMorale` | **指令崩坏的危机** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 士气低落 - 对指令目标 造成的伤害+20% 受到来自指令目标 以外的目标的伤害+10% |
| `BlindFaith_Panic` | **指令崩坏的危机** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 陷入恐慌 - 对指令目标 造成的伤害+30% 受到来自指令目标 以外的目标的伤害+20% |
| `BloodArmor` | **硬血** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：10 - 硬血 1阶段 - 用于特殊技能 |
| `BloodArmorCasting` | **硬血铸造** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 与带有流血 或特殊流血的敌方单位进行拼点时，使自身的拼点威力+1 - 攻击技能消... |
| `BloodArmorMeursault` | **硬血甲胄** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 若自身体力未满，则自身的攻击技能攻击后，使自身恢复造成伤害量10%的体力(每回合... |
| `BloodArmorPersonalityFirst` | **硬血** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 硬血 1阶段 - 硬血 层数不低于10层时，转化为硬血II 。 - 硬血 层数... |
| `BloodArmorPersonalitySecond` | **硬血II** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 硬血 2阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等级提升  ... |
| `BloodArmorPersonalityThird` | **硬血III** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 硬血 3阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等级提升 与... |
| `BloodArmor_2nd` | **硬血II** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：20 - 硬血 2阶段 - 回合开始时：每带有6层该效果，攻击等级+1，防御等级+1 -... |
| `BloodArmor_3rd` | **硬血III** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：30 - 硬血 3阶段 - 回合开始时：每带有6层该效果，攻击等级+2，防御等级+2 -... |
| `BloodBranch` | **盲血** | LLC 基准 (BattleKeywords-a1c9p3.json) | 本效果层数每有1层，下回合对自身施加1层束缚  回合结束时，受到(自身的流血 强度×本效果层数)点体... |
| `BloodDinner` | **血宴** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 最大值：999 - 储存在该战斗场所造成的流血 伤害 - 改变战斗场所时重置本效果 - 全体单位... |
| `BloodDinner_Accumulation` | **消耗血宴总数** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 最大值：999 - 显示本场战斗中累计消耗的血宴 层数 |
| `BloodDinner_Common_Accumulation` | **共用消耗血宴总数** | LLC 基准 (BattleKeywords-a1c7p3.json) | 本场战斗中累计消耗的血宴 层数 |
| `BloodPocket` | **血囊** | LLC 基准 (BattleKeywords.json) | 积蓄到特定层数后将释放强力攻击。 |
| `BloodPocket_LowMorale` | **渴血** | LLC 基准 (BattleKeywords-mowe.json) | 回合开始时对自身施加1层易损 并使自身获得1层伤害强化 |
| `BloodPocket_Panic` | **渴血** | LLC 基准 (BattleKeywords-mowe.json) | 回合开始时对自身施加2层易损 并使自身获得2层伤害强化 |
| `BloodScissor` | **染血的剪刃** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 最大值：10 - 染血的剪刃 1阶段 - 用于特殊技能 |
| `BloodScissorPersonalityFirst` | **染血的剪刃** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 染血的剪刃 1阶段 - 染血的剪刃 层数不低于10层时，转化为染血的剪刃II ... |
| `BloodScissorPersonalitySecond` | **染血的剪刃II** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 染血的剪刃 2阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等级提... |
| `BloodScissorPersonalityThird` | **染血的剪刃III** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 染血的剪刃 3阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等级提... |
| `BloodScissorScars` | **深度裂伤** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 对自身施加3层流血 并触发流血 ，随后使流血 层数减少1层 - 回合结束时解除本效果 |
| `BloodScissorThree` | **染血的剪刃III** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 最大值：30 - 染血的剪刃 3阶段 - 回合开始时，每带有5层本效果，使自身获得2层攻击等级提... |
| `BloodScissorTwo` | **染血的剪刃II** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 最大值：20 - 染血的剪刃 2阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等级提... |
| `BloodShooting` | **血猎！！** | LLC 基准 (BattleKeywords-a1c7p1.json) | 阵亡时 - 获得30层血宴 - 获得持有量最少的2个E.G.O资源 - 下回合使全体友方单位的所有物... |
| `BloodborneDOQ` | **骑士骨血** | LLC 基准 (BattleKeywords-pilgrimage.json) | 受到的伤害+80% |
| `BloodringUp_LowMorale` | **呈血** | LLC 基准 (Bufs-a1c7p3.json) | - 士气低落 若目标未带有流血 ，则使自身的拼点威力-1，攻击命中时使自身恢复相当于目标流血 强度的... |
| `BloodringUp_Panic` | **呈血** | LLC 基准 (Bufs-a1c7p3.json) | - 陷入恐慌 若目标带有流血 ，则使自身的拼点威力+2；若目标未带有流血 ，则使自身的拼点威力-2，... |
| `Bloodthirst` | **血之渴望** | LLC 基准 (BattleKeywords-a1c971.json) | - 基础攻击等级-35 - 基础防御等级-35 |
| `BloodthirstHard` | **血之渴望** | LLC 基准 (BattleKeywords-a1c971.json) | - 基础攻击等级-25 - 基础防御等级-25 |
| `BloodyCrave` | **血色的渴求** | LLC 基准 (BattleKeywords-mowe.json) | - 使自身获得1层拼点威力提升 与1层伤害强化  - 攻击命中时，使自身获得1层浸染的血液  - 若... |
| `BloodyHand` | **染血之手** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 最大值：10 - 基础值：0 - 若本效果的层数为10，则令自身的技能命中时额外使目标增加1级破... |
| `BloodyHandGregFirst` | **染血之手** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 染血之手 1阶段 - 染血之手 层数不低于10层时，转化为染血之手II 。 -... |
| `BloodyHandGregSecond` | **染血之手II** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 染血之手 2阶段 - 回合开始时，每带有10层本效果，使自身获得1层攻击等级提... |
| `BloodyHandGregThird` | **染血之手III** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 染血之手 3阶段 - 回合开始时，每带有10层本效果，使自身获得1层攻击等级提... |
| `BloodyHand_2nd` | **染血之手II** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 任何使自身获得染血之手 的效果改为获得本效果 - 最大值：20 - 基础值：10 - 每带有6层... |
| `BloodyHand_3rd` | **染血之手III** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 任何使自身获得染血之手 的效果改为获得本效果 - 最大值：30 - 基础值：20 - 攻击威力+... |
| `BloodyMucus` | **洗礼（赤红）** | LLC 2026092102／本地格式化 | - 最大值：5 - 自身每带有3级流血 强度，使自身增加1级攻击等级(最多3级) - 若本效果层数为最大值，则使自身受到的流血 伤害变为2倍且不会因流…… |
| `BloomingRose` | **绽放的罪孽** | LLC 基准 (BattleKeywords_Refraction2.json) | 回合结束时 - 本效果层数+1。 - 被连接的人格失去体力上限25%的体力。 - 失去10%与玫瑰相... |
| `BloomingThorns` | **绽放荆棘** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 最大值：10 - 受到技能伤害时，使攻击者增加本效果层数一半的流血 强度，然后使本效果的层数减少... |
| `BloomingThornsRodionFirst` | **绽放荆棘** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 绽放荆棘 1阶段 - 每带有2层本效果，使自身增加1级防御等级(最多5级) -... |
| `BloomingThornsRodionSecond` | **绽放荆棘II** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 绽放荆棘 2阶段 - 每带有2层本效果，使自身增加1级防御等级(最多5级) -... |
| `BloomingThornsRodionThird` | **绽放荆棘III** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 绽放荆棘 3阶段 - 每带有2层本效果，使自身增加1级防御等级(最多5级) -... |
| `BloomingThorns_2nd` | **血编荆棘** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 任何使自身获得绽放荆棘 的效果改为获得本效果 - 最大值：10 - 回合开始时，每带有3层本效果... |
| `BloomingThorns_3rd` | **血塑荆棘** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 任何使自身获得绽放荆棘 的效果改为获得本效果 - 最大值：10 - 回合开始时，每带有2层本效果... |
| `Blue` | **眼泪** | LLC 基准 (BattleKeywords.json) | 回合结束时，使自身失去5点理智值 反面命中时，使目标增加2级沉沦 强度 |
| `BlueSand` | **青沙** | LLC 基准 (BattleKeywords.json) | - 拼点失败时，对自身施加1层沉沦 (每回合最多3次) - 若带有理智值，恐慌类型转变为“青沙” -... |
| `BlueSand_LowMorale` | **青沙** | LLC 基准 (Bufs.json) | - 士气低落 - 自身的拼点威力-1 - 最小与最大速度值-1 |
| `BlueSand_Main` | **青沙** | LLC 基准 (Bufs.json) | - 拼点失败时，对自身施加1层沉沦 (每回合最多3次) - 若带有理智值，恐慌类型转变为“青沙” -... |
| `BlueSand_Panic` | **青沙** | LLC 基准 (Bufs.json) | - 陷入恐慌 - 自身的拼点威力-2 - 最小与最大速度值-1 |
| `BlueSand_Sub` | **青沙** | LLC 基准 (Bufs.json) | - 拼点失败时，对自身施加1层沉沦 (每回合最多3次) - 若未带有理智值，则使最小与最大速度值-1... |
| `Blue_LowMorale` | **抑郁** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 若拼点时硬币掷出过反面，则使本次拼点威力-1。 |
| `Blue_Panic` | **抑郁** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 若拼点时硬币掷出过反面，则使本次拼点威力-3。 |
| `BoldBrushstrokes` | **果敢的笔触** | LLC 基准 (BattleKeywords-twth.json) | - 自身带有本效果时，使自身受到来自流血 与沉沦 的体力与理智伤害变为2倍 - 回合结束时，本效果层... |
| `BoldBrushstrokesRodion` | **果敢的笔触** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 每带有1层本效果，使自身受到来自流血 与沉沦 的体力与理智伤害+10%(最多+2... |
| `BoneBladeTheRings` | **作品名：法西娅** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 回合开始时，使自身获得4层基础威力提升  - 攻击技能对目标施加流血 时，额外使目标增加2级流血... |
| `BongukGiftEnhance` | **本国剑-传授击法** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 加算硬币威力+1，暴击时造成的伤害+15% - 回合结束时解除 |
| `BoseProjektil` | **撕裂的回忆** | LLC 基准 (BattleKeywords.json) | - 最大值：7 - 用于特定技能 |
| `BoseProjektilReplica` | **撕裂的回忆** | LLC 基准 (BattleKeywords-a1c8p3.json) | 最大值：7 |
| `Bothersome` | **切斩** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 目标的斩击抗性视作脆弱(1.5)。(目标的斩击抗性高于1.5时不适用) - 回合结束时解除本效果 |
| `BrandedKimSatgat` | **烙印[奴]** | LLC 基准 (BattleKeywords-exme.json) | - 基础攻击等级-？？ - 基础防御等级-？？ |
| `BreakthroughHorse` | **踏破敌阵** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 回合开始时，本回合使自身获得(本效果层数×10)点护盾 - 若本效果层数为最大值... |
| `Breath` | **呼吸法** | LLC 基准 (BattleKeywords.json) | 攻击命中时，基于效果强度提高该次攻击的暴击率，触发暴击时使效果层数减少1层。 回合结束时，本效果的层... |
| `BreathLoss_LowMorale` | **紊乱的呼吸** | LLC 基准 (BattleKeywords-a1c9p1.json) | 回合开始时，使自身减少3级呼吸法 强度 |
| `BreathLoss_Panic` | **紊乱的呼吸** | LLC 基准 (BattleKeywords-a1c9p1.json) | 回合开始时，使自身减少5级呼吸法 强度 |
| `BreathSupport` | **决战的呼吸法** | LLC 基准 (BattleKeywords_Refraction4.json) | 波次开始时，使自身增加4级呼吸法 强度并使自身获得4层呼吸法 。 |
| `BudgetBulletPropellant` | **推进弹** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 特殊弹药 - 特定技能使用时消耗 - 最大值：4 |
| `BuffetFailed` | **虚脱** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，最小与最大速度值-1 - 回合开始时，对自身施加1层易损  - 回合结束时，本效果层数减少1层 (适用于所有部位…… |
| `BuffetSick` | **痛苦之袋** | LLC 2026092102／本地格式化 | - 最大值：30 - 回合结束时，若狂暴 效果解除，则解除本效果，每减少5层，下回合对自身施加1层易损  |
| `Bull_BuzzingEmotion` | **飘忽不定的情绪** | LLC 基准 (BattleKeywords.json) | 回合开始时，随机对自身施加虚弱 、麻痹 、束缚 中的一种效果，其层数与本效果相同，随后解除本效果 |
| `Bull_FadedHeat` | **片刻冷静** | LLC 基准 (BattleKeywords.json) | 本体与躯干的体力上限-50% |
| `Bull_Fever` | **狂热** | LLC 基准 (BattleKeywords.json) | 每层使造成的伤害+10%。 回合结束时，本效果的层数减少1层 |
| `Bull_ReinforcedSadness` | **愈加膨胀的哀伤** | LLC 基准 (BattleKeywords.json) | 改变自身的行为。 |
| `Bull_Sadness` | **尚未释怀的哀伤** | LLC 基准 (BattleKeywords.json) | 回合开始时，施加与本效果层数相同的虚弱  回合结束时，若层数不低于3层，则转化为愈加膨胀的哀伤 |
| `Bullet` | **弹药** | LLC 基准 (BattleKeywords.json) | 特定技能进行攻击时消耗的资源。 缺少弹药时这些攻击将被取消。 |
| `BulletFreischutz` | **未使用** | LLC 基准 (BattleKeywords.json) | 未使用 |
| `BulletGodok` | **弹药-孤独** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 最大值：6 特定技能使用时消耗  - 本弹药不会因外部效果获得或增加 |
| `BulletLament` | **生蝶·亡蝶** | LLC 基准 (BattleKeywords-walpu4.json) | - 特殊弹药 - 强度与层数之和最大值：20 - 特定技能使用时消耗 - 消耗时，随机选择本效果的生... |
| `BulletPropellant` | **虎标弹** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 特殊弹药 - 特定技能使用时消耗 - 最大值：6 |
| `BulletPropellantAlly` | **虎标弹** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 若自身消耗的虎标弹 与猛虎标弹 之和不低于8发，则使自身的被动效果改为获得心-天退... |
| `BulletPropellantSpecial` | **猛虎标弹** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 特殊弹药 - 特定技能使用时消耗(适用于虎标弹 的效果) - 本效果的强度为已装填的弹药，层数为... |
| `BulletPropellantSpecialAlly` | **猛虎标弹** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 若自身消耗的虎标弹 与猛虎标弹 之和不低于8发，则使自身的被动效果改为获得心-天退... |
| `Bullet_Crab` | **蟹壳废料弹** | LLC 基准 (BattleKeywords.json) | 使用特定技能时，消耗蟹壳废料弹 |
| `Bullet_LogicAtelier` | **弹药-逻辑工作室** | LLC 基准 (BattleKeywords.json) | 特殊弹药 逻辑工作室特制弹药 - 本弹药 的层数不会因为外部效果而增加 |
| `Burn` | **烧伤** | LLC 基准 (BattleKeywords.json) | 回合结束时，受到等同于本效果层数的固定伤害，随后使本效果的层数减半。 |
| `BurningWoundRien` | **灼烧着的伤口** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级-5，防御等级-5 - 回合开始时，每带有1层本效果，对自身施加1层烧伤 与1层流血  ... |
| `BurningWoundRien_Mask` | **里恩的假面** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级-5，防御等级-5 - 每带有1层本效果，使自身受到施加烧伤 或流血 (包括强度、层数与... |
| `BurningWoundYisang` | **灼烧着的伤口** | LLC 基准 (BattleKeywords.json) | - 攻击等级+3，防御等级-3 - 受到单方面攻击的伤害-25% - 回合开始时，使自身增加1级烧伤... |
| `BurningWoundYisangMask` | **遮盖伤口的假面** | LLC 基准 (BattleKeywords.json) | - 攻击等级+2，防御等级-2 - 受到单方面攻击的伤害-10% |
| `Burst` | **破裂** | LLC 基准 (BattleKeywords.json) | 受到攻击时，附加数值等同于本效果强度的固定伤害。 效果生效后，本效果的层数减少1层。 |
| `BurstAgility` | **咒杀【迅捷】** | LLC 基准 (BattleKeywords-a1c9116.json) | 基础值：3 因受到速度值不低于10的目标的攻击技能攻击而触发自身的破裂 时，使本效果的层数减少1层并... |
| `BurstPoison` | **咒杀【剧毒】** | LLC 基准 (BattleKeywords.json) | 基础值：5 - 咒杀 - 因受到目标的暴击攻击而触发自身的破裂 时，使本效果的层数减少1层 - 因该... |
| `BurstProtection` | **破裂守护** | LLC 基准 (BattleKeywords.json) | 一回合内，本效果每有1层，受到来自破裂 效果造成的伤害减少1点 |
| `BurstStop` | **咒杀【勿动】** | LLC 基准 (BattleKeywords-a1c8p2.json) | 基础值：4 - 咒杀 - 自身的束缚 层数不低于3层并触发自身的破裂 时，使本效果的层数减少1层 -... |
| `BurstSuppress` | **咒杀【掣肘】** | LLC 基准 (BattleKeywords-a1c8p2.json) | 基础值：10 - 咒杀 - 自身的其他咒杀通过其条件减少层数时，使本效果的层数减少1层(每回合最多4... |
| `BurstVulnerable` | **破裂易损** | LLC 基准 (BattleKeywords.json) | 一回合内，本效果每有1层，受到来自破裂 效果造成的伤害增加1点 |
| `BurstVulnerableZilu` | **崩坏印记** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 受到暴食技能的伤害+10% - 受到咒杀效果的伤害+10% - 回合结束时解除 |
| `BurstWave` | **咒杀【衰亡】** | LLC 基准 (BattleKeywords-a1c8p2.json) | 基础值：10 - 咒杀 施加本效果的单位触发破裂 时，使本效果的层数减少1层 - 并使自身除本咒杀以... |
| `BurstWeakness` | **咒杀【弱化】** | LLC 基准 (BattleKeywords-a1c8p2.json) | 基础值：5 - 咒杀 - 若目标的速度值高于自身至少5点，则自身因被命中而触发自身的破裂 时，使本效... |
| `BurstZilu` | **咒杀【破】** | LLC 基准 (BattleKeywords.json) | - 基础值：3 - 若自身带有咒杀时触发自身的破裂 ，则使本效果的层数减少1层，并在下回合对自身施加... |
| `CallOfSea_LowMorale` | **同族的呼唤** | LLC 基准 (BattleKeywords-pilgrimage.json) | 回合结束时，消耗自身3%的体力，使全体友方单位获得1层强壮 并对全体友方单位施加1层易损 |
| `CallOfSea_Panic` | **同族的呼唤** | LLC 基准 (BattleKeywords-pilgrimage.json) | 回合结束时，消耗自身5%的体力并对自身施加1层易损 ，使全体友方单位获得1层强壮 并对全体友方单位施... |
| `CalmAnalysisMoses` | **冷静分析** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 对精灵提灯造成的伤害+25% |
| `CanDuelGuard` | **可拼点防御** | LLC 基准 (BattleKeywords.json) | - 拼点胜利时，根据自身的最终拼点威力使目标的混乱阈值前移。 - 拼点失败受到攻击时，根据自身的最终... |
| `CandyForCharon` | **糖果？** | LLC 基准 (BattleKeywords-fools.json) | - 最大值：1 - 糖果在哪里？ |
| `CandyForCharon_LowMorale` | **糖果** | LLC 基准 (BattleKeywords-fools.json) | - 士气低落 - 与带有糖果 的人格进行拼点时，拼点威力+3；与其他人格进行拼点时，拼点威力-1 |
| `CandyForCharon_Panic` | **糖果** | LLC 基准 (BattleKeywords-fools.json) | - 陷入恐慌 - 与带有糖果 的人格进行拼点时，拼点威力+5；与其他人格进行拼点时，拼点威力-2 |
| `CaseOverheating` | **过热的棺** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 回合结束时，下回合使自身增加3级烧伤 强度并解除本效果 |
| `CentipedePoison` | **百足剧毒** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 回合结束时，下回合对自身施加(本效果层数/4)层防御等级降低 (向下取整) -... |
| `CentralCommandTeamCaptain` | **中央本部队长** | LLC 基准 (BattleKeywords-walpu6.json) | - 该人格的行动槽+1，将该人格的一个1技能替换为3技能 - 自身技能增加的烧伤 、流血 、破裂 、... |
| `Charge` | **充能** | LLC 基准 (BattleKeywords.json) | 特定技能发动附加效果所需的资源。最多叠加至20层。回合结束时，本效果的层数减少1层。 |
| `ChargeBodyArt` | **活体材料** | LLC 基准 (BattleKeywords.json) | - 最大层数：20 - 特殊充能 - 本效果强度与层数的增减同样受普通充能 影响 - 回合结束时，本... |
| `ChargeForceField` | **充能力场** | LLC 基准 (BattleKeywords.json) | - 获得(充能力场 层数 × 3)点护盾 - 若失去(充能力场 层数 × 3)点护盾，则使自身消耗1... |
| `ChargeLoad` | **载荷** | LLC 基准 (BattleKeywords.json) | - 最大值：6 - 本效果每有1层，使消耗充能 层数的攻击技能造成的伤害+2.5%（最多+15%） ... |
| `ChargeNoir` | **保存** | LLC 2026092102／本地格式化 | - 特殊充能 - 最大层数：20 - 本效果强度与层数的增减同样受普通充能 影响 - 回合结束时，本效果的层数减少1层 |
| `ChargeNoirAlly` | **保存** | 工作区 (BattleKeywords.json) | - 特殊充能 - 层数上限：20 - 同样受到增加、减少充能强度与层数的效果影响 - 回合结束时，层... |
| `ChargeRouge` | **搏动** | LLC 2026092102／本地格式化 | - 特殊充能 - 最大层数：20 - 本效果强度与层数的增减同样受普通充能 影响 - 回合结束时，本效果的层数减少1层 |
| `ChargeRougeAlly` | **脉动** | 工作区 (BattleKeywords.json) | - 特殊充能 - 层数上限：20 - 同样受到增加、减少充能强度与层数的效果影响 - 回合结束时，层... |
| `ChargedSting` | **电荷针** | LLC 基准 (BattleKeywords.json) | - 每层本效果使自身受到获得或消耗充能 层数(包括特殊充能)的技能的伤害+4%(最多+20%) · ... |
| `ChasingArcana` | **咏唱-阿卡纳光破斩** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：3 - 回合开始时，使本效果的层数增加1层 - 若本效果层数为3层，则下回合使自身的速度... |
| `ChasingArcanahard` | **咏唱-阿卡纳光破斩** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：3 - 回合开始时，使本效果的层数增加1层 - 若本效果层数为3层，则下回合对自身施加2... |
| `CheerUpXichun` | **援** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 若目标带有的负面状态不少于5种，则使自身的拼点威力+1，造成的伤害+10% |
| `Chesed_Mercy` | **Chesed的慈悲** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 全体单位的攻击等级与防御等级调整为全体单位的平均值 - 友方人格应用Chesed效果时，额外增加... |
| `ChickenFightlust` | **血斗本能** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 每带有1层本效果，使自身造成的伤害+0.75% - 每带有10层本效果，回合结... |
| `ChickenStance` | **血炎** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 令自身通过基础技能使敌方单位增加的烧伤 强度与破裂 强度额外+1级 - 自身带有... |
| `ChoSuperCharge` | **超亚光蓄能** | LLC 基准 (BattleKeywords.json) | - 最大值：100 - 自身消耗充能 层数时，获得层数相当于消耗量的本效果 - 最大充能 层数+10... |
| `ChoiSword_LowMorale` | **显影的记忆** | LLC 基准 (BattleKeywords-exme.json) | - 士气低落 - 对自身施加1层易损 ，使自身造成的伤害+10%，暴击时造成的伤害+15% |
| `ChoiSword_Panic` | **显影的记忆** | LLC 基准 (BattleKeywords-exme.json) | - 陷入恐慌 - 对自身施加2层易损 ，使自身造成的伤害+10%，暴击时造成的伤害+30%，令本国弓... |
| `ChoiSwordsmanship` | **本国剑术[肉]** | LLC 基准 (BattleKeywords-exme.json) | - 最小值：1，最大值：9 - 使用技能时，若本效果层数为最小值或最大值，则使自身使用的所有硬币转化... |
| `ChoiSwordsmanshipMany` | **本国姿态-狩虎** | LLC 基准 (BattleKeywords-exme.json) | 使用由<color=#ff6000><mark color=#ff000040><b><u>多硬币<... |
| `ChoiSwordsmanshipOne` | **本国姿态-狩熊** | LLC 基准 (BattleKeywords-exme.json) | 使用由<color=#ff6000><mark color=#ff000040><b><u>单硬币<... |
| `ChoiSwordsmanshipShield` | **布面甲[肉]** | LLC 基准 (BattleKeywords-exme.json) | - 最大值：5 - 获得本效果时，每获得1层本效果，获得相当于自身体力上限10%的护盾(最少1点，向... |
| `Choice_1030301` | **事件效果** | LLC 基准 (Bufs.json) | 战斗开始时，获得3层强壮 。 |
| `Choice_1030501` | **事件效果** | LLC 基准 (Bufs.json) | 每回合开始时施加5层虚弱 。 |
| `Choice_1031001` | **事件效果** | LLC 基准 (Bufs.json) | 每回合开始时施加3层伤害弱化 。 |
| `Choice_1040301` | **未知的伤口** | LLC 基准 (Bufs.json) | 本回合内，使自身增加10级破裂 强度 |
| `Choice_901001` | **燎原** | LLC 基准 (BattleKeywords.json) | 战斗开始时，技能组不包含暴怒属性攻击技能的人格受到5点暴怒伤害 |
| `Choice_901007` | **惜别** | LLC 基准 (BattleKeywords.json) | 回合开始时，恢复10点体力与理智值(最多3回合) |
| `Choice_901009` | **眩目** | LLC 基准 (BattleKeywords.json) | 战斗开始时，技能的最终威力-1。 |
| `Choice_901010` | **放空** | LLC 基准 (BattleKeywords.json) | 战斗开始时，技能组不包含色欲属性攻击技能的人格陷入混乱。 |
| `Choice_901019` | **秽物** | LLC 基准 (BattleKeywords.json) | 战斗开始时，速度值-2。 |
| `Choice_90103301` | **挣扎** | LLC 基准 (BattleKeywords.json) | 本场战斗速度值+1。 |
| `Choice_90103402` | **安心** | LLC 基准 (BattleKeywords.json) | 本场战斗速度值+2。 |
| `Choice_90104001` | **理解** | LLC 基准 (BattleKeywords.json) | 战斗开始时，所有E.G.O资源+2 |
| `Choice_9010400101` | **觉悟** | LLC 基准 (BattleKeywords.json) | 本场战斗中，全体人格技能的最终威力+2 |
| `Choice_90104002` | **思慕** | LLC 基准 (BattleKeywords.json) | 本场战斗中，全体人格的技能威力+1 |
| `Church_LowMorale` | **教团** | LLC 基准 (BattleKeywords-walpu5.json) | - 士气低落 - 战斗中，使自身增加烟气 强度或对自身施加烟气 层数时，额外增加1级烟气 强度或施加... |
| `Church_Panic` | **教团** | LLC 基准 (BattleKeywords-walpu5.json) | - 陷入恐慌 - 战斗中，使自身增加烟气 强度或对自身施加烟气 层数时，额外增加2级烟气 强度或施加... |
| `Cianjing` | **弦惊** | LLC 基准 (BattleKeywords.json) | - 回合开始时，使自身获得1层攻击等级提升 与1层防御等级提升  - 回合结束时，本效果层数减少1层... |
| `CleanUp_LowMorale` | **整理强迫** | LLC 基准 (Bufs-a1c6p1.json) | - 士气低落 - 拼点失败时，使自身失去5点理智值。受到攻击时，下回合使自身获得1层迅捷 (最多2层... |
| `CleanUp_Panic` | **整理强迫** | LLC 基准 (Bufs-a1c6p1.json) | - 陷入恐慌 - 对自身施加2层易损 。受到攻击时，下回合使自身获得1层迅捷 (最多3层) |
| `CloudWall` | **云障** | LLC 基准 (BattleKeywords.json) | 最大值：1 守备技能的最终威力+1 使用“后巷规矩”攻击后或回合结束时解除本效果 |
| `Coffin` | **棺** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 回合结束时： 自身每带有3层本效果，下回合使自身获得2层伤害强化 (最多6层)... |
| `ColdAirDOQ` | **寒冷** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 最大值：3 - 每带有1层寒冷 ，使自身的速度值-1 - 技能结束时，若本效果层数为3层，则受到... |
| `ColdBlackTear` | **漆黑冰冷之泪** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：5 - 回合开始时，对自身施加1层拼点威力降低  - 若自身带有本效果时被命中，则使自身... |
| `Collage_LowMorale` | **混杂的记忆** | LLC 基准 (BattleKeywords-exme.json) | - 回合开始时，使自身获得1~3层攻击等级提升 并对自身施加1~3层防御等级降低 |
| `Collage_Panic` | **混杂的记忆** | LLC 基准 (BattleKeywords-exme.json) | - 回合开始时，使自身获得1~5层攻击等级提升 并对自身施加1~5层防御等级降低 |
| `CollapseAmpoule` | **崩解安瓿** | LLC 基准 (BattleKeywords.json) | 受到体力上限2%的伤害。 |
| `CollapsedPride` | **崩溃的自尊** | LLC 基准 (BattleKeywords-walpu6.json) | 被“饱经风霜的骑士”被动技能使用 |
| `Combustion` | **烧伤** | LLC 基准 (BattleKeywords.json) | 回合结束时，受到数值等同于本效果强度的固定伤害。 回合结束后，本效果的层数减少1层。 |
| `ComeForwardToTheKing` | **觐见之时** | LLC 基准 (BattleKeywords_Refraction4.json) | 使自身所有攻击技能的攻击容量增加相当于本效果层数的数值。(最多+2) 拼点失败时，下回合对自身施加1... |
| `CommonExit` | **脱离战场** | LLC 基准 (BattleKeywords.json) | - 回合结束时，解除自身的混乱并从战斗中撤退(不包括强制混乱，不视作阵亡) |
| `Complacency` | **过热** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：5 - 回合开始时，对自身施加层数相当于本效果层数的拼点威力降低 与易损  - 回合结束... |
| `ConcentratedAttack` | **集中攻击** | LLC 基准 (BattleKeywords-a1c7p1.json) | 对上回合成功攻击的行动槽使用技能时，根据累计成功攻击的回合数，获得对应效果。 - 累计攻击成功1次：... |
| `ConcentratedAttackMeursault` | **集中攻击-默尔索** | LLC 基准 (BattleKeywords-a1c7p1.json) | <集中遭遇战专属> 施加本集中攻击的单位根据目标行动槽的集中攻击层数获得相应效果， 1层：拼点威力+... |
| `ConcussionWei` | **脑震荡** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：3 - 受到攻击时，每带有1层本效果，使自身受到的伤害+30%(最多+90%) - 使自... |
| `ConcussionYisang` | **脑震荡** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 使自身受到的破裂 伤害与震颤引爆 造成的混乱阈值量前移变为1.2倍(向下取整) ... |
| `CondensedBlood` | **污血** | LLC 基准 (BattleKeywords.json) | 最大值：5 - 回合结束时，每带有1层本效果，使自身受到体力上限20%的伤害(不会因该效果而陷入混乱... |
| `CondensedBloodRefraction` | **龙血** | LLC 基准 (BattleKeywords_Refraction6.json) | - 最大强度：50 - 回合结束时，本效果强度每有1级，使自身受到体力上限1%的伤害(最少1点，不会... |
| `ConfinementOfGoldenBranch` | **金枝的强制调律** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 基础攻击等级-30 - 基础防御等级-30 |
| `ConnectedPlug` | **连接的插头** | LLC 基准 (BattleKeywords_Refraction4.json) | 回合结束时： - 最多3层 - 3层时，下回合陷入混乱。 - 3层时，消耗自身所有充能 。 |
| `ContemptPersonality` | **视线的轻蔑** | LLC 基准 (BattleKeywords.json) | - 使自身获得7层守护  - 对自身施加7层伤害弱化  - 使自身1个行动槽的挑衅值 +20 - 视... |
| `ContemptReplica` | **轻蔑** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：1 - 使自身对贾环造成的伤害与受到来自贾环的伤害-50% - 带有轻蔑 的目标不能获得... |
| `ContemptRyoshu` | **轻蔑** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 使自身对良秀造成的伤害与受到来自良秀的伤害-50% - 带有轻蔑 的目标不会获得... |
| `CountSkillMidOutis` | **愈加炽热的兴致** | LLC 基准 (BattleKeywords.json) | 满足以下条件时，使本效果的层数减少1层(每回合最多1次) - 使用技能“仇怨重踏”时(包括通过反击使... |
| `CoverAttack` | **援护攻击** | LLC 基准 (BattleKeywords.json) | - 若A单位使B单位获得本效果，则在A单位的攻击技能结束时，B单位使用自身的1技能对相同的敌方单位进... |
| `CoveringFire` | **锁定目标** | LLC 基准 (BattleKeywords.json) | 若A单位使B单位获得本效果，则在A单位的攻击技能结束时，B单位使用自身的2技能对相同的敌方单位进行单... |
| `CrazyWei` | **狂化** | LLC 基准 (BattleKeywords-cultivation.json) | - 攻击等级-15 - 防御等级-15  - 回合结束时，脚力【午】不会增加防御等级，而改为获得层数... |
| `Crazy_LowMorale` | **疯狂** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 首次陷入士气低落时，进入无差别攻击状态 |
| `Crazy_Panic` | **疯狂** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 进入无差别攻击状态；拼点威力+1，获得2层伤害强化 |
| `CriHurtNightStiletto` | **深度创伤** | LLC 基准 (BattleKeywords.json) | - 基础值：3 - 震颤引爆时，对自身施加1层流血 (每回合最多2次) - 无法被施加创伤 (集中遭... |
| `CrimsonDamageDown` | **暴怒伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低暴怒技能造成的伤害。(最多10层) |
| `CrimsonDamageUp` | **暴怒伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高暴怒技能造成的伤害。(最多10层) |
| `CrimsonResistDown` | **暴怒抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的暴怒抗性增加(每层0.1) |
| `CrimsonResistUp` | **暴怒抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的暴怒抗性减少(每层0.1) |
| `CrimsonResultDown` | **暴怒威力降低** | LLC 基准 (Bufs.json) | 本回合内暴怒技能的最终威力-{0} |
| `CrimsonResultUp` | **暴怒威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高暴怒技能的最终威力。 |
| `CrimsonTakeDamageDown` | **暴怒守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自暴怒技能的伤害。(最多10层) |
| `CrimsonTakeDamageUp` | **暴怒易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自暴怒技能的伤害。(最多10层) |
| `CriticalDamageUp` | **暴击伤害强化** | LLC 基准 (BattleKeywords-a1c9p3.json) | 每带有1层本效果，本回合使自身暴击时造成的伤害+10% |
| `CriticalDmgUpVespa` | **闪蜂光剑术-环刀** | LLC 基准 (BattleKeywords-a1c9p2.json) | 每带有1层本效果，本回合使自身的暴击倍率额外+10% |
| `Cromer_Boredom` | **接受痛苦吧！** | LLC 基准 (Bufs.json) | 造成与受到的伤害+100%。 守备技能的最终威力-5。 |
| `Cromer_Ecstasy` | **狂喜** | LLC 基准 (BattleKeywords.json) | 大嘴部位的物理抗性全部变为“致命”。 |
| `Cromer_Madness` | **纯粹** | LLC 基准 (BattleKeywords.json) | 使所有部位获得3层伤害强化 并对其施加3层束缚 ，且其物理抗性全部变为“致命”。 |
| `Cromer_Target` | **执柄者的凝视** | LLC 基准 (BattleKeywords.json) | 陷入混乱一回合。受到来自克罗默的伤害+100%。 |
| `CrushMarks` | **破碎痕** | LLC 基准 (BattleKeywords.json) | - 受到暴食与忧郁技能的伤害+10% - 若目标带有理智值，则使其恐慌类型转变为“破碎痕” - 若目... |
| `CrushMarks_LowMorale` | **破碎痕** | LLC 基准 (Bufs.json) | - 士气低落 - 自身的拼点威力-1，防御等级-2 |
| `CrushMarks_Main` | **破碎痕** | LLC 基准 (Bufs.json) | - 受到暴食与忧郁技能的伤害+10% - 若目标带有理智值，则使其恐慌类型转变为“破碎痕” - 回合... |
| `CrushMarks_Panic` | **破碎痕** | LLC 基准 (Bufs.json) | - 陷入恐慌 - 自身的拼点威力-2，防御等级-3 |
| `CrushMarks_Sub` | **破碎痕** | LLC 基准 (Bufs.json) | - 受到暴食与忧郁技能的伤害+10% - 若目标未带有理智值，则使其拼点威力-1 - 回合结束时，本... |
| `CtrlTeamCaptain` | **控制部队长** | LLC 基准 (BattleKeywords.json) | - 行动槽+1 - 将该人格的一个1技能替换为3技能 - 当该单位使用技能击杀敌方单位时，使理智值最... |
| `Cubism_LowMorale` | **过时的艺术** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 回合开始时，使自身获得1层攻击等级提升 |
| `Cubism_Panic` | **过时的艺术** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 回合开始时，使自身获得2层攻击等级提升 |
| `CuredFilm` | **硬化屏障** | LLC 基准 (BattleKeywords.json) | - 回合开始时，使自身获得(本效果层数/3)层防御等级提升 (最多3层，向下取整) - 受到敌方单位... |
| `Curse` | **诅咒** | LLC 基准 (BattleKeywords.json) | 回合结束时，下回合随机施加以下效果，随后使本效果的层数减少1层。随机效果包括1层虚弱 ，1层破绽 ，... |
| `CursePackage` | **诅咒包裹** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：1 - 回合结束时，对自身施加1层虚弱 ，1层破绽 ，2层攻击等级降低 与2层防御等级降... |
| `CutbondRyoshu` | **无我** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，本效果层数每有10层，使自身获得1层攻击等级提升 与1层防御等级提升  - 本效果的... |
| `CutoffRyoshu` | **切丝** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时， · 使自身增加3级流血 强度并对自身施加3层流血  · 受到(本效果层数/3)点斩... |
| `Cycle` | **业报** | LLC 基准 (BattleKeywords.json) | 基于本效果层数增加受到的伤害(每层增加1%)。回合结束时，若本效果的层数不低于108层，则使角色直接... |
| `CyclingKarma` | **业报轮回** | LLC 基准 (BattleKeywords.json) | 场上所有单位在攻击命中时会将自身的部分业报 转移给目标。场上有无我入定以外的敌方单位存活时，业报 无... |
| `DOQ_LowMorale` | **蜂巢意识** | LLC 基准 (BattleKeywords-pilgrimage.json) | 所有抗性变为一般 |
| `DOQ_Panic` | **蜂巢意识** | LLC 基准 (BattleKeywords-pilgrimage.json) | 所有抗性变为一般 技能使自身增加的烧伤 、流血 、震颤 与破裂 强度变为2倍 |
| `DamageOverTime` | **持续损伤** | LLC 基准 (BattleKeywords.json) | 回合开始时，受到等同于本效果层数的固定伤害。 |
| `DarkBeastSnake_LowMorale` | **暗臂** | LLC 基准 (BattleKeywords-cultivation.json) | - 士气低落 - 自身的拼点威力-1，受到的伤害-10% |
| `DarkBeastSnake_Panic` | **暗臂** | LLC 基准 (BattleKeywords-cultivation.json) | - 陷入恐慌 - 自身的拼点威力-2，受到的伤害-20% |
| `DarkBeast_LowMorale` | **暗算** | LLC 基准 (BattleKeywords-a1c9116.json) | - 士气低落 - 自身的速度值高于目标或进行单方面攻击时，对目标造成的伤害+10% |
| `DarkBeast_Panic` | **暗算** | LLC 基准 (BattleKeywords-a1c9116.json) | - 陷入恐慌 - 自身的速度值高于目标或进行单方面攻击时，对目标造成的伤害+20%；自身的速度值高于... |
| `DarkFlame` | **黑焰** | LLC 基准 (BattleKeywords.json) | - 特殊烧伤 - 最大值：7 - 基于本效果层数减少防御等级 - 回合结束时，受到(本效果层数×烧伤... |
| `DarkHongluParryGahwan` | **多么可憎啊，兄长。** | LLC 基准 (BattleKeywords.json) | 与贾环进行拼点时，使自身的拼点威力+2 |
| `DarkHongluQiuAndHonglu` | **践行霸道之人** | LLC 基准 (BattleKeywords.json) | - 鸿璐的所有技能最终威力+1 - 拼点胜利时，使理智值最低的1名友方单位(包括自身)恢复5点理智值... |
| `DarkHongluTeaching` | **贯彻** | LLC 基准 (BattleKeywords.json) | 最大值：3 - 回合结束时，使自身恢复5点理智值 - 战斗中自身的体力降至0点时，使自身恢复全部体力... |
| `DarkHonglu_Ai` | **喜、乐、哀** | LLC 基准 (BattleKeywords.json) | - 鸿璐的最终威力+3 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) - 友... |
| `DarkHonglu_EGOResourceup` | **纵使令千万人血流成河…** | LLC 基准 (BattleKeywords.json) | [鸿璐特殊效果] - 本场战斗中，自身的技能攻击结束后，额外获得该技能对应属性的2个E.G.O资源(... |
| `DarkHonglu_Le` | **喜、乐** | LLC 基准 (BattleKeywords.json) | - 鸿璐的最终威力+1 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) - 本... |
| `DarkHonglu_Nu` | **喜、乐、哀、怒** | LLC 基准 (BattleKeywords.json) | - 鸿璐的最终威力+5 - 每回合开始时，使全体友方单位恢复5点理智值(包括自身) - 友方单位阵亡... |
| `DarkHonglu_Xi` | **喜** | LLC 基准 (BattleKeywords.json) | - 鸿璐的拼点威力+1 - 本场战斗中，不低于1名其他友方单位存活时，鸿璐受到致死伤害时不会阵亡，改... |
| `DaughterEducationSpider` | **仔细看好，闺女！** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 每受到2次技能攻击，使本效果的层数减少1层 - 本效果的层数每有2层，使自身的... |
| `DaughterEducationSpiderOutis` | **仔细看好，闺女！** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 每受到2次技能攻击，使本效果的层数减少1层 - 若本效果的层数不低于5层，则使... |
| `Daunted_LowMorale` | **畏缩(士气低落)** | LLC 基准 (Bufs.json) | - 士气低落 - 回合开始时，施加2层虚弱 。 |
| `Daunted_Panic` | **畏缩** | LLC 基准 (Bufs.json) | - 陷入恐慌 - 回合开始时，施加4层虚弱 。 |
| `DawnFaust` | **正午** | LLC 基准 (BattleKeywords.json) | - 最小速度值+2 - 自身使用基础攻击技能时，使该技能基础威力+2，造成的伤害+(45/硬币数)%... |
| `DawnFaustDying` | **孤独的正午** | LLC 基准 (BattleKeywords.json) | - 最小速度值+2 - 自身使用基础攻击技能时，使该技能基础威力+3，造成的伤害+(90/硬币数)%... |
| `DawnGregor` | **自黎明至黄昏** | LLC 基准 (BattleKeywords.json) | - 若自身的混乱阈值不低于3条，则移除自身的第一混乱阈值 - 回合结束时，若自身陷入混乱，则解除自身... |
| `DawnGregorDying` | **燃烧的黄昏** | LLC 基准 (BattleKeywords.json) | - 若自身的混乱阈值不低于3条，则移除自身的第一混乱阈值 - 回合结束时，若自身陷入混乱，则解除自身... |
| `DawnLight` | **迎接黎明** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 增加烧伤 强度，施加烧伤 层数或施加特殊烧伤的基础技能造成的伤害+10% · 若... |
| `DawnTeam` | **黎明事务所** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 每带有1层本效果，使自身增加1级攻击等级 - 回合开始时，若本效果层数为3层，则... |
| `DeadEGOResource` | **遗留的意志** | LLC 基准 (BattleKeywords-Refraction1BokGak.json) | 阵亡时，根据自身拥有的基础攻击技能的罪孽与级别，获得相应的E.G.O资源 |
| `Decay` | **腐化外皮** | LLC 基准 (Bufs.json) | 受到攻击时，对攻击者施加3层剧毒 。 |
| `DecoyRegenerated` | **再生** | LLC 基准 (BattleKeywords_Refraction2.json) | 每当部位被恢复时，层数+1。 |
| `DecreamentalDefense` | **严重的负伤** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 在之前战斗中的负伤还未恢复。 - 体力上限大幅减少 - 回合开始时，根据累计回合数使自身获得相应... |
| `DeepAngry_LowMorale` | **郁愤** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+2 回合开始时，使自身获得2层伤害... |
| `DeepAngry_Panic` | **郁愤** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+3 回合开始时，使自身获得3层伤害... |
| `DeepEvilHeart_LowMorale` | **邪心深重** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+2 回合开始时，使自身获得3层伤害... |
| `DeepEvilHeart_Panic` | **邪心深重** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+3 回合开始时，使自身获得4层伤害... |
| `DefenseBug` | **防御害虫[蜚蠊]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：50 - 自身被增加(烧伤、流血、震颤、破裂、沉沦)强度或被施加该效果层数时，改为使本效... |
| `DefenseDown` | **防御等级降低** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低防御等级。 |
| `DefenseUp` | **防御等级提升** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加防御等级。 |
| `DefensiveStance` | **防御姿态** | LLC 基准 (BattleKeywords.json) | - 最大值：2 -  本效果无法叠加，施加本效果时会改为将现存层数变为施加的层数 - 回合结束时本效... |
| `DeliciousSauce` | **黄金秘传酱汁** | LLC 基准 (BattleKeywords-x1p1c1.json) | - 使自身的拼点威力+2 |
| `DelusionGregBigBird` | **眩惑** | LLC 基准 (BattleKeywords.json) | - 自身的沉沦 强度与烧伤 强度之和每有1级，使自身受到来自基础攻击技能的伤害+0.5%(最多+10... |
| `DelusionGregBigBird_LowMorale` | **眩惑** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 回合结束时，下回合对自身施加1层束缚 与2层攻击等级降低 |
| `DelusionGregBigBird_Main` | **眩惑** | LLC 基准 (BattleKeywords.json) | - 自身的沉沦 强度与烧伤 强度之和每有1级，使自身受到来自基础攻击技能的伤害+0.5%(最多+10... |
| `DelusionGregBigBird_Panic` | **眩惑** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 回合结束时，下回合对自身施加1层束缚 与4层攻击等级降低 |
| `DelusionGregBigBird_Sub` | **眩惑** | LLC 基准 (BattleKeywords.json) | - 自身的沉沦 强度与烧伤 强度之和每有1级，使自身受到来自基础攻击技能的伤害+0.5%(最多+10... |
| `DelusionHohenheimBigBird` | **眩惑** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，若自身未陷入混乱，则自身最后一个行动槽装备的攻击技能优先攻击霍恩海姆，且无法改变目标... |
| `DerivativeHugeIrritation` | **心-天退星** | LLC 基准 (BattleKeywords_Mirror6.json) | - 回合开始时，自身每失去15%的体力，使自身获得1层伤害强化 与1层威力提升 (分别最多5层) -... |
| `Desire` | **欲望** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果的层数不低于5层，则受到30点理智伤害，并施加2层易损 和10层束缚 ，随后解除... |
| `DesireToSave_LowMorale` | **善意之心** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 造成的伤害+(目标的神经损伤 层数/2)%(最多+15%) 回合开始时，使自身获得1层伤害强化 ... |
| `DesireToSave_Panic` | **善意之心** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 造成的伤害+(目标的神经损伤层数)%(最多+30%) - 回合开始时，使自身获得2层伤害强化 并... |
| `DespairAlly` | **绝望** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，自身每带有-8点理智值，使自身获得1层穿刺之剑(最多5层) - 拼点结束时，对目标施... |
| `DesperadoBuff` | **亡命之徒** | LLC 基准 (BattleKeywords-walpu8.json) | - 最大值：2 - 每带有1层本效果，使自身基础攻击技能的拼点威力+1，基础威力+1 - 若本效果层... |
| `DeterioratingBody` | **求生本能** | LLC 2026092102／本地格式化 | - 最大值：5 - 体力不会低于1点 - 受到攻击时，本效果层数减少1层(每个技能最多2次) - 回合结束时，本效果层数减少1层；本效果解除时，自身阵…… |
| `DevyatDimensionalSack` | **派送箱-罗佳** | LLC 基准 (BattleKeywords.json) | - 基础值：0 - 回合开始时，使自身获得3层本效果 - 撤退时本效果层数不会解除，而改为暂存 - ... |
| `DevyatDimensionalSackSinclair` | **派送箱-辛克莱** | LLC 基准 (BattleKeywords.json) | - 基础值：0 - 回合开始时，使自身获得3层本效果 - 撤退时本效果层数不会解除，而改为暂存 - ... |
| `DianxueDonQuixote` | **点穴-堂吉诃德** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 施加本点穴的单位根据目标(或部位)的点穴层数获得相应效果， · 1层：拼点威力+... |
| `DianxueHongLu` | **点穴-鸿璐** | 工作区 (BattleKeywords.json) | - 最大值：3 - 施加点穴的角色根据目标(或部位)的点穴数值获得以下效果： · 1层：拼点威力+1... |
| `DicipleLittleFinger` | **月下青刀** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：50 - 回合开始时，每带有1层本效果，使自身获得5点护盾 - 每带有1层本效果，使自身... |
| `DimensionRift` | **次元裂痕** | LLC 基准 (BattleKeywords.json) | 回合结束时，施加与本效果层数相同的破裂 层数，随后移除本效果。 |
| `DimensionalBagEzraA` | **次元包-阿拉斯工坊** | LLC 基准 (BattleKeywords-a1c9p3.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：阿拉斯工坊手套 - 下件工坊武器：涅斯托尔工坊锤子 |
| `DimensionalBagEzraB` | **次元包-涅斯托尔工坊** | LLC 基准 (BattleKeywords-a1c9p3.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：涅斯托尔工坊锤子 - 下件工坊武器：螺丝工作室钻锤 |
| `DimensionalBagEzraC` | **次元包-螺丝工作室** | LLC 基准 (BattleKeywords-a1c9p3.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：螺丝工作室钻锤 - 下件工坊武器：纳米尔工坊手铠 |
| `DimensionalBagEzraD` | **次元包-纳米尔工坊** | LLC 基准 (BattleKeywords-a1c9p3.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：纳米尔工坊手铠 - 下件工坊武器：阿拉斯工坊手套 |
| `DimensionalBagEzraDTwo` | **次元包-纳米尔工坊** | LLC 基准 (BattleKeywords-exme.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：纳米尔工坊手铠 - 下件工坊武器：尤里亚工坊斧 |
| `DimensionalBagEzraE` | **次元包-尤里亚工坊** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 当前工坊武器：尤里亚工坊手工特制金毛寻回犬专用斧 |
| `DimensionalBagEzraETwo` | **次元包-尤里亚工坊** | LLC 基准 (BattleKeywords-exme.json) | 从次元包里取出下一件工坊武器 - 当前工坊武器：尤里亚工坊斧 - 下件工坊武器：阿拉斯工坊手套 |
| `Disarming` | **破绽** | LLC 基准 (BattleKeywords.json) | 一回合内守备技能的最终威力降低等同于本效果层数的数值。 |
| `Discard` | **丢弃** | LLC 基准 (BattleKeywords.json) | - 连接技能时，将可选技能中符合条件的技能从仪表盘上丢弃。(不包括守备技能，E.G.O技能。被丢弃的... |
| `DisengageCombat` | **脱离战斗** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合结束时，解除自身的混乱并从战斗中撤退(不包括强制混乱，不视作阵亡) |
| `DistortedDongrangEarnestAchievement` | **恳切的成就** | LLC 基准 (BattleKeywords.json) | 若该单位的体力变为1或是被击杀，使攻击者获得强化 |
| `DistortedDongrangEmptiness` | **空虚** | LLC 基准 (BattleKeywords.json) | 层数高于4时，东朗陷入混乱 |
| `DistortedDongrangEmptyHonor` | **空虚的荣誉** | LLC 基准 (BattleKeywords.json) | 东朗击杀该单位时，失去体力并施加1层空虚 。下回合被弱化 |
| `DistortedDongrangEmptyMark` | **空虚的标记** | LLC 基准 (BattleKeywords.json) | 成为东朗的攻击目标。每回合开始时，对自身施加2层束缚 ，受到东朗造成的伤害+50% |
| `DistortedDongrangFruition` | **成熟的果实** | LLC 基准 (BattleKeywords.json) | 使击杀该单位的目标恢复体力并在下回合使其获得1层迅捷 与1层强壮 |
| `DistortedDongrangMomentaryGlory` | **刹那的荣光** | LLC 基准 (BattleKeywords.json) | 层数高于3时，东朗获得强化 |
| `DistortedDongrangRadiantVanity` | **耀眼的虚荣** | LLC 基准 (BattleKeywords.json) | 回合开始时，使东朗获得1层守护 与1层强壮 。 |
| `DogThunder` | **雷电** | LLC 基准 (BattleKeywords.json) | 积蓄到特定层数后将进入强化状态。 |
| `DongbaekFascination` | **恍惚的意识** | LLC 基准 (BattleKeywords.json) | 本回合指定友方单位作为攻击目标 陷入混乱时，下回合解除本效果 若本效果在2回合内没有解除，则在回合结... |
| `DongbaekFlorescence` | **开花** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果层数不低于5层，则使自身受到体力上限(本效果层数)%的怠惰伤害，并进入盛放 状态... |
| `DongbaekFullBloom` | **盛放** | LLC 基准 (BattleKeywords.json) | 无法行动 回合结束时，使自身失去20点理智值。若理智值降至-45点，则使自身理智值恢复至最大值，并在... |
| `DongbaekFullBloomDisplay` | **盛放** | LLC 基准 (BattleKeywords.json) | 无法行动 回合结束时，使自身失去20点理智值。若理智值降至-45点，则使自身理智值恢复至最大值，并在... |
| `DongbaekGrow` | **生长** | LLC 基准 (BattleKeywords.json) | 回合结束时，本效果的层数+1，并根据其数值增加体力上限。(最多3层) |
| `DongbaekScatterPetal` | **落英缤纷** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果的层数不低于6层，则陷入混乱 |
| `DongbaekShowdown` | **对决** | LLC 基准 (BattleKeywords.json) | 回合开始时，使未带有本效果的单位进入盛放 状态 若李箱带有本效果，则使冬柏获得1层强壮 |
| `DragonLance` | **葬花楔** | LLC 基准 (BattleKeywords.json) | 基础值：0 最大值：3 - 使仪表盘上自身位于最左侧的基础攻击技能的所有硬币转化为不可摧毁的硬币  ... |
| `DragonLanceRefraction` | **葬花楔** | LLC 基准 (BattleKeywords_Refraction6.json) | - 最大值：3 - 强化应龙的特定技能 |
| `Dreamy` | **如在梦中的犹豫** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 基础攻击等级-35 - 基础防御等级-35 |
| `DriftingDimensionYisang` | **次元漂流** | LLC 基准 (BattleKeywords.json) | 最大值：3 受到攻击前，使自身获得自身体力上限(本效果层数)%的护盾(每回合最多3次) |
| `DrunkAwakening` | **觉醒** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：1 - 自身带有本效果时，使自身的最终威力+4，受到的伤害+30% - 增加流血 强度的... |
| `DrunkBlood` | **血注** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：5 - 特殊流血 - 掷出攻击技能硬币时，受到数值等同于本效果层数的固定伤害。 |
| `DrunkDrifter_LowMorale` | **醉手夜客** | LLC 基准 (BattleKeywords-cultivation.json) | - 士气低落 - 自身受到来自贾惜春的伤害+10%，反击技能造成的伤害+30% |
| `DrunkDrifter_Panic` | **醉手夜客** | LLC 基准 (BattleKeywords-cultivation.json) | - 陷入恐慌 - 自身的最终威力+1，受到来自贾惜春的伤害+20%，反击技能造成的伤害+50% |
| `DuelDeclaration` | **决斗宣告** | LLC 基准 (BattleKeywords.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1，并在攻击命中时，下回合... |
| `DuelDeclarationMeursault` | **决斗宣告-默尔索** | LLC 基准 (BattleKeywords-a1c7p1.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1 攻击命中时，下回合使自... |
| `DuelDeclaration_Camille` | **决斗宣告-卡米尔** | LLC 基准 (BattleKeywords-a1c7p1.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1 攻击命中时，下回合使自... |
| `DuelDeclaration_DonQuixote` | **决斗宣告-堂吉诃德** | LLC 基准 (BattleKeywords.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1，并在攻击命中时，下回合... |
| `DuelDeclaration_Outis` | **决斗宣告-奥提斯** | LLC 基准 (BattleKeywords.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1，并在攻击命中时，下回合... |
| `DuelDeclaration_Sinclair` | **决斗宣告-辛克莱** | LLC 基准 (BattleKeywords.json) | 施加决斗宣告 的单位与带有该状态的单位拼点时，使施加该状态的单位拼点威力+1，并在攻击命中时，下回合... |
| `DuelEdge` | **决斗高潮** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：20 - “拇指 子辈 - 卢西奥”与带有本效果的单位拼点时，“拇指 子辈 - 卢西奥”... |
| `DuelEdgeAlly` | **决斗高潮** | LLC 基准 (BattleKeywords.json) | - 影响蜘蛛巢 拇指 子辈 希斯克利夫的技能与被动效果 - 每回合最多获得3层本效果 - 最大值：5 |
| `DuelSousTemoinsEast` | **见证-东部Cinq协会** | 工作区 (BattleKeywords.json) | - 最大值：3 - 攻击等级+(数值) - 数值达到2以上时，基础技能的呼吸法 强度获得量+1 - ... |
| `Duello_LowMorale` | **决斗担当** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 士气低落 - 回合开始时，使自身获得2层攻击等级提升 。拼点失败时，对自身施加1层防御等级降低 ... |
| `Duello_Panic` | **决斗担当** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 陷入恐慌 - 回合开始时，使自身获得4层攻击等级提升 。拼点失败时，对自身施加2层防御等级降低 ... |
| `Duress` | **拘束** | LLC 基准 (BattleKeywords.json) | 使自身在3回合内陷入混乱，撤退机制不会生效。 若Kqe-1j-23陷入混乱，则解除本效果。 |
| `EagleClawWound` | **被撕裂的色彩[蓝色]** | LLC 基准 (BattleKeywords-twth.json) | - 最大值：9 - 受到攻击时，每带有3层本效果，使自身增加1级沉沦 强度(每回合最多1次) - 回... |
| `EagleClawWoundAlly` | **被撕裂的色彩[蓝色]** | LLC 基准 (BattleKeywords.json) | - 最大值：9 - 受到攻击时，每带有3层本效果，使自身增加1级沉沦 强度(每回合最多1次) - 回... |
| `EarlyBuffet_LowMorale` | **分裂** | LLC 2026092102／本地格式化 | - 士气低落 - 防御等级-3 - 攻击等级+3 - 与带有的洗礼（赤红） 层数为5层的目标进行拼点时，使自身的拼点威力+2 |
| `EarlyBuffet_Panic` | **分裂** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 防御等级-5 - 攻击等级+3 - 造成的伤害+10% - 与带有的洗礼（赤红） 层数不低于3层的目标进行拼点时，使自身的拼点威力+…… |
| `EatingSin` | **罪孽缠身** | LLC 基准 (BattleKeywords_Refraction2.json) | 体力上限增加(被减少的E.G.O资源数量)%。  阵亡时 -归还被减少的E.G.O资源。 -被连接的... |
| `EchoOfMansion` | **山庄的回响** | LLC 基准 (BattleKeywords.json) | - 因技能或硬币效果使自身增加沉沦强度或对自身施加沉沦层数时，以50%的概率对自身施加1层沉沦 - ... |
| `EchoOfMansion_Main` | **山庄的回响** | LLC 基准 (Bufs.json) | - 因技能或硬币效果使自身增加沉沦 强度或对自身施加沉沦 层数时，以50%的概率对自身施加1层沉沦 ... |
| `EchoOfMansion_Sub` | **山庄的回响** | LLC 基准 (Bufs.json) | - 因技能或硬币效果使自身增加沉沦 强度或对自身施加沉沦 层数时，以50%的概率对自身施加1层沉沦 ... |
| `EgoAwakenDongrangOverHeal` | **过量恢复** | LLC 基准 (BattleKeywords.json) | 根据东朗令目标恢复的体力，相应增加层数。若本效果的层数不低于50层，则根据层数造成相应的暴食伤害，下... |
| `EgoAwakenDongrangRadiantDesire` | **耀眼的欲望** | LLC 基准 (BattleKeywords.json) | 回合开始时，使东朗获得1层伤害强化 与1层守护 |
| `EgoAwakenDongrangSeed` | **种子** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果层数不低于5层，则下两回合进入吸收养分 状态。若本效果层数低于5层，则使本效果的... |
| `EgoAwakenDongrangShardOfBrokenConnection` | **破碎纽带的残片** | LLC 基准 (Bufs.json) | 李箱的技能最终威力+2 友方单位被击杀时，下回合使剩余友方单位获得1层迅捷 与1层强壮 (每回合最多... |
| `EgoAwakenDongrangTree` | **吸收养分** | LLC 基准 (BattleKeywords.json) | 每回合结束时，使东朗恢复10点体力 |
| `EgoAwakenDongrangTreeDisplay` | **吸收养分** | LLC 基准 (BattleKeywords.json) | 每回合结束时，使东朗恢复10点体力 |
| `EgoErode` | **E.G.O侵蚀** | LLC 基准 (Bufs.json) | 本回合内失去控制，仅能使用E.G.O侵蚀技能。 |
| `EgoErodeContempt_LowMorale` | **脆金所铸之心** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 回合开始时，使自身获得1层强壮 并对自身施加1层易损 |
| `EgoErodeContempt_Panic` | **脆金所铸之心** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 回合开始时，使自身获得2层强壮 并对自身施加2层易损 |
| `EgoErodeMemory_LowMorale` | **迈向新时代的心** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 攻击命中时，消耗自身的3点理智值并使目标增加2级沉沦 强度 |
| `EgoErodeMemory_Panic` | **迈向新时代的心** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 攻击命中时，使目标增加3级沉沦 强度并使自身增加1级沉沦 强度 |
| `EgoErodeReplica` | **E.G.O侵蚀-N公司** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：10 - 每回合开始时触发以下效果 · 使自身失去相当于本效果层数的理智值 · 自身每带... |
| `ElectricShock` | **感电** | LLC 基准 (BattleKeywords.json) | 一回合内受到攻击时额外受到数值等同于本效果层数的固定伤害。 |
| `ElectricStorage` | **蓄能** | LLC 基准 (BattleKeywords.json) | 其身体似乎正在积蓄电流。 |
| `EmergencyChargeForceField` | **应急力场电池** | LLC 基准 (BattleKeywords.json) | - 最大值：7 - 自身陷入混乱时，消耗所有应急力场电池 并使自身获得相当于消耗量的充能力场 |
| `EmergencyFeed` | **应急营养源** | LLC 基准 (BattleKeywords.json) | 回合结束时，若该单位的总恢复量不低于自身体力的15%，则下回合使躯干部位恢复。 |
| `Emergency_Operation` | **紧急手术** | LLC 基准 (BattleKeywords.json) | 每层使体力上限增加25%，技能威力+1。 本效果的层数每回合增加1层。 层数达到5层时，角色直接阵亡... |
| `EmittedCurrent` | **电流释放** | LLC 基准 (BattleKeywords.json) | 受到攻击时，攻击者获得1层充能 ；受到忧郁属性技能攻击时，对自身施加1层破裂 ，随后本效果的层数减少... |
| `Emptiness` | **只余灰烬** | LLC 基准 (BattleKeywords-walpu4.json) | - 无法保留赤瞳 与忏悔  - 通过基础技能效果获得赤瞳 时，使自身与现存体力比例最低的1名友方单位... |
| `Endurance` | **忍耐** | LLC 基准 (BattleKeywords.json) | 一回合内守备技能的最终威力增加等同于本效果层数的数值。 |
| `EngageToBattle` | **临战准备** | LLC 基准 (BattleKeywords.json) | 最大值：1 使自身通过技能或硬币效果使目标增加的流血 强度或对目标施加的流血 层数额外+1 本场战斗... |
| `EnhanceRose` | **强化状态** | LLC 基准 (BattleKeywords_Refraction2.json) | 将会发动强化状态的被动效果 |
| `EnhanceRoseSign` | **枷锁** | LLC 基准 (BattleKeywords_Mirror7.json) | - 使全体友方单位的体力上限增加((当前阶层-4)×10)%(最多60%) - 全体友方单位的攻击等... |
| `EnhanceZilu` | **天究星刀** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 本效果层数不低于10层时，回合结束时使自身在下回合获得1层迅捷  - 用于特定... |
| `Enhancement` | **强壮** | LLC 基准 (BattleKeywords.json) | 一回合内攻击技能的最终威力增加等同于本效果层数的数值。 |
| `Enrage` | **狂暴** | LLC 基准 (BattleKeywords.json) | 本回合内获得3层强壮 并施加3层易损 ，随后改变自身的行动。受到攻击时不再获得本能 层数。 |
| `EntangledCurseTalisman` | **纠缠不休的咒符** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 回合结束时解除 -  若本效果层数不低于10层，则自身受到不低于30点来自技能... |
| `EquitableDistribution` | **共同分担时间支出** | LLC 基准 (BattleKeywords-tkt.json) | 消耗共享的时间 时，所有的脑消耗相等的时间。 |
| `ErodingMind` | **渐被侵蚀的心灵** | LLC 基准 (BattleKeywords.json) | 回合开始时，对自身施加2层虚弱 ，2层易损 ，5层束缚 。 |
| `EsteemNeeds` | **认可欲** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 本效果层数每有1层，使自身对良秀造成的伤害与受到来自良秀的伤害+5% (最多+100%) - 本... |
| `EvilHeart_LowMorale` | **邪心** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+2 回合开始时，使自身获得2层伤害... |
| `EvilHeart_Panic` | **邪心** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 与带有不祥符咒 的目标进行拼点时，使自身的拼点威力+3 回合开始时，使自身获得3层伤害... |
| `EvolvingManual` | **逐渐完备的教材** | LLC 基准 (BattleKeywords.json) | - 使自身基础技能造成的伤害+(10+(本效果层数×5))% - 每回合最多获得2层本效果 - 最大... |
| `Exalted` | **昂扬** | LLC 基准 (BattleKeywords.json) | 每回合获得与本效果层数相同的伤害强化 。(最多5层) 带有醉意 时本效果不会生效。 |
| `ExaminationOfQiu` | **一丝期待** | LLC 基准 (BattleKeywords-a1c8p2.json) | 他没有全力战斗。 - 基础攻击等级减少35级，基础防御等级减少35级 - 对目标进行单方面攻击时造成... |
| `ExpensiveJade` | **宝玉摇篮** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 处于无法行动状态，自身的状态效果、体力与理智值不会改变，生成与自身相连的宝玉 |
| `ExternalUpgradeModule` | **小帮手-外置强力升级** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 获得本效果的3回合内，回合开始时使自身获得2层威力提升 与2层伤害强化 (解除待命的人格从解除待... |
| `ExtractCoin` | **截除硬币** | LLC 基准 (BattleKeywords.json) | - 进行拼点时，可摧毁不可摧毁的硬币。 - 此类硬币不会因为拼点失败而被摧毁。 - 若攻击技能带有此... |
| `EzraMiddle_LowMorale` | **自我防御-面具** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 对自身施加1层虚弱  - 使自身获得2层防御等级提升 |
| `EzraMiddle_Panic` | **自我防御-面具** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 对自身施加1层虚弱  - 使自身获得3层防御等级提升 |
| `FailedToAssistQueen` | **我…已无用处了…吗？** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：1 - 使自身减少3级攻击等级 - 使自身减少3级防御等级 |
| `FaintMemory` | **模糊的记忆** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 基础值：10 - 回合开始时，根据本效果的层数使自身获得相应层数的防御等级提升  - 拼点失败时... |
| `FairyCharm` | **魅惑** | LLC 基准 (BattleKeywords_Refraction2.json) | - 对精灵造成的伤害固定为0。 - 精灵阵亡时解除该状态。 |
| `FamilyTreasure` | **爆发游戏** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合结束时 · 基础值：1 · 与自身相连的单位恢复其体力上限25%的体力并失去20点理智值 ·... |
| `FamineBloodDolci_LowMorale` | **虚无的枷锁** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 士气低落 - 回合开始时，使自身获得1层强壮 并对自身施加3层防御等级降低  - 回合结束时，失... |
| `FamineBloodDolci_Panic` | **虚无的枷锁** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 陷入恐慌 - 回合开始时，使自身获得2层强壮 并对自身施加6层防御等级降低  - 回合结束时，恢... |
| `FamineBloodPriestServant_LowMorale` | **饥饿** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 士气低落 - 回合开始时，使自身获得1层拼点威力提升 并对自身施加3层防御等级降低  - 回合结... |
| `FamineBloodPriestServant_Panic` | **饥饿** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 陷入恐慌 - 回合开始时，使自身获得2层拼点威力提升 并对自身施加6层防御等级降低  - 回合结... |
| `FamineBlood_LowMorale` | **饥饿** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 士气低落 回合开始时，对自身施加1层束缚 并使自身获得2层强壮 。 |
| `FamineBlood_Panic` | **饥饿** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 陷入恐慌 回合开始时，对自身施加2层束缚 并使自身获得4层强壮 。 |
| `FasciaPersonality` | **作品名：法西娅** | LLC 基准 (BattleKeywords.json) | 根据自身的活体材料 强度，相应使自身的基础攻击技能与可拼点反击技能获得以下效果 - 不低于1级：基础... |
| `FaubismMaskMeursault` | **野兽派-犬面** | LLC 基准 (BattleKeywords.json) | - 目标每带有3层被撕裂的色彩，使自身造成的伤害+5%(最多+15%) - 令自身基础技能增加的流血... |
| `FaubismWolfMask` | **野兽派-狼面** | LLC 基准 (BattleKeywords-twth.json) | - 最小与最大速度值+1 - 令自身基础技能增加的流血 强度与沉沦 强度额外+1级 - 攻击前，若目... |
| `FaubismWolfMaskBlooded` | **野兽派-染血狼面** | LLC 基准 (BattleKeywords-twth.json) | - 造成的伤害+20%；所有硬币转化为不可摧毁的硬币 - 最小与最大速度值+1 - 令自身技能施加的... |
| `FaubismWolfMaskRodion` | **野兽派-狼面** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+1 - 令自身基础技能增加的流血 强度与沉沦 强度额外+1级 - 攻击命中时，... |
| `FaustFlameMothEmber` | **余火** | LLC 基准 (BattleKeywords.json) | - 最大强度：3 - 最大层数：6 - 若自身带有烧伤 ，则受到增加烧伤 强度，施加烧伤 层数，或施... |
| `FauvismDocent_Lowmorale` | **冲动的着色** | LLC 基准 (BattleKeywords-twth.json) | - 士气低落 - 自身攻击的目标每带有1种负面状态，使自身造成的伤害+2.5%(最多+15%) - ... |
| `FauvismDocent_Panic` | **冲动的着色** | LLC 基准 (BattleKeywords-twth.json) | - 陷入恐慌 - 自身攻击的目标每带有1种负面状态，使自身造成的伤害+5%(最多+30%) - 对自... |
| `Fauvism_Lowmorale` | **衰退的灵感** | LLC 基准 (BattleKeywords-twth.json) | - 士气低落 - 若自身攻击的目标带有被撕裂的色彩，则使自身造成的伤害+10% - 对自身施加1层易... |
| `Fauvism_Panic` | **衰退的灵感** | LLC 基准 (BattleKeywords-twth.json) | - 陷入恐慌 - 若自身攻击的目标带有被撕裂的色彩，则使自身造成的伤害+20% - 对自身施加2层易... |
| `FavorBuff5001AllyFirst` | **映射[中指]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 关卡开始时，若登场的<color=#f8c200>属于中指</color>的人格不低于4名，则获... |
| `FavorBuff5001AllyTwo` | **映射[突袭]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加<color=#f8c200>破裂 或特殊破裂</color>的攻击技能或<color=... |
| `FavorBuff5001EnemyFirst` | **映射[中指]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 关卡开始时，若登场的<color=#f8c200>属于中指</color>的人格不低于4名，则<... |
| `FavorBuff5001EnemySecond` | **映射[突袭]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 里卡多<color=#f8c200>陷入混乱</color>时，若攻击者的速度值高于里卡多，则使... |
| `FavorBuff5001FirstPhaseForUI` | **映射[中指]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 关卡开始时，若登场的<color=#f8c200>属于中指</color>的人格不低于4名，则<... |
| `FavorBuff5001Hard` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+25% - 技能造成的伤害+20% |
| `FavorBuff5001HardForUI` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+25% - 技能造成的伤害+20% - ... |
| `FavorBuff5001HardTwo` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+25% - 技能造成的伤害+20% - ... |
| `FavorBuff5001SecondPhaseForUI` | **映射[突袭]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加<color=#f8c200>破裂 或特殊破裂</color>的攻击技能或<color=... |
| `FavorBuff5012AllyOne` | **映射[狩熊]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加烧伤 或特殊烧伤的攻击技能或暴怒攻击技能造成的伤害+25%(若是E.G.O技能，则改为造... |
| `FavorBuff5012AllyOneForUI` | **映射[狩熊]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格<color=#f8c200>施加烧伤 或特殊烧伤的攻击技能或暴怒攻击技能</color>造... |
| `FavorBuff5012AllyTwo` | **映射[狩虎]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格增加呼吸法 强度，获得呼吸法 层数或消耗呼吸法的攻击技能或傲慢攻击技能造成的伤害+25%(若... |
| `FavorBuff5012AllyTwoForUI` | **映射[狩虎]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格<color=#f8c200>增加呼吸法 强度，获得呼吸法 层数或消耗呼吸法的攻击技能或傲慢... |
| `FavorBuff5012EnemyOne` | **映射[狩熊]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 护盾受到的烧伤 与特殊烧伤的伤害+50%(向下取整) |
| `FavorBuff5012HardOne` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - 体力上限+25% - 自身的理智值不会低于0点 - [林庆业专属] 使用“本国剑[肉]-重整态势... |
| `FavorBuff5012HardTwo` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - 体力上限+25% - 自身的理智值不会低于0点 - [林庆业专属] 使用“本国剑[肉]-重整态势... |
| `FavorBuff5012HardTwoForUI` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+25% - 自身的理智值不会低于0点 -... |
| `FavorBuffLeiheng` | **映射 [插翅虎]** | 工作区 (BattleKeywords-BossRaid.json) | - 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基... |
| `FavorBuffLeiheng1stPhaseForUI` | **映射 [插翅虎]** | 工作区 (BattleKeywords-BossRaid.json) | - 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基... |
| `FavorBuffLeiheng2ndPhaseForUI` | **映射 [天退星]** | 工作区 (BattleKeywords-BossRaid.json) | - 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基... |
| `FavorBuffLeihengHard` | **苦难** | 工作区 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+80% - 理智值不会降低至0以下 - ... |
| `FavorBuffLeihengHardForUI` | **苦难** | 工作区 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+80% - 理智值不会降低至0以下 - ... |
| `FavorBuffLeihengHardTwo` | **苦难** | 工作区 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+80% - 理智值不会降低至0以下 - ... |
| `FavorBuffLeihengTwo` | **映射 [天退星]** | 工作区 (BattleKeywords-BossRaid.json) | - 参与战斗的所有人格<color=#f8c200>消除一条混乱线</color>。基础攻击等级、基... |
| `FavorBuffTwth` | **映射[红色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加流血 或特殊流血的攻击技能或色欲攻击技能造成的伤害+25%(若是E.G.O技能，则改为造... |
| `FavorBuffTwth1stPhaseForUI` | **映射[红色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加<color=#f8c200>流血 或特殊流血</color>的攻击技能或<color=... |
| `FavorBuffTwth2ndPhaseForUI` | **映射[蓝色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加<color=#f8c200>沉沦 或特殊沉沦</color>的攻击技能或<color=... |
| `FavorBuffTwthEnemy` | **映射[红色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 受到的流血 伤害变为1.5倍(向下取整) |
| `FavorBuffTwthEnemyTwo` | **映射[蓝色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 回合开始时，若自身陷入恐慌，则对自身施加3层易损 |
| `FavorBuffTwthHard` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - 体力上限+25% - 技能增加的流血 强度与沉沦 强度，施加的被撕裂的色彩[红色] 与被撕裂的色... |
| `FavorBuffTwthHardForUI` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - <color=#ff0000>体力上限</color>+25% - 技能<color=#ff00... |
| `FavorBuffTwthHardTwo` | **苦难** | LLC 基准 (BattleKeywords-BossRaid.json) | - 体力上限+25% - 技能增加的流血 强度与沉沦 强度，施加的被撕裂的色彩[红色] 与被撕裂的色... |
| `FavorBuffTwthTwo` | **映射[蓝色]** | LLC 基准 (BattleKeywords-BossRaid.json) | - 人格施加沉沦 或特殊沉沦的攻击技能或忧郁攻击技能造成的伤害+25%(若是E.G.O技能，则改为造... |
| `FellBulletGroggy` | **标记** | LLC 基准 (BattleKeywords_Refraction5.json) | - 无法解除 - 回合结束时，若本效果层数为0层，则下回合使自身陷入混乱 - 使用技能指定目标射击时... |
| `FellBulletMark` | **标记** | LLC 基准 (BattleKeywords_Refraction5.json) | - 成为凶弹射手的目标 - 回合结束时解除本效果 |
| `FellBulletMarkReplica` | **标记** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 成为仇甫的目标 - 回合结束时解除本效果 |
| `FellBulletPersonality` | **凶弹** | LLC 基准 (BattleKeywords.json) | 最大值：1 自身每带有1层撕裂的回忆 ，使自身暴击时造成的伤害+3%(最多+18%) 命中时，使目标... |
| `FerrisWheel` | **不停旋转的摩天轮** | LLC 基准 (BattleKeywords-a1c7p3.json) | 每有1个座舱被击杀，使本效果的层数减少1层。 若本效果的层数为0，且下回合没有单位生成，则进入下一阶... |
| `FestivalFever` | **庆典的热潮** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 最大值：10 - 回合开始时，每带有3层本效果，使自身获得1层攻击等级提升 (最多3层) - 用... |
| `FestivalFeverRodion` | **庆典的热潮** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 回合结束时，解除本效果 - 每带有1层本效果，对带有流血 的目标造成的伤害+1... |
| `FireBulletPropellant` | **灼热推进弹** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 最大值：15 - 特定技能使用时消耗 |
| `FireField` | **灼热地带** | LLC 基准 (BattleKeywords.json) | - 最大值：999 - 储存在该战斗场所造成的烧伤 伤害 - 改变战斗场所时重置本效果 - 全体单位... |
| `FirePunchFuel` | **12区燃料** | LLC 基准 (BattleKeywords.json) | 最大值：100 特定技能使用时消耗燃料 若本效果层数不高于50层，则转化为过热燃料 |
| `FirePunchFuelOverheated` | **过热燃料** | LLC 基准 (BattleKeywords.json) | 最大值：100 处于过热燃料 状态时，消耗12区燃料 改为消耗过热燃料  消耗过热燃料 也视作消耗1... |
| `FirmWill` | **坚定的意志** | LLC 基准 (BattleKeywords_Refraction4.json) | 友方单位阵亡时，理智值不会减少。 |
| `Firstlight` | **战斗直觉** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 最小与最大速度值+2 - 基础技能使敌方单位增加的烧伤 强度与对敌方单位施加的烧... |
| `FocusOnActing` | **专注表演** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 属于<拉·曼却领>的人格专属，包括强化技能 - 使自身1技能与2技能的最终威力+... |
| `ForwardToTheBoundKing` | **缚王御前** | LLC 基准 (BattleKeywords.json) | 攻击容量为1的自身攻击命中时，对除自身攻击目标外现存体力最低的2名敌方单位造成硬币结果值100%且与... |
| `ForwardToTheKing` | **御前** | LLC 基准 (BattleKeywords.json) | 攻击容量为1的自身攻击命中时，对除自身攻击目标外现存体力最低的2名敌方单位造成硬币结果值50%且与本... |
| `FourDimensionYisang` | **四色次元** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 根据本效果层数，相应使自身获得以下效果 · 不低于1层：攻击等级+1 · 不低于... |
| `Fragile_Mind_LowMorale` | **岌岌可危的心灵** | LLC 基准 (BattleKeywords.json) | 回合开始时，使自身获得2层强壮 ，3层束缚 。 |
| `Fragile_Mind_Panic` | **混乱不安的心灵** | LLC 基准 (BattleKeywords.json) | 若自身陷入恐慌则使自身陷入混乱。 |
| `FragmentOfHope` | **与同伴们在巴士上一同经历了诸多冒险，** | LLC 基准 (BattleKeywords-a1c7p3.json) | 根据本效果的层数获得相应层数的拼点威力提升 |
| `FragmentOfHopeFamilyMirror` | **我孩子的同伴们啊** | LLC 基准 (BattleKeywords_Mirror6.json) | 每层本效果使自身的拼点威力+1(最多+4) 使自身造成的伤害+5% |
| `FragmentOfHopeSancho` | **为了饱受痛苦的家人们设下血之晚宴，** | LLC 基准 (BattleKeywords-a1c7p1.json) | 根据本效果的层数获得相应层数的拼点威力提升  造成的伤害+10% |
| `FragmentOfHopeTwo` | **梦永不迎来终焉的桑丘，也是我们的堂吉诃德的故事** | LLC 基准 (BattleKeywords-a1c7p3.json) | 每层本效果使自身拼点威力+4 战斗开始时，使自身与所有友方单位获得护盾 |
| `FragmentOfHopeTwoFamilyMirror` | **代替我，与那孩子一同追寻梦想吧** | LLC 基准 (BattleKeywords_Mirror6.json) | - 每层本效果使自身拼点威力+2(最多+8) - 战斗开始时，使自身与所有友方单位获得护盾 - 命中... |
| `FragmentOfHopeTwoSancho` | **处决了背弃孩子的父亲，背负起所有罪恶感的那位血魔的故事** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 每层本效果使自身拼点威力+4 - 战斗开始时，使自身与所有友方单位获得护盾 - 造成的伤害+20... |
| `FreezingDOQ` | **冻结** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 特殊寒冷 - 本回合无法行动 - 体力为1点时，特定技能无法生效 |
| `FreischutzShotCount` | **魔弹** | LLC 基准 (BattleKeywords.json) | - 最大值：7 - 本效果的层数受到特定技能效果的影响。 -[脑叶公司E.G.O::魔弹 奥提斯 人... |
| `FreishutzOutisEgoBulletCnt` | **射手的弹药** | LLC 基准 (BattleKeywords.json) | 根据自身射手的弹药决定发射的弹药 |
| `FreishutzOutisEgoBullet_1st` | **第一发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+20% - 使目标的混乱阈值前移造成伤害量的数值(最多30) |
| `FreishutzOutisEgoBullet_2nd` | **第二发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+10% - 仅对除主要目标以外的目标造成伤害(目标数：最多4名)，对主要目标造成的伤... |
| `FreishutzOutisEgoBullet_3rd` | **第三发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+20% - 攻击前，攻击容量+2 - 命中时，对目标施加2层虚弱 并使其增加10级烧... |
| `FreishutzOutisEgoBullet_4th` | **第四发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+30% - 攻击前，攻击容量+3 - 命中时，使目标的混乱阈值前移造成伤害量的数值(... |
| `FreishutzOutisEgoBullet_5th` | **第五发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+30% - 攻击前，攻击容量+4 - 命中时，使目标增加10级烧伤 强度，并在下回合... |
| `FreishutzOutisEgoBullet_6th` | **第六发魔弹** | LLC 基准 (BattleKeywords.json) | - 攻击前，攻击容量+6 - 命中时，使目标的混乱阈值前移造成伤害量的数值(最多30) - 主要目标... |
| `FreishutzOutisEgoBullet_7th` | **第七发魔弹** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+200% - 目标每失去1%体力，使造成的伤害+2.5%(最多+200%) - 攻击... |
| `Fugacious` | **剑道** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时， · 本效果层数每有5层，使自身获得1层攻击等级提升 并对自身施加1层防御等级降低 ... |
| `FullBloomRose` | **绽放的玫瑰** | LLC 基准 (Bufs_Refraction2.json) |  |
| `FullBloomRose_Amber` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以怠惰属性技能造成/受到的伤害增加 |
| `FullBloomRose_Azure` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以忧郁属性技能造成/受到的伤害增加 |
| `FullBloomRose_Crimson` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以暴怒属性技能造成/受到的伤害增加 |
| `FullBloomRose_Indigo` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以傲慢属性技能造成/受到的伤害增加 |
| `FullBloomRose_Scarlet` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以色欲属性技能造成/受到的伤害增加 |
| `FullBloomRose_Shamrock` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以暴食属性技能造成/受到的伤害增加 |
| `FullBloomRose_Violet` | **绽放的玫瑰** | LLC 基准 (BattleKeywords_Refraction2.json) | 人格以嫉妒属性技能造成/受到的伤害增加 |
| `FullCharon` | **饱腹感** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合开始时，每带有2层本效果，对自身施加1层拼点威力降低 (最多5层) |
| `FullReload` | **再次装填** | LLC 基准 (BattleKeywords.json) | 消耗自身带有的所有弹药，并再次装填至最大值 |
| `FusionVibration` | **振幅纠缠** | LLC 基准 (BattleKeywords-tkt.json) | - 使纠缠的震颤效果与目标带有的震颤种类结合为震颤-叠加 。 - 纠缠时，现有震颤 的强度与层数保持... |
| `FutureEyeOff` | **预知眼 过热** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：30 - 攻击技能造成的伤害-20% - 消耗加速弹的技能的所有硬币转化为不可摧毁的硬币... |
| `FutureEyeOffMirror` | **预知眼 过热** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：30 - 攻击技能造成的伤害-20% - 消耗加速弹的技能的所有硬币转化为不可摧毁的硬币... |
| `FutureEyeOffRodion` | **预知眼 过热** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 攻击等级+3，防御等级-3 - 回合开始时，获得10层本效果 - 若本效果层数... |
| `FutureEyeOn` | **预知眼** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：30 - 拼点威力+2 - 回合开始时，获得10层本效果 - 回合开始时，恢复(本效果层... |
| `FutureEyeOnMirror` | **预知眼** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：30 - 拼点威力+2 - 回合开始时，获得5层本效果 |
| `FutureEyeOnRodion` | **预知眼** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多减少10层本效果 |
| `GahwanEgoContempt` | **不稳定E.G.O感应-轻蔑** | LLC 基准 (BattleKeywords-a1c8p3.json) | - N公司提取的E.G.O装备。虽能力适合，但经验不足，还未能习惯。 - 最大值：5 - 攻击等级与... |
| `GainSinStockAdder` | **E.G.O资源获取量提升** | LLC 基准 (BattleKeywords.json) | 一回合内根据本效果的层数来增加使用技能时获得的E.G.O资源数量。 |
| `GazePersonality` | **轻蔑的视线** | LLC 基准 (BattleKeywords.json) | - 最大值：7 - 每带有1层轻蔑的视线 ，造成的伤害+7% - 回合结束时，解除本效果 - 回合结... |
| `GazeReplica` | **视线** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：7 - 每带有1层本效果，使自身对贾环造成的伤害与受到来自贾环的伤害+10% - 本效果... |
| `GazeRyoshu` | **视线** | LLC 基准 (BattleKeywords.json) | - 最大值：7 - 自身每带有1层视线 ，使自身对良秀造成的伤害与受到来自良秀的伤害+10% - 自... |
| `Gebura_Reinforcement` | **Gebura之刃** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 技能的所有硬币转化为不可摧毁的硬币 - 造成的伤害+100% - 加算硬币技能的硬币威力+1；减... |
| `GhostKimPersonal` | **怨恨** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+2 - 攻击命中时，使自身恢复该技能造成伤害量10%的体力(每个技能的最大体力... |
| `GiftCannon` | **火力** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：10 - 每带有1层本效果，使自身造成的伤害+10% |
| `GiftGlass` | **易碎** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：10 - 每带有1层本效果，使自身受到的伤害+10% |
| `GiveMeCandy` | **糖果** | LLC 基准 (BattleKeywords_Mirror6.json) | 最大值：99 明明带着糖果却不给吗？ |
| `GiveMeCandy_LowMoral` | **糖果** | LLC 基准 (BattleKeywords_Mirror6.json) | - 士气低落 - 与带有[GiveMeCandy]的人格进行拼点时，拼点威力+3；与其他人格进行拼点... |
| `GiveMeCandy_LowMorale` | **糖果** | LLC 基准 (Bufs_Mirror6.json) | - 士气低落 - 与带有糖果 的人格进行拼点时，拼点威力+3；与其他人格进行拼点时，拼点威力-1 |
| `GiveMeCandy_Panic` | **糖果** | LLC 基准 (BattleKeywords_Mirror6.json) | - 陷入恐慌 - 与带有[GiveMeCandy]的人格进行拼点时，拼点威力+5，与其他人格进行拼点... |
| `GlowingLantern` | **诱饵精灵** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 回合开始时，使仪表盘上位于最左侧的行动槽的挑衅值 +10 - 使自身受到的伤害+... |
| `GodokPanicType` | **孤独** | LLC 基准 (BattleKeywords.json) | - 受到来自忧郁技能的伤害+10% - 若目标带有理智值，则使其恐慌类型转变为“孤独” - 若目标未... |
| `GodokPanicType_Main` | **孤独** | LLC 基准 (BattleKeywords.json) | - 受到来自忧郁技能的伤害+10% - 使自身恐慌类型转变为“孤独”  - 回合结束时，本效果层数减... |
| `GodokPanicType_Sub` | **孤独** | LLC 基准 (BattleKeywords.json) | - 受到来自忧郁技能的伤害+10% - 回合结束时对自身施加2层沉沦   - 回合结束时，本效果层数... |
| `Godok_Lowmorale` | **孤独** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 回合结束时，对自身施加2层沉沦 |
| `Godok_Panic` | **孤独** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 回合结束时，对自身施加3层沉沦 |
| `GoldenBoughSync` | **未感应** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 基础攻击等级+2，基础防御等级+2 |
| `GoldenBoughSyncDistorted` | **怪力乱神** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 基础攻击等级+4，基础防御等级+4 |
| `GoldenOpportunity` | **眺望** | LLC 基准 (BattleKeywords.json) | - 若蜘蛛巢 环指 子辈 浮士德在场，则回合开始时使自身获得2层守护  - 回合结束时，本效果的层数... |
| `GotACompliment` | **受到表扬啦！** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 每受到2次技能攻击，使本效果的层数减少1层 - 本效果的层数每有2层，使自身的... |
| `GotAComplimentIshmael` | **受到表扬啦！** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 每受到2次技能攻击，使本效果的层数减少1层 - 若本效果的层数不低于5层，则使... |
| `Gourmandise` | **狂暴** | LLC 2026092102／本地格式化 | - 基础值：3 - 自身每带有3级流血 强度，使自身造成的伤害+5%(最多+30%) - 所有部位不会陷入混乱，受到来自流血 的伤害-75% - 回合…… |
| `GraspReplica` | **掌** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：4 - 回合结束时，下回合对自身施加10层束缚  - 回合结束时本效果的层数减少1层 |
| `GreatAesthetics` | **卓越的美感** | LLC 基准 (BattleKeywords_Mirror7.json) | - 加算硬币技能的硬币威力+1 - 减算硬币技能的基础威力+(4/硬币数) - 技能造成的伤害+30... |
| `Greedy` | **渴望** | LLC 基准 (BattleKeywords.json) | 回合开始时，施加10层束缚 。 物理抗性全部变为“致命”。 攻击技能威力+2。 守备技能威力-2。 |
| `GreedyReady` | **紧缚欲望** | LLC 基准 (Bufs.json) | 在{0}回合后使用会施加渴望 的技能。 |
| `GrownHorns` | **生角** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 令自身基础技能使敌方单位增加的破裂 强度与沉沦 强度额外+1级 - 回合结束时，... |
| `Grudge` | **郁积的怨结** | LLC 基准 (BattleKeywords-ycgd.json) | 带有本效果时，使自身获得与所受伤害相当的层数，回合结束时解除本效果 |
| `GrudgePersonal` | **郁积的怨结** | LLC 基准 (BattleKeywords.json) | - 最大值：999 - “骨断”的最终威力+(本效果层数/100)(最多+6，向下取整) - “肉斩... |
| `GuboEgoShooter` | **不稳定E.G.O感应-凶弹** | LLC 基准 (BattleKeywords-a1c8p3.json) | - N公司提取的E.G.O装备。虽能力适合，但经验不足，还未能习惯。 - 最大值：5 - 攻击等级与... |
| `Guilt_LowMorale` | **负罪感** | LLC 基准 (BattleKeywords-a1c7p3.json) | 回合结束时，下回合对自身施加1层易损 与1层理智值恢复效率减少 |
| `Guilt_Panic` | **负罪感** | LLC 基准 (BattleKeywords-a1c7p3.json) | 回合结束时，下回合对自身施加2层易损 与2层理智值恢复效率减少 |
| `HanafudaCombo` | **光札** | LLC 基准 (BattleKeywords.json) | - 强度：基础值为0，最大值为5 - 层数：基础值为3，最大值为3  - 回合开始时，本效果的强度每... |
| `HanafudaOne` | **组札-松上鹤** | LLC 基准 (BattleKeywords.json) | - 1技能的基础威力+2 - 自身最左侧的行动槽装备并使用<color=#ff0000>暴怒</co... |
| `HanafudaThree` | **组札-青染樱** | LLC 基准 (BattleKeywords.json) | - 3技能的基础威力+1 - 自身最左侧的行动槽装备并使用<color=#15c3ee>忧郁</co... |
| `HanafudaTwo` | **组札-芒上月** | LLC 基准 (BattleKeywords.json) | - 2技能的基础威力+1 - 自身最左侧的行动槽装备并使用<color=#fbc82b>怠惰</co... |
| `HardenedBlood` | **硬化血液** | LLC 基准 (BattleKeywords-mowe.json) | 使自身增加本效果层数级攻击等级与防御等级(最多5级) |
| `Hardening` | **硬化** | LLC 基准 (Bufs.json) | 回合开始时，若本效果的层数不低于3层，则使手臂进入完整状态。 |
| `HeatedGasHarpoon` | **加热的燃气捕鲸叉** | LLC 基准 (BattleKeywords.json) | 1回合内，正面命中时使目标增加1级烧伤 强度 |
| `HeatedWingScales` | **灼热的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的“罗生-回归”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `HeatedWingScalesExplain` | **灼热的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的技能“罗生-回归”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `HeatingWireIshmael` | **热丝** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 若自身基础技能攻击命中的目标带有烧伤 ，则使自身恢复3点理智值(每回合最多2次)... |
| `HeatingWireOffSpider` | **热丝 OFF** | LLC 基准 (BattleKeywords-a1c9p3.json) | 热丝技能的附加效果不会生效 |
| `HeatingWireOnSpider` | **热丝 ON** | LLC 基准 (BattleKeywords-a1c9p3.json) | 热丝技能的硬币命中时，额外增加相当于增加的流血 强度的烧伤 强度，施加层数相当于施加的流血 层数的烧... |
| `HeatingWireOnSpiderTwo` | **热丝 ON** | LLC 基准 (BattleKeywords-twth.json) | 热丝技能的硬币命中时，额外增加相当于增加的流血 强度的烧伤 强度，施加层数相当于施加的流血 层数的烧... |
| `HeavenlyKillerStar` | **天杀星刀-阿赖耶识** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最小与最大速度值+6 - 攻击等级+6 - 技能增加的流血 强度额外+3级 - 回合开始时，本场... |
| `HeishouAttack` | **斩随意动。** | LLC 基准 (BattleKeywords.json) | - 若A单位使B单位获得本效果，则在A单位的攻击技能结束时，B单位使用自身的1技能对相同的敌方单位进... |
| `HeishouCombo` | **遵命** | LLC 基准 (BattleKeywords.json) | - 若A单位使B单位获得本效果，则在A单位的技能结束时，B单位使用自身的基础3技能对相同的敌方单位进... |
| `HeishouComboCount` | **迫近** | LLC 基准 (BattleKeywords.json) | - 与鸿园的君主 鸿璐人格连携的次数 - 最大值：2 - 回合开始时，每带有1层本效果，使自身获得1... |
| `HeishouComboCountHonglu` | **黑兽丸染** | LLC 基准 (BattleKeywords.json) | - 最大值：11 - 根据进行连携的黑兽，使鸿园的君主 鸿璐获得强化 - 强化效果可叠加  · 黑兽... |
| `HeishouDeathCount` | **死中求活** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 回合开始时，触发以下效果 · 每带有1层本效果，使自身获得1层攻击等级提升 (最... |
| `HeishouSupportProtect` | **护卫** | LLC 基准 (BattleKeywords.json) | - 特殊援护防御 - 最大值：1 - 鸿园的君主 鸿璐将受到来自敌方单位的单方面攻击时，消耗1层并使... |
| `HeishouSynergy` | **全体黑兽之主** | LLC 基准 (BattleKeywords.json) | - 最大值：11 - 根据本效果层数，相应获得以下效果： · 每带有1层本效果，使自身的最大速度值+... |
| `HelplessTear` | **无能为力之泪** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：1 - 使自身增加3级攻击等级 - 使自身减少6级防御等级 - 使自身所有技能的攻击容量... |
| `HighVoltageExoshell` | **高压外壳** | LLC 基准 (BattleKeywords.json) | - 获得(本效果层数×5)点护盾 - 若失去(本效果层数×5)点护盾，则使自身消耗1层高压外壳  -... |
| `HitDamageDown` | **打击伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低打击技能造成的伤害。(最多10层) |
| `HitDamageUp` | **打击伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高打击技能造成的伤害。(最多10层) |
| `HitResistDown` | **打击抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的打击抗性增加(每层0.1) |
| `HitResistUp` | **打击抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的打击抗性减少(每层0.1) |
| `HitResultDown` | **打击威力降低** | LLC 基准 (Bufs.json) | 本回合内打击技能的最终威力-{0} |
| `HitResultUp` | **打击威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高打击技能的最终威力。 |
| `HitTakeDamageDown` | **打击守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自打击技能的伤害。(最多10层) |
| `HitTakeDamageUp` | **打击易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自打击技能的伤害。(最多10层) |
| `HohenheimBigBird_LowMorale` | **袭来的睡意** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 通过技能使自身获得的目灯 层数减少1层 |
| `HohenheimBigBird_Panic` | **袭来的睡意** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 一回合内无法行动。 |
| `Hohenheim_LowMorale` | **烦恼** | LLC 基准 (BattleKeywords.json) | 回合开始时，对自身施加1层易损 与2层理智值恢复效率减少 |
| `Hohenheim_Panic` | **烦恼** | LLC 基准 (BattleKeywords.json) | 回合开始时，对自身施加2层易损 与3层理智值恢复效率减少 |
| `HoldingBreath` | **深呼吸** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 暴击时，若自身的呼吸法 强度不低于15级且自身的呼吸法 层数不低于5层，则消耗... |
| `HongluParryGahwan` | **希冀直面的意志** | LLC 基准 (BattleKeywords-a1c8p3.json) | 与贾环进行拼点时，使自身的拼点威力+2 |
| `Honglu_Ai` | **喜、乐、哀** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 鸿璐的最终威力+3 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) - 友... |
| `Honglu_Ai_Mirror` | **喜、乐、哀** | LLC 基准 (Bufs-a1c8p3.json) | - 最终威力+3 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) - 友方单位... |
| `Honglu_EGOResourceup` | **我的本心与想法…** | LLC 基准 (BattleKeywords-a1c8p3.json) | [鸿璐特殊效果] - 本场战斗中，自身的技能攻击结束后，额外获得该技能对应属性的2个E.G.O资源(... |
| `Honglu_Le` | **喜、乐** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 鸿璐的最终威力+1 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) - 本... |
| `Honglu_Le_Mirror` | **喜、乐** | LLC 基准 (Bufs-a1c8p3.json) | - 最终威力+1 - 拼点胜利时，使理智值最低的1名友方单位恢复5点理智值(包括自身) 与贾母拼点胜... |
| `Honglu_Nu` | **喜、乐、哀、怒** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 鸿璐的最终威力+5 - 每回合开始时，使全体友方单位恢复5点理智值(包括自身) - 友方单位阵亡... |
| `Honglu_Nu_Mirror` | **喜、乐、哀、怒** | LLC 基准 (Bufs-a1c8p3.json) | - 最终威力+5 - 每回合开始时，使全体友方单位恢复5点理智值(包括自身) - 友方单位阵亡时，回... |
| `Honglu_Xi` | **喜** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 鸿璐的拼点威力+1 - 本场战斗中，不低于1名其他友方单位存活时，鸿璐受到致死伤害时不会阵亡，改... |
| `Honglu_Xi_Mirror` | **喜** | LLC 基准 (Bufs-a1c8p3.json) | - 拼点威力+1 - 使自身转化为宝玉状态的效果无效1次。与使自身转化为宝玉状态的技能进行拼点时，使... |
| `HonorableDuel_Don` | **光荣的决斗** | LLC 基准 (BattleKeywords-a1c7p2.json) | 回忆中的冒险故事 能力值大幅提升 |
| `HonorableDuel_Knight` | **光荣的决斗** | LLC 基准 (BattleKeywords-a1c7p2.json) | 回忆中的冒险故事 |
| `HornetPoison` | **冈格尼尔的共鸣** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 受到韦斯帕攻击时，受到等同于本效果强度的固定伤害 - 回合结束后，本效果的层数减少1层(本效果适... |
| `HorrHurtNightStiletto` | **致命创伤** | LLC 基准 (BattleKeywords.json) | - 基础值：3 - 震颤引爆时，对自身施加3层流血 (每回合最多2次) - 无法被施加创伤 (集中遭... |
| `HorribleEat` | **重复播放的重复** | LLC 2026092102／本地格式化 | - 最大值：15 - 使自身增加相当于本效果层数的攻击等级 |
| `HorribleTerror` | **可怕的重复播放** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合开始时，若自身处于E.G.O侵蚀状态，则使自身本回合对所有目标造成的伤害-50% - 回合结束时，自身受到现存体力50%的体力…… |
| `HostageCharon` | **人质事件** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 与“拇指 子辈 - 卢西奥”拼点时，拼点威力-1 - 对“拇指 子辈 - 卢西奥”造成的伤害-2... |
| `HousekeepingAssistantModule` | **小帮手-家政辅助模块** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 触发圣徒之手时，下回合额外触发1次 - 回合开始时，获得层数相当于本场战斗中圣徒之手清洗溟痕 次... |
| `HowDareYouApple` | **竟敢…！** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：4 - 每带有1层本效果，使自身造成的伤害+20% - 特定技能使用时消耗 |
| `HowlingCocoon` | **茧的悲鸣-微弱** | LLC 2026092102／本地格式化 | - 偶尔，会听见茧的悲鸣。 - 技能的最终威力+2 |
| `HowlingCocoonTwo` | **茧的悲鸣-恶性** | LLC 2026092102／本地格式化 | - 茧的悲鸣不会停下。 - 技能的最终威力+3 |
| `HugeIrritation` | **心-天退星** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合开始时，自身每失去15%的体力，使自身获得1层伤害强化 与1层威力提升 (分别最多5层) -... |
| `HugeIrritationAlly` | **心-天退星** | LLC 基准 (BattleKeywords.json) | - 使自身的最小与最大速度值+3 - 若自身的速度值高于目标至少3点，则使自身造成的伤害+(速度值之... |
| `HugeIrritationReflectrial` | **心 - 天退星** | 工作区 (BattleKeywords-BossRaid.json) | - 回合开始时，每损失15%体力，自身获得1层伤害量增加与1层威力增加 (各最多5层) - 通过技能... |
| `HumanBloodTheRings` | **活体材料(血)** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：5 - 特殊充能(固定强度) |
| `HumanBoneTheRings` | **活体材料(骨)** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：206 - 特殊充能(固定强度) |
| `HumanFleshTheRings` | **活体材料** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：2 - 特殊充能(固定强度) |
| `Hunger` | **饥饿** | LLC 基准 (BattleKeywords.json) | 回合结束时，若自身未能击杀带有储备粮 的友方单位，则使本效果层数增加1层 若现存体力低于75%，则改... |
| `HungryCharon` | **饥饿-暴怒** | LLC 基准 (BattleKeywords_Mirror6.json) | 最大值：3 肚子饿了。快给我糖果 |
| `HungryPeople_LowMorale` | **错失恐惧症** | LLC 2026092102／本地格式化 | - 士气低落 - 自身每失去20%体力，攻击等级+1(最多+2) - 对自身施加1层易损  |
| `HungryPeople_Panic` | **错失恐惧症** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 自身每失去20%体力，攻击等级+1(最多+2) - 对自身施加1层易损  |
| `HurtNightStiletto` | **创伤** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 回合结束时，下回合对自身施加1层束缚  - 回合结束时，若本效果层数为2层，则下... |
| `HystericGauge` | **歇斯底里** | LLC 基准 (BattleKeywords-walpu6.json) | - 基础值：0 - 最大值：3 - 回合结束时 · 若自身的理智值不低于0点，则使本效果的层数减少1... |
| `IDMicroChip` | **居民登记微芯片** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 使自身受到来自暴怒与嫉妒技能的伤害+10% - 拼点失败时，使自身增加1级烧伤 ... |
| `ImpendingCollapse` | **濒临崩坏** | LLC 基准 (BattleKeywords-walpu4.json) | 回合结束时，使本效果的层数减少1层 回合开始时，若本效果的层数不高于1层，则使用特殊技能 |
| `ImperfectEternalLife` | **不完善的不死** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 受到贾母特定技能攻击时被吸收 - 本效果施加给贾母时，本效果层数每有1层，对其施加1层易损 ；若... |
| `Inactible` | **无法行动** | LLC 基准 (BattleKeywords.json) | 本回合内无法行动。 |
| `IncompleteParade` | **不完善的游行** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 最大值：50 - 血袋阵亡时，对自身施加2层本效果 - 血魔阵亡时，对自身施加3层本效果 - 回... |
| `IncrementalMotionFirmware` | **小帮手-运动增量固件** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 移除全体友方单位的最靠前的1条混乱阈值 - 最多1次，陷入混乱时，下回合开始时解除自身的混乱 |
| `IndelibleGoodwill` | **无法抹去的善意** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 回合结束时自身不会失去护盾(不包括因受到伤害或特定效果而失去护盾) - 护盾受到攻击并被破坏时，... |
| `IndexPrescriptDon_0` | **指令[终端]I** | LLC 基准 (BattleKeywords-a1c9p2.json) | 使用被指令的印记标记的技能或使用被标记的技能命中目标  - 回合开始时，若未带有解放 ，则获得该效果... |
| `IndexPrescriptDon_1` | **指令[终端]II** | LLC 基准 (BattleKeywords-a1c9p2.json) | 使用被指令的印记标记的技能命中目标  - 回合开始时，若自身带有解放 - I，则获得该效果 - 该指... |
| `IndexPrescriptDon_2` | **指令[终端]III** | LLC 基准 (BattleKeywords-a1c9p2.json) | 使用觉醒E.G.O技能或处于绽放E.G.O::代行状态时使用被指令的印记标记的“3技能”命中目标  ... |
| `IndexPrescriptDon_3` | **指令[终端]IV** | LLC 基准 (BattleKeywords-a1c9p2.json) | 处决所有敌人。期限为下一条指令到来之前。  - 回合开始时，若自身带有解放 - III，则获得该效果 |
| `IndexPrescriptEnemy_0` | **指令[纸条]I** | LLC 基准 (BattleKeywords-twth.json) | 攻击并命中罪人。  - 回合开始时，若自身的指令加护层数为0~2层，则获得该效果 - 该指令最多可获... |
| `IndexPrescriptEnemy_1` | **指令[纸条]II** | LLC 基准 (BattleKeywords-twth.json) | 攻击并命中指令对象。  - 回合开始时，若自身的指令加护层数为3~5层，则获得该效果 - 该指令最多... |
| `IndexPrescriptEnemy_2` | **指令[纸条]III** | LLC 基准 (BattleKeywords-twth.json) | 包括自身在内的友方单位使随机罪人陷入混乱或击杀罪人。  - 回合开始时，若自身的指令加护层数为6~8... |
| `IndexPrescriptEnemy_3` | **指令[纸条]IV** | LLC 基准 (BattleKeywords-twth.json) | 处决所有敌人。期限为下一条指令到来之前。  - 回合开始时，若自身的指令加护层数为9层，则获得该效果 |
| `IndexPrescriptFaust_0` | **指令[纸条]I** | LLC 基准 (BattleKeywords-a1c9p1.json) | 使用被指令的印记标记的技能或使用被标记的技能命中目标。  - 回合开始时，若自身的指令加护层数为0~... |
| `IndexPrescriptFaust_1` | **指令[纸条]II** | LLC 基准 (BattleKeywords-a1c9p1.json) | 使用被指令的印记标记的技能命中目标。  - 回合开始时，若自身的指令加护层数为3~5层，则获得该效果... |
| `IndexPrescriptFaust_2` | **指令[纸条]III** | LLC 基准 (BattleKeywords-a1c9p1.json) | 使用觉醒E.G.O技能或被指令的印记标记的“3技能”命中目标。  - 回合开始时，若自身的指令加护层... |
| `IndexPrescriptFaust_3` | **指令[纸条]IV** | LLC 基准 (BattleKeywords-a1c9p1.json) | 处决所有敌人。期限为下一条指令到来之前。  - 回合开始时，若自身的指令加护层数为9层，则获得该效果 |
| `IndexPrescriptRien_0` | **指令[终端]I** | LLC 基准 (BattleKeywords-a1c9p3.json) | 攻击并命中指令对象。期限为首个回合结束之前。  - 回合开始时，若自身未带有解放，则获得该效果 - ... |
| `IndexPrescriptRien_1` | **指令[终端]II** | LLC 基准 (BattleKeywords-a1c9p3.json) | 攻击并命中指令对象；或在本回合内攻击并命中不低于4次。期限为第四回合结束之前。  - 回合开始时，若... |
| `IndexPrescriptRien_2` | **指令[终端]III** | LLC 基准 (BattleKeywords-a1c9p3.json) | 使用运用九种武器的强力技能。  - 回合开始时，若自身带有解放 - II ，则获得该效果 - 该指令... |
| `IndexPrescriptRien_3` | **指令[终端]IV** | LLC 基准 (BattleKeywords-a1c9p3.json) | 清除一切障碍。期限为下一条指令到来之前。  - 回合开始时，若自身带有解放 - III，则获得该效果 |
| `IndexPrescriptStudent_0` | **指令[终端]I** | LLC 基准 (BattleKeywords-a1c9p2.json) | 攻击并命中指令对象。  - 回合开始时，若自身未带有解放，则获得该效果 - 该指令最多可获得3层指令... |
| `IndexPrescriptStudent_1` | **指令[终端]II** | LLC 基准 (BattleKeywords-a1c9p2.json) | 使用首个行动槽装备的技能命中指令对象，或击杀随机目标。  - 回合开始时，若自身带有解放 - I，则... |
| `IndexPrescriptStudent_2` | **指令[终端]III** | LLC 基准 (BattleKeywords-a1c9p2.json) | 使随机目标陷入混乱，或击杀随机目标。  - 回合开始时，若自身带有解放 - II，则获得该效果 - ... |
| `IndexPrescriptStudent_3` | **指令[终端]IV** | LLC 基准 (BattleKeywords-a1c9p2.json) | 清除一切障碍。期限为下一条指令到来之前。  - 回合开始时，若自身带有解放 - III，则获得该效果 |
| `IndexPrescriptTargetMarkToEnemy` | **指令的印记** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 使仪表盘上自身的基础攻击技能获得指令的印记 |
| `IndexPrescriptTargetToEnemy` | **指令对象** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 受到属于食指的单位的伤害+10% - 无论属于食指的单位的数量，本效果每回合仅施加给单个目标 |
| `IndexPrescriptTargetToPersonality` | **食指的指令对象** | LLC 基准 (BattleKeywords-a1c9p2.json) | 对属于食指的敌方单位使用的技能威力-2，受到属于食指的敌方单位的伤害+20% |
| `IndexPrescriptYi_0` | **指令[终端]I** | LLC 基准 (BattleKeywords.json) | 使用被指令的印记标记的技能或使用被标记的技能命中目标  - 回合开始时，若未带有解放 ，则获得该效果... |
| `IndexPrescriptYi_1` | **指令[终端]II** | LLC 基准 (BattleKeywords.json) | 使用被指令的印记标记的技能命中目标  - 回合开始时，若自身带有解放 - I，则获得该效果 - 该指... |
| `IndexPrescriptYi_2` | **指令[终端]III** | LLC 基准 (BattleKeywords.json) | 获得代行[赫尔墨斯] 。重复本条指令直至代行[赫尔墨斯] 层数为9层。  - 回合开始时，若自身带有... |
| `IndexPrescriptYi_3` | **指令[终端]IV** | LLC 基准 (BattleKeywords.json) | 处决所有敌人。期限为下一条指令到来之前。  - 回合开始时，若自身带有解放 - III，则获得该效果 |
| `IndexPrescript_Base` | **指令** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 在特定条件下获得指令[纸条] |
| `IndexPrescript_Base_2nd` | **指令** | LLC 基准 (BattleKeywords-a1c9p2.json) | 在特定条件下获得指令[终端] |
| `IndexPrescript_RienSecondPhase` | **指令[终端]-警告** | LLC 基准 (BattleKeywords-a1c9p3.json) | 优先击杀指令对象。  - 第2阶段开始时，获得该效果 |
| `IndigoDamageDown` | **傲慢伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低傲慢技能造成的伤害。(最多10层) |
| `IndigoDamageUp` | **傲慢伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高傲慢技能造成的伤害。(最多10层) |
| `IndigoResistDown` | **傲慢抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的傲慢抗性增加(每层0.1) |
| `IndigoResistUp` | **傲慢抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的傲慢抗性减少(每层0.1) |
| `IndigoResultDown` | **傲慢威力降低** | LLC 基准 (Bufs.json) | 本回合内傲慢技能的最终威力-{0} |
| `IndigoResultUp` | **傲慢威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高傲慢技能的最终威力。 |
| `IndigoTakeDamageDown` | **傲慢守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自傲慢技能的伤害。(最多10层) |
| `IndigoTakeDamageUp` | **傲慢易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自傲慢技能的伤害。(最多10层) |
| `Inspire` | **灵感** | LLC 基准 (BattleKeywords_Mirror7.json) | 对带有绘画材料 的目标造成的伤害+10% |
| `IntenseColors` | **强烈色彩** | LLC 基准 (BattleKeywords-twth.json) | - 受到属于环指的单位的伤害+(本效果层数×5)% · 若攻击者属于环指 野兽派，则改为受到伤害+(... |
| `IntenseColorsRodion` | **强烈色彩** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 受到属于环指的单位的伤害+(本效果层数×2.5)% · 若攻击者属于环指野兽派，... |
| `InterlockingTime` | **啮合的时间** | LLC 基准 (BattleKeywords.json) | 减少并储存最终伤害的30%。本效果层数为3层时，对自身造成所储存的伤害量1.5倍的固定伤害。 |
| `InterlockingTimeBokGak` | **啮合的时间** | LLC 基准 (BattleKeywords_Refraction2.json) | - 减少并储存最终伤害的30%。 - 本效果层数为3层时，对自身造成储存的伤害量2倍的固定伤害并解除... |
| `InterlockingTime_Re` | **啮合的时间** | LLC 基准 (BattleKeywords_Refraction2.json) | 减少并储存最终伤害的30%。本效果层数为3层时，对自身造成储存的伤害量2倍的固定伤害。下回合对自身施... |
| `IronMaidenPersonality` | **铁处女** | LLC 基准 (BattleKeywords.json) | - 使自身最左侧行动槽的挑衅值 +4 - 回合开始时，使自身获得1层守护 ，5层防御等级提升 与现存... |
| `IronMaiden_LowMorale` | **铁处女** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 士气低落 - 回合开始时，对自身施加1层攻击等级降低 并使自身获得1层防御等级提升 |
| `IronMaiden_Panic` | **铁处女** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 陷入恐慌 - 回合开始时，对自身施加2层攻击等级降低 并使自身获得2层防御等级提升 |
| `Irritation` | **天退星** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合开始时，自身每失去20%的体力，使自身获得1层伤害强化 与1层威力提升 (分别最多3层) -... |
| `IrritationAlly` | **天退星** | LLC 基准 (BattleKeywords.json) | - 使自身的最小与最大速度值+1 - 若自身的速度值高于目标至少3点，则使自身造成的伤害+(速度值之... |
| `JarMaster_LowMorale` | **突击指示** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 回合开始时，对自身施加1层易损 并使全体友方单位获得1层伤害强化 |
| `JarMaster_Panic` | **突击指示** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 回合开始时，对自身施加2层易损 并使全体友方单位获得2层伤害强化 |
| `KAA1C9ActivateEffect` | **使用K公司安瓿** | LLC 基准 (BattleKeywords-a1c9p3.json) | 已使用的K公司的安瓿 |
| `KAmpouleA1C94TH` | **紧急用K公司安瓿** | LLC 基准 (BattleKeywords-a1c9p3.json) | 有除自身以外的友方单位存活时，若受到将自身体力降至0点的伤害，则触发以下效果： - 若陷入混乱，则解... |
| `KAmpouleMirror` | **紧急用K公司安瓿** | LLC 基准 (BattleKeywords_Mirror7.json) | 若受到将自身体力降至0点的伤害，则触发以下效果： - 若陷入混乱，则解除自身的混乱 - 恢复所有体力... |
| `KCorpSerum` | **K公司的安瓿** | LLC 基准 (BattleKeywords.json) | 回合开始时，若本效果层数低于4层，则使自身恢复体力上限(本效果层数×5)%的体力 若本效果层数不低于... |
| `KalpaVine` | **永劫的荆棘** | LLC 基准 (BattleKeywords_Refraction2.json) | 所有角色造成的伤害减少 所有角色受到的伤害减少 |
| `KarmaOfIndexAlly` | **业** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 回合开始时 · 每带有10层本效果，对自身施加1层防御等级降低  · 每带有20层本效果，对自身... |
| `KarmaOfIndexEnemy` | **业** | LLC 基准 (BattleKeywords-twth.json) | - 回合开始时 · 每带有10层本效果，对自身施加1层防御等级降低  · 每带有20层本效果，对自身... |
| `KarmaOfIndexRien` | **业** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时 · 每带有10层本效果，对自身施加1层防御等级降低  · 每带有20层本效果，对自身... |
| `KarmaOfIndexRien_2Phase` | **业[福尔图娜]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时 · 每带有10层本效果，对自身施加1层防御等级降低  · 每带有20层本效果，对自身... |
| `KarmaOfIndexStudent` | **业** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 回合开始时 · 每带有10层本效果，对自身施加1层防御等级降低  · 每带有20层本效果，对自身... |
| `KeptBlood` | **浸染的血液** | LLC 基准 (BattleKeywords-mowe.json) | - 最大值：10 - 自身每损失体力上限5%的体力，本效果减少1层 - 攻击命中时，使自身恢复体力上... |
| `KnightBless` | **加护** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，使自身获得2层守护  - 使自身高于1的物理抗性变为1(不包括陷入混乱) |
| `KnowledgeExplored` | **所解真知** | LLC 基准 (BattleKeywords.json) | 本效果的层数等于带有本效果的单位最后丢弃技能的级别(基础值：1) |
| `KnowledgeTraining` | **磨砺学识** | LLC 基准 (BattleKeywords.json) | - 最大值：6 - 丢弃 技能时，使自身获得体力上限(自身的磨砺学识层数×1.5)%的护盾(每回合最... |
| `LCA_Bullet` | **LCA龟裂弹** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 最大值：16 - 特定技能使用时消耗 - 若缺少弹药 ，部分攻击会取消 |
| `LCEFireFly_LowMorale` | **劣化侵蚀** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 回合开始时，对自身施加1层易损 |
| `LCEFireFly_Panic` | **劣化侵蚀** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 回合开始时，对自身施加1层易损并使自身增加5级烧伤 强度 |
| `LaNoir_LowMorale` | **回到壳中……** | LLC 2026092102／本地格式化 | - 士气低落 最大速度值-1 防御等级+1 |
| `LaNoir_Panic` | **回到壳中……** | LLC 2026092102／本地格式化 | - 陷入恐慌 最大速度值-5 防御等级+3 |
| `LaRouge_LowMorale` | **从皮里出去！** | LLC 2026092102／本地格式化 | - 士气低落 防御等级-3 攻击等级+1 |
| `LaRouge_Panic` | **从皮里出去！** | LLC 2026092102／本地格式化 | - 陷入恐慌 防御等级-5 攻击等级+2 |
| `Laceration` | **流血** | LLC 基准 (BattleKeywords.json) | 掷出攻击技能硬币时，受到数值等同于本效果强度的固定伤害。 效果生效后，本效果的层数减少1层。 |
| `LanternGregBigBird` | **目灯** | LLC 基准 (BattleKeywords.json) | - 最大值：8 - 回合结束时，每带有2层本效果，下回合对自身施加1层束缚 (最多4层) - 回合结... |
| `LanternHohenheimBigBird` | **目灯** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：20 - 本效果层数每有2层，下回合对自身施加1层束缚 (最多10层) - 回合结束时，... |
| `LastingHongwonWill_LowMorale` | **传承的鸿园之意** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 使自身获得2层强壮 并对自身施加1层束缚  - 躯干部位与鸿璐拼点失败时，下回合使... |
| `LastingHongwonWill_Panic` | **传承的鸿园之意** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 使自身获得2层强壮 并对自身施加2层束缚  - 躯干部位与鸿璐拼点失败时，下回合使... |
| `LeRegole_LowMorale` | **纪律** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 若自身上回合增加的震颤 强度不低于2级，则使自身获得1层怠惰伤害强化  - 若自身... |
| `LeRegole_Panic` | **纪律** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 若自身上回合增加的震颤 强度不低于2级，则使自身获得2层怠惰伤害强化  - 若自身... |
| `LeakedOutSauce` | **漏出的酱料** | LLC 基准 (BattleKeywords-x1p1c1.json) | - 回合结束时，每带有2层本效果，下回合使自身获得1层迅捷 (最多10层) - 回合结束时解除本效果 |
| `LegStrength` | **脚力【卯】** | LLC 基准 (BattleKeywords-a1c9116.json) | 最大值：3 回合结束时，下回合使自身获得5层迅捷  回合结束时，本效果的层数减少1层 |
| `LegStrengthHorse` | **脚力【午】** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：3 - 回合结束时，下回合使自身获得2层迅捷 与(本效果层数×2)层防御等级提升  - ... |
| `LegStrengthHorseYisang` | **脚力【午】** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合结束时，下回合使自身获得2层迅捷 并使自身的挑衅值 +(本效果层数×2) -... |
| `LensmanNail` | **定格尖钉** | LLC 基准 (BattleKeywords-exme.json) | - 最大值：10 - 回合开始时，每带有2层束缚 ，对自身施加1层攻击等级降低 (最多3层) - 回... |
| `LensmanPower` | **调查命令** | LLC 基准 (BattleKeywords-exme.json) | - 基础攻击等级+5 - 基础防御等级+5 |
| `Lensman_LowMorale` | **对情报的执念** | LLC 基准 (BattleKeywords-exme.json) | - 与带有获取情报 的目标进行拼点时，使自身的基础威力+1，造成的伤害+10% - 回合开始时，对自... |
| `Lensman_Panic` | **对情报的执念** | LLC 基准 (BattleKeywords-exme.json) | - 与带有获取情报 的目标进行拼点时，使自身的基础威力+1，造成的伤害+20% - 回合开始时，对自... |
| `LibrarianOfHistoryHard` | **历史层司书** | LLC 基准 (Bufs.json) | - 该人格的行动槽+1 - 回合开始时恢复15点理智值 - 自身技能所施加的烧伤、流血、破裂、沉沦、... |
| `LibrarianOfHistoryNormal` | **历史层助理司书** | LLC 基准 (Bufs.json) | - 该人格的行动槽+1 - 回合开始时恢复15点理智值 - 自身技能所施加的烧伤、流血、破裂、沉沦、... |
| `LimitedAwakenSinclair` | **本影 禁制解除** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击技能造成的伤害+10% - 回合开始时，使自身获得1层加算硬币强化 |
| `LimitedTime` | **抢来的时间** | LLC 基准 (BattleKeywords-tkt.json) | - 回合开始时，若层数不低于200层，则使自身获得(层数-200)/50层攻击等级提升 与防御等级提... |
| `LineCutting` | **缝纫对象** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 优先成为？？？的攻击指定目标 - 回合结束时解除本效果 |
| `LineCuttingPersonality` | **缝纫对象** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 自身每带有1级流血 强度，使自身受到的伤害+0.5%(最多+10%) - 回合结... |
| `LittleCourage` | **某道印记** | LLC 基准 (Bufs.json) | 辛克莱向克罗默抗争的决心。画下三道线的话…… |
| `LittleFingerBoss_Shin` | **心-地慧星** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最大值：3 - 回合开始时，触发以下效果 · 每带有1层本效果，使自身增加5级呼吸法 强度并使自... |
| `LittleFingerID` | **月下青刀** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 回合开始时，每带有1层本效果，使自身获得2点护盾 - 每带有1层本效果，使自身... |
| `Liu_Meursault_Guard_Buff` | **坚如泰山** | LLC 基准 (BattleKeywords.json) | 受到攻击时，对攻击者施加1层烧伤 。 |
| `LivingSpecimenPersonality` | **人体观剧** | LLC 基准 (BattleKeywords.json) | - 基础值：3 - 敌方单位的攻击技能对自身施加流血 时，下回合随机对自身施加以下1种负面状态，并使... |
| `LivingSpecimenTheRings` | **人体观剧** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 处于无法行动状态，自身的状态效果、体力与理智值不会改变，生成与自身相连的人体观剧 |
| `LogicAtelierAM` | **集中精神【狙击】** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 回合结束时获得1层本效果 |
| `LongLastingHongwonWill_LowMorale` | **悠久传承的鸿园之意** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 使自身获得2层强壮 并对自身施加1层易损  - 对自身生成的单位施加3层防御等级降... |
| `LongLastingHongwonWill_Panic` | **悠久传承的鸿园之意** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 使自身获得2层强壮 并对自身施加2层易损  - 对自身生成的单位施加6层防御等级降... |
| `LookingFuture` | **加速的未来** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 本效果的层数每有1层，拼点威力+1 - 本效果的层数每有5层，硬币威力+1 -... |
| `LookingFutureMirror` | **瞬间的预知** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：5  - 每带有1层本效果，使自身的拼点威力+2 - 每带有2层本效果，使自身加算硬币技... |
| `LookingFutureRodion` | **加速的未来** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 每带有1层本效果，使自身基础技能造成的伤害+3%(最多+15%) - 每带有2层... |
| `LvDownLittleFingerBoss` | **观望** | LLC 基准 (BattleKeywords-a1c9p2.json) | 未使用buff |
| `LvDownLittleFingerBossTwo` | **天杀星伤** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级-15 - 基础防御等级-15 |
| `LvUpFireFly` | **E.G.O感应度 增加** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级+10 - 基础防御等级+10 |
| `LvUpFireFly_Over` | **E.G.O感应度 过载** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级+10 - 基础防御等级+10 - 回合结束时，使自身增加4级烧伤 强度并失去5点理... |
| `LvUpHohenheimBigBird` | **E.G.O感应度 增加** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级+15 - 基础防御等级+15 |
| `LvUpHohenheimBigBird_Over` | **E.G.O感应度 过载** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级+15 - 基础防御等级+15 - 回合结束时，使自身获得至20层目灯 ，每获得1层... |
| `MD511` | **攻击等级强化I** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +1 |
| `MD512` | **防御等级强化** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +2 |
| `MD513` | **强韧I** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +1，体力上限 +2.5% |
| `MD514` | **生长I** | LLC 基准 (BattleKeywords_Mirror5.json) | 体力上限 +5% |
| `MD515` | **守备技能强化** | LLC 基准 (BattleKeywords_Mirror5.json) | 守备技能最终威力 +1 |
| `MD516` | **受到的伤害减少强化** | LLC 基准 (BattleKeywords_Mirror5.json) | 受到的伤害 -5% |
| `MD521` | **攻击等级强化II** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +2 |
| `MD522` | **肉体强化I** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +1，防御等级 +1，体力上限 +2.5% |
| `MD523` | **锐利I** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +1，体力上限 +5% |
| `MD524` | **强韧II** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +1，体力上限 +7.5% |
| `MD525` | **强韧III** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +2，体力上限 +5% |
| `MD526` | **生长II** | LLC 基准 (BattleKeywords_Mirror5.json) | 体力上限 +10% |
| `MD527` | **顽强I** | LLC 基准 (BattleKeywords_Mirror5.json) | 受到的伤害 -7.5%，造成的伤害 +7.5% |
| `MD531` | **锐利II** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +2，体力上限 +7.5% |
| `MD532` | **锐利III** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +3，体力上限 +5% |
| `MD533` | **强韧IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +3，体力上限 +7.5% |
| `MD534` | **强韧V** | LLC 基准 (BattleKeywords_Mirror5.json) | 防御等级 +4，体力上限 +5% |
| `MD535` | **生长III** | LLC 基准 (BattleKeywords_Mirror5.json) | 体力上限 +15% |
| `MD536` | **拼点威力增幅** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力 +1，体力上限 +7.5% |
| `MD537` | **最终威力增幅** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力 +1，体力上限 +5% |
| `MD538` | **基础威力增幅** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力 +1，体力上限 +2.5% |
| `MD541` | **锐利IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +3，体力上限 +15% |
| `MD542` | **肉体强化II** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +2，防御等级 +3，体力上限 +10% |
| `MD543` | **肉体强化III** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级 +3，防御等级 +2，体力上限 +10% |
| `MD544` | **生长IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 体力上限 +30% |
| `MD545` | **拼点威力增强** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力 +1，体力上限 +15% |
| `MD546` | **最终威力增强** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力 +1，体力上限 +12.5% |
| `MD547` | **基础威力增强** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力 +1，体力上限 +10% |
| `MD548` | **破坏力** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力 +1，减算硬币威力 -1 |
| `MD549` | **顽强 II** | LLC 基准 (BattleKeywords_Mirror5.json) | 受到的伤害 -25%，造成的伤害 +25% |
| `MD551` | **锐利V** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+4，体力上限+10%，造成的伤害+5% |
| `MD552` | **肉体强化IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+3，防御等级+3，体力上限+7.5%，造成的伤害+5% |
| `MD553` | **肉体强化V** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+4，防御等级+2，体力上限+5%，造成的伤害+5% |
| `MD554` | **生长V** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+1，体力上限+25%，造成的伤害+5% |
| `MD555` | **拼点威力增强II** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力+1，攻击等级+1，体力上限+10%，造成的伤害+5% |
| `MD556` | **最终威力增强II** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力+1，攻击等级+1，体力上限+7.5%，造成的伤害+5% |
| `MD557` | **基础威力增强II** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力+1，攻击等级+1，体力上限+5%，造成的伤害+5% |
| `MD558` | **破坏力II** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力+1，减算硬币威力-1，造成的伤害+5% |
| `MD561` | **锐利VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+5，体力上限+10%，造成的伤害+5% |
| `MD562` | **强韧VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+2，防御等级+6，体力上限+10%，造成的伤害+5% |
| `MD563` | **肉体强化VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+5，防御等级+2，体力上限+5%，造成的伤害+5% |
| `MD564` | **生长VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+2，体力上限+25%，造成的伤害+5% |
| `MD565` | **拼点威力增强III** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力+1，攻击等级+2，体力上限+10%，造成的伤害+5% |
| `MD566` | **最终威力增强III** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力+1，攻击等级+2，体力上限+7.5%，造成的伤害+5% |
| `MD567` | **基础威力增强III** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力+1，攻击等级+2，体力上限+5%，造成的伤害+5% |
| `MD568` | **破坏力III** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力+1，减算硬币威力-1，造成的伤害+5% |
| `MD571` | **锐利VII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+5，体力上限+20%，造成的伤害+7.5% |
| `MD572` | **强韧VII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+2，防御等级+6，体力上限+20%，造成的伤害+7.5% |
| `MD573` | **肉体强化VII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+5，防御等级+2，体力上限+15%，造成的伤害+7.5% |
| `MD574` | **生长VII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+2，体力上限+35%，造成的伤害+7.5% |
| `MD575` | **拼点威力增强IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力+1，攻击等级+2，体力上限+20%，造成的伤害+7.5% |
| `MD576` | **最终威力增强IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力+1，攻击等级+2，体力上限+17.5%，造成的伤害+7.5% |
| `MD577` | **基础威力增强IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力+1，攻击等级+2，体力上限+15%，造成的伤害+7.5% |
| `MD578` | **破坏力IV** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力+1，减算硬币威力-1，造成的伤害+7.5% |
| `MD581` | **锐利VIII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+6，体力上限+30%，造成的伤害+7.5% |
| `MD582` | **强韧VIII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+3，防御等级+6，体力上限+30%，造成的伤害+7.5% |
| `MD583` | **肉体强化VIII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+5，防御等级+4，体力上限+22.5%，造成的伤害+7.5% |
| `MD584` | **生长VIII** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+3，体力上限+45%，造成的伤害+7.5% |
| `MD585` | **拼点威力增强V** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力+2，攻击等级+1，体力上限+25%，造成的伤害+7.5% |
| `MD586` | **最终威力增强V** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力+2，攻击等级+1，体力上限+20%，造成的伤害+7.5% |
| `MD587` | **基础威力增强V** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力+2，攻击等级+1，体力上限+15%，造成的伤害+7.5% |
| `MD588` | **破坏力V** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力+2，减算硬币威力-2，造成的伤害+7.5% |
| `MD591` | **锐利IX** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+8，体力上限+40%，造成的伤害+10% |
| `MD592` | **强韧IX** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+3，防御等级+9，体力上限+40%，造成的伤害+10% |
| `MD593` | **肉体强化IX** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+6，防御等级+5，体力上限+32.5%，造成的伤害+10% |
| `MD594` | **生长IX** | LLC 基准 (BattleKeywords_Mirror5.json) | 攻击等级+3，体力上限+72.5%，造成的伤害+10% |
| `MD595` | **拼点威力增强VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 拼点威力+2，攻击等级+2，体力上限+40%，造成的伤害+10% |
| `MD596` | **最终威力增强VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 最终威力+2，攻击等级+2，体力上限+35%，造成的伤害+10% |
| `MD597` | **基础威力增强VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 基础威力+2，攻击等级+2，体力上限+30%，造成的伤害+10% |
| `MD598` | **破坏力VI** | LLC 基准 (BattleKeywords_Mirror5.json) | 加算硬币威力+2，减算硬币威力-2，造成的伤害+10% |
| `MD5Base` | **追加的苦难** | LLC 基准 (BattleKeywords_Mirror5.json) |  |
| `MD6101` | **锐利XII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，攻击等级+8，防御等级+3，体力上限+40%，造成的伤害+10%，头目遭遇战体力上限+... |
| `MD6102` | **强韧XII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，攻击等级+4，防御等级+11，体力上限+40%，造成的伤害+10%，头目遭遇战体力上限... |
| `MD6103` | **肉体强化XII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，攻击等级+6，防御等级+7，体力上限+35%，造成的伤害+10%，头目遭遇战体力上限+... |
| `MD6104` | **生长XII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，攻击等级+3，防御等级+3，体力上限+72.5%，造成的伤害+10%，头目遭遇战体力上... |
| `MD6105` | **拼点威力增强VII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+3，攻击等级+2，防御等级+2，体力上限+42.5%，造成的伤害+10%，头目遭遇战体力上... |
| `MD6106` | **最终威力增强VII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，最终威力+2，攻击等级+2，防御等级+2，体力上限+37.5%，造成的伤害+10%，头... |
| `MD6107` | **基础威力增强VII** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+1，基础威力+2，攻击等级+2，防御等级+2，体力上限+32.5%，造成的伤害+10%，头... |
| `MD6111` | **锐利XIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，攻击等级+8，防御等级+5，体力上限+40%，造成的伤害+12.... |
| `MD6112` | **强韧XIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，攻击等级+5，防御等级+12，体力上限+42.5%，造成的伤害+... |
| `MD6113` | **肉体强化XIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，攻击等级+7，防御等级+7，体力上限+40%，造成的伤害+10%... |
| `MD6114` | **生长XIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，攻击等级+3，防御等级+3，体力上限+80%，造成的伤害+10%... |
| `MD6115` | **拼点威力增强VIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，拼点威力+2，攻击等级+3，防御等级+3，体力上限+45%，造成... |
| `MD6116` | **最终威力增强VIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，最终威力+2，攻击等级+2，防御等级+2，体力上限+40%，造成... |
| `MD6117` | **基础威力增强VIII** | LLC 基准 (BattleKeywords_Mirror6.json) | 加算硬币威力+1，减算硬币威力-1，基础威力+2，攻击等级+2，防御等级+2，体力上限+35%，造成... |
| `MD6121` | **锐利XIV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+10，防御等级+5，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+30% |
| `MD6122` | **强韧XIV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+5，防御等级+15，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+30% |
| `MD6123` | **肉体强化XIV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+8，防御等级+8，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+30% |
| `MD6124` | **生长XIV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+3，防御等级+3，体力上限+90%，造成的伤害+10%，头目遭遇战体力上限+30% |
| `MD6125` | **拼点威力增强IX** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+2，攻击等级+4，防御等级+4，体力上限+45%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6126` | **最终威力增强IX** | LLC 基准 (BattleKeywords_Mirror6.json) | 最终威力+2，攻击等级+3，防御等级+3，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6127` | **基础威力增强IX** | LLC 基准 (BattleKeywords_Mirror6.json) | 基础威力+2，攻击等级+3，防御等级+3，体力上限+35%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6131` | **锐利XV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+10，防御等级+5，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+40% |
| `MD6132` | **强韧XV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+5，防御等级+15，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+40% |
| `MD6133` | **肉体强化XV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+8，防御等级+8，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+40% |
| `MD6134` | **生长XV** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+3，防御等级+3，体力上限+90%，造成的伤害+10%，头目遭遇战体力上限+40% |
| `MD6135` | **拼点威力增强X** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+2，攻击等级+4，防御等级+4，体力上限+45%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6136` | **最终威力增强X** | LLC 基准 (BattleKeywords_Mirror6.json) | 最终威力+2，攻击等级+3，防御等级+3，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6137` | **基础威力增强X** | LLC 基准 (BattleKeywords_Mirror6.json) | 基础威力+2，攻击等级+3，防御等级+3，体力上限+35%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6141` | **锐利XVI** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+10，防御等级+5，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+50% |
| `MD6142` | **强韧XVI** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+5，防御等级+15，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+50% |
| `MD6143` | **肉体强化XVI** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+8，防御等级+8，体力上限+45%，造成的伤害+10%，头目遭遇战体力上限+50% |
| `MD6144` | **生长XVI** | LLC 基准 (BattleKeywords_Mirror6.json) | 攻击等级+3，防御等级+3，体力上限+90%，造成的伤害+10%，头目遭遇战体力上限+50% |
| `MD6145` | **拼点威力增强XI** | LLC 基准 (BattleKeywords_Mirror6.json) | 拼点威力+2，攻击等级+4，防御等级+4，体力上限+45%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6146` | **最终威力增强XI** | LLC 基准 (BattleKeywords_Mirror6.json) | 最终威力+2，攻击等级+3，防御等级+3，体力上限+40%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6147` | **基础威力增强XI** | LLC 基准 (BattleKeywords_Mirror6.json) | 基础威力+2，攻击等级+3，防御等级+3，体力上限+35%，造成的伤害+15%，头目遭遇战体力上限+... |
| `MD6Limit101` | **等级强化** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位提升3级 |
| `MD6Limit102` | **衰弱** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体友方单位的体力上限-10% |
| `MD6Limit103` | **炎之烙印I** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合结束时，使全体友方单位受到5点固定体力伤害。每回合伤害量增加3点(最多20点) |
| `MD6Limit104` | **通货膨胀I** | LLC 基准 (BattleKeywords_Mirror6.json) | 除售卖以外的所有商店功能消耗的经费变为2倍 |
| `MD6Limit105` | **自我干涉I** | LLC 基准 (BattleKeywords_Mirror6.json) | 使用E.G.O技能时消耗的E.G.O资源变为2倍 (本限制不会影响饰品的效果) |
| `MD6Limit111` | **等级强化** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位提升3级 |
| `MD6Limit112` | **衰弱** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体友方单位的体力上限-10% |
| `MD6Limit113` | **精神错乱I** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合结束时，使全体友方单位失去3点理智值 |
| `MD6Limit114` | **神经加速I** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位的最小与最大速度值+1 |
| `MD6Limit115` | **理智枯竭I** | LLC 基准 (BattleKeywords_Mirror6.json) | 战斗中，全体友方单位的理智值无法恢复至35点以上 |
| `MD6Limit121` | **等级强化** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位提升3级 |
| `MD6Limit122` | **衰弱** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体友方单位的体力上限-10% |
| `MD6Limit123` | **震颤阻绝** | LLC 基准 (BattleKeywords_Mirror6.json) | 移除全体敌方单位的第一混乱阈值 |
| `MD6Limit124` | **通货膨胀II** | LLC 基准 (BattleKeywords_Mirror6.json) | 除售卖以外的所有商店功能消耗的经费变为3倍  ※存在相同效果的低级制约时，覆盖该效果 |
| `MD6Limit125` | **自我干涉II** | LLC 基准 (BattleKeywords_Mirror6.json) | 使用E.G.O技能时消耗的E.G.O资源变为3倍 (本限制不会影响饰品的效果)  ※存在相同效果的低... |
| `MD6Limit131` | **等级强化** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位提升3级 |
| `MD6Limit132` | **衰弱** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体友方单位的体力上限-10% |
| `MD6Limit133` | **生命增幅** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位的体力上限+30% |
| `MD6Limit134` | **破坏力** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位的加算硬币威力+2，减算硬币威力-2 |
| `MD6Limit135` | **炎之烙印II** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合结束时，使全体友方单位受到10点固定体力伤害。每回合伤害量增加5点(最多30点)  ※存在相同效... |
| `MD6Limit141` | **等级强化** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位提升3级 |
| `MD6Limit142` | **衰弱** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体友方单位的体力上限-10% |
| `MD6Limit143` | **精神错乱II** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合结束时，使全体友方单位失去5点理智值  ※存在相同效果的低级制约时，覆盖该效果 |
| `MD6Limit144` | **神经加速II** | LLC 基准 (BattleKeywords_Mirror6.json) | 全体敌方单位的最小与最大速度值+2 |
| `MD6Limit145` | **理智枯竭II** | LLC 基准 (BattleKeywords_Mirror6.json) | 战斗中，全体友方单位的理智值无法恢复至30点以上  ※存在相同效果的低级制约时，覆盖该效果 |
| `MD6LimitBaseN` | **追加的制约** | LLC 基准 (BattleKeywords_Mirror6.json) |  |
| `MD7Limit101` | **战力的再分配** | LLC 基准 (BattleKeywords_Mirror7.json) | 敌方单位阵亡时，下回合开始时使全体敌方单位获得3层攻击等级提升 (每回合最多3次，包括波次开始时) |
| `MD7Limit111` | **精神昂扬** | LLC 基准 (BattleKeywords_Mirror7.json) | 回合开始时，使全体敌方单位恢复20点理智值 (拥有的技能全部为减算硬币技能的敌方单位改为失去15点理... |
| `MD7Limit121` | **生成护盾** | LLC 基准 (BattleKeywords_Mirror7.json) | 使全体敌方单位获得3000点护盾 (若是集中遭遇战，则使本体获得；通过本效果获得的护盾不会在回合结束... |
| `MD7Limit131` | **龟裂增殖** | LLC 基准 (BattleKeywords_Mirror7.json) | 敌方单位的技能施加的烧伤 、流血 、震颤 、破裂 与沉沦 变为2倍 |
| `MD7Limit141` | **增加异常状态** | LLC 基准 (BattleKeywords_Mirror7.json) | 回合开始时，使全体友方单位(人格)增加5级某1种随机效果的强度，该效果可能为烧伤 、流血 、震颤 、... |
| `MDEMaa` | **防御等级强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级 +2 |
| `MDEMab` | **守备技能强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 守备技能最终威力 +1 |
| `MDEMac` | **攻击等级强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +1 |
| `MDEMad` | **体力上限提升** | LLC 基准 (BattleKeywords_Mirror4.json) | 体力上限 +5% |
| `MDEMae` | **受到的伤害减少强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 受到的伤害 -5% |
| `MDEMca` | **肉体肥大** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +2，防御等级 +2，体力上限 +5% |
| `MDEMcb` | **肉体强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级+2，防御等级+4 |
| `MDEMcc` | **体力上限强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 体力上限 +20% |
| `MDEMcd` | **最终攻击增强** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+1，体力上限 +5% |
| `MDEMce` | **基础攻击增强** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能基础威力+1，体力上限 +5% |
| `MDEMcf` | **拼点攻击增强** | LLC 基准 (BattleKeywords_Mirror4.json) | 拼点威力 +2，防御等级 -3 |
| `MDEMcg` | **最终威力强化** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+1，守备技能最终威力+1 |
| `MDEMda` | **肉体生长** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +3，防御等级 +2，体力上限 +10% |
| `MDEMdb` | **肉体补强** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +5，体力上限 +7.5% |
| `MDEMdc` | **基本战斗装备** | LLC 基准 (BattleKeywords_Mirror4.json) | 基础威力 +1，防御等级 +3，体力上限 +5% |
| `MDEMdd` | **最终战斗装备** | LLC 基准 (BattleKeywords_Mirror4.json) | 最终威力 +1，防御等级 -2，体力上限 +17.5% |
| `MDEMde` | **防御装备** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级 +3，体力上限 +22.5% |
| `MDEMdf` | **硬币攻击增强** | LLC 基准 (BattleKeywords_Mirror4.json) | 加算硬币威力 +1，减算硬币威力 -1，防御等级 +2 |
| `MDEMdg` | **强大无比** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能的基础威力+1，加算硬币威力+1，减算硬币威力-1 |
| `MDEMdh` | **加倍奉还** | LLC 基准 (BattleKeywords_Mirror4.json) | 受到的伤害 -25%，造成的伤害 +25% |
| `MDHMaa` | **肉体增强I** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +1，防御等级 +1 |
| `MDHMab` | **硬化** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级 +2，守备技能的最终威力 +1 |
| `MDHMac` | **肉体扩展I** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级 +1，体力上限 +5% |
| `MDHMad` | **体力上限增强I** | LLC 基准 (BattleKeywords_Mirror4.json) | 体力上限 +7.5% |
| `MDHMae` | **受到伤害降低** | LLC 基准 (BattleKeywords_Mirror4.json) | 受到的伤害 -7.5% |
| `MDHMba` | **肉体增强II** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +2，防御等级 +2，体力上限 +5% |
| `MDHMbb` | **肉体扩展II** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +2，体力上限 +10% |
| `MDHMbc` | **最终威力增强I** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+1，体力上限 +5% |
| `MDHMbd` | **基础威力增强I** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能基础威力+1，防御等级 +1 |
| `MDHMbe` | **强韧I** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级 +4，体力上限 +10% |
| `MDHMbf` | **复仇I** | LLC 基准 (BattleKeywords_Mirror4.json) | 受到的伤害 -10%，造成的伤害 +10% |
| `MDHMca` | **肉体增强III** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +4，防御等级 +3，体力上限 +7.5% |
| `MDHMcb` | **肉体扩展III** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +4，体力上限 +15% |
| `MDHMcc` | **最终威力增强II** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+1，防御等级+6 |
| `MDHMcd` | **基础威力增强II** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能基础威力+1，防御等级+5 |
| `MDHMce` | **最终威力增强III** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+2，防御等级-2，体力上限+5% |
| `MDHMcf` | **体力上限增强II** | LLC 基准 (BattleKeywords_Mirror4.json) | 体力上限 +30% |
| `MDHMcg` | **拼点攻击增强I** | LLC 基准 (BattleKeywords_Mirror4.json) | 拼点威力 +2，体力上限+7.5% |
| `MDHMda` | **肉体增强IV** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级 +6，防御等级 +6，体力上限+15% |
| `MDHMdb` | **肉体扩展IV** | LLC 基准 (BattleKeywords_Mirror4.json) | 攻击等级+4，防御等级+3，体力上限+30% |
| `MDHMdc` | **最终威力增强IV** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能最终威力+2，体力上限+25% |
| `MDHMdd` | **基础威力增强III** | LLC 基准 (BattleKeywords_Mirror4.json) | 技能基础威力+1，技能最终威力+1，体力上限+20% |
| `MDHMde` | **强韧II** | LLC 基准 (BattleKeywords_Mirror4.json) | 防御等级+9，体力上限+30% |
| `MDHMdf` | **硬币威力增强** | LLC 基准 (BattleKeywords_Mirror4.json) | 加算硬币威力 +2，减算硬币威力 -2 |
| `MDHMdg` | **拼点攻击增强II** | LLC 基准 (BattleKeywords_Mirror4.json) | 拼点威力 +2，体力上限 +30% |
| `MDHMdh` | **顽强** | LLC 基准 (BattleKeywords_Mirror4.json) | 受到的伤害 -50%，造成的伤害 +50% |
| `MDHcFaBa` | **防御等级强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 防御等级+4 |
| `MDHcFaBb` | **守备威力强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 守备技能基础威力+2 |
| `MDHcFaBc` | **体力上限强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 体力上限+10% |
| `MDHcFaBd` | **受到伤害降低** | LLC 基准 (BattleKeywords_Mirror3.json) | 受到的伤害-10% |
| `MDHcFbBa` | **攻击等级强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 攻击等级+3，体力上限+5% |
| `MDHcFbBb` | **最终威力强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能最终威力+1，体力上限+5% |
| `MDHcFbBc` | **基础威力强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能基础威力+1，体力上限+5% |
| `MDHcFbBd` | **造成伤害强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 造成的伤害+15%，体力上限+5% |
| `MDHcFcBa` | **最终威力增幅 I** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能最终威力+1，体力上限+15% |
| `MDHcFcBb` | **最终威力增幅 II** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能最终威力+2，防御等级-4，体力上限+15% |
| `MDHcFcBc` | **基础威力增幅 I** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能基础威力+1，体力上限+10% |
| `MDHcFcBd` | **基础威力增幅 II** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能基础威力+2，防御等级-4，体力上限+10% |
| `MDHcFcBe` | **硬币威力增幅 I** | LLC 基准 (BattleKeywords_Mirror3.json) | 加算硬币威力+1，减算硬币威力-1 |
| `MDHcFcBf` | **过载 I** | LLC 基准 (BattleKeywords_Mirror3.json) | 攻击等级+7，防御等级-7 |
| `MDHcFdBa` | **最终威力增幅 III** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能最终威力+2，防御等级+6，体力上限+10% |
| `MDHcFdBb` | **最终威力增幅 IV** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能最终威力+3，体力上限+10% |
| `MDHcFdBc` | **硬币威力增幅 II** | LLC 基准 (BattleKeywords_Mirror3.json) | 加算硬币威力+1，减算硬币威力-1，体力上限+15% |
| `MDHcFdBd` | **基础威力增幅 III** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能基础威力+2，防御等级+3，体力上限+10% |
| `MDHcFdBe` | **过载 II** | LLC 基准 (BattleKeywords_Mirror3.json) | 攻击等级+10，防御等级-7 |
| `MDHcFdBf` | **强韧** | LLC 基准 (BattleKeywords_Mirror3.json) | 体力上限+25%，防御等级+5 |
| `MDHcFdBg` | **顽强** | LLC 基准 (BattleKeywords_Mirror3.json) | 造成的伤害+50%，受到的伤害-50% |
| `MDcFaBa` | **烧伤追加** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能使目标增加的烧伤 强度额外+1 |
| `MDcFaBb` | **流血追加** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能使目标增加的流血 强度额外+1 |
| `MDcFaBc` | **震颤追加** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能使目标增加的震颤 强度额外+1 |
| `MDcFaBd` | **破裂追加** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能使目标增加的破裂 强度额外+1 |
| `MDcFaBe` | **沉沦追加** | LLC 基准 (BattleKeywords_Mirror3.json) | 技能使目标增加的沉沦 强度额外+1 |
| `MDcFaBf` | **斩击强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 斩击伤害+15% |
| `MDcFaBg` | **突刺强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 突刺伤害+15% |
| `MDcFaBh` | **打击强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 打击伤害+15% |
| `MDcFbBa` | **罪孽抗性强化(除暴怒外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除暴怒属性外的罪孽抗性-0.1 |
| `MDcFbBb` | **罪孽抗性强化(除色欲外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除色欲属性外的罪孽抗性-0.1 |
| `MDcFbBc` | **罪孽抗性强化(除怠惰外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除怠惰属性外的罪孽抗性-0.1 |
| `MDcFbBd` | **罪孽抗性强化(除暴食外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除暴食属性外的罪孽抗性-0.1 |
| `MDcFbBe` | **罪孽抗性强化(除忧郁外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除忧郁属性外的罪孽抗性-0.1 |
| `MDcFbBf` | **罪孽抗性强化(除傲慢外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除傲慢属性外的罪孽抗性-0.1 |
| `MDcFbBg` | **罪孽抗性强化(除嫉妒外)** | LLC 基准 (BattleKeywords_Mirror3.json) | 除嫉妒属性外的罪孽抗性-0.1 |
| `MDcFbBh` | **体力上限提升** | LLC 基准 (BattleKeywords_Mirror3.json) | 体力上限+15% |
| `MDcFcBa` | **容量增加** | LLC 基准 (BattleKeywords_Mirror3.json) | 行动槽容量+1 |
| `MDcFcBb` | **伤害汲取** | LLC 基准 (BattleKeywords_Mirror3.json) | 命中时，恢复自身造成的伤害量5%的体力 |
| `MDcFcBc` | **速度增加** | LLC 基准 (BattleKeywords_Mirror3.json) | 最大速度值+1 |
| `MDcFcBd` | **精神攻击** | LLC 基准 (BattleKeywords_Mirror3.json) | 命中时，对目标造成2点理智伤害 |
| `MDcFcBe` | **锐利** | LLC 基准 (BattleKeywords_Mirror3.json) | 若上回合造成过伤害，回合开始时使自身获得1层伤害强化 。 |
| `MDcFcBf` | **重整旗鼓** | LLC 基准 (BattleKeywords_Mirror3.json) | 若上回合没有受到过体力伤害，回合开始时使自身获得3层攻击等级提升 。 |
| `MDcFcBg` | **单方面攻击强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 单方面攻击时，技能的最终威力+1 |
| `MDcFcBh` | **拼点攻击强化** | LLC 基准 (BattleKeywords_Mirror3.json) | 进行拼点时，技能的最终威力+1 |
| `MRR501` | **施加量折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 通过技能或硬币效果使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 |
| `MRR502` | **获得量折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 友方单位通过技能或硬币效果获得的呼吸法 与充能 层数额外+1层 |
| `MRR503` | **折射的理智** | LLC 基准 (BattleKeywords_Refraction5.json) | 回合结束时使理智值最低的3名友方单位恢复8点理智值(不包括陷入恐慌或侵蚀的友方单位) |
| `MRR504` | **버프 이름** | LLC 基准 (BattleKeywords_Refraction5.json) | 暴击时，若自身的呼吸法 强度高于20级，则消耗最多20级超出20级的呼吸法 强度并使自身暴击时造成的... |
| `MRR505` | **折射的充能** | LLC 基准 (BattleKeywords_Refraction5.json) | 消耗不低于8层充能 的技能命中时，本场战斗期间使目标的嫉妒抗性+0.1(每名敌方单位每个技能最多1次... |
| `MRR506` | **折射的爆发** | LLC 基准 (BattleKeywords_Refraction5.json) | 回合结束时，对全体敌方单位部位造成相当于其烧伤 强度的暴怒伤害，并使其烧伤 层数减少1层；使其震颤引... |
| `MRR507` | **折射的破裂** | LLC 基准 (BattleKeywords_Refraction5.json) | 增加破裂 强度或施加破裂 层数的技能最终威力+2 |
| `MRR508` | **折射的沉沦** | LLC 基准 (BattleKeywords_Refraction5.json) | 对理智值低于0点或未带有理智值的敌方单位造成的伤害+(目标的沉沦 强度)%(最多+45%) |
| `MRR509` | **弱点破坏** | LLC 基准 (BattleKeywords_Refraction5.json) | 对被破坏或陷入混乱的部位造成的伤害+30% |
| `MRR510` | **雾化吸入器** | LLC 基准 (BattleKeywords_Refraction5.json) | 波次的首个回合开始时，使全体友方单位增加5级呼吸法 强度并获得5层呼吸法 。激活傲慢共鸣时，战斗开始... |
| `MRR511` | **孤独的射手** | LLC 基准 (BattleKeywords_Refraction5.json) | 第1顺位友方单位的最小与最大速度值+1。该友方单位减少1个1技能，增加1个3技能 |
| `MRR512` | **延续斗志** | LLC 基准 (BattleKeywords_Refraction5.json) | 从第7顺位友方单位起，其解除待命的回合开始时，使其恢复30点理智值，本场战斗期间使其获得1层强壮 ，... |
| `MRR513` | **资源收获** | LLC 基准 (BattleKeywords_Refraction5.json) | 攻击或反击技能结束时，若击杀了敌方单位，则获得该技能对应的E.G.O资源2个(每个技能最多1次，包括... |
| `MRR514` | **버프 이름** | LLC 基准 (BattleKeywords_Refraction5.json) | 新的敌方单位增援时，战斗开始时使其增加5级流血 强度并对其施加3层流血 。若友方单位中存在<血魔>，... |
| `MRR515` | **顽强防御** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位受到的伤害-50% |
| `MRR516` | **生死决断** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位造成的伤害+30% |
| `MRR517` | **愤怒的反击** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位受到技能攻击时，下回合使其获得2层攻击等级提升 (最多6层) |
| `MRR518` | **追忆吊坠** | LLC 基准 (BattleKeywords_Refraction5.json) | 战斗开始时，使最先编入的3名友方单位增加10级呼吸法 强度 |
| `MRR519` | **버프 이름** | LLC 基准 (BattleKeywords_Refraction5.json) | 消耗弹药 的技能拼点威力+2，造成的伤害+(60/硬币数)%。若自身弹药 数为0发，则下回合开始时获... |
| `MRR520` | **凶弹倾泻** | LLC 基准 (BattleKeywords_Refraction5.json) | 友方单位阵亡时，对全体敌方单位的所有部位造成相当于该友方单位体力上限50%的固定伤害 |
| `MRR521` | **体力扭曲** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位的体力上限+25%，第一混乱阈值无效 |
| `MRR522` | **危险竞赛** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位技能的最终威力+1 |
| `MRR523` | **染血宴会** | LLC 基准 (BattleKeywords_Refraction5.json) | 命中时，若使敌方单位失去体力，则使自身恢复造成伤害量10%的体力。回合结束时，使全体友方单位的流血 ... |
| `MRR524` | **血之庆典** | LLC 基准 (BattleKeywords_Refraction5.json) | 友方单位每消耗10层血宴 ，使其所有技能造成的伤害+1%(最多+30%) |
| `MRR526` | **折射的斩击** | LLC 基准 (BattleKeywords_Refraction5.json) | 斩击技能的加算硬币威力+1，减算硬币威力-1 第3区段的最终头目的斩击抗性变为脆弱(×1.5) |
| `MRR527` | **折射的突刺** | LLC 基准 (BattleKeywords_Refraction5.json) | 突刺技能的加算硬币威力+1，减算硬币威力-1 第3区段的最终头目的突刺抗性变为脆弱(×1.5) |
| `MRR528` | **折射的打击** | LLC 基准 (BattleKeywords_Refraction5.json) | 打击技能的加算硬币威力+1，减算硬币威力-1 第3区段的最终头目的打击抗性变为脆弱(×1.5) |
| `MRR529` | **生长折射 I** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方等级 +1 |
| `MRR530` | **生长折射 II** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方等级 +2 |
| `MRR531` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 战斗中，增援的敌方单位在其增援的回合开始时获得2层拼点威力提升 |
| `MRR532` | **资源挥发** | LLC 基准 (BattleKeywords_Refraction5.json) | 觉醒E.G.O技能攻击结束后，按持有量由多到少消耗持有量多于1个的E.G.O资源1个，总计消耗2个 |
| `MRR533` | **绽放之血** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位通过技能或硬币效果使带有流血 的目标增加的流血 强度或对该目标施加的流血 层数额外+1 |
| `MRR534` | **顽强防御** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体敌方单位受到的伤害-20% |
| `MRR535` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位的体力上限-50% |
| `MRR536` | **折射的愤怒** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体敌方单位受到技能攻击时，下回合随机获得1层攻击等级提升 或1层防御等级提升 (每回合每名敌方单位... |
| `MRR537` | **体力折射 II** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的体力上限+20% |
| `MRR538` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位技能的最终威力+1 |
| `MRR539` | **染血宴会** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位通过技能或硬币效果恢复的体力+20% |
| `MRR540` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位消耗血宴 的技能最终威力+1，造成的伤害+10% |
| `MRR541` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体敌方单位以流血 强度最低的友方单位为主要目标时，使该敌方单位攻击时技能的最终威力+1 |
| `MRR542` | **体力折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的体力上限+10% |
| `MRR543` | **延续意志** | LLC 基准 (BattleKeywords_Refraction5.json) | 阵亡时，根据自身拥有的基础攻击技能的罪孽与级别，获得相应的E.G.O资源。 |
| `MRR544` | **威力轮盘赌** | LLC 基准 (BattleKeywords_Refraction5.json) | 回合开始时，使全体友方单位技能的最终威力+1~3 |
| `MRR545` | **玻璃大炮** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位造成的伤害+20% |
| `MRR546` | **高风险** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位造成的伤害+10% 第3区段的最终头目的斩击、突刺与打击抗性变为脆弱(×1.3) |
| `MRR547` | **威力轮盘赌** | LLC 基准 (BattleKeywords_Refraction5.json) | 回合开始时，使全体敌方单位技能的最终威力+1~3 |
| `MRR548` | **危险竞赛** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的拼点威力+2 |
| `MRR549` | **生死决断** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位的体力上限-25% |
| `MRR550` | **中等风险** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的加算硬币威力+1 |
| `MRR551` | **折射的流血** | LLC 基准 (BattleKeywords_Refraction5.json) | 回合开始时，使体力为最大值的敌方单位增加5级流血 强度并对其施加3层流血 (每场战斗每名敌方单位每个... |
| `MRR552` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位阵亡时，按现存体力由低到高在下回合使1名友方单位获得2层拼点威力提升 |
| `MRR553` | **一次呼吸** | LLC 基准 (BattleKeywords_Refraction5.json) | E.G.O技能造成的伤害+30% |
| `MRR554` | **增益名称** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位造成的伤害+15% |
| `MRR555` | **拼点威力折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的拼点威力+1 |
| `MRR556` | **玻璃大炮** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位受到的伤害+30% |
| `MRR557` | **折射的呼吸法** | LLC 基准 (BattleKeywords_Refraction5.json) | 暴击时造成的伤害+(10+自身的呼吸法 强度与层数之和)%(最多+50%) |
| `MRR558` | **折射的暴怒** | LLC 基准 (BattleKeywords_Refraction5.json) | 暴怒技能造成的伤害+30% 第3区段的最终头目的暴怒抗性变为脆弱(×1.25) |
| `MRR559` | **折射的色欲** | LLC 基准 (BattleKeywords_Refraction5.json) | 色欲技能造成的伤害+30% 第3区段的最终头目的色欲抗性变为脆弱(×1.25) |
| `MRR560` | **折射的怠惰** | LLC 基准 (BattleKeywords_Refraction5.json) | 怠惰技能造成的伤害+30% 第3区段的最终头目的怠惰抗性变为脆弱(×1.25) |
| `MRR561` | **折射的暴食** | LLC 基准 (BattleKeywords_Refraction5.json) | 暴食技能造成的伤害+30% 第3区段的最终头目的暴食抗性变为脆弱(×1.25) |
| `MRR562` | **折射的忧郁** | LLC 基准 (BattleKeywords_Refraction5.json) | 忧郁技能造成的伤害+30% 第3区段的最终头目的忧郁抗性变为脆弱(×1.25) |
| `MRR563` | **折射的傲慢** | LLC 基准 (BattleKeywords_Refraction5.json) | 傲慢技能造成的伤害+30% 第3区段的最终头目的傲慢抗性变为脆弱(×1.25) |
| `MRR564` | **折射的嫉妒** | LLC 基准 (BattleKeywords_Refraction5.json) | 嫉妒技能造成的伤害+30% 第3区段的最终头目的嫉妒抗性变为脆弱(×1.25) |
| `MRR565` | **安乐** | LLC 基准 (BattleKeywords_Refraction5.json) | 全体友方单位的最小与最大速度值+2，体力上限+25% |
| `MRR566` | **攻击性折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的拼点威力+1，造成的伤害+10% |
| `MRR567` | **高风险** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的加算硬币威力+2 |
| `MRR568` | **防御折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位的防御等级+3 |
| `MRR569` | **伤害折射** | LLC 基准 (BattleKeywords_Refraction5.json) | 敌方单位造成的伤害+10% |
| `MRR5BaseN` | **生效的苦难** | LLC 基准 (BattleKeywords_Refraction5.json) |  |
| `MRR5BaseP` | **生效的增益** | LLC 基准 (BattleKeywords_Refraction5.json) |  |
| `MRcAfBa` | **棉花** | LLC 基准 (BattleKeywords_Refraction3.json) | 若浸染棉花带有红染棉花 ，则回合结束时增加(棉花 层数/2)级流血 强度并施加相同层数流血 |
| `MRcAfBb` | **红染棉花** | LLC 基准 (BattleKeywords_Refraction3.json) | 回合开始时，攻击技能使目标增加的流血 强度与施加的流血 层数变为2倍。 若目标带有棉花 ，则使自身的... |
| `MRcAiBa` | **火种** | LLC 基准 (BattleKeywords_Refraction3.json) | 最多5层 获得火种时，将与自身火种 层数相同数量的非暴怒技能转化为暴怒技能 翅膀部位破坏时，对最后的... |
| `MRcAiBb` | **闪烁的火种** | LLC 基准 (BattleKeywords_Refraction3.json) | 最多5层 被特定技能攻击时施加点燃 。随后解除闪烁的火种 。 |
| `MRcAiBc` | **点燃** | LLC 基准 (BattleKeywords_Refraction3.json) | 战斗开始时，以速度为基准，使位于自身两侧的人格增加自身烧伤 强度的烧伤 强度 带有点燃 时无法获得火... |
| `MRcAmBa` | **轻蔑** | LLC 基准 (BattleKeywords_Refraction3.json) | 回合结束时，失去3个所选技能罪孽属性的E.G.O资源。 回合结束时，下回合对自身施加3层伤害弱化 。 |
| `MRcAmBb` | **掌** | LLC 基准 (BattleKeywords_Refraction3.json) | 最大值：3 处于无法行动状态 回合结束时，若本效果的层数不高于2层，则造成目标体力上限的一半的伤害。... |
| `MRcAmBbDisplay` | **掌** | LLC 基准 (BattleKeywords_Refraction3.json) | 最大值：3 处于无法行动状态 回合结束时，若本效果的层数不高于2层，则造成目标体力上限的一半的伤害。... |
| `MRcAmBc` | **视线** | LLC 基准 (BattleKeywords_Refraction3.json) | 每带有1层视线 ，造成的伤害+10% 回合结束时，若视线 层数为7层，则使自身增加15级流血 强度并... |
| `MRcAmBd` | **一览无余的视线** | LLC 基准 (BattleKeywords_Refraction3.json) | 回合结束时，本效果的层数增加1层。 带有视线 的人格在回合结束时，受到(4×层数)点固定体力伤害与(... |
| `MadFeather` | **眼羽** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 最大值：10 - 回合结束时，对自身施加(本效果层数/2)层破裂 与流血 (向下取整) - 回合... |
| `MadFeather_LowMorale` | **双刃羽** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 回合开始时，对自身施加1层易损 并使自身获得1层体力恢复提升 。自身的攻击命中时，使目... |
| `MadFeather_Panic` | **双刃羽** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 回合开始时，对自身施加2层易损 并使自身获得2层体力恢复提升 。自身的攻击命中时，使目... |
| `MagicalGirlAppear` | **魔法少女登场！** | LLC 基准 (BattleKeywords-walpu6.json) | - 本回合自身使用加算硬币技能作为基础攻击技能  - 自身每带有1级爱/憎 强度，使自身基础攻击技能... |
| `MagicalGirlResponse` | **魔法少女的咏唱** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：2 - 自身获得本效果时，使自身获得1层强壮 与1层伤害强化  - 自身获得或消耗充能 ... |
| `Malkuth_Imperfect` | **Malkuth的统治-不完全显现** | LLC 基准 (BattleKeywords-a1c9p2.json) | <i><color=#d3a562>虽不完整、但仍具统治王国之力的碎片</color></i> |
| `MarkOfButler` | **管·标** | LLC 基准 (BattleKeywords.json) | 目标带有本效果时强化埃德加家族 首席管家 良秀的技能 回合结束时，本效果减少1层 |
| `MarkOfHeresy` | **凝视** | LLC 基准 (BattleKeywords.json) | 本回合内受到来自突刺和打击技能的伤害+20%。友方单位击杀被本效果标记的敌方单位时，使该友方单位恢复... |
| `MatchesPersonality` | **燃烧** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+1 - 使本回合首个使用的基础攻击技能的最终威力+2 - 该技能命中时，使自身... |
| `MaxHpMultiplier` | **体力上限提升** | LLC 基准 (BattleKeywords.json) | 每层效果增加10%体力上限 |
| `MeatGearForce` | **血肉齿轮-强迫** | LLC 基准 (BattleKeywords-walpu5.json) | - 战斗中即使体力降至1点以下也不会阵亡 - 回合结束时，若自身的体力为1点，则自身阵亡 |
| `MeleeCover` | **近战支援** | LLC 基准 (BattleKeywords.json) | - 若A单位使B单位获得本效果，则在A单位的技能结束时，B单位使用技能“近战支援”对攻击A单位的敌方... |
| `MelodyBodyArt` | **以人体奏响的旋律** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+1 - 自身的基础攻击技能的拼点威力+1，造成的伤害+10% |
| `MelodyBodyArtChebello` | **以人体奏响的旋律[强化]** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+2 - 自身的基础攻击技能的拼点威力+2，造成的伤害+20% |
| `MentalCrack` | **精神裂痕** | LLC 基准 (BattleKeywords-walpu4.json) | 每层本效果使自身理智值减少效率 +1(最多+5) 层数为5层时解除并失去10点理智值 每回合使本效果... |
| `MentalIncreaseDown` | **理智值恢复效率减少** | LLC 基准 (BattleKeywords-a1c7p3.json) | 根据本效果的层数相应减少理智值恢复效率 |
| `MentalSystemResultDecrease_Typo` | **理智值减少效率** | LLC 基准 (BattleKeywords.json) | 人格基础理智值减少条件下的理智值减少量 |
| `MentalSystemResultIncrease_Typo` | **理智值恢复效率** | LLC 基准 (BattleKeywords.json) | 人格理智值增加条件下的理智值增加量 |
| `MeursaultBeeGunLong` | **黄蜂[步枪]** | LLC 基准 (BattleKeywords.json) | 现在的模式：黄蜂[步枪] |
| `MeursaultBeeGunShort` | **黄蜂[霰弹枪]** | LLC 基准 (BattleKeywords.json) | 现在的模式：黄蜂[霰弹枪] |
| `MeursaultBeeSpore` | **孢子** | LLC 基准 (BattleKeywords.json) | - 最大值：15 - 回合结束时，每带有5层本效果，对自身施加1层烧伤  - 下回合对自身施加1层束... |
| `MeursaultBuffet` | **嵌钉者** | LLC 2026092102／本地格式化 | - 本场战斗中，自身使用技能时，获得2个对应属性的E.G.O资源(每回合最多2次) - 回合开始时，若有其他友方单位在场，则本回合自身不会因受到伤害阵…… |
| `MeursaultSporeBulletLong` | **孢子弹[基础]** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 最大值：10 - 特定技能使用时消耗 - 若缺少弹药 ，部分攻击会取消 - 消耗并... |
| `MeursaultSporeBulletReloading` | **再次装填[孢子补充]** | LLC 基准 (BattleKeywords.json) | - 适用于孢子弹(特殊弹药)的效果 - 消耗((16-自身的孢子弹数之和)/2)点理智值，使自身的孢... |
| `MeursaultSporeBulletShort` | **孢子弹[霰弹]** | LLC 基准 (BattleKeywords.json) | - 特殊弹药 - 最大值：6 - 特定技能使用时消耗 - 若缺少弹药 ，部分攻击会取消 - 消耗并命... |
| `MeursaultWorkerBee` | **忠诚信息素** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合结束时，根据本效果层数，在下回合获得以下效果 不低于1层：1层守护  不低于... |
| `Meursault_Last_Remodeling` | **最终改造** | LLC 基准 (BattleKeywords.json) | 回合开始时，使自身获得3层强壮 、忍耐 和迅捷 。在3回合后阵亡。 |
| `MidFamilyOutis` | **家人的复仇** | LLC 基准 (BattleKeywords.json) | - 嫉妒基础技能造成的伤害+20% - 基础技能的最终威力+1 |
| `MiddleFatherGuts` | **过人的毅力** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 受到的伤害固定为1点(包括关键词伤害) - 拼点胜利时，额外恢复(拼点次数×5)点理智值(最多1... |
| `MiddleFatherGutsMirror` | **过人的毅力** | LLC 基准 (BattleKeywords_Mirror7.json) | - 受到的技能伤害-(50+自身已失去体力比例)%(向下取整)  - 拼点胜利时，额外恢复(拼点次数... |
| `MiddleFatherGutsOutis` | **过人的毅力** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 使自身高于一般(1.0)的物理抗性变为一般(1.0)(不包括陷入混乱) - 受到... |
| `MiddleFatherSwordFour` | **莱瓦汀** | LLC 基准 (BattleKeywords-a1c9p3.json) | 根据剑的状态可以使用特定技能。 回合开始时，使全体单位增加5级烧伤 强度并对其施加2层烧伤 |
| `MiddleFatherSwordFourOutis` | **莱瓦汀** | LLC 基准 (BattleKeywords.json) | - 回合开始时，使场上全体单位增加3级烧伤 强度 - 自身的基础技能替换为对应级别的莱瓦汀专用技能 ... |
| `MiddleFatherSwordOne` | **封印之剑** | LLC 基准 (BattleKeywords-a1c9p3.json) | 根据剑的状态可以使用特定技能。 |
| `MiddleFatherSwordOneOutis` | **封印之剑** | LLC 基准 (BattleKeywords.json) | - 回合结束时，下回合使自身获得2层迅捷  - 敌方单位每带有4级流血 强度，使自身打击基础技能造成... |
| `MiddleFatherSwordThree` | **2阶段 封印解除** | LLC 基准 (BattleKeywords-a1c9p3.json) | 根据剑的状态可以使用特定技能。 |
| `MiddleFatherSwordThreeOutis` | **2阶段 封印解除** | LLC 基准 (BattleKeywords.json) | - 回合结束时，下回合使自身获得1层迅捷 - 敌方单位的烧伤 强度与流血 强度之和每有4级，使自身打... |
| `MiddleFatherSwordTwo` | **1阶段 封印解除** | LLC 基准 (BattleKeywords-a1c9p3.json) | 根据剑的状态可以使用特定技能。 |
| `MiddleFatherSwordTwoOutis` | **1阶段 封印解除** | LLC 基准 (BattleKeywords.json) | - 回合结束时，下回合使自身获得1层迅捷 - 敌方单位的烧伤 强度与流血 强度之和每有4级，使自身打... |
| `MiddleFingerBook` | **中指的复仇对象** | LLC 基准 (BattleKeywords-a1c9116.json) | 最大值：10 受到中指攻击时，使自身受到的伤害+3%(最多+30%) |
| `MiddleFingerDaddy_LowMorale` | **狂怒** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 回合开始时，使自身获得2层强壮 并对自身施加4层防御等级降低 ； 上回合每受到30点体... |
| `MiddleFingerDaddy_Panic` | **狂怒** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 回合开始时，使自身获得3层强壮 并对自身施加5层防御等级降低 ； 上回合每受到25点体... |
| `MiddleFingerDaughter_LowMorale` | **狂热** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 回合开始时，对自身施加2层防御等级降低 ； 上回合每受到30点体力伤害，使自身获得1层... |
| `MiddleFingerDaughter_Panic` | **狂热** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 回合开始时，使自身获得1层强壮 并对自身施加3层防御等级降低 ； 上回合每受到25点体... |
| `MiddleFingerEzraSin` | **心-以斯拉** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础防御等级+2 - 基础攻击威力+1，守备威力+2 - 摩西每带有1层“深长吐息-红色”，使以... |
| `MiddleFingerLeashBuff` | **被抑制的力量** | LLC 基准 (BattleKeywords_Refraction6.json) | - 单方面攻击造成的伤害-100% - 回合结束时，若本场战斗中阵亡的友方单位数不低于3名，则解除本... |
| `MiddleFingerTattooID` | **仇怨纹身** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 每带有1层本效果，使自身基础技能造成的伤害+1% |
| `MineTheRings` | **作品名：提比娅** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，使自身获得4层威力提升 与2层斩击威力提升  - 攻击技能对目标施加流血 时，额外使... |
| `MiniDecontaminationKit` | **小帮手-迷你去污套组** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 溟痕 不再对友方单位造成伤害或施加神经损伤 |
| `MinusCoinValueDown` | **减算硬币弱化** | LLC 基准 (BattleKeywords.json) | 变动值为减算的技能硬币威力减少等同于本效果层数的数值。 |
| `MinusCoinValueUp` | **减算硬币强化** | LLC 基准 (BattleKeywords.json) | 变动值为减算的技能硬币威力提高等同于本效果层数的数值。 |
| `MlynarWaiting` | **鞘中人** | LLC 基准 (BattleKeywords.json) | - 最大值：40 - 每带有8层本效果，使自身的挑衅值 +1(最多+5，向下取整，适用于仪表盘上位于... |
| `MoonLight` | **月华** | LLC 基准 (BattleKeywords.json) | 特定技能发动附加效果所需的资源。 |
| `MosesMiddle_LowMorale` | **破损至无可挽回的身体** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 回合开始时，对自身施加1层易损 ，并使以斯拉与韦斯帕获得2层忍耐 |
| `MosesMiddle_Panic` | **破损至无可挽回的身体** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 回合开始时，对自身施加1层易损 ，并使用“调整呼吸” |
| `MosesPurpleBreathBind` | **紫色吐息-歇斯底里** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：4 - 回合结束时，使自身的体力与理智值减少等同于本效果层数的数值 - 回合结束时，使摩... |
| `MosesRedBreathAttack` | **红色吐息-疾驰的身体** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级增加5 - 基础技能的拼点威力+5 |
| `MosesRedBreathBody` | **红色吐息-身体强化** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级与防御等级+(自身的理智值/10)(向下取整) - 回合结束时，本效果的层数减少1层 |
| `MosesRedBreathCharge` | **深长吐息-红色** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：3 - <color=#ff6000><mark color=#ff000040><b>... |
| `MosesRedBreathShield` | **红色吐息-守护** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，本回合内使自身获得30点护盾 |
| `MosesSin` | **心-摩西** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 防御等级+3，守备威力+2 - 若通过技能效果使自身减少了理智值，则下回合使自身获得(理智值减少... |
| `MosesWarPTSD` | **那一日的记忆** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级-？？ - 基础防御等级-？？ - 回合开始时使自身获得5层迅捷 |
| `MosesWhiteBreathMental` | **白色吐息-精神守护** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 单位的基础理智值增加条件下的理智值恢复量增加5 - 单位的基础理智值减少条件下的理智值减少量减少... |
| `Muckworm` | **蛆虫** | LLC 基准 (BattleKeywords.json) | 回合结束时，受到数值等同于本效果层数的暴食伤害并施加1层流血 ，随后使本效果的层数减少1层。 |
| `MuscleContraction` | **肌纤维的机械性收缩与舒张** | LLC 基准 (BattleKeywords-a1c9p1.json) | 最大值：2 每带有1层本效果，使自身造成的伤害+15% 若本效果层数为2层，则战斗开始时使自身使用的... |
| `NEgoFleshSpatula_LowMorale` | **肉勺** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 士气低落 - 回合开始时，使自身增加5级流血 强度并使自身获得1层强壮 |
| `NEgoFleshSpatula_Panic` | **肉勺** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 陷入恐慌 - 回合开始时，使自身增加10级流血 强度并使自身获得2层强壮 |
| `Nail` | **N公司的尖钉** | LLC 基准 (BattleKeywords.json) | 回合开始时，增加1级流血 强度并施加与本效果层数相同的流血 层数。回合结束时，本效果的层数减少1层。 |
| `NailPersonality` | **尖钉** | LLC 基准 (BattleKeywords.json) | 特殊流血 回合开始时，增加1级流血 强度并获得与本效果层数相同的流血 层数。回合结束时，使本效果的层... |
| `NebulizerExhale` | **雾化吸入器α** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 本效果在本场战斗期间维持 - 战斗开始时，使包括自身在内全体友方单位增加1级呼吸... |
| `NebulizerInhale` | **雾化吸入器β** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 本效果在本场战斗期间维持 - 激活傲慢完全共鸣时，战斗开始时，使自身与(本效果层... |
| `Nervous` | **焦虑** | LLC 基准 (BattleKeywords.json) | 回合结束时，若自身的理智值不高于-15点，则下回合使自身获得5层防御等级提升 。 |
| `NervousImpairment` | **神经损伤** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 最大值：30 - 若本效果层数为30层，则使自身陷入混乱并受到体力上限25%的固定伤害，并解除本... |
| `NetherseaBrand` | **溟痕** | LLC 基准 (BattleKeywords-pilgrimage.json) | 每经过1回合，溟痕的影响范围会向罪人阵营扩散 - 1阶段：恐鱼阵营 - 2阶段：最靠前的2名罪人 -... |
| `NetherseaBrandUnit` | **溟痕** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 位于溟痕上的罪人在回合结束时受到体力上限5%的固定伤害并对其施加3层神经损伤 - 位于溟痕上的恐... |
| `NextHallway` | **群体迁移** | LLC 基准 (BattleKeywords-walpu8.json) | - 回合结束时，解除自身的混乱并从战斗中撤退 (不包括强制混乱，不视作阵亡) - 连续遭遇战中，将自... |
| `NiddleEGO` | **针** | LLC 基准 (BattleKeywords.json) | - 特殊流血 - 受到嫉妒伤害时，对自身施加1层流血 并使本效果的层数减少1层 - 回合结束时，使自... |
| `NiddleExpected` | **刺舌之针** | LLC 2026092102／本地格式化 | - 自身装备守备技能时  - 使自身的针钉 层数减少1层  - 解除本效果  - 回合结束时，对自身施加3层针钉 ，随后解除本效果 |
| `NiddlePin` | **针钉** | LLC 2026092102／本地格式化 | - 特殊流血 - 受到突刺伤害时，对自身施加1层流血 并使本效果层数减少1层 - 回合结束时，使自身增加1级流血 强度并使本效果层数减少1层 |
| `NiddlePinned` | **标本化** | LLC 2026092102／本地格式化 | - 最大值：2  - 受到攻击时，对自身施加1层流血 (每回合最多3次) - 带有本效果时，自身无法行动  - 回合结束时，失去15点体力，并使自身的…… |
| `NightDrifterGuilty` | **微弱的负罪感** | LLC 基准 (BattleKeywords-cultivation.json) | - 攻击等级-15 - 防御等级-15 |
| `NightPathfinding` | **杜拉罕** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 增加3级攻击等级 - 减少3级防御等级 - 最小与最大速度值+1 - 回合结束时... |
| `NoVillain` | **反转-逆位** | LLC 基准 (BattleKeywords-walpu6.json) | - 本回合自身使用减算硬币技能作为基础攻击技能 |
| `NoeulNageuneBuffA3` | **晚霞旅人的树液** | LLC 基准 (BattleKeywords_Refraction6.json) | - 自身的体力上限+50%(最多200点，不包括嫉妒罪种) - 移除自身的第一混乱阈值 |
| `NoeulNageuneBuffA4` | **晚霞旅人的树液** | LLC 基准 (BattleKeywords_Refraction6.json) | - 自身的体力上限+50%(最多200点，不包括嫉妒罪种) - 受到来自不可摧毁的硬币的伤害-20% |
| `NoeulNageuneBuffA5` | **晚霞旅人的树液** | LLC 基准 (BattleKeywords_Refraction6.json) | - 自身的体力上限+50%(最多200点，不包括嫉妒罪种) - 移除自身的第一混乱阈值 - 回合结束... |
| `NoeulNageuneBuffB3` | **晚霞旅人的蛾** | LLC 基准 (BattleKeywords_Refraction6.json) | - 回合开始时，场上每有1名与自身属于同一阵营的友方单位(包括自身)，使自身获得1层攻击等级提升 (... |
| `NoeulNageuneBuffB4` | **晚霞旅人的蛾** | LLC 基准 (BattleKeywords_Refraction6.json) | - 每回合随机使自身获得1层某1种随机效果，该效果可能为斩击伤害强化 、突刺伤害强化 或打击伤害强化... |
| `NoeulNageuneBuffB5` | **晚霞旅人的蛾** | LLC 基准 (BattleKeywords_Refraction6.json) | - 回合开始时，本场战斗中每有1名阵亡的友方单位，使自身获得1层攻击等级提升 (最多6层) - 战斗... |
| `NoirBindArmor` | **黑派 精纺面料** | LLC 2026092102／本地格式化 | - 最大值：15 - 每带有5层本效果，最大速度值-1，攻击等级+1，防御等级+1 - 回合结束时，本效果的层数减少1层 |
| `NoirNoComply` | **违反规定** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，受到的伤害+5% |
| `NoirSuit` | **黑派 华达呢大衣** | LLC 2026092102／本地格式化 | - 最大值：100 - 回合开始时，每带有20层本效果，使自身获得1层防御等级提升 (最多4层) - 自身通过技能或被动效果消耗或获得保存 层数时，获…… |
| `NoirSuitAlly` | **黑派华达呢大衣** | 工作区 (BattleKeywords.json) | - 最大值：100 - 每25点，防御等级+1 - 最左侧技能槽的嘲讽值+5 - 拥有护盾时受击，增... |
| `Nutrition` | **夺来的某物。** | LLC 2026092102／本地格式化 | - 最大值：5 - 回合结束时，下回合使自身获得(本效果层数×2)层搏动 ，随后解除本效果 - 若本效果解除时层数为最大值，则下回合使自身所有部位获得…… |
| `ObedienceGregBigBird` | **森林的守望者** | LLC 基准 (BattleKeywords.json) | 攻击前，触发以下效果 - 若为加算硬币技能，则使自身恢复4点理智值(通过该效果恢复理智值时，若理智值... |
| `Obedient` | **空虚的顺从** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 与贾母进行拼点时，使自身的拼点威力-2 - 自身的理智值达到45点或本效果层数为0层时解除 - ... |
| `ObjectOfExploration` | **探究对象** | LLC 基准 (BattleKeywords_Mirror7.json) | 满足特定条件时，转化为“绘画材料” |
| `ObservationMoses` | **观察力** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 不会成为魅惑 的目标 - 对精灵部位造成的伤害+25% |
| `ObservationTheRings` | **眺望** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 基础攻击等级-20 - 基础防御等级-20 - 罪人与援助单位的撤退机制不会生效 - 若环指 子... |
| `ObservationTheRingsHidden` | **眺望** | LLC 基准 (BattleKeywords_Mirror7.json) | - 基础攻击等级-20 - 基础防御等级-20 - 若环指 子辈处于可战斗状态，则使自身受到的最终伤... |
| `ObservationTheRingsRail` | **眺望** | LLC 基准 (BattleKeywords_Refraction6.json) | - 基础攻击等级-20 - 基础防御等级-20 - 若环指 子辈处于可战斗状态，则回合开始时使自身获... |
| `ObservedPerson` | **观察对象** | LLC 基准 (BattleKeywords-a1c971.json) | - 最大值：30 - 回合开始时获得3层本效果(获得本效果的下回合起生效) - 自身受到扭曲的霍恩海... |
| `ObsessedTeacher_LowMorale` | **家族之耻** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，使自身获得1层斩击伤害强化 与1层拼点威力提升 ，并对自身施加1层易损  - 使用技... |
| `ObsessedTeacher_Panic` | **家族之耻** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，使自身获得2层斩击伤害强化 与2层拼点威力提升 ，并对自身施加2层易损  - 使用技... |
| `ObsessionAndGreed` | **心-瓦伦希娜** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 上回合自身每拼点失败1次，使自身防御等级+3(最多+6) 自身的呼吸法 强度每有1级，使自身造成... |
| `ObsessionAndGreedRodion` | **心-不光彩** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+1 - 令自身基础技能增加的震颤 强度与烧伤 强度，施加的震颤 层数与烧伤 层... |
| `OffenseBug` | **攻击害虫[蜚蠊]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：50 - 本效果层数每有1层，体力上限减少1% - 战斗开始时，受到(本效果层数×12)... |
| `OminousTalisman` | **不祥符咒** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 最大值：10 - 若本效果层数为0层，则受到相当于自身破裂 强度的暴食伤害与理智伤害并解除本效果... |
| `OneDropNutrition` | **一滴养分** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：10 - 每通过攻击恢复体力上限10%的体力，使自身获得1层本效果 - 显示已恢复体力的... |
| `OneOnOneDuel` | **单挑决斗** | LLC 基准 (BattleKeywords.json) | 在目标行动槽仅被一个单位指向时触发。仅在目标行动槽与指向目标行动槽的攻击技能之间构成单挑决斗 。(重... |
| `Operation` | **手术** | LLC 基准 (BattleKeywords.json) | 在层数达到5层时直接阵亡。 每层减少20%体力上限。 每层增加20%造成的伤害。 回合开始时，使自身... |
| `OutisNoHat` | **强力征收执行** | LLC 基准 (BattleKeywords-tkt-re.json) | - 自身带有迅捷时，令自身基础技能对自身施加的震颤 层数额外+1层 - 若自身的速度值高于目标，则使... |
| `OutpouringAnger` | **挣扎** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 若技能“尔等尚不知那眼瞳之力与奇特之处吧”的主要目标为鸿璐，则无视技能效果使该技能的所有硬币转化... |
| `OverHeatedGasHarpoon` | **过热的燃气捕鲸叉** | LLC 基准 (BattleKeywords.json) | 1回合内，攻击命中时使目标增加1级烧伤 强度 |
| `Overwhelm_LowMorale` | **无措(士气低落)** | LLC 基准 (Bufs.json) | - 士气低落 - 回合开始时，施加2层虚弱 。 |
| `Overwhelm_Panic` | **无措** | LLC 基准 (Bufs.json) | - 陷入恐慌 - 本回合内无法行动。 |
| `OwnTime` | **共享的时间** | LLC 基准 (BattleKeywords-tkt.json) | - 回合开始时，若层数不低于40层，则使自身获得(层数-40)/10层攻击等级提升 与防御等级提升 ... |
| `PainfulScarRailway_LowMorale` | **仿造的父辈** | LLC 基准 (BattleKeywords_Refraction6.json) | - 士气低落 - 回合开始时，使自身增加5级烧伤 强度与5级流血 强度 |
| `PainfulScarRailway_Panic` | **仿造的父辈** | LLC 基准 (BattleKeywords_Refraction6.json) | - 陷入恐慌 - 回合开始时，使自身增加5级烧伤 强度与5级流血 强度并对自身施加3层烧伤 与3层流... |
| `PainfulScar_LowMorale` | **仿造的父辈** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 回合开始时，使自身增加5级烧伤 强度与5级流血 强度 - 受到罪人良秀造成的伤害+... |
| `PainfulScar_Panic` | **仿造的父辈** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 回合开始时，使自身增加5级烧伤 强度与5级流血 强度并对自身施加3层烧伤 与3层流... |
| `PaintingMaterial` | **绘画材料** | LLC 基准 (BattleKeywords_Mirror7.json) | 若自身带有流血 (集中遭遇战中各部位单独计算)，则使自身受到来自色欲技能的伤害+10% |
| `PanicChangeLock` | **固定恐慌** | LLC 基准 (BattleKeywords-twth.json) | 被施加改变恐慌类型的状态时，自身的恐慌类型不会改变。效果改为对未带有理智值的单位施加的效果。 |
| `ParadeConcentration` | **拉·曼却游行** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 使自身受到来自色欲技能的伤害+10% · 若目标为属于<拉·曼却领>的人格，则无... |
| `Paralysis` | **麻痹** | LLC 基准 (BattleKeywords.json) | 一回合内使硬币的变动值固定为0。每层影响1枚硬币。 |
| `ParryingResultDown` | **拼点威力降低** | LLC 基准 (BattleKeywords-tkt.json) | 拼点时，拼点威力减少等同于本效果层数的数值 |
| `ParryingResultUp` | **拼点威力提升** | LLC 基准 (BattleKeywords-tkt.json) | 拼点时，拼点威力增加等同于本效果层数的数值 |
| `ParticipationMod` | **临战状态** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 受到伤害时，进入使用攻击技能的状态 - 回合开始时若处于临战状态，则 · 对全体敌方单位施加3层... |
| `PassedPortal_Blue` | **电流涌动的次元** | LLC 基准 (BattleKeywords_Refraction2.json) | 硬币威力+1 |
| `PassedPortal_Green` | **剧毒沸腾的次元** | LLC 基准 (BattleKeywords_Refraction2.json) | 体力上限提升20% |
| `PassedPortal_GreenBokGak` | **剧毒沸腾的次元** | LLC 基准 (BattleKeywords-Refraction2BokGak.json) | 本体体力上限增加20% |
| `PassedPortal_Red` | **血流成河的次元** | LLC 基准 (BattleKeywords_Refraction2.json) | 造成的伤害+10% |
| `PassedPortal_Yellow` | **震颤不止的次元** | LLC 基准 (BattleKeywords_Refraction2.json) | 最小与最大速度值+1 |
| `PenanceFirst` | **忏悔** | LLC 基准 (BattleKeywords-walpu4.json) | - 基础技能获得忏悔 的硬币命中时，使自身恢复2点理智值 - 最大值：20 - 特殊充能(固定强度)... |
| `PenanceSecond` | **忏悔-警戒** | LLC 基准 (BattleKeywords-walpu4.json) | - 基础技能获得忏悔 的硬币命中时，使自身恢复4点理智值 - 最大值：20 - 特殊充能(固定强度)... |
| `PenanceThird` | **忏悔-告解** | LLC 基准 (BattleKeywords-walpu4.json) | - 基础技能获得忏悔 的硬币命中时，使自身恢复6点理智值 - 最大值：20 - 特殊充能(固定强度)... |
| `PenetrateDamageDown` | **突刺伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低突刺技能造成的伤害。(最多10层) |
| `PenetrateDamageUp` | **突刺伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高突刺技能造成的伤害。(最多10层) |
| `PenetrateResistDown` | **突刺抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的突刺抗性增加(每层0.1) |
| `PenetrateResistUp` | **突刺抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的突刺抗性减少(每层0.1) |
| `PenetrateResultDown` | **突刺威力降低** | LLC 基准 (Bufs.json) | 本回合内突刺技能的最终威力-{0} |
| `PenetrateResultUp` | **突刺威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高突刺技能的最终威力。 |
| `PenetrateTakeDamageDown` | **突刺守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自突刺技能的伤害。(最多10层) |
| `PenetrateTakeDamageUp` | **突刺易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自突刺技能的伤害。(最多10层) |
| `PenetratingSword` | **穿刺之剑** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，每带有1层本效果，使自身获得1层攻击等级提升 (最多5层) - 回合开始时，使自身所... |
| `Penetration` | **正在凝固的血** | LLC 基准 (BattleKeywords-a1c7p3.json) | 2回合内无法行动，生成友方单位贯穿之枪 |
| `Perfected` | **完整外壳** | LLC 基准 (Bufs.json) | 回合开始时，使手臂获得2层强壮 。若手臂的体力低于50%，则解除本效果。 |
| `Persistent` | **坚韧** | LLC 基准 (BattleKeywords-a1c9116.json) | 最大值：4 受到使体力降至0点的伤害时，以80%的概率不会受到伤害并使自身恢复60点体力，解除自身的... |
| `PhantomIncision` | **剑痕[残像]** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 最大值：99 - 回合开始时，每带有10层本效果，对自身施加1层易损 (最多5层) |
| `PhantomIncisionID` | **剑痕[残像]** | LLC 基准 (BattleKeywords.json) | - 最大值：100 - 每带有10层本效果，使自身受到的斩击伤害+1% |
| `PhantomIncisionTotal` | **地慧星刀** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 本场战斗的剑痕[残像] 层数之和 |
| `PhantomIncisionTotalID` | **地慧星刀** | LLC 基准 (BattleKeywords.json) | - 最大值：70 - 自身施加的剑痕层数之和 - 每回合最多获得25层本效果 |
| `PhotoElectricity` | **光电** | LLC 基准 (BattleKeywords.json) | 最大值：3 自身受到攻击时，使攻击者获得层数相当于本效果层数的充能 (每个技能最多1次) - 若攻击... |
| `PhotoTransition` | **记忆转换** | LLC 基准 (BattleKeywords-exme.json) | - 基础值：3 - 回合结束时，本效果层数减少1层。回合开始时若本效果层数为0层，则改变特定单位与效... |
| `PhotoTransitionChoi` | **记忆转换** | LLC 基准 (BattleKeywords-exme.json) | - 基础值：3 - 回合结束时，本效果层数减少1层 - <color=#ff6000><mark c... |
| `PhotoTransitionChoiCamera` | **记忆转换** | LLC 基准 (BattleKeywords-exme.json) | - 基础值：3 - 回合结束时，本效果层数减少1层 - <color=#ff6000><mark c... |
| `PileObedient` | **积累的顺从** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合结束时，若本效果层数为3层，则下回合使本效果转化为空虚的顺从 |
| `PinkPetals` | **粉红花瓣** | LLC 基准 (BattleKeywords-walpu8.json) | - 最大值：30 - 每带有1层本效果，使自身受到忧郁技能的伤害+1%(最多+15%) - 每带有1... |
| `PinkRibbon` | **粉红丝带** | LLC 基准 (BattleKeywords.json) | 回合结束时，若本效果的层数不低于5层，则解除本效果并在下回合施加渴望 。 |
| `PinkRibbon_Ishmael` | **粉红丝带** | LLC 基准 (BattleKeywords.json) | 本回合内，每次掷出攻击技能硬币时使本效果的层数增加1层。 回合结束时，施加与本效果层数相同的束缚 ，... |
| `PlayingWithWaterTogetherMirror` | **拍拍** | LLC 基准 (BattleKeywords_Mirror7.json) | - 最大值：10 - 与断首鱼进行拼点时，触发以下效果(每个技能最多1次)  · 使自身与目标增加相... |
| `PlusCoinValueDown` | **加算硬币弱化** | LLC 基准 (BattleKeywords.json) | 变动值为加算的技能硬币威力减少等同于本效果层数的数值。 |
| `PlusCoinValueUp` | **加算硬币强化** | LLC 基准 (BattleKeywords.json) | 变动值为加算的技能硬币威力提高等同于本效果层数的数值。 |
| `Poison` | **剧毒** | LLC 基准 (BattleKeywords.json) | 回合结束时，受到数值等同于本效果层数的固定伤害，随后使本效果的层数减半。 |
| `PowerOfLoveAndJustice` | **爱/正义** | LLC 基准 (BattleKeywords-walpu6.json) | - 每带有1级本效果强度，令自身增加的破裂 强度额外+1级 |
| `Precarious` | **不负责任的梦** | LLC 基准 (BattleKeywords-a1c7p3.json) | 被堂吉诃德命中时阵亡。 |
| `Predation` | **捕食** | LLC 基准 (BattleKeywords.json) | 似乎在准备使用强力的技能。 |
| `PrepareSinRose` | **冠冕** | LLC 基准 (BattleKeywords_Refraction2.json) | 生成被施加本效果的目标拥有的最多的技能对应罪孽属性的玫瑰单位 - 若该效果生成的玫瑰高于7朵，则移除... |
| `PreparedMeat` | **储备粮** | LLC 基准 (BattleKeywords.json) | 若满足条件，则回合结束时精灵女王击杀该单位 |
| `PressureOfPrescript` | **压迫感** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 每带有1层本效果，使自身造成的伤害+25%(最多+50%) - 若处于绽放E.G.O::代行状态... |
| `PressureOfPrescript_2nd` | **强烈的压迫感** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 每带有1层本效果，使自身造成的伤害+50%(最多+100%) - 若处于绽放E.G.O::代行状... |
| `Prey` | **猎物** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 与敌方单位进行拼点时，自身的拼点威力-5 - 战斗开始时 · 若装备了攻击技能，则使自身的攻击技... |
| `Prey_leiheng` | **猎物** | 工作区 (BattleKeywords-BossRaid.json) | - 与敌方进行拼点时，拼点威力-5 - 战斗开始时， · 若装备了攻击技能，则使用攻击技能对雷横造成... |
| `PriceOfCare` | **难以餍足** | LLC 基准 (Bufs.json) | 吃掉的精灵的碎块的数量：{0} |
| `ProtectStance` | **守护姿态** | LLC 基准 (BattleKeywords-a1c8p2.json) | 最大值：2 本效果的层数不会叠加，获得层数时改为刷新本效果 回合结束时，使本效果的层数减少1层 单位... |
| `ProtectStanceRyoshu` | **护卫姿态** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 受到的伤害-(本效果层数×10)% - 回合开始时，使自身获得相当于自身呼吸法 ... |
| `Protection` | **守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自技能的伤害。(最多10层) |
| `ProtectiveSword` | **守护之剑** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，每带有1层本效果，使自身获得1层防御等级提升 (最多5层) - 回合开始时，使仪表盘... |
| `Prowl_LowMorale` | **徘徊** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 回合结束时，友方单位失去2点理智值。 |
| `Prowl_Panic` | **徘徊** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 3回合内，每回合结束时友方单位失去5点理智值。3回合结束后逃离战斗。 |
| `PseudoLastBoss_KingCrap` | **蟹·愤** | LLC 基准 (BattleKeywords.json) | 每回合开始时，使除自身以外的全体螃蟹友方单位获得1层强壮 ，若外壳未被破坏，则使自身获得2层守护 。... |
| `PumpkinJelly` | **橙子味的噗扭扭** | LLC 基准 (BattleKeywords-walpu8.json) | - 最大值：1 回合开始时，若现存体力低于体力上限的60%，则使自身恢复体力上限30%的体力并解除本... |
| `QiuAndHonglu` | **我的本心…** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 鸿璐的所有技能最终威力+1 - 拼点胜利时，使理智值最低的1名友方单位(包括自身)恢复5点理智值... |
| `Qiu_LowMorale` | **贾丘** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 - 对除鸿璐以外的目标造成的伤害+10% |
| `Qiu_Panic` | **贾丘** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 - 对除鸿璐以外的目标造成的伤害+20% |
| `QueenBeeMark` | **信息素标记** | LLC 基准 (BattleKeywords-walpu8.json) | - 自身每带有3级烧伤 强度，使自身受到的伤害+1%(最多+20%) - 回合结束时解除本效果 |
| `QueenBeepheromone` | **信息素** | LLC 基准 (BattleKeywords-walpu8.json) | - 挑衅值 +10 - 受到攻击时，使目标增加3级烧伤 强度 |
| `RageResonance` | **紧握的暴怒** | LLC 基准 (BattleKeywords-a1c6p3.json) | 回合结束时，下回合使自身获得{0}层攻击等级提升 (本效果每回合都会强化) |
| `RailBuffForLine2_A_ALLY` | **斩击强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_A_ENEMY` | **巡回** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_B_ALLY` | **突刺强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_B_ENEMY` | **机会主义** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_C_ALLY` | **打击强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_C_ENEMY` | **硬化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_D_ALLY` | **暴怒强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_D_ENEMY` | **加速** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_E_ALLY` | **色欲强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_E_ENEMY` | **吸血** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_F_ALLY` | **怠惰强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_F_ENEMY` | **饥渴** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_G_ALLY` | **暴食强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_H_ALLY` | **忧郁强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_I_ALLY` | **傲慢强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_J_ALLY` | **嫉妒强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_K_ALLY` | **全体恢复** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_L_ALLY` | **选择恢复** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_M_ALLY` | **烧伤强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_N_ALLY` | **流血强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_O_ALLY` | **震颤强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_P_ALLY` | **破裂强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_Q_ALLY` | **沉沦强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_R_ALLY` | **呼吸法强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_S_ALLY` | **充能强化** | LLC 基准 (Bufs.json) |  |
| `RailBuffForLine2_T_ALLY` | **复活** | LLC 基准 (Bufs.json) |  |
| `RailLine2Buff` | **折射** | LLC 基准 (Bufs_Refraction2.json) |  |
| `RapidGrowthApple` | **急速生长** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：3 - 每带有1层本效果，部位的防御等级-1(防御等级最低为1) - 所有手臂部位被破坏... |
| `ReCompulsion` | **反转强迫** | LLC 基准 (BattleKeywords.json) | 每回合开始时，使自身恢复15点理智值 |
| `RealPaperBear` | **真正的熊** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 这头可怕的熊连人都吃 |
| `Realisation` | **织纹觉醒** | LLC 2026092102／本地格式化 | - 最大值：100 - 回合开始时，每带有10层本效果，使自身恢复5点理智值 - 回合开始时，每带有20层本效果，使自身获得1层攻击等级提升 与1层防…… |
| `RealisationAlly` | **觉醒之铠** | 工作区 (BattleKeywords.json) | - 最大值：100 - 最小速度+2，最大速度+2 - 每25点，攻击等级+1，防御等级+1 - 所... |
| `ReattachedCurseTag` | **复贴的咒符** | LLC 基准 (BattleKeywords.json) | 若层数不低于9层，则在回合开始时对自身施加5层束缚 。 若层数不低于12层，则在回合开始时对自身施加... |
| `ReattachedCurseTag_Re` | **复贴的咒符** | LLC 基准 (BattleKeywords_Refraction2.json) | - 最大值：12 - 若本效果层数不高于8层，则使自身造成的伤害+30% - 若本效果层数不低于9层... |
| `ReboundWei` | **反冲力** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：5 |
| `RecklessDuel` | **鲁莽的决斗** | LLC 基准 (BattleKeywords-a1c7p1.json) | 回合结束时，自身每失去10%的体力，下回合使自身获得1层拼点威力提升 (最多5层) 回合结束时，自身... |
| `RedApricotBlossom` | **红梅** | LLC 基准 (BattleKeywords.json) | - 特殊流血 - 最大值：10 - 若自身为主要目标，被暴击率+10% - 被暴击时使自身增加本效果... |
| `RedButterfly` | **撕裂而出之蝶** | LLC 基准 (BattleKeywords_Mirror7.json) | - 所有技能的最终威力+2 - 因受到伤害而陷入混乱时，立即解除自身的混乱并使自身获得体力上限100... |
| `RedEyeFirst` | **赤瞳** | LLC 基准 (BattleKeywords-walpu4.json) | 基础技能硬币效果增加的流血 强度额外+1级 - 最大值：20 - 特殊充能(固定强度) - 特定技能... |
| `RedEyeSecond` | **赤瞳-警戒** | LLC 基准 (BattleKeywords-walpu4.json) | 基础技能硬币效果增加的流血 强度额外+2级 - 最大值：20 - 特殊充能(固定强度) - 特定技能... |
| `RedEyeThird` | **赤瞳-捕食** | LLC 基准 (BattleKeywords-walpu4.json) | 基础技能硬币效果增加的流血 强度额外+3级 - 最大值：20 - 特殊充能(固定强度) - 特定技能... |
| `RedemptionTheRings` | **材料脱落的伤口** | LLC 基准 (BattleKeywords-a1c9p3.json) | 使用技能时，对自身施加2层攻击等级降低 (每回合最多3次) |
| `Reduction` | **虚弱** | LLC 基准 (BattleKeywords.json) | 一回合内攻击技能的最终威力减少等同于本效果层数的数值。 |
| `RefractedWill` | **折射的意志** | LLC 基准 (BattleKeywords_Refraction4.json) | 友方单位阵亡时，基础理智值减少条件下的理智值减少量减半。(向下取整) |
| `Refraction4A` | **第1顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 人格等级+2 |
| `Refraction4B` | **第2顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 理智值恢复效率 +3 起始理智值+10点 |
| `Refraction4C` | **第3顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 攻击等级+2 |
| `Refraction4D` | **第4顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 防御等级+2 |
| `Refraction4E` | **第5顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 最大速度值+2 |
| `Refraction4F` | **第6顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 体力上限+5% |
| `Refraction4G` | **第7顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 拼点威力+1 起始理智值+15点 |
| `Refraction4H` | **第8顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 受到的伤害-10% 起始理智值+15点 |
| `Refraction4I` | **第9顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 挑衅值 +5 起始理智值+20点 |
| `Refraction4J` | **第10顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 造成的伤害+10% 起始理智值+20点 |
| `Refraction4K` | **第11顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 最终威力+1 起始理智值+30点 |
| `Refraction4L` | **第12顺位效果** | LLC 基准 (BattleKeywords_Refraction4.json) | 人格等级+3 起始理智值+30点 |
| `RegainedStrength` | **复还的血之冲动** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：10 - 复还的血之冲动 1阶段 |
| `RegainedStrength_2nd` | **复还的血之冲动II** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：20 - 复还的血之冲动 2阶段 - 回合开始时，每带有5层本效果，使自身获得1层攻击等... |
| `RegainedStrength_3rd` | **复还的血之冲动III** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：30 - 复还的血之冲动 3阶段 - 回合开始时，每带有5层本效果，使自身获得2层攻击等... |
| `RegretSCorp` | **刺痛的记忆** | LLC 基准 (BattleKeywords-exme.json) | - 最大值：1 - 回合结束时，下回合对自身施加1层束缚  - 回合结束时，下回合使自身获得(当前回... |
| `ReinforcedAssemble` | **克罗默的哨音** | LLC 基准 (Bufs.json) | 执柄者与吾等同在，吾等无所畏惧。 |
| `ReinforcedTattooIshmael` | **中指式强化纹身** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 每带有5层本效果，使自身基础技能的最终威力+1(最多+2) - 每带有1层本效... |
| `ReinforcedTattooSpider` | **中指-仇怨纹身[<s>长兄</s>]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：2 - 回合结束时解除 - 造成的打击与嫉妒伤害+10% |
| `ReinforcedTattooSpiderDaughter` | **中指式强化纹身** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：3 - 回合结束时解除 - 造成的打击与嫉妒伤害+10% |
| `ReinforcedTattooSpiderDaughterTwo` | **<s>中指式</s>强化纹身** | LLC 基准 (BattleKeywords-twth.json) | - 最大值：3 - 造成的打击与嫉妒伤害+10% |
| `ReinforcedTattooSpiderOutis` | **中指-仇怨纹身[<s>长姊</s>]** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 每带有5层本效果，使自身基础技能的最终威力+1(最多+2) - 每带有1层本效... |
| `ReleaseBreath` | **急促喘息** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 若自身的呼吸法 强度不低于20级，则通过自身的技能或硬币效果使自身增加呼吸法 强... |
| `ReliefSense` | **感谢聆听** | LLC 2026092102／本地格式化 | - 最大值：3 - 回合开始时，本效果层数增加1层，并使自身恢复10点理智值 - 使自身技能对本关卡头目造成的伤害+(本效果层数×50)%，该技能攻击…… |
| `ReloadKeepAmmo` | **再次装填-余弹维持** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 自身再次获得弹药至最大值(不会丢弃剩余的弹药) |
| `ReloadLament` | **再次装填** | LLC 基准 (BattleKeywords-walpu4.json) | - 适用于生蝶·亡蝶 (特殊弹药)的效果 - 消耗((30-自身带有的生蝶与亡蝶之和)/2)点理智值... |
| `RemoveBreakSection` | **坚韧不拔** | LLC 基准 (Bufs.json) | 友方人格的第一混乱阈值无效 |
| `RepressedMurderousIntend` | **压抑的杀气** | LLC 基准 (BattleKeywords-a1c9116.json) | 基础攻击等级-10，基础防御等级-10 |
| `RepressedMurderousIntendHard` | **压抑的杀气** | LLC 基准 (BattleKeywords-night-clean-up-re.json) | 基础攻击等级-5，基础防御等级-5 |
| `RepressedMurderousIntendTwo` | **抑制杀气** | LLC 基准 (BattleKeywords-a1c8p2.json) | 基础攻击等级减少5级 基础防御等级减少5级 |
| `RequestedTarget` | **委托目标** | LLC 基准 (BattleKeywords.json) | 斩击、突刺与打击抗性中不高于1.5的抗性+0.2。击杀带有本效果的目标时，获得所有属性的E.G.O资... |
| `Resentment` | **仇怨** | LLC 基准 (BattleKeywords.json) | 击中带有<sprite name="RetaliationBook"><color=#e30000>... |
| `ResentmentIshmael` | **中指-仇怨** | LLC 基准 (BattleKeywords.json) | - 最大值：15 - 若目标带有报复对象 ，则使自身造成的伤害+20% |
| `ResentmentSpider` | **中指-仇怨** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 特定技能使用时消耗 - 本效果层数每有1层，攻击等级+1，防御等级-2，反击技... |
| `ResentmentSpiderDaughter` | **中指-仇怨** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 特定技能使用时消耗 - 本效果层数每有1层，攻击等级+1，防御等级-2，反击技... |
| `ResentmentSpiderDaughterTwo` | **<s>中指</s>-仇怨** | LLC 基准 (BattleKeywords-twth.json) | - 最大值：10 - 特定技能使用时消耗 - 本效果层数每有1层，攻击等级+1，防御等级-2，反击技... |
| `ResentmentSpiderOutis` | **中指-仇怨** | LLC 基准 (BattleKeywords.json) | - 最大值：15 - 若目标带有报复对象 ，则使自身造成的伤害+20% |
| `Resonate` | **共振** | LLC 基准 (BattleKeywords.json) | 使目标震颤引爆 或前移混乱阈值时，每层额外造成3点伤害，并使混乱阈值前移3%。 |
| `RestingKimSatgat_LowMorale` | **沉溺的悔恨** | LLC 基准 (BattleKeywords-exme.json) | - 士气低落 - 回合开始时，对自身施加2层伤害弱化 并使自身恢复40点体力 |
| `RestingKimSatgat_Panic` | **沉溺的悔恨** | LLC 基准 (BattleKeywords-exme.json) | - 陷入恐慌 - 回合开始时，对自身施加3层伤害弱化 并使自身恢复60点体力 |
| `RestoredBattleSense` | **极力** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 最大值：50 - 视作底力 ，特定技能使用时消耗，该回合结束时，使自身恢复相当于消耗量的理智值 ... |
| `ResultEnhancement` | **威力提升** | LLC 基准 (BattleKeywords.json) | 一回合内技能的最终威力提升等同于本效果层数的数值。 |
| `ResultReduction` | **威力降低** | LLC 基准 (BattleKeywords.json) | 一回合内技能的最终威力降低等同于本效果层数的数值。 |
| `RetaliationBook` | **报复对象** | LLC 基准 (BattleKeywords.json) | 施加给上回合内对单个友方单位造成技能伤害最多的敌方单位(最多1次) |
| `RetaliationBookFamily` | **兄弟姐妹们的报复对象** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 回合结束时，解除本效果 - 视作所有人格的报复对象 |
| `RetaliationBookSpiderOutis` | **复仇账簿[蜘蛛巢]** | LLC 基准 (BattleKeywords.json) | - 蜘蛛巢 中指 父辈 奥提斯或蜘蛛巢 中指 子辈 以实玛利技能命中带有本效果的单位时，使攻击者恢复... |
| `Retreat` | **战略性休息福利模式** | LLC 基准 (BattleKeywords.json) | - 回合结束时，解除自身的混乱并从战斗中撤退(不包括强制混乱，不视作阵亡) · 连续遭遇战中，将自身... |
| `RetreatForCommon` | **战场撤退** | LLC 基准 (BattleKeywords.json) | - 回合结束时，解除自身的混乱并从战斗中撤退(不包括强制混乱，不视作阵亡) - 连续遭遇战中，将自身... |
| `Retreat_FullStop` | **后方支援分派** | LLC 基准 (BattleKeywords.json) | - 回合结束时，解除自身的混乱并从战斗中撤退(不包括强制混乱，不视作阵亡) · 连续遭遇战中，将自身... |
| `RicardoBookRaid` | **写进账簿** | LLC 基准 (BattleKeywords-BossRaid.json) | 最大值：30 每带有1层本效果，使自身受到的伤害+3% |
| `RicardoJokeRaid` | **大哥的试炼** | LLC 基准 (BattleKeywords-BossRaid.json) | 回合结束时，本效果的层数减少1层 带有该效果时，受到的技能伤害与震颤引爆 造成的混乱阈值前移量变为2... |
| `RicardoTattooRaid` | **仇怨纹身** | LLC 基准 (BattleKeywords-BossRaid.json) | 最大值：300 每带有10层本效果，使自身技能的攻击等级+1 |
| `RienWeapon01Hatchet` | **用手斧将肋骨砍下时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 未摧毁并命中时，使自身增加2级呼吸法 强度 |
| `RienWeapon01Hatchet2phase` | **用手斧将肋骨砍下时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 未摧毁并命中时，使自身增加2级呼吸法 强度并使自身获得2层呼吸法 |
| `RienWeapon02Stiletto` | **用锥将肺贯穿时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 未摧毁并命中时，使目标增加2级沉沦 强度 |
| `RienWeapon02Stiletto2phase` | **用锥将肺贯穿时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 未摧毁并命中时，使目标增加2级沉沦 强度并对其施加2层沉沦 |
| `RienWeapon03Greatsword` | **用手半剑将肩膀击碎时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，下回合使自身获得1层攻击等级提升 ... |
| `RienWeapon03Greatsword2phase` | **用手半剑将肩膀击碎时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+7.5% - 未摧毁并命中时，直到下回合使自身获得1层攻击等... |
| `RienWeapon04Rapier` | **应该用刺剑在身体上开超过十个洞时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，下回合对目标施加1层防御等级降低 ... |
| `RienWeapon04Rapier2phase` | **应该用刺剑在身体上开超过十个洞时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 此硬币造成的伤害+7.5% - 未摧毁并命中时，直到下回合对目标施加1层防御等... |
| `RienWeapon05Sledgehammer` | **应该用锤子将后脑敲碎时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，使目标的混乱阈值前移3 |
| `RienWeapon05Sledgehammer2phase` | **应该用锤子将后脑敲碎时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 此硬币造成的伤害+7.5% - 未摧毁并命中时，使目标的混乱阈值前移5 |
| `RienWeapon06Ultragreatsword` | **应该用大剑将躯干劈开时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+10% - 未摧毁并命中时，对目标施加1层斩击易损 (每回合... |
| `RienWeapon06Ultragreatsword2phase` | **应该用大剑将躯干劈开时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施加1层斩击易损... |
| `RienWeapon07Lance` | **应该用长枪刺穿一个20英寸的洞时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 此硬币造成的伤害+10% - 未摧毁并命中时，对目标施加1层突刺易损 (每回合... |
| `RienWeapon07Lance2phase` | **应该用长枪刺穿一个20英寸的洞时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成突刺伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施加1层突刺易损... |
| `RienWeapon08Chain` | **应该用鞭子抽落上万块肉时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 此硬币造成的伤害+10% - 未摧毁并命中时，对目标施加1层打击易损 (每回合... |
| `RienWeapon08Chain2phase` | **应该用鞭子抽落上万块肉时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成打击伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施加1层打击易损... |
| `RienWeapon09Scythe` | **应该用镰刀…像某人一般沿着空间斩裂时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+20% - 未摧毁并命中时，必定暴击 |
| `RienWeapon09Scythe2phase` | **应该用镰刀…像某人一般沿着空间斩裂时…** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 造成斩击伤害 - 此硬币造成的伤害+30% - 未摧毁并命中时，必定暴击 |
| `RighteousFeeling` | **正义至极！！** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 每回合结束时，下回合使自身获得1层迅捷 ，3层攻击等级提升 与3层防御等级降低  - 每满3回合... |
| `RighteousFeelingSancho` | **含着血泪，我会承担起责任。** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 使自身获得硬血 时，额外获得1层硬血 。(每回合最多5次) - 每回合结束时，下回合使自身获得2... |
| `RingFingerFauvism` | **野性美** | LLC 基准 (BattleKeywords_Mirror7.json) | - 对流血 强度不低于20级的敌方单位使用的基础技能硬币威力+1，造成的伤害+20%(攻击容量不低于... |
| `RingFingerPhysical` | **肉体美** | LLC 基准 (BattleKeywords_Mirror7.json) | - 对流血 强度不低于20级的敌方单位使用的基础技能硬币威力+1，造成的伤害+20%(攻击容量不低于... |
| `RisingMadnessNoir` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层…… |
| `RisingMadnessNoir2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 …… |
| `RisingMadnessRouge` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层…… |
| `RisingMadnessRouge2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果的层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 …… |
| `RisingMadnessSisyphe` | **阳光** | LLC 2026092102／本地格式化 | - 最大值：2 - 回合结束时，本效果层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得1层伤害强化 并对自身施加1层易…… |
| `RisingMadnessSisyphe2nd` | **刺眼的阳光** | LLC 2026092102／本地格式化 | - 最大值：1 - 回合结束时，本效果层数减少1层 - 回合开始时，若本效果层数为0层，则触发以下效果 · 使自身获得2层威力提升 与2层伤害强化 并…… |
| `RootSoupKimPersonal` | **寄宿怨恨的剑鞘** | LLC 基准 (BattleKeywords.json) | - 包括自身在内的友方单位受到体力伤害时，使自身获得层数相当于伤害量的郁积的怨结  - 被动追悼可无... |
| `RootSoupKimSatgat` | **本国剑-传授真意** | LLC 基准 (BattleKeywords.json) | - 基础攻击技能的最终威力+(场上属于剑契组的友方单位数/3)(最多+2，向下取整) - 若自身属于... |
| `RoseThorn` | **贪食棘** | LLC 基准 (BattleKeywords.json) | 最大值：9  回合结束时，对自身施加层数相当于色欲共鸣数的流血 ，贪食棘 层数减少1层。(最大流血 ... |
| `RoseWedge` | **玫瑰之楔** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 强度最大值：10 - 层数最大值：4 - 自身每受到10点流血 伤害，则使自身增加1级本效果强度... |
| `RougeIshmaelCocoon` | **更衣室** | 工作区 (BattleKeywords.json) | - 最大值：2 - 速度固定为1 - 受到的技能伤害-50% - 获得时立即移除混乱阈值，若处于混乱... |
| `RougeIshmaelEclose` | **焕然一新** | 工作区 (BattleKeywords.json) | - 最小速度、最大速度+1 - 最大体力增加25% - 受到的技能伤害-10% - 通过基础技能对敌... |
| `RougeThreeCocoon` | **更衣室** | LLC 2026092102／本地格式化 | - 最大值：3 - 不会受到体力伤害 - 受到攻击时，触发以下效果(每回合最多20次)  · 使自身获得1层搏动  · 使自身获得1层伤害强化  · …… |
| `RougeThreeCocoonHit` | **迫害** | LLC 2026092102／本地格式化 | - 最大值：20 |
| `RougeThreeCocoonShield` | **信仰** | LLC 2026092102／本地格式化 | - 回合开始时，获得相当于本效果层数的护盾 - 护盾减少时，本效果层数减少 |
| `RougeThreeNormal` | **精品店新品** | LLC 2026092102／本地格式化 | - 最大值：20  使用技能时，消耗自身体力上限1%的体力并使该技能造成的伤害+(消耗的体力)% |
| `RunHallway` | **群体移动准备** | LLC 基准 (BattleKeywords-walpu8.json) | - 最大值：3 - 战斗开始时本效果层数减少1层 - 若本效果层数为0层，则回合开始时使用技能“群体... |
| `RunSinclair` | **逃脱装置** | LLC 基准 (BattleKeywords.json) | - 自身受到使自身体力降至10点的伤害时，本回合自身的体力不会低于10点 - 以上效果触发的回合结束... |
| `Run_LowMorale` | **溃退** | LLC 基准 (Bufs.json) | 无法行动。受到攻击时，在攻击结束后阵亡。 |
| `Run_Panic` | **无措** | LLC 基准 (BattleKeywords.json) | 一回合内无法行动。受到攻击时，在攻击者的技能结束后逃离战斗。 |
| `RunawayHorseWei_LowMorale` | **脱缰之马** | LLC 基准 (BattleKeywords-cultivation.json) | - 士气低落 - 回合开始时，使自身获得2层攻击等级提升 并对自身施加1层易损 |
| `RunawayHorseWei_Panic` | **脱缰之马** | LLC 基准 (BattleKeywords-cultivation.json) | - 陷入恐慌 - 回合开始时，使自身的最大速度值+1，获得2层攻击等级提升 并对自身施加2层易损 |
| `RustedWingScales` | **锈蚀的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的技能“罗生-到来”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `RustedWingScalesExplain` | **锈蚀的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的技能“罗生-到来”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `RyoshuEGOPF` | **罗生** | LLC 基准 (BattleKeywords-a1c9p3.json) | 最大值：999 - 良秀的技能每造成1点伤害，获得1层本效果 - 本效果层数每有33层，使自身基础技... |
| `RyoshuParryIndexFingerThey` | **赤丝** | LLC 基准 (BattleKeywords-a1c9p3.json) |  |
| `RyoshuParryIndexFingerWe` | **赤丝** | LLC 基准 (BattleKeywords-a1c9p3.json) |  |
| `RyoshuParrySoji` | **相互纠缠、扭曲的记忆与回忆** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 行动槽+1 - 对小指父辈造成的伤害与受到来自小指父辈的伤害+20%，拼点胜利时，使小指父辈失去... |
| `RyoshuParrySojiThey` | **赤丝** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 所有硬币转化为不可摧毁的硬币 - 最终威力+4 |
| `RyoshuParrySojiThree` | **未曾割舍的时间** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 对小指父辈造成的伤害与受到来自小指父辈的伤害+20%，拼点胜利时，使小指父辈失去5点理智值 - ... |
| `RyoshuParrySojiTwo` | **未曾割舍的记忆** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 对小指父辈造成的伤害与受到来自小指父辈的伤害+20%，拼点胜利时，使小指父辈失去5点理智值 - ... |
| `RyoshuParrySojiWe` | **赤丝** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 行动槽+3 对小指 父辈造成的伤害+50% - 本场战斗中自身使用技能时，获得对应属性的1个E.... |
| `RyoshuSlotPlusA1C9` | **过往的恶臭** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 行动槽+1 - 对属于蜘蛛巢的敌方单位造成的伤害+10% - 陷入混乱时，下回合开始时解除自身的... |
| `RyoshuStartA1C9` | **复燃的喜悦** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 对属于蜘蛛巢的敌方单位造成的伤害+10% - 陷入混乱时，下回合开始时解除自身的混乱并获得1层强... |
| `RyoshuStartA1C9P2` | **被千刀万剐的记忆** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 行动槽+1 - 对属于蜘蛛巢的敌方单位造成的伤害+10% - 陷入混乱时，下回合开始时解除自身的... |
| `Ryoshu_Attackup` | **被千刀万剐的记忆** | LLC 基准 (BattleKeywords-a1c8p3.json) | [良秀特殊效果] - 本场战斗中，对雷横造成的伤害+(当前回合数×2.5)%(最多+30%) |
| `Ryoshu_IndexFightBuff` | **被千刀万剐的记忆与回忆** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 行动槽+1 - 对属于蜘蛛巢的敌方单位造成的伤害+10% - 受到使自身陷入混乱的伤害时，不会陷... |
| `Ryoshu_RienBattle_1Phase` | **血缘[けつえん]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 本场战斗中，不低于1名其他友方单位存活时，良秀的体力不会降至1点以下 - 拼点威力+1，攻击命中... |
| `Ryoshu_RienBattle_2Phase` | **连血缘[れんけつえん]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 本场战斗中，不低于1名其他友方单位存活时，良秀的体力不会降至1点以下 - 拼点威力+2，攻击命中... |
| `S2Mirror1stFloor_Hard` | **镜中之镜困难 - 第一层** | LLC 基准 (Bufs.json) | 技能最终威力+1 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `S2Mirror2ndFloor` | **镜中之镜 - 第二层** | LLC 基准 (Bufs.json) | 技能最终威力+1 |
| `S2Mirror2ndFloor_Hard` | **镜中之镜困难 - 第二层** | LLC 基准 (Bufs.json) | 技能最终威力+1 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `S2Mirror3rdFloor` | **镜中之镜 - 第三层** | LLC 基准 (Bufs.json) | 技能最终威力+1 攻击等级+3 |
| `S2Mirror3rdFloor_Hard` | **镜中之镜困难 - 第三层** | LLC 基准 (Bufs.json) | 技能最终威力+2 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `S2Mirror4thFloor` | **镜中之镜 - 第四层** | LLC 基准 (Bufs.json) | 技能最终威力+1 攻击等级+3 技能基础威力+1 |
| `S2Mirror4thFloor_Hard` | **镜中之镜困难 - 第四层** | LLC 基准 (Bufs.json) | 技能最终威力+3 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `S2Mirror5thFloor` | **镜中之镜 - 第五层** | LLC 基准 (Bufs.json) | 技能最终威力+1 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `S2Mirror5thFloor_Hard` | **镜中之镜困难 - 第五层** | LLC 基准 (Bufs.json) | 技能最终威力+5 攻击等级+3 技能基础威力+1 加算技能硬币威力+2 减算技能硬币威力-2 |
| `SadLamanchaland` | **责任感** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 拼点威力+1 - 造成的伤害+20% - 受到的伤害+20% |
| `SanchoMind_LowMorale` | **觉醒杀戮的昂扬感** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 士气低落 每回合开始时，使自身获得2层攻击等级提升 。理智值恢复效率+2 |
| `SanchoMind_Panic` | **觉醒杀戮的昂扬感** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 陷入恐慌 回合开始时，使自身获得6层防御等级提升 。下回合使自身获得3层攻击等级提升 |
| `SapsareeCooking` | **切碎的食材** | LLC 2026092102／本地格式化 | - 最大值：5 - 回合结束时解除 |
| `SapsareeHungry` | **我说我肚子饿了噢** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，使自身增加1级攻击等级 - 若本效果层数为3层，则使自身造成的伤害+50% - 副主厨使用技能“啊！我说吃饭时间…… |
| `SapsareeShield` | **吃吧……** | LLC 2026092102／本地格式化 | - 副主厨将受到来自敌方单位的单方面攻击时，消耗1层并使该敌方单位的目标改为自身，随后使用援护防御专用技能 - 多个友方单位带有援护防御 时，层数最高…… |
| `SapsareeSpices` | **火辣辣酱** | LLC 2026092102／本地格式化 | - 最大值：3 - 每带有1层本效果，使自身减少1级攻击等级 |
| `SapsareeYammi` | **我说吃好喝好，精神百倍噢** | LLC 2026092102／本地格式化 | - 最大值：5 - 每带有1层本效果，使自身增加1级攻击等级 - 回合开始时，自身每带有1层“我说我肚子饿了噢”，使本效果的层数减少1层 |
| `Sapsaree_LowMorale` | **烹饪欲望** | LLC 2026092102／本地格式化 | - 士气低落 - 自身每带有1层“我说我肚子饿了噢”，使自身攻击等级+1，受到的伤害+3% |
| `Sapsaree_Panic` | **烹饪欲望** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 自身每带有1层“我说我肚子饿了噢”，使自身攻击等级+2，受到的伤害+5% |
| `SatisfyingEsteemNeeds` | **被满足的认可欲** | LLC 基准 (BattleKeywords.json) | - 使自身被指令的印记 标记的技能造成的伤害+7.5% - 使自身对指令对象 造成的伤害+7.5% |
| `SavePlacenta` | **自我保护** | LLC 2026092102／本地格式化 | - 命脉将受到来自敌方单位的单方面攻击时，消耗1层并使该敌方单位的目标改为自身，随后使用援护防御专用技能 - 回合结束时解除 |
| `ScarBygoneDaysRefraction_LowMorale` | **爱憎** | LLC 基准 (BattleKeywords_Refraction6.json) | 造成与受到的伤害+10% |
| `ScarBygoneDaysRefraction_Panic` | **爱憎** | LLC 基准 (BattleKeywords_Refraction6.json) | 造成与受到的伤害+20% |
| `ScarBygoneDays_LowMorale` | **爱憎** | LLC 基准 (BattleKeywords-a1c9p2.json) | 对良秀造成的伤害与受到来自良秀的伤害+10% |
| `ScarBygoneDays_Panic` | **爱憎** | LLC 基准 (BattleKeywords-a1c9p2.json) | 对良秀造成的伤害与受到来自良秀的伤害+20% |
| `Scared` | **恐惧** | LLC 基准 (BattleKeywords.json) | 回合结束时，若自身的理智值不高于-20点，则下回合使自身获得1层守护 。 |
| `ScarletDamageDown` | **色欲伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低色欲技能造成的伤害。(最多10层) |
| `ScarletDamageUp` | **色欲伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高色欲技能造成的伤害。(最多10层) |
| `ScarletMothRodion` | **朱红之蛾** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合结束时，使自身恢复体力上限(本效果层数)%的体力(最低体力恢复量：1) - ... |
| `ScarletResistDown` | **色欲抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的色欲抗性增加(每层0.1) |
| `ScarletResistUp` | **色欲抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的色欲抗性减少(每层0.1) |
| `ScarletResultDown` | **色欲威力降低** | LLC 基准 (Bufs.json) | 本回合内色欲技能的最终威力-{0} |
| `ScarletResultUp` | **色欲威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高色欲技能的最终威力 |
| `ScarletTakeDamageDown` | **色欲守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自色欲技能的伤害。(最多10层) |
| `ScarletTakeDamageUp` | **色欲易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自色欲技能的伤害。(最多10层) |
| `ScratchesHurt` | **撕裂的伤口** | LLC 基准 (BattleKeywords-exme.json) | - 最大值：3 - 回合开始时，每带有1层本效果，使自身增加2级流血强度  · 若本效果层数为最大值... |
| `ScratchesHurtID` | **撕裂的伤口** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合开始时，使自身增加2级流血 强度 - 回合结束时，下回合对自身施加1层束缚 ... |
| `SeaTerrorCell` | **恐鱼同化** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 最大值：5 - 回合开始时，本效果层数增加1层 - 每带有1层本效果，对自身施加1层攻击等级降低... |
| `SelfCharge` | **自体发电** | LLC 基准 (BattleKeywords.json) | 身体周围似乎有电流浮现。 若死亡前自身仍带有自体发电 ，则消耗完所有层数前固定体力为1(最多20层) |
| `SelfChargeAlly` | **自体发电** | LLC 基准 (BattleKeywords.json) | - 使自身的最终威力+2 - 本效果层数减少时，使自身获得相应层数的充能  - 满足以下条件时，使本... |
| `SelfHarm_LowMorale` | **自残** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 回合开始时，使自身获得2层迅捷 并对自身施加2层易损 。 |
| `SelfHarm_Panic` | **自残** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 回合开始时，使自身失去10点体力 |
| `SeniorCianjing` | **大弦惊** | LLC 基准 (BattleKeywords.json) | - 回合开始时，使自身获得2层攻击等级提升 与2层防御等级提升  - 回合结束时，本效果层数减少1层... |
| `SeveredTendon` | **肌腱切断** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：3 - 每带有1层本效果，使自身基础攻击技能的基础威力-1 - 回合结束时，本效果层数减... |
| `SeveredTendonAlly` | **肌腱切断** | LLC 基准 (BattleKeywords.json) | - 基础威力-1 - 回合结束时，解除本效果 - 最大值：1 |
| `ShamrockDamageDown` | **暴食伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低暴食技能造成的伤害。(最多10层) |
| `ShamrockDamageUp` | **暴食伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高暴食技能造成的伤害。(最多10层) |
| `ShamrockResistDown` | **暴食抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的暴食抗性增加(每层0.1) |
| `ShamrockResistUp` | **暴食抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的暴食抗性减少(每层0.1) |
| `ShamrockResultDown` | **暴食威力降低** | LLC 基准 (Bufs.json) | 本回合内暴食技能的最终威力-{0} |
| `ShamrockResultUp` | **暴食威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内，暴食属性技能的最终威力根据本层数相应增加 |
| `ShamrockTakeDamageDown` | **暴食守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自暴食技能的伤害。(最多10层) |
| `ShamrockTakeDamageUp` | **暴食易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自暴食技能的伤害。(最多10层) |
| `ShardOfUmbrella` | **雨伞碎片** | LLC 基准 (BattleKeywords.json) | 回合结束时，每层增加5级破裂 强度 |
| `ShareCharge` | **自谐振电路** | LLC 基准 (BattleKeywords.json) | 当前全体友方单位带有的充能 层数之和  技能命中时造成的伤害+(当前友方单位的充能 层数之和/3)%... |
| `SheutFracture` | **影之龟裂** | LLC 基准 (BattleKeywords.json) | - 特殊沉沦 - 最大值：10 - 自身每带有1层本效果，受到来自怠惰与忧郁技能的伤害+1% - 本... |
| `ShieldManagerCryingToad` | **泪珠** | LLC 基准 (BattleKeywords.json) | - 本效果视作“护盾管理”效果 - 回合结束时，本效果的层数减少1层 - 若自身带有泪珠 ，则回合结... |
| `Shin_IndexFingerYisang` | **心-命运** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+1 - 令自身基础技能增加的呼吸法 强度与获得的呼吸法 层数额外+1 - 若自... |
| `Shin_Rien` | **心-里恩** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 回合开始时，根据自身已失去体力，相应获得以下效果 · 每失去体力上限15%的体力，使自身获得1层... |
| `SignAwakenSinclair` | **印记-未来显现** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 与等级高于自身的敌方单位进行拼点时，使自身的拼点威力+2 - 回合结束时，若自身陷入混乱，则下回... |
| `SignOfDespair` | **绝望的加护** | LLC 基准 (BattleKeywords-walpu6.json) | 攻击结束后，若有目标未带有漆黑冰冷之泪，则下回合解除本效果  使自身获得1层拼点威力提升与1层伤害强... |
| `SilverOpportunity` | **拘束解除-创作沉浸** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+2 - 替换一组新的基础技能 - 通过基础攻击技能对速度值低于自身的敌方单位造... |
| `SingBulletSupport` | **(엄지 싱클 탄환 보급 받는 대상 이펙트)** | LLC 基准 (BattleKeywords.json) |  |
| `Sinking` | **沉沦** | LLC 基准 (BattleKeywords.json) | 受到攻击时，失去数值等同于本效果强度的固定理智值点数(未带有理智值的目标则受到忧郁伤害)。 效果生效... |
| `SinkingBlack` | **过期状态** | LLC 基准 (BattleKeywords-walpu4.json) |  |
| `SinkingSurge` | **沉沦泛滥** | LLC 基准 (BattleKeywords.json) | 对目标造成(其沉沦 层数×沉沦 强度)点理智伤害，随后解除目标的沉沦  若目标的理智值不高于-45点... |
| `SinkingVulnerable` | **沉沦易损** | LLC 基准 (BattleKeywords.json) | 一回合内，本效果每有1层，受到来自沉沦 效果造成的伤害增加1点 |
| `SinkingWhite` | **蝶** | LLC 基准 (BattleKeywords-walpu4.json) | - 特殊沉沦 - 基础值：0，最大值：15 - 本效果的强度为生蝶，层数为亡蝶 - 受到攻击时，使攻... |
| `SipOfAlcohol` | **小酌** | LLC 基准 (BattleKeywords-a1c8p1.json) | - 最大值：5 - 回合结束时，若本效果层数不低于3层，则使自身恢复3%的体力（本体与部位） - 回... |
| `SipOfAlcoholJin` | **小酌（真）** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：5 - 回合结束时，下回合使自身增加(本效果层数×2)级呼吸法 强度 - 回合结束时，下... |
| `SisyphusAmber` | **琥珀** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 |
| `SisyphusAmethyst` | **紫水晶** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 |
| `SisyphusEmerald` | **祖母绿** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusGold` | **黄金** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusRuby` | **红宝石** | LLC 2026092102／本地格式化 | - 技能使敌方单位增加的烧伤 、流血 、震颤 、破裂 与沉沦 强度额外+1级 - 获得的充能 与呼吸法 层数额外+1层 - 获得本效果时，使自身获得1…… |
| `SisyphusTopaz` | **托帕石** | LLC 2026092102／本地格式化 | - 无效果 |
| `SkillPowerUp` | **基础威力提升** | LLC 基准 (BattleKeywords.json) | 基于本效果的层数提高技能的基础威力 |
| `SlashDamageDown` | **斩击伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低斩击技能造成的伤害。(最多10层) |
| `SlashDamageUp` | **斩击伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高斩击技能造成的伤害。(最多10层) |
| `SlashResistDown` | **斩击抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的斩击抗性增加(每层0.1) |
| `SlashResistUp` | **斩击抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的斩击抗性减少(每层0.1) |
| `SlashResultDown` | **斩击威力降低** | LLC 基准 (Bufs.json) | 本回合内斩击技能的最终威力-{0} |
| `SlashResultUp` | **斩击威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高斩击技能的最终威力。 |
| `SlashTakeDamageDown` | **斩击守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自斩击技能的伤害。(最多10层) |
| `SlashTakeDamageUp` | **斩击易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自斩击技能的伤害。(最多10层) |
| `SlaveHunersPower` | **押送命令** | LLC 基准 (BattleKeywords-exme.json) | - 基础攻击等级+5 - 基础防御等级+5 |
| `Smoke` | **烟气** | LLC 基准 (BattleKeywords-walpu5.json) | - 强度最大值：10 - 层数最大值：5 - 强度不低于9级时，使自身的最终威力+1 - 每级强度使... |
| `SnakePoisonJin` | **扩散的蛇毒** | LLC 基准 (BattleKeywords-cultivation.json) | - 攻击等级-7 - 防御等级-7 进行拼点时，受到自身体力上限1%的伤害 |
| `SnakePoisonJinWeak` | **蛇毒** | LLC 基准 (BattleKeywords-cultivation.json) | - 攻击等级-1 - 防御等级-1 |
| `SnakeStance` | **巳臂** | LLC 基准 (BattleKeywords.json) | 最大值：3 回合结束时，下回合使自身增加3级呼吸法 强度并使自身获得2层呼吸法  使用基础攻击技能时... |
| `Snare` | **套索** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合结束时，根据自身的速度值相应使自身增加破裂 强度(最多5)，下回合对自身施加... |
| `SnipingArrowMode` | **狙击姿势** | LLC 基准 (BattleKeywords.json) | - 自身带有本效果时，触发以下效果 · 使仪表盘上自身位于最左侧的基础攻击技能转化为“闪弓”，并在战... |
| `SojiAbiAgeFuture` | **顺行-怜悯** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：20 - 本效果层数每有1层，使自身造成与受到的伤害-2% |
| `SojiAbiAgePast` | **逆行-憎恶** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：20 - 本效果层数每有1层，使自身造成与受到的伤害+2% |
| `SojiAbiBuffOne` | **鸡鸣** | LLC 基准 (BattleKeywords-a1c9p3.json) | 可与敌方单位的特定行动槽进行拼点 |
| `SojiAbiBuffThree` | **黄昏** | LLC 基准 (BattleKeywords-a1c9p3.json) | 可与敌方单位的特定行动槽进行拼点 |
| `SojiAbiBuffTwo` | **日入** | LLC 基准 (BattleKeywords-a1c9p3.json) | 可与敌方单位的特定行动槽进行拼点 |
| `SojiRyoshuEchoFuture` | **残影** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 受到来自蜘蛛巢之刃 良秀的基础攻击技能的伤害+5% |
| `SojiRyoshuEchoPast` | **纠缠** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 技能与被动效果可使本效果的最小值增加至5，最大值增加至9 |
| `SojiRyoshuEntangle` | **断缘** | LLC 基准 (BattleKeywords.json) | - 最大值：4 - 每有1名属于蜘蛛巢 父辈的友方人格阵亡，获得1层本效果 - 根据阵亡的属于蜘蛛巢... |
| `SojiRyoshuShin` | **心-地慧星** | LLC 基准 (BattleKeywords.json) | - 最小与最大速度值+2 - 使用基础攻击技能时，使自身增加2级呼吸法 强度并使自身获得1层呼吸法 ... |
| `SpecimenTheRings` | **展览完成** | LLC 基准 (BattleKeywords-a1c9p3.json) | 全体罪人与援助单位都处于人体观剧状态时，战斗失败 |
| `StackFuture` | **未来状态（已禁用）** | LLC 基准 (BattleKeywords_Refraction6.json) | - 禁用被动技能“未来” - 最大值：30 |
| `StackFutureActivate` | **未来状态** | LLC 基准 (BattleKeywords_Refraction6.json) | - 激活被动技能“未来” - 根据本效果层数获得不同效果： · 0~10层：技能增加的流血 强度与施... |
| `StackPast` | **过去状态（已禁用）** | LLC 基准 (BattleKeywords_Refraction6.json) | - 禁用被动技能“过去” - 最大值：30 |
| `StackPastActivate` | **过去状态** | LLC 基准 (BattleKeywords_Refraction6.json) | - 激活被动技能“过去” - 根据本效果层数获得不同效果： · 0~10层：技能增加的烧伤 强度与施... |
| `StackPresent` | **现在状态（已禁用）** | LLC 基准 (BattleKeywords_Refraction6.json) | - 禁用被动技能“现在” - 最大值：30 |
| `StackPresentActivate` | **现在状态** | LLC 基准 (BattleKeywords_Refraction6.json) | - 激活被动技能“现在” - 根据本效果层数获得不同效果： · 0~10层：技能增加的呼吸法 强度与... |
| `StackRienSpecialSkill` | **代行[赫尔墨斯]** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 使用攻击技能时，获得1层本效果(每个技能仅可获得1次，相同技能不能获得2次) - 回合开始时，若... |
| `StackYisangSpecialSkill` | **代行[赫尔墨斯]** | LLC 基准 (BattleKeywords.json) | - 回合开始时，若本效果层数为9层，则可使用强力技能 - 每回合最多获得(自身的解放 阶段+2)层本... |
| `StartXichun` | **始** | LLC 基准 (BattleKeywords.json) | - 最大值：6 - 自身参战的回合数 - 撤退时解除本效果 - 回合结束时获得1层本效果 |
| `StarvingBarberOne` | **衰老** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 很久未曾饮用血液了。 - 基础攻击等级-15 - 基础防御等级-15 |
| `StarvingBarberTwo` | **衰老** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 很久未曾饮用血液了。 - 基础攻击等级-25 - 基础防御等级-25 |
| `StarvingDolcineaOne` | **衰老** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 很久未曾饮用血液了。 - 基础攻击等级-35 - 基础防御等级-35 |
| `StarvingDolcineaServant` | **衰老** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 很久未曾饮用血液了。 - 基础攻击等级-15 - 基础防御等级-15 |
| `StarvingDonqui` | **饥饿与衰老** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 基础攻击等级-10 - 基础防御等级-10 |
| `StarvingPriestOne` | **衰老** | LLC 基准 (BattleKeywords-a1c7p2.json) | - 很久未曾饮用血液了。 - 基础攻击等级-15 - 基础防御等级-15 |
| `StarvingPriestTwo` | **衰老** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 很久未曾饮用血液了。 - 基础攻击等级-25 - 基础防御等级-25 |
| `StickCoinHeadAndTailToMaxPer` | **概率坍缩** | LLC 基准 (Bufs.json) | 每3回合，根据友方人格使用的技能硬币种类，使硬币的朝向全部为正面或反面 |
| `StigmaWorkshopCelloCaseOne` | **炎蝶之棺** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 基础技能命中时，使自身获得2层本效果 - 回合... |
| `StigmaWorkshopCelloCaseThree` | **炎蝶之棺** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 基础技能命中时，使自身获得2层本效果 - 回合... |
| `StigmaWorkshopCelloCaseTwo` | **炎蝶之棺** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 基础技能命中时，使自身获得2层本效果 - 回合... |
| `StigmaWorkshopHandStep1` | **黎明之火** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 回合开始时，每带有5层本效果，使自身增加1级烧... |
| `StigmaWorkshopHandStep2` | **黎明之火** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 回合开始时，每带有5层本效果，使自身增加1级烧... |
| `StigmaWorkshopHandStep3` | **黎明之火** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每回合最多获得20层本效果 - 回合开始时，每带有5层本效果，使自身增加1级烧... |
| `Stressed` | **压力** | LLC 基准 (BattleKeywords.json) | 回合结束时，若自身的理智值不高于-25点，则下回合使自身获得1层忍耐 。 |
| `Strong_Chicken` | **难以言表的愤怒** | LLC 基准 (Bufs.json) | 每回合获得1层强壮 |
| `StudySignSinclair` | **某道印记** | LLC 基准 (BattleKeywords-cultivation.json) | - 下回合使自身恢复30点理智值 - 回合结束时解除 |
| `StudyStatSinclair` | **为破卵而出的挣扎** | LLC 基准 (BattleKeywords-cultivation.json) | - 根据自身从课程中获得的智/勇/仁之和，相应获得强化 |
| `StudyStatSinclair_A` | **为破卵而出的挣扎Ⅰ** | LLC 基准 (BattleKeywords-cultivation.json) | - 每回合使自身恢复3点理智值 - 最小与最大速度值+1 - 增加2级攻击等级 - 增加2级防御等级 |
| `StudyStatSinclair_B` | **为破卵而出的挣扎Ⅱ** | LLC 基准 (BattleKeywords-cultivation.json) | - 每回合使自身恢复5点理智值 - 最小与最大速度值+1 - 每回合使自身获得1层强壮 与1层守护 ... |
| `StudyStatSinclair_C` | **为破卵而出的挣扎Ⅲ** | LLC 基准 (BattleKeywords-cultivation.json) | - 每回合使自身恢复5点理智值 - 最小与最大速度值+1，每回合使自身获得1层强壮 与1层守护  -... |
| `StudyStatSinclair_D` | **为破卵而出的挣扎Ⅳ** | LLC 基准 (BattleKeywords-cultivation.json) | - 每回合使自身恢复10点理智值 - 最小与最大速度值+1，每回合使自身获得1层强壮 与1层守护  ... |
| `StudyStatSinclair_E` | **为破卵而出的挣扎Ⅴ** | LLC 基准 (BattleKeywords-cultivation.json) | - 每回合使自身恢复15点理智值 - 最小与最大速度值+2，每回合使自身获得1层强壮 与1层守护  ... |
| `Stun` | **晕眩** | LLC 基准 (BattleKeywords.json) |  |
| `Suicide_LowMorale` | **自尽** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 首次陷入士气低落状态时，进入无法行动状态 |
| `Suicide_Panic` | **自尽** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 3回合内无法行动，回合开始时阵亡，全体友方单位失去10点理智值。 |
| `SuperCoin` | **不可摧毁的硬币** | LLC 基准 (BattleKeywords.json) | - 此类硬币不会因为拼点失败而被摧毁。 - 若攻击技能带有此类硬币，则受到攻击后以此类硬币进行攻击。... |
| `SupportProtect` | **援护防御** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 当友方单位将受到来自敌方单位的单方面攻击时，消耗1层并使该敌方单位的目标改为自身... |
| `SupportProtectTypo` | **援护防御** | LLC 基准 (BattleKeywords.json) |  |
| `SupremeEternalLife` | **至高无上的不死** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 回合开始时，使贾母的本体与所有部位获得其体力上限5%的护盾 |
| `SweeperA` | **第一波** | LLC 基准 (BattleKeywords-a1c9116.json) | 第一波在{0}回合后结束 |
| `SweeperB` | **第二波** | LLC 基准 (BattleKeywords-a1c9116.json) | 第二波在{0}回合后结束 |
| `SweeperC` | **第三波** | LLC 基准 (BattleKeywords-a1c9116.json) | 第三波在{0}回合后结束 |
| `SweptAwayWei` | **余波** | LLC 基准 (BattleKeywords-cultivation.json) | - 最大值：10 - 使自身受到的震颤引爆 造成的混乱阈值前移量变为2倍 - 回合结束时，本效果层数... |
| `SwirlingBlood` | **摇曳【血魔】** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 本效果生效时，自身受到伤害时，攻击后使攻击者增加5级流血 强度。 - 本效果生效时，回合结束时护... |
| `SwirlingBloodPersonality` | **摇曳【血魔】** | LLC 基准 (BattleKeywords.json) | - 最大值：50 - 本效果生效时，使护盾体力受到的流血 伤害转化为血宴 。 - 获得本效果时，使自... |
| `Switch_Vibration` | **振幅转换** | LLC 基准 (BattleKeywords.json) | 将目标的震颤 与已转换的震颤 转换为其他类型的震颤。 转换时，现有震颤的强度与层数保持不变。 |
| `SwordCutwithTear` | **泪锋** | LLC 基准 (BattleKeywords-walpu6.json) | - 回合开始时，使自身获得5层深泪 · 若本效果层数为3层，则额外获得5层深泪  - 回合结束时，使... |
| `SwordPlayOfTheHomeland` | **本国剑术** | LLC 基准 (BattleKeywords.json) | - 使用技能时，若呼吸法 强度不低于5级，使1技能和2技能的硬币威力+(3/硬币数，最少为1)，暴击... |
| `SwordPlayOfTheMemorial` | **追悼** | LLC 基准 (BattleKeywords.json) | - 使用技能时，若呼吸法 强度不低于5级，使1技能和2技能的硬币威力+(3/硬币数，最少为1)，暴击... |
| `TagGameBuff` | **鬼** | LLC 基准 (BattleKeywords_Refraction6.json) | - 单方面攻击造成的伤害-100% - 受到来自单方面攻击的伤害+80% - 包括自身在内的全体嫉妒... |
| `TakeBreath_LowMorale` | **调息** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 回合开始时，使自身获得2层防御等级提升 并使自身的呼吸法 强度减少2级 |
| `TakeBreath_Panic` | **调息** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 回合开始时，使自身获得5层防御等级提升 并使自身的呼吸法 强度减少5级 |
| `TakeHpHealIncrease` | **体力恢复提升** | LLC 基准 (BattleKeywords.json) | 提升被动技能，技能，硬币效果提供的体力恢复效果(最多+5) |
| `TakeHpHealReduce` | **体力恢复降低** | LLC 基准 (BattleKeywords.json) | 一回合内根据本效果的层数来降低被动，技能及硬币效果的体力恢复量。(最多5层) |
| `TakePicture` | **获取情报** | LLC 基准 (BattleKeywords-exme.json) | - 使用与被拍摄的技能相同级别的技能时，拼点威力-5 (※ 守备技能与E.G.O技能分别计算) - ... |
| `Talisman` | **符咒** | LLC 基准 (BattleKeywords.json) | 最大值：6 攻击命中时，消耗目标的1层破裂 并使其增加(本效果层数/2)级破裂 强度(消耗破裂 层数... |
| `Target` | **标记** | LLC 基准 (BattleKeywords.json) | 被拥有被动技能[利刃]的角色指定为攻击目标。 |
| `Taunt` | **嘲讽** | LLC 基准 (BattleKeywords.json) |  |
| `TcorpSpecialInvestigator` | **T公司特别搜查官徽章** | LLC 基准 (BattleKeywords-tkt.json) | - 受到体力减少至0点的伤害时，体力不会低于1点，立即恢复体力上限80%的体力 并且解除自身的混乱(... |
| `TeachersCommand` | **拇指父辈的命令** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 攻击等级-5 |
| `TeachersPet_LowMorale` | **教材** | LLC 基准 (Bufs-a1c9p1.json) | - 与带有决斗高潮 的目标拼点时，拼点威力+1 - 拼点失败时，下回合对自身施加1层易损 (每回合最... |
| `TeachersPet_Panic` | **教材** | LLC 基准 (Bufs-a1c9p1.json) | - 与带有决斗高潮 的目标拼点时，拼点威力+2 - 拼点失败时，下回合对自身施加1层易损 (每回合最... |
| `TeachersPrey` | **狩猎目标** | LLC 基准 (BattleKeywords-a1c9p3.json) | 速度值固定为1，成为“拇指 父辈 - 瓦伦希娜”的所有攻击技能指定的目标 |
| `TeachersPreyMirror` | **狩猎目标** | LLC 基准 (BattleKeywords_Mirror7.json) | 速度值固定为1，成为“拇指 父辈 - 瓦伦希娜”的攻击技能“处置”指定的主要目标 |
| `TeachersPreyRodion` | **狩猎目标** | LLC 基准 (BattleKeywords.json) | - 受到来自蜘蛛巢 拇指 父辈 罗佳的基础技能的伤害+15% |
| `Teaching` | **问答** | LLC 基准 (BattleKeywords-a1c8p2.json) | 最大值：3 - 回合结束时，使自身恢复5点理智值 - 战斗中自身的体力降至0点时，使自身恢复全部体力... |
| `TensionUp` | **亢奋** | LLC 基准 (BattleKeywords-walpu8.json) | - 最大值：3 - 每带有1层本效果，使自身的暴怒与色欲技能造成的伤害+5% - 受到攻击时，使自身... |
| `TestWaitDocentRodion` | **反思** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 带有本效果的回合内，自身不能使用“批评” - 回合开始时，使自身恢复5点理智值 ... |
| `TestWaitingMeursault` | **缺陷补全** | LLC 基准 (BattleKeywords.json) | - 造成的伤害+10% - 环指 野兽派 讲解员 罗佳的技能“批评”的硬币重复使用时，使自身恢复3点... |
| `ThankyouDocentRodion` | **敬意** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 回合开始时，每带有1层本效果，随机使自身获得1层攻击等级提升或1层防御等级提升(... |
| `ThatIsRhythm` | **旋律** | LLC 基准 (BattleKeywords.json) | - 最大值：5 - 每带有1层本效果，使自身造成的伤害+2%(最多+10%) - 每带有1层本效果，... |
| `TheDrifter_LowMorale` | **朴刀** | LLC 基准 (BattleKeywords-a1c8p1.json) | - 士气低落 - 受到来自单方面攻击的伤害+10%，造成的反击伤害+30% |
| `TheDrifter_Panic` | **朴刀** | LLC 基准 (BattleKeywords-a1c8p1.json) | - 陷入恐慌 - 受到来自单方面攻击的伤害+20%，造成的反击伤害+50% |
| `ThePowerOfLoveAndHate` | **爱/憎** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大层数：20 - 特殊充能 - 特定技能发动附加效果所需的资源。最多叠加至20层。回合结束时，... |
| `TheUdjatOutis` | **瓦吉特之眼[先锋]** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 使自身最小与最大速度值+3 - 战斗开始时，使自身获得1层守护  - 战斗中使自... |
| `Thirst` | **饥渴** | LLC 基准 (BattleKeywords.json) | 增加即兴烹饪的体力恢复量。 被动触发时消耗。 |
| `ThirstyRose` | **饥渴的玫瑰** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：5 - 回合结束时，若自身带有的流血 强度不低于10级，则受到自身体力上限1%的色欲伤害... |
| `Thorn` | **荆棘** | LLC 基准 (BattleKeywords.json) | 受到攻击时，将所受伤害的50%反弹给攻击者。 |
| `ThornNoose` | **荆棘套索** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：3 - 回合结束时，使自身增加2级破裂 强度并对自身施加2层破裂  - 回合结束时，若本... |
| `ThornyFall_LowMorale` | **荆棘** | LLC 基准 (BattleKeywords-a1c7p2.json) | 拼点胜利时，使自身获得1层伤害强化 |
| `ThornyFall_Panic` | **荆棘** | LLC 基准 (BattleKeywords-a1c7p2.json) | 拼点胜利时，使自身获得1层伤害强化  回合结束时，下回合使自身获得2层拼点威力提升 |
| `ThreeMirrorpartYiSang` | **破碎的世界** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：1 - 回合结束时解除 - 受到的烧伤 伤害×1.2(向下取整，不包括特殊烧伤) - 受... |
| `ThundercloudFormation` | **雷云汇集** | LLC 基准 (BattleKeywords_Refraction4.json) | - 最多5层 - 层数为1时，使用强力技能。 - 回合结束时，本效果的层数减少1层。陷入混乱时，获得... |
| `TibiaPersonality` | **作品名：提比娅** | LLC 基准 (BattleKeywords.json) | 根据自身的活体材料 强度，相应使自身的基础攻击技能与可拼点反击技能获得以下效果： - 不低于1级：基... |
| `TickTockTickTock` | **滴答滴答？！** | LLC 基准 (BattleKeywords-fools.json) | - 回合结束时，恢复10点理智值 |
| `TiedRope` | **捕缚** | LLC 基准 (BattleKeywords-exme.json) | - 基础值：3 - 自身的速度值固定为1 - 自身基础技能的硬币威力固定为0点 - 回合结束时，本效... |
| `TiedRopeHonglu` | **捕缚[鸿璐]** | LLC 基准 (BattleKeywords.json) | - 基础值：3 - 最小与最大速度值-2 - 受到的傲慢伤害+10% - 施加者撤退，阵亡或对不同的... |
| `TiedWithRope` | **押送准备** | LLC 基准 (BattleKeywords-exme.json) | - 基础值：1 - 自身的速度值固定为1 - 若自身对目标施加的捕缚效果解除，或自身(推奴人)阵亡或... |
| `TiedWithRopeID` | **押送准备** | LLC 基准 (BattleKeywords.json) | - 基础值：1 - 与带有捕缚[鸿璐] 的敌方单位拼点时，使自身的拼点威力+1 - 攻击命中带有捕缚... |
| `TimeAcceleration` | **时间加速** | LLC 基准 (BattleKeywords-tkt.json) | - 使自身的速度值增加5 - 自身技能获得强化 - 对自身施加1层易损 ，因震颤引爆 ，技能，硬币效... |
| `TimeAccumulation` | **时间泄露** | LLC 基准 (BattleKeywords-tkt.json) | 带有本效果时，受到的伤害将被暂存。 回合结束时，本效果的层数减少1层。 回合结束时，若本效果仅剩1层... |
| `TimeEntangleDesc` | **残像纠缠** | LLC 基准 (BattleKeywords-a1c9p2.json) | 残像纠缠状态 随战斗模式进行改变阶段 |
| `TimeEntangleFour` | **四重残像纠缠** | LLC 基准 (BattleKeywords-a1c9p2.json) | 残像纠缠4阶段 - 使自身的最小与最大速度值-2 - 自身攻击命中时，触发以下效果  · 对目标施加... |
| `TimeEntangleOne` | **一重残像纠缠** | LLC 基准 (BattleKeywords-a1c9p2.json) | 残像纠缠1阶段 - 自身攻击命中时，触发以下效果   · 使目标增加2级烧伤 强度 |
| `TimeEntangleThree` | **三重残像纠缠** | LLC 基准 (BattleKeywords-a1c9p2.json) | 残像纠缠3阶段 - 自身攻击命中时，触发以下效果  · 使目标增加2级流血 强度  · 下回合对目标... |
| `TimeEntangleTwo` | **二重残像纠缠** | LLC 基准 (BattleKeywords-a1c9p2.json) | 残像纠缠2阶段 - 自身攻击命中时，触发以下效果  · 下回合对目标施加1层束缚   · 使目标增加... |
| `TimeEntangleUnstable` | **暴走-残像纠缠** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最大值：10 - 自身的攻击命中时，根据本效果层数触发以下效果：  · 造成(该硬币最终伤害量/... |
| `TimeGap` | **时间背离** | LLC 基准 (BattleKeywords_Refraction6.json) | - 自身每次在过去形态/现在形态/未来形态间转换时，使本效果的层数增加1层 - 受到的伤害+(本效果... |
| `TimeGapAb` | **背离** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 回合开始时，使自身部位获得相当于本效果层数的护盾 - 护盾减少时，本效果层数相应减少 |
| `TimeKillerWatch` | **时间救援目标** | LLC 基准 (BattleKeywords-tkt.json) | 时间加速 持续期间，被时间杀人魔指定为攻击目标。 |
| `TimeRental` | **心象中的时间租赁** | LLC 基准 (BattleKeywords.json) | 回合结束时，使自身获得3层迅捷 与2层伤害强化 。回合结束时，若本效果层数为1层，则下回合对自身施加... |
| `TimeRentalTwo` | **T公司的时间租赁** | LLC 基准 (BattleKeywords-tkt.json) | 回合结束时： - 下回合使自身获得(时间租赁 层数-1)层迅捷 、拼点威力提升 与易损 。 - 若层... |
| `TimeRentalTwoPersonality` | **时间租赁** | LLC 基准 (BattleKeywords.json) | 回合结束时若本效果的层数不低于2层： - 下回合使自身获得(时间租赁 层数-1)层迅捷 、拼点威力提... |
| `TimeRental_Re` | **时间租赁** | LLC 基准 (BattleKeywords_Refraction2.json) | 回合结束时，使自身获得3层迅捷 ，2层伤害强化 与2层攻击等级提升 。 回合结束时，若本效果层数为1... |
| `TimeSuspend` | **时间延付** | LLC 基准 (BattleKeywords.json) | - 带有本效果时，受到的伤害将被暂存。 - 战斗结束时，若本效果的层数为1层，则自身受到暂存的伤害(... |
| `TimesCoinValueDown` | **乘算硬币弱化** | LLC 基准 (BattleKeywords.json) | 变动值为乘算的技能硬币威力减少等同于本效果层数的数值。 |
| `TimesCoinValueUp` | **乘算硬币强化** | LLC 基准 (BattleKeywords.json) | 变动值为乘算的技能硬币威力提高等同于本效果层数的数值。 |
| `TinyCarmilla` | **小卡蜜拉** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：3 - 每次获得本效果时使自身增加2级流血 强度 - 回合结束时，对自身施加2层流血  ... |
| `Tipsiness` | **醉意** | LLC 基准 (BattleKeywords.json) | 拼点威力减少等同于本效果层数的数值。(最多5层) |
| `TipsinessRail` | **醉意** | LLC 基准 (BattleKeywords_Refraction2.json) | 拼点威力减少等同于本效果层数的数值(最多5层) |
| `TrainTeamCaptain` | **培训部队长** | LLC 基准 (BattleKeywords-walpu4.json) | 该人格的行动槽+1 将该人格的一个1技能替换为3技能 回合开始时恢复15点理智值 自身技能施加的烧伤... |
| `TransparentWingScales` | **锐利的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的“罗生-显现”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `TransparentWingScalesExplain` | **锐利的鳞粉** | LLC 基准 (BattleKeywords_Refraction6.json) | - 与罗生蝶::蛹使用的技能“罗生-显现”拼点的技能对应的攻击类型与罪孽属性的抗性+0.25 |
| `TraumaShield` | **精神屏蔽力场** | LLC 基准 (BattleKeywords-walpu6.json) | - 受到来自敌方单位的理智伤害-80% - 受到的沉沦 伤害-80% - 回合结束时，使本效果的层数... |
| `TrulyWeak` | **弱者** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 造成的伤害-10% |
| `UltraPrecisionTimeAcceleration` | **超精密时间加速** | LLC 基准 (BattleKeywords-tkt.json) | 自身的基础最小与最大速度值增加相当于本效果层数的数值 增加震颤 强度，施加震颤 层数或造成震颤引爆 ... |
| `UncontrolledChargeAxe_LowMorale` | **充能回路逆流** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 与带有破裂 的目标进行拼点时，使自身获得3层充能 并对自身施加1层易损 (每回合最多2... |
| `UncontrolledChargeAxe_Panic` | **充能回路逆流** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 与带有破裂 的目标进行拼点时，使自身获得5层充能 与1层伤害强化 并对自身施加2层易损... |
| `UnfairDistribution` | **内部分裂** | LLC 基准 (BattleKeywords-tkt.json) | 消耗共享的时间 时，所有的脑不再消耗相等的时间。 回合开始时：使所有部位获得与其剩余时间不同的部位数... |
| `UnfinishedDream` | **关于自浓于水之血中解放出来，** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 每回合结束时，下回合使自身获得1层迅捷 与3层攻击等级提升  - 每满3回合后，使自身额外获得2... |
| `UnfinishedDreamMirror` | **关于自浓于水之血中解放出来，** | LLC 基准 (BattleKeywords_Mirror6.json) | - 每回合结束时，下回合使自身获得1层迅捷 与3层攻击等级提升  - 每满3回合后，使自身额外获得2... |
| `UnfinishedDreamSancho` | **关于无法自浓于水之血中解放，** | LLC 基准 (BattleKeywords-a1c7p1.json) | - 使自身获得硬血 时，额外获得2层硬血 。(每回合最多5次) - 每回合结束时，下回合使自身获得2... |
| `UnfinishedDreamSanchoMirror` | **关于无法自浓于水之血中解放，** | LLC 基准 (BattleKeywords_Mirror6.json) | - 使自身获得硬血 时，额外获得2层硬血 。(每回合最多5次) - 每回合结束时，下回合使自身获得2... |
| `UninvitedGuest` | **不速之客** | LLC 基准 (BattleKeywords_Refraction4.json) | 带有不速之客 的人格阵亡时，转移到未带有本效果的人格上。 |
| `UninvitedGuestPersonality` | **不速之客** | LLC 基准 (BattleKeywords.json) | - 最大值：2 - 自身阵亡时，使最后的攻击者恢复3点理智值，然后随机对未带有本效果的友方单位施加2... |
| `Unjust_Enrichment` | **不义之财** | LLC 基准 (BattleKeywords.json) | - 正面命中带有流血 的目标时，使本效果层数增加(最多4层) - 当被动子弹很贵触发时，消耗所有本效... |
| `UnlockBuffAlly_1` | **解放 - I** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 防御等级+1 - 战斗结束时，使自身恢复5点理智值 |
| `UnlockBuffAlly_2` | **解放 - II** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 防御等级+2 - 战斗结束时，使自身恢复10点理智值 |
| `UnlockBuffAlly_3` | **解放 - III** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 防御等级+3 - 战斗结束时，使自身恢复15点理智值 |
| `UnlockBuff_1` | **解放 - I** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 攻击等级+1，防御等级+1 - 战斗结束时，使自身恢复15点理智值 |
| `UnlockBuff_2` | **解放 - II** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 攻击等级+2，防御等级+2 - 战斗结束时，使自身恢复30点理智值 |
| `UnlockBuff_3` | **解放 - III** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 攻击等级+3，防御等级+3 - 战斗结束时，使自身恢复45点理智值 |
| `UnlockBuff_Base` | **解放** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 自身的指令加护 层数不低于一定值时，使自身获得本效果 - 根据自身的指令加护 层数，使本效果阶段... |
| `UnlockBuff_Rien1` | **解放 - I** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级+1，防御等级+1 - 战斗结束时，使自身恢复10点理智值 |
| `UnlockBuff_Rien2` | **解放 - II** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级+2，防御等级+2 - 战斗结束时，使自身恢复20点理智值 |
| `UnlockBuff_Rien3` | **解放 - III** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 攻击等级+3，防御等级+3 - 战斗结束时，使自身恢复30点理智值 |
| `Unobservable` | **无法观测** | LLC 基准 (BattleKeywords-a1c6p3.json) |  |
| `UnresolvedFeelings` | **多层拼布** | LLC 2026092102／本地格式化 | - 最大值：30 - 使自身增加相当于本效果层数的防御等级 - 受到带有“感谢聆听”的目标攻击时，使本效果层数减少相当于“感谢聆听”层数(每回合每名人…… |
| `UnstableFeeling` | **不稳定的激情** | LLC 基准 (BattleKeywords.json) | - 攻击命中时，使目标增加1级烧伤 强度 - 主要目标带有烧伤 时，使自身技能最终威力+1 -  战... |
| `Unstable_LowMorale` | **分裂** | LLC 基准 (Bufs-a1c6p1.json) | - 士气低落 - 每次拼点使自身失去2点体力。回合开始时，使自身获得1层攻击等级提升 。 |
| `Unstable_Panic` | **分裂** | LLC 基准 (Bufs-a1c6p1.json) | - 陷入恐慌 - 每次拼点使自身失去3点体力。回合开始时，使自身获得2层攻击等级提升 。 |
| `UnsteadyTheRings` | **剧烈振动的甲胄** | LLC 基准 (BattleKeywords-a1c9p1.json) | - 最大值：3 - 使用“受压肉体”时，每带有1层本效果，使该技能的最终威力-10 - “受压肉体”... |
| `UnstoppableFunny` | **无法停止的欢喜** | LLC 基准 (BattleKeywords-a1c7p2.json) | 阵亡时 - 分别获得持有量最少的3种E.G.O资源各1个 - 对1名敌方单位施加3层流血 (优先选择... |
| `UsedTooMuchPower` | **好像用力过猛了** | LLC 基准 (BattleKeywords-walpu6.json) | - 最大值：1 - 回合结束时，自身脱离战斗 |
| `VendettaMark` | **复仇对象** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 被特定技能或被动消耗 - 每带有1层本效果，使自身受到来自属于中指的敌方单位的... |
| `VengeanceBookHeathcliff` | **复仇账簿[希斯克利夫]** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 每带有5层本效果，使自身的攻击等级+1，防御等级+1 |
| `VengeanceBookSinclair` | **复仇账簿[辛克莱]** | LLC 基准 (BattleKeywords.json) | - 最大值：30 - 使自身造成的伤害+(本效果层数)%(最多+30%) - 根据本效果层数在下回合... |
| `VengeanceBookSpider` | **复仇账簿** | LLC 基准 (BattleKeywords-a1c9p3.json) | 中指 父辈 - 马蒂亚斯或中指 子辈 - 绮罗的技能命中带有本效果的目标时，使攻击者恢复7点理智值(... |
| `Vengeance_LowMorale` | **复仇** | LLC 基准 (Bufs-a1c6p2.json) | - 士气低落 - 对自身施加3层防御等级降低 并使自身获得3层伤害强化 |
| `Vengeance_Panic` | **复仇** | LLC 基准 (Bufs-a1c6p2.json) | - 陷入恐慌 - 对自身施加6层防御等级降低 并使自身获得5层伤害强化 |
| `VerEmergencyCandy` | **备用糖果** | LLC 基准 (BattleKeywords_Mirror6.json) | 回合结束时，若现存体力不高于体力上限的60% 则使自身恢复体力上限30%的体力，恢复15点理智值，自... |
| `VerHunger` | **饥饿** | LLC 基准 (BattleKeywords_Mirror6.json) | 最大值：3 回合结束时，每带有1层本效果，下回合使自身获得2层攻击等级提升 与1层伤害强化  若本效... |
| `VerShiningFullness` | **光辉的饱腹感** | LLC 基准 (BattleKeywords_Mirror6.json) | 本场战斗期间，使自身基础体力上限增加30% 回合开始时，使自身恢复全部体力与理智值(每场战斗最多1次... |
| `VergiliusSin` | **心-猩红视线** | LLC 基准 (BattleKeywords-a1c9p3.json) | 造成的暴怒伤害+50% |
| `Vespa_LowMorale` | **不快** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 士气低落 - 使自身获得1层突刺威力提升 并对自身施加1层理智值恢复效率减少 |
| `Vespa_Panic` | **不快** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 陷入恐慌 - 使自身获得2层突刺威力提升 ，1层突刺伤害强化 并对自身施加2层理智值恢复效率减少 |
| `Veteran_LowMorale` | **第二次烟霾战争的** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 士气低落 - 回合开始时，对自身施加1层易损  - 理智值恢复效率 +2 |
| `Veteran_Panic` | **第二次烟霾战争的** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 陷入恐慌 - 回合开始时，对自身施加2层易损 并使自身获得2层拼点威力提升 |
| `Vibration` | **震颤** | LLC 基准 (BattleKeywords.json) | 受到造成震颤引爆 的攻击时，混乱阈值前移等同于本效果强度的数值。 回合结束后，本效果的层数减少1层。 |
| `VibrationAssimilation` | **震颤同步** | LLC 基准 (BattleKeywords.json) | 目标每带有5级震颤 强度，使其拼点威力-1 |
| `VibrationBleeding` | **震颤-大出血** | LLC 基准 (BattleKeywords.json) | - 被震颤引爆 时，受到(自身的震颤 强度与流血 强度之和/2)点色欲伤害，并使自身的流血 层数减少... |
| `VibrationChain` | **震颤-锁链** | LLC 基准 (BattleKeywords-tkt.json) | - 每带有10级震颤 强度，使自身的拼点威力-1(最多-3) - 受到造成震颤引爆 的攻击时，混乱阈... |
| `VibrationChainPersonality` | **震颤-锁链** | LLC 基准 (BattleKeywords.json) | - 每带有10级震颤 强度，使自身的拼点威力-1(最多-3) - 受到造成震颤引爆 的攻击时，混乱阈... |
| `VibrationCollapse` | **震颤-崩坏** | LLC 基准 (BattleKeywords.json) | 目标每带有4级震颤 强度，防御等级减少1级 受到造成震颤引爆 的攻击时，混乱阈值前移 回合结束后，本... |
| `VibrationContinue` | **震颤-永恒** | LLC 基准 (BattleKeywords.json) | - 技能或硬币效果使自身震颤引爆 时，以(自身的震颤 强度)%的概率额外震颤引爆 1次。(最多50%... |
| `VibrationCrack` | **震颤-裂痕** | LLC 基准 (BattleKeywords.json) | - 若陷入混乱时，自身的震颤 强度与层数之和不低于20点，则使自身的混乱阶段加深1层 - 该效果不能... |
| `VibrationDistribution` | **震颤-分配** | LLC 基准 (BattleKeywords-tkt.json) | - 回合结束时，下回合使自身获得(全体友方单位震颤 层数之和/友方单位存活数)层攻击等级提升 (最多... |
| `VibrationEcho` | **震颤-回响** | LLC 基准 (BattleKeywords.json) | - 被震颤引爆 时，受到等同于本效果强度的怠惰伤害。 - 受到造成震颤引爆 的攻击时，混乱阈值前移等... |
| `VibrationExplosion` | **震颤引爆** | LLC 基准 (BattleKeywords.json) | 使目标的混乱阈值前移与震颤 强度相同的数值 |
| `VibrationIgnition` | **震颤-灼热** | LLC 基准 (BattleKeywords-a1c8p3.json) | - 被震颤引爆 时，受到(自身的震颤 强度与烧伤 强度之和/2)点暴怒伤害，并使自身的烧伤 层数减少... |
| `VibrationNesting` | **震颤-叠加** | LLC 基准 (BattleKeywords-tkt.json) | - 通过振幅纠缠 获得。 - 振幅转换 时，使震颤-叠加 增加该特殊震颤 的效果。 |
| `VibrationSpring` | **震颤-上弦** | LLC 基准 (BattleKeywords.json) | - 最大速度值+2 - 通过自身的技能或硬币效果增加震颤 强度或施加震颤 层数时，消耗自身的1层震颤... |
| `VillainMark` | **恶人标记** | LLC 基准 (BattleKeywords-walpu6.json) | - 受到来自堂吉诃德攻击的伤害+10%  - 仅施加给每回合首个施加的目标 |
| `VioletDamageDown` | **嫉妒伤害弱化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数降低嫉妒技能造成的伤害。(最多10层) |
| `VioletDamageUp` | **嫉妒伤害强化** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数提高嫉妒技能造成的伤害。(最多10层) |
| `VioletPeccatulumTwo` | **嫉妒罪种 2型** | LLC 基准 (BattleKeywords_Refraction4.json) | - 造成的伤害+15% - 受到的伤害-15% - 带有本效果的单位获得嫉妒罪种2型光环效果 |
| `VioletResistDown` | **嫉妒抗性弱化** | LLC 基准 (BattleKeywords.json) | 目标的嫉妒抗性增加(每层0.1) |
| `VioletResistUp` | **嫉妒抗性强化** | LLC 基准 (BattleKeywords.json) | 目标的暴怒嫉妒减少(每层0.1) |
| `VioletResultDown` | **嫉妒威力降低** | LLC 基准 (Bufs.json) | 本回合内嫉妒技能的最终威力-{0} |
| `VioletResultUp` | **嫉妒威力提升** | LLC 基准 (BattleKeywords.json) | 本回合内基于本效果的层数提高嫉妒技能的最终威力。 |
| `VioletTakeDamageDown` | **嫉妒守护** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数减少受到来自嫉妒技能的伤害。(最多10层) |
| `VioletTakeDamageUp` | **嫉妒易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自嫉妒技能的伤害。(最多10层) |
| `VioletUnderstand` | **理解** | LLC 基准 (BattleKeywords-walpu4.json) | 每层本效果使自身造成的伤害+5% 每层本效果使自身受到的伤害+5% (最大值：5) |
| `Vulnerable` | **易损** | LLC 基准 (BattleKeywords.json) | 一回合内基于本效果层数增加受到来自技能的伤害。(最多10层) |
| `WOverCharge` | **过度充能** | LLC 基准 (BattleKeywords.json) | - 最大值：1 - 变为无法行动状态 - 使自身受到的伤害-(10+自身的充能 强度×5)%(最多-... |
| `WaitingXichun` | **待** | LLC 基准 (BattleKeywords.json) | - 最大值：3 - 自身解除待命或重返战斗前，自身处于待命或撤退状态的回合数 |
| `WaitingforCommandMod` | **待命状态** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 处于待命状态时，直到受到伤害前不会使用攻击技能 |
| `WanderingFootsteps` | **破灭将至** | LLC 基准 (BattleKeywords.json) | - 若目标带有理智值：目标的恐慌类型转变为“破灭” (破灭：自身士气低落时，回合结束时使自身增加3级... |
| `WanderingFootsteps_LowMorale` | **破灭** | LLC 基准 (BattleKeywords.json) | - 士气低落 - 自身的拼点威力-1。每回合结束时使自身增加3级沉沦 强度 |
| `WanderingFootsteps_Main` | **破灭将至** | LLC 基准 (BattleKeywords.json) | - 使带有理智值的目标的恐慌类型转变为“破灭” - 回合结束时，本效果的层数减少1层 |
| `WanderingFootsteps_Panic` | **破灭** | LLC 基准 (BattleKeywords.json) | - 陷入恐慌 - 自身的拼点威力-2。每回合结束时使自身增加5级沉沦 强度并对自身施加3层沉沦 |
| `WanderingFootsteps_Sub` | **破灭将至** | LLC 基准 (BattleKeywords.json) | - 硬币朝向正面的概率-10% - 回合结束时，本效果的层数减少1层 |
| `Wariness` | **戒心** | LLC 2026092102／本地格式化 | - 最大值：10 - 使自身减少相当于本效果层数的攻击等级，增加相当于本效果层数的防御等级 - 若自身拼点失败，则使本效果层数减少3层 |
| `WaterPocket` | **液囊** | LLC 基准 (BattleKeywords.json) | 基于本效果层数恢复体力。 |
| `WaveFoxUmbrella` | **保护伞** | LLC 基准 (BattleKeywords_Refraction2.json) | 使所有部位获得与本效果层数相同的守护  使用“等待”技能时，召唤与本效果层数相同数量的旧伞 每当伞被... |
| `WaveSinking` | **逆流** | LLC 基准 (BattleKeywords.json) | - 最大值：3 受到攻击时，使自身增加相当于本效果层数的沉沦 强度  回合结束时，若自身的理智值不高... |
| `WeakWithering_LowMorale` | **胡乱缝纫** | LLC 2026092102／本地格式化 | - 士气低落 - 回合开始时，对自身施加1层攻击等级降低  |
| `WeakWithering_Panic` | **胡乱缝纫** | LLC 2026092102／本地格式化 | - 陷入恐慌 - 回合开始时，对自身施加1层攻击等级降低 与1层伤害弱化  |
| `Weak_Chicken` | **鸡群的末日菜肴** | LLC 基准 (Bufs.json) | 因罪人的菜肴引发的反应。失去体力上限40%的体力 |
| `WeakenDOQ` | **苦厄灾难** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 攻击等级-？？ - 防御等级-？？ |
| `WeaknessAnalysis` | **弱点分析** | LLC 基准 (BattleKeywords.json) | 本回合内随机使1个抗性等级为“耐性”或“一般”的攻击类型[承伤系数+0.2]。 |
| `WeighedMurderousIntend` | **深深压抑的杀气** | LLC 基准 (BattleKeywords-a1c9116.json) | 基础攻击等级-25，基础防御等级-25 |
| `WeighedMurderousIntendHard` | **深深压抑的杀气** | LLC 基准 (BattleKeywords-night-clean-up-re.json) | 基础攻击等级-15，基础防御等级-15 |
| `WeightOfResponsibility_LowMorale` | **是时候放弃我的梦了…** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 士气低落 - 使自身获得2层强壮 并对自身施加1层易损 ，自身的最大速度值+2 - 恢复的体力+... |
| `WeightOfResponsibility_Panic` | **作为父亲，为了家人…** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 陷入恐慌 - 使自身获得2层强壮 与2层迅捷 ，并对自身施加2层易损  - 恢复的体力+50% ... |
| `Whistle_Courage` | **战胜恐惧的勇气** | LLC 基准 (Bufs.json) | 回合开始时，获得1层强壮 和2层守护 。 |
| `Whistle_Fear` | **令人恐惧的哨音** | LLC 基准 (Bufs.json) | 回合开始时，施加1层束缚 和1层麻痹 。 |
| `WideAreaRampage` | **广域乱射** | LLC 基准 (BattleKeywords.json) | - 本技能掷出硬币时，随机对其目标之一的1名单位进行攻击 · 第一枚硬币必定命中主要目标 · 每枚硬... |
| `WildHunt` | **狂猎** | LLC 基准 (BattleKeywords.json) | - 自身首次获得狂猎 的回合内，剩余体力维持为1点；回合结束时，使自身恢复体力上限50%的体力并使自... |
| `WildernessSurvivalModule` | **小帮手-野外维生单元** | LLC 基准 (BattleKeywords-pilgrimage.json) | - 体力上限+20%，通过技能、被动与状态效果恢复的体力+40% |
| `WillAwakenSinclair` | **心-某个辛克莱** | LLC 基准 (BattleKeywords-a1c9p3.json) | - 最小与最大速度值+3 - 单方面攻击造成的伤害+20% - 自身的技能使自身增加的呼吸法 强度额... |
| `WindBlade` | **墨工坊-锐 二式拔刀/动力：鬼怪之火** | LLC 基准 (BattleKeywords-exme.json) | - 最大值：20 - 每带有1层本效果，使自身造成的斩击伤害+1%(最多+10%) - 每带有2层本... |
| `WindBladeIshmael` | **墨工坊-锐 二式拔刀/动力：鬼怪之火** | LLC 基准 (BattleKeywords.json) | - 最大值：20 - 每回合最多获得10层本效果 - 每带有1层本效果，使自身斩击基础攻击技能造成的... |
| `WitheredWood_LowMorale` | **古木化** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 士气低落 - 使自身获得1层伤害强化 并对自身施加1层易损 与1层破裂易损 |
| `WitheredWood_Panic` | **古木化** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 陷入恐慌 - 使自身获得2层伤害强化 并对自身施加2层易损 与2层破裂易损 |
| `WornHeart` | **磨灭的心** | LLC 基准 (BattleKeywords-a1c7p3.json) | - 最大值：10 - 关卡开始时自身带有3层本效果 - 回合开始时，每带有1层本效果，使自身获得1层... |
| `WornHeartGreg` | **磨灭的心** | LLC 基准 (BattleKeywords.json) | - 最大值：10 - 回合结束时，获得1层本效果 - 回合开始时，自身每带有3层本效果，使自身获得1... |
| `WornOutKnight` | **饱经风霜的骑士** | LLC 基准 (BattleKeywords-walpu6.json) | 本回合使自身受到的伤害+100% |
| `WrappedCurseTag` | **纠缠的咒符** | LLC 基准 (BattleKeywords.json) | 每层本效果使自身造成的伤害+1% 若本效果层数不低于9层，则在回合开始时对自身施加2层虚弱 。 |
| `WrappedCurseTagRe` | **纠缠的咒符** | LLC 基准 (BattleKeywords_Refraction2.json) | - 最大值：9 - 每层本效果使自身造成的伤害+1% - 若本效果层数为9层，则在回合开始时对自身施... |
| `YellowHarpoon` | **蜜黄标枪** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 回合开始时，使自身获得4层迅捷 并使自身增加8级呼吸法 强度 - 回合结束时，若有带有穿刺标枪 ... |
| `YellowHarpoonSin` | **心-蜜黄标枪** | LLC 基准 (BattleKeywords-a1c9p2.json) | - 基础攻击等级+3，基础防御等级+3 - 攻击上回合攻击自身的目标时，使自身恢复3点理智值 - 若... |
| `YesdragonBurst` | **刃棘** | LLC 基准 (BattleKeywords.json) |  |
| `YesdragonNodie` | **不许** | LLC 基准 (BattleKeywords.json) | 受到使自身体力降至0点的伤害时，本回合自身体力不会低于1点，解除自身因受到伤害而陷入的混乱 触发以上... |
| `YesdragonPower` | **龙气** | LLC 基准 (BattleKeywords_Refraction6.json) | - 受到的伤害-100% - 受到攻击后，在该技能结束后解除本效果 |
| `YesdragonScale` | **覆盖的鳞片** | LLC 基准 (BattleKeywords_Refraction6.json) | - 最大值：20 - 层数为0层时不会解除本效果 - 受到来自葬花针 的伤害时，使本效果层数减少1层... |
| `YesdragonSelf` | **葬花针** | LLC 基准 (BattleKeywords.json) | 最大值：20 - 回合结束时或受到攻击时，获得1层本效果 - 每带有5层本效果，使自身增加1级攻击等... |
| `YesdragonSelfRefraction` | **葬花针** | LLC 基准 (BattleKeywords_Refraction6.json) | - 最大值：10 - 本效果层数每有2层，使自身增加1级攻击等级与1级防御等级 - 若本效果层数不低... |
| `YesdragonWind` | **变化无常的慈悲** | LLC 基准 (BattleKeywords_Refraction6.json) | - 最小与最大速度值+3 - 拼点威力+2 - 受到攻击后，在该技能结束后解除本效果 |
| `YisangParryGubo` | **责任感** | LLC 基准 (BattleKeywords-a1c8p3.json) | 与仇甫进行拼点时，使自身的拼点威力+2 |
| `YisangWeapon01Hatchet` | **用手斧将肋骨砍下时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为打击伤害 - 未摧毁并命中时，使自身增加2级呼吸法 强度 |
| `YisangWeapon02Stiletto` | **用锥将肺贯穿时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为突刺伤害 - 未摧毁并命中时，使目标增加2级沉沦 强度 |
| `YisangWeapon03Greatsword` | **用手半剑将肩膀击碎时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为斩击伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，下回合使自身获得1层... |
| `YisangWeapon04Rapier` | **应该用刺剑在身体上开超过十个洞时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为突刺伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，下回合对目标施加1层... |
| `YisangWeapon05Sledgehammer` | **应该用锤子将后脑敲碎时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为打击伤害 - 此硬币造成的伤害+5% - 未摧毁并命中时，使目标的混乱阈值前移... |
| `YisangWeapon06Ultragreatsword` | **应该用大剑将躯干劈开时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为斩击伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施... |
| `YisangWeapon07Lance` | **应该用长枪刺穿一个20英寸的洞时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为突刺伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施... |
| `YisangWeapon08Chain` | **应该用鞭子抽落上万块肉时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为打击伤害 - 此硬币造成的伤害+15% - 未摧毁并命中时，直到下回合对目标施... |
| `YisangWeapon09Scythe` | **应该用镰刀…像某人一般沿着空间斩裂时…** | LLC 基准 (BattleKeywords.json) | - 此硬币造成的伤害为斩击伤害 - 此硬币造成的伤害+30% - 未摧毁并命中时，必定暴击 |
| `Yummy_Lowmorale` | **变好吃了** | LLC 基准 (BattleKeywords-x1p1c1.json) | - 士气低落 - 回合开始时，对自身施加1层易损 |
| `Yummy_Panic` | **变好吃了** | LLC 基准 (BattleKeywords-x1p1c1.json) | - 陷入恐慌 - 回合开始时，对自身施加2层易损 |
| `Yurodivy_LowMorale` | **瓦解的同盟** | LLC 基准 (BattleKeywords-tkt.json) | - 士气低落 对自身施加1层易损 。受到攻击时对自身施加1层震颤 。(最多3次) |
| `Yurodivy_Panic` | **瓦解的同盟** | LLC 基准 (BattleKeywords-tkt.json) | - 陷入恐慌 对自身施加2层易损 。受到攻击时对自身施加2层震颤 。(最多3次) |
| `Zazen` | **禅那** | LLC 基准 (BattleKeywords.json) | - 最大值：108 - 每带有1层本效果，造成的伤害+1% |
| `ZiluDebuff` | **杀气抑制** | LLC 基准 (BattleKeywords-a1c8p2.json) | - 基础攻击等级减少20级，基础防御等级减少20级 |
