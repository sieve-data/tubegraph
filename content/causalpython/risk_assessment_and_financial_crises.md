---
title: Risk assessment and financial crises
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

The world of finance, particularly in the context of risk assessment, has faced significant challenges, especially highlighted by the 2008 financial crisis. This period exposed fundamental flaws in how risk was measured and managed, leading to a re-evaluation of traditional models and a push towards more robust, forward-looking approaches, notably incorporating [[Causal inference in finance | causal inference]].

## Historical Flaws in Risk Assessment
Prior to the 2008 financial crisis, the financial system exhibited severe misalignments of incentives. There was a strong motivation to "misreport risk" by using historical data, even though many knew this data was not representative of future conditions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach was aligned with incentives to take on more risk, generate more money, and earn larger bonuses, often with little regard for future consequences <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

Traditional financial measurement theories heavily relied on the concept of statistical repeatability, assuming that markets were almost stationary and that stable statistical patterns could be extracted <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This implied a stable data-generating process without external interventions <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

A prime example was the widely cherished risk measure, Value at Risk (VaR) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. VaR aimed to construct a statistical distribution of a portfolio's movement, allowing for the measurement of different percentiles, like the extreme one percentile, to determine required capital <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. However, this 1-percentile risk was derived from a distribution assumed to be stable <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## The 2008 Financial Crisis: An Awakening
The 2008 financial crisis revealed the profound limitations of these models <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Events previously considered "Sigma events" (very rare, one-in-100-year occurrences) began happening "very very often," even on a daily basis <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This led to numerous financial institutions going "busted" <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

Practitioners, even without deep mathematical backgrounds, understood that VaR had limitations but continued to use it because it suited their incentives by showing lower risk <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This period served as an "Awakening" for regulators, prompting the realization that "something different needed to be done" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Shift Towards Forward-Looking Risk Assessment
The crisis spurred an idea to create "forward-looking distributions" instead of relying on stable historical data-generating processes <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This involves modeling the world with uncertainty in a [[stochastic_processes_and_financial_modeling | stochastic setting]] to embrace how things can evolve <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

The core dilemma became: Is it better to be "approximately right or precisely wrong?" <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a> Using historical distributions can be "precisely wrong" because the future is unlikely to be a repetition of the past <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Building future distributions, while involving approximation and subjectivity, offers the chance to be "approximately right" <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

This approach acknowledges exogenous factors like:
*   **Black Swans**: Unpredictable, high-impact events (e.g., a meteorite falling on Earth) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   **Gray Swans**: Events that are known to be going to happen, but their outcomes are uncertain (e.g., political elections, referendums like Brexit, or geopolitical conflicts) <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

## The Role of [[Causal inference in finance | Causality]] in Risk Assessment
[[Causal inference in finance | Causality]] becomes vital because financial relationships are often asymmetric <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. For instance, a crash in the S&P 500 will cause implied volatilities to spike, but a spike in implied volatilities does not necessarily mean a crash has occurred <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

Economists already reason in terms of probabilities and uncertainty, using scenarios and competing narratives <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. The goal is to encode this thinking into a mathematical framework that reasons in terms of causes and effects rather than mere associations <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

[[Probabilistic modeling and Bayesian frameworks | Bayesian networks]] and graphical models, by leveraging conditional probabilities, allow for the derivation of a "joint probability distribution" that is forward-looking <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. This enables the calculation of a "forward-looking VaR" <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Unlike historical correlations, which fail during crises when assets move together (e.g., 2007-2008 or during high inflation) <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>, a forward-looking causal approach can provide more stable results reflecting the underlying mechanisms <a class="yt-timestamp" data-t="00:52:04">[00:52:04]</a>.

### Benefits of Causal Models
*   **Transparency and Auditability**: Causal models, particularly graphical models, make the structure more transparent, showing what causes what <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. This fosters discussion, allowing senior management to understand the thinking and provide input, creating a "social model" <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.
*   **Preparation for Scenarios**: The explicit hypothesis formation in [[Causal inference in finance | causal models]] means that even if a specific prediction is wrong, the preparation through considering different scenarios proves indispensable <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.
*   **Improved Investment Strategies**: By using forward-looking, causally derived correlation matrices, it's possible to build "causal efficient frontiers" for portfolio [[Optimization and Resource Allocation Strategies | optimization]], improving upon traditional Markowitz investment theses which rely on historical distributions <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

## Challenges in Implementing Causal Models
Despite their benefits, [[Causal inference in finance | causal models]] have "failed to take over in finance and in economics" <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.

### Reasons for Resistance:
*   **Dominance of Econometrics**: Econometrics, which relies on historical data, still dominates economics <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. Professionals in this field are reluctant to change to something new <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
*   **Institutional Inertia**: Institutions have invested heavily in existing methodologies, training, and software systems, creating resistance to change without a strong stimulus <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>.
*   **Regulatory Requirements**: Regulators, in the wake of the crisis, often mandated "quick and dirty" stress tests, sometimes providing incoherent or contradictory macroeconomic scenarios without narrative context <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. These often required replaying past stress scenarios, like the great financial crisis, which is not forward-looking as the world has changed <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. These misaligned incentives meant no strong push for innovation <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>.

### [[Causal modeling challenges in macroeconomics | Causal modeling challenges in macroeconomics]]:
*   **Scale and Aggregates**: Macroeconomics deals with aggregates (e.g., GDP, unemployment) that are often low-frequency measurements <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>. This makes it challenging to decide on causal directions, as macroeconomic variables can lag behind micro-level issues like mismanagement or leverage that actually cause crises <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.
*   **Feedback Loops**: Economic variables can have feedback loops, where one variable causes another, which in turn causes the first, making "pure established relationships" difficult to find <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.
*   **Hybrid Models**: Sometimes, it's better to have a hybrid picture, using [[Causal inference in finance | causality]] where possible (especially for exogenous events like weather or war) and associational measures where clear causal links are hard to establish, such as in macroeconomic equilibrium relationships <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>. Chain graphs, which mix directed (causal) and undirected (associational) relationships, can be useful for modeling interventions in interconnected systems <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

## Future Outlook and Remaining Challenges
The "holy grail" remains building a fully causal, structural model of the economy that is dynamic, up-to-date, and adaptive <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. While data availability (high-frequency, big data) is improving <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>, and [[Causal inference in fintech | causality]] in AI is gaining traction <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>, significant challenges persist:
*   **Dynamic Structures**: Economies are time-varying and subject to unpredictable exogenous shocks <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>. The stability of micro-causal links in finance and behavioral economics is also a concern <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>.
*   **Computational Power**: Discovering thousands of causal mechanisms between numerous data sources is computationally intensive (NP-hard for discrete models) <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
*   **Scale-Specificity**: [[Causal inference in finance | Causal models]] are scale-specific <a class="yt-timestamp" data-t="00:46:43">[00:46:43]</a>. Higher-level structural changes might be understood by zooming in on more stable causal structures at lower, more granular levels, which high-frequency data can help disentangle <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>.

The awareness that problems have structure and that this structure matters is changing modeling culture for the better <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>. Asking "why" is crucial, and understanding that conditional independence depends on feature selection (e.g., avoiding colliders or mediators) affects the generalizability of models <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>.

## Advice for Learning Complex Fields
For those entering complex fields like [[Causal inference in finance | causality]], machine learning, or finance:
*   **Understand the Domain**: It is crucial to understand what you are modeling <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>. This means reading extensively and understanding the underlying economics or financial principles <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.
*   **Leverage Existing Knowledge**: Build upon the "shoulders of giants" <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>. Do not disregard traditional models or econometric tests, as they provide a solid foundation <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>.
*   **Continuous Learning**: Be open to learning all the time, not just in depth but also across several domains <a class="yt-timestamp" data-t="00:57:32">[00:57:32]</a>.
*   **Technical Skills**: Proficiency in data engineering and programming languages like Python is a must <a class="yt-timestamp" data-t="00:55:26">[00:55:26]</a>.
*   **Patience**: Given the complexity, patience is key <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>. Tools like ChatGPT can assist with summarizing or coding, acting as "AI Giants" <a class="yt-timestamp" data-t="00:57:58">[00:57:58]</a>.

Notable books that have influenced this field include:
*   Judea Pearl's works, particularly "Causality" and "The Book of Why," which promote asking "why" questions <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.
*   Ricardo Rebonato's "Coherent Stress Testing," which was the first book to introduce [[Causal inference in finance | causality]] in finance <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>.
*   Hastie, Tibshirani, and Friedman's "Elements of Statistical Learning" for machine learning <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>.
*   Kevin Murphy's machine learning book, which discusses directed and undirected graphical models <a class="yt-timestamp" data-t="00:59:34">[00:59:34]</a>.