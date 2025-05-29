---
title: Causal inference in finance
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

Causal inference, the process of determining cause-and-effect relationships, offers a powerful alternative to traditional statistical and associational methods in finance. This approach can lead to more robust risk management, improved investment strategies, and greater transparency in financial decision-making, particularly in dynamic and uncertain environments.

## From Physics to Finance: Alexander Den's Journey

Alexander Den, a guest on the Causal Bandits podcast, transitioned from a PhD in superstring theory to a career in finance <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. His background in physics, which emphasizes practicality, mathematics, statistics, and experimentation, prepared him for the financial world by teaching him to look for connections between mathematical concepts and the real world <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. While superstring theory moved too far from experimental validation for his preference, finance, particularly in its need to calculate risk based on behavioral patterns, offered an opportunity to apply his quantitative skills <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

Key mathematical tools found useful in finance included:
*   Basic statistics and probability <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   Stochastic processes and stochastic differential equations <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
*   Pattern recognition, a precursor to [[Machine learning and causal inference methodologies | machine learning]], for making sense of observations and decisions <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.
*   Statistical classification and regression models, especially for building credit applications <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

## The Shortcomings of Traditional Financial Models

Traditional financial models, particularly those for risk measurement like Value at Risk (VaR), heavily rely on the concept of statistical repeatability and the assumption that things are almost stationary <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. This implies a stable data-generating process without external interventions <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. However, the 2008 financial crisis exposed the flaws in this assumption <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>. Events previously considered "Sigma events" (very rare) began occurring frequently, leading to widespread financial institution failures <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

### Incentives and Misreporting Risk
During the financial crisis, there was an incentive for financial institutions to misreport risk by using historical data, even though many knew this data was not representative <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This was aligned with incentives to take more risk, make more money, and earn bigger bonuses <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### The Dynamic Nature of Economic Systems
Unlike experimental sciences like physics, economics is messy and not easily falsifiable, as experiments cannot be switched back and forth <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. The environment is not controlled, with constant exogenous factors and changing contexts <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. This means the concept of statistical repeatability does not apply because the environment cannot be fixed <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

## The Rise of Causal Thinking in Finance

Recognizing these limitations, Alexander Den and his supervisor, Ricardo Rebonato, explored creating forward-looking distributions instead of relying on stable historical data-generating processes <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. The core idea was to be "approximately right" with a future-oriented distribution, rather than "precisely wrong" with a historical one that is unlikely to repeat <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>.

### Asymmetry and Directional Mechanisms
In finance, relationships are not always symmetric <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>. For example, a crash in the S&P 500 will cause implied volatilities to spike, but a spike in implied volatilities does not necessarily mean a financial market crash has occurred <a class="yt-timestamp" data-t="15:10:00">[15:10:10]</a>. This highlights the need for directional reasoning, akin to understanding that water causes mud, but mud does not cause water <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>. Financial and geopolitical events unfold with causes and consequences <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.

### Probabilistic Causality
Financial models often reason in probabilistic terms due to the lack of a rich enough description of the system <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. Probability captures uncertainty about system details and background causes that cannot be modeled <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>. This aligns with a probabilistic setting of causality, rather than a deterministic "necessary conjunction" view <a class="yt-timestamp" data-t="17:03:00">[17:03:00]</a>.

### Advantages of Causal Models
[[Causal inference and machine learning | Causal models]], such as Bayesian networks or graphical models, offer several advantages:
*   **Transparency and Auditability**: The structure of causal models makes it clear what causes what, fostering discussion <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>.
*   **Communication**: They provide a clear language for explaining hypotheses about how the world works, even to senior management <a class="yt-timestamp" data-t="22:32:00">[22:32:00]</a>.
*   **Preparedness**: Explicitly defining hypotheses, even if they might be wrong, allows for clear correction when something goes awry <a class="yt-timestamp" data-t="22:18:00">[22:18:00]</a>. This preparation for different scenarios is indispensable <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>.

> "All plans in battles in battle turn to be useless but preparation will prove to be indispensable." <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>
> — General Eisenhower

## Challenges to Adopting Causal Models

Despite their benefits, [[causal inference in practical applications | causal models]] have not been widely adopted in finance and economics due to several factors:
*   **Entrenched Econometrics**: Econometrics, which relies on historical data, still dominates the field, and many long-time practitioners are reluctant to change <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   **Institutional Inertia**: Organizations have invested heavily in existing methodologies, training, and software systems, making change costly and difficult <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>.
*   **Regulatory Requirements**: Regulators often mandate backward-looking stress tests or scenarios that are not context-driven, such as replaying past crises, rather than focusing on forward-looking, narrative-based scenarios <a class="yt-timestamp" data-t="26:47:00">[26:47:00]</a>.
*   **Macroeconomic Complexity**: In macroeconomics, it is challenging to establish clear causal directions due to aggregates, low-frequency data, and feedback loops between variables <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>. For example, while oil prices clearly impact inflation, and interest rate hikes aim to lower inflation, this doesn't hold true for all economies or central banks <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>.

### Hybrid Models for Complex Systems
Sometimes, a hybrid approach is more useful, combining causality where possible with associational measures where clear causal links are hard to establish <a class="yt-timestamp" data-t="33:09:00">[33:09:00]</a>. [[Machine learning and causal inference methodologies | Markov networks]] or Markov random fields can model associational relationships between agents or institutions in a network <a class="yt-timestamp" data-t="33:22:00">[33:22:00]</a>.

**Chain graphs** are a type of hybrid model that combines directed (causal) and undirected (associational/spatial separation) relationships <a class="yt-timestamp" data-t="34:49:00">[34:49:00]</a>. These can be used to model interventions and how they propagate across large, interconnected systems, such as financial networks <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>. Despite their potential, applications of chain graphs remain few <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>.

## Causal Models in Investment Strategies

[[Causal inference and decision theory | Causal models]] can significantly impact investment strategies by enabling a forward-looking perspective. Once a joint probability distribution (a forward-looking data-generating process) is established based on a scenario, it can be used for various analyses <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.

### Enhancing Portfolio Optimization
The Markowitz investment thesis, which minimizes risk by maximizing returns through portfolio diversification, relies on historical distributions of asset variances and correlations <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>. However, by using forward-looking distributions derived from causal considerations, one can construct a forward-looking correlation matrix that is not purely associational <a class="yt-timestamp" data-t="39:03:00">[39:03:00]</a>. This allows for building [[causal inference and individual treatment effects | causal efficient frontiers]] that better reflect future risks and returns <a class="yt-timestamp" data-t="39:28:00">[39:28:00]</a>.

### Event-Driven vs. Structural Models
*   **Event-driven investment**: For investors focusing on micro-events, scenarios based on exogenous shocks (e.g., elections, geopolitical events) can be used to build forward-looking efficient frontiers <a class="yt-timestamp" data-t="40:00:00">[40:00:00]</a>.
*   **Structural causal models of the economy**: Building a purely macroeconomic and financial structural causal model remains a significant research problem <a class="yt-timestamp" data-t="40:46:00">[40:46:00]</a>. Challenges include the lack of clear directionality and the aggregate nature of macroeconomic measures <a class="yt-timestamp" data-t="40:32:00">[40:32:00]</a>.

## The Future of Causal AI in Finance

There is growing awareness that [[causal inference and machine learning | causal AI]] is crucial for building adaptive systems that can truly learn and adapt, especially in complex domains like economics and finance <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   **Data Availability**: The increasing availability of high-frequency and micro-level data can help disentangle micro-causal structures that are missed when looking at aggregated, lower-frequency data <a class="yt-timestamp" data-t="47:22:00">[47:22:00]</a>.
*   **Computational Power**: While learning causal models can be computationally intensive, especially for discrete models which are NP-hard, advancements in computational power are expected to drive progress <a class="yt-timestamp" data-t="45:50:00">[45:50:00]</a>.
*   **Scale-Specific Models**: [[Assumptions in causal inference | Causal models]] are often scale-specific. Understanding interactions at a lower, more stable causal level can explain changes in structure at higher aggregation levels <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>.

### Exploiting Market Inefficiencies
Building a relevant causal model can help exploit market inefficiencies by providing more stable and robust results <a class="yt-timestamp" data-t="51:17:00">[51:17:00]</a>. Unlike purely associational relationships that can break down (e.g., Google flu trends), a causal mechanism reflects the underlying process generating the inefficiency, offering a more reliable understanding of *why* something happens <a class="yt-timestamp" data-t="52:05:00">[52:05:00]</a>.

## Advice for Aspiring Professionals in Complex Fields

For those entering complex fields like [[causal_inference_in_fintech | causal inference in finance]] and [[Machine learning and causal inference methodologies | machine learning]], Alexander Den offers the following advice:
*   **Understand the Domain**: Deeply understand what you are modeling. This helps in selecting relevant variables and applying causal thinking, even if not using a fully fledged computational causal model <a class="yt-timestamp" data-t="53:16:00">[53:16:00]</a>.
*   **Master Technical Skills**: Proficiency in data engineering, programming (e.g., Python), and [[Machine learning and causal inference methodologies | machine learning]] is essential <a class="yt-timestamp" data-t="55:26:00">[55:26:00]</a>.
*   **Build on Classical Foundations**: Do not disregard traditional models and econometrics. Instead, build on the "shoulders of giants" to gain a solid base <a class="yt-timestamp" data-t="56:57:00">[56:57:00]</a>.
*   **Embrace Continuous Learning and Patience**: These fields are constantly evolving, requiring ongoing learning and patience to grasp all aspects <a class="yt-timestamp" data-t="57:32:00">[57:32:00]</a>.

Key influential books mentioned include:
*   Judea Pearl's "The Book of Why" for changing his perspective on asking "why" <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.
*   Ricardo Rebonato's "Coherent Stress Testing" for introducing [[causal_inference_in_fintech | causality in finance]] <a class="yt-timestamp" data-t="59:05:00">[59:05:00]</a>.
*   Hastie, Tibshirani, and Friedman's "Elements of Statistical Learning" and Kevin Murphy's machine learning book for foundational [[Machine learning and causal inference methodologies | machine learning]] knowledge <a class="yt-timestamp" data-t="59:26:00">[59:26:00]</a>.