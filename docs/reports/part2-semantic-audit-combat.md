# 第十章下半（Part 2 / a1c10p2）战斗机制与语音资产深度语义精读校对报告

> **执行代理**：战斗机制与语音资产深度语义精读校对代理 (Combat & Voice Semantic Audit Agent)  
> **审查周期**：2026-09-25  
> **质量规范依据**：`AGENTS.md` (LLC Standards)、`SKILL.md` (Limbus Company Localization)、动词三元法则 (L06)、L01~L09 静态门禁  
> **对照基准数据源**：`backups/part2-scope-20260924/source-kr/` (官方韩文原版数据)  
> **门禁测试结果**：全量 10 个目标资产文件 **Linter 0 错误（FATAL: 0, ERROR: 0, WARN: 0）** | E2E 测试套件 **116/116 PASS (100%)**

> **事实修订日期**：2026-09-25（Asia/Shanghai）嘎呜
> **证据与边界**：依据 `docs/reports/part2-handoff-reaudit-20260925.md` 第三、四节及 `backups/part2-handoff-reaudit-20260925/review-*.md`、`engineering-reaudit.json` 修订；下述修复与测试记录均属本次授权修复前的历史快照，不代表当前全库结果，新的结果由主代理最终交接记录嘎呜

---

## 一、 审查资产范围与资产盘点

本报告盘点第十章下半（a1c10p2）的 10 个战斗机制与语音资产文件，共 **273 个顶层记录**（59+43+9+10+79+24+21+6+21+1），不包含展开子硬币与多阶段等级后的计数，也不以结构盘点证明全部文本已逐字精校嘎呜

| 资产文件路径 | 条目数 | 资产性质 | 审核状态 |
| :--- | :---: | :--- | :---: |
| `workspace/LLC_zh-CN/Skills_Abnormality-a1c10p2.json` | 59 | 异想体与首领战斗技能数据 | 历史审校记录（已修复 11 处） |
| `workspace/LLC_zh-CN/Passives_Abnormality-a1c10p2.json` | 43 | 异想体与首领被动能力数据 | 历史审校记录（已修复 13 处） |
| `workspace/LLC_zh-CN/Skills_Assist-a1c10p2.json` | 9 | 协助者战斗技能数据 | 历史审校记录（已修复 1 处） |
| `workspace/LLC_zh-CN/Passives_Assist-a1c10p2.json` | 10 | 协助者战斗被动数据 | 历史审校记录（已修复 2 处） |
| `workspace/LLC_zh-CN/BattleSpeechBubbleDlg-a1c10p2.json` | 79 | 战斗气泡台词数据 | 历史审校记录（已修复 1 处） |
| `workspace/LLC_zh-CN/PersonalityVoiceDlg/Voice_Rodion_Contem_10917.json` | 24 | 罗佳专属新语音资产 | 历史审校记录（未报告明确语义错误） |
| `workspace/LLC_zh-CN/Enemies-a1c10p2.json` | 21 | 敌人名称与部位命名数据 | 历史审校记录（名称抽核未发现明确身份错译） |
| `workspace/LLC_zh-CN/PanicInfo-a1c10p2.json` | 6 | 首领恐慌/士气低落机制数据 | 历史审校记录（已修复 1 处） |
| `workspace/LLC_zh-CN/BattleResultHint-a1c10p2.json` | 21 | 战败重试关卡机制提示数据 | 历史审校记录（已修复 3 处） |
| `workspace/LLC_zh-CN/AbnormalityGuides-a1c10p2.json` | 1 | 异想体观察指引说明 | 历史审校记录（未报告明确错误） |
| **合计** | **273** | **全领域战斗与语音资产** | **顶层记录盘点，不等于最终验收** |

---

## 二、 拦截并纠正的重大机制与逻辑缺陷 (P0 级重点)

在此次深度逐条韩文对照精读中，成功捕获并修正了多处**严重影响战斗关卡机制理解、硬币数值逻辑颠倒、以及描述文本被完全错位覆盖**的重大缺陷：

### 1. 异想体技能数值与硬币效果重大错位 (Skills_Abnormality)
- **ID 149501 (修剪 / 트리밍)**：
  - **韩文原文**：
    - 硬币 0: `[OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가`
    - 硬币 1: `[OnSucceedAttack] 자신의 [ChargeKhaki] 횟수 2 증가`
  - **历史错译**：硬币 0 与硬币 1 均被错误复制为 `[OnSucceedAttack] 自身的[漂流惯性] 次数增加3次`！不仅彻底丢失了原本施加目标 2 层震颤与增加 2 次震颤次数的核心机制，还把硬币 1 的自身充能次数从 2 错写为 3！
  - **精校修复**：
    - 硬币 0：`[OnSucceedAttack] 对目标施加2层[震颤] ，使目标的[震颤] 次数增加2次`
    - 硬币 1：`[OnSucceedAttack] 自身的[漂流惯性] 次数增加2次`
- **ID 149502 (裁剪 / 커팅)**：
  - **韩文原文**：硬币 0: `[OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 2 증가`
  - **历史错译**：硬币 0 被错误写为 `[OnSucceedAttack] 自身的[漂流惯性] 次数增加3次`！
  - **精校修复**：硬币 0：`[OnSucceedAttack] 对目标施加3层[震颤] ，使目标的[震颤] 次数增加2次`。

### 2. 首领机制条件判定双重否定导致逻辑彻底反向 (Passives_Abnormality)
- **ID 150102 (永不凋零的花 / 시들지 않는 꽃)**：
  - **韩文原文**：`턴 시작시 [FlowerLaurelWreath]을 보유한 적이 없으면, [散发宜人香气的月桂冠] 장착`
  - **历史错译**：`若未持有[赎罪桂冠] 的敌方单位不存在，则装备“散发宜人香气的月桂冠”`
  - **严重影响**：历史译文使用了双重否定（“未持有者不存在”等同于“所有人均已持有”），导致首领在场上没有任何人戴桂冠时触发的戴冠逻辑，被颠倒成了“只有当所有敌方单位都戴上了桂冠才触发”，与游戏机制完全相反！
  - **精校修复**：纠正为精准的逻辑直译：`若不存在持有[赎罪桂冠] 的敌方单位，则装备“散发宜人香气的月桂冠”`。

### 3. 被动技能机制整段缺失与文本错位覆盖 (Passives_Abnormality)
- **ID 150403 (品质保全 / 품질 보존)**：
  - **韩文原文**：
    - `desc`: `보호막이 있는 동안 적에게 피격 시 [ChargeNoir] 횟수 1 증가\n\n[ChargeNoir] 횟수가 10 이상이면, 강력한 스킬 사용`
    - `flavor`: `상품의 품질은 엄격하게 관리되고 보존되어야합니다.`
  - **历史缺陷**：此条目此前被后续条目 150503（验品保全）的文本完全覆盖，`desc` 仅有 `[保存] 次数在10以上时，使用强力技能`，导致第一句极其关键的核心机制——“持有护盾期间受到敌人攻击时自身充能次数增加”**整句丢失**！同时 `flavor` 背景文本也被错位覆盖为 150503 的说明。
  - **精校修复**：完整恢复第一句机制：`持有护盾期间受到敌人攻击时，自身的[保存] 次数增加1次\n\n[保存] 次数在10以上时，使用强力技能`；并将背景说明纠正为 `商品的品质必须得到严格管理并保全。`。

---

## 三、 专有名词与基准术语统一 (L09)

对战斗提示（Hints）、恐慌信息（PanicInfo）、台词气泡（SpeechBubbles）中脱离零协会基准与剧情专名的词汇进行了全量统一：

1. **黄金茧名称统一（BattleSpeechBubbleDlg）**：
   - 检查项：10SV-049 中韩文原文为 `내가 꼬무리를…… 아프게 해서 그런 건가요……?`
   - 历史译文误将黄金茧的专属爱称 `꼬무리` 译为泛称“小家伙”；而在剧情与 RPG 文本中，全篇统一命名为 **“扭扭”**（`……扭扭。喜欢。` / `不是虫子。是扭扭。`）。
   - 修复结果：统一修改为 `是因为我才哭的吗……？是因为我让扭扭……感到痛了吗……？`。
2. **关键词与特殊硬币术语归一（PanicInfo & BattleResultHint）**：
   - **`파괴 불가 코인`**：历史文本在 PanicInfo（ID 1113）与 BattleResultHint（`battleTip_11040_2`）中被写为“不可破坏硬币”，统一修正为官方基准库正式术语 **`[不可摧毁的硬币] `**。
   - **`바늘못` (NiddlePin)**：在 `battleTip_11032_1` 中曾被误写为“约定之钉”，对照基准词条修正为 **`[针钉] `**。
   - **`무저갱의 아가리`**：在 `battleTip_11038_3` 中曾被写为“无底坑巨口”，与异想体技能表 150107 统一对齐为 **「无底深渊之口」**。

---

## 四、 动词三元法则全面治理 (L06 门禁专项)

依据 LLC 动词三元法则规范，对全部正面/负面状态、数值强度/层数的变化动词进行了系统性梳理，彻底杜绝了“施加强度”、“获得负面状态”、“获得强度”等违规用词：

### 1. 负面状态自身生效：统一纠正为“对自身施加”（严禁“获得”）
- `Skills_Abnormality-a1c10p2.json`:
  - 151903 `[DefeatDuel] 下回合获得1层[束缚] ` -> `下回合对自身施加1层[束缚] `
  - 151905 `[DefeatDuel] 获得10层[伤害弱化] 与4层[麻痹] ` -> `对自身施加10层[伤害弱化] 与4层[麻痹] `
  - 149503 `[DefeatDuel] 获得4层[麻痹] ` -> `对自身施加4层[麻痹] `
  - 149504 `[DefeatDuel] 获得4层[麻痹] ` -> `对自身施加4层[麻痹] `
  - 149506 `[WhenUse] 装备了守备技能，则获得4层[麻痹] ` -> `装备了守备技能，则对其施加4层[麻痹] `
  - 150607 `[DefeatDuel] 获得1层[易损] ` -> `对自身施加1层[易损] `
  - 150405 `[WhenUse] 每获得2次数值，获得1层[易损] ` -> `每获得2次数值，对自身施加1层[易损] `
- `Passives_Abnormality-a1c10p2.json`:
  - 150303 `则本回合与下回合获得3层[易损] ` -> `则本回合与下回合对自身施加3层[易损] `
  - 150102 `- 下回合获得2层[易损] ` -> `- 下回合对自身施加2层[易损] `
  - 149504 `并获得3层[易损] ` -> `并对自身施加3层[易损] `
  - 150603 `所有黑派所属友方单位获得1层[阵型崩溃]` -> `对所有黑派所属友方单位施加1层[阵型崩溃]`
  - 151003 `下回合获得2层[易损] ` -> `下回合对自身施加2层[易损] `
- `Skills_Assist-a1c10p2.json`:
  - 40004105 `获得5层[束缚]` -> `对自身施加5层[束缚]`

### 2. 状态强度数值增加：统一纠正为“增加X点”（严禁“获得/施加强度”）
- `Skills_Abnormality-a1c10p2.json`:
  - 150106 硬币 0: `对目标施加等同于目标[余香] 强度的[震颤] 强度(分别生效)` -> `使目标的[震颤] 强度增加等同于目标[余香] 强度的数值(分别生效)`
  - 150106 硬币 0: `对目标施加等同于目标[余香] 强度的[沉沦] 强度(分别生效)` -> `使目标的[沉沦] 强度增加等同于目标[余香] 强度的数值(分别生效)`
- `Passives_Abnormality-a1c10p2.json`:
  - 151904: `获得1层[漂流惯性] 强度` -> `自身的[漂流惯性] 强度增加1点`
  - 149505: `获得1层[漂流惯性] 强度` -> `自身的[漂流惯性] 强度增加1点`
  - 150601: `获得1层[保存] 强度` -> `自身的[保存] 强度增加1点`
  - 150402: `获得1层[保存] 强度` -> `自身的[保存] 强度增加1点`
  - 150502: `获得1层[保存] 强度` -> `自身的[保存] 强度增加1点`
  - 148305: `获得2层[保存] 强度与15次[保存] 次数` -> `自身的[保存] 强度增加2点，获得15次[保存] 次数`
- `Passives_Assist-a1c10p2.json`:
  - 40004101: `获得1层[搏动] 强度` -> `自身的[搏动] 强度增加1点`
  - 40004204: `获得1层[搏动] 强度` -> `自身的[搏动] 强度增加1点`

### 3. 关键词后置空格规范（L04）与括号补全
- `Skills_Abnormality-a1c10p2.json`:
  - 150108 硬币 0: 补齐缺失的括号与后置空格：`对目标施加10点沉沦 ` -> `对目标施加10点[沉沦] `
- `Passives_Abnormality-a1c10p2.json`:
  - 151903: `自身技能命中的目标获得1层[焦油染料] ` -> `对自身技能命中的目标施加1层[焦油染料] `

---

## 五、 特殊资产结构保全确认

在本次校对中，严格遵循了前序既定工程约束，未引入任何破坏性变动：
1. **支援技能 40004104 单硬币双说明结构完好保全**：
   - 硬币 0 的两条 `coindescs`（冻结源与译文均为 `[EndCoin]` 效果）完整保留，未合并或精简嘎呜
2. **已修复的 16 组 Buff / Keyword 资产未受波及**：
   - 保持前期工作成果，未触发任何历史脚本回滚。

---

## 六、 门禁与回归验证

针对已修改的战斗与语音资产，历史记录包含目标文件静态检查与既有 E2E 回归；116 项主要面向 a1c10p1，部署项只读文件，不启动游戏，不能证明本章实机显示、战斗结算或全部语义正确嘎呜

```bash
# 1. 目标 10 个资产文件逐个静态质检 (启用严格模式与韩文残留检测)
python3 tools/linter.py --target workspace/LLC_zh-CN/Skills_Abnormality-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/Passives_Abnormality-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/Skills_Assist-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/Passives_Assist-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/BattleSpeechBubbleDlg-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/PersonalityVoiceDlg/Voice_Rodion_Contem_10917.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/Enemies-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/PanicInfo-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/BattleResultHint-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
python3 tools/linter.py --target workspace/LLC_zh-CN/AbnormalityGuides-a1c10p2.json --source-dir backups/part2-scope-20260924/source-kr --check-korean --strict
# 结果：10 个文件全部 0 FATAL, 0 ERROR, 0 WARN [PASSED]

# 2. 全量端到端 116 项测试套件回归
python3 tests/e2e/run_tests.py
# 结果：116 tests | PASS: 116 | FAIL: 0 | ERR: 0 | PASS RATE: 100.00%
```

**结论**：上述历史修复及静态通过记录不构成无瑕疵或发布验收；复审仍发现累计触发等语义问题，31 处裸数值“施加N点震颤/沉沦”未被裁定为必须批量改层，资源修复与最终门禁结果由主代理交接，本报告不预写完成状态嘎呜
