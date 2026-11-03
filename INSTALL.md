# 在各类 AI 工具里安装这四个技能

> 配套仓库：<https://github.com/Xiangyu-Ge/sci-writing-geors>（v2.0.0）
> 更新日期：2026-11-04。各平台的菜单名称与目录会变，**以官方文档和实际界面为准**。

---

## 先说原理

一个 Skill 就是一个文件夹：里面有一份 `SKILL.md`（带 `name` / `description` 的 YAML 头），可选再带 `references/` 放详细内容。支持 [Agent Skills](https://agentskills.io) 标准的工具，启动时会扫描固定目录，把技能的名字和描述注进系统提示，模型自己去判断什么时候读正文。

所以安装方式只有两大类：

- **工具会自己扫目录** → 把文件夹放到它认的路径，重启即生效，不用每次手动喊
- **工具不扫目录** → 只能把 `SKILL.md` 的文字贴进系统提示/人设里，属于"降级使用"

本仓库的结构是标准的 `<技能名>/SKILL.md`，两类平台都能用。

---

## 一、放进技能目录，自动调用

| 工具 | 放到哪里 | 生效方式 |
|---|---|---|
| **Claude Code** | `~/.claude/skills/`（全局）或项目里 `.claude/skills/` | 自动发现，对话时按需调用 |
| **Codex CLI** | `~/.codex/skills/`（`CODEX_HOME` 可改路径） | 同上 |
| **Kimi Code CLI** | `~/.kimi/skills/`，或推荐的 `~/.config/agents/skills/` | 自动发现；也可 `/skill:<名字>` 手动调 |
| **DSH（DeepSeek Harness）** | `~/.dsh/skills/`（即 `DSH_HOME/skills/`） | 自动发现 |
| **Claude.ai 网页版** | 在设置里上传 zip | 上传后对话自动调用 |
| **WorkBuddy** | 「技能」板块上传 zip | 上传后自动配置 |
| **ChatGPT** | 用自带的 Skills 功能 | 见官方文档，入口随版本变化 |
| **Claude API** | Skills API 上传，用 `skill_id` 挂载 | 程序化调用 |

### 命令行：一次装到位

macOS / Linux / Windows 的 Git Bash 均可：

```bash
git clone https://github.com/Xiangyu-Ge/sci-writing-geors.git
cd sci-writing-geors

# Claude Code
mkdir -p ~/.claude/skills && cp -r skills/* ~/.claude/skills/

# Codex CLI
mkdir -p ~/.codex/skills && cp -r skills/* ~/.codex/skills/

# Kimi Code CLI（推荐位置）
mkdir -p ~/.config/agents/skills && cp -r skills/* ~/.config/agents/skills/

# DSH
mkdir -p ~/.dsh/skills && cp -r skills/* ~/.dsh/skills/
```

Windows PowerShell 里把 `~` 换成 `$HOME` 即可：

```powershell
git clone https://github.com/Xiangyu-Ge/sci-writing-geors.git
cd sci-writing-geors

mkdir "$HOME\.claude\skills" -Force
Copy-Item -Recurse -Force skills\* "$HOME\.claude\skills\"
```

### 一个省事的发现

**Kimi Code CLI 除了自己的目录，也会回退读取 `~/.claude/skills/` 和 `~/.codex/skills/`。**

所以把四个技能放进 `~/.claude/skills/`，**Claude Code 和 Kimi Code CLI 两个工具能同时用**。Codex CLI 不读别人的目录，它只认 `~/.codex/skills/`，要共用就做个软链接：

```bash
# macOS / Linux / Git Bash
ln -s ~/.claude/skills/sci-paper-writing ~/.codex/skills/sci-paper-writing

# Windows（命令提示符管理员或开启开发者模式）
mklink /D "%USERPROFILE%\.codex\skills\sci-paper-writing" "%USERPROFILE%\.claude\skills\sci-paper-writing"
```

（Kimi 的加载优先级：项目级 > 用户级 > 额外目录 > 内置；用户级里同名的按 `.kimi/skills` > `.claude/skills` > `.codex/skills` 取。）

### 上传 zip 的平台

`dist/` 目录里已经打好包，每个 zip 解压后就是 `<技能名>/SKILL.md` 结构，直接上传即可：

- `dist/sci-paper-writing.zip`
- `dist/geo-review-writing.zip`
- `dist/geo-reviewer-response.zip`
- `dist/geo-writing-style.zip`
- `dist/geo-writing-suite-v2.0.0.zip`（四个合一）

Claude.ai 和 WorkBuddy 都走这条路。也可以在 [Releases 页面](https://github.com/Xiangyu-Ge/sci-writing-geors/releases/tag/v2.0.0) 直接下载。

WorkBuddy 的入口：左侧边栏 **专家 · 技能 · 连接器 → 技能 → 添加技能 → 上传技能**，拖入 zip 即可，导入后系统自动配置。

---

## 二、没有技能目录的平台（降级使用）

Kimi 网页版、DeepSeek 网页版/App、ChatGPT 的普通对话、各类"上传文件问答"的产品，**没有读取本地目录的能力**，也没有技能市场。这些地方只能用下面这个通用办法。

### 做法

1. 打开 `skills/sci-paper-writing/SKILL.md`，**把全文**（约 109 行）复制出来
2. 粘进平台的自定义指令 / 人设 / 系统提示，前面加一句：

   ```
   以下是一套地理与遥感 SCI 论文写作规范。之后我请你写、改、润色论文任何部分时，
   都按这套规则执行。规则里提到的 references/xxx.md 是我会另外发你的附件。
   ```

3. `references/` 里的文件**不要一次全发**。用到哪章就发哪份，比如写讨论时只发 `06-discussion.md`。

### 这条路的局限

- 模型不会"按需翻目录"，你得自己判断该发哪份参考
- 长对话里规则容易被稀释，隔几轮重申一句
- 四个技能不要一次性全塞进去，`SKILL.md` 之间会互相干扰；一次只挂一个

### DeepSeek 的特殊情况

DeepSeek 网页/App 本身没有技能机制。但本仓库的四个技能在 **DSH（DeepSeek Harness）** 里是原生支持的，目录是 `~/.dsh/skills/`。想在 DeepSeek 生态里用出自动调用的效果，走 DSH，不要指望网页版。

---

## 三、装完怎么验证

重启工具，然后直接问：

```
你现在有哪些技能？分别什么时候用？
```

正常的话它应该能报出 `sci-paper-writing`、`geo-review-writing`、`geo-reviewer-response`、`geo-writing-style` 四个名字和各自用途。

再测一次真实调用：

```
帮我看看这段引言的问题在哪：随着遥感技术的快速发展，土壤盐渍化监测变得越来越重要……
```

如果它按引言的写法逐句点评、并提到"全球尺度收口""gap 段"这类词，说明技能确实被读到了。

---

## 四、升级与卸载

```bash
# 升级：先删旧的，再装新的
rm -rf ~/.claude/skills/sci-paper-writing
cp -r skills/* ~/.claude/skills/

# 卸载
rm -rf ~/.claude/skills/{sci-paper-writing,geo-review-writing,geo-reviewer-response,geo-writing-style}
```

**一定要先删旧目录再装。** v1 的主文件是小写的 `skill.md`，v2 是 `SKILL.md`，Windows 和 macOS 默认文件系统不区分大小写，两个文件并存会互相覆盖或造成重复加载。

WorkBuddy 里卸载走界面：「已安装」→ 选技能 →「...」→ 卸载。注意**关闭开关不等于卸载**，关闭只是暂停调用。

---

## 五、装不上的常见原因

| 现象 | 原因 |
|---|---|
| 重启后模型说没有这个技能 | 目录层级错了。必须是 `skills/<技能名>/SKILL.md`，不是 `skills/SKILL.md` |
| 技能列表里出现了但从不调用 | `description` 里没写清触发场景；四个技能都写了触发词，若被截断可检查文件是否完整 |
| 中文乱码 | 文件需存为 UTF-8，Windows 上用记事本另存时注意编码 |
| 只说"已加载"但答得不专业 | 走到「降级使用」那一档了，检查是不是把文字贴进去了而没放进技能目录 |

---

## 六、参考来源

- Agent Skills 开放标准：<https://agentskills.io>
- Kimi Code CLI 技能文档：<https://moonshotai.github.io/kimi-cli/zh/customization/skills.html>
- WorkBuddy 技能文档：<https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market>
- ChatGPT Skills 文档：<https://learn.chatgpt.com/docs/build-skills>
- Codex 技能目录约定：`~/.codex/skills/<name>/SKILL.md`
- Claude Skills 概览：<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>
