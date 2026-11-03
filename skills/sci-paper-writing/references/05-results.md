# 05 · 结果（Results）

把散点图、趋势图用文字念一遍，对读者没有价值，他们自己会看图。结果部分要引导读者看到你想让他们看到的东西，并给出初步判断。

## 1. 顺序

- 结果的先后与方法的先后保持一致
- 每个结果回答的问题，与引言中的研究目标一一对应
- 同时兼顾讲故事的逻辑：先给支撑性结果（精度、可靠性），再给核心发现（格局、变化、归因）

**放在结果里的**：精度验证结果、模型之间的比较、不同方案/时段/区域之间的比较。
**不放在结果里的**：与前人文献的比较（放讨论）、机制解释（放讨论）。验证方案本身在方法中交代。

## 2. 每段结果的五步结构

```
[1] 总起：这张图表表达了什么，或直接给出本段的总结句
[2] 最重要的信息，并且要有比较
[3] 这些信息说明了什么
[4] 还有哪些需要陈述的发现（空间、时间上直观可见的规律）
[5] 以上结果表明什么，为后面的结果提供什么支撑
```

**示范**（盐分反演精度，构造示例）：

| 步骤 | 句子 |
|---|---|
| 1 总起 | *Fig. 5 compares measured and predicted soil salinity for the independent validation set.* |
| 2 关键信息 + 比较 | *The BC-Stacking model yielded the lowest RMSE (2.3 dS/m), 18% lower than RF (2.8 dS/m) and 31% lower than PLSR (3.3 dS/m).* |
| 3 说明什么 | *This indicates that combining base learners reduced errors across the full salinity range rather than only at low values.* |
| 4 其他发现 | *Underestimation remained for samples above 20 dS/m, which accounted for 6% of the validation set.* |
| 5 小结与承接 | *These results support the use of BC-Stacking for the salinity mapping presented in Section 4.3.* |

## 3. 两类研究的结果重心

**定量反演 / 模拟**：变量筛选与重要性 → 模型比较 → 验证精度（散点图、指标）→ 空间制图 → 误差与不确定性的空间分布

```
achieved an R² of X and an RMSE of Y (dS/m) on the independent validation set
outperformed the optical-only model / the linear baseline (R² = X)
the most important predictors were..., together accounting for X% of the total importance
high-salinity areas were concentrated in...
```

**时空变化**：总体趋势 → 空间格局与热点 → 变化速率分级 → 显著性 → 突变或阶段 → 驱动归因

```
NDVI increased significantly (Sen's slope = X yr⁻¹, p < 0.05) across X% of the basin
greening was concentrated in..., whereas browning occurred mainly in...
an abrupt change was detected in (year) (Pettitt test, p < 0.05)
human activities and climate contributed X% and Y%, respectively
```

**观测对照**：按"处理 vs 对照"组织，报告效应大小和置信区间，而不只是 p 值。

## 4. 评价：用幅度和对比，不用强调词

同一个数字，写法不同，读者印象相反。评价要匹配数据的真实强度，靠数字本身说话：

| 用这些 | 少用这些 |
|---|---|
| *as much as 63% of the basin* / *only 9%* | *a striking pattern* |
| *a 2.4-fold increase* / *from 0.64 to 0.81* | *a remarkable improvement* |
| *18% lower than RF* | *notably better* |
| *substantial / modest*（与数字连用） | *significant*（未做检验时） |

*significant* 只用于统计显著，并给出检验方法和 p 值。

## 5. 图表引用

```
Fig. 4 shows the spatial distribution of...
As shown in Fig. 4, ... / The results are summarized in Table 2.
```

每张图表至少被正文引用一次，并且有解读，而不只是 *see Fig. 4*。正文中的数字与图表中的数字必须一致。

## 6. 不完美的结果

承认、限定范围、给出可能原因：

```
underestimation was observed for samples above X
some confusion occurred between bare saline soil and built-up areas, possibly because of similar spectral responses
```

正面和负面的发现都要呈现。原因的展开放到讨论中。

## 7. 时态

| 内容 | 时态 |
|---|---|
| 图表"显示"什么 | 现在简单（*Fig. 4 shows…*） |
| 本研究观测或计算得到的结果 | 过去简单（*NDVI increased…*） |
| 模型或公式的属性 | 现在简单 |

## 8. 子标题

用信息型子标题，读者扫一眼就知道这一节发现了什么（先查目标期刊是否采用）：

- *Multi-source fusion reduces retrieval error by 18–31%*
- *Salinity is concentrated in low-lying oasis margins*
- *Human activities explain most of the 2000–2022 greening*

## 9. 常见问题

| 问题 | 修改 |
|---|---|
| 图表的文字翻译 | 走五步结构，突出最重要的信息和比较 |
| 把讨论写进结果 | 机制解释、文献对比移到讨论 |
| 念数 | 只报最值、对比、趋势，其余让读者看表 |
| 结论过强（*proves*） | *identifies*、*indicates* |
| 报喜不报忧 | 误差、失败的模型、不显著的区域也要报 |
| 结果顺序与方法、目标不对应 | 按方法顺序重排，并检查每个结果对应哪个目标 |

## 10. 自查清单

- [ ] 结果顺序与方法一致，每个结果对应一个研究目标
- [ ] 每段按五步结构：总起、关键信息与比较、说明什么、其他发现、小结与承接
- [ ] 精度验证结果和模型比较在结果中
- [ ] 与前人文献的比较留在讨论
- [ ] 评价靠幅度和对比，没有堆砌强调词
- [ ] 数字、单位、小数位、显著性标记全文一致，与图表一致
- [ ] 每张图表都被引用并有解读
- [ ] 负面或不完美的结果也已报告
