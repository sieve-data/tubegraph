---
title: Stochastic processes and financial modeling
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

Alexander Denev, a former PhD student in superstring theory, transitioned into finance, driven by a desire to apply practical, experimental approaches to real-world problems <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. His background in physics, which emphasized connecting mathematics and experimentation to the real world, found a surprising, yet fitting, application in the financial sector <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. He noted a "big wave" of physicists moving into finance, finding a growing field where their skills in mathematics and statistics were highly valued <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

### Core Mathematical Tools in Finance

For "quants" (quantitative analysts) in finance, a strong foundation in [[probabilistic_modeling_and_bayesian_frameworks | statistics and probability]] is essential <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Specifically, stochastic processes and stochastic differential equations were critical for tasks like derivative pricing at the beginning of the century <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. His physics background, which involved building pattern recognition tools in laboratories to make sense of observations and decisions, naturally translated to financial applications such as statistical classification and regression models for credit applications <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

### The Shift to Causal Reasoning in Finance

Denev realized that, unlike experimental sciences, economics and finance operate in a "messy" environment where controlled experiments and statistical repeatability are not possible <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>. Financial and economic theories are often not falsifiable, meaning they cannot be robustly inferred statistically <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

The 2008 financial crisis highlighted a major flaw in traditional financial [[risk_assessment_and_financial_crises | risk assessment]] <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. Measures like Value at Risk (VaR) relied on the assumption that conditions were stationary, allowing for the extraction of stable statistical patterns from historical data <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. However, the crisis demonstrated that distributions could suddenly change shape, making "sigma events" (rare, extreme events) occur with unexpected frequency <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. This led to many financial institutions failing <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

There was also a systemic incentive to misreport risk by using historical data that, while known to be unrepresentative, aligned with the desire to take more risk and earn bigger bonuses <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This "awakening," especially among regulators, spurred a need for different approaches <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.

The idea emerged to create forward-looking distributions, moving away from relying on stable historical data-generating processes <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. This meant aiming to be "approximately right" about future distributions, acknowledging subjectivity and approximation, rather than "precisely wrong" by using exact but irrelevant historical data <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.

This necessity led to a focus on [[causal_inference_in_finance | causal inference in finance]] <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. In finance, relationships are not always symmetric; for example, a crash in the S&P 500 will cause implied volatilities to spike, but a spike in implied volatilities does not necessarily mean a crash has occurred <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. This highlights the need for directional mechanisms, similar to how water causes mud but mud does not cause water <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

Causal models allow for reasoning in terms of probabilistic consequences, assigning probabilities to events and their impacts, even if not 100% certain <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>. This probabilistic setting captures the uncertainty within the system due to unmodeled background causes and changing contexts <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.

### Challenges and Benefits of Causal Models

One significant advantage of [[applications_of_bayesian_modeling_in_industry | causal models]], particularly graphical and Bayesian networks, is their transparency and auditability <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>. They provide a clear language for communication, allowing senior management to understand the underlying logic and contribute to brainstorming, fostering a "social model" that prepares institutions for various scenarios <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>.

Despite these benefits, Denev regrets that [[applications_of_bayesian_modeling_in_industry | causal models]] have largely failed to take over in finance and economics <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>. The reasons for this include:
*   The continued dominance of econometrics, which relies on historical data, and the reluctance of established professionals to change <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   Internal institutional resistance due to investments in existing methodologies, training, and software systems <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>.
*   Regulators' preference for "quick and dirty" stress tests using historical or high-level macroeconomic scenarios that lack context or narrative, rather than truly forward-looking causal models <a class="yt-timestamp" data-t="26:51:00">[26:51:00]</a>.
*   Misaligned incentives, where showing lower risk (even if inaccurately) was prioritized <a class="yt-timestamp" data-t="27:46:00">[27:46:00]</a>.

[[causal_modeling_challenges_in_macroeconomics | Causal modeling challenges in macroeconomics]] are particularly complex because of aggregated, low-frequency data, and pervasive feedback loops, making clear causal directions difficult to establish <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>. In such cases, a "hybrid picture" or "chain graphs" combining both causal (directed) and associational (undirected) relationships can be more useful, especially for modeling interventions in interconnected systems <a class="yt-timestamp" data-t="33:09:00">[33:09:00]</a>.

### Investment Strategies and Market Efficiency

Applying [[causal_inference_in_finance | causal models]] to investment strategies involves using forward-looking distributions to derive forward-looking correlation matrices based on causal considerations <a class="yt-timestamp" data-t="38:58:00">[38:58:00]</a>. This allows for building "causal efficient frontiers," optimizing returns for a given risk level based on future scenarios rather than historical patterns <a class="yt-timestamp" data-t="39:28:00">[39:28:00]</a>.

While markets are not "strongly efficient" (reflecting all possible information), they often incorporate more information than economists' average opinions <a class="yt-timestamp" data-t="49:57:00">[49:57:00]</a>. Building a relevant [[causal_inference_in_finance | causal model]] can help exploit market inefficiencies by providing more stable and robust results, as it aims to understand the underlying mechanisms generating these inefficiencies <a class="yt-timestamp" data-t="51:57:00">[51:57:00]</a>.

### Learning and the Future of Causality in Economics

For newcomers, Denev emphasizes the importance of:
*   **Understanding the Domain**: Knowing what you are modeling rather than just "crunching numbers" <a class="yt-timestamp" data-t="53:19:00">[53:19:00]</a>.
*   **Data Engineering and Programming**: Proficiency in languages like Python is a must <a class="yt-timestamp" data-t="55:26:00">[55:26:00]</a>.
*   **Machine Learning**: While important, it should build upon traditional knowledge and not disregard past methodologies <a class="yt-timestamp" data-t="56:32:00">[56:32:00]</a>.
*   **Continuous Learning and Interdisciplinary Thinking**: The field is constantly evolving, requiring adaptability <a class="yt-timestamp" data-t="57:32:00">[57:32:00]</a>.

The future of [[causal_inference_in_finance | causality]] in economics looks promising with the availability of more high-frequency data, which can help disentangle micro-causal structures <a class="yt-timestamp" data-t="43:00:00">[43:00:00]</a>. However, significant [[causal_modeling_challenges_in_macroeconomics | challenges]] remain, including dynamic structures, non-stationary distributions, and the immense computational power required for adaptive causal systems necessary for generalized artificial intelligence (AGI) <a class="yt-timestamp" data-t="44:21:00">[44:21:00]</a>.

Causal models are "scale specific," meaning that zooming in to a lower level of aggregation can reveal more stable causal structures that influence higher-level changes <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>. The growing number of publications and [[uncertainty_quantification_in_machine_learning | causal libraries]] in the software space indicate a strong interest and progress in the field <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>. Even without implementing explicit causal models, the shift towards thinking about problems having a structure that matters is changing the modeling culture for the better <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>.