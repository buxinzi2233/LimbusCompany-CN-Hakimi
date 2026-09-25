# 本地翻译参考资源

既有设定与翻译规范的上游入口、已译新剧情查法统一见[翻译资料入口](../docs/TRANSLATION_GUIDE.md)。本目录提供本地检索与版本比对数据；目录名本身不证明全部内容来自同一发布版本。

## 当前优先参考

已下载并校验零协会 **2026092102** 原包，优先按同 ID 检索 `LLC-2026092102/LimbusCompany_Data/Lang/LLC_zh-CN/`；其与工作区格式、安全门禁和旧译名的差异，统一见[更新调研](../docs/reports/zeroasso-update-research.md)。不要用旧 `baseline-zh-CN` 覆盖新版已确认译名。

## 只读基准

**不要修改或删除下列基准子目录及历史包**；差异工具、语言资源管理和发布测试依赖其路径，翻译改动写入 `workspace/LLC_zh-CN/`。

| 位置 | 用途与边界 |
| --- | --- |
| [baseline-zh-CN](baseline-zh-CN/) | 既有零协会中文译名与台词的优先检索入口；本地整理数据不等于某一发布包的原样副本，遇到具体版本冲突再与冻结包比对 |
| [baseline-KR](baseline-KR/) | 冻结韩文，用于历史差异；新版本句义和占位符应检查当前客户端对应记录 |
| `LLC-2026092102/`、`LLC-2026092102.zip` | 新版零协会原样快照与 ZIP，保留上游文件结构，不直接视为通过本项目门禁的发布物 |
| `LLC-2026090501/`、`LLC-2026090501.zip` | 已保存的零协会历史发布快照，供版本追溯和指定基准的测试使用 |

当前机器的客户端韩文目录：

```text
/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr
```

该目录中的文件通常带 `KR_` 前缀，按相对目录和记录 ID 对应中文文件；剧情对白还要核对说话人与上下文。新赛季译文已在[工作区](../workspace/LLC_zh-CN/)中，不应只查冻结基准就认定“没有译过”。

[tools/linter.py](../tools/linter.py)支持 `--source-dir` 显式指定韩文；未指定时，读取 `source-snapshot.json` 指定的版本化源路径并校验源清单哈希，不再静默采用 Steam 旧导出；本地快照不随 Git 分发，缺失时明确失败，必须恢复对应快照或显式指定源目录。占位符对照需要对应原文，韩文残留检查由 `--check-korean` 开启；检查通过与翻译语义正确是不同结论。

## 词条索引

[战斗词条 ID 与译名速查](battle_keywords_glossary.md)用于查找名称和来源。S8 词条现已对齐新版零协会，具体格式差异见更新调研；表中缩略说明不替代 JSON 的完整触发条件、数值和限制。内置 ID 也不是官方英文显示名。
