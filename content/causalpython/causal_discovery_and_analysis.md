---
title: Causal Discovery and Analysis
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

[[Causal analysis and its importance|Causal analysis]] and [[causal_discovery_algorithms|causal discovery algorithms]] were key topics presented at the Clear conference on Causal Learning and Representation <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Researchers shared their work on applying these methods to various real-world problems, from climate science to robust system analysis and explainable AI.

## Causal Discovery in Climate Time Series

Kevin Blechschmidt, from the German Aerospace Center in Munich, focuses on applying [[causal_discovery_algorithms|causal discovery methods]] with climate time series <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### Research Focus
Blechschmidt presented a paper at the conference that utilized bootstrap aggregation to provide confidence measures for the edges outputted by [[time_series_causal_discovery|time series causal discovery methods]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Empirically, the aggregated graph resulting from bootstrap aggregation showed higher precision and recall compared to the baseline method tested <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Desired Impact
His work aims to foster applications of these methods with climate time series to better understand how climate processes are linked <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This understanding could help clarify how climate change impacts these processes within climate models and assess if climate models accurately represent these processes in historical data <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Key Learnings
A significant personal learning experience for Blechschmidt was collaborating with many people on a paper for the first time, learning the process of group paper writing and the review process <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Recommended Paper
Blechschmidt recommends a review paper by Gustavo Campfíl from the University of Valencia titled "Discovering Causal Relationships and Equations from Data" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This paper explains current methods to estimate relationships and equations from data, and presents opportunities and challenges in the domain, focusing on physical sciences <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Meaningful Causal Aggregation and Paradoxical Confounding

Utkarsh Dwivedi, a PhD student at UCL, presented work on "Meaningful Causal Aggregation and Paradoxical Confounding," completed during an internship at Amazon Research <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Research Focus
The work highlights a paradox in aggregated [[causal_analysis_and_its_importance|causal models]]: even confounding, a structural property of causal models, becomes ill-defined when considering ambiguous interventions on aggregated variables <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. An "ambiguous intervention" occurs because when intervening on an aggregated variable (e.g., "cleaning products sold"), there are many ways to realize that intervention at the micro-level (e.g., individual products with different prices) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

The researchers propose a "Natural Intervention" to mitigate this problem and generalize the observation to general causal graphs <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Desired Impact
Dwivedi aims to see more academic work analyzing the consequences of ambiguous interventions on aggregated variables, given that most real-world variables are aggregated <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. It would also be beneficial to develop methods that can learn a complete set of macro variables from data, summarizing the micro-model <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Recommended Paper
Dwivedi frequently refers to the paper "Multi-level Cause Effect Systems" by Christoph Kuppe, which focuses on learning sufficient macro variables for a specific model <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This paper has provided inspiration for understanding how to mitigate reward hacking in large models by considering transfers from lower-dimensional models <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

## Causal Assembly: Benchmarking Causal Discovery Algorithms

Konstantin Goebl, a PhD student at the Technical University of Munich and affiliated with Robert Bosch, presented "Causal Assembly," a tool designed to facilitate benchmarking for [[causal_discovery_algorithms]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Research Focus
Causal Assembly aims to fill a gap in the field by addressing issues in obtaining reasonably complex ground truth data for [[causal_discovery_algorithms]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The tool makes proprietary data publicly accessible via semi-synthetic data steps, ensuring that the data used for benchmarking adheres to the ground truth causal graph <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Advantages
The primary advantage is ensuring the accuracy of the ground truth causal structure for complex real data <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This prevents scenarios where an algorithm might be correct but appears wrong due to an inaccurate ground truth <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### Desired Impact
Goebl hopes his work facilitates progress in the field, making [[causal_discovery_algorithms]] more reliable and scalable to solve real-world problems <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### Recommended Paper
Goebl enjoyed a paper on nonlinear independent component analysis (ICA) by Hyvärinen and co-authors, particularly appreciating its readability despite complex proofs <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

## The Role of Causality in Explainable AI

Ojas B, from Munster Technological University in Ireland, discussed the impact of neighborhood on Explainable AI (XAI) frameworks and their ability to convey the sufficiency and necessity of features <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Research Focus
Ojas B's work defines and examines the concept of "explanandum," focusing on whether feature importance rankings from XAI frameworks like SHAP, LIME, or DICE accurately convey feature sufficiency and necessity <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. XAI frameworks are highly sensitive to the neighborhoods they use for explanations, and different neighborhoods can produce varied or even false explanations <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. Experiments showed that "outside-based neighborhoods" generally performed well in conveying sufficiency and necessity <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Relationship to Causality
Ojas B emphasizes that the domain of explainability should be "very very overlapping with causality," as "without causality it's kind of ambiguous to have explainability" <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. The research touched upon [[causal_analysis_and_its_importance|causal relationships]] by constructing medical workflows (e.g., which test follows which test) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

### Desired Impact
The research advocates for people to define a specific "explanandum" before evaluating XAI frameworks, experimenting with different neighborhoods to find the most relevant answers <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. This approach ensures that explanations are not just a "checkbox exercise" for ethical permissions but truly represent the model and aid stakeholders in decision-making <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

### Recommended Paper
Ojas B recommends the paper "Dear XAI Community," which highlights the need for standardization in explainable AI research, focusing on clear definitions and the importance of the "explanandum" <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## Formalizing Root Cause Analysis as a Causal Problem

Will Orchard, from the University of Cambridge, presented his work on root cause analysis, focusing on its formalization as a [[causal_analysis_and_its_importance|causal problem]] and its real-world application in areas like microservice-based applications <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

### Approach to Formalization
Existing root cause analysis works often do not approach the problem from a causal perspective, despite "cause" being in the name <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. Orchard's approach involves classifying existing methods based on the causal hierarchy (associational, interventional, or counterfactual questions) to provide a unifying causal description <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. He particularly focuses on the counterfactual approach to root cause analysis <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

### Main Challenges
Key challenges include determining the best way to formalize the problem to capture intuition accurately, and ensuring that the formalization works effectively in real-world scenarios <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. This requires engaging with engineers who work with the data and have developed their own heuristics for problem-solving <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

### Key Learnings
Orchard learned that the question "what is a root cause?" is a deep one, interconnected with other concepts in causality such as explainability, sufficiency, necessity, and the relationship between anomalous values and interventions <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Desired Impact
A significant impact Orchard hopes to see is the availability of standardized, publicly accessible datasets for evaluating root cause analysis methods <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. The current lack of such datasets leads to many methods being developed without a causal perspective and benchmarked against other methods using non-public simulated data <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. Public data sets are crucial for convincing people of the importance of [[causal_analysis_and_its_importance|causal approaches]] and understanding which approaches work in practice <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

### Recommended Paper
Orchard found score-based [[causal_discovery_algorithms_and_techniques|causal discovery methods]] that use the derivative of the log of probability to be inspiring <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. Specifically, he highlighted theoretical work on identifiability results and the use of score matching for [[causal_discovery_algorithms_and_techniques|causal discovery]], as well as work on using heavy-tailed distributions for [[causal_discovery_algorithms_and_techniques|causal discovery]] and identifiability <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.