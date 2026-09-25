# 边狱公司翻译资料入口

本库服务后续汉化：复用巴士 Wiki 与零协会已有资料，保存本项目的新译名、已译上下文及确实影响翻译的疑点。已有设定直接查上游；本地研究按需查阅，不以重建百科或全库逐条考证为目标。

## 最新零协会对照

当前优先检索零协会 `2026092102` 原包与修订后的工作区；下载来源、版本边界、术语变化、逐句对照教训及未决项统一见[零协会更新调研](reports/zeroasso-update-research.md)，本地路径见[参考资源版本](../references/README.md)。旧研究中的项目暂译名不能覆盖此版已经收录的译名。

## 按问题查资料

| 当前要解决的问题 | 优先入口 | 本地补充的用途 |
| --- | --- | --- |
| 人物、组织、地点、旧剧情背景 | [巴士 Wiki](https://limbuscompany.huijiwiki.com/wiki/首页)、[世界观](https://limbuscompany.huijiwiki.com/wiki/世界观)、[但丁笔记](https://limbuscompany.huijiwiki.com/wiki/但丁笔记) | 保存具体条目链接、必要摘要；仅在影响当前译句的冲突处追查脚注与原文 |
| 既有译名和命名理由 | [零协会命名归档](https://www.zeroasso.top/docs/translate/namearchive/)、[中文基准](../references/baseline-zh-CN/) | 先用既有译名；再检索工作区，避免同一实体重复起名 |
| 角色称呼与语气 | [零协会罪人语言风格](https://www.zeroasso.top/docs/translate/sinnerstyle/)、[观察记录风格](https://www.zeroasso.top/docs/translate/sinnerrep/) | [已定位人物台词](references/02_character_personas/sinners/)、[观察实例](references/02_character_personas/observation/obs_overview_and_nicknames.md)，按角色和剧情阶段读取 |
| 技能、被动与状态 | [零协会技能类文本翻译](https://www.zeroasso.top/docs/translate/skills/)、[BattleKeywords](../references/baseline-zh-CN/BattleKeywords.json)、[Bufs](../references/baseline-zh-CN/Bufs.json) | [词条 ID 与译名索引](../references/battle_keywords_glossary.md)用于找词；完整机制读取同 ID JSON |
| 标点、标签与占位符 | [零协会符号规范](https://www.zeroasso.top/docs/translate/punctuation/)、[项目规则](../AGENTS.md) | 上游写作规范与本项目资源格式分开；验证命令见[本地化技能](../.agents/skills/limbus-company-localization/SKILL.md) |
| 新赛季尚未覆盖的内容 | [我们已有的中文译文](../workspace/LLC_zh-CN/)、当前客户端同 ID 韩文 | 补新词、称呼、语境与具体翻译难点，不重译已有成果 |

Wiki 页面标注为推测的内容仍按推测使用；引用其已经整理好的资料不要求先逐条重审整个词条。只有遇到来源冲突、版本变动、疑似错译或本句存在歧义，才扩大核对范围。网页暂时打不开不代表未收录，可检索具体页面或使用本地既有译文。

## 新剧情：先检索我们已经译好的内容

| 资料 | 查阅位置与定位方式 |
| --- | --- |
| 主线对白 | [StoryData](../workspace/LLC_zh-CN/StoryData/)，用文件名 + `id`；第十章现有 `S10*.json` 可直接检索，保留 `model`、`teller` 与相邻对白 |
| 探索对白与任务 | [RPGSystem](../workspace/LLC_zh-CN/RPGSystem/)，对白用 `key + texts.index`，任务和物品用 `key`；同时检查 `speaker` |
| 人格及 E.G.O 语音 | [PersonalityVoiceDlg](../workspace/LLC_zh-CN/PersonalityVoiceDlg/)、[EGOVoiceDig](../workspace/LLC_zh-CN/EGOVoiceDig/)，按 `id` 读取 `dlg`，`desc` 是事件标签 |
| 人物显示名 | [模型姓名表](../workspace/LLC_zh-CN/ScenarioModelCodes-AutoCreated.json)，结合当前对白的姓名遮蔽字段，不凭内部模型名提前揭示身份 |
| 机制、物品及笔记 | [第十章词条](../workspace/LLC_zh-CN/BattleKeywords-a1c10p1.json)、[物品](../workspace/LLC_zh-CN/Items-a1c10p1.json)、[探索物品](../workspace/LLC_zh-CN/RPGSystem/rpg-loc-item-common-a1c10p1.json)、[但丁笔记13](../workspace/LLC_zh-CN/StoryTheaterDanteNoteDetail_13.json)；与相关 Skills、Passives、Bufs 同查 |

在仓库根目录按实际问题替换检索词：

```bash
rg -n -F '玛普丝' workspace/LLC_zh-CN/StoryData workspace/LLC_zh-CN/RPGSystem
rg -n -F 'ChargeNoir' references/baseline-zh-CN workspace/LLC_zh-CN -g '*.json'
```

中文基准、冻结韩文与当前客户端韩文的用途和路径见[参考资源说明](../references/README.md)。工作区已有译文是本项目连续性依据；新句仍以其对应韩文为语义依据，发现具体冲突才记录和处理。

以下是可直接接续的第十章定位点，详细分析沿用[现有专题](references/03_season8_literary_research/03_canto10_lore_and_audit.md)与[剧情工作台](../STORY_NOTES.md)，不在入口另写剧情梗概：

| 翻译问题 | 已译资料位置 | 使用注意 |
| --- | --- | --- |
| 章节与赛季名称 | [StageChapterText](../workspace/LLC_zh-CN/StageChapterText.json)，`chapter_n_110` | 主线章名为用户确认的“被凝视者”；第八赛季 PUNCTUM 为“刺点”，二者分开 |
| 母亲的命令、判断与行动 | [S1061B](../workspace/LLC_zh-CN/StoryData/S1061B.json)，`2–8` | 保留说话人及命令语气，不从这些话补写未出现的行为或完整动机 |
| 让娜与家具 | [S1062B](../workspace/LLC_zh-CN/StoryData/S1062B.json)，`4–5`；[探索物品](../workspace/LLC_zh-CN/RPGSystem/rpg-loc-item-common-a1c10p1.json)，`I990407` | 旁白的“或许”与物品说明分别保留，不相互改写成统一定论 |
| 感官经验与恐惧 | [4层探索对白](../workspace/LLC_zh-CN/RPGSystem/rpg-loc-dialogue-floor-4.json)，`D40815`、`D40816` | 依各条 `speaker` 与问句／自述翻译，不预设所有角色持同一哲学立场 |
| 西西弗百货与玛普丝 | [第十章专题3.5、3.6](references/03_season8_literary_research/03_canto10_lore_and_audit.md) | 已有基准与项目译名差异集中在该处；沿用已译称呼上下文，不另造第三套名称 |

## 本地只补会改变翻译判断的信息

- 上游已覆盖：记录条目链接及必要摘要即可，不另写完整人物传记、势力百科或旧章复述。
- 上游未覆盖：先检索我们已译内容，再读同 ID 韩文及上下文；只补新增译名、称呼关系、双关解释和跨文件一致性决定。
- 出现具体分歧：在现有专题记下“问题、现用译法、来源位置、处理结论或未决原因”，不为普通资料建立逐段核验任务。
- 文学与哲学：只有具体用词、典故或互文需要时，再查[加缪材料](references/03_season8_literary_research/01_camus_archetype.md)或[哲学术语研究](references/07_philosophical_lineage/08_multilingual_philosophical_lexicon.md)；原著人物经历和哲学解释不能自动变成游戏事实。
- 用户想法：[USER_THOUGHTS](../USER_THOUGHTS.md)保留原话，[STORY_NOTES](../STORY_NOTES.md)保留来源归属与假说程度，不把整理者扩写写成用户结论。

现有[标准与句法](references/01_philosophy_and_standards/)、[名称资料](references/04_corpus_and_terminology/report_name_archive.md)、[旧章节笔记](references/05_canto_plot_compendium/)、[世界观笔记](references/06_worldbuilding_and_theories/)及[文学哲学研究](references/07_philosophical_lineage/)保留为按需参考，不作为每次翻译的必读清单。未定位的示例不能当实机台词，过期前瞻不能覆盖已译新剧情。

资料状态及尚存的具体风险见[知识库审查状态](reports/knowledge-base-audit.md)；不再用段落、表头或标题的核验比例衡量翻译准备程度。
