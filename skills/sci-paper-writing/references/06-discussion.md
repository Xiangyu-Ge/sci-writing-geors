# 06 · 讨论（Discussion）

讨论主要是解释数据的原因和意义。它通过与先前研究的比较得出解释，并回答引言中提出的具体问题和空白。这是审稿人最关注、也最容易出问题的部分。

## 1. 功能与组织

**功能**：

- 解释结果背后的原因和意义
- 通过与先前研究比较得出解释：讲清异同，解释为什么会这样，推断可能的原因
- 回答引言中提出的具体问题和空白（gap 段的 C 和三个目标）

**组织**：可以把分布在不同结果中的内容整合到一起讨论，也可以按结果和目标的逻辑来组织。

**与引言镜像**：引言中设下的每个 gap 和假说，讨论中都要兑现。

## 2. 结构：3–4 个小节

1. 主要讨论观点 1
2. 主要讨论观点 2
3. （可选）主要讨论观点 3
4. 研究的不确定性、局限与展望

写之前先确定"磁极"：本研究的主贡献是方法/精度、结果/制图、认知还是应用？所有小节都指向它。主贡献在摘要、引言末尾、讨论结尾都要出现。

## 3. 讨论段落的骨架

```
观点句 → 本研究的证据 → 与前人研究比较（相同与不同）→ 解释原因 → 意义或适用边界
```

**示范**（构造示例）：
> **[观点]** *The response of salinity to irrigation differed between heavily and lightly salinized oases.*
> **[证据]** *In Oasis A, salinity declined after drip irrigation was introduced, whereas in Oasis B it remained stable (Fig. 7).*
> **[比较]** *The decline agrees with field observations in other arid oases (refs), but the stable trend in Oasis B contrasts with reports of desalinization under drip irrigation elsewhere (refs).*
> **[原因]** *A likely explanation is the deeper groundwater table in Oasis B, which weakens capillary rise and limits the effect of reduced leaching.*
> **[边界]** *This suggests that the benefit of drip irrigation for salinity control depends on groundwater depth, a condition that should be considered before extending the result to other oases.*

## 4. 机理解释怎么展开

**地理学的两条主线：时间尺度、空间尺度**

- 结合已有研究讲清尺度效应和边界：结论在哪个尺度成立？换尺度会怎样？
- 推断可能的机理，同时考虑自然因素（气候、地形、水文、土壤）和人类活动因素（灌溉、政策、土地利用）
- 有异常、突变、滞后、阈值时，这些往往是讨论中最有价值的部分

**遥感反演类的光谱解释**

- 光谱响应机制：为什么这个波段或指数对目标属性敏感
- 敏感波段与吸收特征
- 辐射传输过程与遥感物理：饱和、混合像元、土壤湿度和粗糙度的干扰

**SHAP 与因果**：SHAP 结果是推断的依据，因果关系需要结合理论知识和文献来推断和解释（见 `04-validation-uncertainty.md` §4）。

## 5. 两类研究的讨论重点

**定量反演 / 模拟**：精度与前人和已有产品对比 → 误差来源（高值低估、饱和、混合像元、季节失配）→ 变量的物理机理 → 可迁移性 → 局限、展望与应用

**时空变化**：趋势与格局与前人对比（尺度、时段、数据差异）→ 驱动归因（自然 vs 人类活动及其机制）→ 格局的空间机制 → 归因方法的假设与不确定性 → 管理含义

讨论里"不同的发现"比"相同的发现"更有价值。与前人对比是为自己的发现定位，不是再综述一遍。每条分歧都要给出原因（研究区、时段、方法、尺度的差异）。

## 6. 语气匹配证据

**确定性梯度**

| 强度 | 句式 |
|---|---|
| 几乎确定 | *demonstrate / establish* |
| 强 | *show / confirm* |
| 中 | *indicate / support / are consistent with* |
| 弱 | *suggest / imply / point to the possibility* |
| 很弱 | *we speculate that* |

**归因表述阶梯**（同一发现，语气递减）：

1. *Irrigation expansion **caused** the greening.*（需要严格的因果证据）
2. *…**drove** the greening.*
3. *The greening **was largely attributable to** irrigation expansion.*（有归因分析时合适）
4. *The greening **was associated with** irrigation expansion.*（相关）
5. *The greening **may be partly explained by** irrigation expansion.*

两个高发问题：把相关写成因果；把本区结论说成普适规律。

**同时避免防御性写作**：核心结论用与证据相称的强度直接陈述；限定词只用在证据确实不足的地方，并说明不足来自哪里。见 `13-critical-writing-de-ai.md`。

## 7. 局限与展望

- 局限按方法、数据、理论三类主动写出，每条后面跟一句它对结论边界的影响
- 写缓解措施或为何结论仍然成立
- 展望要具体：哪个变量、哪套数据、哪类实验
- 不用 *further studies are needed* 收尾

```
A potential limitation is that... This may lead to... However,...
The attribution assumes a stationary climate–vegetation relationship, which may not hold under...
These results should be interpreted with caution in areas where...
```

## 8. 结果在讨论里怎么出现

讨论里可以、也必须用结果，但要把结果当论据：

- 不照搬数字，一句话概括（*the low retrieval error*）
- 不照搬图，引图号
- 按论证逻辑重组顺序
- 加上"为什么"和"意味着什么"

## 9. 时态

| 情景 | 时态 |
|---|---|
| 本研究的发现 | 过去简单（*We found that…*） |
| 普遍规律 | 现在简单（更强，风险更高） |
| 前人的具体发现 | 过去简单 / 现在完成 |
| 推测机制 | 现在简单 + 情态动词（*may be driven by*） |

## 10. 自查清单

- [ ] 3–4 个小节：2–3 个主要观点 + 不确定性、局限与展望
- [ ] 引言中的每个 gap 和目标都有回应
- [ ] 与前人文献的比较在讨论中，讲清了异同和原因
- [ ] 机理解释覆盖了时间尺度、空间尺度，兼顾自然与人类活动
- [ ] 反演类有光谱机制或遥感物理解释
- [ ] SHAP 结论有理论或文献支撑，没有写成因果
- [ ] 语气与证据强度匹配，没有防御性堆砌限定词
- [ ] 局限具体，说明了影响和缓解
- [ ] 不是结果的重复，也不是文献综述
- [ ] 结尾有明确的意义或管理含义
