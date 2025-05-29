---
title: Causal discovery and learning
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

[[causal_discovery_and_inference_in_ai | Causal Discovery]] and learning involve identifying and understanding cause-and-effect relationships from data <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This field was a central theme at the CLEAR conference on [[causal_discovery_and_inference_in_ai | Causal Learning]] and Representation <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Applications and Research Areas

### Climate Time Series Analysis
Kevin from the German Aerospace Center in Munich focuses on applying [[causal_discovery_and_inference_in_ai | causal discovery]] methods to climate time series <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

*   **Research Focus**: The work aims to better understand how climate processes are linked, how [[climate change]] impacts these processes, and if [[climate models]] accurately represent these processes in historical data <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Methodology**: A presented paper utilized bootstrap aggregation to provide confidence measures for edges outputted by time series [[causal_discovery_and_inference_in_ai | causal discovery]] methods <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Empirically, the aggregated graph from this method showed higher precision and recall compared to baseline methods <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Find the Work**: Search for "bootstrap aggregation for time series [[causal_discovery_and_inference_in_ai | causal discovery]]" on arXiv <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Recommended Reading**: "Discovering Causal Relationships and Equations from Data" by Gustavo Campelo from the University of Valencia <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This review paper covers current methods, opportunities, and challenges, with a focus on physical sciences <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Meaningful Causal Aggregation
Utan Drew, a PhD student at UCL and intern at Amazon Research, presented work on "Meaningful [[causal_discovery_and_inference_in_ai | Causal]] Aggregation and Paradoxical Confounding" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

*   **The Paradox**: When considering aggregated [[structural_causal_models_and_causal_discovery | causal models]], the property of confounding is not well-defined, especially with ambiguous interventions on aggregated variables <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   **Ambiguous Intervention**: This occurs when intervening on an aggregated variable (e.g., "cleaning products") where there are many ways to realize that intervention at a finer, micro-level (e.g., specific products with different prices) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Proposed Solution**: The concept of "Natural Intervention" can help mitigate this problem <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Real-World Impact**: Most variables of interest in real applications are aggregated <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. The work aims to encourage more analysis of ambiguous interventions and potentially enable learning a complete set of macro variables from data <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Find the Work**: Search for "Meaningful Causal Aggregation and Related Paradoxes" or Utan Drew's name <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Recommended Reading**: "Multi-level Cause Effect Systems" by Christoph Kummer, published around 2016 or 2017 <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This paper explores learning sufficient macro variables for a specific model <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Benchmarking Causal Discovery Algorithms
Constantine Gobler, a PhD student at Technical University of Munich and affiliated with Robert Bosch GmbH, presented "[[causal_discovery_algorithms_and_realworld_applications | Causal Assembly]]" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

*   **Purpose**: To facilitate the benchmarking of [[causal_discovery_algorithms_and_realworld_applications | causal discovery algorithms]] by addressing the challenge of obtaining reasonably complex ground truth data <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Approach**: The tool makes proprietary data publicly accessible via semi-synthetic data steps in a principled manner <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This ensures that the data used for benchmarking truly follows the ground truth [[structural_causal_models_and_causal_discovery | causal graph]] implemented in the Python library <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Advantage**: It prevents situations where an algorithm is correct but appears wrong due to an incorrect ground truth <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This is crucial where there's uncertainty about the ground truth [[structural_causal_models_and_causal_discovery | causal structure]] in complex real data <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Impact**: Aims to facilitate progress in the field, making [[causal_discovery_algorithms_and_realworld_applications | causal discovery]] more reliable and scalable to solve real-world problems <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Find the Work**: Search for "[[causal_discovery_algorithms_and_realworld_applications | Causal Assembly]]" <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Recommended Reading**: A paper on "nonlinear IA" by Hyvärinen <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Root Cause Analysis as a Causal Problem
Will Orchard from the University of Cambridge and Amazon, focused on formalizing root cause analysis as a [[causal_discovery_and_inference_in_ai | causal problem]] <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

*   **Formalization**: Existing root cause analysis works often don't approach the problem from a [[causal_discovery_and_inference_in_ai | causal perspective]] despite the name <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. His work attempts to classify existing methods according to the [[causal_discovery_and_inference_in_ai | causal hierarchy]] (associational, interventional, counterfactual questions) <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. The focus is on the counterfactual approach <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Challenges**:
    *   Formulating the right question to capture the intuition of a problem <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   Ensuring the formalization works in real-life problems, by collaborating with engineers <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
*   **Main Learning**: The question "what is a root cause?" is deeply interconnected with other [[causal_discovery_and_inference_in_ai | causality]] questions such as explainability, sufficiency, necessity, and the relationship between anomalous values and interventions <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Real-World Impact**: A significant lack of standardized datasets for evaluating root cause analysis methods exists <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. The goal is to provide publicly accessible datasets to convince people that [[causal_discovery_and_inference_in_ai | causal approaches]] are important and to understand which problem formalizations work best in practice <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   **Find the Work**: Twitter, arXiv paper, and a [[Git]] repository for the data set <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. Search for "Pet Shop data set Amazon" <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Recommended Reading**:
    *   Score-based [[causal_discovery_and_inference_in_ai | causal discovery]] methods, particularly theoretical work on identifiability results and using score matching <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   Work from NFP on using heavy-tailed distributions for [[causal_discovery_and_inference_in_ai | causal discovery]] and identifiability <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

## Relation to Explainable AI (XAI)
Ojas B, from Munster Technological University, works on the impact of neighborhood on Explainable AI (XAI) frameworks <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. While his primary domain is XAI, he acknowledges the strong overlap with [[causal_discovery_and_inference_in_ai | causality]] <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

*   **Key Concepts**: Sufficiency and necessity of features are fundamental blocks of any explanation <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **XAI Frameworks**: State-of-the-art frameworks like SHAP, LIME, and DICE were tested to see how their feature importance scores convey sufficiency and necessity <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. These frameworks are sensitive to the neighborhoods they use, and different neighborhoods can produce different explanations, potentially leading to false explanations <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Explanandum**: Users should define a specific "explanandum" (what exactly needs to be explained) and then test if XAI frameworks can convey that <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. Experimenting with different neighborhoods can help find the most relevant answers <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Impact**: To move beyond XAI as a "checkbox exercise" for ethical permissions <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. Clinicians, for example, need explanations to answer specific questions like "do I need to do further tests?" or "what is the next most important diagnostic test?" <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Recommended Reading**: "Dear XAI Community" <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This paper highlights the need for standardization in XAI, focusing on clear definitions and the importance of defining the audience and actionability of explanations <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

---
[!INFO] Conference:
The work presented at the CLEAR conference on [[causal_discovery_and_inference_in_ai | Causal Learning]] and Representation <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

---
[!NOTE] Core Principle:
Without [[causal_discovery_and_inference_in_ai | causality]], explainability becomes ambiguous <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.