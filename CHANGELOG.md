# 更新日志

本仓库遵循 [语义化版本](https://semver.org/lang/zh-CN/)。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

---

## [2.0.0] · 2026-11-03

第二版。从"一个写作 skill"扩展为**写作 · 综述 · 审稿回复 · 风格档案**四件套。

### 新增

- **`geo-review-writing`** —— 综述与 Meta 分析写作
  - 四种综述类型的判定（一般性综述 / 系统综述 / Meta 分析 / 文献计量）
  - PICO(T) 检索式设计、多库检索与检索式记录规范
  - 筛选与证据表、PRISMA 2020 与 PRISMA-EcoEvo 流程图
  - 效应量（lnRR / Hedges' d / Fisher z / OR·RR）、随机效应与多水平模型（`metafor::rma.mv`）
  - 异质性（I²、Q）、亚组分析与 Meta 回归、敏感性与发表偏倚（漏斗图 + Egger + 失安全数）
  - 文献计量参数规范（Time Slicing、Top N）与图谱解读边界
  - `references/review-methods.md`（202 行）

- **`geo-reviewer-response`** —— 审稿意见回复
  - 意见编号（R1.1、R1.2…）与五类分类（编辑 / 澄清 / 论证 / 分析 / 分歧）
  - 修改依赖排序、审稿人之间的冲突处理、连带影响同步
  - 四类情形写法:同意并已修改、礼貌反驳（引文献）、无法满足（用文献解释）、审稿人误读
  - 固定回复格式（Comment / Response / Revised text + 页码行号）
  - 修回四件套核对:Response Letter、标记版、干净版、新增图表
  - `references/handout-response.md`（课程话术与避坑清单）、`references/templates.md`（可直接套用的英文句式）

- **`geo-writing-style`** —— 个人写作风格档案
  - 六类归纳法:句子长度、语气、用词、结构、一贯的做法、从来不做的事
  - 每条规则须配样本原句作证据，不写恭维性总结
  - 使用方式:按档案起草;润色默认**只批注、不改写**
  - 迭代机制与边界（不得与去 AI 味规则、期刊 AI 声明冲突时如何取舍）
  - `references/style-profile-template.md`

- **`dist/`** 分发目录:4 个独立 zip + 1 个四件套合集 zip
- **`VERSION`** 文件，便于脚本读取当前版本
- **引用信息**（BibTeX）与版本历史表（README）

### 变更

- **`sci-paper-writing`** 参考文件由 11 个（3339 行）扩充到 **19 个（4418 行）**:
  - 新增 `00-journal-targeting.md` 选刊与期刊定位
  - 新增 `01-research-question.md` 科学问题、创新层次与"好故事"
  - 新增 `04-validation-uncertainty.md` 精度验证、不确定性与可解释性
  - 新增 `10-figures.md` 图件与制图
  - 新增 `13-critical-writing-de-ai.md` 批判性写作与去 AI 味
  - 新增 `16-paper-types.md` 三类研究论文的写法
  - 新增 `17-ai-collaboration.md` AI 协同写作与学术诚信
  - 新增 `course-handout.md` 课程完整讲义
  - **全部 19 个文件直接取自《202610版地理学论文写作-审稿-回复skill》技能包，与源包逐字节一致**，未做改写、拼接或与 v1 合并
  - v1 的 11 个参考文件已整体删除，**不是**把旧文件改名搬进 v2。下表只是内容对应关系，方便老用户找位置:
    - `01-introduction.md` → `02-introduction.md`（重写）
    - `02-methods.md` → `03-methods.md`（重写）
    - `03-results.md` → `05-results.md`（重写）
    - `04-discussion.md` → `06-discussion.md`（重写）
    - `05-conclusion.md` → `07-conclusion.md`（重写）
    - `06-abstract.md` → `08-abstract-highlights.md`（重写，并入 Highlights 与 Graphical Abstract）
    - `07-title.md` → `09-title.md`（重写）
    - `08-vocabulary.md` → `11-vocabulary.md`（续用并微调）
    - `09-grammar-style.md` → `12-grammar-style.md`（续用并微调）
    - `10-checklist.md` → `15-checklist.md`（重写）
    - `11-cover-letter.md` → `14-cover-letter-submission.md`（重写，并入投稿材料与桌面拒稿）
  - 上表 11 组中，标「续用」的 2 篇与 v1 文本高度重合（>90%），其余 9 篇为重写（<35%）。这些重合来自 v2 技能包本身，不是本次整理引入的
  - 论文类型由两类（定量反演 / 时空变化）扩展为三类，新增**观测对照**
- **目录结构**改为 Agent Skills 标准布局:`skills/<skill-name>/SKILL.md`
  - v1 的 `skills/skill.md`（小写）与 `skills/references/` 已删除
  - 新位置为 `skills/sci-paper-writing/`，主入口 `SKILL.md` 取自 v2 技能包（重写，178 → 109 行）
- **README** 重写为四件套总览，补充协同流程图、v2 迁移说明、按 skill 的快速上手段落
- **许可说明**改为如实描述，不再引用仓库中并不存在的 `LICENSE` 文件

### 移除

- 根目录 `sci-writing-geo-rs.zip`（v1 整包，已被 `dist/` 下按 skill 拆分的 zip 取代;原始文件仍保留在 git 历史与 v1.0.0 tag 中）
- `skills/skill.md` 与 `skills/references/`（被新的 `skills/sci-paper-writing/` 取代）

### 迁移说明

从 v1 升级时，把旧的技能目录整体删掉再装 v2，避免 `skill.md` 与 `SKILL.md` 并存导致重复加载:

```bash
# Claude Code
rm -rf .claude/skills/sci-paper-writing      # 旧 v1 目录
cp -r skills/* .claude/skills/               # 装 v2 四件套
```

---

## [1.0.0] · 2026-06-03

首版。

### 新增

- **`sci-paper-writing`** —— 地理 / 遥感 SCI 中英文论文写作技能，面向两类论文:
  - 地表 / 土壤属性的遥感定量反演（土壤盐分、SOC、土壤水分、植被指数、LST）
  - 盐渍化 / 退化等地表过程的时空变化分析（趋势、变化检测、驱动因子归因）
- 11 个参考文件:
  - `01-introduction.md` 引言的地学漏斗
  - `02-methods.md` 研究区 + 数据 + 方法
  - `03-results.md` 结果 5 步配方
  - `04-discussion.md` 倒漏斗讨论 + 确定性阶梯
  - `05-conclusion.md` 结论 11 要素
  - `06-abstract.md` 摘要 5 要素
  - `07-title.md` 标题双分支骨架
  - `08-vocabulary.md` 通用 + 地学专属词库
  - `09-grammar-style.md` 时态、衔接、确定性、主被动
  - `10-checklist.md` 投稿前自查
  - `11-cover-letter.md` 投稿信
- 双分支（定量反演 / 时空变化）与双轨（配方速用版 / 反向工程版）设计
- 根目录整包 `sci-writing-geo-rs.zip`

---

[2.0.0]: https://github.com/Xiangyu-Ge/sci-writing-geors/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/Xiangyu-Ge/sci-writing-geors/releases/tag/v1.0.0
