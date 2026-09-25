# 都市零协会（LLC）本地化质量门禁与语法规范速查

本参考手册详尽定义了《边狱公司》（Limbus Company）汉化工程必须遵守的 8 大质量安全门禁（L01~L08），包括其底层原理、正则表达式模式、违规示例与修复方案。

---

## 门禁规则总览

| 门禁 ID | 规则常量名 | 级别 | 违规后果 | 自动修复 |
| :--- | :--- | :--- | :--- | :---: |
| **L01** | `RULE_1_JSON_INTEGRITY` | **FATAL** | 游戏解析失败、致命黑屏或无法读档 | ❌ |
| **L02** | `RULE_2_FULLWIDTH_TILDE` | **FATAL** | TextMeshPro 缺字，渲染为方框 `□` 或导致引擎崩溃 | ✅ |
| **L03** | `RULE_3_PLACEHOLDER_PARITY` | **FATAL/ERROR** | 动态数值丢失、UI 错乱或 C# String.Format 异常闪退 | ❌ |
| **L04** | `RULE_4_KEYWORD_SPACE` | **ERROR** | 战斗中关键词无法识别为 Token，浮窗说明不弹出 | ✅ |
| **L05** | `RULE_5_TMP_TAGS` | **FATAL** | 渲染标签泄漏、颜色污染后续所有对话甚至崩溃 | ❌ |
| **L06** | `RULE_6_VERB_TRIAD` | **ERROR** | 机制术语歧义、破坏零协会统一用词哲学 | ❌/部分 |
| **L07** | `RULE_7_TYPOGRAPHY` | **WARN** | 文本排版低劣，机翻感重 | ✅ |
| **L08** | `RULE_8_KOREAN_RESIDUE` | **ERROR** | 出现未汉化韩文残留，破坏玩家沉浸感 | ❌ |

---

## 1. L01: JSON 格式与编码完整性 (JSON Integrity)

- **标准**：
  - 编码必须为无 BOM 的严格 UTF-8 (`utf-8`)。
  - 文件结构必须为有效的 JSON 对象或数组，外层通常为 `{"dataList": [...]}`。
  - 字段类型必须与原版韩文基准严格匹配（如 `"id"` 为整数或字符串，`"desc"` 为字符串等）。
- **错误排查**：
  - 逗号多余（Trailing comma）或缺少逗号。
  - 字符串中未转义的双引号 `\"`。
  - 非法 Unicode 转义字符。

---

## 2. L02: 绝对封杀全角波浪号 (Full-Width Tilde)

- **原理**：
  - Unity 引擎采用 TextMeshPro 渲染文本。游戏内挂载的字体（包括官方字体与本项目定制更纱黑体）在某些字体分支中未映射全角波浪号 `～` (`\uFF5E`) 或 `〜` (`\u301C`)。缺字时会显示为方框 `□`；是否导致底层异常或崩溃需另行复现，不能由缺字推定。
- **模式**：
  - 正则：`[\uff5e\u301c]`
- **转换规则**：
  - 一律转为半角波浪号 `~` (`\u007E`)。
  - 示例：`10～20点` ➔ `10~20点`。

---

## 3. L03: 占位符 1:1 严格对齐 (Placeholder Parity)

- **原理**：
  - 游戏运行时使用 C# `string.Format` 注入动态数值（如骰子点数、目标名称、回合数等）。
- **规则**：
  - 中文译文中的 `{0}`, `{1}`, `{Slot}` 等占位符必须与基准韩文原版完全对应。
  - 占位符数量必须 1:1，不能漏译、多译或写错变量名。
  - 严禁出现单边未闭合的大括号 `{` 或 `}`。
- **示例**：
  - 韩文：`{0}이(가) {1}을(를) 획득`
  - 正确中文：`{0}获得{1}`
  - 错误中文：`{0}获得数值`（丢失 `{1}`，运行时直接报 IndexOutOfRangeException 崩溃）

---

## 4. L04: 关键词后置空格 (Keyword Trailing Space)

- **原理**：
  - 零协会[技能规范](https://www.zeroasso.top/docs/translate/skills/)区分名称后空格与方括号键值。这里的中文方括号及空格要求来自本工作区 AGENTS.md；解析器实现与实机悬浮窗效果尚需验证。
- **规则**：
  - 所有方括号包裹的关键词 `[关键词] ` 必须紧跟一个且仅一个半角空格。
  - 本工作区按 AGENTS.md 保留后置半角空格，不自行添加句尾或标点例外。
- **示例**：
  - 错误：`使目标陷入[沉沦]状态`
  - 正确：`使目标陷入[沉沦] 状态`
  - 正确（句末）：`使目标陷入[沉沦]`
  - 正确（标点）：`自身获得[强壮]，并提升拼点威力`

---

## 5. L05: Unity TextMeshPro 标签配对与嵌套 (TMP Tag Nesting)

- **成对标签（必须成对闭合）**：
  - `<color=#RRGGBB>...</color>`
  - `<b>...</b>`
  - `<i>...</i>`
  - `<size=N>...</size>`
  - `<mark=#RRGGBB>...</mark>`
  - `<u>...</u>`, `<s>...</s>`, `<style=...>...</style>`
- **单标签（自闭合，禁止加结束标签）**：
  - `<sprite name="...">`, `<sprite=N>`
  - `<br>`
- **LIFO 嵌套原则**：
  - 后打开的标签必须先闭合。
  - 错误：`<b><color=#ff0000>文字</b></color>`（交叉闭合）
  - 正确：`<b><color=#ff0000>文字</color></b>`

---

## 6. L06: 动词三元法则 (Verb Triad)

都市零协会为确保所有战斗机制翻译的一致性与严谨性，制定了极其严格的状态效果动词规范：

| 机制类型 | 规范动词 | 严禁使用的动词 | 示例 |
| :--- | :--- | :--- | :--- |
| **正面状态层数/次数** | **获得** | 施加、赋予、得到、附加 | `自身获得3层[呼吸法] ` |
| **负面状态层数/次数** | **施加** | 获得、赋予、给予、附着、烙印 | `对目标施加2层[流血] ` |
| **状态强度 (Potency)** | **增加** / **减少** | 获得、施加、叠加、提升、扣减 | `使目标的[破裂] 强度增加4` |
| **消耗与触发** | **消耗** / **降低** | 扣除、减少、剥夺 | `消耗5点[充能] 计数` |

> **血泪教训**：严禁出现“获得破裂强度”或“施加沉沦强度”！必须使用“破裂强度增加”或“沉沦强度增加”。

---

## 7. L07: 中文标点排版规范 (Typography Standards)

- **省略号**：
  - 必须使用双字符标准中文六点省略号 `……`（`\u2026\u2026`）。
  - 严禁使用英文半角点 `...`、三点省略号 `…` 或日文圈圈 `。。。`。
- **引号**：
  - 对话使用全角双引号 `“` 和 `”`。
  - 嵌套引号使用全角单引号 `‘` 和 `’`。
  - 严禁使用西文直引号 `"` 或 `'`。
- **破折号**：
  - 使用双破折号 `——`（占两个中文字符宽度）。
  - 严禁使用减号 `-`、双减号 `--` 或全角减号 `－`。

---

## 8. L08: 韩文未译残留检测 (Hangul Residue Scan)

- **定义**：
  - 扫描 Unicode 范围 `[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]` 的韩文字符。
- **白名单机制**：
  - 允许在纯英数字符号标识、特殊美术代号或明确标注不可翻译的字段（如 `ScenarioModelCodes`, `model` 字段等）保留原生字符串。
  - 所有的 `desc`, `name`, `content`, `dialog`, `title` 字段严禁出现韩文残留。

---

## 9. L09: 机制术语零协会资料优先原则 (LLC-First Terminology)

### 核心铁律
在翻译技能、被动、状态机制（如“自身获得X层[XXX]”、“对目标施加X层[XXX]”、“消耗X层[XXX]”）时，**严禁在中文说明中直接残留英文内部代码**（如 `[Vulnerable]`、`[Protection]`、`[ChargeNoir]` 等）。

### 双层检索工作流
1. **第一优先级：强制对齐零协会官方基准语料库**
   - 优先在 `references/baseline-zh-CN/BattleKeywords.json` 与 `Bufs.json` 中检索对应的英文 ID，使用官方既定译名。
   - **基础战斗机制官方权威对照表**：
     - `Vulnerable` ➔ `易损`
     - `Protection` ➔ `守护`
     - `Enhancement` ➔ `强壮`
     - `Reduction` ➔ `虚弱`
     - `Agility` ➔ `迅捷`
     - `Endurance` ➔ `忍耐`
     - `Binding` ➔ `束缚`
     - `Taunt` ➔ `嘲讽`
     - `Laceration` ➔ `流血`
     - `Vibration` ➔ `震颤`
     - `Breath` ➔ `呼吸法`
     - `Charge` ➔ `充能`
     - `Sinking` ➔ `沉沦`
     - `Burst` ➔ `破裂`
     - `Combustion` ➔ `烧伤`
     - `AttackDmgUp` ➔ `伤害强化`
     - `AttackDmgDown` ➔ `伤害弱化`
     - `AttackUp` ➔ `攻击等级提升`
     - `AttackDown` ➔ `攻击等级降低`
     - `DefenseUp` ➔ `防御等级提升`
     - `DefenseDown` ➔ `防御等级降低`
     - `ResultEnhancement` ➔ `威力提升`
     - `ParryingResultUp` ➔ `拼点威力提升`
     - `PenetrateResultUp` ➔ `突刺威力提升`
     - `PenetrateTakeDamageUp` ➔ `突刺易损`
     - `PenetrateResistDown` ➔ `突刺抗性弱化`

2. **第二优先级：合理精当的自主翻译**
   - 当遇到全新赛季、突发更新、零协会语料库尚未收录的新专属机制名词时，结合原著文学背景、世界观设定（如第8赛季西西弗斯百货公司、黑派/红派裁缝与精纺面料工坊）和韩文字面原义进行**合理自译**。
   - **自译命名必须在同赛季所有文本（Skills、Passives、Bufs、BattleKeywords）中 100% 保持统一**，严禁同词异译。
   - *示例（S8 自译/定名对照）*：
     - `ChargeNoir` ➔ `保存`
     - `ChargeRouge` ➔ `脉动`
     - `NoirBindArmor` ➔ `黑派精纺面料`
     - `NoirSuit` ➔ `黑派华达呢大衣`
     - `NiddlePin` ➔ `针钉`
     - `NiddlePinned` ➔ `标本状态`
     - `NiddleExpected` ➔ `扎入舌头的针`
     - `Wariness` ➔ `戒备心`
     - `Realisation` ➔ `觉醒之铠`
     - `SavePlacenta` ➔ `自我保护`
     - `HorribleTerror` ➔ `可怖的循环播放`
     - `HorribleEat` ➔ `循环播放再循环`
     - `UnresolvedFeelings` ➔ `多层拼布`
     - `BloodyMucus` ➔ `洗礼[赤]`
     - `BuffetSick` ➔ `痛楚囊袋`
     - `Gourmandise` ➔ `暴走`
     - `BuffetFailed` ➔ `虚脱`
     - `Nutrition` ➔ `劫掠之物。`

