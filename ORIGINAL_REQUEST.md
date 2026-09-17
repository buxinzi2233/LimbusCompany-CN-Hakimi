# Original User Request

## 2026-09-17T17:35:47+08:00

# Teamwork Project Prompt — Launched

> Status: Launched
> Goal: Full-scope localization of Limbus Company new season update
> Requested team: Full team (multi-agent team for research, translation, verification, and localization deployment)

为《边狱公司》（Limbus Company）最新赛季（包含 a1c10p1 及全量新增资源）进行本地化汉化，严格遵循都市零协会（LLC）技术架构、文风规范与“信”字哲学，完成全量主线剧情文本、UI文本、敌方机制文本与状态技能的高质量译制与本地工程化部署。

Working directory: /home/buxinzi/Documents/巴士汉化-哈基米版
Game path: /home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/
Integrity mode: development

## Requirements

### R1. 全域文本差分锁定与目录对齐
- 针对最新下载的客户端（包含 `a1c10p1` 相关的全部机制文件与新剧情文件），以零协会官方现行汉化目录 `workspace/LLC_zh-CN` 为基线，提取全量待翻译文件。
- 覆盖范围必须 100% 对齐零协会汉化广度：
  1. **主线剧情文本**（`StoryData/` 下的全部新增剧情章节）；
  2. **UI 文本**（`MainUIText-a1c10p1.json`, `BattlePass-a1c10.json`, `BattleResultHint-a1c10p1.json` 等）；
  3. **敌方机制与战斗文本**（`Enemies-a1c10p1.json`, `Skills_Enemy-a1c10p1.json`, `Passives_Enemy-a1c10p1.json`, `Skills_Abnormality-a1c10p1.json`, `Passives_Abnormality-a1c10p1.json`, `BattleKeywords-a1c10p1.json`, `Bufs-a1c10p1.json`, `PanicInfo-a1c10p1.json`）；
  4. **播报员、关卡节点与物品**（`Announcer-a1c10p1.json`, `StageNode-a1c10p1.json`, `Items-a1c10p1.json`）。

### R2. 严格遵循零协会规范的高保真译制
- 严禁使用 GLM 模型进行文本翻译（仅可作为语法质检力工）。
- 动词层数严格区分：正面层数“获得”、负面层数“施加”、数值强度一律“增加”。
- 关键字空格后置机制：`[关键词] `（必须后置一个半角空格激活词条高亮与浮窗）。
- 标点符号铁律：全角波浪号 `～` 100% 绝对封杀，强制使用半角 `~`；剧情统一使用六点省略号 `……` 与全角双引号 `“”`。
- 角色口吻对齐：剧情文本严格对齐《15 核心角色语言风格研报》与实机语料库标准。

### R3. 本地工程化落地、自动化质检与 Steam 部署
- 编写/运行质检脚本 `tools/linter.py`，执行 100% 全量扫描：0 语法错误、0 全角波浪号、占位符 `{0}` 1:1 一致。
- 部署至游戏官方原生目录 `LimbusCompany_Data/Lang/LLC_zh-CN/`，确保 23.8MB 更纱黑体正确挂载。

## Acceptance Criteria

### 文本覆盖与完整性
- [ ] 所有 `a1c10p1` 系列新增机制与 UI 文件均已汉化并合并入工作空间。
- [ ] 新增剧情故事文本均已规范汉化。
- [ ] 战斗关键词与 Buff 描述 100% 正确触发游戏高亮。

### 质量与安全性
- [ ] 0 个全角波浪号 `～`（无字体方框乱码隐患）。
- [ ] 0 个破坏性 JSON 语法错误或未闭合富文本标签。
- [ ] 游戏启动后可在主界面直接载入并正常显示新赛季汉化。
