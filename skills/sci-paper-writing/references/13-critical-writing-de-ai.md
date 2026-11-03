# 13 · 批判性写作与去 AI 味

这一节的目标是写出准确、直接、像作者本人写的英文，而不是"骗过检测器"。使用 AI 辅助写作时，按期刊要求如实声明（见 `17-ai-collaboration.md`）。

## 1. 原则：拒绝防御性写作，做批判性写作

| | 防御性写作 | 批判性写作 |
|---|---|---|
| 动机 | 预先防备审稿人质疑 | 按证据强弱下判断 |
| 限定词 | 处处加 *may*、*to some extent*、*it should be noted that*，把结论稀释到无法证伪 | 只在证据确实不足处限定，并说明不足来自哪里（样本、尺度、方法）及其影响方向 |
| 结果陈述 | 先铺垫、先辩解，再给结果 | 直接给结果和数字 |
| 对前人和自身 | 回避比较，或泛泛说"仍有局限" | 有依据地指出前人和本研究各自的问题与边界 |
| 贡献 | 堆砌 novel、robust、comprehensive | 用可验证的事实说明贡献 |

**示范**：
> ❌ 防御性：*It should be noted that, to some extent, the proposed model may potentially provide relatively better performance in some cases.*
> ✅ 批判性：*The ensemble reduced RMSE by 18% relative to random forest, but still underestimated samples above 20 dS/m, which made up 6% of the validation set.*

核心贡献句用与证据相称的强度直接陈述；推测句才用 *may*、*suggest*。强弱要有分工，不能满篇 *may*，也不能满篇 *demonstrate*。

## 2. 去 AI 味：先改结构，再看词表

只替换几个"AI 词"不解决问题。词表最不可信，结构特征更能暴露机器写作的痕迹；真正要修的是空泛、缺证据、过度拔高。

### 2.1 结构层面的痕迹（优先检查）

| 痕迹 | 例 | 改法 |
|---|---|---|
| 拔高意义 | *plays a pivotal role in*、*underscores the importance of*、*highlights the critical need* | 说清楚具体作用和数字：*controls 40% of the variance in* |
| 段末空泛总结 | *Overall, these findings highlight the complex interplay between…* | 删掉，或换成一句有信息量的判断 |
| 三连排比 | *innovative, efficient, and scalable* | 只留有证据的那一个，并配数字 |
| "不是 X，而是 Y"反复出现 | *This is not merely a mapping exercise, but a…* | 直接陈述 Y |
| 每段用 *Moreover* / *Furthermore* / *Additionally* 开头 | | 用关键词重复和代词衔接（`12-grammar-style.md` §3）；信号词一段最多一个 |
| 空主语开头 | *It is worth noting that…*、*It is important to emphasize that…* | 删掉开头，直接说内容 |
| 破折号频繁 | 一段两三个 — | 一段最多一处，改逗号、括号或拆句 |
| 句长、段长均一 | 每段 4 句、每句 22 词 | 长短相间；转折处用短句 |
| 泛泛的归因 | *studies have shown*、*experts suggest* | 给出具体文献 |
| 讨论里的"教科书段" | 先用半段解释众所周知的概念 | 删掉，直接进入本研究的论点 |

### 2.2 词表层面（其次）

下列词在大语言模型文本中出现频率远高于人类学术写作。词本身是合法英语，问题在于滥用和空泛；能换成具体表达就换，不能换时一篇里也只用一两次。

```
delve (into)   intricate   tapestry   pivotal   underscore   showcase
landscape (比喻义)   realm   myriad   foster   testament   meticulous
seamless   leverage (动词)   crucial   notably   noteworthy   commendable
shed light on   pave the way for   a deeper understanding of   in the realm of
```

**不要误删**：

- *perhaps*、*tends to*、*may* 这类正常限定是人的写作习惯，证据不足时就该用
- 方法部分的被动语态是学术惯例，不是 AI 痕迹
- *robust* 作为统计术语（robust regression、robust to outliers）可以用；作为评价形容词（*a robust framework*）才要换

## 3. 修改方式

1. **外科式修改**：先通读，标出已经像作者本人写的句子并保留；只修有问题的句子
2. **改完不应变长**：AI 文本几乎总是偏长；去掉空话后通常会变短
3. **批注不改写**：润色他人或学生稿件时，默认原文不动，在论证不清或表达有问题的地方加批注，由作者决定怎么改（见 `17-ai-collaboration.md`）
4. **对照作者的风格档案**：有个人风格档案时，按档案里的句长、用词和"从不做的事"修改（见 geo-writing-style skill）
5. **最后通读一遍**：只问一个问题："这段话有没有哪一句换成任何一篇论文都成立？"有，就改得更具体

## 4. 中文作者需要额外注意的

| 问题 | 改法 |
|---|---|
| *With the rapid development of…* 开头 | 第一句直接上主题和数字 |
| *high accuracy* / *good performance* | 用数字：*R² = 0.81, RMSE = 2.3 dS/m* |
| 相关写成因果：*Precipitation decline caused degradation.* | *Degradation was associated with declining precipitation.*（有归因分析时可用 *was largely attributable to*） |
| 无主语被动：*A framework was developed.* | *We developed a framework.* |
| 术语漂移：soil salinity / salt content / salinization level 混用 | 全文一个名字 |
| 空洞修饰：*basically / very / obviously / clearly* | 删掉 |

## 5. 改写示范（构造示例）

**原文**（典型 AI 风格）：
> *Soil salinization plays a pivotal role in shaping the agricultural landscape of arid regions. Moreover, it poses significant challenges to sustainable development. In this context, remote sensing has emerged as a powerful tool, offering unprecedented opportunities to monitor salinity dynamics. Overall, these advances underscore the critical need for robust and scalable approaches.*

**修改后**：
> *More than 424 million ha of topsoil worldwide are salt-affected (FAO, 2021), and in the oases of Northwest China secondary salinization has reduced cotton yields by up to 30% (refs). Remote sensing can map salinity across entire oases, but optical indices saturate in heavily salinized soils (refs).*

改了什么：删掉 pivotal、landscape、Moreover、powerful tool、unprecedented、underscore、robust and scalable；用两个具体数字代替"意义重大"；把"需要好方法"换成具体的技术问题（饱和）。（示例中"up to 30%"为构造值，写作时用真实文献数据。）

## 来源

- Wikipedia: Signs of AI writing（WikiProject AI Cleanup）
- blader/humanizer；hardikpandya/stop-slop；tae898/academic-de-llm；jalaalrd/anti-ai-slop-writing（GitHub，2026 年 9 月）
- Capital & Compute (2026). Stop Slop vs Humanizer: Which Claude Skill to Install
- Goldsmith-Pinkham, P. (2026). Writing & Thinking with AI Assistance
