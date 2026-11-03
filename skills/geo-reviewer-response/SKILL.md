---
name: geo-reviewer-response
description: 处理 SCI 论文的审稿意见并撰写回复信（Response to Reviewers）与修回材料，面向地理学、遥感、土壤、生态方向。用于把审稿意见拆成可执行的修改任务、分类排序、识别审稿人之间的冲突、起草逐条回复（同意、补充分析、礼貌反驳、无法满足）、标注页码行号、准备修回 cover letter 与修回材料清单。用户提到审稿意见、返修、major/minor revision、response letter、rebuttal、怎么回复审稿人、审稿人不同意、补实验做不到、reject and resubmit 时使用。
---

# 审稿意见回复

课程讲义中的话术模板与避坑清单见 `references/handout-response.md`，可直接套用的英文句式见 `references/templates.md`。

## 1. 回复原则

- **逐条回复**，不遗漏任何一条，哪怕只是拼写意见；每条给出修改处的**页码和行号**
- **语气建设性**；对建设性强、很重要的问题，先表示感谢。全文开头致谢一次即可，不要每条都道歉
- **同意的意见**：明确表示接受，说明改了什么、改在哪里
- **不同意的意见**：不直接反对，而是陈述事实、给出论据进行解释，尤其要**引用文献支持**；同时修改正文措辞，避免其他读者产生同样的误解
- **做不到的补充实验或数据**：用文献解释原因，提供替代证据，并在局限部分写明
- **越尖锐的意见越要正面、详细地回应**
- 编辑提出的意见通常意味着重大问题，原则上照办

## 2. 工作流程

### 第一步：冷却并通读

收到意见后先放一两天。动笔前把所有审稿人的意见通读一遍：不同审稿人的意见可能互相牵连，边读边改会造成前后矛盾。

### 第二步：拆成任务并分类

把每条意见编号（R1.1、R1.2、R2.1……），每条拆成一个或多个独立任务，再分类：

| 类别 | 例 | 处理 |
|---|---|---|
| 编辑类 | 拼写、格式、图表标注 | 先清掉，攒"配合度" |
| 澄清类 | 方法没写清、术语不一致 | 改写原文，回复中引用改后的句子 |
| 论证类 | 补讨论、补文献、改结论强度 | 重写相关段落 |
| 分析类 | 补实验、补对比、补不确定性 | 评估可行性，排进计划 |
| 分歧类 | 审稿人误解或方法学争议 | 准备事实与文献，礼貌反驳 |

### 第三步：理清依赖与冲突

- **依赖**：哪些修改必须先做（例如重跑模型会改变结果表，结果表又影响讨论和摘要）。先做上游任务，再做下游任务
- **审稿人之间的冲突**：一位要求删、另一位要求加时，给编辑写一段说明，陈述两种意见、你的权衡与选择，并对未采纳的一方给出文献依据
- **连带影响**：每个改动会影响哪些图表、数字、段落；摘要、结论、Highlights 中的数字要同步更新

输出一张修改计划表：编号 | 意见摘要 | 类别 | 依赖 | 涉及位置 | 状态。

### 第四步：逐条起草回复

每条按固定格式：

```
Comment R1.3: [审稿意见原文]

Response: [致谢（重要意见时）] + [同意/解释] + [做了什么修改] + [修改位置]

Revised text (Page X, Lines Y–Z): "[修改后的原文]"
```

每条回复一般 150–250 词，复杂问题可以更长；不要写成小论文。

### 第五步：核对修回材料

- 回复信、标记版手稿、干净版手稿三者的页码行号一致
- 新增图表注明 *new Figure X*；新增文字注明 *newly added text*
- 修回四件套：Response Letter + 标记版手稿 + 干净版手稿 + 新增图表文件；修回 cover letter 简述主要改动

## 3. 四类情形的写法

**同意并已修改**：
> *We thank the reviewer for this important suggestion. We have added an independent validation using 40 samples collected in 2023, and the results are presented in new Table 4 and discussed on Page 14, Lines 285–302.*

**礼貌反驳（引用文献）**：
> *We understand the reviewer's concern about using a random split rather than spatial cross-validation. Our samples were collected with a stratified random design, and for probability samples a random split gives approximately unbiased estimates of map accuracy, whereas spatial cross-validation can be overly pessimistic (Wadoux et al., 2021). To address the concern, we have added a sensitivity analysis that holds out one sub-region at a time (new Table S3), and we have clarified the sampling design in Section 2.3 (Page 6, Lines 118–125).*

**无法满足（用文献解释）**：
> *We agree that soil profiles below 1 m would strengthen the analysis. However, deep sampling was not feasible across the study period, and previous work in similar oases has shown that salt accumulation is concentrated in the top 30 cm (refs). We have stated this limitation in Section 5.3 (Page 18, Lines 352–360).*

**审稿人误读**：先假设是原文没写清楚。重写原文对应段落，回复中说明改动，不指责审稿人。

更多句式见 `references/templates.md`。

## 4. 本 skill 的边界

- 回复中引用的文献必须真实存在且内容相符；本 skill 不编造文献、数据和分析结果，缺少的信息标注 `[需补充：…]`
- 补充分析的结果来自用户；未完成的分析不写成已完成
- 涉及方法学争议（如空间交叉验证、SHAP 的因果解释）时，可参考 sci-paper-writing skill 的 `04-validation-uncertainty.md`

## 5. 自查清单

- [ ] 每条意见都有回复，编号与审稿意见一致
- [ ] 每条修改都有页码和行号，三份文件版本一致
- [ ] 重要意见有致谢，全文没有满篇道歉
- [ ] 不同意的意见都有事实和文献支撑，并修改了原文表述
- [ ] 做不到的部分用文献解释，并写进局限
- [ ] 审稿人之间的冲突已向编辑说明
- [ ] 摘要、结论、Highlights 中的数字已随修改同步更新
- [ ] 修回四件套齐全
