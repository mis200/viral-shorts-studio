# viral-shorts-studio · 爆款短视频内容工厂

把任意产品 / 品牌 / 话题，变成一套**能发、敢发、容易爆**的短视频内容包（脚本 + 标题 + 封面 + 标签 + 发布策略 + 变现路径）。专为抖音 / 快手 / 视频号 / 小红书等中文短视频平台设计。

## 为什么火 / 怎么赚钱

内容创作是 AI 应用最大赛道之一；商家和素人都在抢"爆款内容产能"。本 skill 把爆款方法论 + 平台规则 + 合规扫描打包成可复用技能，直接对接四条变现路：

- 🛒 **短视频带货**（挂车 / 橱窗，无货源也能跑）
- 💬 **私域引流**（微信 / 社群，高客单复购）
- 💰 **商单接广**（星图 / 快接单 / 蒲公英）
- 📚 **知识付费 / 课程**

## 功能

- 5 步爆款工作流（定盘 → 选题钩子 → 脚本 → 包装 → 变现）
- 5 类钩子公式 + 3 套脚本模板
- 4 大平台规则速查（快手 / 抖音 / 视频号 / 小红书）
- 违禁词扫描（合规优先，避免限流封号）
- 标题生成器脚本

## 安装

支持 Agent Skills 标准的工具（WorkBuddy / Claude Code / Cursor / Codex 等），把本目录复制到 skills 目录即可，例如：

- `~/.workbuddy/skills/viral-shorts-studio/`（WorkBuddy，用户级）
- `.claude/skills/viral-shorts-studio/`（项目级）

重启后技能即可被调用。仅 `scripts/` 下的两个 Python 脚本需要 Python3，SKILL 主体不依赖运行环境。

## 用法

直接对智能体说：

> 帮我给"柳州螺蛳粉"做一条快手带货短视频，目标挂车转化。

它会输出完整内容包（钩子 / 脚本 / 标题 A·B·C / 封面 / 标签 / 发布时间 / 变现路径 / 合规扫描）。

也可以单独用脚本：

```bash
python3 scripts/generate_titles.py "螺蛳粉"
python3 scripts/check_banned.py "这是全网最低价"
```

## 目录结构

```
viral-shorts-studio/
├── SKILL.md                 # 技能定义与工作流
├── references/
│   ├── hook-formulas.md     # 5 类钩子公式
│   ├── script-templates.md  # 3 套脚本模板
│   ├── platform-rules.md    # 平台规则速查
│   ├── money-paths.md       # 4 条变现路径
│   └── banned-words.md      # 违禁词清单
├── scripts/
│   ├── generate_titles.py   # 标题生成器
│   └── check_banned.py      # 违禁词扫描
├── README.md
└── LICENSE
```

## License

MIT
