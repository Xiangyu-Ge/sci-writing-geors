# 07 · 标题(Title)写作详解 · 地理/遥感版

互联网时代,**标题决定论文是否被搜到、被点开**。搜索引擎以标题排序,读者扫几十上百个标题。差标题会埋没好工作。**标题不是 name tag,是 marketing copy。**

## 1. 🍳 配方:两类论文的标题骨架(双分支)

### 【定量反演】标题骨架
```
[属性/对象] + [反演/估算] + [手段/数据] + [研究区]
模式:  Retrieval/Estimation/Mapping of <属性> using <数据/方法> in <研究区>
       <属性> mapping by integrating <A> and <B>: a case study in <研究区>
```
例:
- *Mapping topsoil salinity by integrating Sentinel-1 and Sentinel-2 data in an arid oasis, Northwest China*
- *Retrieval of soil organic carbon from hyperspectral imagery using a deep-learning model in cropland*
- *Estimating surface soil moisture from SAR–optical fusion in a semi-arid basin*

### 【时空变化】标题骨架
```
[对象] + [时空动态/变化/趋势] + [时段] + [研究区] + (± 驱动归因)
模式:  Spatiotemporal dynamics of <对象> and its drivers in <研究区> (period)
       <对象> change and attribution in <研究区> from <year> to <year>
```
例:
- *Spatiotemporal dynamics of vegetation greening and its drivers in an arid oasis, 2000–2022*
- *Soil salinization expansion and its climatic and anthropogenic drivers in the Tarim Basin (1990–2020)*
- *Quantifying the relative contributions of climate and human activities to NDVI change in drylands*

> 反演重 **属性+手段+区**;变化重 **对象+动态+时段+区(+归因)**。时段、研究区是地理/遥感标题的高频要素,但别让它们把关键词挤到后面。

## 2. 标题的"7 步检查法"

### 步骤 1·平均长度
地理/遥感标题平均约 **12-16 词**(实际数目标期刊;RSE 偏中等,Catena/Geoderma 常稍长)。越短不一定越好——重点是含关键词、能判相关性、反映"产出"而非"过程"。

### 步骤 2·关键词位置(SEO 黄金法则)
**最重要的关键词放最前面**。读者搜的是对象/属性(soil salinity, vegetation, SOC),不是 *a study on*。
❌ *A study on the application of remote sensing for monitoring soil salinity in arid regions*
✅ *Soil salinity monitoring in arid regions using multi-source remote sensing*

### 步骤 3·标题关键词 vs 关键词列表
单独提交的 5-8 个关键词应**与标题互补**,扩大读者面:标题已含 *soil salinity, Sentinel*,关键词可补 *electrical conductivity, random forest, dryland, precision agriculture*。

### 步骤 4·语法检查(地理/遥感高发)
**问题 1·复合名词链过长**(遥感标题重灾区)
❌ *Sentinel-2 multi-temporal vegetation index time series soil salinity inversion model accuracy assessment*
✅ *Accuracy of soil salinity retrieval from Sentinel-2 vegetation-index time series*(用介词拆开)
> 复合名词左边全在修饰右边,一长串挂下来关系全乱。**名词链 ≤ 3 个**。

**问题 2·介词太多**
❌ *Estimation of the spatial distribution of the content of soil organic carbon in the topsoil of the cropland of the basin*
✅ *Mapping topsoil organic carbon in basin cropland*(砍掉多余 of)

**问题 3·介词造成歧义**
❌ *Retrieval of soil moisture with vegetation*(用 vegetation 反演?还是有植被覆盖的土壤水分?)
✅ *Retrieval of soil moisture under vegetation cover*

### 步骤 5·结构内容映射(勾选)
```
□ 含对象/属性(必须,且前置)
□ 含数据/方法(Sentinel, SAR, random forest, Theil–Sen)— 反演几乎必含
□ 含研究区(in <region>;地理/遥感常含)
□ 含时段(period;变化类几乎必含)
□ 含 happy word(0-2 个:multi-source, high-resolution, first long-term)
□ 缩写都是领域常识?(NDVI/LST/SAR/SOC 可;自造缩写慎用)
□ 用冒号分主题:贡献?
```

### 步骤 6·期待 vs 兑现(不标题党)
标题暗示 X,论文必须 deliver X。若只是"可能性",用 may/might 软化:
> *Irrigation expansion **may** explain recent greening in arid oases*

### 步骤 7·删"工作标题"痕迹
工作标题含 *study, investigation, analysis, application* 等无信息词:
| 工作标题(差) | 论文标题(好) |
|---|---|
| *A study on soil salinity in arid areas* | *Mapping soil salinity in arid oases by radar–optical fusion* |
| *Research on vegetation change using remote sensing* | *Spatiotemporal vegetation dynamics and their drivers in an arid basin (2000–2022)* |
| *Application of machine learning in SOC estimation* | *Random-forest retrieval of topsoil organic carbon from hyperspectral data* |

## 3. 标题三大类型
- **A·名词短语**(最常见):*Mapping topsoil salinity by radar–optical fusion in an arid oasis*
- **B·主题:焦点**(冒号):*OasisSalt: a multi-source framework for operational soil-salinity mapping*
- **C·句子型**(完整句,结果够强 + 期刊接受):*Human activities dominate vegetation greening in arid oases* / *Irrigation expansion may drive recent greening in drylands*
> 句子型标题在 RSE/顶刊变化归因类越来越多;Catena/Geoderma 仍以 A/B 为主。看目标期刊。

## 4. 语言原则
1. **具体 > 模糊**:❌ *A study on water and soil* ✅ *Retrieval of topsoil salinity from Sentinel-1/2 in an arid oasis*
2. **产出 > 过程**:❌ *Investigation of factors affecting NDVI* ✅ *Human activities, not climate, drive NDVI greening in an arid basin*
3. **happy words 节制**:挑一个最准的(*multi-source* 或 *high-resolution* 或 *first long-term*),别堆。
4. **避免弱词单飞**:*Study of / Analysis of / Application of* → *Retrieval of / Mapping of / Spatiotemporal dynamics of / Attribution of*。
5. **慎用 "The effect of / The role of" 开头**:太常见,搜索里不显眼。
6. **数字有意义才放**:*10 m* / *2000–2022* / *R² = 0.81 提升* 可放;无意义细节不放。

## 5. 前 6 词检查
搜索结果常只显示前 6-8 词。问:**只看前 6 词,读者能识别这是关于什么的吗?**
✅ *"Mapping topsoil salinity by radar–optical..."* → 能
❌ *"A case study using multi-source data to..."* → 不能

## 6. 中文用户的标题"陷阱"(地理/遥感)
- **陷阱 1·套中文句式**:"基于 X 的 Y 研究"直译冗长。
  ❌ *A study on soil salinity inversion based on Sentinel data in the Yanqi Basin* ✅ *Soil-salinity retrieval from Sentinel data in the Yanqi Basin, Northwest China*
- **陷阱 2·谦虚开头**:*A preliminary study of... / Some considerations on...* → 英语读者直接划走。
- **陷阱 3·堆叠定语**:中文可挂很多"的",英文复合名词链会爆。用冒号或介词拆。
- **陷阱 4·不"卖"**:怕自夸去掉所有评价词 → 标题平淡。*multi-source / high-resolution / first long-term* 是合规的"卖点"。
- **陷阱 5·研究区写法不统一**:统一用 *in <region>, <country>*(如 *in the Tarim Basin, Northwest China*),别一会儿拼音一会儿英译。

## 7. 标题模板库(可直接套)
```
反演:
  <属性> retrieval/mapping from <数据> using <方法> in <研究区>
  Integrating <A> and <B> for <属性> estimation in <研究区>
  <ToolName>: a <adj> framework for <属性> mapping
变化:
  Spatiotemporal dynamics of <对象> in <研究区>, <year>–<year>
  <对象> change and its drivers in <研究区> over the past <N> years
  Quantifying the contributions of climate and human activities to <对象> change
  <Driver> dominates/drives <对象> change in <研究区>  (句子型)
```

## 8. 反向工程练习
让用户用 7 列分析 5-10 篇目标论文标题:

| 标题 | 词数 | 类型(A/B/C) | 主关键词 | 含数据/方法? | 含研究区/时段? | 含 happy word? |
|---|---|---|---|---|---|---|

看自己的标题:词数偏离均值?类型与期刊主流一致?关键词前置?研究区/时段位置合理?"风味"对不对?

## 9. 实操写作清单
- [ ] 词数符合目标期刊?
- [ ] **对象/属性关键词前置**?
- [ ] 反演:含手段+研究区?变化:含时段+研究区(±归因)?
- [ ] 类型(短语/冒号/句子)与目标期刊一致?
- [ ] 复合名词链 ≤ 3?介词 ≤ 3 且无歧义?
- [ ] 缩写都是领域常识?
- [ ] 无 working-title 痕迹(*A study of / Application of*)?
- [ ] 前 6 词就传达核心?
- [ ] happy words 0-2 个且真实?
- [ ] 不标题党(确实兑现)?
- [ ] 关键词列表与标题互补?
- [ ] Google Scholar 搜你的标题关键词,搜出的论文与目标读者一致(SEO 测试)?

## 10. 一个完整"标题进化"案例(反演)
```
迭代1(工作标题): "Soil salinity and remote sensing"               → 太空泛
迭代2(描述话题): "Soil salinity estimation in an arid oasis"      → 没说手段/产出
迭代3(加手段):   "Soil salinity estimation using Sentinel data in an arid oasis"  → 好一点
迭代4(加价值):   "Soil salinity estimation by integrating Sentinel-1 and Sentinel-2 in an arid oasis"  → 体现多源
迭代5(优化位置): "Mapping topsoil salinity by radar–optical fusion in an arid oasis, Northwest China"  → 关键词前置,产出动词,13 词 ✅
```
让用户写 5 个候选标题,给同事看(不说论文内容)让他们猜讲了什么,选最多人猜对的那个。通常 4-5 轮稳定。

## 11. 🍳 配方速用版 vs 🔬 反向工程版
- **🍳 配方**:按反演/变化骨架套(§1),过 7 步检查。够投 Catena/Geoderma/JAG/IJRS。
- **🔬 反向工程**:冲 RSE/ISPRS J 时,数 4 篇近作标题:平均几词?用不用冒号?句子型多不多?是否都含研究区/时段?照它校准。
