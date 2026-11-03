# 安装这四个技能

> 仓库：<https://github.com/Xiangyu-Ge/sci-writing-geors>（v2.0.0）

四个技能都遵循 [Agent Skills](https://agentskills.io) 标准：每个目录下有一份 `SKILL.md`（含 `name` / `description` 头），`references/` 放详细参考。凡是支持这个标准的工具都能装。

---

## 一、万能安装提示词

把下面整段发给任意 AI 工具——Claude、ChatGPT、Codex、Kimi、WorkBuddy、DSH 都行。它会读仓库或你上传的 zip，用平台自己的技能功能装好。

```text
请帮我在当前工具里安装一个现成的 Agent Skill（技能包）。

【来源】下面两样，你给我哪个就用哪个：
· 我上传的 zip 附件
· GitHub 仓库：https://github.com/Xiangyu-Ge/sci-writing-geors

【要求】
1. 先读内容，确认每个技能目录下有 SKILL.md，且 YAML 头部含 name 和 description。
2. 用你平台自带的「创建技能 / 上传技能」功能，把下面四个技能分别建成独立技能，
   不要合并成一个：
   · sci-paper-writing（研究论文写作）
   · geo-review-writing（综述与 Meta 分析）
   · geo-reviewer-response（审稿意见回复）
   · geo-writing-style（个人写作风格档案）
3. name 和 description 保持原样，一个字都别改 —— description 决定这个技能会不会被
   自动触发，改写之后就失效了。
4. references/ 下的文件作为技能的支持资料一并带上；平台只收单个文件时，就以
   SKILL.md 为主说明，其余算附件。
5. 如果你的平台根本没有「技能」功能，就退一步：把 sci-paper-writing 的 SKILL.md
   全文设成我的自定义指令 / 系统提示。
6. 装完告诉我：四个技能的名字、装在哪里、怎么触发。哪一步做不到就直接说，
   不要报告成功。
```

三个前置条件别忘了：**ChatGPT** 的技能目前面向 Business / Enterprise / Healthcare / Edu 等套餐；**Kimi** 要在 Agent 模式里；**Claude.ai** 上传自定义技能需要付费套餐并开启代码执行。

---

## 二、验证

装完重启工具，问一句：

```text
你现在有哪些技能？分别什么时候用？
```

报得齐这四个才算真装上：

| 技能 | 管什么 |
|---|---|
| `sci-paper-writing` | 研究论文全流程：选题、选刊、各章节、图件、去 AI 味、cover letter |
| `geo-review-writing` | 综述与 Meta 分析：PICO、PRISMA、效应量、文献计量 |
| `geo-reviewer-response` | 审稿意见拆解与回复信 |
| `geo-writing-style` | 个人写作风格档案 |

再测一次真实调用：

```text
帮我看看这段引言的问题在哪：随着遥感技术的快速发展，土壤盐渍化监测变得越来越重要……
```

它如果按引言的写法逐句点评，并提到"全球尺度收口""gap 段"这类词，说明技能确实被读到了。

---

## 三、可能遇到的问题

| 现象 | 原因与处理 |
|---|---|
| 报不出四个技能名 | 没真正建成技能，只是把文字读了一遍。重发提示词，强调"用平台自带的技能创建功能" |
| 报得出名字，但回答很泛 | 同样属降级状态（只当提示词用）。能用，但不会自动触发 |
| ChatGPT 里找不到 Skills 入口 | 套餐或工作区设置不满足；企业/教育版管理员可能默认关闭了技能 |
| ChatGPT 上传后标 Needs Review / Blocked | 平台的扫描结果。Needs Review 需你确认后才能用，Blocked 不可用 |
| Kimi 网页版没有"上传技能包" | 它不收 zip，只能用 `/skill-creator` 对话创建，或把 `SKILL.md` 转成 `.docx` 走"文档转技能" |
| 装了但一直不生效 | 检查目录层级：必须是 `<技能名>/SKILL.md`，不能是 `skills/SKILL.md` |
| 升级后行为没变 | v1 是小写的 `skill.md`、v2 是 `SKILL.md`，Windows/macOS 不区分大小写会打架，先删旧目录再装 |
| 四个全装反而互相干扰 | 一次只挂当前需要的那个，尤其 `sci-paper-writing` 和 `geo-review-writing` 别同时塞进同一段系统提示 |
| 中文乱码 | 文件存成 UTF-8 |

---

## 参考

- Agent Skills 标准：<https://agentskills.io>
- ChatGPT 技能帮助：<https://help.openai.com/en/articles/20001066-skills-in-chatgpt>
- Kimi 技能帮助：<https://www.kimi.ai/zh-hans/help/plugins-and-skills/use-skills-in-agent>
- Kimi Code CLI 技能目录：<https://moonshotai.github.io/kimi-cli/zh/customization/skills.html>
- WorkBuddy 技能文档：<https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market>
- Claude Skills 概览：<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>
