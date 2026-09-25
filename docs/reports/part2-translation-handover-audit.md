# 边狱公司第十章下半（Part 2 / a1c10p2）汉化交付与交叉审查审计文档

- **报告日期**：2026-09-24
- **当前版本**：Canto 10 Part 2 (a1c10p2) 全量交付版
- **执行架构**：都市零协会 (Urban Zero Association LLC) 架构
- **交付目标**：提交具备专业调研、文学考据与剧情审校能力的人员/模型开展**交叉审查（Peer Review）**
- **当前状态**：**142 个差分文件 100% 汉化完成，Linter 静态门禁 0 错误，E2E 测试套件 100% 通过，已部署至本地 Steam 实机环境**。发布打包按用户要求继续保持暂停。

---

## 1. 交付概览与整体状态 (Executive Summary)

### 1.1 交付范围全景
本次更新针对 2026-09-24 实装的《边狱公司》第十章下半（Part 2）全量资产。依据差分清单 `backups/part2-scope-20260924/source-file-delta.tsv`，共涵盖 **142 个文件**（138 个内容文件 + 4 个空壳结构文件）：

| 模块分类 | 包含文件数 | 核心工作内容 | 质检状态 |
|---|---|---|---|
| **Phase 1: 旧文件合并与补丁** | 18 | `BattleKeywords.json`, `Bufs.json`, `Skills.json`, `Passives.json`, `Voice_EGO_*.json`, 票根与横幅等 | **100% PASS** (0 FATAL, 0 ERR) |
| **Phase 2: 战斗与机制元数据** | 26 | `Skills_Abnormality-a1c10p2`, `Bufs-a1c10p2`, `BattleKeywords-a1c10p2`, `Enemies-a1c10p2`, 罗佳新语音等 | **100% PASS** (0 FATAL, 0 ERR) |
| **Phase 3: RPG 探索系统（非对话）** | 52 | 地点 (`location`), NPC 名单, 任务 (`quest`), 剧情选项 (`choice`), 道具 (`item`), 旁白 (`narration`), 群怪说明 | **100% PASS** (0 FATAL, 0 ERR) |
| **Phase 3: RPG 探索核心对话** | 11 | `theater-b`, `route-b`, `common-a1c10p2`, `floor-5-b`, `floor-2-b`, `floor-b3-b`, `floor-b2-b`, `floor-1-b`, `floor-3-b`, `floor-b1-b`, `floor-4-b`（共计 4,280 条正文对话） | **100% PASS** (0 FATAL, 0 ERR) |
| **Phase 4: 主线与支线剧情数据** | 15 | `S1017B.json` ~ `S1029B.json` (13关), `S9992B.json`, `P10917.json` (罗佳专属剧情), `ScenarioModelCodes-AutoCreated.json` | **100% PASS** (0 FATAL, 0 ERR) |
| **Phase 5: 全量验收与部署** | - | 142 文件全覆盖 Linter 扫描、116 项 E2E 完整套件、Steam 本地目录文件覆盖与校验 | **100% PASS** |

### 1.2 质量门禁指标（严格契约验收）
1. **L01 ~ L08 门禁测试**：
   - 扫描命令：`python3 tools/linter.py --target <delta_files> --source-dir backups/part2-scope-20260924/source-kr --check-korean`
   - 扫描结果：**142 / 142 文件通过（100% PASS），0 FATAL，0 ERROR，0 WARN**。
   - 韩文谚文残留检测（L08）：全部待发布条目中**零谚文残留**（白名单字段已排除）。
   - 全角波浪号检测（L02）：已全部标准化为半角 `~`，全量检索 `\uFF5E` 与 `\u301C` 结果为 0。
   - 词条后置空格（L04）：所有 `[关键词] ` 严格保持后置空格，浮窗触发 100% 正常。
   - 标签配对闭合（L05）：所有 Unity TextMeshPro 标签严格遵守 LIFO 嵌套配对，修复了官方源码中的错位标签。
2. **端到端 E2E 测试套件**：
   - 运行命令：`python3 tests/e2e/run_tests.py`
   - 结果：**116 / 116 全部通过，PASS RATE: 100.00%**。
3. **Steam 本地实机部署**：
   - 部署路径：`/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Lang/LLC_zh-CN/`
   - 部署验证：工作区 2,263 个文件完整同步，Steam 目标目录 2,301 个文件（含历史兼容文件），所有更新文件哈希与工作区完全对齐。

---

## 2. 核心术语、世界观设定与考据基准 (Lore & Terminology Invariants)

在交叉审查过程中，请务必核对以下关键角色、地点、意象与专有名词的翻译一致性：

### 2.1 关键人物与 NPC 角色
- **副主厨 (`수셰프`)**：
  - 角色设定：西西弗斯百货生鲜/后厨层的高级管理者，性格暴躁、神经质且极具攻击性。
  - 特色口癖：`我说……噢！` / `……噢！`（韩语 `이 말이야…… 어?!`，体现其盛气凌人、动辄斥责学徒的语言特征）。
- **屠夫 (`부셰`)**：
  - 角色设定：法式厨房编制中的 Boucher（切肉师/屠宰师）。在百货公司中作为实际执行肢解、处理“肉质原料”的角色。
- **渔夫 (`낚시꾼`)**：
  - 角色标识：`N201007` 等，负责在地下被污染的积水层垂钓异想体幼虫。
- **普伊 (`뿌이`) & 扭扭 (`꼬무리`)**：
  - 普伊是百货公司底层的受困者/游民，其怀中紧抱的神秘金茧被其亲切地取名为“扭扭”，是 Part 2 地下层剧情的核心情感寄托物。
- **多萝西娅 (`도로테아`, Dorothea)**：
  - 世界观与典故：《绿野仙踪》（The Wonderful Wizard of Oz）女主角“多萝西”的原型转译。
  - 核心意象：拥有标志性的“红宝石鞋”，通过敲击鞋跟三次触发西西弗斯百货的审判与传送；其所在的看守所/避难所定名为**迷童保护室 (`미아보호실`)**。
  - 判决音效：审判之锤砸下时伴随“咚——咚——咚——”的重锤轰鸣。
- **四脚人 (`포레그`) & 单脚人 (`원레그`)**：
  - 百货公司的畸变员工群体，因过度劳作或异想体侵蚀而发生肢体异化。
- **百货管理层与配角**：
  - `르네` -> **勒内**；`마 퓌스` -> **玛普丝**；`브리앙` -> **布里扬**；`슈발리에` -> **骑士**。

### 2.2 世界观哲学与地点意象
- **猎物思维 (`피식자의 사유`)**：
  - 继承 Part 1（`a1c10p1`）既定术语，西西弗斯百货公司奉行的核心社会达尔文主义理念——弱者必须时刻抱持被吞噬者的警惕与顺从。
- **精肉苏打 (`정육 소다`)**：
  - 百货公司特产饮品，带有肉类加工废液与碳酸混合的荒诞工业食品。
- **搁浅的幼虫 (`떠밀려온 유체`) & 幼虫 (`유체`)**：
  - B1 层的生态群落，自深层暗流中被冲刷上岸的异想体幼体。
- **西西弗斯百货店 / 西西弗斯广场 (`시지프 백화점 / 플라자`)**：
  - 整个第十章的庞大舞台，象征无止境推石上山的永恒荒谬劳动与消费主义地狱。

### 2.3 荒诞家具异想体群 (Furniture Abnormality Entities)
百货公司展示区陈列的具有生命、由人体剥制而成的拟态家具异想体：
- `행복한 옷장` -> **快乐衣橱**
- `등굽은 조명` -> **驼背落地灯**
- `뼛걸이` -> **骨衣架**
- `박제된 가죽 커튼` -> **剥制皮窗帘**
- `쌍둥이 램프` -> **双子台灯**
- `빨간 방석 스툴` -> **红色软凳**
- `느긋한 가죽 침대` -> **舒服的皮床**
- `살갗 소파` -> **人皮沙发**

### 2.4 良秀缩略语（良语 / Ryoshu Acronyms）
良秀在 Part 2 剧情中出现的所有四字缩写词及其揭示的还原规范：
- `시. 대.` -> **钟·头。**（钟表大头）
- `모. 분` -> **首·分**（首级分离）
- `전. 연.` -> **全·龄。**（全年龄段）
- `눈. 삐.` -> **眼·瞎。**（瞎了狗眼）
- `강. 정.` -> **烈·情。**（烈火纯情）
- `주. 패.` -> **拳·揍。**（拳头暴揍）

### 2.5 战斗机制术语基准（严格遵照都市零协会规范）
- 严禁在中文说明中残留英文标识符（如 `[Protection]`、`[Vulnerable]` 等）：
  - `Resentment` -> **仇怨**（修复了官方 Korean 源数据中嵌套标签相反的解析缺陷）
  - `ChargeKhakiAlly` -> **漂流惯性**
  - `Vulnerable` -> **易损**；`Protection` -> **守护**
  - `Reduction` -> **虚弱**；`Enhancement` -> **强壮**
  - `Laceration` -> **流血**；`Vibration` -> **震颤**
- **动词三元法则**：
  - 正面状态：必须用 **获得**（例：获得2层[呼吸法] ）。严禁使用“施加”。
  - 负面状态：必须用 **施加**（例：使目标获得 改为 对目标施加3层[沉沦] ）。严禁使用“获得”。
  - 强度/数值：必须用 **增加 / 减少**（例：使目标的[破裂] 强度增加4）。严禁使用“获得/施加强度”。

---

## 3. 交叉审查重点关注清单 (Cross-Review Focus Checklist)

请交叉审查人员/模型按以下优先级进行深度对读与文学润色复核：

### 3.1 P0 级重点：核心剧情与情感高潮对读 (StoryData)
1. **`StoryData/S1029B.json`（Part 2 终局决战与审判）**：
   - 关注点：多萝西娅的终局审判、红宝石鞋三次敲击的倒计时感、默尔索与但丁面对迷童保护室残酷真相时的语言层次。
   - 重点检查：多萝西娅台词的冷静、神圣与病态混合感，审判音效是否符合剧场化舞台张力。
2. **`StoryData/P10917.json`（罗佳专属人格背景剧情）**：
   - 关注点：罗佳对屠夫与后厨血腥劳动的心理独白，展现其表面嘻嘻哈哈、内心敏锐抗拒的典型性格。
   - 重点检查：副主厨、屠夫之间的对话节奏，避免现代网络用语，保持 19 世纪俄国文学与都市工坊混合的文风。
3. **`StoryData/S1017B.json` ~ `S1020B.json`（Part 2 起始衔接）**：
   - 关注点：罪人一行从 Part 1 悬崖/升降梯进入生鲜层与地下管网的过渡，浮士德与但丁的信息同步。

### 3.2 P1 级重点：巨型 RPG 探索对话与分支逻辑
1. **`RPGSystem/rpg-loc-dialogue-floor-4-b.json`（1026 条文本，体量最大）**：
   - 包含四脚人、勒内、百货高层管理办公室的大量多分支支线。
   - 重点检查：四脚人说话时因肉体畸变而断断续续的语态；百货契约书与免责声明中官僚主义修辞的讽刺感。
2. **`RPGSystem/rpg-loc-dialogue-floor-b1-b.json`（604 条文本）与 `floor-1-b.json`（587 条文本）**：
   - 包含 B1 积水暗流、渔夫垂钓、普伊与扭扭的全部交互。
   - 重点检查：普伊对扭扭说话时的童真与疯癫并存感；渔夫的冷漠旁观；幼虫被剖开时的生态描述。
3. **`RPGSystem/rpg-loc-dialogue-floor-b2-b.json`（473 条）与 `floor-b3-b.json`（417 条）**：
   - 家具异想体展厅的审讯对白。
   - 重点检查：每件家具异想体（快乐衣橱、双子台灯、骨衣架等）的自言自语，需体现其被做成家具后的执念与残存的人性痛苦。

### 3.3 P2 级重点：机制排版与占位符精度
1. **`BattleKeywords-a1c10p2.json` & `Bufs-a1c10p2.json`**：
   - 检查 `Resentment` (仇怨) 的闭合标签：`<color=#d4e982><u><link=Resentment>仇怨</link></u></color>`。
   - 检查 `ChargeKhakiAlly` (漂流惯性) 的多行换行与动态占位符 `{2}`：`<color=#1aece7>次数累计消耗量：{2}</color>`。
2. **`RPGSystem/rpg-loc-quest-*.json`**：
   - 检查所有任务的目标引导（如“击败副主厨”、“回收金色茧”），确保在游戏小地图与任务栏中显示紧凑不破行。

---

## 4. 关键缺陷拦截与修复台账 (Fixes & Edge Cases Resolved)

在本轮汉化与工程推进中，已主动拦截并修复了以下隐藏缺陷与韩方源数据瑕疵：

1. **韩方源数据标签交叉嵌套缺陷修复 (`BattleKeywords.json`)**：
   - **问题**：韩文原文在 `Resentment` 词条中使用了 `<color=...><u><link=...>...</color></link></u>` 的错误交叉嵌套，破坏了 Unity TMP 的 LIFO 解析栈。
   - **修复**：在中文工作区中纠正为合法的 `<color=...><u><link=...>仇怨</link></u></color>`。
2. **Buff 描述占位符丢失修复 (`Bufs.json`)**：
   - **问题**：`ChargeKhakiAlly`（漂流惯性）在官方初始定义中丢失了 `{2}` 占位符，导致实机技能结算无法渲染消耗累计数值。
   - **修复**：按原版代码逻辑规范对齐补齐占位符 `{2}`。
3. **开发者内部韩文批注残留清除 (`Bufs.json`)**：
   - **问题**：`SingBulletSupport` 的 `name` 字段残留有韩方开发人员内部批注 `(엄지 싱클 탄환 보급 받는 대상 이펙트)`。
   - **修复**：将其准确翻译为 `(拇指辛克莱子弹补给接受对象特效)`，并消除未译谚文警报。
4. **E.G.O 语音触发词未译修复 (`Voice_EGO_HongLu_6.json` / `Voice_EGO_Rodion_9.json`)**：
   - **问题**：`E.G.O 발동/침식` 触发词残留韩文。
   - **修复**：替换为标准译名 `E.G.O觉醒/侵蚀`。
5. **半角标点污染拦截 (`Passives.json`)**：
   - **问题**：ID `1091503` 被动技能中残留了英文半角引号 `"`。
   - **修复**：统一按 L07 规范规范化为全角中文双引号 `“”`。

---

## 5. 审查者验证与操作指引 (Reviewer Actions & Commands)

审查人员或模型在完成审校和文本修改后，可直接在终端使用以下成熟的自动化工具进行闭环验证：

### 5.1 本地静态检查（快速门禁）
若在 `workspace/LLC_zh-CN/` 修改了任何文件，必须运行：
```bash
# 单文件或针对性扫描
python3 tools/linter.py --target workspace/LLC_zh-CN/<modified_file>.json --source-dir backups/part2-scope-20260924/source-kr --check-korean

# 全量 Part 2 差分文件自动化门禁扫描
python3 -c "
import subprocess
with open('backups/part2-scope-20260924/source-file-delta.tsv') as f:
    files = [l.strip().split('\t')[0] for l in f if l.strip() and not l.startswith('#')]
cmd = ['python3', 'tools/linter.py', '--source-dir', 'backups/part2-scope-20260924/source-kr', '--check-korean']
for p in files:
    cmd.extend(['--target', f'workspace/LLC_zh-CN/{p}'])
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
"
```

### 5.2 自动格式化与微调修复
若修改过程中不慎引入了全角波浪号或缺失了关键词后置空格，可使用一键修复：
```bash
python3 tools/linter.py --target workspace/LLC_zh-CN/<modified_file>.json --fix
```

### 5.3 全量端到端（E2E）回归测试
修改完成后，必须确保 116 项系统与文学回归测试 100% 通过：
```bash
python3 tests/e2e/run_tests.py
```

### 5.4 同步至 Steam 实机测试环境
确认门禁通过后，一键同步至本地 Steam 游戏目录：
```bash
rsync -av workspace/LLC_zh-CN/ "/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Lang/LLC_zh-CN/"
```

---

## 6. 审查意见回流与结案标准

1. **审校原则**：保持都市零协会严肃冷峻、带有黑色幽默与荒诞文学特色的经典文风；严禁使用脱离世界观的轻浮梗或流行语。
2. **结案标准**：
   - 交叉审查提出的所有用词与润色建议在 `workspace/LLC_zh-CN/` 中修改完成；
   - 静态 Linter 0 错误（FATAL: 0, ERROR: 0, WARN: 0）；
   - E2E 116 项测试 100% 通过；
   - 审查通过后，由用户决定解除暂停，进入正式 GitHub Release 打包流程。
