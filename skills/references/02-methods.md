# 02 · 研究区 / 数据 / 方法(Materials and Methods)写作详解 · 地理/遥感版

地理/遥感论文的"方法"通常**拆成三块**,务必分开写好:

```
研究区 Study Area   →   数据 Data   →   方法 Methods/Algorithm
(你在哪做)            (你用什么)        (你怎么做)
```

核心使命仍是:**让别的研究者能复现你的工作**——能找到同样的区、拿到同样的数据、跑出同样的结果。

---

# 第一部分 · 研究区(Study Area)

## 1. 🍳 配方:研究区的"漏斗"逻辑

**位置 → 自然地理 → 人文 → 科学意义**,先宏观定位,再细化要素,最后**收敛到本研究关心的那个过程**。

```
[1] 地理位置:经纬度范围 + 行政/地理单元 + 总面积
[2] 自然地理:气候(类型、年均温、年降水、蒸发)、地形(高程、地貌)、水文(河流、地下水)
[3] 土壤与植被:主要土壤类型、植被类型/覆盖、土地利用
[4] 人文(可选):人口、灌溉/农业活动、人类干扰
[5] 科学意义:本区存在的环境问题(如盐渍化/退化),以及为什么适合做本研究 → 收敛到研究问题
```

> ⚠️ 不要写成"地理课本"。每一句都要**最终为本研究问题服务**。研究盐分,就突出干旱、强蒸发、浅地下水、灌溉——这些是盐渍化的成因;不研究的要素一句带过或删掉。

## 2. 研究区高频表达(领域词库)

```
位置
The study area is located in / lies in / is situated in...
covers an area of approximately X km²
extends from X°N to Y°N and from A°E to B°E
encompasses / spans the (basin, oasis, delta, plateau) of...

气候
is characterized by a (typical) arid / semi-arid / temperate continental / monsoon climate
The mean annual temperature is X °C, and the mean annual precipitation is Y mm
Potential evaporation (~X mm) far exceeds precipitation
Precipitation is concentrated in (summer) / unevenly distributed throughout the year

地形与水文
The terrain is (flat / undulating); elevation ranges from X to Y m a.s.l.
is drained by the X River / is fed by snowmelt from...
The groundwater table is shallow (typically < X m)

土壤与植被
The dominant soil types are (Solonchaks / Aridisols / loess-derived soils)
according to the (WRB / USDA / Chinese Soil Taxonomy) classification
Natural vegetation is dominated by (halophytes / desert shrubs / grassland)
Land use is mainly (irrigated cropland / grazing land)

科学意义/问题(收敛句)
Owing to intense evaporation and shallow groundwater, the area is highly prone to soil salinization
making it an ideal/representative site for studying...
These conditions make the region a typical case of (secondary salinization / dryland degradation)
```

## 3. 研究区示范(标注每句功能,构造示例)

> **[位置]** *The study area is located in the Yanqi Basin, an arid oasis in the southern margin of the Tianshan Mountains, Northwest China (41.8°–42.5°N, 86.0°–86.9°E), covering approximately 5,800 km².*
> **[气候]** *The region has a typical temperate arid climate, with a mean annual temperature of 8.4 °C, mean annual precipitation of only 68 mm, and potential evaporation exceeding 2,000 mm.*
> **[地形+水文]** *The terrain is generally flat (elevation 1,050–1,100 m a.s.l.) and is fed by snowmelt-derived rivers; the shallow groundwater table (typically < 2 m) is recharged by irrigation return flow.*
> **[土壤+植被]** *The dominant soils are Solonchaks (WRB), and natural vegetation is sparse, dominated by salt-tolerant halophytes such as Tamarix and Suaeda.*
> **[人文]** *Intensive flood irrigation has expanded over recent decades to support cotton and maize production.*
> **[科学意义/收敛]** *The combination of intense evaporation, shallow saline groundwater, and inefficient irrigation makes the basin highly prone to secondary salinization, providing a representative setting for evaluating multi-source salinity retrieval.*

> 习惯上配一张 **study area / location map**(常含 DEM、采样点分布、Sentinel/Landsat 真彩或假彩底图)。正文里务必引用:*The location of the study area and sampling sites is shown in Fig. 1.*

---

# 第二部分 · 数据(Data)

## 4. 🍳 配方:数据分两类写

```
4.1 实测数据(field / in-situ data)
4.2 遥感及辅助数据(remote sensing + auxiliary data)
```

每一类都要交代清楚:**数据类别 + 数据来源 + 关键参数**。下面是必给参数的"清单"。

### 4.1 实测数据 —— 必给参数
- 采样/观测**时间**(年月,是否与遥感过境同步)
- 样点**数量**与布设方式(网格/随机/分层;是否分训练-验证)
- **仪器型号**(如便携式电导率仪、ASD 光谱仪)
- **测量参数**与方法(如表层 0–20 cm 土壤 EC、SOC 用重铬酸钾氧化法)
- 质控/预处理(异常值剔除、单位换算 EC→dS/m)

### 4.2 遥感及辅助数据 —— 必给参数
- **遥感数据**:卫星/传感器名称、获取时间、空间分辨率、光谱分辨率/波段范围、产品级别、预处理(大气校正、几何校正、去云)、获取平台(GEE/Copernicus/USGS)
- **辅助数据**:DEM(来源、分辨率)、土地利用/土地覆盖图、气象站/再分析数据(降水、温度)、土壤数据库等——给来源、分辨率、时段

## 5. 数据描述高频句式

```
遥感数据
Sentinel-2 Level-2A surface reflectance images (10 m) acquired in (July 2022) were used
Landsat-8 OLI imagery (30 m, Path/Row XXX) was obtained from the USGS Earth Explorer
All images were atmospherically and geometrically corrected; cloudy pixels were masked
were processed on the Google Earth Engine (GEE) platform
A total of X cloud-free scenes covering 2000–2022 were composited

实测数据
A total of N soil samples were collected from the topsoil (0–20 cm) in (month/year)
Sampling sites were distributed using a (stratified random / grid) scheme (Fig. 1)
Electrical conductivity (EC) was measured with a (model, manufacturer, city, country)
The dataset was randomly split into training (70%) and validation (30%) subsets

辅助数据
A digital elevation model (DEM, 30 m) was obtained from (SRTM / ASTER GDEM)
Land-use/land-cover data were derived from...
Meteorological data (precipitation, temperature) were obtained from (X stations / ERA5 reanalysis)
```

## 6. 数据表(强烈建议)

地理/遥感论文几乎都用一张表汇总数据源。列示例:

| Data | Source / Sensor | Acquisition time | Resolution | Use |
|---|---|---|---|---|
| Optical | Sentinel-2 L2A | Jul 2022 | 10 m | spectral indices |
| SAR | Sentinel-1 GRD | Jul 2022 | 10 m | polarimetric features |
| DEM | SRTM | 2000 | 30 m | terrain covariates |
| Field EC | portable EC meter | Jul 2022 | 120 points | calibration/validation |

> 正文里务必引用表:*The data sources used in this study are summarized in Table 1.*

---

# 第三部分 · 方法(Methods / Algorithm)

## 7. 🍳 配方:介绍一个算法的 6 要素

每个核心算法/方法,按这 6 点写(不必都长,但都要有):

```
[1] 是什么:方法全称 + 缩写 + 一句定位(it is a ... that ...)
[2] 原理:核心思想/数学基础(1-3 句,可给关键公式)
[3] 步骤:在本研究里的实施流程(按时序)
[4] 优势:为什么选它(对比替代方法;为什么适合本问题)
[5] 本研究参数设置:超参数、阈值、窗口、训练设置——给具体数值
[6] 平台与包(版本):实现平台、软件、库及版本号(可复现关键)
```

**示范**(随机森林反演,构造示例):
> **[是什么]** *Random forest (RF) is an ensemble learning algorithm that constructs multiple decision trees and aggregates their outputs.*
> **[原理]** *Each tree is trained on a bootstrap sample, and at each split a random subset of predictors is considered, which reduces overfitting and variance.*
> **[步骤]** *We used spectral indices, polarimetric features, and terrain covariates as predictors and field-measured EC as the response. The model was trained on the 70% training subset and applied pixel-by-pixel to produce a wall-to-wall salinity map.*
> **[优势]** *RF was chosen for its robustness to high-dimensional, collinear predictors and its ability to capture non-linear relationships without strong distributional assumptions.*
> **[参数]** *The number of trees (ntree) was set to 500 and the number of variables per split (mtry) was tuned by 10-fold cross-validation.*
> **[平台/包]** *RF was implemented in Python 3.10 using scikit-learn (v1.3); spatial pre-processing was performed in Google Earth Engine.*

## 8. 双分支:两类论文的方法写什么

### 【定量反演】方法链常见组件
```
预测变量构建:spectral indices, band ratios, texture, polarimetric features, terrain covariates
变量筛选:correlation analysis, RFE, variable importance, Boruta, VIF
建模:PLSR / RF / XGBoost / SVR / CNN / Cubist...
精度验证:k-fold / leave-one-out CV;独立验证集;指标 R², RMSE, MAE, RPD, bias
不确定性:bootstrap, prediction interval
```
关键句:
- *Predictor variables were selected based on variable importance and Pearson correlation with measured EC.*
- *Model performance was assessed using the coefficient of determination (R²), root-mean-square error (RMSE), and the ratio of performance to deviation (RPD), based on 10-fold cross-validation.*

### 【时空变化】方法链常见组件
```
长时序构建:annual composites, max-NDVI compositing, gap-filling, harmonic fitting
趋势分析:linear regression slope, Theil–Sen median slope, Mann–Kendall (MK) test
变化检测:image differencing, post-classification comparison, LandTrendr/BFAST, CVA
显著性/分级:p < 0.05, trend significance classes
驱动归因:partial correlation, residual trend analysis, multiple regression,
         geographical detector, contribution rate of climate vs human activities
```
关键句:
- *Per-pixel trends in annual NDVI from 2000 to 2022 were quantified using the Theil–Sen median slope, and their significance was tested with the Mann–Kendall test (p < 0.05).*
- *The relative contributions of climate change and human activities were separated using residual trend analysis.*

## 9. 关键写作决策(沿用通用规则,领域例)

### 决策 1:主动还是被动?
- **数据处理/标准流程**:多用被动(*Images were atmospherically corrected... Samples were oven-dried...*)
- **你的核心方法贡献**:用主动突出主权(*We developed a multi-source framework... We fused optical and radar features...*)
- 混合策略最常见(遥感论文典型)。

### 决策 2:**主权(ownership)** 必须清晰
无主体被动分不清"你做的"还是"引用的":
> ❌ *A salinity index was calculated.*(谁提出的?你还是前人?)
> ✅ *We calculated the salinity index proposed by Khan et al. (2005).* / *In this study, the salinity index was calculated as...*

| 你想表达 | 怎么标记 |
|---|---|
| 这是我们做的 | *We did X* / *Here, X was done* / *In this study, X was done* |
| 这是引用的方法 | *following X et al. (2020)* / *using the index proposed by...* + 引文 |
| 这是标准流程 | *X is computed as...*(现在简单)+ 引文 |

### 决策 3:时态
| 描述对象 | 时态 |
|---|---|
| 你做的操作(采样、训练、反演) | **过去简单**(*Samples were collected... We trained...*) |
| 标准/通用定义(指数公式、算法属性) | **现在简单**(*NDVI is defined as (NIR−Red)/(NIR+Red).*) |
| 设备/算法的永久属性 | **现在简单**(*RF constructs multiple decision trees.*) |

⚠️ 隐形错误:把自己做的写成现在简单,变"标准流程",丢失贡献。

## 10. 承认问题 / 局限(地理/遥感版,中文作者最该补)

**主动承认 = 专业可信**。常见可承认点:
```
数据局限:cloud contamination, mixed pixels, limited field samples, temporal mismatch
方法局限:empirical model may not transfer, saturation at high values, scale mismatch
策略:弱化问题 + 弱化责任 + 给方向
A potential limitation is that field samples were collected in a single season...
Owing to persistent cloud cover, optical observations were limited to the dry season...
The 10 m resolution may not fully resolve fine-scale salt patches; however,...
Future work will incorporate hyperspectral data to mitigate index saturation.
```
> 区别:*Future work **should**...* = 建议研究界;*Future work **will**...* = 我自己接着做。

## 11. 子标题(Subsections)写法
方法常分子节,风格一致(全名词短语或全 -ing):
- *Field sampling and laboratory analysis*
- *Satellite data and pre-processing*
- *Spectral index calculation*
- *Model development and validation*
- *Trend and change-point analysis*

## 12. 实操写作清单(研究区/数据/方法)
- [ ] 研究区按**位置→自然→人文→意义**漏斗,末句**收敛到研究问题**?
- [ ] 研究区有 location map 且正文引用?经纬度/面积/气候/土壤都给了?
- [ ] 数据分**实测 / 遥感+辅助**,每类**参数齐全**(时间/分辨率/波段/样点数/仪器型号)?
- [ ] 有数据汇总表且正文引用?
- [ ] 每个核心方法按 **6 要素**(是什么/原理/步骤/优势/参数/平台版本)写?
- [ ] **软件/库都标了版本号**(可复现)?
- [ ] 反演:验证指标(R²/RMSE/RPD)、验证方式(CV/独立集)写清楚?
- [ ] 变化:趋势方法(Sen+MK)、显著性、驱动归因方法写清楚?
- [ ] 所有被动句读者都能分清"你做的"还是"引用的"?
- [ ] 时态一致,切换有理由?
- [ ] 引用前人方法时说清相同/不同?
- [ ] **承认至少一个局限**(数据或方法)并合理弱化?

## 13. 常见错误
- **流水账**:*We downloaded images. Then we corrected them. Then we...* → 用从句/并列组织,突出关键参数。
- **被动丢主权**:*A novel framework was developed.*(谁?)→ *We developed...* 或 *Here, ... was developed*。
- **研究区写成地理课本**:堆无关地理事实 → 只留服务研究问题的。
- **数据缺参数**:只说"用了 Sentinel-2",没给时间/分辨率/波段/预处理 → 补全。
- **版本号缺失**:审稿要求可复现 → 软件、库、产品级别都标号。
- **回避局限**:整节不提任何问题 → 审稿人会自己找。

## 14. 🍳 配方速用版 vs 🔬 反向工程版
- **🍳 配方**:研究区四段漏斗 + 数据两类参数表 + 方法 6 要素(按反演/变化分支)。够投 Catena/Geoderma/JAG/IJRS。
- **🔬 反向工程**:冲 RSE/ISPRS J/TGRS 时,数 4 篇该刊近作:研究区给多细?数据用表还是文字?方法多依赖公式?验证用哪几个指标、报到几位小数?照它校准。
