# Part 2 汉化更新范围确认

核对时间：2026-09-24T15:01:00+08:00；本次仅确认资源与翻译范围，未修改工作区译文、未部署、未提交嘎呜

## 结论

**本轮韩文资源共 2,277 个 JSON；相对本机 2026-09-17 的韩文资源，新增 100 个、解析内容变化 42 个、不变 2,135 个、删除 0 个嘎呜**

100 个新增对应文件在工作区及当前游戏汉化目录均不存在；其中 4 个是无文本空壳，实际需要补建的有内容文件为 96 个，另有 42 个旧文件需要逐字段复核与合并，因此以 **138 个有内容文件的处理范围** 为当前计划基数，而不是 142 个全部重译嘎呜

“对应文件不存在”不等于所有词句都从零翻译，NPC 名称、关键词和重复台词仍应复用已验证译法；原文只改拼写、空格或已由现有中文覆盖的字段，不应制造无意义差异嘎呜

| 文件组 | 新增 | 内容变化 | 合计 |
| --- | ---: | ---: | ---: |
| 根目录战斗、人物与系统文本 | 12 | 21 | 33 |
| RPGSystem | 72（含4个空壳） | 16 | 88 |
| StoryData | 15 | 3 | 18 |
| 人格语音／E.G.O语音 | 1 | 2 | 3 |
| 总计 | 100 | 42 | 142 |

## 证据与边界

- Steam 本地 buildid 为 `25472760`，下载完成时间为 2026-09-24 11:11:16（北京时间），StateFlags=4，已下载字节数与目标一致嘎呜
- 游戏 `resources.assets` 中的 `TextAssetPatchConfig` 指向 `l20260924_4eb8-Rb7MrVjKfF17k-j`，据此获取同版官方清单与韩文 ZIP，不以旧导出目录冒充新版资源嘎呜
- 官方 ZIP CRC 检查通过，2,277 个韩文文件全部匹配官方清单的大小与文本哈希；哈希按去 BOM、CRLF 转 LF 的文本计算，保存的源文件原始字节不改写嘎呜
- `RemoteLocalizeFileList.json` 与 `rpg-loc-file-list-a1c10p2.json` 也已获取并匹配清单哈希与大小，它们是资源索引，不计入 2,277 个韩文翻译文件嘎呜
- 本机旧 `Assets/Resources_moved/Localize/kr` 仍有 2,177 个文件，时间为 2026-09-17；这是更新前对照，不能再作为 Part 2 翻译和占位符质检的当前原文嘎呜
- 这份差异是“9月24日原包相对9月17日本机原文”的累计差异，包含同期人格、E.G.O与旧内容修订，不声称每项都由 Part 2 当天首次引入嘎呜
- 核对时零协会 GitHub 最新发布仍为 `2026092102`，当前游戏 `Info/version.json` 同样为 `2026092102`；新版主线范围不能认为已经被现装包覆盖嘎呜

## 按功能划定的更新范围

### 一、Part 2 战斗机制

新增 12 个文件包括敌人／支援单位、状态关键词、Buf、技能、被动、恐慌、异想体图鉴、战斗提示与气泡台词，精确文件名见下方完整清单嘎呜

其中 BattleKeywords 与 Bufs 各有 58 条源记录，技能文件为 59 条异想体技能和 9 条支援技能，被动为 43 条异想体被动和 10 条支援被动；这些是源记录数量，不是去重后的翻译工时嘎呜

`BattleKeywords.json`、`Bufs.json`、`Passives.json`、`Passive_Ego.json` 以及旧 `Skills_Abnormality-a1c10p1.json` 等共享资源也有变化，不能只按 `a1c10p2` 文件名搜索嘎呜

### 二、RPG 探索

新增 72 个：对话／选项16、NPC20、群体敌人13、地点8、任务8、旁白3、玩家路线2、物品1、UI1；其中4个空壳不计翻译量嘎呜

范围覆盖 B 路线地上1至5层、地下1至3层、路线／剧场公共对白、任务链、物品与系统提示；同时新增 A 路线玩家和群体敌人文件，不能仅筛选文件名 `-b` 嘎呜

需要复核16个既有 RPG 文件，包括旧楼层对白、NPC名称、物品、地点、任务与公共UI嘎呜

### 三、剧情与同期人格／E.G.O

- 主线新增14个：`S1017B.json` 至 `S1029B.json` 共13个，加 `S9992B.json`，只按资源文件确认，不把编号直接等同于游戏关卡数量嘎呜
- 同期人格剧情新增 `P10917.json`，人格语音新增 `Voice_Rodion_Contem_10917.json`，并在既有角色、技能、被动、获取条件等文件中增加对应内容嘎呜
- 鸿璐与罗佳 E.G.O 的文本增量在 `Skills_Ego_Personality-06.json`、`Skills_Ego_Personality-09.json`、`Passive_Ego.json` 及两个 E.G.O 语音文件中嘎呜
- 旧剧情 `P10416.json`、`P10816.json`、`S1004B.json` 有修订，部分属于源文拼写／富文本变化，现有中文可能已覆盖，逐字段确认即可嘎呜

### 四、必须处理的旧内容变化

1. `rpg-loc-ui-common-a1c10p1.json` 的 `Log_NpcDefeated` 从两个占位符改为只保留 `{0}`，旧中文仍有 `{1}`，必须同步，不能原样沿用嘎呜
2. 同文件的 `ProgressPopup_Suicide` 与 `Setting_Sisyphus_GauntletSuicide` 从护手自杀改成返回泉水处的含义，现有中文必须随之复核嘎呜
3. `RPGSuicideBoxUI.json` 增加库存整理／物品收集说明，并移除两条 E.G.O 异想解析条件行嘎呜
4. 旧任务中有3个非空字段被清空，另有69个原非空字符串字段被删除，不能只做追加合并而把旧提示永久留下嘎呜
5. `PanicInfo-a1c10p1.json` 为删除型变化；旧B2层对白也有删除，合并时核对记录身份，避免索引错位或误删新分支嘎呜

字段级机器扫描得到新增10,986个非空候选文本字段、修改后仍非空59个、清空3个、删除69个；候选字段含重复说话人、称谓与内部说明，不等于11,045句正文，更不等于去重后工作量嘎呜

## 四个空壳文件

- `RPGSystem/rpg-loc-location-floor-1-b.json`：当前无文本，无需编造译文或盲目补空文件嘎呜
- `RPGSystem/rpg-loc-location-floor-2-b.json`：当前无文本，无需编造译文或盲目补空文件嘎呜
- `RPGSystem/rpg-loc-location-floor-3-b.json`：当前无文本，无需编造译文或盲目补空文件嘎呜
- `RPGSystem/rpg-loc-narration-floor-1-b.json`：当前无文本，无需编造译文或盲目补空文件嘎呜

## 执行顺序与验收边界

建议先冻结本次原文快照并在后续检查中显式指定它，再处理术语／战斗机制及高风险旧UI，随后完成RPG任务与交互、主线剧情、同期人格／E.G.O，最后做全量门禁与游戏内验证嘎呜

既有 `game_update_watcher.py`、`diff_extractor.py`、默认 linter 会使用游戏旧韩文目录；后续必须显式传 `--source-dir` 到本次 `source-kr`，并以本机旧韩文归一化文件名作为 Part 2 差分基准，不要使用更早的冻结 `baseline-KR` 误把Part 1再次纳入嘎呜

本次已执行 `python3 tools/linter.py`（只读）与 `python3 tests/e2e/run_tests.py`：E2E为116/116，默认全量Linter为1,261 FATAL、24,292 ERROR、25 WARN，未通过发布门禁嘎呜

这些测试结果仅记录现有工作区状态，E2E标题仍为 `a1c10p1`，默认linter仍读旧韩文；它们不代表新文件已汉化，不代表Part 2覆盖通过，也不代表游戏内显示已验收嘎呜

## 可复核证据

- [原包与统计校验](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/verification.txt) 嘎呜
- [142文件范围与字段数量](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/translation-scope.tsv) 嘎呜
- [逐字段旧韩文／新韩文／工作区／现装中文](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/field-delta.json) 嘎呜
- [新增与变更文件表](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/source-file-delta.tsv) 嘎呜
- [原文文件SHA256](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/source-sha256.tsv) 嘎呜
- [官方资源清单](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/LocalizePatchInfo.json) 嘎呜
- [零协会发布查询快照](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/upstream-release.json) 嘎呜
- [E2E日志](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/e2e.log) 嘎呜
- [全量Linter日志](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/linter.log) 嘎呜

新版原文快照：`/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/source-kr`；所有下载、验证环境与脚本留在忽略跟踪的本次证据目录，不替换历史基准嘎呜

## 完整文件清单

表内路径为去掉 `KR_` 前缀后的中文对应资源相对路径；“新增文本”包含说话人等重复字段，仅用于定位，不作为翻译工时估计嘎呜

| 变更 | 对应文件 | 新增文本 | 修改文本 | 清空文本 | 删除文本 |
| --- | --- | ---: | ---: | ---: | ---: |
| 新增 | `AbnormalityGuides-a1c10p2.json` | 6 | 0 | 0 | 0 |
| 新增 | `Assist-a1c10p2.json` | 4 | 0 | 0 | 0 |
| 新增 | `BattleKeywords-a1c10p2.json` | 165 | 0 | 0 | 0 |
| 新增 | `BattleResultHint-a1c10p2.json` | 21 | 0 | 0 | 0 |
| 新增 | `BattleSpeechBubbleDlg-a1c10p2.json` | 79 | 0 | 0 | 0 |
| 新增 | `Bufs-a1c10p2.json` | 165 | 0 | 0 | 0 |
| 新增 | `Enemies-a1c10p2.json` | 28 | 0 | 0 | 0 |
| 新增 | `PanicInfo-a1c10p2.json` | 20 | 0 | 0 | 0 |
| 新增 | `Passives_Abnormality-a1c10p2.json` | 123 | 0 | 0 | 0 |
| 新增 | `Passives_Assist-a1c10p2.json` | 33 | 0 | 0 | 0 |
| 新增 | `PersonalityVoiceDlg/Voice_Rodion_Contem_10917.json` | 48 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-choice-floor-1-b.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-choice-floor-3-b.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-choice-floor-4-b.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-choice-floor-b1-b.json` | 13 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-choice-floor-b2-b.json` | 7 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-common-a1c10p2.json` | 95 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-1-b.json` | 1069 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-2-b.json` | 475 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-3-b.json` | 904 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-4-b.json` | 1837 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-5-b.json` | 370 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-b1-b.json` | 1030 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-b2-b.json` | 833 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-floor-b3-b.json` | 725 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-route-b.json` | 65 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-dialogue-theater-b.json` | 1 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-item-common-a1c10p2.json` | 194 | 0 | 0 | 0 |
| 新增空壳 | `RPGSystem/rpg-loc-location-floor-1-b.json` | 0 | 0 | 0 | 0 |
| 新增空壳 | `RPGSystem/rpg-loc-location-floor-2-b.json` | 0 | 0 | 0 | 0 |
| 新增空壳 | `RPGSystem/rpg-loc-location-floor-3-b.json` | 0 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-location-floor-4-b.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-location-floor-5.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-location-floor-b1-b.json` | 2 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-location-floor-b2-b.json` | 8 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-location-floor-b3.json` | 8 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-narration-common-warden-boss-a1c10p2.json` | 1 | 0 | 0 | 0 |
| 新增空壳 | `RPGSystem/rpg-loc-narration-floor-1-b.json` | 0 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-narration-floor-3-b.json` | 7 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-common-a1c10p2.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-common-warden-boss-a1c10p2.json` | 2 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-1-b-enemy.json` | 7 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-1-b.json` | 28 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-2-b-enemy.json` | 3 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-2-b.json` | 23 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-3-b-enemy.json` | 11 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-3-b.json` | 15 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-4-b-enemy.json` | 9 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-4-b.json` | 40 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-5-b-enemy.json` | 22 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-5-b.json` | 9 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json` | 22 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b1-b.json` | 33 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b2-b-enemy.json` | 31 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b2-b.json` | 24 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b3-b-enemy.json` | 25 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-floor-b3-b.json` | 14 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-route-b-warden.json` | 2 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-npc-route-b.json` | 9 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-player-route-a.json` | 13 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-player-route-b.json` | 16 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-1-b.json` | 28 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-2-b.json` | 30 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-3-b.json` | 47 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-4-b.json` | 94 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-5-b.json` | 40 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-b1-b.json` | 31 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-b2-b.json` | 45 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-quest-floor-b3-b.json` | 89 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-1-a.json` | 5 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-1-b.json` | 5 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-2-a.json` | 6 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-3-a.json` | 4 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-3-b.json` | 3 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-4-a.json` | 2 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-4-b.json` | 3 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-5-b.json` | 3 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-b1-a.json` | 7 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-b1-b.json` | 10 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-b2-a.json` | 5 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-b2-b.json` | 7 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-swarm-mob-floor-b3-b.json` | 9 | 0 | 0 | 0 |
| 新增 | `RPGSystem/rpg-loc-ui-common-a1c10p2.json` | 20 | 0 | 0 | 0 |
| 新增 | `Skills_Abnormality-a1c10p2.json` | 368 | 0 | 0 | 0 |
| 新增 | `Skills_Assist-a1c10p2.json` | 116 | 0 | 0 | 0 |
| 新增 | `StoryData/P10917.json` | 192 | 0 | 0 | 0 |
| 新增 | `StoryData/S1017B.json` | 95 | 0 | 0 | 0 |
| 新增 | `StoryData/S1018B.json` | 106 | 0 | 0 | 0 |
| 新增 | `StoryData/S1019B.json` | 54 | 0 | 0 | 0 |
| 新增 | `StoryData/S1020B.json` | 16 | 0 | 0 | 0 |
| 新增 | `StoryData/S1021B.json` | 16 | 0 | 0 | 0 |
| 新增 | `StoryData/S1022B.json` | 56 | 0 | 0 | 0 |
| 新增 | `StoryData/S1023B.json` | 38 | 0 | 0 | 0 |
| 新增 | `StoryData/S1024B.json` | 22 | 0 | 0 | 0 |
| 新增 | `StoryData/S1025B.json` | 70 | 0 | 0 | 0 |
| 新增 | `StoryData/S1026B.json` | 56 | 0 | 0 | 0 |
| 新增 | `StoryData/S1027B.json` | 33 | 0 | 0 | 0 |
| 新增 | `StoryData/S1028B.json` | 24 | 0 | 0 | 0 |
| 新增 | `StoryData/S1029B.json` | 37 | 0 | 0 | 0 |
| 新增 | `StoryData/S9992B.json` | 40 | 0 | 0 | 0 |
| 修订 | `BattleKeywords.json` | 35 | 0 | 0 | 0 |
| 修订 | `Bufs.json` | 35 | 0 | 0 | 0 |
| 修订 | `CouponUIText.json` | 16 | 0 | 0 | 0 |
| 修订 | `EGOVoiceDig/Voice_EGO_HongLu_6.json` | 14 | 0 | 0 | 0 |
| 修订 | `EGOVoiceDig/Voice_EGO_Rodion_9.json` | 4 | 0 | 0 | 0 |
| 修订 | `GachaTitle.json` | 1 | 0 | 0 | 0 |
| 修订 | `IAPProduct-a1c10.json` | 4 | 0 | 0 | 0 |
| 修订 | `IntroductionPreset.json` | 6 | 0 | 0 | 0 |
| 修订 | `MirrorDungeonRentalName.json` | 1 | 0 | 0 | 0 |
| 修订 | `PanicInfo-a1c10p1.json` | 0 | 0 | 0 | 3 |
| 修订 | `Passive_Ego.json` | 4 | 0 | 0 | 0 |
| 修订 | `Passives.json` | 10 | 0 | 0 | 0 |
| 修订 | `Personalities.json` | 4 | 0 | 0 | 0 |
| 修订 | `Personality_Get_Condition.json` | 2 | 0 | 0 | 0 |
| 修订 | `RPGSuicideBoxUI.json` | 0 | 3 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-1.json` | 0 | 3 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-2.json` | 0 | 1 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-3.json` | 0 | 1 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-4.json` | 0 | 6 | 0 | 1 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-b1.json` | 0 | 4 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-dialogue-floor-b2.json` | 0 | 6 | 0 | 61 |
| 修订 | `RPGSystem/rpg-loc-item-common-a1c10p1.json` | 0 | 6 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-location-floor-3.json` | 0 | 1 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-npc-floor-2.json` | 0 | 1 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-npc-floor-b2.json` | 0 | 6 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-quest-floor-1.json` | 0 | 2 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-quest-floor-3.json` | 0 | 8 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-quest-floor-4.json` | 0 | 1 | 0 | 0 |
| 修订 | `RPGSystem/rpg-loc-quest-floor-b1.json` | 0 | 0 | 2 | 0 |
| 修订 | `RPGSystem/rpg-loc-quest-floor-b2.json` | 0 | 2 | 1 | 0 |
| 修订 | `RPGSystem/rpg-loc-ui-common-a1c10p1.json` | 14 | 3 | 0 | 4 |
| 修订 | `ScenarioModelCodes-AutoCreated.json` | 131 | 0 | 0 | 0 |
| 修订 | `Skills_Abnormality-a1c10p1.json` | 0 | 1 | 0 | 0 |
| 修订 | `Skills_Ego_Personality-06.json` | 37 | 0 | 0 | 0 |
| 修订 | `Skills_Ego_Personality-09.json` | 62 | 0 | 0 | 0 |
| 修订 | `Skills_personality-09.json` | 53 | 0 | 0 | 0 |
| 修订 | `StoryData/P10416.json` | 0 | 1 | 0 | 0 |
| 修订 | `StoryData/P10816.json` | 0 | 2 | 0 | 0 |
| 修订 | `StoryData/S1004B.json` | 0 | 1 | 0 | 0 |
| 修订 | `StoryTheaterMirrorWorldStoryTitle.json` | 1 | 0 | 0 | 0 |
| 修订 | `StoryTheaterUIText.json` | 1 | 0 | 0 | 0 |
| 修订 | `UnitKeyword.json` | 1 | 0 | 0 | 0 |
