# 第十章下半汉化：审查修复交接文档

## 1. 当前结论

主人，上一轮主代理终审确认的必改项已经完成工作区修复，并由原五位 Luna 子代理以 max 思考强度完成修后交叉复核，主代理已审核修复结果及验证证据嘎呜

**当前状态：本轮限定修复通过；142项增量静态门禁通过；全库默认门禁仍未通过；未提交、未打包、未部署、未进行游戏内验收**嘎呜

| 项目 | 当前结果 |
|---|---|
| 源文范围 | 2026-09-24冻结韩文，142文件，100新增＋42修改 |
| 实际修改 | 40个工作区JSON；范围外工作区文件0改动 |
| 精确字段差异 | 708个叶路径差异：663修改、43新增、2移除；含新增key、ID类型恢复及说明结构搬移，不等于708句重译 |
| 原审计的实质问题 | 16状态／32说明、2技能、支援结构、27缺字段、3组风味文本错配，以及采纳的正文／任务／名词问题已修 |
| 完整性检查追加发现 | 另修2个“字段存在但内容为空”、1个ID类型不符，与原27缺字段分开计数 |
| 机制引用归一 | 9文件527个本轮源差分字段，86种已知词条ID转为中文显示名；与部分语义修复重合，数量不能相加 |
| 当前发布状态 | **保持阻断；不能将本轮修复完成写成全项目或实机验收通过** |

本次按已确认的冻结快照修复，未重新获取后续线上补丁；历史审查文档保留当时“不通过”的判定，不把它回写成当时已合格嘎呜

## 2. 接手入口与备份

- 工作区：`/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN`
- 冻结韩文：`/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-scope-20260924/source-kr`
- 原终审：[part2-cross-review-20260924.md](/home/buxinzi/Documents/巴士汉化-哈基米版/docs/reports/part2-cross-review-20260924.md)
- 本轮证据根：`/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-review-fix`
- 修前142项完整副本：`/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-review-fix/before`
- 全工作区修前／修后指纹：证据根中的 `before-sha256.json`、`after-sha256.json`
- 仅本轮40项译文差异：[repair-only.patch](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-review-fix/repair-only.patch)
- 按稳定身份定位的完整字段变更：[field-changes.json](/home/buxinzi/Documents/巴士汉化-哈基米版/backups/part2-review-fix/field-changes.json)

差异文件相对于本轮开始时的副本，**不是相对于Git HEAD**；工作区原先已有大量修改、删除和未跟踪文件，这些没有回滚，也没有为本轮创建提交嘎呜

补丁所描述的修改已经应用在当前工作区，接手时用它审阅，不要再次直接应用；若后续需要回退，应逐项核对后续改动，不能整目录覆盖或执行强制Git重置嘎呜

## 3. 已完成的实质修复

下文短路径相对于上述工作区及同路径韩文根，精确定位以 `id`／`key`／`level`／`texts.index` 为准，不使用编辑器行号充当身份嘎呜

### 3.1 战斗机制、风味与结构

**`BattleKeywords-a1c10p2.json`、`Bufs-a1c10p2.json`**：以下16个ID的desc均按同ID韩文重译，两文件32字段同步一致，条件、对象、时机、上限与数值已交叉对读嘎呜

```text
AlriunePetal       ThreadDye             SpreadingDye
StickyDye         ChargeKhaki           FinishedFabric
LargeTailoringShears  TailoringTarget    ScissorsMark
DamagedFabric     GoldenLeatherEnhance  NoirShieldUp
NoirShieldPiece   VibrationResonance     NoirField
NoirSquareCollapse
```

- 恢复花瓣上限3及对应触发、染色线无法获得迅捷／满值无法行动、漂流惯性次数上限与衰减、完成面料上限30等真实机制，不再保留此前编造的另一套效果嘎呜
- `AlriunePetal`、`ThreadDye`、`SpreadingDye` 的两份flavor共6字段恢复对应意象，不再写成不相干的道具概述嘎呜
- `Skills_Abnormality-a1c10p2.json`：149501／149502的level1.desc恢复真实充能次数、剪刀条件与加成，149502为自身次数增加4，不是消耗4换威力嘎呜
- `Skills_Assist-a1c10p2.json`：40004104的level2／3均恢复“一枚硬币、两条coindescs”，体力／理智说明按原顺序保留；词条中文化之外没有丢失或重复原有说明嘎呜
- 韩文部分TMP标签原来交叉闭合，译文采用正确逆序闭合，未为追求字符串一致而复制坏结构；未据此宣称复现或解决了某个实机崩溃嘎呜

### 3.2 27个真正缺失字段

| 文件 | 已补项目 | 数量 |
|---|---|---:|
| RPGSystem/rpg-loc-ui-common-a1c10p1.json | 楼层未购买道具提示、两类日志、光照／亮度／移动控制等新增UI | 14 |
| BattleKeywords.json | EmpathicDistressAlly、ChargeKhakiAlly、NoirScissorAlly、NoirScissorCut、NoirScissorShield的flavor | 5 |
| Bufs.json | 上述列表除原已存在的ChargeKhakiAlly之外的flavor | 4 |
| Skills_Abnormality-a1c10p2.json | 150308、148803、148804、148806的level1.flavor | 4 |

新增UI key清单及译文保存在 `ui-added-fields.json`，`Setting_Sisyphus_RunStartDelayValue` 保留唯一的 `{0}` 并译为秒；没有把20个 `undefined: "-"` 源导出元数据当作玩家文本补进资源嘎呜

### 3.3 任务与道具

- B1任务Q-1000／Q-1004／Q-1005／Q-1008／Q-1009恢复对应阶段、人物、寻找活幼体／交给副主厨的目标及黄金茧命名转折，不再以皮革加工或诱饵交易剧情替代嘎呜
- Q-1000保留“普伊说需要穿寿衣”，不补原句省略的穿衣主体；Q-1005修正幼体群沉海场景，不把原有调查活动幼体目标误报为完全缺失嘎呜
- 5F的Q5005恢复茧裂开后观察布菲变化，Q5009恢复进帷幕后避敌逃向深处，Q5006第一项目标恢复9名黑派店员[阳光]，同源敌名与五项目标数量9／7／3／2／2已核嘎呜
- I990918名称删除无据的“话”，I991011恢复“勒内昂”群体；I990918／I990812正向状态改用“使目标获得”，触发与数值不变嘎呜

### 3.4 正文与名词

- 修复主线的N公司／N巢混用、向前靠近一步／仅剩一步距离混淆、没有人／空无一物、轮次／回目等问题，并统一相关黄金皮革和扭扭称呼嘎呜
- 修复RPG的否定反转、吞咽失败因果、人称与祈愿语气、老客户／旧主、供应／供求、必要性／紧俏、楼层／阶层、无据翻倍、指代成“这地方”、具体降回副主厨职位漏义等采纳项嘎呜
- 浮士德D2029B#index2恢复原文第一人称，机器产物恢复丝线，旧B2 D-2034-1#index0恢复但丁尖括号；未给格里高尔的源异常尾括号擅补开括号嘎呜
- 堂吉诃德、鸿璐、多萝西娅、扭扭、勒内昂等按同源实体统一，勒内昂没有与해체파“解构派”混同，红派没有与其他派系合并嘎呜
- 改衣师安妮特、黑派品牌世家、油灰的同实体名称已从敌人表延伸核到对白speaker、战斗提示和被动说明，已核定旧变体在142项中无残留嘎呜
- 成年模型뷔페어른的name改为布菲，三个幼年模型仍为普伊，S1029B揭名前的teller覆盖未改，未全局替换普伊嘎呜
- 教义“披上／披覆”已在3F旁白与D3005对应对白中保持一致嘎呜

## 4. 主代理补充修复与词条归一

### 新增结构检查发现的3项

| 定位 | 修前 | 当前 |
|---|---|---|
| GachaTitle.json，id297 | 整数297，与源类型不同 | 字符串"297"，与韩文一致；content不变 |
| RPGSystem/rpg-loc-location-floor-3.json，key130600.text | 源已非空，目标仍为空 | `(临时)公共-3楼-(52,64)-4楼 (临时)` |
| RPGSystem/rpg-loc-quest-floor-5-b.json，Q5011.steps[index=0].goalDescription1 | 源???，目标为空 | `？？？`，与中文title一致 |

这两处空值不是原27个“字段不存在”，ID类型也不是译文缺失，不能合并声称补了30个缺失字段；新增3项已由另一代理独立核准嘎呜

### 本轮增量机制引用

遵循项目既有零协会更新处理方式：先查同ID基准名称，未收录的新词用已核定本地名称，仅替换冻结源差分中的显示字段，不扫描替换整库旧正文嘎呜

- 527字段的变换已独立验证为**仅已知方括号词条引用替换**，没有借机修改其他字句、数字或触发器，依据与前后值保存在 `keyword-normalization.json` 嘎呜
- `[WhenUse]`、`[OnSucceedAttack]`、`[EndCoin]`、`[TabExplain]` 等控制标签原样保留，不能当作英文漏译继续清除嘎呜
- `ChargeForceField` 和 `VibrationExplosion` 分别沿用工作区已有显示格式“充能 力场”“震颤 引爆”，与基准的无空格译名语义相同；两份VibrationResonance说明也已与后者逐字匹配，未扩改旧未变正文嘎呜
- GoldenLeatherEnhance／SapsareeGold／GoldenManager的显示名内方括号改为全角圆括号，两名称表共6字段同步，避免生成嵌套关键词括号；此为格式适配，不是改变实体或机制嘎呜
- 本轮源差分机制字段内，已知词条英文ID剩余0；这不是“整个历史工作区无任何英文ID”的声明，也不等于游戏悬浮窗已验证嘎呜

## 5. 修后交叉复核结果

| 报告 | 独立复核内容 | 结论 |
|---|---|---|
| postcheck-A.md | E的2技能、4风味、支援两级结构；按中文词条归一核保留内容 | 限定范围通过 |
| postcheck-B.md | D的11文件17项＋主代理B2两处改名；追加核2空值和1身份类型 | 限定范围通过 |
| postcheck-C.md | B的8文件24项任务、道具、名字、教义修复 | 24项通过，无新确定错义 |
| postcheck-D.md | C的4文件44字段，包括25处名称对应补充 | 44项通过，无新确定错义 |
| postcheck-E.md | 14个UI、A的32机制＋9新增风味＋6重译风味；追加显示名空格 | 限定范围通过，静态引用不一致已解除 |

这些是对**实际修复字段**的交叉复核，不是对全部142文件每个旧句重新双人通读；527字段的机械词条替换另有主代理逐字段变换验证，不能说五位代理重新精读了这527处所有机制嘎呜

各组阶段报告里的文件哈希／字段数量可能早于主代理合并与补修，最终状态以 `after-sha256.json`、`field-changes.json` 和本交接文档为准，不能把旧阶段“只改这些字段”套用到最终文件嘎呜

## 6. 验证结果与发布阻断

| 检查 | 最终结果 | 证明边界 |
|---|---|---|
| 142项逐文件严格Linter，显式冻结韩文 | 142扫描，0 FATAL／ERROR／WARN | 增量格式检查，不证明全句翻译准确 |
| 116项E2E | 116/116 PASS | 未启动游戏，主要为既有资源与工具契约 |
| 源字段完整性 | 按规则排除元数据后，非空源显示字段缺失／空译0 | 不等于每个非空中文均正确 |
| 占位符多重集 | 142项对应可见字段0不一致 | 不能推导布局或运行效果 |
| 源身份字段和值类型 | 142项0不一致 | 不要求删除既有源外兼容条目 |
| 双文件状态说明／风味 | 16组desc与3组flavor分别一致 | 已另由人工对照原义 |
| 支援40004104 | level2／3均一硬币两说明 | 实际显示与恢复效果尚未实机验收 |
| 源快照完整性 | 142项SHA-256仍匹配冻结清单 | 未确认快照之后有无更新 |
| 修改范围 | 40项均在142清单内；范围外工作区0变化 | 保留用户已有脏工作区 |
| 全库默认Linter | **2262文件：1259 FATAL／21859 ERROR／24 WARN，退出1** | **未通过，不可宣称全项目合格** |
| 全库同环境修前／修后比较 | 计数相同，问题签名新增0、消失0 | 本轮未新增这些报告，但不自动认定它们全部为真实运行故障或全部为误报 |

全库修前对照由“未改文件的当前内容＋142项修前副本”在隔离临时目录重建，以相同默认检查器执行；问题签名比较包含规则、严重度、相对路径、字段与消息，排除用于展示上下文的snippet，详细结果保存在 `global-lint-comparison.json` 嘎呜

默认检查还会读取旧客户端韩文，其中 `Log_NpcDefeated` 仍含旧 `{1}`，对本轮已按新源只保留 `{0}` 的译文报占位符错误；**不要为了通过旧基准检查把 `{1}` 加回去**，本轮必须显式指定冻结源目录嘎呜

上述已定位旧基准问题不代表其余全库报告都能忽略；应另行甄别历史文本、动态标签片段及规则适用性，未得到授权前不把本轮扩成数万处全库自动修复，更不能豁免发布门禁嘎呜

## 7. 仍保留的边界与接手顺序

1. **先保留本轮修复**：通过差异及源译证据复核，不重跑历史生成脚本覆盖新译文；这些旧生成脚本未在本轮改写，可能重新写回旧内容嘎呜
2. **后续补齐人工语义覆盖**：原审计未完整精读的技能、被动、战斗台词与语音仍不具备全量语义验收，本轮关键词归一不能替代它嘎呜
3. **处理全库门禁**：按当前可靠源重新区分旧基准、工具适用范围及真正缺陷；修复前不要盲用全库 `--fix`，也不要为降计数删文本或占位符嘎呜
4. **保留未决译法**：S1028B id20省略主语、良秀缩写、部分性别／称呼、黄金手套实体关系及可选润色不在本轮强改范围，上一轮撤销的误报不得重新执行嘎呜
5. **实机确认UI与解析**：“光照模式”与“跑步限制时间”按韩文及邻近标签译出，实际开关功能、半径／延迟交互仍未操作验证；关键词悬浮窗、硬币说明和字体布局亦未验收嘎呜
6. **发布前再比对源版本并取得授权**：本轮没有打包／部署；不能因142项增量绿灯绕过全库问题和实机边界嘎呜

## 8. 可复现检查与证据索引

以下命令不修改译文；验证脚本会刷新证据目录中的检查结果，运行前应保留交接快照以便区分后续变化嘎呜

```bash
cd '/home/buxinzi/Documents/巴士汉化-哈基米版'
python3 backups/part2-review-fix/verify_repairs.py "$PWD"
python3 tests/e2e/run_tests.py
```

对当前142项请使用下列逐文件循环，不重复传单值 `--target` 参数，也不以扫描before目录替代当前工作区检查嘎呜

```bash
cd '/home/buxinzi/Documents/巴士汉化-哈基米版'
python3 - <<'PY'
import csv
from pathlib import Path
import subprocess

root = Path.cwd()
manifest = root / 'backups/part2-scope-20260924/source-file-delta.tsv'
with manifest.open() as handle:
    for row in csv.DictReader(handle, delimiter='\t'):
        subprocess.run([
            'python3', str(root / 'tools/linter.py'),
            '--target', str(root / 'workspace/LLC_zh-CN' / row['path']),
            '--source-dir', str(root / 'backups/part2-scope-20260924/source-kr'),
            '--check-korean', '--strict'
        ], check=True)
PY
```

| 证据文件（位于本轮证据根） | 用途 |
|---|---|
| fix-A.md 至 fix-E.md | 五组修复字段、韩文及前后对照 |
| postcheck-A.md 至 postcheck-E.md | 五组修后只读交叉复核与边界 |
| repair-validation.json | 完整性、占位符、身份、范围、双文件和支援结构断言 |
| field-changes.json、repair-only.patch | 最终稳定字段差异与仅本轮文本补丁 |
| lint-index.json、lint-reports.json | 142次独立检查及文件对应关系 |
| e2e-final.log | 最后一次116/116结果 |
| linter-global-before.json、linter-global-after.json | 同环境全库默认检查原始报告 |
| global-lint-comparison.json | 全库问题修前后归因 |
| keyword-normalization.json、keyword-remaining-check.json | 527字段纯词条变换及剩余控制标签 |
| additional-integrity-fixes.json | 2处空值与1处身份类型新增修复 |
| name-closure-final.json | 已核定旧名变体剩余0 |
| before-sha256.json、after-sha256.json | 本轮修前／最终工作区指纹 |
| deployment-state.json | Steam仍为修前状态，当前40项不同 |
| final-summary.json | 本轮机器可读验收摘要 |

`normalize_incremental_keywords.py` 是已执行变换的审计脚本，**不要为了查看结果重复运行并覆盖原始变换证据**；复核应读JSON及补丁，或在独立副本中重放嘎呜

## 9. 部署与交接确认

Steam目录 `/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Lang/LLC_zh-CN` 的142项仍与修前副本逐字节相同，其中40项与修后工作区不同，证明当前游戏安装中尚未应用本轮修复嘎呜

**交接结论：已确认问题的工作区修复完成，修后交叉复核和增量验证通过；全库门禁与实机验收仍未通过／未执行，继续保持未提交、未发布、未部署状态**嘎呜
