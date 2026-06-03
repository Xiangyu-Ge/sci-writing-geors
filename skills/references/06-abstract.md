# 06 · 摘要(Abstract)写作详解 · 地理/遥感版

摘要是**整篇论文里被读得最多的部分**。决定文章会不会被检索到、被引用、被注意。一个好摘要提升能见度,差摘要会让好工作被埋没。

## 1. 🍳 配方:地理/遥感摘要的 5 要素

这是给本领域两类论文的强默认结构。**按这 5 步,各占指定句数**:

```
[1] 背景:1 句讲清楚本属性/过程为什么重要(全球或区域尺度)
[2] gap/科学问题:1 句点明现有手段或认知的不足、本文要回答什么
[3] 方法:2-3 句讲清楚研究区、数据、核心方法
[4] 结果:核心结果 + 关键数字(反演:R²/RMSE;变化:趋势/速率/归因比例)
[5] 结论与意义:take-home + 应用/影响
```

> 总字数通常 150-250 词。背景+gap 控制在 ≤ 30%,核心在中后段。

## 2. 5 要素映射到通用 3-Block
```
Block 1 设置场景 = [1]背景 + [2]gap + (本文做什么)
Block 2 内容     = [3]方法 + [4]结果(+😊)
Block 3 收尾     = [5]含义/贡献/应用(+😊)
```
😊 = happy word 出现位置(robust, high-resolution, first long-term, transferable...);摘要里密度高于正文,合规且必要。

## 3. 核心要求
| 要求 | 详情 |
|---|---|
| 独立成立 | 摘要可能是读者唯一会看的部分,不能假设看了正文 |
| 极度清晰 | 任何模糊都会被略过 |
| 字数 | 通常 150-250 词,一段(查目标期刊) |
| 写作时机 | **最后写**,等正文定稿 |
| 核心信息 | 1-2 个关键贡献 + 关键结果 + 关键含义,不面面俱到 |

## 4. 时态
| 内容 | 时态 |
|---|---|
| 论文做了什么 | 现在简单(*We present... / This study develops...*) |
| 方法 | 过去简单(*Field samples were collected... We trained...*) |
| 结果 | 过去简单或现在简单(摘要里现在简单更显权威,但要能分辨"是你做的") |
| 含义/应用 | 现在简单+模态(*This could support...*) |
| 贡献 | 现在完成/现在简单(*We have produced... / provides...*) |

> 中文用户高发:"结果表明…"译成现在简单,读者分不清是常识还是你的发现。用 *In this study / Here / We* 或过去简单明确主权。

## 5. 完整摘要示范(标注 5 要素)

### 例 1·定量反演(构造示例,~190 词)
> **[1 背景]** *Soil salinization is a major form of land degradation in arid regions, threatening agricultural productivity and food security.*
> **[2 gap]** *However, optical remote sensing of soil salinity is often limited by vegetation cover and surface roughness, and the integration of radar data to overcome these limitations remains underexplored.*
> **[3 方法]** *Here, **we developed a multi-source retrieval framework** that combines Sentinel-2 spectral indices, Sentinel-1 polarimetric features, and terrain covariates with field-measured electrical conductivity. A random-forest model was trained on 120 topsoil samples and applied to produce a wall-to-wall salinity map of an arid oasis in Northwest China.*
> **[4 结果]** *The multi-source model achieved an R² of 0.81 and an RMSE of 2.3 dS/m, **substantially outperforming** the optical-only model (R² = 0.64); radar backscatter was identified as a key predictor. Severely salinized soils accounted for 18% of the area, concentrated along low-lying oasis margins.*
> **[5 结论/意义]** *These results demonstrate that radar–optical fusion offers a **robust and operational** basis for mapping soil salinity in vegetated drylands, **with direct implications for** precision reclamation and salinization monitoring.*

### 例 2·时空变化(构造示例,~185 词)
> **[1 背景]** *Vegetation dynamics in arid oases are sensitive to both climate change and intensifying human activities.*
> **[2 gap]** *Yet the relative contributions of these drivers to recent vegetation change, and their spatial patterns, remain poorly quantified at the pixel level.*
> **[3 方法]** *Using annual maximum NDVI from MODIS and Landsat over 2000–2022, **we quantified** per-pixel trends with the Theil–Sen slope and the Mann–Kendall test, and **separated** the contributions of climate and human activities using residual trend analysis.*
> **[4 结果]** *Significant greening occurred across **63%** of the basin, concentrated within the irrigated oasis, whereas browning was confined to the desert–oasis ecotone (9%). Human activities and climate contributed **71%** and **29%** to the greening, respectively.*
> **[5 结论/意义]** *Our findings reveal a **spatially decoupled, human-driven** greening superimposed on background climatic stress, **highlighting** the dominant role of irrigation expansion and **informing** sustainable land and water management in arid oases.*

## 6. 摘要高频句式(按 5 要素)
```
[1] 背景(1 句,具体)
X is a major/widespread/critical (form of land degradation / driver of...)
X plays a key role in the (carbon/water/energy) cycle / regional sustainability
X is sensitive to both climate change and human activities

[2] gap(1 句)
However, X remains challenging because... / is limited by (vegetation, clouds, mixed pixels)
Yet the (drivers / accuracy / long-term pattern) of X remains poorly quantified
The integration of X and Y to overcome this remains underexplored

[3] 方法(2-3 句)
Here, we developed/present/applied... / Using (sensor + period), we quantified...
We combined / fused / integrated (data) ... and trained/calibrated a (model)
We separated the contributions of... using (method)

[4] 结果
The model achieved an R² of X and an RMSE of Y, outperforming...
X exhibited a significant (increasing/decreasing) trend (slope = X, p < 0.05)
X% of the area showed significant (greening/salinization); A and B contributed X% and Y%

[5] 含义
These results demonstrate/suggest that... offers a robust/operational basis for...
with direct implications for (monitoring, management, policy)
Our approach could be applied to / paves the way for...
```

## 7. "前 30 词"原则
摘要前 30 词内,读者要能判断这篇值不值得读。第一句不能浪费:
❌ *With the rapid development of remote sensing, more and more attention has been paid to soil salinization.*
✅ *Soil salinization affects over 1 billion ha worldwide and is a leading cause of cropland loss in arid regions.*

## 8. 特殊问题
- **能否引文献?** 通常不引。除非直接延伸/反驳某一前作,可引 1 次。
- **缩写?** 首次全称+缩写(*soil organic carbon (SOC)*);新缩写 ≤ 3 个;国际通用(NDVI, LST, SAR, DEM, RMSE)可不展开。
- **数字?** 关键数字放(R²、RMSE、趋势斜率、面积百分比、贡献率),服务"价值判断";不要堆细节。
- **we 还是被动?** 都行,看期刊;混用:主动表贡献,被动表标准操作。
- **公式/图?** 不能,摘要是纯文本。

## 9. Highlights / Graphical Abstract(地理/遥感几乎必备)
RSE/ISPRS J/Catena/Geoderma 等 Elsevier 刊要 **Highlights(3-5 条,每条 ≤ 85 字符)** 和 **Graphical Abstract**。
Highlights 示例:
- *A multi-source framework integrates Sentinel-1 and Sentinel-2 for salinity retrieval.*
- *Radar–optical fusion improves accuracy (R² = 0.81) over optical-only models.*
- *Human activities drove 71% of the 2000–2022 greening in the oasis.*

## 10. 实操写作清单
- [ ] 字数在目标期刊范围内?
- [ ] **5 要素齐全**(背景/gap/方法/结果/意义)且背景+gap ≤ 30%?
- [ ] **第一句**传递具体信息(不空泛)?
- [ ] 反演:R²/RMSE 在?变化:趋势/速率/归因比例在?
- [ ] 时态让读者分辨"你做的"还是"常识"?
- [ ] happy words 2-4 个标记贡献?
- [ ] 新缩写 ≤ 3,首次全称?
- [ ] 关键数字 2-4 个,服务价值判断?
- [ ] 几乎不引文献?无图表公式?
- [ ] **独立成立**?关键术语**前后一致**(不混搭近义词)?
- [ ] 平均句长 < 25 词?最后一句有 take-home/应用?
- [ ] (Elsevier 刊)Highlights 和 Graphical Abstract 准备了?

## 11. 常见错误
- **覆盖所有结果**:只突出 1-2 个最关键的,其余留正文。
- **背景太长**:背景+gap ≤ 30%,核心在中后段。
- **含义缺席**:写到结果就停 → 读者"so what?";至少一句"意味着什么/能做什么"。
- **套话开头**:直接讲具体的事。
- **贡献藏深处**:用 *To our knowledge, this is the first... / We provide quantitative evidence that...* 显式标记。
- **近义词替换关键术语**:*soil salinity* 别一会儿 *salt content* 一会儿 *salinization level*。

## 12. 摘要"金字塔"——只保留三句话
1. **本文做了什么(贡献 + happy words)**
2. **核心结果(数字/评价)**
3. **意味着什么 / 能用来做什么**
让用户先写 50 词"超简摘要"(只这三句),再扩到目标字数,保证核心不被稀释。

## 13. 🍳 配方速用版 vs 🔬 反向工程版
- **🍳 配方**:5 要素直接套,按反演/变化分支用 §5 示范。够投 Catena/Geoderma/JAG/IJRS。
- **🔬 反向工程**:冲 RSE/ISPRS J 时,数 4 篇近作摘要:第一句多具体?方法占几句?报哪几个精度指标?最后一句怎么收?Highlights 怎么写?照它校准。
