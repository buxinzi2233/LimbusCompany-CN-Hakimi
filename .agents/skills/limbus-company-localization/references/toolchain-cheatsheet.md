# 都市零协会本地化工程工具链操作手册 (Toolchain Cheatsheet)

本手册汇总了项目 `tools/` 与 `tests/` 目录下所有自动化脚本的命令行参数、常用场景与协同流程。

---

## 1. 静态质检与代码安全引擎: `tools/linter.py`

`linter.py` 是本项目的核心安全网，严格检测并自动修复 8 大质量门禁规则（L01~L08）。

### 命令格式
```bash
python3 tools/linter.py [OPTIONS]
```

### 核心参数
- `--target PATH`：指定待检测目标文件或子目录（默认：`workspace/LLC_zh-CN`）。
- `--fix`：启用安全自动修复模式（自动更正半角波浪号、关键词后置空格、中文标点规范）。
- `--strict`：严苛门禁模式：即使只有 WARNING 警告，也返回非零退出码（适用于 CI / 发布前检查）。
- `--check-korean`：启用未汉化韩文残留深度检测（L08 规则）。
- `--source-dir PATH`：韩文原版资源基准路径（用于 L03 占位符比对）。
- `--rules RULES`：仅执行指定的规则（例如 `--rules L02,L04` 或 `--rules tilde,keyword`）。
- `--json-report PATH`：导出结构化 JSON 报告。
- `-j N` / `--workers N`：多进程并发检测（0 为自动探测 CPU 核心数）。
- `-q` / `--quiet`：静默模式，仅打印汇总统计大表。

### 常用场景范例
```bash
# 场景 1：日常修改单个文件后快速扫描与自动修复
python3 tools/linter.py --target workspace/LLC_zh-CN/Skills_Enemy-a1c10p1.json --fix

# 场景 2：全量工作区安全修复
python3 tools/linter.py --fix

# 场景 3：发布前终审严苛门禁（扫描韩文残留，有警告即阻断）
python3 tools/linter.py --strict --check-korean

# 场景 4：仅针对波浪号与关键词空格做针对性扫描
python3 tools/linter.py --rules L02,L04
```

---

## 2. 端到端分层测试套件: `tests/e2e/run_tests.py`

黑盒 E2E 测试套件，用于验证工作区 17 项系统特性的结构一致性、边界鲁棒性、跨模块契约与部署资源。

### 命令格式
```bash
python3 tests/e2e/run_tests.py [OPTIONS]
```

### 常用参数
- `-v`, `--verbose`：输出每个测试用例的详细执行状态。
- `-t N`, `--tier N`：只运行指定层级测试（1=Feature Coverage, 2=Boundary, 3=Cross-Feature, 4=Real-World）。
- `--report PATH`：输出结构化 JSON 测试指标。

### 执行范例
```bash
# 运行全量 116 项测试
python3 tests/e2e/run_tests.py

# 详细模式排查特定层级
python3 tests/e2e/run_tests.py --tier 2 -v
```

---

## 3. 双版本发布打包工具: `tools/package_release.py`

自动从工作空间抽离、去噪并打包两套独立面向玩家的分发归档包（保存在 `dist/` 目录下）。

### 命令格式
```bash
python3 tools/package_release.py [--version VERSION] [--output-dir OUTPUT_DIR] [--verify-only]
```

### 核心参数
- `--version VERSION`：指定发布版本号标识（如 `2026.09.18` 或 `v1.0.0`）。
- `--output-dir PATH`：产物输出目录（默认 `dist/`）。
- `--verify-only`：仅检验已有 zip 包的哈希与文件完整性，不执行重新打包。

### 产物说明
1. `LLC_zh-CN-Full-v<VER>.zip`（完整版）：包含全部战斗机制 + 第 10 章完整剧情 + RPGSystem 探索对话。
2. `LLC_zh-CN-CombatOnly-v<VER>.zip`（仅战斗辅助版）：自动过滤剔除 `StoryData/` 与 `RPGSystem/` 中的新章节，战斗纯汉化，新剧情无缝 fallback 回退官方原生文本。

---

## 4. 冻结基准回归门禁: `tools/verify_release.py`

在打包或部署前，对比基准韩文与中文资源，确保零意外回归。

### 命令格式
```bash
python3 tools/verify_release.py \
  --workspace workspace/LLC_zh-CN \
  --source <PATH_TO_KR_SOURCE> \
  --baseline-kr <PATH_TO_FROZEN_KR> \
  --baseline-zh <PATH_TO_FROZEN_ZH> \
  --report dist/verification_report.json
```

---

## 5. Steam 原生模组部署: `tools/deploy_mod.py`

将工作区中经过验证的汉化资源与 23.8MB 更纱黑体（Sarasa Gothic SC）部署至 Steam 游戏运行目录。

### 命令格式
```bash
python3 tools/deploy_mod.py
```

### 关键防呆机制
- 验证 `ChineseFont.ttf` 文件的 SHA-256：`a56a06f1af27726bc5def015b61deecbbdf5ae6d954a91b1131d8a17290def35`。
- 自动备份原有的语言文件夹与 `config.json`。
- 采用原子替换（Atomic Swap），部署失败自动回滚，杜绝半成品损坏游戏。

---

## 6. 辅助差分与版本工具
- `tools/diff_extractor.py`：对比游戏客户端更新与工作区既有译文，提取新赛季新增待翻译文件列表。
- `tools/game_update_watcher.py`：监控 Steam 本地游戏更新与补丁版本变动。
- `tools/manage_game_lang.py`：切换游戏配置中的语言设置。
