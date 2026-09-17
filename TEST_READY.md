# 当前验收与交付状态嘎呜

当前已完成调研与零协会风格修正并备份部署，范围、18 字段修订与证据统一见 [当前修正报告](docs/reports/final-polish-style-review.md) 嘎呜。

- [TODO](TODO.md)、[逐字段差异](docs/reports/style-alignment-diff.json)、[可读补丁](docs/reports/style-alignment.diff) 嘎呜。
- [当前资源门禁及哈希](docs/reports/style-alignment-release-check.json)、[原始全库扫描](docs/reports/style-alignment-lint.json)、[当前部署回执](docs/reports/style-alignment-deployment.json) 嘎呜。
- 67 项 linter 测试、3 项集成测试及 116 项静态 E2E 全部通过；原始全库扫描仍有 25798 项历史告警，不能称为全库零问题嘎呜。
- 当前修正版的游戏内表现、字体挂载，以及被动 1041621 源文冲突仍待验证，测试通过不能代替这些验收嘎呜。

复验时，明确指定客户端韩文源目录，再执行现有入口嘎呜。

```bash
SOURCE_KR='/home/buxinzi/.local/share/Steam/steamapps/common/Limbus Company/LimbusCompany_Data/Assets/Resources_moved/Localize/kr'
python3 -m unittest discover -s tests -p 'test_linter.py'
python3 -m unittest tests.test_release_integrity
python3 tests/e2e/run_tests.py
python3 tools/linter.py --target workspace/LLC_zh-CN --source-dir "$SOURCE_KR" --check-korean --strict --json-report docs/reports/style-alignment-lint.json --quiet
python3 tools/verify_release.py --workspace workspace/LLC_zh-CN --source "$SOURCE_KR" --baseline-kr references/baseline-KR --baseline-zh references/baseline-zh-CN --report docs/reports/style-alignment-release-check.json
```

后续部署使用 `tools/deploy_mod.py`，明确传入 `--workspace`、`--source`、`--lang-dir`、`--report` 和不存在的 `--backup` 目录，报告过期、源变更或复制不一致必须报错嘎呜。
两个版本打包及 GitHub 发布仍暂停，本轮未创建仓库或提交嘎呜。
