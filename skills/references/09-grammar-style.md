# 09 · 语法与文风:时态、衔接、确定性、主被动

这是 SCI 写作的"暗规则"集合。规则少,但每一条都直接影响审稿人对论文的判断。

## 1. 时态选择:不是语法,是功能

**核心信念**:时态不是"对错"问题,是"意图"问题。每个时态都在告诉读者一件事——不要随机切换。

### 1.1 三大时态对应的核心功能

| 时态 | 例 | 传达 |
|---|---|---|
| **现在简单** | *X **affects** Y.* | 普遍真理 / 公认事实 / 永恒规律 |
| **过去简单** | *X **affected** Y in this study.* | 某次具体研究的结果 |
| **现在完成** | *X **has affected** Y.* | 累积至今的状态;与当下相关 |

### 1.2 三个时态的微妙差别

#### 现在简单 vs 过去简单

> *They **found** that the pressure **increased** as the temperature rose.*
> ↑ 只是这次研究里他们的发现

> *They **found** that the pressure **increases** as the temperature rises.*
> ↑ 他们发现的是一个普遍规律(更强)

#### 过去简单 vs 现在完成

> *I lived in Tokyo for 5 years.* → 已经不住了
> *I have lived in Tokyo for 5 years.* → 仍然住

但在 STEMM 里更微妙:

> *I broke my glasses.* → 描述过去事件(可能已修好)
> *I have broken my glasses.* → 现在状态(因此现在看不清)

**用在论文里**:

> *...effect of keratin **was demonstrated** over two years ago, ... little attention **was paid** to the selection of an alternative biocompatible material.*
> ↑ 当时关注少。**也许现在已经被关注。** 模棱两可,不利于论证空白。

> *...effect of keratin **was demonstrated** over two years ago, ... little attention **has been paid** to the selection of an alternative biocompatible material.*
> ↑ "到现在为止"关注仍然少 → **本文要解决的就是这个空白**。逻辑清晰。

**学术写作的常用模式**:用现在完成时把"过去的状态"拉到"当下",从而铺垫"本文要做什么"。

### 1.3 各章节默认时态(再速查)

| 章节 | 默认时态 |
|---|---|
| 引言 — 背景事实 | 现在简单 |
| 引言 — 前人工作具体发现 | 过去简单 / 现在完成 |
| 引言 — "至今仍然 X" | 现在完成 |
| 引言 — 本文做什么 | 现在简单 或 过去简单 |
| 方法 — 我们做的 | 过去简单 |
| 方法 — 标准流程 / 设备属性 | 现在简单 |
| 结果 — 我们观察到的 | 过去简单 |
| 结果 — 图表"显示的" | 现在简单 |
| 讨论 — 与文献对比 | 现在完成 / 过去简单 |
| 讨论 — 含义 / 推测 | 现在简单 + 模态动词 |
| 结论 — 本文做了什么 | 现在简单 / 现在完成 |
| 摘要 — 全文 | 混合,但**现在简单**比例较高 |

### 1.4 切换时态时,问自己

每次切换都要问:**为什么这里要换?读者能感受到我换的原因吗?**

如果你说不出原因 → **不要换**。

## 2. 主动 vs 被动

### 2.1 趋势

- 过去 30 年:被动占主流(*was measured, was observed*)
- 现在:主动越来越多,尤其在 CS、ML、生物医学顶刊
- 化学、材料、传统工程:仍以被动为主

让用户**核查目标期刊**(数 20 句方法中主动 vs 被动比例)。

### 2.2 被动的最大风险:丢失主权(ownership)

**Agentless passive**(无主体被动)看上去客观,实际上有歧义:

> *Samples were collected using a sterile swab.*
> ↑ 你做的?还是引用的?**搞不清**。

**审稿人最讨厌的就是搞不清**。

### 2.3 5 种被动场景 + 如何明确

| 场景 | 你想说 | 如何明确 |
|---|---|---|
| 1 | 我们在本研究做的 | 改主动:*We collected X*;或加 *here / in this study / in our procedure* |
| 2 | 我们引用的前人做的 | 加引文 + *in their work / in that study / using the method of* |
| 3 | 标准流程 / 业界惯例 | 现在简单 + 加 *using standard procedures / as in [ref]* |
| 4 | 通用属性(永久) | 现在简单 + 主语用设备 / 物质 | *The PENELOPE code simulates...* |
| 5 | 暧昧:某文献提到但没指明 | 慎用,最好查清后明确 |

### 2.4 隐形错误

❌ *A flexible section **is inserted** in the pipe.* (听起来是标准流程)
✅ *A flexible section **was inserted** in the pipe.* (清楚是本研究做的)

中文用户特别容易把"我做的事"用现在简单被动表达,因为中文里"在管道中插入一段柔性结构"既可以指自己做也可以指标准。

### 2.5 主动 vs 被动的快速决策

如果你能明确写出"谁做的",**主动通常更清晰**:

| 被动 | 主动(更好) |
|---|---|
| *It was found that...* | *We found that...* |
| *It is argued that...* | *We argue that...* / *Smith et al. argue that...* |
| *Theoretical modelling suggests...* | *Our theoretical modelling suggests...* |
| *Data were analyzed using SPSS.* | *We analyzed data using SPSS.* |

例外:**操作步骤的细节**(温度、时间等)被动更自然:

> *The mixture was heated to 80 °C for 2 h.* (没必要写 *We heated the mixture to 80 °C for 2 h*——主语显然是研究者)

### 2.6 "we" 的两种用法

```
We A (the authors):    "we collected the samples..."  →  指作者
We B (everyone):        "we now have a better understanding..."  →  指整个研究界
```

两者并用容易混淆。**避免**在同一篇论文里用 We B,改成:

❌ *We can now design proteins with new functions...* (我们?所有人?)
✅ *It is now possible to design proteins with new functions...*

---

## 3. 句间衔接

### 3.1 "危险地带":句号到下一个大写字母

读者在这里最容易跑神。你要"粘"住。

### 3.2 四种衔接武器

#### 武器 1:重复(overlap)

把上一句末尾的关键词重复到下一句开头。**简单、有效**。

> *...patterns that are characteristic of a deeply anesthetized brain and those that arise at the onset of **unconsciousness**. **Unconsciousness** can occur in tens of seconds...*

#### 武器 2:代词短语(pro-form)

```
This + 名词   These + 名词   Such + 名词
This method   These results   Such an approach
This finding  These data      Such conditions
This effect   These networks  Such systems
```

**铁律**:代词后跟的名词必须和上文**一致**。

❌ *...we used **a novel device**... **This method** is...*  ← device 改 method,读者搞不清是同一个东西吗
✅ *...we used **a novel device**... **This device** is...*  ← 保持一致

**单独的 It / They / This / These 风险高**——读者要花脑子去找指代:

❌ *This result was statistically significant and is in line with results in previous studies. **This** suggests that...*
> 这里 *This* 指"统计显著",还是"与文献一致",还是"两者"?不清楚。

✅ *...**This consistency with previous work** suggests that...*

#### 武器 3:分号(semicolon)合并

两个紧密相关、其中之一较短时:

> *The procedure usually takes many hours; this means that tests are rarely repeated.*

> *Simple pulse-echo signals usually consist of interfering reflections; these unwanted reflections are a source of coherent noise.*

> *Due to the small width of the crack, this electric field has a large gradient; this encourages electrons to leave the negatively charged crack face.*

注意:**用分号后整句不要太长**。总长超过 35 词就要拆。

#### 武器 4:信号词(signal connector)

详见 `08-vocabulary.md` 第 13 节。

**警告**:信号词是**emphatic**(强调性的)。每句开头都用 → 文章变得机械、急促。

**最佳实践**:**多用武器 1(重复) + 武器 2(代词短语)**,只在真正需要标记功能转折时才用信号词。

### 3.3 范例:一段中各种衔接武器混用

> General anesthesia is a drug-induced reversible coma commonly initiated by administering a large dose of a fast-acting drug to induce **unconsciousness** within seconds (1). **This state** can be maintained as long as needed to execute surgical and many nonsurgical procedures. One of the most widely used **anesthetics is propofol**, an i.v. drug that enhances GABAergic inhibitory input to neurons (2–4), with effects in cortex, thalamus, brainstem, and spinal cord (5–7). Despite the understanding of **propofol's** molecular actions, it is not clear how these effects at molecular targets affect single neurons and larger-scale neural circuits to produce **unconsciousness**.

注意:`unconsciousness` 重复 2 次,`anesthetic → propofol`,`propofol → This state / propofol's`。**完全没用信号词**,但句子之间无缝衔接。

---

## 4. 确定性连续谱(Certainty Continuum)

这是 SCI 写作最微妙、也最关键的一项技能。**语气强度必须匹配证据强度**。

### 4.1 从"绝对"到"几乎不确定"的 5 级

| 级 | 句式 | 例 |
|---|---|---|
| **5 · 绝对** | demonstrate / prove / establish | *We **prove** that X = Y.* |
| **4 · 强** | show / confirm / provide evidence | *Our results **show** that X causes Y.* |
| **3 · 中** | indicate / support / be consistent with | *These data **indicate that** X relates to Y.* |
| **2 · 弱** | suggest / imply / point to | *Our findings **suggest that** X may relate to Y.* |
| **1 · 推测** | speculate / it is tempting to suggest | *We **speculate that** X could relate to Y.* |

### 4.2 同一个发现的 5 个版本

```
We find that sunbathing causes cancer.                                                   (5 · 绝对)
We find that sunbathing may cause cancer.                                                (4 · 强但软化)
We find evidence to suggest that sunbathing may be related to cancer.                    (3 · 中)
It appears therefore that in some cases, sunbathing may have been related to             (2 · 弱)
  the onset of cancer.
The evidence points to the possibility that in some cases, excessive sunbathing          (1 · 推测)
  may have contributed to the onset of certain types of cancer.
```

### 4.3 中文用户最常见的偏差

**倾向于级 4-5**(中文论文里"证明""表明"用得多)。

→ 审稿人会要求 weaken 措辞,或要求补加证据。

**修正方法**:写完一句强论断后,问自己:
- 我的数据**真的能证明**(prove)吗?还是只能"提供证据"(provide evidence)?
- 我的结论对**所有情况**都成立吗?还是只在"某些条件下"?
- 加 *may, often, in some cases, under these conditions* 是否更准确?

### 4.4 风险降低语(risk-reducers)

往任何强论断里加入以下任意一种 → 风险降低:

#### a. "看起来"短语

```
it appears that...                  there is evidence to indicate that...
it seems that...                    the evidence points to...
it is reasonable to suppose that...  it is likely that...
it is plausible that...              it can be inferred that...
```

#### b. 频率限定

```
often, frequently, commonly, typically, usually,
in many / most / some cases, in virtually all cases
```

#### c. 数量限定

```
some, most, the majority of, a large proportion of,
in part, partly, in some / many cases
```

#### d. 模态动词

```
may, might, could, would, should
may possibly, might conceivably
```

### 4.5 实战:把"过强"修改为"刚好"

| 过强 | 刚好 |
|---|---|
| *Our method is the best.* | *Our method **performs favorably** compared with state-of-the-art baselines on the tested benchmarks.* |
| *X always causes Y.* | *X **typically** causes Y, **particularly in...** conditions.* |
| *This proves the hypothesis.* | *This **provides strong support for** the hypothesis.* |
| *No previous study has examined this.* | ***To our knowledge**, no previous study has examined this.* |
| *Our results show that X cures Y.* | *Our results **suggest that** X **may** be efficacious in treating Y, **although** larger trials are needed to confirm clinical utility.* |

### 4.6 但也不要太弱

中文用户矫枉过正后,可能写得过于含蓄:

❌ *Our results may possibly suggest that there might perhaps be some weak relationship between X and Y.* (堆叠 hedging,读者怀疑你自己都不信)

✅ *Our results suggest that X relates to Y.* (一次 hedging 就够)

**原则**:**hedging 不要叠加**。一句话里 hedge 一次足矣。

---

## 5. 段落的内部组织

### 5.1 段落必须有**单一功能**

**症状**:写到一半发现这段在讲两件事 → 拆成两段。

### 5.2 段落入口句(Topic sentence)

每段第一句应能让读者"看出这段要做什么"。**几种常见入口句模式**:

```
We now consider the connection between...           [介绍下一议题]
To address this question, we used...                [引入方法]
Taken together, these studies suggest that...        [小结]
There are two potential alternatives to such an approach...  [对比展开]
Several factors may explain this observation...     [引入解释]
A potential limitation of our approach is...        [转向局限]
```

避免开头就是 "It was found that..." 或直接 "Figure 3 shows...",这些是中间句的句式,不是入口。

### 5.3 段落长度

- 大多数 STEMM 期刊段落:**150-170 词**
- 一段超过 250 词:必拆
- 连续多个一两句的短段落:必合
- 例外:结论 / 摘要可以有更短的段

### 5.4 段间衔接

段尾的最后一句可以**铺垫下一段**:

> *...however, several aspects of the mechanism remain unclear, particularly **the role of temperature**.* ← 段尾
> ***The effect of temperature** was investigated by varying...* ← 下段首,自然衔接

---

## 6. 句子的内部组织

### 6.1 已知信息 → 新信息

**铁律**:句子开头先放"已知"(读者已经懂的),句尾放"新"(读者要学的)。

❌ *A novel mechanism was identified by us using single-cell sequencing, which reveals that...*
✅ *Using single-cell sequencing, we identified **a novel mechanism**, which reveals that...*  ← 新信息(mechanism)在中后段,便于下一句继续用 *This mechanism*

### 6.2 句长

- 平均句长:**20-26 词**
- < 20 词:90% 读者一遍理解
- > 40 词:**只有 10%** 一遍理解
- 连续 3 句长句:严重影响可读性

### 6.3 句子的"减肥"

复杂句的减肥技巧:

#### 技巧 1:删除"that 子句套娃"

❌ *We found that the results that were obtained showed that there was a significant effect that we observed.*
✅ *Our results showed a significant effect.*

#### 技巧 2:动词化名词

❌ *We **made the conclusion** that X **had the effect** of decreasing Y.*
✅ *We **concluded** that X **decreased** Y.*

#### 技巧 3:把 "There is/are" 换成主语

❌ *There are three factors that affect this process.*
✅ *Three factors affect this process.*

#### 技巧 4:删除冗词

```
应删除                       原句                  
in order to → to             
due to the fact that → because
in spite of the fact that → although
at this point in time → now
prior to → before
subsequent to → after
in the event that → if
the majority of → most
a large proportion of → many
a small number of → few
```

---

## 7. 主谓一致的隐形错误

### 7.1 主语和动词不挨着

❌ *The number of samples taken from the various sites and analyzed by mass spectrometry **were** consistent.*
✅ *The number of samples taken from the various sites and analyzed by mass spectrometry **was** consistent.*
> 主语是 *the number*(单数),不是 *samples*(复数)。

### 7.2 主谓"逻辑不可能"

❌ *The nature of the problem decided how to resolve it.*
> *the nature of a problem* 不能 *decide*——它是抽象概念,无主动性。

✅ *The nature of the problem determined how it was resolved.*

### 7.3 复合名词的真主语

复合名词里**最右边的名词**才是"真"名词,前面的都是修饰语:

```
An oil can opener repair technician training programme funding problem
                                                       └────────┘
                                                       真主语:problem
```

如果你的标题或主题是 5 个以上名词的串,**改写为"of"或"that"短语**。

---

## 8. 冠词:a vs the vs ∅

### 8.1 总览

| 冠词 | 用法 |
|---|---|
| **a / an** | 单数可数名词的"首次提及" |
| **the** | 已被提及 / 共识 / 唯一 |
| **∅(无冠词)** | 不可数名词 / 复数泛指 |

### 8.2 STEMM 写作里的常见困惑

#### a. 抽象不可数名词

```
research, equipment, evidence, information, software, knowledge, advice
```

**不能加复数 s,通常无冠词**。

❌ *We collected **researches** on...*
✅ *We **collected research** on... / We collected **studies** on...*

❌ *We developed **a software** to...*
✅ *We developed **software** to... / We developed **a software package** to...*

#### b. 该不该 the?

| 例 | 解读 |
|---|---|
| *We measured **temperature** in the sample.* | 测量"温度"这个量(无冠词) |
| *We measured **the temperature** of the sample.* | 测量这个样品的具体温度(特指) |
| *We measured **temperatures** at three points.* | 测了三个温度值(复数泛指) |

#### c. 中文用户常错点

```
❌ Steel is widely used in industry.   (这其实对!steel 不可数)
❌ The steel is widely used.            (错:不要无故加 the)

❌ Environment is changing.              (错:abstract 不可数也常加 the)
✅ The environment is changing.          (对:特指地球环境)

❌ Technology is developing quickly.     (单数不可数,可)
❌ Technologies are developing quickly.  (用复数表示"多种技术",也可)
```

#### d. 数值前的冠词

```
✅ a temperature of 80 °C
✅ a pressure of 2 atm
✅ a yield of 75%
```

数值用 *a* 而不是 *the*——表示"一个值",泛指。

---

## 9. 介词的隐形陷阱

### 9.1 同根动词的不同搭配

```
normalised FOR exon length
performed AT quasi-static rates
performed ON tissue samples
placed UNDER vacuum
based ON data
exposed TO radiation
correlated WITH temperature
correlation BETWEEN X and Y
focused ON / IN(化学结构常 "in")
```

**做法**:查 Google Scholar 看真实用法。在引号里搜 "performed at" 和 "performed on" 各自的频率。

### 9.2 用错介词改变意思

```
evidence OF X       =  X 的证据(X 确实存在)
evidence FOR X      =  支持 X 的证据(X 可能存在)

improved up to 3 times    =  最多提高了 3 倍
improved by up to 3 times  =  提高的幅度最多 3 倍(同义但更清楚)

interested IN X     =  对 X 感兴趣
interested OF X     =  ❌ 错
```

### 9.3 "with" 的歧义

`with` 是英文里最暧昧的介词之一:

> *We trained the model **with** GPUs.*
> ↑ 用 GPU 训练?和 GPU 同时训练?还是有 GPU 的模型?

**替代方案**(具体表达):

| with 替代 | 用法 |
|---|---|
| *using* | 工具 / 方法 |
| *having* | 拥有的属性 |
| *in combination with* | 联合 |
| *together with* | 伴随 |
| *as a result of* | 因为 |
| *at the same time as* | 同时 |

### 9.4 介词链的危险

❌ *We apply in this approach the concept of host rock to intrusive relationships through seismic-stratigraphic analysis with conventional biostratigraphic dating to constrain the timing of the events for the first time.*

读到末尾,读者已经迷失。**5 个以上介词短语堆叠时,拆句**。

### 9.5 "for the first time" 的位置

```
We used X-ray imaging to measure contact angles within oil-bearing rocks at reservoir conditions for the first time.
```

歧义:
- 第一次用 X-ray imaging?
- 第一次测 contact angles?
- 第一次在 oil-bearing rocks 中测?
- 第一次在 reservoir conditions 下测?

**修正**:把 *for the first time* 放在最贴近被修饰部分的位置,或拆句。

> *Here we present **the first measurements** of contact angles within oil-bearing rocks at reservoir conditions, using X-ray imaging.*

---

## 10. 副词位置改变意义

`only / just / simply / even` 这类副词的位置非常敏感。

| 句子 | 意义 |
|---|---|
| **Only we** analysed models that can simulate the response. | 只有我们一组人做了这个分析 |
| We **only** analysed models that can simulate the response. | 我们只做了分析(没做别的) |
| We analysed **only models** that can simulate the response. | 我们只分析了某些模型(其他类型没分析) |
| We analysed models that can **only** simulate the response. | 这些模型只能模拟响应(干不了别的) |
| We analysed models that can simulate **only the response**. | 模型只能模拟响应(其他参数不能) |
| We analysed models that can simulate the **only response**. | 模型能模拟唯一的那个响应 |

**铁律**:`only / just` 放在被它修饰的词**正前面**。中文里"只"的位置常常错,英文里这一错就改变意思。

---

## 11. -ing 形式的歧义陷阱

`-ing` 形式没有时态,没有单复数,没有主语——**天然模糊**。

### 11.1 典型歧义

> *The lipids can influence protein functions indirectly **altering** the biophysical properties of the membrane.*

`altering` 可能表达 10 种意思:

```
A   by [verb]ing
B   as a result of [verb]ing
C   on the basis of [verb]ing
D   when [verb]ing
E   thereby [verb]ing
F   therefore verbing
G   which is/are capable of [verb]ing
H   which/that [verb]
I   if we/it/they [verb]
J   because it/they [verb]
```

哪个意思?不清楚。读者要猜。

### 11.2 修正

✅ *The lipids can influence protein functions **by altering** the biophysical properties of the membrane.*
✅ *The lipids can influence protein functions, **thereby altering** the biophysical properties of the membrane.*
✅ *The lipids can influence protein functions, **which alters** the biophysical properties of the membrane.*

每种修改都给出不同的因果关系——但**都比原句清晰**。

### 11.3 实战例

❌ *MTCs are deposits resulting from creep, slide, slump and flow processes producing a variety of rheological units...*
> 谁在 producing?deposits 还是 processes?

✅ *MTCs are deposits that result from creep, slide, slump and flow processes. These processes produce a variety of rheological units...*

---

## 12. 弱动词清单(避免使用)

这些动词意思太多,读者必须猜:

```
get   → obtain, achieve, become, receive...
have  → possess, contain, include, exhibit...
keep  → retain, maintain, preserve, conserve...
make  → produce, generate, cause, create, perform...
do    → perform, conduct, carry out, execute...
spread → distribute, diffuse, scatter, extend...
bring → provide, yield, cause, introduce...
get into → enter, penetrate, enter into...
look at → examine, investigate, analyse, study...
```

**替换为具体动词**——更精确、更专业。

---

## 13. 词义的隐形错误

### 13.1 易混淆词对

| 词 | 意 | 例 |
|---|---|---|
| alternately | 交替地 | *We alternated between A and B.* |
| alternatively | 另一种方法 | *Alternatively, we could use B.* |
| beside | 在...旁边 | *Beside the lake.* |
| besides | 除了...还 | *Besides X, we also studied Y.* |
| criterion / criteria | 单数 / 复数 | *one criterion / several criteria* |
| phenomenon / phenomena | 单数 / 复数 | *one phenomenon / several phenomena* |
| different | 不一样的 | *X is different from Y.* |
| various | 多种 | *We tested various methods.* |
| effective | 有效(能起作用) | *The drug is effective.* |
| efficient | 高效(性价比好) | *The algorithm is efficient.* |
| adapt | 改造 / 修改 | *We adapted the protocol.* |
| adopt | 采用 / 选择 | *We adopted this approach.* |
| affect (v.) | 影响 | *Temperature affects yield.* |
| effect (n.) | 影响 | *the effect of temperature* |
| effect (v.) | 实施 / 引起 | *to effect a change* (少用) |
| imply | 暗示(发出方) | *His findings imply that...* |
| infer | 推论(接收方) | *We infer that...* |
| e.g. | 比如(举例) | *fruits, e.g., apples* |
| i.e. | 也就是说(改述) | *fruits, i.e., edible plant products* |
| comprise / consist of | 由...组成(所有部分) | *Water consists of H and O.* |
| include | 包括(选择部分) | *Examples include H and O.* |
| respectively | 按照前述顺序 | *A and B are 1 and 2, respectively.* |

### 13.2 连字符的差别

```
five centimetre-wide layers   = 5 个 1cm 宽的层
five-centimetre wide layers   = 每层都是 5cm 宽
```

**写复合形容词时,加连字符就成了一个整体修饰语**:

```
high-resolution image (✅)
high resolution image (歧义:high 修饰 resolution? 还是 high resolution 整体修饰 image?)
state-of-the-art method
real-time analysis
machine-learning-based approach
```

---

## 14. 标点的写作习惯

### 14.1 分号

```
Use 1: 连接两个相关短句
  Tests are time-consuming; they are rarely repeated.

Use 2: 在长列表中分隔有内部逗号的项
  We collected samples from Beijing, China; Tokyo, Japan; and Seoul, Korea.
```

### 14.2 冒号

```
Use 1: 在解释 / 列表之前
  Three factors are involved: temperature, pressure, and time.

Use 2: 标题中分隔主题和焦点
  GridSpice: a distributed simulation platform for the smart grid
```

### 14.3 破折号 — / em-dash

```
Use 1: 强调插入语
  The result — surprising at first — was confirmed by replication.

Use 2: 替代逗号 / 括号(更强的语气)
  Three factors — temperature, pressure, and time — affect this process.
```

⚠️ **破折号对国际读者不直观**。如果文章读者很国际化,**用括号 / 逗号替代**。

### 14.4 括号

```
Use: 补充信息(可选)
  The sample (n=25) was analyzed.
```

⚠️ **括号滥用是常见 tic**。规则:**如果内容重要,不该放括号;如果不重要,可能根本不该写**。

### 14.5 不要的标点

- **感叹号**(!):学术写作里不用。用 *strikingly, remarkably* 替代。
- **不必要的逗号**:简单主谓宾不要中间打逗号。

---

## 15. "中式英文"症状速查与修正

| 症状 | 修正 |
|---|---|
| *With the rapid development of...* | 删除,直接讲具体事 |
| *More and more researchers...* | *A growing number of studies have...* / *Recent research has...* |
| *In recent years, much attention has been paid to...* | *Recent studies have focused on...* |
| *As is known to all that...* | 删除,或 *It is well established that...* |
| *Researches show...* | *Studies show / Research shows...*(研究不可数) |
| *Make some experiments...* | *Conduct / Perform / Carry out experiments...* |
| *Get a good result* | *Achieve / Obtain a strong result* |
| *Very many studies* | *Numerous studies / A wealth of studies* |
| *Some experiments have proved that...* | *Previous studies have shown / suggest that...* (谨慎用 prove) |
| *In a word, ...* | *In summary / In short, ...* |
| *Last but not least, ...* | *Finally, ...* |
| *As a coin has two sides, ...* | 删除,直接说具体内容 |

---

## 16. 写作 tics(个人陋习)自查

很多写作者有自己不察觉的 tics。下面是中文用户高发的:

| Tic | 症状 | 修正 |
|---|---|---|
| 过度使用 "indeed / in fact" | 像在加重语气,实则空洞 | 删掉,看句子有没有损失;通常没损失 |
| 过度使用 "basically / essentially" | 空洞 | 删掉 |
| 过度使用 "clearly / obviously" | 暗示读者笨 | 删掉 |
| 过度使用 "very / so / really" | 形容词上的"补丁" | 用更强的形容词替代:*very important* → *crucial* |
| 句尾堆 prepositional phrases | 句子越走越长 | 用从句或拆句 |
| 滥用 "however" 在每段开头 | 段段都"然而",读者疲劳 | 多用重复 / 代词衔接 |
| 滥用 "it" 作主语 | 指代不明 | 用具体名词 |
| 滥用 "this" 单独出现 | 同上 | *this finding / this observation / this approach* |
| 滥用括号 / 破折号 | 显得碎片化 | 整合或删除 |
| 滥用动名词(-ing) | 语义歧义 | 改成 from clause |

写完一段后,**对自己的 tic 做一次"搜索式自查"**(Ctrl+F 查 *however, very, it, this, basically*)。

---

## 速查总表

| 我现在在改的问题 | 跳到 |
|---|---|
| 时态错乱 | §1 |
| 被动滥用 / ownership 丢失 | §2 |
| 句子衔接不流畅 | §3 |
| 语气太强 / 太弱 | §4 |
| 段落功能不清 | §5 |
| 句子太长 / 复杂 | §6 |
| 主谓不一致 | §7 |
| a/the 用错 | §8 |
| 介词错 | §9 |
| 副词位置 | §10 |
| -ing 歧义 | §11 |
| 弱动词 | §12 |
| 词义混淆 | §13 |
| 标点 | §14 |
| 中式英文 | §15 |
| 自己的写作陋习 | §16 |

---

## 17. ★ 地理 / 遥感写作的领域化语言要点

通用的时态、主被动、确定性规则都适用;以下是本领域(定量反演 + 时空变化)最常踩的几个专属点。

### 17.1 主权(ownership):分清"你做的反演/检测"还是"引用的方法"
无主体被动在遥感论文里尤其危险——读者分不清某个指数/方法是你提的还是前人的:
> ❌ *A salinity index was used and a random-forest model was trained.*(谁的指数?)
> ✅ *We computed the salinity index proposed by Khan et al. (2005) and trained a random-forest model.*
- 你的核心贡献(融合框架、建模、归因)→ 主动 *We developed / We fused / We attributed*
- 标准预处理(大气校正、滤波、采样)→ 被动 *Images were atmospherically corrected; samples were oven-dried*

### 17.2 "相关 ≠ 因果":归因表述的确定性阶梯
变化/归因研究最高发的雷区。看到两条曲线同步就写 *cause* 会被审稿人逼问因果证据。
```
强 caused / drove
中 was largely attributable to / was the dominant driver of   ← 有归因分析(残差趋势、地理探测器)时合适
稳 was associated with / coincided with / co-varied with       ← 只有相关时用
弱 may be partly explained by / may have contributed to
```
> ✅ *Residual trend analysis indicates that human activities **were the dominant driver** (71%) of the greening.*(有方法支撑,可中强)
> ✅ *The greening **was associated with** expanded irrigation.*(只观察到同步,用相关)

### 17.3 反演精度的表述:用数字,别用空形容词
> ❌ *Our model achieved high accuracy and good performance.*("high"多高?)
> ✅ *Our model achieved an R² of 0.81 and an RMSE of 2.3 dS/m, outperforming the optical-only model (R² = 0.64).*
- 精度词与证据匹配:R² 0.8+ 可说 *high/strong*;0.5–0.7 说 *moderate*;别给 0.5 的 R² 戴 *excellent*。
- 报告完整:给 R²**和**误差(RMSE/MAE)**和**验证方式(CV/独立集),缺一审稿人会问。

### 17.4 时态:反演/变化里的典型选择
- 你的采样、训练、反演、检测 → 过去简单(*We collected... We trained... NDVI increased...*)
- 指数公式、算法属性、地表物理规律 → 现在简单(*NDVI is defined as...; backscatter is sensitive to soil moisture*)
- 别把"本研究反演得到"写成现在简单,会变成"普遍规律",丢主权也夸大。

### 17.5 单位、精度、符号(一致性)
- 数值给单位:slope = 0.003 yr⁻¹;RMSE = 2.3 dS/m;resolution = 10 m。
- 时段用 en dash:2000–2022(不是 2000-2022 的 hyphen)。
- 数字与单位间空格:10 m, 30 m, 68 mm(°C 例外按期刊)。
- R² 两位小数、p 值 p < 0.05 全文统一;同一指标小数位一致。
- 术语一致:*Sentinel-2 imagery* 不要时而 *the optical data* 时而 *satellite scenes*;*soil salinity* 不要时而 *salt content*。

### 17.6 地理/遥感"中式英文"症状速查(补充 §15)
| 症状 | ❌ | ✅ |
|---|---|---|
| "随着…的发展"开篇 | *With the rapid development of RS...* | *Soil salinization affects over 1 billion ha worldwide...* |
| 研究区像地理课本 | 堆一堆无关地理事实 | 漏斗收敛到研究问题(盐渍化/退化) |
| 数据缺参数 | *We used Sentinel-2.* | *We used Sentinel-2 L2A (10 m, July 2022, atmospherically corrected).* |
| 精度空泛 | *high accuracy* | *R² = 0.81, RMSE = 2.3 dS/m* |
| 相关当因果 | *Precipitation decline caused degradation.* | *Degradation was associated with declining precipitation.* |
| 被动丢主权 | *A framework was developed.* | *We developed a framework.* |
| 术语漂移 | salinity / salt content / salinization level 混用 | 全文统一 *soil salinity* |
| 软件无版本 | *implemented in Python* | *implemented in Python 3.10 (scikit-learn v1.3)* |
