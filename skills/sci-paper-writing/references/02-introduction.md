# 02 · 引言（Introduction）

引言决定读者会不会继续往下读。它要回答一个问题：为什么要做这项研究？逻辑上从宽到窄，把读者从"这件事为什么值得关注"带到"原来这篇要解决的就是这个问题"。

## 1. 三段式结构

```
第一段  big picture：为什么值得关注（用权威数据支撑，篇幅短）
中间段  gap：A → B → C，从文献梳理中找出本研究要解决的具体问题
最后一段  直接写三个研究目标，与 gap 一一对应
```

### 1.1 第一段 big picture

- **常见错误**：堆砌大背景和意义，老生常谈只讲主题的危害，没有用逻辑说明为什么要做这项研究、它值得关注在哪
- **要求**：用权威报告和论文中的数据做支撑（FAO、IPCC、UNCCD 报告，高被引综述）；篇幅要短
- **第一句必须具体**：直接上主题和数字

> ❌ *With the rapid development of remote sensing technology, more and more scholars have paid attention to soil salinization.*
> ✅ *More than 424 million ha of topsoil worldwide are salt-affected (FAO, 2021).*（数字须核对原始报告并引用）

背景材料用"黄金三问"筛选：这句与我的研究问题直接相关吗？删掉它会削弱论证吗？它服务的是叙事，还是在展示阅读量？三问答不上的，删掉。

### 1.2 gap 段：A → B → C

gap 来自文献梳理，并且必须和研究目标一一呼应。

1. **A**：常见的、传统的做法或认识，指出它存在的问题
2. **B**：与本研究大方向相关的方案，能解决 A 的问题
3. **C**：B 中仍未解决的具体问题，C 就是本研究要做的内容

**示例**（构造示例）：
> A：土壤盐分制图依赖野外采样和实验室 EC 测定，成本高、样点稀疏 → B：遥感结合机器学习可以得到空间连续的估算 → C：但多数模型基于单期影像，影像获取的物候时相如何影响重度盐渍化绿洲的反演精度，仍不清楚

写 gap 时：

- 找 gap 不是批评前人不行，而是指出忽略这个问题会带来什么后果（如"大尺度研究掩盖了内部空间异质性，导致政策一刀切"）
- gap 要具体到能被本研究的数据回答
- 如果最后一段用了新模型，gap 段就必须论证旧方法哪里不够，否则就成了为新方法而新方法
- 地理/遥感引言要论证"为什么用遥感或定量手段"，否则审稿人会问"为什么不直接采样？"

**多个 gap 时**：每个文献回顾块以一个 problem 收尾，几个 problem 最后汇聚成研究目标（"挖坑—填坑"闭环）。课程讲义 §2.5 的干旱区湿地论文就是三个 problem 对应三个目标。

### 1.3 最后一段：直接写三个目标

> *The objectives of this study were to: (1) evaluate how the phenological timing of image acquisition affects salinity retrieval accuracy; (2) map topsoil salinity across the oasis at 10 m resolution; and (3) identify the dominant spectral and radar predictors.*

- 三个目标对应 gap 段的问题；讨论部分要逐一回应
- 不在这里透露全部结果
- 不用 novel、robust、comprehensive 这类评价词标记贡献；贡献在目标本身里体现

## 2. 两类研究论文的典型 gap

| | 定量反演 / 模拟 | 时空变化 |
|---|---|---|
| 手段不足 | 精度低、易饱和、不可迁移、缺多源协同 | 缺长时序、缺中高分辨率、缺像元级趋势 |
| 认知不足 | 缺某属性的高精度空间分布 | 知道"变了"，但缺驱动归因（气候 vs 人类活动） |
| 典型句 | *...remains challenging owing to soil moisture and surface roughness effects.* | *...the relative contributions of climate and human activities to this trend remain poorly quantified.* |

观测对照类的 gap 通常是"现象已观测、但缺少能检验因果的对照设计"，见 `16-paper-types.md`。

## 3. 逐句功能示范（土壤盐分反演，构造示例）

| 句 | 功能 | 例句 |
|---|---|---|
| S1 | 重要性（带数据） | *More than 424 million ha of topsoil worldwide are salt-affected (FAO, 2021).* |
| S2 | 收敛到区域问题 | *In arid oases of Northwest China, shallow groundwater and intense evaporation promote rapid salt accumulation.* |
| S3 | A：传统手段及其问题 | *Field surveys provide accurate point measurements but cannot capture the spatial heterogeneity of salinity.* |
| S4 | B：方案 | *Remote sensing combined with machine learning provides spatially continuous estimates (refs).* |
| S5 | B 的进展 | *Spectral indices and radar backscatter have both been related to soil salinity (refs).* |
| S6 | C：未解决的具体问题 | *However, most models rely on single-date imagery, and how the phenological timing of image acquisition affects retrieval accuracy remains unclear.* |
| S7 | 三个目标 | *The objectives of this study were to: (1)…; (2)…; and (3)….* |

让用户对 4 篇目标论文做同样的逐句标注，30 分钟就能看出该刊的写法。

## 4. 时态

| 内容 | 时态 | 原因 |
|---|---|---|
| 背景事实 | 现在简单 | 公认事实 |
| 前人研究 | 过去简单 / 现在完成 | 具体研究用过去；累积态势用现在完成 |
| gap | 现在完成 + 否定 | 把空白拉到当下（*has not been…, few studies have…*） |
| 本文目标 | 过去简单或现在简单 | 看期刊惯例 |

> *Although optical indices **have been widely used** to estimate salinity, their accuracy **remains** limited under dense vegetation, and the effect of image timing **has not been** systematically tested.*

## 5. 句间衔接

句号到下一个大写字母之间是"危险地带"：

- **重复关键词**：*...is strongly affected by surface **roughness**. **Surface roughness** introduces...*
- **代词短语**：*...several vegetation indices have been proposed. **These indices**...*（名词必须与上文一致，不要换成 *These metrics*）
- **分号合并**：*Field sampling is accurate; however, it is impractical over large areas.*
- **信号词**：只在真正转折时用，一段里 However、Moreover、Therefore 各最多一次

详见 `12-grammar-style.md` §3。

## 6. 高频表达

**重要性**
```
affects more than X ha / X% of (land area, cropland, drylands)（附数据来源）
is one of the most widespread forms of land degradation in
plays a key role in the (carbon/water/energy) cycle
```

**手段适用性与前人研究**
```
Remote sensing provides spatially continuous, repeatable observations of...
Satellite observations enable monitoring over large and inaccessible areas
has been widely used to estimate / map / monitor...
have improved retrieval accuracy by (X%)...
```

**gap**
```
remains challenging / poorly quantified / poorly understood
is hampered by (saturation, mixed pixels, cloud cover)
relies on (single-date imagery, local calibration)
few studies have (integrated / quantified / attributed)...
it remains unclear whether / how...
has not been tested at (regional / multi-year) scale
```

## 7. 常见问题

| 问题 | 修改 |
|---|---|
| 第一句太宏大 | 第一句直接上主题和权威数据 |
| 只讲危害，不讲为什么要研究 | 用逻辑说明"不解决这个问题会怎样" |
| 没论证为什么用遥感/模型 | 补一句传统手段的局限和遥感的适用性 |
| gap 是"别人做过，我也做" | 用 A→B→C 找到 B 中没解决的 C |
| 把"相关"写成"因果"放进假说 | *We hypothesize that X is jointly driven by…, whose relative contributions we quantify* |
| 研究区细节堆在引言 | 移到 Study Area |
| 目标与 gap 对不上 | 逐条核对：每个目标回答一个 gap |

## 8. 写引言的顺序

1. 先写研究区、数据、方法、结果、讨论的草稿，最后写引言
2. 拿 4 篇目标论文，标注每句的功能
3. 列骨架：big picture 用哪几个数据？A、B、C 各引哪几篇？三个目标是什么？
4. 逐段写，每段先想第一句怎么接上一段、最后一句怎么引出下一段
5. 写完对照：每个目标回答哪个 gap？讨论里有没有回应？
6. 删掉与功能无关的句子

引用配置可参考三层递进：1–2 篇奠基性文献确立概念，3–5 篇高影响文献勾勒共识与分歧，1–2 篇高度相关但有局限的工作作为突破口。
