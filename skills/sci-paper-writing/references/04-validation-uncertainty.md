# 04 · 精度验证、不确定性与可解释性

验证设计是遥感和地理建模论文最容易在外审中被打回的环节。本文件说明三件事：验证怎么做、不确定性怎么报、SHAP 结果能说到哪一步。

## 1. 验证策略的选择

**本 skill 的默认立场**：

1. 独立验证集最好（单独采集、不参与建模的样点，或独立年份、独立区域的数据）
2. 没有独立验证集时，划分建模集和验证集的策略优于空间交叉验证
3. 空间交叉验证存在不足，有文献支持；写作时在方法中交代划分方式和理由，必要时引用文献回应审稿人

**文献中的争论**（审稿人可能站在任何一方，写作时要能回应）：

| 立场 | 代表文献 | 主张 |
|---|---|---|
| 支持空间 CV | Meyer et al. (2019)；Ploton et al. (2020) | 空间自相关下，随机 CV 会高估精度 |
| 反对空间 CV | Wadoux et al. (2021), Ecological Modelling | 空间 CV 缺乏理论基础，结果偏悲观；概率抽样的数据用常规 CV 即可；但样点强烈聚集时常规 CV 也有缺陷 |
| 折中 | Meyer & Pebesma (2021) 的适用区域（AOA） | 用预测变量空间的相异性指数划出模型的适用区域，只在该区域内声称 CV 精度；kNNDM 是较新的折中划分方法 |

**写作要点**：

- 说明样点是概率抽样还是目的性布点、是否空间聚集
- 说明划分方式（随机、分层、按区域、按年份）及比例
- 推到全区制图时，交代模型在哪里外推（例如给出 AOA 或预测变量覆盖范围）
- 被质疑时的回应思路：先说明采样设计，再引用 Wadoux et al. (2021) 说明独立验证或常规划分在该设计下的合理性，并补充一个敏感性分析（如按区域留出）

## 2. 精度指标

**连续变量（反演、模拟）**：R² + RMSE + MAE，土壤光谱常加 RPD，报告 bias（平均误差的正负说明系统性高估或低估）。

- 报告验证集指标，而不只是训练集
- 与简单基线（线性回归、单一指数、单传感器模型）比较
- 与已有数据产品或已发表结果比较，先说规律相似，再说提高了多少（见 `01-research-question.md` §1）
- 精度用词与数值匹配：R² = 0.5 不写 excellent

**分类与变化图**：遵循 Olofsson et al. (2014, RSE) 的良好实践，三部分是抽样设计、响应设计和分析。

- 用概率抽样（如分层随机抽样）选验证样本，而不是目的性抽样
- 按面积比例报告误差矩阵，给出总体精度、用户精度、生产者精度
- 给出精度和面积估计的置信区间
- 评估参考数据本身的误差："ground truth" 这个说法有误导性，参考数据也有不确定性
- 记录所有偏离良好实践的地方

审稿人常见的三类问题：用目的性抽样代替概率抽样；参考数据标注流程不规范；精度计算错误且不报置信区间。CEOS LPV 的土地覆盖精度评估协议（v1.1, 2025）是更新的参考。

## 3. 不确定性

数字土壤制图论文中，绝大多数做了验证，但只有约三分之一估算了不确定性。不确定性来源可分四类：观测数据、协变量、模型结构和参数。

至少给一种不确定性表达：

- 预测区间或分位数回归森林（QRF）
- bootstrap 重复建模得到的标准差图
- 预测区间覆盖率（PICP），用于检验不确定性估计本身是否可靠
- 误差的空间分布图

独立验证集样点少时，验证指标本身就有较大波动，解读时要谨慎。不确定性图与预测图并排展示，或在同一图中用透明度或分级表达。

## 4. 可解释性：SHAP 能说什么、不能说什么

**本 skill 的默认立场**：SHAP 结果是推断的依据；因果关系需要结合理论知识和文献来推断和解释。

SHAP 解释的是模型的行为，不是真实的数据生成过程。地学数据有三个特有风险：

- 强空间、时间和多变量相关，违背许多 SHAP 实现的特征独立假设
- 相关变量之间会互相"分走"贡献，导致重要性排序不稳定
- SHAP 值与回归系数不是一回事，不能当作效应量来讲

**写作规则**：

- 做 SHAP 前先处理共线性（相关阈值剪枝、VIF 或变量分组），并在方法中交代
- 结果中写 *the model relied most on…* / *was most sensitive to…*，而不是 *X drives Y*
- 讨论中从"模型重要性"过渡到"地学机制"时，用第二条证据链：物理过程、光谱响应机制、实测或文献
- 术语统一：方法输出叫 SHAP values，理论概念叫 Shapley values

**过渡句示范**（构造示例）：
> *SHAP analysis indicated that the model relied most on the SWIR-based salinity index. This is consistent with the absorption features of hydrated salts in the SWIR region (refs), which suggests that the index captured salt-related spectral variation rather than vegetation effects.*

一份 2026 年 EGUsphere 的作者回复里，作者接受审稿意见，把 SHAP 结果改述为模型解释工具而非直接的物理因果证据，并统一了 SHAP values 和 Shapley values 的用法。这是回复此类审稿意见的参考做法。

## 5. 机器学习类地理论文的自查清单

- [ ] 说明了为什么选这个模型，并与简单基线比较
- [ ] 超参数怎么确定的（网格搜索、贝叶斯优化、交叉验证）写清楚了
- [ ] 验证方案在方法中交代：独立验证集或建模/验证划分，划分方式和理由
- [ ] 没有数据泄漏：特征筛选、标准化、调参只在建模集上做
- [ ] 报告了验证集的 R²、RMSE、MAE（及 RPD、bias）
- [ ] 与已有产品或前人结果比较过
- [ ] 至少给了一种不确定性表达
- [ ] 做 SHAP 前处理了共线性
- [ ] SHAP 结论有理论或文献的第二条证据，没有写成因果
- [ ] 讨论了模型的适用范围和可迁移性

## 来源

- Olofsson, P. et al. (2014). Good practices for estimating area and assessing accuracy of land change. Remote Sensing of Environment, 148, 42–57
- CEOS WGCV LPV (2025). Land Cover and Change Map Accuracy Assessment and Area Estimation Good Practices Protocol, v1.1
- Wadoux, A. M. J.-C. et al. (2021). Spatial cross-validation is not the right way to evaluate map accuracy. Ecological Modelling, 457, 109692
- Meyer, H., & Pebesma, E. (2021). Predicting into unknown space? Estimating the area of applicability of spatial prediction models. Methods in Ecology and Evolution, 12, 1620–1633
- Ploton, P. et al. (2020). Spatial validation reveals poor predictive performance of large-scale ecological mapping models. Nature Communications, 11, 4540
- Piikki, K. et al. (2021). Perspectives on validation in digital soil mapping of continuous attributes — a review. Soil Use and Management
- Interpreting and evaluating digital soil mapping prediction uncertainty (Geoderma 450, 117052, 2024)
- Explainable AI in spatial analysis (arXiv 2505.00591)
