# 翻译参考库：当前状态与证据

当前维护范围：复用巴士 Wiki、零协会资料和我们已有译文，只补翻译所需的新内容与具体疑点；统一查阅方式见[翻译资料入口](../TRANSLATION_GUIDE.md)。本报告保存已有核查证据，不要求译者先读完报告或重审全部资料。

## 当前状态

| 项目 | 状态 |
| --- | --- |
| 上游复用 | 入口已按设定、命名、口吻、机制与格式连接上游资料；遇到具体冲突再追查原文 |
| 已译新剧情 | 主线、探索、人格／E.G.O语音、模型名、机制、物品与笔记已接入入口；按文件及 ID 检索 |
| 项目名称 | `StageChapterText.json / chapter_n_110` 为“被凝视者”；第八赛季 PUNCTUM 为“刺点” |
| 本地研究 | 已有有用修正与可定位引文保留；旧章、世界观、文学哲学笔记按需读取，不作为上游资料的替代百科 |
| 审查进度 | 停用7205个Markdown单元的核验分母及1.96%结案率；它们不能反映翻译参考库的可用程度 |
| 后续工作 | 按当前翻译涉及的词条、称呼、语义冲突报告已处理／未决项，不再宣称或追求“百科事实全库通过” |

此前“63篇均有重点复核”只说明每篇处理过部分问题；“277处原有引文已定位”和“314条修正后引文与资源对应”仅指来源核对，不代表整篇语义、人物推测或全部译文正确。自动化测试也不能替代这类判断。

旧全库台账与本次改前文档已移入本地忽略目录 `docs/reports/raw_dumps/kb-reference-scope-20260920/`，仅作追溯备份，不继续分派为待办，也不作为技能默认检索材料。

## 需要时再处理的具体疑点

| 翻译遇到的情况 | 已有定位与处理边界 |
| --- | --- |
| 希斯克利夫思考能力的描述 | [观察记录](../references/02_character_personas/observation/obs_heathcliff.md)保存简介中韩否定句差异；不能根据现有中文扩写智力结论 |
| 罗佳动机与索尼亚判断 | [观察记录](../references/02_character_personas/observation/obs_rodion.md)保存 `2D306B/75` 的韩文否定结构疑点，角色判断与客观叙述分开 |
| 新章地名与姓名栏 | [第十章专题3.2、3.5](../references/03_season8_literary_research/03_canto10_lore_and_audit.md)记录西西弗百货的基准／工作区差异及克罗默姐姐显示名问题，不按出现次数或模型键直接改名 |
| 机制词条摘要 | [词条索引](../../references/battle_keywords_glossary.md)含截断说明，只用于找名称；触发条件、上限和数值回到对应 JSON |

## 本次调整范围

调整9份Markdown：翻译入口、本文、参考资源说明、词条索引、观察资料入口、技能主文档、技能角色入口、根README及TODO；归档1份旧台账。撤下重复角色例句、百科式导航摘要与失实完成声明，修正词典中的“莫尔索／白派”、震颤引爆名称及流血／烧伤的错误别名合并。

游戏资源JSON、用户原话与剧情工作台保持本轮改前内容，已有翻译继续作为后续工作依据。修改保持未提交；没有打包或部署。

## 验证

2026-09-20执行：`python3 tests/e2e/run_tests.py` 为116/116通过；技能 `quick_validate.py` 通过；9份修改文档中的100处本地链接全部可达（README的3个既有GitHub页面链接另计）。2162份游戏JSON及 `USER_THOUGHTS.md`、`STORY_NOTES.md` 的SHA-256均与改前相同。

这些结果验证文档入口与资源未被意外改动，不表示全部研究内容或现有译文已通过语义审查。本次未修改游戏JSON，未执行批量自动修复。

## 已有核查证据（按需查阅）

以下保留此前的具体来源与证据，作为纠正旧资料的依据，不扩大为后续全库逐条审查任务。

## 已有观察专题证据

| 核验点 | 已定位证据 | 处置与剩余问题 |
| --- | --- | --- |
| 李箱收尾例外 | `AbnormalityGuides/8002/storyList/level=0,1,2`中韩，上游[观察规范](https://www.zeroasso.top/docs/translate/sinnerrep/) | 等级0/1有报告结束，等级2被中断并有批注；补入可定位实例，不强制统一收尾 |
| 浮士德第一人称及规则 | `AbnormalityGuides/8001`中韩，等级0含`제가 알고 있는 언어` | 日志本身已有第一人称；公司守则在具体条目确实出现，不能以禁止增写为由删掉原有信息 |
| 默尔索／奥提斯报告 | `8015`三个等级与`8038`两个等级，中韩原文 | 保留感觉、推测、箭头批注与不同时间；凤老爹记录明确判断为扭曲 |
| 桑丘与子嗣 | `7D101B/32,65`、`7D109B/26–28`、`7D111I2/121–122,199`中韩；[灰机桑丘](https://limbuscompany.huijiwiki.com/wiki/桑丘) | 桑丘拒绝创造家人；鞋履与忘却河分开，旧“我的孩子们”拟写句撤出实机范例 |
| 希斯简介否定句 | `IntroduceCharacter/히스클리프.description`中韩；[零协会风格](https://www.zeroasso.top/docs/translate/sinnerstyle/) | 韩文否定思维体系有严重问题，现有中文却否定有深入思考；正文单列差异，游戏JSON未改 |
| 希斯仍保有记忆 | `E901B/18–19,23,27`与KR同ID；[《呼啸山庄》第1、4章](https://www.gutenberg.org/files/768/768-h/768-h.htm) | 保留互相核对凯瑟琳记忆；小说外貌标签不证明游戏族裔或人生结局 |
| 船员是否全灭 | `5D104B/3,11–12,19`、`5D106B/21–23`中韩；[《白鲸》Epilogue](https://www.gutenberg.org/files/2701/2701-h/2701-h.htm) | 游戏鲸腹中仍有亚哈与船员，不能套用小说唯一幸存者结局；PTSD、固定身体反应仍缺证 |
| 罗佳动机归属 | `2D306B/65–78`中韩；`IntroduceCharacter/로쟈` | 区分罗佳自述与索尼亚判断；75条否定结构另记未决，不把全街区零幸存当统计事实 |
| 格里高尔异化及口吻 | `IntroduceCharacter/그레고르`、`S823B/14–16`、`E908B/54–55`中韩及既有`S945B/74–80` | 原简介允许全身虫化；能严肃谈论战争；疾病比喻不等于酒精依赖诊断 |
| 辛克莱与文学 | `3D309A/5–6`、`S951B/114`、`S1002B/87,89,97`中韩；[《德米安》德文第1、2章](https://www.gutenberg.org/files/41907/41907-h/41907-h.htm) | 补齐德米安自述、编号、姐姐自述与原作章节，不把文学事件移植为游戏履历 |
| 良秀新剧情材料 | `StoryTheaterDanteNoteDetail_11`的156、163与KR同ID | 保留旧推测与浮士德后续区分，不简单等同概念焚化炉 |

旧观察范例中长度不少于12字的19段引号内容，已在当前中文基准的StoryData、人格语音、E.G.O语音中进行原样检索，均未匹配；这是指定目录和当前版本的检索结果，不能证明这些文字在全部版本或所有媒介中从未出现嘎呜

## 指定信源与已译文本的使用方式

- 世界观、设定、既有名称以[灰机Wiki](https://limbuscompany.huijiwiki.com/wiki/首页)与[零协会文档](https://www.zeroasso.top/docs/main/)为基准，保留网页标注的推测程度；Wiki首页访问曾返回403，具体条目仍可通过搜索读取；这里保存已查阅页面，不据首页访问结果认定整站无法使用嘎呜
- 新剧情同时使用我们已译的StoryData、RPGSystem、技能、被动、物品和同ID韩文；未被Wiki收录的近期内容不因此被删除或判假，翻译版本与原文证据分别记录嘎呜
- 文学、哲学和社区研究保留为解释材料；未定位的前瞻、心理诊断、作者意图及示例不得作为已确认剧情或强制译法嘎呜
- 零协会[猩红视线说明](https://www.zeroasso.top/archive/name/red-gaze/)使用“凝视之下”，本项目“被凝视者”来自用户明确决定；二者没有被伪装成相同来源的译名嘎呜

## 人物引文核验口径

先前核验固定改前15篇人物档案第4节中277处台词为来源核验分母：231处LCB语音、23处基础E.G.O语音、23处剧情摘句；标题、履历、心理解释、关系矩阵和未定位写作示例不混入分母嘎呜

下表“原有处数”不随拆句或补录改变，“当前记录”则计入新增内容；每个当前记录已校验中文基准的 `dlg`／`content`、工作区同字段和韩文同 ID，剧情另核对 `model`，不能将这一来源定位工作称作全库语义审核嘎呜

| 人物档案 | 原有处数 / 已定位 | 当前记录 | 已记录处置 |
| --- | ---: | ---: | --- |
| [01_yi_sang.md](../references/02_character_personas/sinners/01_yi_sang.md) | 24 / 24 | 24 | 24处补ID，Yisang文件名大小写修正 |
| [02_faust.md](../references/02_character_personas/sinners/02_faust.md) | 22 / 22 | 22 | 22处补ID |
| [03_don_quixote.md](../references/02_character_personas/sinners/03_don_quixote.md) | 23 / 23 | 23 | 23处补ID，Donquixote文件名大小写修正 |
| [04_ryoshu.md](../references/02_character_personas/sinners/04_ryoshu.md) | 23 / 23 | 23 | 23处补ID；恢复2处换行，纠正缩写展开规则 |
| [05_meursault.md](../references/02_character_personas/sinners/05_meursault.md) | 22 / 22 | 22 | 22处补ID |
| [06_hong_lu.md](../references/02_character_personas/sinners/06_hong_lu.md) | 2 / 2 | 23 | Honglu文件名修正；空栏目补21条已有语音 |
| [07_heathcliff.md](../references/02_character_personas/sinners/07_heathcliff.md) | 27 / 27 | 27 | 保留3条overdrive失控语音，与erosion分开 |
| [08_ishmael.md](../references/02_character_personas/sinners/08_ishmael.md) | 23 / 23 | 23 | 取消全录标签，原LCB节选21/23条 |
| [09_rodion.md](../references/02_character_personas/sinners/09_rodion.md) | 22 / 22 | 22 | 取消全录标签，原LCB节选21/23条 |
| [10_sinclair.md](../references/02_character_personas/sinners/10_sinclair.md) | 22 / 22 | 22 | 取消全录标签，原LCB节选21/23条 |
| [11_outis.md](../references/02_character_personas/sinners/11_outis.md) | 22 / 22 | 22 | 22处补ID |
| [12_gregor.md](../references/02_character_personas/sinners/12_gregor.md) | 22 / 22 | 22 | 取消全录标签，原LCB节选21/23条 |
| [13_dante.md](../references/02_character_personas/sinners/13_dante.md) | 10 / 10 | 11 | 2处改写恢复基准；增加自救下半句；纠正序章误标 |
| [14_vergilius.md](../references/02_character_personas/sinners/14_vergilius.md) | 6 / 6 | 15 | 3处拼接拆分；补“但是”“我不知道”及插话提示 |
| [15_charon.md](../references/02_character_personas/sinners/15_charon.md) | 7 / 7 | 13 | 5处拼接拆分，保留“我的乘客们”第一人称 |

当前12份基础E.G.O语音的20101至21201对应条目未包含 `battle_erosion`；`Voice_EGO_Heathcliff_7.json` 的 `battle_overdrive_20701_1-1`、`1-2`、`1-3` 确实存在，韩文事件标作 `E.G.O 폭주 발동`、中文为“E.G.O失控”，与 `E.G.O 침식`／“侵蚀”区分；语音文本不证明所有普通战斗中的可用性、侵蚀或解放触发条件，不能反推“初始E.G.O绝不会有任何异常形态或特殊语音”嘎呜

LCB的72项技能／被动名称及基础E.G.O的24项技能／被动名称已按 ID 定位到中韩文件；这里确认名称引用，不代表96项技能机制描述全部重审，危险等级及演出触发也不计入这一统计嘎呜

## 人物引文与术语核验的证据

| 核对点 | 可直接复核的证据 | 结果 |
| --- | --- | --- |
| 但丁质问阿方索 | [4D305A](../../references/baseline-zh-CN/StoryData/4D305A.json) `13–14`；[灰机4-54-23](https://limbuscompany.huijiwiki.com/wiki/4-54-23)明确标注零协会译文 | 恢复“去你妈的”“委托し协会将施伦妮灭口”；韩文 `엿이나 먹어`、`시협회…슈렌느` 支持原场景，但不支持冒称旧稿改写为零协会原句 |
| 但丁旁白及转述 | 同文件 `61–69` 中韩：思绪无尖括号，`65`对白有尖括号，`66`浮士德转达、`67–68`向导否认听到 | 撤出全句加括号、脑电波转码及大巴神经直连说；不把特定情境说成完整能力名单 |
| 陪伴与自救 | [S833I6](../../workspace/LLC_zh-CN/StoryData/S833I6.json) `57–58`，韩文后句为 `결국 스스로를 구할 수 있는 건… 너뿐일 거야.` | 加回“但最终能拯救你的……只有你自己”，保留我们已有译文 |
| 向导的判断限度 | [S945B](../../workspace/LLC_zh-CN/StoryData/S945B.json) `74–80`，`74`为 `…모르겠군.`；`76–77`为罗佳插话 | 保留“不知道”与问答间隔，不把多条摘句写成无缝独白 |
| 语音同形缩写 | [良秀E.G.O语音](../../references/baseline-zh-CN/EGOVoiceDig/Voice_EGO_Ryoshu_4.json) `battle_awaken_20401_1/2` 中韩 | 同为 `모.불.아.위.`，展开分别含 `아름다움`、`아라야`；对应“美”“阿”的不同译法和换行均保留 |
| 良秀规则与上游冲突 | [零协会语言风格](https://www.zeroasso.top/docs/translate/sinnerstyle/)与 `get_10401_1`、`battle_defeat_10401_1` | “除·缩·没·想”不是质问；“夜良秀苦”未加中点；不强制四字、唯一展开或辛克莱每次代译 |
| 猩红视线被动 | [Passives](../../references/baseline-zh-CN/Passives.json) `999901`及同 ID 韩文 | 下回合3层束缚与按攻击意图、受伤状态计算的虚弱是不同条件，修正合并叙述 |
| 高温装置 | `Passives/999902`，`BattleKeywords-a1c6p3`、`Bufs-a1c6p3` 的 `AaCfPcBi`，韩文名 `고열기전` | 保留基准正式名称“高温装置”，替换旧概述“特殊灼热” |
| 血泪及档案完整性 | `Passives/999903–999907`、`Skills/999901–999909` | 补3%不致死固定伤害、攻击后每击杀恢复15%；当前还有望及问号技能，撤销“第六章全录”定位；原6项被动均已核对，新增999907单列 |
| 卡戎称呼、第一人称及玩偶 | [S708B](../../references/baseline-zh-CN/StoryData/S708B.json) `74、89–90`；[E001X](../../references/baseline-zh-CN/StoryData/E001X.json) `303–304`；[灰机活动剧情](https://limbuscompany.huijiwiki.com/wiki/仲春夜之梦2战前) | 不拼接远隔的对白；`내 승객들이`支持“我的乘客们”；`꼬미`与“最珍惜的玩偶”可定位，撤出“15号核心”编号 |
| 畏与敬畏不能凭中文近义合并 | [P41–P42及版本边界](../references/07_philosophical_lineage/08_multilingual_philosophical_lexicon.md)；《存在与时间》英译p.230搜索索引、[KCI论文摘要](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001850855)、中韩英Egos `20407` | 不将 `경외` 无依据并入Angst；游戏“轻蔑，敬畏”不被研究表覆盖；尚未完成韩译本逐页审定 |

## 已核验的游戏资料证据与处置

| 核对点 | 可复核证据 | 处置 |
| --- | --- | --- |
| 四位巨人与神父 | RPG floor-4 `D40220/6、24`（其余三位）；floor-2 `D2012/2–3`（神父、黑派巨人），中韩一致 | 保留可支持的事实；让娜卡其归属、卡门身份及完整名单不靠数量脑补 |
| 家具化的因果 | `S1062B/4–5` 否定直观形变并保留推测；物品 `I990407` 另明确家具化与阳光低语 | 并列保留两条，不截断旁白证明让娜一句话改变肉体 |
| 洗礼减少方式 | `Passives_Abnormality-a1c10p1/148402.desc` 中韩都有E.G.O、守备技能 | 去除“唯有E.G.O”和一次必定消除；不把技能释放等同个人绽放 |
| 单足的来源 | floor-4 `D40213/2–7、31–35` 区分修行信念与四足求斩腿；技能 `148303.flavor` 提到品牌经理 | 保留用户手撑地观察，撤出全体自我截肢、高层绝对豁免、最高统帅等无证据扩写 |
| 母亲与恐惧 | `S1061B/2–8` 是求死话语；`D40816/0–5` 回答默尔索自己的恐惧起点 | 不确诊精神机制，不把用户猜想写成弑亲完整动机 |
| 落日与经验 | `D40815/7–19` 是让娜的疑问；笔记 `DanteNoteDetail_174` 中韩都写不提供梦或经验 | 不宣称技术永远不能共感；用户回忆中的相反说法保持原话并待定位 |
| 社区转贴归属 | USER记录7含伊呂亜須署名及主页；记录13、15含社区与用户猜测 | 与用户原创、游戏事实分开，未冒称定位到原帖 |
| 公司技术 | [J](https://limbuscompany.huijiwiki.com/wiki/世界观/J公司)、[T](https://limbuscompany.huijiwiki.com/wiki/世界观/T公司)、[U](https://limbuscompany.huijiwiki.com/wiki/世界观/U公司)、[14区](https://limbuscompany.huijiwiki.com/wiki/世界观/14区)、[24区](https://limbuscompany.huijiwiki.com/wiki/世界观/24区)，H另见笔记143 | 17行公司表区分业务、产品、奇点与未知，修正旧新公司混同 |
| E.G.O译名 | 基准Egos与KR_Egos同ID：20103、21206、20304、21003、21203、21102；[零协会肉食提灯](https://www.zeroasso.top/archive/ego/meat-lantern/) | 祈愿石、往昔、一生炖菜、提灯、黑檀枝干，纠正对应角色及异想体／E.G.O混淆 |
| 组织与称号 | 基准Personalities `10915/10109/10515`；[하나](https://limbuscompany.huijiwiki.com/wiki/世界观/하나协会)、[Tres](https://limbuscompany.huijiwiki.com/wiki/世界观/Tres协会)、[蜜黄标枪](https://www.zeroasso.top/archive/name/amber-harpoon/) | 环指讲解员与学徒分开；协会职责与名词来源修正 |
| 人物关键事实 | [9.5-01战前](https://limbuscompany.huijiwiki.com/wiki/9.5-01战前)、[桑丘](https://limbuscompany.huijiwiki.com/wiki/桑丘)、[德米安](https://limbuscompany.huijiwiki.com/wiki/德米安)、[鸿璐](https://limbuscompany.huijiwiki.com/wiki/鸿璐)、[卡戎](https://limbuscompany.huijiwiki.com/wiki/卡戎) | 希斯仍记得凯茜；桑丘与老堂不同；克罗默最终由德米安击杀；鸿璐左眼；拉佩丝／卡戎关系恢复为带来源概述 |
| 罪种认识更新 | [罪种整合](https://limbuscompany.huijiwiki.com/wiki/罪种整合)、`E706B/6` 中韩霍恩海姆明确陈述；笔记99早期推测、129后续记录 | 纠正仅凭早期记录判为“截至当前仍未确认”的不完整审查 |
| 阿赖耶识与焚化炉 | 笔记156与163，后者浮士德区分原理性质 | 保留前后解释差别，不简单等同焚化炉原型 |
| 旧新译文状态 | 米莫萨敌人1494／NPC N101004／任务Q1023；4层无单脚；克罗默姐姐模型名中韩一致 | 撤销已过期的重复修复建议，保留实机显示待核问题 |
| 社区舆情数字 | 旧稿没有40+译者、数百万字、全网一致评分的样本或帖文来源 | 撤出事实依据，保留文学语感、术语与社区反馈的研究主题 |

以上对韩文的核对针对所引具体条目，不代表第十章全部台词已经重新逐句审校；对用户记录的100%是忠实性审查覆盖率，不是假说验证率嘎呜

## 文学与哲学重点核验的实际来源

| 核对点 | 实际证据 | 修正与边界 |
| --- | --- | --- |
| 零协会所谓“四大支柱”和40多位译者 | [语言风格](https://www.zeroasso.top/docs/translate/sinnerstyle/)、[观察记录规范](https://www.zeroasso.top/docs/translate/sinnerrep/)只支持具体规范；原稿无名册或制度声明 | 撤出无来源的组织历史、人数与表决机制；翻译理论保留为项目分析工具 |
| 默尔索固定结尾与批注 | `AbnormalityGuides/8015/storyList`，等级0/1、2的中韩收尾不同，且有箭头批注 | 纠正唯一收尾和所有行必须短横杠；撤出未定位的“反震力”实机例句 |
| 良秀缩写 | 零协会语言风格的良秀条 | “除·缩·没·想”展开为“除了缩写外没有想法”，不是质问句；不保留未定位的经典映射 |
| 辛克莱与克罗默 | [Wiki德米安](https://limbuscompany.huijiwiki.com/wiki/德米安)、`3D309A`后续对话 | 最终击杀者是德米安；原著经历、镜像人格与本体不混同 |
| 小说十字架、庭审、结尾 | [《局外人》法文](https://www.fadedpage.com/books/20150715/html.php)，第二部第一、三至五章 | 象牙改银质；撤出“90%”伪统计；等待处决不写成执行现场 |
| 推石地点及哲学自杀 | [《西西弗神话》法文](https://www.fadedpage.com/books/20160912/html.php)，末章、“LE SUICIDE PHILOSOPHIQUE”章 | 未指定阿克罗科林斯山为受罚山顶；补回胡塞尔等讨论对象，不将黑格尔写成该章代表 |
| 亚伯拉罕的信仰 | [《恐惧与战栗》Lowrie英译](https://dhspriory.org/kenny/PhilTexts/Kierkegaard/Fear%20and%20Trembling.htm)，检索“God would not require Isaac” | 区分愿意献祭与相信不会最终失去以撒；不是已核丹麦文逐字引文 |
| “上帝不存在则一切允许” | [萨特讲演英译](https://www.marxists.org/reference/archive/sartre/works/exist/sartre.htm)，Dostoevsky段 | 能证实萨特如此概括，不能据此冒称俄文小说有同样的一句 |
| 叔本华钟摆、自杀与意志否定 | [第一卷英译](https://www.gutenberg.org/files/38427/38427-h/38427-h.html)§57、§69 | 保留钟摆概述；撤出未核版德文拼句，补上自杀不等于意志否定的边界 |
| 尼采“这个世界”引文 | [遗稿38[12]德文转录](https://ksa.apoliteia.ru/11_38)，KSA11，1885年6—7月 | `Diese Welt`不是`Dieses Leben`；遗稿与生前出版著作分开 |
| 沉沦及极限情境 | 《存在与时间》§38英译p.220索引正文；[雅斯贝尔斯基金会原文](https://jaspers-stiftung.ch/de/karl-jaspers/grenzsituationen)引1950年版pp.20–21 | 沉沦不作道德贬斥；极限情境列举含偶然，非固定四项；整本海德格尔PDF未成功直读 |
| 《禁闭》名句 | [萨特说明转录](https://lecarrerond.fr/huisclos)、[演出教学资料p.4](https://theatre-martyrs.be/wp-content/uploads/2017/01/TMADOSPED_HUISCLOS.pdf) | 修正正文残留的“终句”；否认一切关系必然是地狱的泛化 |
| 齐奥朗书目与格言 | [Gallimard目录](https://www.gallimard.fr/system/files/inline-files/Catalogue_Quarto_0.pdf)、[企鹅试读](https://cdn.penguin.co.uk/dam-assets/books/9780241467275/9780241467275-sample.pdf)版权页及正文pp.1–2、12 | 撤出无依据的中文书名与两条未定位法文格言；保留失眠、诞生及写作研究，不将断片观点写成定律 |
| 多语术语表及谱系图 | 以上各原作与现有正文交叉 | 撤销权威／强制词典定位；区分Entwurf与Verstehen、décomposition与déconstruction；主题分组不冒充已证实的师承链 |

新剧情仍使用我们已译的 `S1061B`、`S1062B`、第4层 `D40815`、`D40816` 和笔记156、163；相关文档补有入口，不以文学原作代替游戏剧情，也没有新增猜测性译文嘎呜

## 已识别问题的当前处置

| 编号 | 核验项 | 当前结果及证据 |
| --- | --- | --- |
| 01 | 错误实机引文 | 语料报告改为可定位条目：`S454B/24` 是东朗；浮士德胜利 ID 是 `battle_clear_10201_1`；`S648B` 没有 ID 41 嘎呜 |
| 02 | 统计项目与方法 | 按保存数据区分辛克莱“我”653、奥提斯问号258；撤销旧统计作为官方文风定论的资格，脚本缺陷明确列为待修嘎呜 |
| 03 | 浮士德绝对第三人称 | 人物、观察记录、指南和技能同步改为按原文人称；证据为 `smalltalk_10201_3` 的 `제가` 与中文“我”，以及上游风格规范嘎呜 |
| 04 | 赛季与章节名 | 主线“被凝视者”与赛季“刺点”分别记录，主线标题 JSON 已同步嘎呜 |
| 05 | 百货机构名 | 保留 `시지프 백화점` 和基准“西西弗百货”，不再用自主译文多数票推翻 `DanteNoteDetail_174`；未批量修改其他剧情译文嘎呜 |
| 06 | 不存在的剧情文件引用 | 第1–3章错误“实机引文”段落撤除，改用存在且已核验的 `1D306A`、`2D306B`、`3D309A` 条目定位嘎呜 |
| 07 | 关卡标题 | 第九章标题按中韩同 ID 对齐；全部387个被检查标题现与中文基准一致，10940 为小指 `소지` 嘎呜 |
| 08 | 基础名词与人物 | 环指韩文 `약지`、Ezra以斯拉、鸿璐、Öufi等修正，现实汉化团队与游戏协会分开，排序与罪人编号不再混称嘎呜 |
| 09 | 后巷之夜 | 开始时间改为3:13；保留官网区间与但丁笔记80分钟表述的差别，不擅自拼成一致结论嘎呜 |
| 10 | 罪种起源 | 早期笔记99保留推测语气，同时补入E706B/6及笔记129的较晚说明，不能只凭早期状态判定当前仍未确认嘎呜 |
| 11 | 缺乏依据的身世和组织定性 | 卡戎脑罐、奥提斯本体旧G军官及未定位协会职能等不再列为已确定事实；卡戎前传概述有Wiki证据，Eight可见Wiki导航但职能未核；小指按 `DanteNoteDetail_150`，R公司不再标为“第四折翼”嘎呜 |
| 12 | 微表情与剧情新增动作 | 毫秒/0.1秒精度和固定动作标待考证，未定位观察日志示例撤除；第十章不再把所引文本未出现的扣扳机写成实机动作嘎呜 |
| 13 | 官方规则与本地约定 | 关键词语法、标点、角色观察模板分清来源；按 `SkillTag.json` 区分使用时与攻击前，状态动词不再按敌我判断嘎呜 |
| 14 | 词典 | 4处专名按基准修正，3个未定位别名撤出有效映射；S8自主译名明确区别于零协会定稿嘎呜 |
| 15 | 哲学出处 | 《禁闭》名句不再标作终句，Entwurf待版本核验；九篇均已重点复核，仍未完成所有引文及多语版本校勘嘎呜 |
| 16 | 过期修复指令 | 让娜、米莫萨、单足所引资源当前已统一；克罗默姐姐模型name与韩文同名，不再将这些列为自动修复项嘎呜 |

浮士德原文使用第三人称时不应改成“我”，这条条件性原则保留；已纠正的是不看原文就强制全用第三人称的要求嘎呜

## 可复核的数据与来源

- 关卡标题：`references/baseline-zh-CN/StageNode*.json` 与知识库带“关卡节点”的387项按 ID 核对，**387/387 一致**；这不包含随后剧情解读的正确率嘎呜
- 机制词典：1936行映射、拆分别名后1938项；其中1807项名称与中文基准匹配，131项仅能在工作区对应字典找到，全部1938项与工作区名称一致、无未定位键、无名称差异，描述正文未据此宣称全部正确嘎呜
- 来源版本：当前中文基准与本地 `LLC-2026090501` 快照比较，1914文件字节相同、124个JSON内容不同、25个文件快照未收录；不得将整个基准目录标成该发布包的原样副本嘎呜
- 当前游戏原文根目录：`/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/`；韩文在 `kr/KR_*.json`，英文在 `en/EN_*.json` 嘎呜
- 公开依据：[零协会语言风格](https://www.zeroasso.top/docs/translate/sinnerstyle/)、[观察记录规范](https://www.zeroasso.top/docs/translate/sinnerrep/)、[技能翻译规范](https://www.zeroasso.top/docs/translate/skills/)、[符号规范](https://www.zeroasso.top/docs/translate/punctuation/)、[游戏官网](https://limbuscompany.com/)、[《禁闭》演出教学资料第4页](https://theatre-martyrs.be/wp-content/uploads/2017/01/TMADOSPED_HUISCLOS.pdf) 嘎呜

