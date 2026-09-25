---
name: limbus-company-localization
description: >-
  Comprehensive guide and toolchain workflow for 《边狱公司》（Limbus Company）Chinese localization
  under the Urban Zero Association (都市零协会 LLC) architecture. Use when translating, proofreading,
  linting, packaging, or deploying Limbus Company game assets (skills, passives, buffs, story dialogues,
  UI text, and RPG exploration), enforcing the 8 localization safety rules, and running release gates.
---

# Limbus Company 本地化汉化专家技能

本技能专门指导《边狱公司》（Limbus Company）游戏资源的本地化汉化工作。项目基于都市零协会（LLC）技术架构，旨在为玩家提供稳定、符合官方与原著风格的高质量中文文本。

---

## 1. 核心架构与目录认知

- **翻译工作区源文件**：`workspace/LLC_zh-CN/`
  - `Skills_*.json`, `Passives_*.json`：战斗技能与被动机制
  - `BattleKeywords-*.json`, `Bufs-*.json`：关键词与状态效果（增益/减益）
  - `Enemies-*.json`, `PanicInfo-*.json`：敌方信息、恐慌机制与战斗台词
  - `MainUIText-*.json`, `BattlePass-*.json`：系统 UI、通行证与节点提示
  - `StoryData/*.json`：主线剧情对话（按小节编排）
  - `RPGSystem/*.json`：迷宫探索与 RPG 互动系统
  - `PersonalityVoiceDlg/*.json`：人格台词与语音
- **自动化工具链**：`tools/`
  - `linter.py`：静态代码检查与安全自动修复引擎（本地门禁规则）
  - `package_release.py`：双版本发布打包脚本（完整版 + 仅战斗辅助版）
  - `verify_release.py`：基准冻结比对与增量回归门禁
  - `deploy_mod.py`：Steam 原生本地化部署与更纱黑体字库注入
- **测试套件**：`tests/e2e/`
  - `run_tests.py`：四层分级端到端测试套件（Tier 1~4，共 116 项检查）

---

## 2. 本工作区门禁规范 (速查)

| 门禁 ID | 严重级别 | 规范名称 | 核心要求与原理 |
| :--- | :--- | :--- | :--- |
| **L01** | FATAL | JSON 与编码完整性 | 严格合法的 UTF-8（无 BOM），符合 `dataList` 等外层架构，无残缺截断。 |
| **L02** | FATAL | 绝对零全角波浪号 | **严禁使用 `～` (`\uFF5E`) 与 `〜` (`\u301C`)**。必须统一使用半角 `~`（防止 TMP 渲染方框乱码 `□`）。 |
| **L03** | FATAL | 占位符 1:1 对齐 | `{0}`, `{1}`, `{Slot}` 必须与韩文原版数量和标识符严格一致，括号必须闭合。 |
| **L04** | ERROR | 关键词后置空格 | `[关键词] ` 必须紧跟一个半角空格（本地格式约定，悬浮窗需实机验证）。 |
| **L05** | FATAL | TextMeshPro 标签配对 | 成对标签（`<color>`, `<b>`, `<i>`, `<size>`, `<mark>` 等）严格闭合并遵循 LIFO 嵌套。 |
| **L06** | ERROR | 动词三元法则 | 正面层数用 **获得**；负面层数用 **施加**；数值/强度用 **增加** / **减少**；消耗衰减用 **消耗** / **降低**。 |
| **L07** | WARN | 标点排版规范 | 标准中文六点省略号 `……`；全角双引号 `“”`；双破折号 `——`。禁止英文点点点 `...` 或圈圈 `。。。`。 |
| **L08** | ERROR | 韩文未译残留 | 正文文本严禁残留韩文谚文字符（仅白名单字段如 `model` 模型标识符允许）。 |
| **L09** | ERROR | 机制术语中文归一 | **严禁在机制文本中残留英文标识**（如 `[Vulnerable]`、`[Protection]`、`[ChargeNoir]`）。必须优先查阅零协会官方资料（`references/baseline-zh-CN/`）对齐官方译名；资料未收录时再行合理自译。 |

> 详细规范与语法范例参见 [rules-and-syntax.md](./references/rules-and-syntax.md)。  
> 罪人口吻与文风规范参见 [character-personas.md](./references/character-personas.md)。

---

## 3. 标准任务工作流 (Standard Runbooks)

### 任务 A：机制与技能翻译 (Combat & Mechanics)
1. 查阅基准原文（或韩文参考 `diff_new_season.json`）。
2. 在 `workspace/LLC_zh-CN/` 对应文件中编写中文：
   - 技能名与被动名尽量贴合文学典故与零协会既有译名库。
   - 词条名方括号后加空格，如 `自身获得3层[呼吸法] 与2点[呼吸法] 强度`。
   - 负面词条用施加，如 `下一回合对目标施加2层[流血] `。
3. 执行 Linter 单文件安全检测并自动修复：
   ```bash
   python3 tools/linter.py --target workspace/LLC_zh-CN/Skills_Enemy-a1c10p1.json --fix
   ```

### 任务 B：剧情与探索对话翻译 (Story & RPG)

先按[翻译资料入口](../../../docs/TRANSLATION_GUIDE.md)复用巴士 Wiki、零协会规范与本项目已译文本，只读取当前任务涉及的资料。已有设定不重复编写百科；新赛季未覆盖的词句结合已有译文与同 ID 韩文补充，只有具体冲突或歧义需要追查原始证据，不将全库审查设为翻译前置条件。文学研究按具体典故需要查阅，用户假说保留其确定程度。第十章 `chapter_n_110` 的本项目中文名为“被凝视者”，赛季 PUNCTUM 仍为“刺点”。
1. 检查对话发言人身份（`model` 或 `teller`），调取对应角色口吻人设（见 [character-personas.md](./references/character-personas.md)）：
   - 浮士德：常用第三人称“浮士德”，但原文使用第一人称时保留“我”；不得以人物倾向覆盖具体原文。
   - 良秀：先核对韩文缩写及其展开，再对照已译缩写；`battle_awaken_20401_1/2` 的同形韩文缩写有不同展开，不按字数或拼音模板自行补义。
   - 但丁：区分带尖括号的发声对白与未加括号的内心旁白，保留原文格式，不逐句添加钟表拟声词。
   - 奥提斯：对但丁常用尊称，军人式条理可供参考；称呼按原文，不能凭口吻补写立正敬礼动作。
2. 严格使用中文标点 `……` 与 `“”`。
3. 检查 Unity 富文本标签是否平衡（如 `<color=#990000>...</color>`）。

### 任务 C：全量静态质检与修复 (Linter Sweep)
在任何批量修改或提交前，执行全量门禁检查：
```bash
# 1. 安全自动修复已知标点、关键词空格与波浪号
python3 tools/linter.py --fix

# 2. 严苛门禁检测（包含韩文残留检测，警告即失败）
python3 tools/linter.py --strict --check-korean
```

### 任务 D：E2E 端到端回归测试 (Test Suite)
确保修改不破坏项目既有测试与整体契约：
```bash
python3 tests/e2e/run_tests.py
```
- Tier 1: 17 项特性覆盖测试（85+ 项）
- Tier 2: 边界与极端字符用例测试（16 项）
- Tier 3: 跨特性双向契约矩阵（10 项）
- Tier 4: 真实游戏资源与部署场景测试（5 项）
- 目标：**116/116 PASS (100%)**。

### 任务 E：打包双版本发布分发物 (Release Packaging)
根据社区不同需求，必须同时打包两种独立的 release bundle：
```bash
python3 tools/package_release.py --version 2026.09.18
```
- **完整版 (`dist/LLC_zh-CN-Full-v*.zip`)**：包含新赛季全量剧情、探索对话、UI与战斗机制。
- **仅战斗辅助版 (`dist/LLC_zh-CN-CombatOnly-v*.zip`)**：只包含战斗机制（Skills, Passives, Bufs, Enemies, BattleUI），剔除新剧情与探索对话（利用游戏原生回退机制 fallback 到原版韩文/英文），适合打算等待零协会精翻但急需中文辅助开荒战斗的纯机制玩家。

### 任务 F：本地部署与字体校验 (Steam Native Deployment)
```bash
# 部署至本地 Steam 目录并挂载 23.8MB 更纱黑体
python3 tools/deploy_mod.py
```
确保 `ChineseFont.ttf` SHA-256 哈希值匹配：`a56a06f1af27726bc5def015b61deecbbdf5ae6d954a91b1131d8a17290def35`。

---

## 4. 故障排除与高频错误速修 (Troubleshooting)

- **Q: 游戏内文字出现方块 `□` 乱码**
  - **原因**：引入了全角波浪号 `～`，或者字体未正确加载。
  - **解决**：运行 `python3 tools/linter.py --rules L02 --fix` 批量转为 `~`；并检查 `Font/Context/ChineseFont.ttf` 是否完好。
- **Q: 战斗中 Buff 悬浮窗不弹出，词条没有高亮**
  - **原因**：关键词方括号后缺少空格，例如 `[沉沦]次数`。
  - **解决**：运行 `python3 tools/linter.py --rules L04 --fix` 自动补全空格。
- **Q: 游戏加载特定关卡或技能时直接闪退（CTD）**
  - **原因**：富文本标签 `<color>` 未闭合，或存在未配对的 `{0}` 占位符。
  - **解决**：运行 `python3 tools/linter.py --rules L01,L03,L05` 查找报错行并修正闭合标签。

---

## 5. 按当前任务查阅资料

- [统一翻译资料入口](../../../docs/TRANSLATION_GUIDE.md)：巴士 Wiki、零协会文档、已译新剧情及具体问题的检索方式。
- [资源规则与语法](./references/rules-and-syntax.md)：处理占位符、标签、标点和机制句式时查阅。
- [角色口吻入口](./references/character-personas.md)：上游风格规范与项目特例，不提供自编台词模板。
- [工具命令](./references/toolchain-cheatsheet.md)：需要检查、打包或部署时查阅，并遵守当前任务授权范围。
- [词条 ID 与译名索引](../../../references/battle_keywords_glossary.md)：名称检索；完整机制以同 ID JSON 为准。
- [参考资源与版本](../../../references/README.md)：区分中文基准、冻结韩文和当前客户端原文。
