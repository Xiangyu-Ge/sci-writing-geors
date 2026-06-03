# 03 · 结果(Results)写作详解 · 地理/遥感版

很多作者把结果写成图表的"文字版"(把散点图、趋势图用文字念一遍)——对读者毫无价值,他们自己也会看图。**好的 Results 用叙事引导读者去看你想让他们看到的东西,并初步评价。**

## 1. 🍳 配方:每个图表按 5 步写

这是地理/遥感结果段落的强默认结构。**每呈现一张关键图/表,走一遍这 5 步**:

```
[1] 图表内容:这是什么图/表(邀请读者看)
[2] 最值/最重要信息:最高/最低/峰值/最显著的那个数或区域
[3] 数据的含义:这些数字/格局说明了什么(不是念数,是解读趋势/分布)
[4] 直观信息:空间上/时间上肉眼可见的规律(哪里高、哪里低、何时转折)
[5] 意义:这个结果意味着什么、预告讨论(suggesting that...)
```

**示范**(盐分反演精度图,构造示例,标注 5 步):
> **[1 内容]** *Figure 3 shows the scatterplot of measured versus predicted soil salinity for the validation set.*
> **[2 最值/关键]** *The multi-source model achieved the best performance, with an R² of 0.81 and an RMSE of 2.3 dS/m.*
> **[3 含义]** *Predicted values closely followed the 1:1 line across the full salinity range, indicating that the model captured both low- and high-salinity samples well.*
> **[4 直观]** *Slight underestimation was visible only at extreme values (> 20 dS/m), where field samples were sparse.*
> **[5 意义]** *These results suggest that integrating radar features substantially improved retrieval over the optical-only model (R² = 0.64).*

## 2. 整体安排:Results 区的 4 种组织
| 方案 | 结构 | 适用 |
|---|---|---|
| 1 | Results / Discussion / Conclusion | 标准三段式 |
| 2 | Results / Discussion | 结论并入讨论 |
| 3 | Results and Discussion / Conclusion | 结果与讨论交织(地理/遥感常见,尤其变化分析) |
| 4 | Results / Conclusion | 简洁文章 |

让用户查目标期刊主流是哪种(Catena/Geoderma 常见 Results and Discussion 合写)。

## 3. 结果的通用模型(4 组件)
```
┌───────────────────────────────────────────────┐
│ 1·引入:回顾目标/方法关键点 + 邀请看图表          │
│ 2·关键结果:详细呈现 + 评价语言 + 与前人/模型对比 │
│ 3·问题/局限 ± 原因                              │
│ 4·初步意义 / happy words(预告讨论)             │
└───────────────────────────────────────────────┘
```

## 4. 双分支:两类论文的结果重心不同

### 【定量反演】结果重心 = 精度验证
顺序常为:**变量重要性 → 模型对比 → 验证精度(散点/指标)→ 空间制图 → 误差空间分布**
```
报告精度:achieved an R² of X, an RMSE of Y, and an RPD of Z
模型对比:outperformed the optical-only model / single-sensor baseline
变量重要性:the most important predictors were... contributing X% to model performance
空间制图:the resulting salinity map (Fig. X) revealed that high-salinity areas were concentrated in...
```
- *The RF model achieved the highest accuracy (R² = 0.81, RMSE = 2.3 dS/m), outperforming PLSR (R² = 0.58).*
- *Variable importance analysis identified the salinity index and VH backscatter as the dominant predictors.*
- *The salinity map (Fig. 5) showed that severely salinized soils were concentrated in the low-lying oasis margins.*

### 【时空变化】结果重心 = 格局 + 速率 + 热点 + 驱动
顺序常为:**总体趋势 → 空间格局/热点 → 变化速率分级 → 显著性 → 驱动归因**
```
总体趋势:NDVI exhibited a significant increasing trend (Sen's slope = X /yr, p < 0.05)
空间格局:greening was concentrated in..., whereas browning occurred mainly in...
速率分级:X% of the area showed significant greening, Y% showed significant browning
驱动归因:climate change and human activities contributed X% and Y%, respectively
```
- *Over 2000–2022, annual NDVI increased significantly across 63% of the basin (Sen's slope > 0, p < 0.05).*
- *Greening was concentrated in the irrigated oasis, whereas browning dominated the desert–oasis ecotone (Fig. 4).*
- *Residual trend analysis attributed 71% of the greening to human activities and 29% to climate.*

## 5. 时态选择
| 描述对象 | 时态 |
|---|---|
| 图表"看得见"的内容(*Figure 2 shows...*) | **现在简单** |
| "我们观测到/反演得到"(具体发现) | **过去简单** |
| 已知属性/公式 | **现在简单** |
| 模型"运行/输出"的描述 | **现在简单** |

> *Fig. 4 **shows** the spatial trend of NDVI. Significant greening **was observed** in the oasis, which **is consistent with** expanded irrigation.*

## 6. 必须有"评价"——但要会评价
只描述图里能看到的 = 没说。读者已看图,你要告诉他们**这意味着什么**。

### 评价语言(两类)
**类 1·形容词/副词**(同一数字,印象相反):
| 强调"很好/很多/很显著" | 强调"只有一点" |
|---|---|
| substantially, markedly, considerably | only, just, merely |
| significantly, notably, pronounced | slightly, marginally |
| a striking/remarkable (improvement) | a modest/minor (increase) |
| as high as, as much as | a mere |

> R² 提升:强→*a substantial improvement (R² from 0.64 to 0.81)*;弱→*a modest improvement*。匹配数据真实强度。

**类 2·"惊叹号替代词"**(英文不用"!"):
```
striking   remarkable   pronounced   notably   importantly
substantial  considerable  marked  interestingly  unexpectedly
```
> *We observed a **striking** spatial contrast between the greening oasis and the degrading ecotone.*

## 7. 邀请看图表的高频句式
```
Figure 1 shows / illustrates / displays / presents / depicts...
As shown in Fig. 1, / As can be seen from Fig. 1, ...
The spatial distribution of X is shown in Fig. 1
The results are summarized in Table 1
Close inspection of Fig. 1 reveals that...
(data not shown)
```
> 小区别:*from* = 可从图**推断/总结**;*in* = 图里**直接显示**。

## 8. 描述结果的高频动词(地理/遥感)
```
increased / decreased / declined / rose / fell / remained stable
peaked / reached a maximum / dropped to a minimum
was concentrated in / was distributed across / clustered around
exhibited / displayed / showed (a trend / a pattern)
ranged from X to Y / varied between
accounted for X% of / covered X% of the area
overestimated / underestimated / agreed well with
```
- *Severely salinized soils accounted for 18% of the study area.*
- *Predicted salinity ranged from 0.5 to 28 dS/m, peaking near the oasis margins.*
- *NDVI declined steadily in the ecotone, reaching a minimum in 2014.*

## 9. 与他人/模型对比
```
与前人:in line with / consistent with / in agreement with / in contrast to / unlike / higher/lower than reported by
与模型/预测:agrees well with / fits the 1:1 line / deviates from / overestimates / underestimates / captures the trend
```
- *Our retrieval accuracy (R² = 0.81) is comparable to or higher than values reported in similar arid regions (refs).*
- *Predicted values closely fit the 1:1 line, although high values were slightly underestimated.*
- *In contrast to previous studies that reported overall browning, we observed widespread greening within the irrigated oasis.*

## 10. 表达"问题/不完美结果"
策略:承认 + 弱化 + 给原因。
```
underestimation / overestimation was observed at...
some scatter / discrepancy can be seen at high values
possibly because of (saturation, mixed pixels, sparse samples)
within the uncertainty bounds / within experimental error
```
- *Slight underestimation at high salinity (Fig. 3) **probably reflects** the scarcity of field samples in that range.*
- *Some classification confusion **occurred** between bare saline soil and built-up areas, **possibly because of** similar spectral responses.*

## 11. 表达"结果的意义"(过渡到 Discussion)
动词强度梯度(匹配你的真实信心):
```
弱 → 强:suggest, indicate, imply, point to → support, are consistent with → demonstrate, show, confirm → prove, establish
```
- *These results **suggest that** radar–optical fusion can overcome the vegetation limitation of optical retrieval.*
- *Taken together, **these findings indicate that** human activities, rather than climate, dominate the recent greening.*

> 详见 `09-grammar-style.md` 的"确定性连续谱"。

## 12. 子标题:信息型(顶刊趋势)
用**带结论的子标题**,读者扫一眼就懂:
- *Multi-source fusion outperforms single-sensor retrieval*
- *Soil salinity is concentrated in low-lying oasis margins*
- *Human activities dominate the 2000–2022 greening trend*

检查目标期刊是否采用这种句子型子标题(RSE/ISPRS J 常见)。

## 13. 一个完整小段示范(标注每句功能,变化分析)
> **[引入/方法回顾]** ¹To examine vegetation dynamics, we computed per-pixel trends in annual maximum NDVI from 2000 to 2022 using the Theil–Sen slope and the Mann–Kendall test (see Methods).
> **[邀请看图]** ²The spatial pattern of NDVI trends is shown in Figure 4.
> **[关键结果+评价]** ³**Significant greening (p < 0.05) was observed across as much as 63% of the basin**, whereas significant browning was confined to only 9%.
> **[直观/空间格局]** ⁴Greening was concentrated within the irrigated oasis, while browning occurred mainly along the desert–oasis ecotone (Fig. 4).
> **[对比]** ⁵This spatial contrast differs from earlier reports of basin-wide degradation (refs).
> **[初步意义]** ⁶**These results suggest that** vegetation change in the basin is spatially decoupled, **pointing to** a human-driven greening superimposed on background climatic stress.
> **[局限+弱化]** ⁷We note that the coarse temporal resolution of the early-period imagery **may have introduced** some uncertainty into the trend estimates.

让用户给自己的 Results 每句做同样的功能标注。

## 14. 实操写作清单
- [ ] 每张关键图/表都走了 **5 步配方**(内容→最值→含义→直观→意义)?
- [ ] 反演:报了 R²/RMSE/RPD + 模型对比 + 空间制图?变化:报了趋势+速率+热点+归因?
- [ ] 每张图表**至少被正文引用一次**且**有解读**(不是只 *see Fig. X*)?
- [ ] 关键结果有**评价词**(striking/only/as much as/substantial)?
- [ ] 读者能分辨"哪些是亮点",不是所有结果同等详细?
- [ ] 与前人/模型做了对比?
- [ ] 承认了**至少一个**问题/局限?
- [ ] 用 *suggest/indicate* 预告了讨论?
- [ ] 数字、单位、精度位数、显著性标记一致(p < 0.05;R² 报两位小数)?
- [ ] 时态切换有理由?

## 15. 常见错误
- **图表文字翻译**:❌ *Figure 4 shows NDVI. It goes up here and down there.* → ✅ 用评价+解读+格局描述。
- **把讨论写进结果**:连写 3 句以上"为什么重要、如何改写领域"→ 挪到讨论。
- **过度肯定**:❌ *Our map proves where salinization occurs.* → ✅ *Our map identifies areas most prone to salinization.*
- **念数不解读**:❌ 把表里每个数字念一遍 → ✅ 只点最值/对比/趋势,其余让读者看表。
- **报喜不报忧**:只报高精度区,不报误差区 → 正负发现都呈现。

## 16. 🍳 配方速用版 vs 🔬 反向工程版
- **🍳 配方**:每张关键图表走 5 步,按反演/变化分支组织顺序。够投 Catena/Geoderma/JAG/IJRS。
- **🔬 反向工程**:冲 RSE/ISPRS J 时,数 4 篇近作:结果分几个子节?子标题是不是句子型?精度报到几位?图表比例多少?评价词密度?照它校准。
