# 汉化工作报告与调研修复交接嘎呜

报告日期：2026-09-18；用途：交给具备调研能力的模型继续进行原著、剧情背景、文学互文与译文审校，并直接修复资源嘎呜

**交接结论：已完成当前交付批次的资源补齐、游戏原文对读、结构修复及部署，但没有完成系统的原著／官方预告调研，不能将“逐句复核”理解为文学考据已经完成嘎呜**

**最新阻断：中文工作区哈希仍与上次交付一致，但本次交接核验发现韩文源有两处文本更新，其中 RPG 返回主界面的提示发生了实质变化，旧发布门禁报告已不适用于当前源快照，必须先处理再重新验收嘎呜**

## 1. 当前状态与审阅边界嘎呜

- 用户已亲自查看前三关剧情，并反馈翻译质量过关；未提供具体场景 ID，不能据此扩展为全部剧情、探索或战斗实机验收通过嘎呜
- 本轮修复针对当前客户端相对冻结 LLC 原文基线的全部新增与修改资源，覆盖剧情、RPG、战斗、UI、播报员与人格／E.G.O 语音，不仅筛选文件名含 `a1c10p1` 的文件嘎呜
- 工作区已部署过，后续只编辑工作区不会自动同步到游戏，请审校通过后再重新部署嘎呜
- 打包与 GitHub 发布已按用户要求暂停，目前尚未创建发布仓库，也没有完成完整版／机制版安装包嘎呜
- 当前目录没有 Git 仓库；使用接手备份、SHA-256 清单与统一差异文件追踪变更，未创建 Git 提交嘎呜
- 本报告记录的是已经做过的工作及其证据，既有译文和本轮译文均可继续被审阅模型纠正，不应被视为术语权威或不可修改的最终稿嘎呜

## 2. 第一优先级：原文更新导致的两处待修复嘎呜

本次重新计算哈希确认，中文工作区未变，韩文源只有下列两个文件发生变化，未发现新增或删除源文件，Steam build 仍为 `25345468` 嘎呜

### P0：退出探索是否保存进度的提示失真嘎呜

- 文件：`RPGSystem/rpg-loc-ui-common-a1c10p1.json`；定位：`dataList[key=ReturnToMainUiScene].text` 嘎呜
- 当前中文仍为“要保存探索进度并返回主界面吗？”嘎呜
- 旧韩文确实询问保存探索进度后返回主界面，新韩文已改为返回“玻璃窗”时当前探索进度可能不保存，并明确自动保存发生于任务完成、楼层移动、区域移动，要求返回前确认保存状态嘎呜
- 这是直接影响玩家操作判断的实质差异，必须优先重译，完整保留红色提示标签与自动保存条件，不能只润色旧句嘎呜

### P1：以实玛利新人格语音用词更新嘎呜

- 文件：`PersonalityVoiceDlg/Voice_Ishmael_Contem_10816.json`；定位：`dataList[id=smalltalk_10816_1].dlg` 嘎呜
- 原文由 `재고를 바쁘게 팔아내면` 改为 `재고를 빠르게 팔아내면`，从忙于清库存改为快速清库存的表述，现中文“忙着清空库存”需跟随核对嘎呜
- 同句“季末特惠”“捕获更多眼球”等表达也适合结合百货公司设定重新审阅，但不要将文学猜测直接当成确定的原文含义嘎呜

完整新旧韩文、当前中文及字段路径保存在 `docs/reports/handoff-source-drift.json`，报告末尾亦附原文快照，便于脱离工作区先行研读嘎呜
本次只生成交接报告，没有修改上述两处译文，留给接手模型一并审校修复嘎呜

## 3. 已完成的资源与翻译工作嘎呜

下列人工复核数量来自本轮主代理和两名子代理的实际对读及交接记录，其中“可见字符串”“正文”“条目”“字段”口径不同且范围重叠，不能简单相加为总翻译条数嘎呜

| 范围 | 已完成工作与数量 |
|---|---|
| 全量源差分 | 扫描 2177 个韩文 JSON，识别 103 个新增文件、49 个变更文件，共 152 文件、19479 个变化叶字段，含标识和结构字段嘎呜 |
| StoryData | 对读 22 文件、1408 条记录、2048 个可见字符串字段；21 文件修改，P10616 使用经核对的正式 LLC 译文嘎呜 |
| RPG 对话 | 对读 9 文件、803 组、3255 条正文，修正 171 处说话人值并删除原文不存在的 543 个 speaker 字段嘎呜 |
| RPG 物品 | 复核 257 个非空文本字段，补译 69 个 statText 机制字段，按原文重译 84 条说明／风味文本嘎呜 |
| RPG 其他资源 | 对读 29 文件、643 个文本字段（含空白／测试文本），涉及 NPC、地点、旁白、任务、UI，修正 71 条任务说明及至少 38 处目标字段嘎呜 |
| 战斗／通用 UI 首轮 | 本域 85 个源差分文件、3597 个变化字段；补译 256 种原文字符串，并修复嵌套硬币效果、人格技能、被动与术语嘎呜 |
| 语音专项 | 对读 7 文件、171 条 dlg、74 条 desc，部分沿用与当前原文匹配的正式 LLC 译文，不能把 desc 数量全部解释为独立台词嘎呜 |
| 关键词与状态专项 | 对照原文重审 BattleKeywords-a1c10p1 与 Bufs-a1c10p1 对应的 57 个机制条目，处理强度、层数、状态、对象与时点嘎呜 |
| 敌方／异常体被动专项 | 两份文件共 60 条 desc 全条复核，源文件没有 summary 字段嘎呜 |
| 主线程交叉复核 | 逐项对读 341 个 UI／物品等字段与 51 个数字差异候选，修正礼包种类、奖励等级、触发次数及术语嘎呜 |
| 最终改动范围 | 相对接手备份，131 个汉化资源文件发生变化，完整资源与代码变化清单共 141 个文件，另有交付文档和报告嘎呜 |

### 剧情文件清单嘎呜

```text
StoryData/P10416.json    StoryData/P10616.json    StoryData/P10816.json
StoryData/S1000B.json    StoryData/S1001B.json    StoryData/S1002B.json
StoryData/S1003B.json    StoryData/S1004B.json    StoryData/S1005B.json
StoryData/S1008B.json    StoryData/S1009B.json    StoryData/S1010B.json
StoryData/S1011B.json    StoryData/S1012B.json    StoryData/S1013B.json
StoryData/S1014B.json    StoryData/S1015B.json    StoryData/S1016B.json
StoryData/S1060B.json    StoryData/S1061B.json    StoryData/S1062B.json
StoryData/S9991B.json
```

### RPG 对话范围嘎呜

| 文件内容 | 组数 | 正文数 |
|---|---:|---:|
| floor-1 | 153 | 671 |
| floor-2 | 44 | 222 |
| floor-3 | 169 | 660 |
| floor-4 | 124 | 598 |
| floor-b1 | 105 | 454 |
| floor-b2 | 128 | 436 |
| common | 77 | 174 |
| route | 2 | 39 |
| theater | 1 | 1 |

具体文件名与条目路径以覆盖报告为准，不从这张简称表猜测文件名嘎呜

### 语音专项文件嘎呜

```text
BattleAnnouncerDlg/Announcer_CallistoAlbina_53.json
BattleAnnouncerDlg/Announcer_Emporium_55.json
BattleAnnouncerDlg/Announcer_RienSora_54.json
EGOVoiceDig/Voice_EGO_Gregor_12.json
PersonalityVoiceDlg/Voice_Honglu_EastCinq_10616.json
PersonalityVoiceDlg/Voice_Ishmael_Contem_10816.json
PersonalityVoiceDlg/Voice_Ryoshu_Contem_10416.json
```

## 4. 修复过的真实问题：接手者应重点防范同类错误嘎呜

- 旧剧情生成脚本主要做词语替换，部分正文仍为韩文；另一些已经是中文的资源存在整段捏造、错配和截断，因此“无韩文残留”不是语义合格证据嘎呜
- `S1004B` 曾在末尾伪造追加 `id=217`，实际韩文原文中对应位置是一条不带 id 的记录，已恢复原位置译文并删除伪造追加记录，不应为满足连续 ID 断言再造条目嘎呜
- `S1000B` 将洗手间误译为更衣室等问题已按原文纠正，良秀相关表达也参照过既有 LLC 用语，但仍缺少系统文学审校嘎呜
- RPG 二楼、地下楼层和四楼曾出现整段剧情伪译、虚构纯度 95%、把记忆叙述改成“梯子前进”、任务来源和价格被省略等情况，已按原文修复嘎呜
- RPG 说话人曾将默尔索错误标为其他角色、鸿璐标成堂吉诃德、无说话人的叙述凭空加上角色名，已进行独立来源对照并修正嘎呜
- RPG 物品大量世界观说明曾被写成原文没有的商品外观介绍，例如衣物材质、缎带、抛光和奇点能量等，已重译 84 条；涉及自由、文明、衣服、家具、钉子、绳子、影子、颜色、泪水的文本特别值得后续文学审阅嘎呜
- 以实玛利新人格的获取／早间语音曾整段偏离原文，良秀语音也有脚数和缩略语问题，已重新对读修正嘎呜
- 战斗文本曾缺失整个 coinlist/coindescs 层级，且存在强度／层数混淆、每技能 1 次误写为 1 层、阈值大于等于误为等于、作用对象和充能转移方向错误，已恢复结构并专项复核嘎呜
- UI 曾把经验礼包译为狂气礼包、90 级奖励写成 70 级、110 级免费奖励写成购买礼包，已修正嘎呜
- 新资源里还发现两份关键词／状态文件的 94 个多余叶字段，以及 Items-a1c10p1 中 3 条源文不存在的物品记录，已删除并加入检查嘎呜

以上是已发现并修复的实例，不意味着同类问题在全部历史译文中已被彻底排除嘎呜

## 5. 做过什么调研、没有做什么调研嘎呜

### 实际使用的依据嘎呜

- 当前客户端韩文文本是本轮翻译校验的主要依据，必要时对照英文，例如并列条件中的“强度不少于 3、层数不少于 12”嘎呜
- 参照现有 LLC 文风、术语、角色口吻材料与相邻游戏文本，复用可与原文匹配的正式 LLC 译文，未使用 GLM 翻译嘎呜
- 冻结了 LLC Git 基线 `231a8bcfc347273e7769b70ebc4f9f3e2fecaa5a`，另参考正式发布包 `2026090501`，二者用途不同，不要把较早 Git 基线当作发布当天的最新译文嘎呜

### 明确未完成的研究嘎呜

- 未系统通读或核对默尔索原型《局外人》，未建立小说段落、角色性格、叙述语体与本次游戏文本的对应关系嘎呜
- 未系统整理本次新主线官方预告、宣传文案、官方访谈／开发者说明，也没有逐项记录其与当前实装剧情的关系嘎呜
- 未完成原著典故、法语词源、宗教引文、哲学用语、品牌命名和剧情意象的证据链考据嘎呜
- 没有“原著引文—官方改写—韩文原句—中文译法—出处”对照表，因此当前文案不能称为已完成文学互文审校嘎呜

建议调研模型先查《局外人》及官方材料；“西西弗斯”等名称可作为检索其他作品的线索，但关联作品及对应段落须有证据，不能仅凭名称或主题相似便强行套用典故嘎呜

## 6. 现用译名与文学复核重点嘎呜

现用译名仅是跨文件一致性起点：默尔索、鸿璐、雷诺阿、勒鲁日、勒卡其、西西弗斯百货公司、阿内特、调色盘、腻子、奈基德、利纳莫维布尔、鲜肉苏打、米莫萨、古斯塔夫、奎利安、杜布瓦、法兰绒、毛毡、两件套、单脚、玛普丝、黄金松脂、黄金皮革、黄金线团、金枝、影界、象征界、修补室、修补师、幸福衣柜、弧形落地灯、骨衣架嘎呜

- `달퐁이` 目前音译为“达蓬”，仅在 NPC 尸骸名称处发现，英文资源亦未翻译，缺少外部命名依据，适合列入待考证表嘎呜
- “影界／象征界”等涉及概念的译法、“雷诺阿／勒鲁日／勒卡其”等品牌名称、法国人名及艺术相关称谓，需要结合原文词形、游戏语境和可靠外部资料复核嘎呜
- 检查默尔索叙述是否被过度抒情、过度解释或擅自补充心理活动，保留原文的事实、含混、重复与冷静口吻，不要为了“像原著”而改写游戏有意做出的变化嘎呜
- 优先审阅太阳、炎热、凝视、审判、母亲、神父、信仰等实际出现的表述，再判断它们是否构成可证实的互文；没有出现的主题不要凭印象补入嘎呜
- 原文故意重复、截断或不完整的引文不可擅自补全，例如部分风味文本曾被旧译自行补成更完整的宗教引文，本轮已纠正这种做法嘎呜
- 改术语时需同时检查剧情正文、speaker/teller、NPC 名称、物品、任务目标、UI、人格标题、战斗关键词及语音；直接全文替换容易误伤普通名词或内部标识嘎呜

## 7. 验证结果及不能据此宣称的结论嘎呜

以下数字对应上一次实际部署的冻结资源，当前两处韩文更新尚未重新验收嘎呜

| 项目 | 已有结果 | 解释 |
|---|---|---|
| 既有 linter 测试 | 67/67 | 检查规则实现，不证明语义准确嘎呜 |
| 真实资源集成测试 | 3/3 | 检查覆盖、部署、过期报告拒绝、旧文件删除、伪造新增条目、暂存目录隔离嘎呜 |
| 现有 E2E | 116/116 | 读取 JSON、配置、字体，未实际操作游戏场景嘎呜 |
| 全库静态扫描 | 2162 JSON | 原始扫描仍有 25834 项历史告警，退出码 1 嘎呜 |
| 本次范围门禁 | 零覆盖问题、零新增阻断 | 只表示当时新增范围及改动字段通过，当前源已变化须重跑嘎呜 |
| 文件部署 | 2163 文件哈希一致 | 含字体文件，不证明字体实际挂载嘎呜 |
| 代理实机 | 启动页与中文标签可见 | 登录后的菜单、剧情、探索、战斗浮窗未由代理验证嘎呜 |
| 用户实机反馈 | 前三关剧情质量过关 | 属用户补充验证，尚未写回较早的 runtime JSON，阅读时以本条补充为准嘎呜 |

历史告警为 1263 FATAL、24546 ERROR、25 WARN，门禁仅在中文字段和韩文源字段都与冻结基线相同时将其归入历史项，编码／JSON 及禁用波浪号问题不作此类豁免嘎呜
6 个历史占位符频次告警系译文重复已有参数，25 个历史排版警告已复核归类；其他历史问题不能仅凭“以前就有”判为误报，更不能说全部已修复嘎呜
启动日志存在 TLS 证书校验错误，尚未确认是否影响登录，采集的新启动日志未出现此前的配置占用和 JsonDataList／Exception 错误，这些结论仅限当时启动阶段嘎呜

## 8. 文件位置、证据与修复入口嘎呜

项目根目录嘎呜

```text
/home/buxinzi/Documents/巴士汉化-哈基米版
```

| 用途 | 位置 |
|---|---|
| 待修中文 | `workspace/LLC_zh-CN/` |
| 旧韩文基线／旧中文基线 | `references/baseline-KR/`、`references/baseline-zh-CN/` |
| 正式 LLC 参考包 | `references/LLC-2026090501/LimbusCompany_Data/Lang/LLC_zh-CN/` |
| 接手备份 | `backups/20260917-204256/`，其中资源位于 `workspace/LLC_zh-CN/`，另含工具、测试、旧游戏语言目录及配置嘎呜 |
| 部署前独立备份 | `backups/deployment-takeover-verified/` |
| 基线信息 | `docs/reports/takeover-baseline.json` |
| 字段级差分与原文快照 | `docs/reports/takeover-coverage.json` |
| 本次新发现的源更新 | `docs/reports/handoff-source-drift.json` |
| 发布门禁／原始 linter | `docs/reports/takeover-release-check.json`、`docs/reports/takeover-lint-after.json` |
| 实际文件变更／统一差异 | `docs/reports/takeover-file-diff.json`、`docs/reports/takeover-changes.diff` |
| 剧情／RPG 专项证据 | `docs/reports/story-validation.json`、`docs/reports/rpg-dialogue-validation.json`、`docs/reports/rpg-dialogue-speaker-fixes.json` |
| 测试证据 | `docs/reports/takeover-linter-tests.txt`、`docs/reports/takeover-integration-tests.txt`、`docs/reports/takeover-e2e-tests.json` |
| 实机记录 | `docs/reports/runtime/verification.json`、`game-verified-startup.png`、`Player-after.log`，后两项位于同一 runtime 目录嘎呜 |

当前客户端韩文原文与部署目录嘎呜

```text
/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr
/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Lang/LLC_zh-CN
```

英文对照在上述 `Localize/en`，英文也可能保留韩文或滞后，遇到语义冲突必须说明取舍理由嘎呜
原文文件通常带 `KR_` 前缀，中文版去掉此前缀但保留子目录结构，请按相对路径、条目 id/key 和嵌套字段匹配，不能依赖数组位置或假定 ID 连续嘎呜

工具入口嘎呜

- `tools/diff_extractor.py`：全源差分、缺失字段、非翻译字段变化、残留韩文、占位符计数、关键词引用和新资源多余字段检查嘎呜
- `tools/resource_fields.py`：区分引擎标识、源文注释、气泡触发说明等非正文；名字、昵称及实际台词仍需翻译嘎呜
- `tools/linter.py`：指定韩文源的静态扫描，关键词空格只自动判断 ASCII 编码引用，不强拆普通中文词或复合词嘎呜
- `tools/verify_release.py`：输出带工作区和源目录哈希的范围门禁报告，当前旧报告会因源变化被部署器拒绝嘎呜
- `tools/deploy_mod.py`：完整备份、复制到 Lang 外的暂存目录、校验哈希后激活，暂存目录不能放在 Lang 内，否则会被游戏列成可选语言嘎呜

不要直接重跑 `translate_season8_stories.py`、`build_quest_files.py`、`build_rpg_meta_files.py` 等历史生成脚本，先读实现确认它们不会以旧规则覆盖本轮人工修复，也不要用 linter 自动修复替代语义审阅嘎呜

## 9. 给接手调研模型的执行要求嘎呜

1. 先备份当前中文工作区，处理第 2 节两处源更新并重新识别完整源差分，不直接复用旧报告的 passed 状态嘎呜
2. 建立可追溯的文学与官方资料证据表，区分官方事实、原著事实、游戏文本明示、合理推测及无法确认项，记录出处链接、版本和日期嘎呜
3. 优先审阅新增主线、默尔索相关叙述和 RPG 物品／任务文本；发现实质错误时直接修复对应 JSON 文本，并记录文件、条目、旧译、新译、原因与依据嘎呜
4. 外部材料用于解释语言和互文，不能覆盖游戏当前原文，更不能以预告、英文旧版本或个人剧情理论替换已实装文本嘎呜
5. 保持 JSON 结构、id/key/model/index/level、引用关系和非翻译字段，保留占位符数量及富文本；无 speaker 的叙述不擅自加角色，不能为凑连续 ID 伪造记录嘎呜
6. 延续 LLC 文风，核对“获得／施加／增加”、强度／层数、次数、对象、时间点和不等号边界，采用半角 `~`、中文引号和六点省略号；禁止使用 GLM 翻译嘎呜
7. 修改只发生在待修中文与必要工具中，源码、原文基线、接手备份保持可追溯；不要混入尚未授权的重构或重新发布动作嘎呜
8. 完成后运行指定源目录的检查与真实资源测试，分别报告新范围问题、历史问题、人工语义结论和实机结果，不用通过率代替文学审校证据嘎呜
9. 打包及公开发布继续保持暂停；修复交接完成后再回到用户原先要求的完整版和机制版发布任务嘎呜

在项目根目录运行以下检查，源路径明确指定，部署须另选尚不存在的备份目录并在游戏关闭时进行嘎呜

```bash
SOURCE_KR='/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr'
python3 tools/diff_extractor.py --source-dir "$SOURCE_KR" --baseline-dir references/baseline-KR --target workspace/LLC_zh-CN --output docs/reports/takeover-coverage.json
python3 tools/linter.py --target workspace/LLC_zh-CN --source-dir "$SOURCE_KR" --check-korean --strict --quiet --json-report docs/reports/takeover-lint-after.json
python3 -m unittest discover -s tests -p 'test_linter.py'
python3 -m unittest tests.test_release_integrity
python3 tools/verify_release.py --workspace workspace/LLC_zh-CN --source "$SOURCE_KR" --baseline-kr references/baseline-KR --baseline-zh references/baseline-zh-CN --report docs/reports/takeover-release-check.json
python3 tests/e2e/run_tests.py
```

若修复后尚未部署，E2E 中的工作区与安装目录一致性检查可能失败，需要据实区分“等待部署”与“资源错误”；不要修改测试或旧部署资源来掩盖差异嘎呜

## 10. 暂停中的双版本打包事项嘎呜

原定完整包包含当前全量中文，机制包面向愿意等待更精细剧情汉化、但需要看懂敌人机制的玩家嘎呜
仅机制包不能只靠文件名筛选，因为技能、关键词和状态文件也含 flavor，敌人文件含身份说明，异常体事件和观察日志混有剧情；应保留战斗机制及必要名称，明确排除剧情、语音、RPG 对话／任务和风味译文嘎呜
未实证部分语言资源缺失时的原生加载行为，不能随意删除字段或承诺自动回退；从完整包切换必须防止残留旧剧情文件，同时不能宣传为“零剧透”，敌人名字和招式本身也可能透露内容嘎呜
已查阅 LLC 上游文件标注的 CC BY-NC-SA 4.0，正式打包还需保留来源署名、标明改动并核实字体许可证等材料，本阶段尚未执行发布嘎呜

## 11. 本次源更新的原文附录嘎呜

以下 JSON 为交接时实际读取的旧快照、新源及当前中文，未对其内容做翻译修复嘎呜

```json
[
  {
    "file": "PersonalityVoiceDlg/Voice_Ishmael_Contem_10816.json",
    "field": "dataList[id=smalltalk_10816_1].dlg",
    "previous_korean": "단순히 많이 팔아선 눈알을 많이 가질 수 없을 테죠. 아래층이야 시즌 오프 전까지 재고를 바쁘게 팔아내면 그만이지만…\n저희는 누구에게 어떻게 파느냐가 중요하거든요. 그런 부분에선 제가 건너편의 멍청한 르누아르들보다 뛰어나죠.",
    "current_korean": "단순히 많이 팔아선 눈알을 많이 가질 수 없을 테죠. 아래층이야 시즌 오프 전까지 재고를 빠르게 팔아내면 그만이지만…\n저희는 누구에게 어떻게 파느냐가 중요하거든요. 그런 부분에선 제가 건너편의 멍청한 르누아르들보다 뛰어나죠.",
    "current_chinese": "单凭卖得再多，也是无法捕获更多眼球的吧。楼下那群家伙固然只要赶在季末特惠前忙着清空库存就万事大吉了，但……\n我们关心的可是面向何人、以何种形式售卖。在这一点上，我可比对面那群愚蠢的雷诺阿高明得多呢。"
  },
  {
    "file": "RPGSystem/rpg-loc-ui-common-a1c10p1.json",
    "field": "dataList[key=ReturnToMainUiScene].text",
    "previous_korean": "탐색 진도를 저장하고 메인 화면으로 돌아가시겠습니까?",
    "current_korean": "유리창으로 이동하시겠습니까?\n<color=#ff0000>유리창 복귀 시 현재 탐색 진도가 저장되지 않을 수 있습니다.</color>\n\n※ 탐색 진도는 퀘스트 완료 / 층 이동 / 구역 이동 시 자동으로 저장됩니다.\n유리창으로 이동하기 전, 현재 저장 상태를 확인해주세요.",
    "current_chinese": "要保存探索进度并返回主界面吗？"
  }
]
```
