# 01 · 引言(Introduction)写作详解 · 地理/遥感版

引言决定**是否会有人继续往下读**。它从宽到窄,像倒置的漏斗,把读者从"这个地表过程/属性为什么重要"引导到"原来这篇要解决的就是这个 gap"。

地理/遥感论文的引言有一个**领域特有的漏斗形状**,务必记住:

```
全球/宏观重要性  →  区域问题与必要性  →  遥感/定量手段的适用性与局限  →  本研究的 gap + 目标
   (最宽)                                                              (最窄)
```

第三段"手段适用性"是地理/遥感引言区别于一般 STEMM 的关键——**你必须论证"为什么用遥感 / 为什么用这种反演或变化检测方法",并指出现有手段的不足,gap 才站得住**。

## 1. 引言的 4 大 Block(领域化)

```
┌─────────────────────────────────────────────────────────────┐
│  Block 1 · 建立重要性(全球→区域)                              │
│    • 该地表属性/过程为什么重要(土壤盐渍化/碳/水/退化…)         │
│    • 全球或区域尺度的背景事实(面积、人口、生态/粮食安全)        │
│    • 收敛到本研究区所在的区域问题                                │
├─────────────────────────────────────────────────────────────┤
│  Block 2 · 研究地图 + 手段适用性                                │
│    • 前人怎么做的(传统采样 vs 遥感;不同传感器/方法/指数)       │
│    • 为什么遥感/定量手段适合这个问题(覆盖广、可重复、低成本)    │
│    • 引用关键文献                                              │
├─────────────────────────────────────────────────────────────┤
│  Block 3 · 研究空白(手段或认知的不足)                          │
│    • 现有反演精度不够 / 缺多源协同 / 缺长时序 / 缺驱动归因       │
│    • 描述本文要解决的问题、动机、假说                            │
├─────────────────────────────────────────────────────────────┤
│  Block 4 · 本文做了什么                                        │
│    • 本研究的对象、数据、方法、研究区                            │
│    • 用 happy words 显式标记贡献(novel, first long-term, robust…)│
│    • 常以"目标/objectives"列点收尾                              │
└─────────────────────────────────────────────────────────────┘
```

**关键观察**:
- 几乎所有论文**第一句就在 Block 1**,且具体(不要"随着遥感技术快速发展…")
- 几乎所有引言**最后一句在 Block 4**(常是"the objectives of this study are to: (1)… (2)… (3)…")
- 地理/遥感引言里 **Block 2 必须包含"手段适用性"的论证**——否则审稿人会问"为什么不直接采样?"

## 2. 两类论文的 gap 长什么样(双分支)

| | 【定量反演】常见 gap | 【时空变化】常见 gap |
|---|---|---|
| 手段不足 | 现有反演模型精度低 / 易饱和 / 不可迁移 / 缺多源协同 | 缺长时间序列 / 中高分辨率 / 缺像元级趋势 |
| 认知不足 | 缺对某地表属性的高精度空间制图 | 知道"变了"但缺**驱动归因**(气候 vs 人类活动) |
| 典型句 | *...remains challenging due to soil moisture and surface roughness effects.* | *...the relative contributions of climate and human activities to this trend remain poorly quantified.* |

## 3. 一句一句怎么写:演示(土壤盐分反演引言,构造示例)

每句标注其功能。注意时态切换和漏斗收窄。

| 句号 | 功能(在做什么) | 例句 |
|---|---|---|
| S1 | 建立全球重要性(现在简单) | *Soil salinization is one of the most widespread forms of land degradation, affecting more than 1 billion ha of land across over 100 countries.* |
| S2 | 补充区域背景 | *In arid and semi-arid regions, secondary salinization driven by irrigation threatens agricultural productivity and food security.* |
| S3 | 收敛到研究区问题 | *The arid oases of Northwest China are particularly vulnerable, where shallow groundwater and intense evaporation promote rapid salt accumulation.* |
| S4 | 传统手段的局限 | *Conventional field surveys provide accurate point measurements but are labour-intensive and cannot capture the spatial heterogeneity of salt distribution.* |
| S5 | 引出遥感手段的适用性 | *Remote sensing offers a cost-effective alternative for mapping soil salinity over large areas with repeated coverage (refs).* |
| S6-7 | 研究地图(前人方法) | *Previous studies have related soil salinity to spectral indices and surface reflectance, and machine-learning models have further improved estimation accuracy (refs).* |
| S8 | **指出研究空白**(现在完成 + 否定) | *However, the accuracy of optical retrieval is often limited by vegetation cover and surface roughness, and few studies have integrated optical and radar data to overcome these limitations.* |
| S9 | 描述本文研究 | *To address this gap, we developed a multi-source retrieval framework combining Sentinel-2 and Sentinel-1 data for estimating topsoil salinity.* |
| S10 | 概述方法/数据 | *We coupled spectral indices, polarimetric features, and field-measured electrical conductivity using a gradient-boosting model.* |
| S11 | **贡献 + happy word + 目标** | *The objectives of this study are to: (1) develop a robust multi-source salinity retrieval model; (2) map topsoil salinity across the study area; and (3) identify the dominant spectral and radar predictors.* |

让用户对自己的目标论文做这个练习——30 分钟,效果立竿见影。

## 4. 时态选择:Block by Block

| Block | 主要时态 | 为什么 |
|---|---|---|
| Block 1 背景重要性 | **现在简单** | 公认事实(*Soil salinization affects over 1 billion ha worldwide.*) |
| Block 2 前人研究 | **过去简单** / **现在完成** | 具体研究(过去)或累积态势(现在完成:*ML models have improved...*) |
| Block 3 研究空白 | **现在完成** + 否定(*has not been...，few studies have...*) | 把空白"拉到当下" |
| Block 4 本文 | **现在简单**(*This study presents...*)或**过去简单**(*we developed...*) | 看期刊惯例 |

**时态切换是有意义的**:

> Although optical indices **have been widely used** to estimate salinity, their accuracy **remains** limited under dense vegetation, and the potential of radar–optical fusion **has not been fully explored**.

从现在完成切到现在简单再切回现在完成,暗示"radar–optical fusion"正是本文要解决的、仍悬而未决的问题。

## 5. 句间衔接的 4 种武器(领域例)

句号到下一个大写字母是"危险地带"。

**武器 1·重复(overlap)**
> ...is strongly affected by surface **roughness**. **Surface roughness** introduces backscatter variations that...

**武器 2·代词/代词短语(pro-form)**
> ...several vegetation indices have been proposed. **These indices** are sensitive to canopy structure but...
> 铁律:代词短语里的名词必须和上文一致——上文叫 *indices*,这里就用 *These indices*,不要换成 *These metrics*。

**武器 3·分号合并**
> Field sampling is accurate; however, it is impractical over large, inaccessible terrain.

**武器 4·信号词**(however, therefore, in contrast, in addition…),只在真正需要标记功能转折时用,不要每句都挂。

## 6. 4 大 Block 的领域高频表达

### Block 1 · 建立重要性(开篇,具体而非空泛)

```
is one of the most widespread/severe forms of land degradation
poses a serious threat to / threatens (food security, ecosystem...)
plays a critical/key role in the (carbon/water/energy) cycle
has profound implications for regional sustainability
is a major environmental concern in arid/semi-arid regions
affects more than X ha / X% of (land area, cropland, drylands)
is closely linked to climate change and human activities
has attracted increasing attention over the past (two) decades
```

**第一句示范**(都"具体不空泛"):
- *Soil organic carbon (SOC) is the largest terrestrial carbon pool and a key indicator of soil health.*
- *Land surface temperature (LST) is a critical variable governing surface energy and water exchange.*
- *Vegetation degradation in drylands threatens the livelihoods of millions and accelerates desertification.*
- *Soil moisture is a key state variable linking the water, energy, and carbon cycles.*

**绝不要**这样开头(中文高发):*With the rapid development of remote sensing technology, more and more scholars have paid attention to...* —— 英文读者会立即跳过。

### Block 2 · 手段适用性 + 前人研究

```
论证"为什么用遥感/定量手段"
Remote sensing provides a cost-effective and repeatable means of...
Satellite observations enable monitoring over large and inaccessible areas...
offers synoptic, multi-temporal coverage that field surveys cannot provide
allows wall-to-wall mapping at (10 m / 30 m / regional) scale

描述前人工作(动词库)
estimate / retrieve / invert / derive / map / monitor / quantify
relate X to Y / establish (empirical) relationships between
apply / develop / train / calibrate / validate (a model)
employ / adopt / integrate / combine / fuse (data sources)
demonstrate / report / propose / improve
```

**例句**:
- *Optical remote sensing **has been widely used to estimate** soil salinity through salinity indices (refs).*
- *Machine-learning algorithms **have substantially improved** the retrieval accuracy of soil properties (refs).*
- *Several studies **have employed** the Mann–Kendall test to detect vegetation trends (refs).*
- *Sentinel-1 SAR **has been shown to be sensitive to** surface soil moisture (refs).*

### Block 3 · 研究空白(分两组)

**组 A:手段/认知的不足**
```
remains challenging / limited / poorly understood / poorly quantified
is hampered by / is affected by / suffers from (saturation, mixed pixels, atmospheric effects)
relies heavily on / is restricted to (single sensor, empirical index, local calibration)
lacks (long-term, high-resolution, transferable, pixel-level) ...
few studies have (integrated / fused / quantified / attributed)
little is known about / it remains unclear whether
has not been (fully) explored / addressed / validated at regional scale
```

**组 B:研究机会(常配模态动词 may/might/could)**
```
the potential of X for Y has not been fully exploited
multi-source integration may overcome these limitations
a long-term, pixel-level analysis is needed to...
attributing the relative contributions of climate and human activities remains an open question
there is an urgent need to / it is therefore essential to
```

**例句**:
- *However, optical retrieval of salinity **is often hampered by** vegetation cover, and **few studies have integrated** radar data to address this.*
- *Most existing SOC maps **are restricted to** coarse resolution, **limiting their use** for precision management.*
- *The drivers of this greening trend **remain poorly quantified**, and **it is unclear whether** climate or human activities dominate.*
- *To date, **little attention has been paid to** the transferability of retrieval models across regions.*

### Block 4 · 本文做了什么 + Happy Words 😊

```
动词:present / develop / propose / construct / map / quantify / assess / attribute / integrate / fuse
Happy words(地理/遥感版):
  robust        high-resolution / fine-resolution     transferable
  novel         first / first long-term / first regional   operational
  accurate      multi-source / multi-sensor             scalable
  comprehensive cost-effective                          spatially explicit
  reliable      wall-to-wall                            quantitative
```

**例句**:
- *In this study, **we present a robust multi-source framework** for retrieving topsoil salinity.*
- ***To our knowledge, this is the first** pixel-level attribution of vegetation change in this basin over the past two decades.*
- *We **developed and validated** a transferable model that **outperforms** single-sensor approaches.*
- *The objectives of this study are to: (1)…; (2)…; and (3)….*

## 7. 段落长度与句长

- 引言平均段落:**150-180 词**(地理/遥感引言常 4-6 段,每段对应一个 Block 或一个子主题)
- 平均句长:**20-26 词**;超过 30 词时只有约一半读者一次能读懂
- 末段几乎都是 Block 4,常以编号目标(objectives)收尾——RSE/IJRS/Catena 非常常见,值得检查目标期刊是否采用

## 8. 常见错误与"中式英文"症状(地理/遥感)

### 症状 1:第一句太宏大
❌ *With the rapid development of satellite remote sensing in the 21st century, scholars have paid more and more attention to soil salinization.*
✅ *Soil salinization affects more than 1 billion ha worldwide and is a leading cause of cropland abandonment in arid regions.*

### 症状 2:没论证"为什么用遥感"
❌ (直接说"我们用 Sentinel-2 反演盐分",没说为什么不采样)
✅ *Field surveys cannot capture the spatial heterogeneity of salinity over large areas; remote sensing provides a repeatable, cost-effective alternative.*

### 症状 3:Block 3 没说清楚
❌ *Many studies have retrieved soil salinity. Here we also retrieve soil salinity in our area.*(读者:那为什么读你这篇?)
✅ *Many studies have retrieved salinity from optical data (refs). However, accuracy degrades under vegetation, and radar–optical fusion remains underexplored. Here, we...*

### 症状 4:把"相关"当"因果"写进引言假说
❌ *We hypothesize that precipitation decline causes vegetation degradation.*(还没归因就下因果)
✅ *We hypothesize that vegetation change in this region is jointly driven by climatic and anthropogenic factors, whose relative contributions we aim to quantify.*

### 症状 5:背景信息过载
引言不是教科书。**只写支撑论文逻辑所必需的背景**(研究区的详细地理放到 Study Area,不要堆在引言)。

### 症状 6:Block 4 没 happy words
❌ *In this paper, we did some experiments to retrieve salinity. We got some results.*
✅ *In this paper, we present a robust, transferable multi-source framework. Our model provides the first wall-to-wall salinity map of the basin at 10 m resolution.*

## 9. 写引言的实操步骤(交给用户)

1. **不要先写**。先把研究区、数据、方法、结果、讨论都有清晰草稿。
2. **拿出 4 篇目标论文**,对每篇引言标注每句的 Block(1/2/3/4),特别注意它在哪句引入"遥感手段适用性"、在哪句说 gap。
3. **算结构指标**:平均句数、Block 比例、第一句什么样、末段是否用编号 objectives。
4. **先列骨架**:
   - Block 1:全球重要性几句?怎么收敛到研究区?
   - Block 2:引哪几篇?在哪句论证"为什么用遥感/这个方法"?
   - Block 3:gap 具体是什么?(一句话总结——是精度?多源?长时序?归因?)
   - Block 4:对象/数据/方法/研究区 + objectives + happy words
5. 按骨架**逐段动笔**,每段先想第一句怎么进、末句怎么出。
6. 写完**回头对照模型**:每句对应哪个 Block?时态对不对?衔接了吗?
7. **删掉 loose sentences**:任何与功能不符、舍不得删的句子,全删。

## 10. 🍳 配方速用版 vs 🔬 反向工程版

- **🍳 配方**:照本节漏斗(全球→区域→手段适用性 + 前人→gap→本文 + objectives)四段搭好,套用 §6 表达。够投 Catena/Geoderma/JAG/IJRS 级别。
- **🔬 反向工程**:冲 RSE/ISPRS J 时,去数 4 篇该刊近作的引言:它们第一句多具体?gap 用什么句式?是否用 objectives 收尾?引用密度多少?照它的"风味"校准你的骨架。
