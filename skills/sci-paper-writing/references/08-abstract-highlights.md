# 08 · 摘要、Highlights 与 Graphical Abstract

摘要是论文中被读得最多的部分，决定论文会不会被检索到、被点开、被引用。摘要最后写，等正文定稿后再写。

## 1. 句子结构

```
背景         1 句：这个属性或过程为什么重要（具体，最好带数字）
问题/空白    1 句：现有手段或认知的不足（However / Yet / Despite）
方法         2–3 句：研究区、数据、核心方法
结果         2–3 句：核心结果 + 关键数字
意义         1 句：take-home 与应用
```

总字数以目标期刊要求为准（多数 150–250 词）。结果部分必须有具体数字：反演报 R²、RMSE；变化报趋势、面积比例、归因比例；观测对照报效应大小。

## 2. 示范（构造示例）

**定量反演**：
> **[背景]** *Soil salinization threatens irrigated agriculture in arid oases.* **[空白]** *However, optical retrieval of salinity saturates in heavily salinized soils, and single machine-learning models tend to underestimate high values.* **[方法]** *We developed a stacking ensemble that combines Sentinel-1 polarimetric features, Sentinel-2 spectral indices, and terrain covariates, and validated it against 120 independent topsoil samples from an oasis in Northwest China. SHAP analysis was used to identify the predictors that contributed most at high salinity.* **[结果]** *The ensemble achieved an R² of 0.81 and an RMSE of 2.3 dS/m, 18% lower than random forest, and reduced the bias for samples above 20 dS/m from −4.1 to −1.6 dS/m. Severely salinized soils covered 18% of the oasis, mostly along low-lying margins.* **[意义]** *Radar–optical fusion extends salinity retrieval to heavily salinized soils and provides a 10 m basis for targeting reclamation.*

**时空变化**：
> **[背景]** *Vegetation in arid oases responds to both climate and irrigation.* **[空白]** *Yet the relative contributions of these drivers remain poorly quantified at the pixel level.* **[方法]** *Using annual maximum NDVI from Landsat for 2000–2022, we computed per-pixel Theil–Sen trends with Mann–Kendall tests and separated climatic and human contributions with residual trend analysis.* **[结果]** *Significant greening occurred across 63% of the basin, concentrated in the irrigated oasis, while browning affected 9%, mainly in the desert–oasis ecotone. Human activities accounted for 71% of the greening.* **[意义]** *Irrigation expansion, rather than climate, has controlled recent vegetation change, which matters for water allocation between oases and their surrounding ecotones.*

## 3. 要求

| 要求 | 说明 |
|---|---|
| 独立成立 | 读者可能只读摘要 |
| 第一句 | 前 30 词内读者就要判断值不值得读，第一句不讲"随着……发展" |
| 核心信息 | 只突出 1–2 个最关键的结果 |
| 缩写 | 首次给全称；新缩写不超过 3 个；NDVI、SAR、RMSE 等领域通用缩写可不展开 |
| 文献、图表、公式 | 不出现 |
| 主权 | 用 *We* / *Here* / *In this study* 标明是你的工作 |
| 评价词 | 不用 novel、robust、comprehensive；贡献用数字和事实表达 |

## 4. 时态

| 内容 | 时态 |
|---|---|
| 本研究做了什么 | 过去简单（*We developed…*）或现在简单（*This study presents…*） |
| 方法操作 | 过去简单 |
| 结果 | 过去简单 |
| 意义 | 现在简单 + 情态动词 |

## 5. 先写三句话版本

先写 50 词的超简摘要，只保留三句：

1. 本文做了什么（贡献）
2. 核心结果（数字）
3. 意味着什么、能用来做什么

再扩到目标字数，保证核心不被背景稀释。

## 6. 高频句式

```
空白    However, X remains challenging because... / Yet X remains poorly quantified at...
方法    Here, we developed... / Using (data, period), we quantified... / We separated... using...
结果    achieved an R² of X and an RMSE of Y, Z% lower than...
        increased significantly across X% of the area (p < 0.05)
        A and B contributed X% and Y%, respectively
意义    These results show that... / This provides a basis for...
```

## 7. Highlights

Elsevier 期刊（RSE、ISPRS J、JAG、Catena、Geoderma、Ecological Indicators 等）通常要求 3–5 条 Highlights，每条不超过 85 个字符（含空格）。

- 每条一个发现，带数字或可验证的事实
- 写发现，不写"本文做了什么研究"
- 不用 novel、robust、comprehensive

示例：
- *Radar–optical fusion reduced salinity RMSE by 18% relative to RF*
- *Human activities explained 71% of oasis greening in 2000–2022*
- *Severe salinization covered 18% of the oasis, mainly low-lying margins*

## 8. Graphical Abstract

一张图讲清"数据 → 方法 → 核心发现"。文字少、字号大、色盲友好，避免把技术路线图直接搬过来。

## 9. 自查清单

- [ ] 背景 1 句、空白 1 句、方法 2–3 句、结果 2–3 句、意义 1 句
- [ ] 第一句具体，结果有关键数字
- [ ] 能独立读懂；关键术语与正文一致
- [ ] 没有文献、图表、公式；新缩写不超过 3 个
- [ ] 没有评价形容词，贡献用数字表达
- [ ] Highlights 3–5 条，每条不超过 85 字符
