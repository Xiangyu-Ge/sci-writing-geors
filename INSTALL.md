# 在各类 AI 工具里安装这四个技能

> 配套仓库：<https://github.com/Xiangyu-Ge/sci-writing-geors>（v2.0.0）
> 更新日期：2026-11-04。各平台的菜单名称、可用套餐和目录会变，**以官方文档和实际界面为准**。

---

## 先说原理

一个 Skill 就是一个文件夹：里面有一份 `SKILL.md`（带 `name` / `description` 的 YAML 头），可选再带 `references/` 放详细内容。支持 [Agent Skills](https://agentskills.io) 标准的工具，启动时扫描固定目录，把技能的名字和描述注进上下文，模型自己判断什么时候读正文。

本仓库的结构就是标准的 `<技能名>/SKILL.md`，所以同一份文件能装进下面几乎所有工具。

---

## 懒人版：把这段发给 AI，让它自己装

不想按平台一个个查步骤，就把下面整段复制给任何一个支持技能的 AI。它读得懂仓库，也知道自己的安装入口在哪。

```text
请帮我在当前工具里安装一个现成的 Agent Skill（技能包）。

【来源】下面两样,你给我哪个就用哪个：
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

装完用一句话验证：

```
你现在有哪些技能？分别什么时候用？
```

能报出四个名字就算成了。报不出来，多半是它只"读了一遍"却没真正建成技能——这种降级状态也能用，但不会自动触发。

> 各平台的前置条件还是要留个心：ChatGPT 的技能目前面向 Business / Enterprise / Healthcare / Edu 等套餐；Kimi 要用 Agent 模式；Codex 可以直接说"用 `$skill-installer` 从这个仓库安装"。

---

## 一、能直接吃技能包的工具

| 工具 | 放哪里 | 怎么调用 |
|---|---|---|
| **Claude Code** | `~/.claude/skills/`（全局）或项目里 `.claude/skills/` | 自动发现 |
| **Codex CLI** | `~/.agents/skills/`（用户级）或仓库里 `.agents/skills/` | 自动发现；`$技能名` 显式调用；`/skills` 查看 |
| **Kimi Code CLI** | `~/.config/agents/skills/`（推荐）或 `~/.kimi/skills/` | 自动发现；`/skill:<名字>` 调用 |
| **DSH（DeepSeek Harness）** | `~/.dsh/skills/`（即 `DSH_HOME/skills/`） | 自动发现 |
| **Claude.ai 网页 / App** | 设置里上传 zip | 对话时自动调用 |
| **ChatGPT** | Plugins → Skills → Create → Upload from your computer | 对话时自动调用 |
| **WorkBuddy** | 「技能」板块上传 zip | 上传后自动配置 |
| **Claude / OpenAI API** | Skills API 上传，用 `skill_id` 挂载 | 程序化调用 |

### 命令行：一次装到位

macOS / Linux / Windows 的 Git Bash 均可：

```bash
git clone https://github.com/Xiangyu-Ge/sci-writing-geors.git
cd sci-writing-geors

mkdir -p ~/.claude/skills        && cp -r skills/* ~/.claude/skills/          # Claude Code
mkdir -p ~/.agents/skills        && cp -r skills/* ~/.agents/skills/          # Codex
mkdir -p ~/.config/agents/skills && cp -r skills/* ~/.config/agents/skills/   # Kimi Code
mkdir -p ~/.dsh/skills           && cp -r skills/* ~/.dsh/skills/             # DSH
```

Windows PowerShell 里把 `~` 换成 `$HOME`、`cp -r` 换成 `Copy-Item -Recurse`：

```powershell
git clone https://github.com/Xiangyu-Ge/sci-writing-geors.git
cd sci-writing-geors

mkdir "$HOME\.claude\skills" -Force
Copy-Item -Recurse -Force skills\* "$HOME\.claude\skills\"
```

### 各平台的细节

**Codex CLI** 除了手动放目录，还带一个安装器，可以直接从仓库装：

```text
$skill-installer install a skill from github.com/Xiangyu-Ge/sci-writing-geors
```

装完用 `/skills` 或输入 `$` 会弹出技能选择器，确认能按名字看到；调用时写 `$sci-paper-writing`。想临时关掉某个技能，在 `~/.codex/config.toml` 里加一条：

```toml
[[skills.config]]
path = "/Users/you/.agents/skills/sci-paper-writing/SKILL.md"
enabled = false
```

> 早期版本和部分社区文档把用户级目录写作 `~/.codex/skills/`，Kimi 也会去读它。如果你的 Codex 没识别 `~/.agents/skills/`，再把目录复制一份到 `~/.codex/skills/`。

**Kimi Code CLI** 的发现顺序是：项目级 > 用户级 > 额外目录 > 内置；用户级里同名的按 `.kimi/skills` > `.claude/skills` > `.codex/skills` 取。**它也会回退读 `~/.claude/skills/`**，所以放进这一个目录，Claude Code 和 Kimi 能同时用。另可用 `--skills-dir` 指定额外目录。

**ChatGPT** 的技能入口在侧边栏：

1. 点侧边栏 **Plugins**
2. 进 **Plugin Directory**，切到 **Skills** 标签
3. 点 **Create** → **Upload from your computer**，选 `dist/` 里的 zip
4. 上传后会先扫一遍；多数立即可用，个别会标 **Needs Review**（需要你再看一眼）或 **Blocked**（不可用）

> ⚠️ ChatGPT 的技能目前面向 **Business / Enterprise / Healthcare / Edu** 等符合条件的套餐，并受工作区设置控制；个人版不一定能看到入口。技能还不会在 ChatGPT、Codex、API 之间同步。

**WorkBuddy** 的入口：左侧边栏 **专家 · 技能 · 连接器 → 技能 → 添加技能 → 上传技能**，拖入 zip，导入后自动配置。

### 上传 zip 的平台

`dist/` 里已经打好包，每个 zip 解压后就是 `<技能名>/SKILL.md` 结构：

- `dist/sci-paper-writing.zip`
- `dist/geo-review-writing.zip`
- `dist/geo-reviewer-response.zip`
- `dist/geo-writing-style.zip`
- `dist/geo-writing-suite-v2.0.0.zip`（四个合一）

也可以从 [Releases 页面](https://github.com/Xiangyu-Ge/sci-writing-geors/releases/tag/v2.0.0) 直接下载。

---

## 二、Kimi 网页版 / App：用 Agent 模式创建技能

Kimi 的网页版和 App 有技能机制，但**它不收 `SKILL.md` 压缩包**，自定义技能要靠下面两条路建出来。

### 做法 A：让 `/skill-creator` 帮你建（推荐）

1. 进入 **Agent 模式**
2. 输入 `/skill-creator`，然后把它需要的信息一次给全：

   ```
   帮我创建一个技能，名字叫 sci-paper-writing。
   下面是它的 SKILL.md 全文，请原样作为技能说明：

   （粘贴 skills/sci-paper-writing/SKILL.md 的全部内容）
   ```

3. 按它的追问确认，生成后保存

### 做法 B：文档转技能

把 `SKILL.md` 转成 `.docx`（用 Word 打开另存即可），然后在**技能**面板选「将 Office 文档转为技能」，上传后填一句描述，比如"按这份规范帮我写、改、润色地理与遥感 SCI 论文的任何部分"。

> 文档转技能每次最多 3 个文件、每个不超过 100 MB，支持 `docx` / `xlsx` / `pdf` / `pptx` 和截图。

### 调用

- 输入框中打 `/` 打开技能列表，点选即可
- 点输入框旁的 **➕** 菜单选技能
- 或者直接描述需求，Kimi 按技能描述自己判断

管理在**技能**面板的「自定义技能」标签页里，可以编辑、更新、删除。

`references/` 里那 19 份文件不用都塞进技能，它们本来就是"用到再读"的；真需要时在对话里直接发那一份。

---

## 三、没有技能机制的平台

DeepSeek 网页版 / App 本身没有技能机制，只能降级使用：

1. 打开 `skills/sci-paper-writing/SKILL.md`，把全文复制出来
2. 粘进自定义指令 / 人设，前面加一句：

   ```
   以下是一套地理与遥感 SCI 论文写作规范。之后我请你写、改、润色论文任何部分时，
   都按这套规则执行。规则里提到的 references/xxx.md 是我会另外发你的附件。
   ```

3. `references/` 用到哪章发哪份，不要一次全发

**这条路的局限**：模型不会"按需翻目录"，得你自己判断该发哪份；长对话里规则容易被稀释；四个 `SKILL.md` 不要一次性全塞进去，会互相干扰。

> DeepSeek 生态里想要自动调用，用 **DSH**（目录 `~/.dsh/skills/`），不要指望网页版。

---

## 四、装完怎么验证

重启工具后，直接问：

```
你现在有哪些技能？分别什么时候用？
```

正常应该能报出 `sci-paper-writing`、`geo-review-writing`、`geo-reviewer-response`、`geo-writing-style` 四个名字和各自用途。

再测一次真实调用：

```
帮我看看这段引言的问题在哪：随着遥感技术的快速发展，土壤盐渍化监测变得越来越重要……
```

如果它按引言的写法逐句点评，并提到"全球尺度收口""gap 段"这类词，说明技能确实被读到了。

各工具的检查方式：

| 工具 | 检查方式 |
|---|---|
| Claude Code / Codex | 直接问，或用 Codex 的 `/skills` |
| Kimi Code CLI | `/skill:<名字>` 看是否命中 |
| Kimi 网页版 | 输入框打 `/` 看列表 |
| ChatGPT | 侧边栏 Plugins → Skills 看「Installed」 |
| WorkBuddy | 「技能」→「已安装」 |

---

## 五、升级与卸载

```bash
# 升级：先删旧的，再装新的
rm -rf ~/.claude/skills/sci-paper-writing
cp -r skills/* ~/.claude/skills/

# 卸载
rm -rf ~/.claude/skills/{sci-paper-writing,geo-review-writing,geo-reviewer-response,geo-writing-style}
```

**一定要先删旧目录再装。** v1 的主文件是小写的 `skill.md`，v2 是 `SKILL.md`，Windows 和 macOS 默认文件系统不区分大小写，两个文件并存会互相覆盖或造成重复加载。

界面式平台：

- **ChatGPT**：Plugins → Skills，在技能上点 ••• 管理或删除
- **WorkBuddy**：「已安装」→ 选技能 →「...」→ 卸载。注意**关闭开关不等于卸载**
- **Kimi 网页版**：技能面板 → 自定义技能 → 删除

---

## 六、装不上的常见原因

| 现象 | 原因 |
|---|---|
| 重启后模型说没有这个技能 | 目录层级错了。必须是 `skills/<技能名>/SKILL.md`，不是 `skills/SKILL.md` |
| ChatGPT 里找不到 Skills 入口 | 套餐或工作区设置不满足，见上面的说明 |
| ChatGPT 上传后标 Needs Review / Blocked | 平台扫描结果；Needs Review 需你确认后才能用 |
| Kimi 网页版里没有"上传技能包" | 它只支持 `/skill-creator` 或文档转技能，见第二节 |
| 中文乱码 | 文件需存为 UTF-8 |
| 只说"已加载"但答得不专业 | 可能走了降级路径，检查是不是把文字贴在对话里而没真正装成技能 |

---

## 七、参考来源

- Agent Skills 开放标准：<https://agentskills.io>
- ChatGPT 技能（官方帮助中心）：<https://help.openai.com/en/articles/20001066-skills-in-chatgpt>
- ChatGPT / Codex 技能构建文档：<https://learn.chatgpt.com/docs/build-skills>
- Kimi 技能与 Agent 模式：<https://www.kimi.ai/zh-hans/help/plugins-and-skills/use-skills-in-agent>
- Kimi Code CLI 技能目录与优先级：<https://moonshotai.github.io/kimi-cli/zh/customization/skills.html>
- WorkBuddy 技能文档：<https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market>
- Claude Skills 概览：<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>
