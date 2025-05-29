---
title: Tools and frameworks for causal analysis
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

[[Causal analysis and its importance | Causal analysis]] is presented as a fundamental framework for improving decision-making, emphasizing curiosity as a key component <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The core challenge in applying [[causal_discovery_and_analysis | causal analysis]] in industry, especially marketing, is the perceived complexity of the topic, which requires a structured conceptual framework <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Core Concepts and Methodologies

### Direct Acyclic Graphs (DAGs)
A central tool in [[causal_inference_concepts_and_applications | causal inference]] is the Direct Acyclic Graph (DAG) <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. DAGs allow for explicitly stating assumptions about the data generation process <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>, which is crucial for identifying causal relationships and avoiding biased estimations <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Thinking about a problem as a DAG makes the process more transparent <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a> and helps systematically determine the necessary model structure <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

The process of constructing a DAG involves identifying which channels and variables are direct causes of the target variable <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This contrasts with traditional approaches, like linear regression, where all available data or channels are often included, potentially leading to biased estimations due to mediator effects <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. For example, in marketing, throwing all channels into a regression model can lead to bias because some channels, like search, might act as mediators between initial touchpoints (e.g., TV, out-of-home) and final conversions <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

A key benefit of DAGs is that they force explicit assumption-making, which reveals potential limitations or infeasibility of estimations from observational data <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This helps in understanding the problem and domain more deeply <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.

### Bayesian Framework
The Bayesian framework is highly suitable for [[causal_inference_methods_and_applications | causal inference]] because it naturally forces the explicit statement of assumptions regarding the data generation process <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. It aids in understanding variance and variability by setting up distributions and incorporating domain knowledge <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This explicit assumption-making aligns well with [[causal_discovery_and_analysis | causal analysis]] by providing a natural way to think about data problems with a causal structure <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Simulations
Simulations are a powerful tool for communicating the value of a [[causal_discovery_and_analysis | causal approach]] to stakeholders, especially those less technical <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. By controlling the "truth" in a simulated environment, one can demonstrate how naive methods can lead to misleading or very wrong results, which could cause significant financial losses <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This hands-on demonstration helps convince non-technical audiences without delving into the intricate details of [[causal_inference_concepts_and_applications | causal inference]] concepts <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Quasiexperimental Methods (Geo-lift/Synthetic Control)
In marketing, "geo-lift" or synthetic control methods are used to estimate counterfactuals when a proper control group is unavailable <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. For example, to measure the impact of a TV campaign in Berlin without splitting the city, one might use a comparable city like Hamburg as a proxy for the counterfactual (what would have happened without the campaign) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.

While powerful, these methods are not a "silver bullet" <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>. They rely on assumptions, and a DAG can help determine if the chosen geographies are comparable and whether the assumptions hold <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>. The use of DAGs with quasiexperimental methods ensures transparency by forcing explicit assumptions about the data generation process, which is critical because quasiexperimental methods alone do not guarantee identification out of the box <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## Software and Libraries

While conceptual understanding is prioritized, practical implementation uses several tools:
*   **DoWhy** <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>
*   **EconML** <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>
*   **Statsmodels** (for estimation) <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>

## Overcoming Challenges

### Transition from Academia to Industry
The transition from pure mathematics to data science in an applied context can be challenging due to the shift from theoretical impact to real-world business problems <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. However, a background in pure mathematics, particularly linear algebra, provides a strong foundation for problem-solving by breaking down complex issues into smaller, manageable steps <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This foundational knowledge helps in tackling ill-defined problems and reduces intimidation <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Communicating Value to Stakeholders
Communicating the value of complex [[causal_inference_concepts_and_applications | causal concepts]] to non-technical stakeholders is best achieved through practical demonstrations, such as simulations, rather than pure theory <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. It is important to start with simpler models to deliver results quickly and iterate, adding complexity as needed to gain buy-in <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Model Evaluation
[[evaluating_causal_models_in_practice | Evaluating causal models]] involves assessing both the [[causal_discovery_and_analysis | causal structure]] (DAG) and the estimation process <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. Techniques for [[evaluating_causal_models_in_practice | causal model evaluation]] include:
*   **Stability testing:** Shuffling or removing data to check estimate stability <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.
*   **Edge manipulation:** Adding an edge to the graph that should not affect the estimation if the arrows are properly placed <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
*   **Cross-validation:** Essential for verifying that models are not merely estimating noise <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.
*   **Parallel testing:** Running Geo tests or uplift tests alongside media mix models to compare results <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

### Importance of Fundamentals
For newcomers to [[causal_inference_and_its_applications | causal inference]], it is essential to focus on fundamental concepts over specific software or trendy technologies <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. Understanding the core principles first ensures a strong base, preventing confusion later if issues arise <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. Foundational knowledge in linear algebra and probability theory is considered halfway to success <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

## Future Outlook

[[Causal analysis and its importance | Causality]] is viewed not as a mere trend but as fundamental for humanity and decision-making <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. There is a need for more [[causal_discovery_and_analysis | causal education]] and thinking in the industry to ensure it is treated as a core concept rather than a fleeting hype <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>. Causal reasoning is relevant for all decision-makers, not just modelers, as intuition can be misleading <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

### Intersection with Large Language Models (LLMs)
While still in early stages, LLMs show potential for boosting productivity through tools like GitHub Copilot, summarization, and automation <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. However, direct application in sensitive areas like marketing campaigns requires caution due to the risk of unexpected or harmful responses <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

## Recommended Learning Resources
*   **Statistical Rethinking by Richard McElreath:** Recommended for its focus on [[causal_inference_concepts_and_applications | causality]] within a Bayesian framework <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:45:12">[00:45:12]</a>.
*   **Pearl's book on Causality:** Good for understanding the theory <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>.
*   **Causal Inference: The Brave and the True by Matheus Facure:** Praised for building concepts and using `statsmodels` for estimation, focusing on structure over estimation method <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>, <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

Hands-on coding and simulations are crucial for grasping these concepts, allowing users to build intuition and test assumptions <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. It is beneficial to intentionally distort data or assumptions to understand the sensitivity of methods <a class="yt-timestamp" data-t="00:46:31">[00:46:31]</a>. Curiosity is key to navigating the field <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.