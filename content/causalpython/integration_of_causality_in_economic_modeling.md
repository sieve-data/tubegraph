---
title: Integration of causality in economic modeling
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

## Introduction
Alexander Den, a former PhD in Superstring Theory who transitioned to finance, joins the Causal Bandits podcast to discuss the [[Integration of Causal Thinking in Machine Learning | integration of causal thinking in machine learning]], particularly in economics and finance. He shares insights on the limitations of traditional models and the potential of causal inference to provide more robust and transparent financial analysis <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Transition from Physics to Finance
Den's journey from theoretical physics to finance was driven by a desire for practicality and real-world application <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. While physics taught him to look for connections between mathematics and the real world, Superstring Theory pushed too far from experimentation for his liking <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>. He found finance, initially considered boring and political, could greatly benefit from mathematics and statistics <a class="yt-timestamp" data-t="02:54:33">[02:54:33]</a>.

Key mathematical tools useful in finance included:
*   **Statistics and Probability**: Basic understanding is essential <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   **Stochastic Processes and Differential Equations**: Crucial for derivative pricing, which was a major focus early in his career <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
*   **Pattern Recognition**: Early forms of machine learning were relevant for making decisions based on observations, especially in credit applications <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

Den observed a feeling of stagnation in theoretical physics compared to the growth and utility he felt in finance <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

## Limitations of Traditional Economic Models
A significant realization in economics is that, unlike experimental sciences such as physics, it lacks a controlled environment for repeatable experiments <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. Economic theories are often not falsifiable, meaning statistical repeatability is difficult to achieve due to dynamic environments and exogenous factors <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

Traditional financial risk measurement, such as Value at Risk (VaR), relied on the assumption of stationary or stable statistical patterns extracted from historical data <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. The 2008 financial crisis exposed the flaws in this approach. Events previously considered extremely rare ("Sigma events") began occurring daily, leading to the collapse of many financial institutions <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. This was compounded by incentives to misreport risk, as using historical data aligned with the goal of showing lower risk and taking on more for bigger bonuses <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.

## The Shift Towards Causal Thinking
The crisis prompted a "kind of Awakening" among regulators and practitioners that a different approach was needed <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. This led to the idea of creating **forward-looking distributions** instead of relying solely on stable historical data-generating processes <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. The question became: is it better to be approximately right or precisely wrong? Historical distributions offer precise, but often wrong, insights into the future <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. Future distributions, while involving approximation and subjectivity, offer a path to being "approximately right" <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.

[[Causality in AI | Causality]] comes into play because financial relationships are often asymmetric <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. For example, an S&P 500 crash spikes implied volatilities, but a spike in volatilities does not necessarily cause a crash <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>. This demonstrates the need for reasoning in directional mechanisms, where one event (cause) leads to consequences, but not vice-versa <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

This thinking aligns with Judea Pearl's probabilistic setting of causality, where relationships are not necessarily deterministic <a class="yt-timestamp" data-t="17:04:00">[01:03:15]</a>. Probability captures the uncertainty about certain details of the system and unmodeled background causes <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>. Economists already reason in terms of scenarios and competing narratives, making the encoding of this into a mathematical causal framework a natural progression <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.

## Benefits and Tools of Causal Models
Causal models, often implemented using graphical models or Bayesian networks, offer several advantages:
*   **Transparency and Auditability**: The explicit structure allows for clear understanding of cause-and-effect relationships <a class="yt-timestamp" data-t="22:29:00">[22:29:00]</a>.
*   **Improved Communication**: Models can be exposed to senior management, fostering discussion and incorporating diverse inputs <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>.
*   **Better Preparation**: By modeling different scenarios and hypotheses, organizations become better prepared, even if specific predictions are wrong <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>.
*   **Data Integration**: They can incorporate diverse data sources, from board meeting minutes to satellite images and news data <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>.
*   **Forward-Looking Risk Assessment**: By deriving a forward-looking joint probability distribution, causal models can generate a "forward-looking VaR" <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.
*   **Enhanced Investment Strategies**: In [[Causal inference in finance | finance]], causal models can be used to derive forward-looking correlation matrices based on causal considerations, improving portfolio optimization and the concept of an "efficient frontier" <a class="yt-timestamp" data-t="38:53:00">[38:53:00]</a>. This contrasts with traditional Markowitz theory that relies on historical distributions <a class="yt-timestamp" data-t="38:26:00">[38:26:00]</a>.

## Challenges in Adopting Causality in Finance
Despite the clear benefits, [[Challenges of implementing causality in research and industry | implementing causality in finance and economics]] has faced significant hurdles <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>:
*   **Incentives**: Financial institutions are often driven by incentives to maintain existing practices, even if they are suboptimal, especially if regulators don't explicitly demand change <a class="yt-timestamp" data-t="25:04:00">[25:04:00]</a>.
*   **Resistance to Change**: The dominance of econometrics and long-standing methodologies, coupled with significant investment in existing systems and training, creates resistance to new approaches <a class="yt-timestamp" data-t="26:12:00">[26:12:00]</a>.
*   **Regulatory Approach**: Post-crisis, regulators often implemented "quick and dirty" stress tests that rely on historical scenarios and macroeconomic aggregates, lacking coherent narrative or forward-looking context <a class="yt-timestamp" data-t="26:51:00">[26:51:00]</a>.

## Causality in Macroeconomics
Applying causality in macroeconomics presents specific challenges:
*   **Aggregated Measures**: Macroeconomic variables are aggregates, making it difficult to establish clear causal directions due to low-frequency data and feedback loops <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
*   **Lagging Indicators**: Macroeconomic variables often lag micro-level events. For instance, the 2008 financial crisis was caused by mismanagement and leverage at the institutional level, which then led to GDP falls and unemployment increases, not the other way around <a class="yt-timestamp" data-t="29:37:00">[29:37:00]</a>.
*   **Hybrid Models**: In macroeconomics, a hybrid approach combining causal and associational measures (e.g., Chain Graphs) might be more useful. This allows for modeling temporal causality alongside spatial separation in networks of agents or institutions <a class="yt-timestamp" data-t="33:09:00">[33:09:00]</a>. These models can be used to understand how interventions propagate through interconnected systems <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>.

## Future Outlook and [[Causality in AI | Challenges of Implementing Causality in Research and Industry]]
The increasing availability of high-frequency and granular data is crucial for disentangling micro-causal structures that are lost at higher levels of aggregation <a class="yt-timestamp" data-t="43:00:00">[43:00:00]</a>. However, challenges remain:
*   **Stability of Causal Links**: The stability of micro-causal links over time in dynamic economic environments is a concern <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>.
*   **Adaptive Causal Systems**: The "holy grail" of [[Causality in AI | AI]] is to build adaptive causal systems that continuously learn and adapt to changing data-generating processes <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   **Computational Power**: Learning causal models, especially discrete ones, is computationally intensive (NP-hard), requiring significant resources <a class="yt-timestamp" data-t="45:26:00">[45:26:00]</a>.

Despite these [[Challenges of implementing causality in research and industry | challenges]], there is growing awareness that integrating [[Causality in AI | causality in AI]] is essential for building truly universal and adaptive artificial intelligence systems, especially in economics <a class="yt-timestamp" data-t="45:54:00">[45:54:00]</a>. The concept that causal models are scale-specific implies that understanding micro-level interactions can explain changes in macro-level structures <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>.

## Causality and Market Efficiency
While the efficiency of markets is debatable, causal models can exploit inefficiencies more stably <a class="yt-timestamp" data-t="51:17:00">[51:17:00]</a>. Unlike associational relationships (e.g., Google searches for flu trends don't cause flu), causal mechanisms reflect the underlying process generating the inefficiency, leading to more robust and reliable results <a class="yt-timestamp" data-t="51:35:00">[51:35:00]</a>. Markets, while not perfectly efficient, often contain more predictive information than purely fundamental economic models <a class="yt-timestamp" data-t="50:33:00">[50:33:00]</a>.

## Advice for Learning Complex Fields
For those starting in complex fields like causality, machine learning, or finance, Alexander Den advises:
*   **Understand the Domain**: Deeply understand the subject matter you are modeling. For example, to predict inflation, one must understand economics, not just crunch numbers <a class="yt-timestamp" data-t="53:37:00">[53:37:00]</a>.
*   **Data and Programming Skills**: Data engineering and proficiency in programming languages like Python are essential <a class="yt-timestamp" data-t="55:26:00">[55:26:00]</a>.
*   **Machine Learning Knowledge**: Study excellent machine learning texts <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>.
*   **Build on the Past**: Do not disregard traditional models (e.g., econometrics, financial models). Leverage classical foundations to build new approaches <a class="yt-timestamp" data-t="56:53:00">[56:53:00]</a>.
*   **Continuous Learning and Patience**: The field is constantly evolving, requiring continuous learning and patience <a class="yt-timestamp" data-t="57:32:00">[57:32:00]</a>.

## Influences and Motivation
Alexander Den credits several key figures and books for influencing his thinking and career:
*   **Judea Pearl's "Causality" and "The Book of Why"**: These books profoundly changed his perspective from associational thinking to asking "why" <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.
*   **Ricardo Rebonato's "Coherent Stress Testing"**: The first book to introduce [[Causal inference in finance | causality in finance]] <a class="yt-timestamp" data-t="59:05:00">[59:05:00]</a>.
*   **Trevor Hastie, Robert Tibshirani, and Jerome Friedman's "The Elements of Statistical Learning"**: A foundational machine learning textbook <a class="yt-timestamp" data-t="59:26:00">[59:26:00]</a>.
*   **Kevin Murphy's "Machine Learning: A Probabilistic Perspective"**: Also covers directed and undirected graphical models <a class="yt-timestamp" data-t="59:34:00">[59:34:00]</a>.
*   **Daniel Amit**: His PhD supervisor, whose work on modeling brain functions and neural networks highlighted the value of cross-pollination between fields <a class="yt-timestamp" data-t="01:01:33">[01:01:33]</a>.

His motivation is driven by curiosity, a sense of purpose to make a meaningful contribution, and the desire to leave a mark on how people think about [[Causality in AI | causality]] in finance and economics <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. The podcast host, Alex, shares similar motivations, rooted in a desire to answer questions that correlational methods cannot address and to simplify the challenging learning journey for others in the [[Causality in AI | causality]] community <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. The exponential growth in [[Applications of generative modeling in causality | causal publications]] and software libraries (e.g., DoWhy, EconML) indicates a positive shift in the modeling culture towards understanding structure and its importance <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>.