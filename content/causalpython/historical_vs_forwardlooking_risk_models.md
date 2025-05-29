---
title: Historical vs forwardlooking risk models
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

The debate between historical and forward-looking risk models is central to financial risk management, particularly in the wake of the 2008 financial crisis. This discussion highlights how relying solely on past data can lead to significant misjudgments and offers a perspective on how [[Causal inference in finance | causal models]] can provide a more robust approach to understanding and managing risk.

## Limitations of Historical Risk Models

Historically, financial risk measurement has heavily relied on past data and the assumption of [[Machine learning versus causal models in business | statistical stationarity]] <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This approach assumes that financial conditions and the relationships between assets remain largely stable over time, allowing for the extraction of stable statistical patterns <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

A prime example is "Value at Risk" (VaR), a widely cherished measure in finance used to quantify portfolio risk <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. VaR calculates a statistical distribution of how a portfolio moves and identifies extreme percentiles, such as the 1% tail risk, which an institution must be able to withstand <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. However, this measure is derived from a distribution assumed to be stable <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### The 2008 Financial Crisis and its Aftermath

The 2008 financial crisis exposed the critical flaws in this backward-looking methodology. Events that were statistically predicted to be rare, like "Sigma events" (one in 100 years), began occurring frequently, sometimes daily <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. This led to numerous financial institutions collapsing <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

A significant issue was the incentive structure within financial institutions:
*   Many practitioners knew that historical data was not representative <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   However, using it allowed them to misreport risk, showing lower risk figures that aligned with their incentives to take more risk, make more money, and secure bigger bonuses <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   This created a situation where being "precisely wrong" (using precise historical distributions that didn't reflect future reality) was preferred over being "approximately right" (acknowledging future uncertainty) <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

Regulatory requirements, such as post-crisis stress testing, often mandated the use of past stress scenarios, effectively replaying history <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. This backward-looking approach fails to account for the evolving nature of the world, where past crises may not repeat in the same form <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>.

## The Promise of Forward-Looking (Causal) Risk Models

An alternative approach, championed by figures like Ricardo Rebonato, focuses on creating forward-looking distributions rather than relying on stable historical data-generating processes <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. These models aim to embrace how things can evolve under uncertainty, seeking to be "approximately right" about the future rather than "precisely wrong" by clinging to a potentially irrelevant past <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### Key Principles of Causal Models in Finance

*   **Asymmetric Relationships**: Causal models recognize that relationships in finance, like in nature, are often asymmetric. For instance, a stock market crash might cause implied volatilities to spike, but a spike in volatilities does not necessarily cause a crash <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   **Directional Mechanisms**: They reason in terms of "directional mechanisms," understanding that events unfold with causes and consequences <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Probabilistic Causality**: The influence of events is probabilistic, not deterministic, reflecting uncertainty about the system's details or unmodeled background causes <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Scenario-Based Reasoning**: They allow for reasoning about future scenarios, such as political elections, by assigning probabilities to potential outcomes based on quantitative measures (polls) and market information <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. This allows for thinking about "gray swans" – events that are likely to happen, even if their exact impact is uncertain <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   **Joint Probability Distribution**: By consistently modeling events and their probabilities in a causal framework (e.g., using Bayesian Networks), a forward-looking joint probability distribution can be derived <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This allows for querying future risk levels, and deriving forward-looking correlation matrices based on causal considerations <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Transparency and Auditability**: Causal graphical models offer transparency, making the underlying structure of causes and effects visible <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>. This fosters discussion among stakeholders, including senior management, allowing for diverse inputs and creating a "social model" for preparedness <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. As General Eisenhower noted, "all plans in battle turn to be useless but preparation will prove to be indispensable" <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

### [[Causal inference in finance | Applications of Causal Models in Finance]]

*   **Investment Strategies**: Causal models can enhance investment strategies by building "causal efficient frontiers." Instead of relying on historical correlations and variances, these frontiers use forward-looking distributions derived from causal considerations <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>.
*   **Micro Event-Driven Investing**: For investors focused on specific micro-events (e.g., election outcomes), causal scenarios can directly inform portfolio adjustments <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Understanding Inefficiencies**: By modeling the underlying mechanisms that generate market inefficiencies, causal models can provide more stable and reliable results than purely associational models, which are prone to breaking down (e.g., Google Flu Trends) <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

## Challenges and Future Outlook

Despite their advantages, [[Causal inference in finance | causal models]] have not yet been widely adopted in finance and economics <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>.

### Reasons for Reluctance:

*   **Resistance to Change**: The dominance of econometrics, which relies on historical data, and established methodologies within institutions create inertia <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
*   **Regulatory Frameworks**: Regulators often mandate backward-looking stress tests or provide macroeconomic scenarios that lack narrative context or causal coherence <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>.
*   **Macroeconomic Complexity**: In macroeconomics, causal direction can be hard to determine due to aggregated measures, low data frequency, and feedback loops (e.g., GDP changes lagging institutional defaults) <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. Identifying "pure established relationships" between macroeconomic aggregates is challenging <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
*   **[[Generative models and the future of AI | Dynamic Systems]]**: Financial and economic systems are highly dynamic, with continuously changing data-generating processes, making it difficult to infer stable causal mechanisms from data <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>.

### Integration and Future Development:

*   **Hybrid Models**: A promising approach involves hybrid models, which combine directed (causal) relationships with undirected (associational) relationships, such as chain graphs <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>. These can model interventions in complex, interconnected systems <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   **Data Availability**: The increasing availability of high-frequency and granular data (e.g., consumer surveys) can help disentangle micro-causal structures that are lost at lower aggregation levels <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>.
*   **[[Iterative approach in building causal models | Causal AI]]**: The growing field of [[Generative models and the future of AI | Causal AI]] aims to build adaptive systems that can continuously learn and adapt causal relationships, moving beyond purely associational deep learning models <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>. This is seen as a "holy grail" for building truly universal artificial intelligence that can be applied to complex domains like economics <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.
*   **Scale-Specific Models**: [[Generative models and the future of AI | Causal models]] are understood to be scale-specific <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>. Zooming in allows for the understanding of changes in structure at higher levels of aggregation as consequences of interactions at a more stable, lower level <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.
*   **Computational Challenges**: Learning causal models, especially discrete ones, can be computationally intensive, but increased computational power and data availability are paving the way for progress <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.

The shift towards forward-looking, [[Causal inference in finance | causal models]] represents a fundamental change in modeling culture, encouraging practitioners to ask "why" events happen and to understand the underlying mechanisms rather than merely observing associations <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>. This deeper understanding is crucial for building more robust and adaptive financial systems.