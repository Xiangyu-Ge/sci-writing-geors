# 03 · 研究区、数据与方法（Materials and Methods）

方法部分的唯一标准是可复现：别的研究者能找到同样的研究区、拿到同样的数据、跑出同样的结果。地理/遥感论文的方法通常分三块：

```
研究区 Study Area  →  数据 Data  →  方法 Methods
（在哪做）            （用什么）       （怎么做）
```

**方法与结果的边界**：验证方案（数据怎么划分、用哪些指标）在方法中交代；精度验证结果和模型比较写在结果中。

---

## 第一部分 · 研究区

### 1. 逻辑：位置 → 自然 → 人文 → 科学意义

先宏观定位，再细化到气候、土壤、植被等要素，最后聚焦研究问题。

**必含要素**：

1. 地理位置（经纬度范围、行政或地理单元、面积）
2. 自然地理特征（气候、地形、水文）
3. 土壤和植被类型（土壤注明分类体系：WRB / USDA / 中国土壤系统分类）
4. 存在的环境问题或研究意义（如土壤盐渍化）

人文要素（人口、灌溉、放牧）按研究需要写。

> 不要写成"地理课本"。每一句都要为研究问题服务：研究盐分，就突出干旱、强蒸发、浅地下水、灌溉这些盐渍化成因；与研究无关的要素一句带过或删掉。

配一张研究区图（位置、DEM、采样点、底图），正文引用：*The location of the study area and sampling sites is shown in Fig. 1.*

### 2. 研究区示范（构造示例）

> **[位置]** *The study area is located in the Yanqi Basin on the southern margin of the Tianshan Mountains, Northwest China (41.8°–42.5°N, 86.0°–86.9°E), covering approximately 5,800 km².*
> **[气候]** *The region has a temperate arid climate, with a mean annual temperature of 8.4 °C, mean annual precipitation of 68 mm, and potential evaporation exceeding 2,000 mm.*
> **[地形 + 水文]** *The terrain is flat (1,050–1,100 m a.s.l.) and fed by snowmelt rivers; the groundwater table is shallow (typically < 2 m).*
> **[土壤 + 植被]** *The dominant soils are Solonchaks (WRB), and natural vegetation is dominated by halophytes such as Tamarix and Suaeda.*
> **[人文]** *Flood irrigation has expanded over recent decades to support cotton and maize production.*
> **[收敛到研究问题]** *Intense evaporation, shallow saline groundwater, and inefficient irrigation make the basin highly prone to secondary salinization.*

（示例中的数字为构造值，写作时用研究区的实测或文献数据并引用。）

### 3. 研究区高频表达

```
位置    The study area is located in / lies in...; covers approximately X km²; extends from X°N to Y°N
气候    is characterized by a (temperate arid / semi-arid / monsoon) climate;
        mean annual temperature is X °C and mean annual precipitation is Y mm;
        potential evaporation (~X mm) far exceeds precipitation
地形水文 elevation ranges from X to Y m a.s.l.; is fed by snowmelt from...; the groundwater table is shallow (< X m)
土壤植被 The dominant soil types are... according to the WRB classification; vegetation is dominated by...
收敛句   Owing to..., the area is highly prone to...; making it a representative setting for...
```

---

## 第二部分 · 数据

### 4. 分两类写，参数给全

**实测数据必给**：

- 采样或观测时间，是否与遥感过境同步（时间差写明天数）
- 采样设计：随机、分层、网格还是目的性布点；样点数
- 样品支撑（sample support）：采样深度、样方大小、是否混合样
- 仪器型号与测定方法（如 EC 用 1:5 土水比浸提，注明仪器型号）
- 质控与预处理（异常值剔除、单位换算）

一项对 188 篇数字土壤制图论文的系统综述发现，25% 没写采样设计，45% 没写样品支撑，这使验证指标难以解读。这两项务必写。

**遥感及辅助数据必给**：

- 卫星/传感器、获取时间、空间分辨率、波段、产品级别
- 预处理：大气校正、几何校正、云掩膜
- 平台：GEE、USGS、Copernicus
- 辅助数据（DEM、土地利用、气象、再分析）：来源、分辨率、时段

### 5. 数据汇总表

| Data | Source / Sensor | Acquisition time | Resolution | Use |
|---|---|---|---|---|
| Optical | Sentinel-2 L2A | Jul 2022 | 10 m | spectral indices |
| SAR | Sentinel-1 GRD | Jul 2022 | 10 m | polarimetric features |
| DEM | SRTM | 2000 | 30 m | terrain covariates |
| Field EC | portable EC meter | Jul 2022 | 120 points | calibration / validation |

正文引用：*The data sources used in this study are summarized in Table 1.*

### 6. 数据描述高频句式

```
Sentinel-2 Level-2A surface reflectance images (10 m) acquired on (date) were used
All images were atmospherically and geometrically corrected, and cloudy pixels were masked
A total of N soil samples were collected from the topsoil (0–20 cm) in (month year)
Sampling sites were distributed using a stratified random scheme (Fig. 1)
EC was measured in a 1:5 soil/water suspension with a (model, manufacturer, country)
The dataset was split into modeling (70%) and independent validation (30%) subsets
```

---

## 第三部分 · 方法

### 7. 流程图放在方法最开始

方法第一节先放一张技术路线图，清楚展示整体方法框架（数据 → 预处理 → 特征 → 建模/分析 → 验证 → 制图/归因）。后面每个小节对应图中的一个模块。

### 8. 常用方法和新方法写法不同

| 方法类型 | 写法 |
|---|---|
| **常用方法** | 第一句定义 → 一句原理 → 1–2 句步骤和优势 → 参数如何设置 → 本研究所用参数、软件包、平台（版本号） |
| **新方法或改进方法** | 重点写在哪里做了更新、优化或改进，以及为什么这样改；尽量配图说明 |

**常用方法示范**（随机森林，构造示例）：
> **[定义]** *Random forest (RF) is an ensemble learning algorithm that builds multiple decision trees and aggregates their outputs.*
> **[原理]** *Each tree is trained on a bootstrap sample, and a random subset of predictors is considered at each split, which reduces variance.*
> **[步骤与优势]** *We used spectral indices, polarimetric features, and terrain covariates as predictors of field-measured EC. RF was chosen because it handles collinear predictors and non-linear relationships without distributional assumptions.*
> **[参数]** *The number of trees was set to 500, and mtry was tuned by 10-fold cross-validation on the modeling subset.*
> **[平台]** *RF was implemented in Python 3.10 with scikit-learn 1.3.*

**新方法示范**（构造示例）：
> *Unlike the original stacking framework, which combines base learners with a linear meta-learner, we replaced the meta-learner with a Bayesian-optimized gradient-boosting model (Fig. 3). This change allows the ensemble to weight base learners differently across the salinity range, which addresses the underestimation of high-salinity samples reported in earlier studies.*

### 9. 两类研究的方法链

**定量反演 / 模拟**
```
预测变量：光谱指数、波段比值、纹理、极化特征、地形协变量
变量筛选：相关分析、RFE、Boruta、VIF（先处理共线性，再做 SHAP）
建模：PLSR / RF / XGBoost / SVR / CNN / 集成模型；与简单基线比较
验证方案：独立验证集优先（见 04-validation-uncertainty.md）；指标 R²、RMSE、MAE、RPD、bias
不确定性：bootstrap、分位数回归森林、预测区间
```

**时空变化**
```
长时序：年合成、最大值合成、插补、谐波拟合
趋势：Theil–Sen 斜率 + Mann–Kendall 检验
变化检测：差值法、分类后比较、LandTrendr / BFAST、CVA
显著性分级：p < 0.05
驱动归因：偏相关、残差趋势分析、地理探测器、SEM、SHAP / GeoShapley
```

观测对照类的设计要素（处理、对照、重复、随机化、伪重复）见 `16-paper-types.md`。

### 10. 主权、语态、时态

- **主权**：读者要分得清哪些是你做的，哪些是引用的。
  > ❌ *A salinity index was calculated.*
  > ✅ *We calculated the salinity index proposed by Khan et al. (2005).*
- **语态**：标准处理流程多用被动；本研究的核心方法贡献用主动（*We developed…*）。
- **时态**：自己做的操作用过去简单；标准定义、公式、算法属性用现在简单（*NDVI is defined as…*）。

### 11. 局限的写法

主动承认局限，并说明它对结论的影响：

```
A potential limitation is that field samples were collected in a single season...
Owing to persistent cloud cover, optical observations were limited to...
The 10 m resolution may not resolve fine-scale salt patches; however,...
```

*Future work should…* 是建议研究界；*Future work will…* 是自己接着做。

### 12. 新手方法写法的典型问题

- 缩写没有全称
- 描述复杂，读完无法形成概念
- 步骤、参数描述不清楚
- 参数为什么这样设置没有讲
- 简单方法写得复杂，复杂方法写得简单
- 只写"用了 Sentinel-2"，没有时间、分辨率、波段、预处理
- 软件、库、产品没有版本号
- 被动句满篇，分不清是自己做的还是引用的

### 13. 自查清单

- [ ] 研究区按"位置→自然→人文→科学意义"组织，四类必含要素齐全，末句收敛到研究问题
- [ ] 有研究区图并在正文引用
- [ ] 实测数据写了采样设计、样点数、样品支撑、采样与过境时间差、仪器与方法
- [ ] 遥感与辅助数据参数齐全，有数据汇总表
- [ ] 方法开头有技术路线图
- [ ] 常用方法按"定义→原理→步骤与优势→参数→平台"写；新方法写清改了哪里、为什么改
- [ ] 验证方案（划分方式、指标）在方法中交代，并说明理由
- [ ] 软件、库都有版本号
- [ ] 每个缩写首次出现时给出全称
- [ ] 承认了至少一个数据或方法局限
