---
title: Causal inference in drug repurposing
videoId: Q7sinHrknC8
---

From: [[causalpython]] <br/> 

## What is Drug Repurposing?
Drug repurposing involves taking existing drugs and finding new uses for them <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. This approach is favored by pharmaceutical companies because it shortens the typical drug discovery process <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. Since the drugs are already approved, they are known to be relatively safe, and the focus shifts to proving their efficacy for the new disease <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.

## Approaches to Drug Repurposing
There are various methods for drug repurposing <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>:
*   **Molecular Level**: This includes proteomics-level analysis to identify molecules that bind to target proteins and inhibit or excite their function <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>.
*   **Statistical Approach with Observational Data**: This method bypasses the need to find the specific molecular pathway or mechanism <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>. It involves using [[causal_inference_in_practical_applications | electronic health records]] or insurance claims data <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.

### Leveraging Observational Data with Causal Inference
In the statistical approach, researchers stratify patients with a specific disease, enumerate all the drugs they are taking, and then compare outcomes between those who took a particular drug and those who didn't <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. The main challenge is to ensure this comparison is unbiased and [[assumptions_in_causal_inference | de-confounded]], isolating the drug's true effect <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. This is where [[causal_inference_in_practical_applications | causal inference]] plays a crucial role <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.

## IBM's System for Drug Repurposing
At IBM, a system was developed for drug repurposing that takes a high-level, abstract configuration file, which physicians can even define <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>. This system then uses database querying to translate the configuration into matrices of confounders, treatment assignments, and outcomes <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. This processed data is then fed into a [[causal_inference_in_practical_applications | causal inference]] engine to estimate causal effects, such as survival differences or cumulative incidents under different drug regimes <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>.

### Challenges in High-Throughput Analysis
*   **Multiplicity Issue**: The system needs to enumerate hundreds of potential drug candidates, leading to a multiplicity issue that must be accounted for in the analysis <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
*   **Lack of Tailored Design**: It's not feasible to tailor a specific Directed Acyclic Graph (DAG) for each treatment-outcome pair when dealing with hundreds of candidates <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>.
*   **Data Richness**: There's a reliance on the data being rich enough to capture the internal state of patients, including diagnostics, tests, and previous prescriptions, to inform about their inherent health status <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
*   **Triangulation**: Results from observational analysis need to be triangulated with evidence from other sources to increase confidence in promising candidates <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

### Role of Large Language Models (LLMs)
LLMs, especially those grounded in knowledge bases like PubMed for medical publications, can assist in triangulating evidence <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>. If [[causal_inference_in_practical_applications | causal inference]] analysis suggests a drug's benefit, querying an LLM to find existing articles about its effectiveness (e.g., in mice) can reinforce trust in the candidate <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.

## Importance of Good Code
The code used in [[causal_inference_in_practical_applications | causal inference]] and scientific research is critical because it definitively shows what was done and how <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>. Good code contributes to trustworthy results and confidence in the methods <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>. Testing code not only ensures correctness but also leads to better code design and the ability to break down complex questions into components <a class="yt-timestamp" data-t="00:39:42">[00:39:42]</a>.

### Modularity in [[causal_inference_in_practical_applications | Causal Inference]] Libraries
A modular system like the calib library allows for:
*   **Learning**: People new to [[causal_inference_in_practical_applications | causal inference]] methods can learn by examining the clean and simple code <a class="yt-timestamp" data-t="00:41:25">[00:41:25]</a>.
*   **Scalability**: It enables natural and easy scaling, allowing complex models to be created easily by changing minor parameters <a class="yt-timestamp" data-t="00:41:38">[00:41:38]</a>.
*   **Component Reuse**: Components can be easily reused, for example, combining treatment and outcome modeling for double-robust models, which helps reduce residual confounding bias <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.