# 角色口吻参考入口

角色用语直接参照零协会[罪人语言风格](https://www.zeroasso.top/docs/translate/sinnerstyle/)与[观察记录风格](https://www.zeroasso.top/docs/translate/sinnerrep/)，并检索我们已译的同角色、同剧情阶段对白。人物关系和背景先查巴士 Wiki 对应人物页；不从文学原型推导未出现的游戏经历。

[统一资料入口](../../../../docs/TRANSLATION_GUIDE.md)说明来源优先级与已译文本路径。需要具体语料时，只读取[对应人物档案](../../../../docs/references/02_character_personas/sinners/)中带文件名、ID的引用；档案中的心理分析和未定位例句不作台词模板。

## 容易影响译文的项目特例

| 问题 | 处理方式与定位 |
| --- | --- |
| 浮士德的自称 | 常见第三人称不能覆盖原文第一人称；`Voice_Faust_LCB_10201.json / smalltalk_10201_3` 含第一人称，见[浮士德档案](../../../../docs/references/02_character_personas/sinners/02_faust.md) |
| 良秀同形缩写 | `Voice_EGO_Ryoshu_4.json / battle_awaken_20401_1/2` 的 `모.불.아.위.` 有不同展开；先读同句解释，见[良秀档案](../../../../docs/references/02_character_personas/sinners/04_ryoshu.md)，不固定成四字模板 |
| 但丁的对白与旁白 | 保留原文尖括号区分，不给内心旁白统一加括号或补钟表拟声，见[但丁档案](../../../../docs/references/02_character_personas/sinners/13_dante.md) |
| 堂吉诃德／桑丘 | 按当前身份、时间与对象选称呼，不把老堂与桑丘混为一人，见[观察记录](../../../../docs/references/02_character_personas/observation/obs_don_quixote.md) |
| 默尔索的新剧情 | 优先读已有 `S1061B`、`S1062B` 与探索 `D40815/D40816`，不套“没有感情”的早期印象，见[新剧情入口](../../../../docs/TRANSLATION_GUIDE.md) |
| 观察记录与批注 | 保留原文段落、箭头、犹疑与不同发言人，不补固定汇报结尾或敬礼动作，见[观察资料入口](../../../../docs/references/02_character_personas/observation/obs_overview_and_nicknames.md) |

只为当前句子涉及的称谓、人称、缩写、语气或版本冲突继续查证；不将全部人物档案的重审设为翻译前置条件。
