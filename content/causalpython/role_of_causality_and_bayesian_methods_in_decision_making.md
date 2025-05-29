---
title: Role of causality and Bayesian methods in decision making
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

[[Causality and Causal Models | Causality]] is described as a fundamental framework for improving the [[causal inference and decision making | decision-making process]] in humanity <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Curiosity is a key component in this process <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores the role of [[causality in marketing and decisionmaking | causality]] and Bayesian methods, drawing insights from Dr. Juan Orus, a leading advocate for using [[causality in marketing and decisionmaking | causality in marketing]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Dr. Juan Orus's Journey into Causality

Dr. Juan Orus, born and raised in Bogotá, Colombia, initially pursued a PhD in geometric analysis <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After realizing that pure mathematics didn't bring him happiness, he transitioned to data science <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. He found data science interesting because it allowed him to apply his learned knowledge <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

His background in pure mathematics, particularly linear algebra, taught him how to approach and solve complex problems by breaking them down, which proved beneficial in applied contexts <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This perspective helps in tackling ill-defined problems and provides a strong foundational toolbox <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Similarly, his physics background instilled a tendency to model phenomena without overcomplicating them, starting simple and iteratively adding complexity <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

Dr. Orus realized the need for [[causality and machine learning | causality]] early in his career, especially when dealing with marketing analytics problems like media efficiency and budget optimization <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Traditional methods, such as throwing all variables into a linear regression model, often led to "torturing the data to get a story" and didn't feel natural <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. His turning point came from reading "Statistical Rethinking" by Richard McElreath, which, while primarily about Bayesian statistics, had a significant focus on [[causality and causal models | causality]], including concepts like DAGs and confounders <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. He saw [[causal inference and decision making | causality]] as a powerful tool to solve past problems <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Causality in Marketing and Business

Traditional marketing approaches, particularly in media mix modeling, often involve combining all data channels into a regression framework, assuming they compete against each other to determine ROI <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. However, this approach can lead to biased estimations due to the complex nature of the marketing funnel <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. For instance, channels like TV or paid social create awareness, while search acts as a mediator before final conversion <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Throwing all these into a single model can mask effects <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

A [[causal reasoning in decisionmaking | causal approach]], in contrast, requires identifying which channels and exogenous variables to include or exclude, essentially building a Directed Acyclic Graph (DAG) of assumptions <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This often means running multiple models and leaving certain channels out to get unbiased estimations of media efficiency <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### Role of Bayesian Methods

Dr. Orus highlights the value of the Bayesian framework for [[causality and causal models | causality]] <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>:
*   It forces explicit articulation of assumptions about the data generation process <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   It aids in understanding variability by setting up distributions and incorporating domain knowledge <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   It naturally supports simulations to demonstrate causal effects <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

### Communication and Iteration

Communicating complex [[causal inference and decision making | causal inference]] concepts to non-technical stakeholders, such as marketeers, is challenging <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Instead of pure theory, simulations are a great tool <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. By controlling the "truth" in a simulation, one can demonstrate how naive models can produce misleading results that lead to significant financial losses <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. This empirical evidence convinces stakeholders without delving into the intricate details of [[causal inference and decision making | causal inference]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

An iterative approach to problem-solving is also crucial <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. Starting with a simpler model, delivering quick results, and then iteratively adding complexity ensures speed and stakeholder buy-in <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. In industry, delivering results promptly is often more important than a "perfect" model a year later <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.

### Practical Applications: Geo-Lift and Synthetic Control

In marketing, methods like geo-lift are used to estimate counterfactuals when a controlled experiment (like an A/B test) is not feasible <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. For example, to estimate the impact of a TV campaign in Berlin, one might use a city like Hamburg as a proxy to simulate what conversions would have been without the campaign <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.

Using a DAG becomes very handy here, as it helps articulate the assumptions about city comparability <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>. Synthetic control methods can use multiple cities to create a better estimation of the counterfactual <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. These methods work surprisingly well and are often preferred over purely time-series-based counterfactuals (e.g., using a Bayesian time structure model), as they rely less on complex future predictions and allow for simpler models with better estimations <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.

### Model Evaluation

Evaluating [[causal models | causal models]] involves two components:
1.  **Estimation Process**: Evaluated using standard statistical techniques <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.
2.  **Causal Component**: Evaluated by testing the stability of estimates. This includes shuffling data, removing data, or adding an edge to the DAG that shouldn't affect the estimation if the arrows are placed correctly <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Cross-validations are performed to ensure the model isn't just estimating noise <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.

## Causal Reasoning Beyond Modeling

[[Causal reasoning in decisionmaking | Causal thinking]] is not just for modelers but should be widespread across industries <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. Anyone making decisions from data, like business analysts or marketing managers, implicitly thinks causally <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>. Without fundamental [[causality and causal models | causality]] knowledge, intuition can be misleading <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. For instance, filtering data by variables that act as colliders to a campaign could lead to contradictory results <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a>. Understanding basic [[causality and causal models | causality]] can prevent decision-makers from being "fooled by their intuition" <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

This concept is essential for humanity as it provides a framework for better [[importance of understanding causal inference for decision making | decision-making]] <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

### Human Capacity for Causal Thinking

While humans learn quickly, causal thinking is not always innate <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>. Dr. Orus shares an anecdote about his son initially associating putting on gloves with feeling cold, rather than gloves protecting from the cold <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>. It took repeated experience and iteration for his son to understand the correct causal direction <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>. This illustrates that [[causality and causal models | causality]] comes from experience and iteration, and even adults can be fooled by intuition because [[causality and causal models | causality]] is not trivial <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.

## Learning and the Future of Causality

For those starting with [[causality and machine learning | causality]], Dr. Orus recommends focusing on core concepts rather than immediately diving into specific software or complex estimation methods <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.

Recommended resources include:
*   "Statistical Rethinking" by Richard McElreath (for a Bayesian framework with [[causality and causal models | causality]]) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>
*   Books by Judea Pearl (for theory) <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>
*   "Causal Inference: The Brave and The True" by Matheus Facure (uses `statsmodels` for estimation, focusing on concepts) <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>

It's crucial to combine reading with hands-on coding and simulations to develop intuition <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. This includes generating examples, testing when assumptions break, and understanding how sensible the methods are to data distortions <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>. Maintaining a "childlike curiosity" and challenging what is read is key <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.

For aspiring machine learning or [[causality and machine learning | causality]] practitioners, the advice is to focus on fundamentals like linear algebra and probability theory, and solve concrete problems that genuinely interest them <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. Practical experience, even with basic data analysis tools, helps overcome anxiety and builds confidence <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.

Dr. Orus firmly believes [[causality and causal models | causality]] is not a trend but "fundamental for Humanity" <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. It is a framework for better [[causal inference and decision making | decision-making]] <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. To prevent it from fading out, more [[causal reasoning in decisionmaking | causal education]] and thinking are needed in the industry, treating it as a fundamental concept rather than just a hype or a tool <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.