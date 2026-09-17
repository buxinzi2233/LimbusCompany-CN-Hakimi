# -*- coding: utf-8 -*-
import json
import os

ZH_DIR = "/home/buxinzi/Documents/巴士汉化-哈基米版/workspace/LLC_zh-CN/RPGSystem"

quests_floor_1 = [
  {
    "key": "Q1000",
    "title": "序幕",
    "description": "加载后播放开场演出(S1001B)的处理用隐藏任务",
    "steps": [{"index": 0}]
  },
  {
    "key": "Q1011",
    "title": "环顾四周",
    "description": "来到了名为西西弗斯百货公司的地方。默尔索究竟在哪里呢？总之先环顾四周确认情况为好。",
    "steps": [{"index": 0, "goalDescription1": "环顾四周"}]
  },
  {
    "key": "Q1012",
    "title": "返回盥洗室",
    "description": "在西西弗斯百货公司遇到了克罗默的亲姐姐。先回到盥洗室重新整顿一下吧。",
    "steps": [{"index": 0, "goalDescription1": "返回盥洗室"}]
  },
  {
    "key": "Q1013",
    "title": "寻找默尔索",
    "description": "在盥洗室见到了默尔索。但他却提出希望我们能够协助他。先听听他的说法吧。",
    "steps": [{"index": 0, "goalDescription1": "与默尔索搭话"}]
  },
  {
    "key": "Q1014",
    "title": "???",
    "description": "???",
    "steps": [{"index": 0, "goalDescription1": "与默尔索搭话"}]
  },
  {
    "key": "Q1021",
    "title": "寻找默尔索 2",
    "description": "默尔索说他在美妆馆深处发现了可疑的人体模特。去美妆馆深处找他吧。",
    "steps": [{"index": 0, "goalDescription1": "前往美妆馆深处"}]
  },
  {
    "key": "Q1022",
    "title": "默尔索的提议",
    "description": "默尔索提议由罪人们来帮助人体模特们退场。听取他具体的想法吧。",
    "steps": [{"index": 0, "goalDescription1": "与默尔索搭话"}]
  },
  {
    "key": "Q1023",
    "title": "人体模特退场",
    "description": "为了帮助人体模特退场，必须拔除刺入其体内的钉子。用默尔索递过来的拔钉器拔除钉子吧。",
    "steps": [{"index": 0, "goalDescription1": "拔除人体模特的钉子"}]
  },
  {
    "key": "Q1031",
    "title": "环顾西西弗斯百货公司",
    "description": "成功帮助人体模特退场了。现在去看看西西弗斯百货公司的其他区域吧。",
    "steps": [{"index": 0, "goalDescription1": "环顾快时尚馆"}]
  },
  {
    "key": "Q1032",
    "title": "环顾西西弗斯百货公司 2",
    "description": "快时尚馆里有许多店员和顾客。去探探更深处的卖场吧。",
    "steps": [{"index": 0, "goalDescription1": "前往当代馆"}]
  },
  {
    "key": "Q1041",
    "title": "浏览陈列的服装",
    "description": "雷诺阿当代馆里陈列着诸多具有古典气息的服饰。浏览一下展示品吧。",
    "steps": [{"index": 0, "goalDescription1": "浏览陈列的服装"}]
  },
  {
    "key": "Q1042",
    "title": "抵挡发起袭击的雷诺阿员工",
    "description": "雷诺阿的员工们突然发难发起攻击。将他们击退吧。",
    "steps": [{"index": 0, "goalDescription1": "击退雷诺阿员工"}]
  },
  {
    "key": "Q1051",
    "title": "前往勒鲁日的卖场",
    "description": "雷诺阿对面的勒鲁日卖场似乎传来了不寻常的动静。过去看看吧。",
    "steps": [{"index": 0, "goalDescription1": "前往勒鲁日当代馆"}]
  },
  {
    "key": "Q1052",
    "title": "寻获巨大针钉",
    "description": "勒鲁日的含羞草请求我们去寻获一根43cm的巨大针钉。去寻找针钉吧。",
    "steps": [{"index": 0, "goalDescription1": "寻获巨大针钉"}]
  },
  {
    "key": "Q1061",
    "title": "选购服装",
    "description": "含羞草赠予了我们服装。为前往上一层做好充分的穿搭准备吧。",
    "steps": [{"index": 0, "goalDescription1": "确认穿搭装扮"}]
  },
  {
    "key": "Q1062",
    "title": "前往自动扶梯",
    "description": "1层的探索告一段落。前往自动扶梯厅，准备登上2层吧。",
    "steps": [{"index": 0, "goalDescription1": "前往自动扶梯"}]
  },
  {
    "key": "Q1064",
    "title": "搭乘自动扶梯",
    "description": "站上通往2层的自动扶梯，向名品馆所在的楼层进发吧。",
    "steps": [{"index": 0, "goalDescription1": "搭乘自动扶梯前往2层"}]
  },
  {
    "key": "Q1018",
    "title": "???",
    "description": "???",
    "steps": [{"index": 0, "goalDescription1": "探索未知区域"}]
  },
  {
    "key": "Q1001",
    "title": "任务1 - 开始",
    "description": "第1层探索启动引导任务",
    "steps": [{"index": 0, "goalDescription1": "踏入第1层大堂"}]
  }
]

quests_floor_2 = [
  {
    "key": "Q2001",
    "title": "环顾2层",
    "description": "抵达了2层名品馆入口。四周弥漫着格外压抑浓烈的异样香气。先观察一下周围吧。",
    "steps": [{"index": 0, "goalDescription1": "环顾2层入口"}]
  },
  {
    "key": "Q2002",
    "title": "前往2层",
    "description": "深入2层前线，找寻通向深处的通路。",
    "steps": [{"index": 0, "goalDescription1": "前往名品馆大厅"}]
  },
  {
    "key": "Q2003",
    "title": "进入名品馆",
    "description": "推开名品馆沉重的大门，踏入展厅核心区域。",
    "steps": [{"index": 0, "goalDescription1": "进入名品馆"}]
  },
  {
    "key": "Q2011",
    "title": "击退蜂拥而至的勒鲁日们",
    "description": "狂热的勒鲁日教徒与守卫如潮水般蜂拥袭来。全员进入迎击态势将其彻底击溃！",
    "steps": [{"index": 0, "goalDescription1": "消灭阻挡前路的勒鲁日群体"}]
  },
  {
    "key": "Q2004",
    "title": "进入帷幕之中",
    "description": "撕开层层帷幕，直面名品馆深处隐匿的崇拜圣所。",
    "steps": [{"index": 0, "goalDescription1": "穿过帷幕"}]
  }
]

quests_floor_3 = [
  {
    "key": "Q3001",
    "title": "前往3层",
    "description": "搭乘扶梯登上3层。这里是高级定制与面料工坊的中心。",
    "steps": [{"index": 0, "goalDescription1": "踏上3层"}]
  },
  {
    "key": "Q3002",
    "title": "顺着剪刀声寻去",
    "description": "耳畔传来了咔嚓咔嚓清脆而诡谲的剪刀裁切声。顺着声响追寻来源吧。",
    "steps": [{"index": 0, "goalDescription1": "寻访剪刀声源头"}]
  },
  {
    "key": "Q3003",
    "title": "前往走廊",
    "description": "穿过嘈杂的工坊区，向主干走廊挺进。",
    "steps": [{"index": 0, "goalDescription1": "前往走廊"}]
  },
  {
    "key": "Q3004",
    "title": "环顾3层",
    "description": "仔细勘察3层的各处店铺与工坊分布。",
    "steps": [{"index": 0, "goalDescription1": "环顾3层主要展区"}]
  },
  {
    "key": "Q3005",
    "title": "与精品店的勒鲁日搭话",
    "description": "与驻守在精品店前台的勒鲁日员工交涉，打探楼层机密。",
    "steps": [{"index": 0, "goalDescription1": "与精品店店员交谈"}]
  },
  {
    "key": "Q3006",
    "title": "前往广播室",
    "description": "百货公司的广播播报似乎是从这一层的广播室发出的。前去一探究竟。",
    "steps": [{"index": 0, "goalDescription1": "前往广播室"}]
  },
  {
    "key": "Q3007",
    "title": "返回不可移动身边",
    "description": "带着收集到的信息，返回向名为不可移动的存在汇报。",
    "steps": [{"index": 0, "goalDescription1": "与不可移动对话"}]
  },
  {
    "key": "Q3008",
    "title": "返回不可移动身边",
    "description": "再次与不可移动确认下一阶段的突击方案。",
    "steps": [{"index": 0, "goalDescription1": "与不可移动搭话"}]
  },
  {
    "key": "Q3009",
    "title": "尝试与两件套搭话 2",
    "description": "两件套似乎知晓某些不为人知的内部矛盾。进一步试探他的态度。",
    "steps": [{"index": 0, "goalDescription1": "与两件套交谈"}]
  },
  {
    "key": "Q3010",
    "title": "前往缝补室",
    "description": "前往缝补师阿内特所在的缝补室，寻求破解僵局的专业工具。",
    "steps": [{"index": 0, "goalDescription1": "前往缝补室"}]
  },
  {
    "key": "Q3012",
    "title": "前往右侧",
    "description": "沿右侧回廊深入，突破防御薄弱的侧翼。",
    "steps": [{"index": 0, "goalDescription1": "穿过右侧通道"}]
  },
  {
    "key": "Q3013",
    "title": "消灭着魔的雷诺阿们",
    "description": "数名狂暴失控、彻底着魔的雷诺阿员工拦住了去路。将其全部肃清！",
    "steps": [{"index": 0, "goalDescription1": "击杀着魔的雷诺阿"}]
  },
  {
    "key": "Q3011",
    "title": "购买剪刀结束会议",
    "description": "买下一把特制裁缝剪刀，强制打断并解散僵持不下的荒唐会议。",
    "steps": [{"index": 0, "goalDescription1": "购买剪刀"}]
  },
  {
    "key": "Q4014",
    "title": "将情报传达给雷诺阿们",
    "description": "把关键军情与裁决转告给雷诺阿一方，促成局势逆转。",
    "steps": [{"index": 0, "goalDescription1": "与雷诺阿代表交谈"}]
  },
  {
    "key": "Q4015",
    "title": "前往缝补室",
    "description": "再次返回缝补室，向阿内特求取更高级别的工坊物资。",
    "steps": [{"index": 0, "goalDescription1": "进入缝补室"}]
  },
  {
    "key": "Q4017",
    "title": "前往勒鲁日精品店",
    "description": "突入勒鲁日精品店核心陈列区，压制守军。",
    "steps": [{"index": 0, "goalDescription1": "踏入精品店"}]
  },
  {
    "key": "Q4016",
    "title": "获取“钉子”并前往雷诺阿之屋",
    "description": "取到关键的钉子道具后，全速赶往雷诺阿之屋完成部署。",
    "steps": [{"index": 0, "goalDescription1": "前往雷诺阿之屋"}]
  },
  {
    "key": "Q3016T",
    "title": "楼层经理战斗开始信号",
    "description": "触发3层楼层经理Boss战的系统引导信号",
    "steps": [{"index": 0, "goalDescription1": "进入对决"}]
  },
  {
    "key": "Q3016H1",
    "title": "楼层经理攻击 1",
    "description": "抵御楼层经理的第一波狂暴打击",
    "steps": [{"index": 0, "goalDescription1": "抵御打击 1次"}]
  },
  {
    "key": "Q3016H2",
    "title": "楼层经理攻击 2",
    "description": "抵御楼层经理的第二波致命狂攻",
    "steps": [{"index": 0, "goalDescription1": "抵御打击 2次"}]
  }
]

quests_floor_4 = [
  {
    "key": "Q4001",
    "title": "前往4层",
    "description": "带上雷诺阿开具的鉴定书，搭乘扶梯登上4层。",
    "steps": [{"index": 0, "goalDescription1": "搭乘通往4层的自动扶梯"}]
  },
  {
    "key": "Q4002",
    "title": "环顾4层",
    "description": "来到了4层。这里又有哪些卖场呢？总之先向右探索看看吧。",
    "steps": [{"index": 0, "goalDescription1": "环顾4层"}]
  },
  {
    "key": "Q4003",
    "title": "环顾4层 2",
    "description": "从雷诺阿鞋履馆员工单脚处获悉，有一柄能够剪碎任何布料的特制宝剑。继续环顾4层，寻找线索吧。",
    "steps": [
      {"index": 0, "goalDescription1": "结束与单脚的对话"},
      {"index": 1, "goalDescription1": "环顾4层", "goalDescription2": "与驼背照明对话"}
    ]
  },
  {
    "key": "Q4004",
    "title": "会见家具馆的主人",
    "description": "来到了名为家具馆的地方。驼背照明说想要找到适合自己的新衣服，就必须去见家具馆的主人。前去拜访吧。",
    "steps": [{"index": 0, "goalDescription1": "与家具馆主人搭话"}]
  },
  {
    "key": "Q4005",
    "title": "给驼背照明送去新衣服",
    "description": "家具馆的主人“幸福衣柜”默默地从自己体内取出了衣物。将这件衣服带去送给驼背照明吧。",
    "steps": [{"index": 0, "goalDescription1": "给驼背照明送去新衣服"}]
  },
  {
    "key": "Q4006",
    "title": "从幸福衣柜中取出衣服",
    "description": "目睹驼背照明穿上新衣后，其他家具们也躁动不安地吵着想要衣服。再去向幸福衣柜求取衣物吧。",
    "steps": [{"index": 0, "goalDescription1": "从幸福衣柜中取出衣服"}]
  },
  {
    "key": "Q4007",
    "title": "将衣服分发给家具们",
    "description": "从幸福衣柜中取出了好几套衣裳。现在逐一送去分发给各个家具吧。",
    "steps": [
      {
        "index": 0,
        "goalDescription1": "将衣服送给骨架",
        "goalDescription2": "将衣服送给惬意的皮革床",
        "goalDescription3": "将衣服送给剥制的皮革帘",
        "goalDescription4": "将衣服送给红坐垫圆凳",
        "goalDescription5": "将衣服送给皮肤沙发",
        "goalDescription6": "将衣服送给双子灯"
      }
    ]
  },
  {
    "key": "Q4008",
    "title": "返回幸福衣柜身边",
    "description": "已经把衣服全部送给了其他家具。现在再次返回幸福衣柜处确认情况吧。",
    "steps": [
      {"index": 0, "goalDescription1": "返回幸福衣柜身边"},
      {"index": 1, "goalDescription1": "目睹家具们的暴动袭击"}
    ]
  },
  {
    "key": "Q4013",
    "title": "与驼背照明搭话",
    "description": "连心脏都被扯出的幸福衣柜再无一丝动静。家具们四散奔逃，只余下驼背照明还留在原地。前去搭话吧。",
    "steps": [{"index": 0, "goalDescription1": "与驼背照明搭话"}]
  },
  {
    "key": "Q4009",
    "title": "前往地下层",
    "description": "依据我们获取的配方，为了利用黄金茧纺出黄金线团，就必须前往地下获取黄金染料。前往自动扶梯向地下进发吧。",
    "steps": [
      {"index": 0, "goalDescription1": "搭乘通往下层的美食广场扶梯"},
      {"index": 1, "goalDescription1": "环顾地下1层"}
    ]
  }
]

quests_floor_b1 = [
  {
    "key": "Q-1000",
    "title": "A1 : 前往地下1层",
    "description": "探索地下1层食品馆",
    "steps": [
      {"index": 0, "goalDescription1": "踏入地下1层食品馆"},
      {"index": 1, "goalDescription1": "食品馆进入对话"}
    ]
  },
  {
    "key": "Q-1001",
    "title": "前往地下2层",
    "description": "获得了布歇烹饪好的黄金茧。现在去寻找通往地下2层的下行通道吧。",
    "steps": [{"index": 0, "goalDescription1": "寻找前往地下2层的通路"}]
  },
  {
    "key": "Q-1002",
    "title": "寻找下行的自动扶梯",
    "description": "来到了满是停摆自动扶梯的大厅。调查这些扶梯，看看哪一部尚能运转。",
    "steps": [{"index": 0, "goalDescription1": "调查自动扶梯"}]
  },
  {
    "key": "Q-1003",
    "title": "前往美食广场",
    "description": "下到了地下1层。地下的景象与地上的优雅卖场迥然不同，到处散发着刺鼻的生肉与熟食气味。前往美食广场探查吧。",
    "steps": [{"index": 0, "goalDescription1": "前往美食广场"}]
  },
  {
    "key": "Q-1004",
    "title": "追赶副厨师长",
    "description": "遭遇了自称副厨师长的人物。那家伙声称黄金茧已被上交给了名为布歇的管事者，随即拔腿就跑。立刻追上去！",
    "steps": [{"index": 0, "goalDescription1": "追赶副厨师长"}]
  },
  {
    "key": "Q-1005",
    "title": "拜访布歇",
    "description": "从副厨师长处得知了地下1层楼层经理布歇的存在。去拜访布歇并交涉取回黄金茧吧。",
    "steps": [{"index": 0, "goalDescription1": "拜访布歇"}]
  },
  {
    "key": "Q-1006",
    "title": "取回猎物的沉思",
    "description": "为了从布歇手中换取黄金茧，必须先取回被称为“猎物的沉思”的特殊食材。前去搜寻吧。",
    "steps": [{"index": 0, "goalDescription1": "取回猎物的沉思"}]
  },
  {
    "key": "Q-1008",
    "title": "返回自动扶梯室",
    "description": "集齐了全部所需线索，返回满是扶梯的大厅。",
    "steps": [
      {"index": 0, "goalDescription1": "返回自动扶梯室"},
      {"index": 1, "goalDescription1": "自动扶梯室回归对话"}
    ]
  },
  {
    "key": "Q-1009",
    "title": "定义自动扶梯",
    "description": "依照让娜的说法，若想找到通向下方的自动扶梯，就必须对其本质赋予定义。在梯子、山丘、鞋子三者之间做出抉择吧。",
    "steps": [{"index": 0, "goalDescription1": "将自动扶梯定义为梯子、山丘、鞋子中的一种"}]
  },
  {
    "key": "Q-1010",
    "title": "启动自动扶梯",
    "description": "成功赋予概念后，自动扶梯的履带开始缓缓震颤转动。",
    "steps": [{"index": 0, "goalDescription1": "启动自动扶梯"}]
  },
  {
    "key": "Q-1011",
    "title": "搭乘自动扶梯下行",
    "description": "站上运转起来的扶梯，向更深邃的地下2层降下吧。",
    "steps": [{"index": 0, "goalDescription1": "搭乘扶梯前往地下2层"}]
  }
]

quests_floor_b2 = [
  {
    "key": "Q-2000",
    "title": "环顾地下2层",
    "description": "抵达了地下2层。空气中充斥着浓重的染料与织机机油气味。继续向前探索吧。",
    "steps": [{"index": 0, "goalDescription1": "环顾地下2层"}]
  },
  {
    "key": "Q-2001",
    "title": "前往线绞巢穴",
    "description": "降落到了地下2层。从克罗默的姐姐处打探到，名为线绞巢穴的地方隐藏着纺织的核心秘密。前往该处吧。",
    "steps": [{"index": 0, "goalDescription1": "前往位于左侧的线绞巢穴"}]
  },
  {
    "key": "Q-2002",
    "title": "走出盥洗室",
    "description": "方才虽试图前往线绞巢穴，却被正体不明的庞然怪兽狂追不舍，众人只得慌忙逃入盥洗室避难。探头向外观察动静吧。",
    "steps": [{"index": 0, "goalDescription1": "走出盥洗室"}]
  },
  {
    "key": "Q-2003",
    "title": "前往线绞巢穴 2",
    "description": "万幸那头凶煞的怪兽似乎暂时移开了视线。趁此千载难逢的空当，再度向线绞巢穴进发吧。",
    "steps": [{"index": 0, "goalDescription1": "再次前往线绞巢穴"}]
  },
  {
    "key": "Q-2004",
    "title": "与地下2层的楼层经理对话",
    "description": "终于安然抵达了线绞巢穴。前去与掌管此处的地下2层楼层经理交谈吧。",
    "steps": [{"index": 0, "goalDescription1": "与地下2层楼层经理搭话"}]
  },
  {
    "key": "Q-2005",
    "title": "前往染色室",
    "description": "楼层经理告知我们，若想纺出黄金线团，就必须先取得黄金染料。动身前往染色室吧。",
    "steps": [{"index": 0, "goalDescription1": "前往染色室"}]
  },
  {
    "key": "Q-2006",
    "title": "收集传闻/未实装",
    "description": "潜伏侧听劳作顾客们的闲聊，搜集情报传闻。",
    "steps": [
      {"index": 0, "goalDescription1": "侧听劳作顾客的交谈"},
      {"index": 1, "goalDescription1": "向劳作顾客打探情报"}
    ]
  },
  {
    "key": "Q-2007",
    "title": "寻找内基德交涉",
    "description": "若想取得黄金染料，便不得不忍受荒诞至极的排队等候。去寻找插队掮客内基德商谈交易吧。",
    "steps": [{"index": 0, "goalDescription1": "寻找内基德交涉"}]
  },
  {
    "key": "Q-2008",
    "title": "深海染料传闻收集",
    "description": "向在线绞巢穴前排长队的顾客们打探深海染料的情报。",
    "steps": [{"index": 0, "goalDescription1": "向等候中的雷诺阿打探"}]
  },
  {
    "key": "Q-2009",
    "title": "拜托调色盘能否给予无色染料",
    "description": "内基德那家伙显然不肯轻易交出黄金染料，要求以罕见的“无色染料”作为交换。前去拜托调色盘制作无色染料吧。",
    "steps": [{"index": 0, "goalDescription1": "拜托调色盘制作无色染料"}]
  },
  {
    "key": "Q-2010",
    "title": "在染色仓库引爆泪滴",
    "description": "好在调色盘答应若能凑齐基础染料，便能为我们现场调配无色染料。前去染色仓库收集黄泪、红泪与蓝泪吧。",
    "steps": [
      {
        "index": 0,
        "goalDescription1": "收集黄泪",
        "goalDescription2": "收集红泪",
        "goalDescription3": "收集蓝泪"
      },
      {"index": 1, "goalDescription1": "将染料泪滴交付给调色盘"}
    ]
  },
  {
    "key": "Q-2011",
    "title": "前往内基德处换取黄金染料",
    "description": "自调色盘处如愿取得了无色染料。折返回内基德处，将无色染料与黄金染料进行置换吧。",
    "steps": [{"index": 0, "goalDescription1": "找内基德用无色染料置换黄金染料"}]
  },
  {
    "key": "Q-2012",
    "title": "黄金染料",
    "description": "从调色盘与内基德手中拿回黄金染料。",
    "steps": [{"index": 0, "goalDescription1": "接收黄金染料"}]
  },
  {
    "key": "Q-2013",
    "title": "前往地下2层楼层经理处",
    "description": "在奥提斯的机智施压下，内基德终于老老实实交出了黄金染料。立刻将其送往楼层经理处！",
    "steps": [{"index": 0, "goalDescription1": "返回地下2层楼层经理处"}]
  },
  {
    "key": "Q-2014",
    "title": "阻挡走廊的入侵者",
    "description": "在自黄金茧纺制丝线的关键时刻，走廊深处骤然传来了怪物的咆哮声。立刻迎击挡下入侵者！",
    "steps": [{"index": 0, "goalDescription1": "击退走廊入侵者"}]
  },
  {
    "key": "Q-2015",
    "title": "领取制作完成的黄金线团",
    "description": "成功击退了凶暴的怪兽。返回地下2层楼层经理身边，接收刚刚纺织成型的黄金线团吧。",
    "steps": [{"index": 0, "goalDescription1": "向楼层经理领取黄金线团"}]
  },
  {
    "key": "Q-2016A",
    "title": "离开地下2层",
    "description": "安然得到了纺织完好的黄金线团。地下2层的使命业已圆满达成，动身准备离去吧。",
    "steps": [{"index": 0, "goalDescription1": "离开地下2层"}]
  },
  {
    "key": "Q-2017",
    "title": "前往3层",
    "description": "现在返回3层，利用黄金线团在工坊中织就出最终的黄金面料吧！",
    "steps": [{"index": 0, "goalDescription1": "搭乘通往3层的自动扶梯"}]
  }
]

quest_dict = {
  "rpg-loc-quest-floor-1.json": quests_floor_1,
  "rpg-loc-quest-floor-2.json": quests_floor_2,
  "rpg-loc-quest-floor-3.json": quests_floor_3,
  "rpg-loc-quest-floor-4.json": quests_floor_4,
  "rpg-loc-quest-floor-b1.json": quests_floor_b1,
  "rpg-loc-quest-floor-b2.json": quests_floor_b2,
}

for fname, qlist in quest_dict.items():
    target_path = os.path.join(ZH_DIR, fname)
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump({"dataList": qlist}, f, ensure_ascii=False, indent=2)
    print(f"Generated {fname} ({len(qlist)} quests)")

print("Successfully generated all 6 quest files!")
