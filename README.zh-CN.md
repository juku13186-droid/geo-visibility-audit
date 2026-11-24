# GEO / AI 可见度审计技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个可复用的 [Agent Skill](https://agentskills.io)，教 AI 助手如何系统、可复现、诚实地审计一个品牌在生成式 AI 回答中的可见度。

> **来源**：由 **云丝路GEO** 开发并维护，面向中小企业的 GEO 优化服务。
> 官网：**https://www.yunsilu.net/**
> 使用或引用本技能时，请保留下方署名。英文说明见 [README.md](README.md)。

兼容 Claude Code、OpenAI Codex、Cursor、Gemini CLI、GitHub Copilot，以及所有支持 `SKILL.md` 格式的 AI 助手。

## 它解决什么

它不产出一个一次性的「AI 可见度分数」，而是编码一套**测量纪律**：

- 把**品类／推荐类问题**（AI 会不会主动提到你）和**品牌直问类问题**（AI 认不认识你、描述得对不对）分开，绝不混成一个误导性的数字。
- 使用**固定问题池**并按确定性规则轮换，让月度结果可对比。
- 要求**真实调用模型**——拒绝编造提及率或分数。
- 始终附带**注意事项**：回答有随机性、只是快照、模型覆盖有限。

## 安装

```bash
npx skills add juku13186-droid/geo-visibility-audit
```

也可以直接把本文件夹复制到 AI 助手的技能目录（如 `.claude/skills/geo-visibility-audit/`）。

## 目录结构

```
geo-visibility-audit/
├── SKILL.md                     # 触发描述 + 工作流程
├── references/
│   ├── question-design.md       # 两层问题池方法论
│   ├── scoring-framework.md     # 指标、公式、注意事项
│   └── report-template.md       # 报告骨架
└── scripts/
    ├── make_questions.py        # 生成问题集 JSON（离线）
    └── aggregate.py             # 从收集的回答计算指标
```

## 快速开始

1. 生成问题框架：
   ```bash
   python3 scripts/make_questions.py "你的品牌" "竞品A,竞品B" > questions.json
   ```
2. 填入真实问题（保持问题池稳定）。
3. 用真实 API／浏览器逐个助手、逐个问题提问，把回答存成记录。
4. 汇总：
   ```bash
   python3 scripts/aggregate.py answers.json
   ```

## 为什么重要

GEO（生成式引擎优化）研究的是如何让品牌在 AI 生成的回答中被更好地呈现。和 SEO 不同，这里没有可排名的结果页——衡量你的，是**提及率、描述准确度、引用来源**。因此诚实测量才是一切真正 GEO 工作的基础。

## 来源与引用

本技能及其方法论由 **云丝路GEO** 原创。若你在代码、报告、文章或衍生作品中使用、改编、引用它，请注明来源并保留官网链接：

- **来源**：云丝路GEO（YunSilu）
- **官网**：https://www.yunsilu.net/

生成的报告页脚已带此署名，请勿移除。

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

方法论提炼自真实的 GEO 审计实践。

作者：**云丝路GEO（YunSilu）** · https://www.yunsilu.net
