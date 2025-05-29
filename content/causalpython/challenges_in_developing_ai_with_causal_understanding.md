---
title: Challenges in developing AI with causal understanding
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

Developing artificial intelligence (AI) with a deep understanding of [[causality_in_ai | causality]] presents numerous challenges, extending beyond mere modeling to encompass data, assumptions, and ethical considerations <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Limitations of Current AI in Critical Fields

A significant challenge arises when considering AI applications in critical fields like medical imaging. A 2016 prediction by Jeffrey Hinton suggested that deep learning would surpass human radiologists within five years <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. However, this has not materialized, primarily because a radiologist's job involves more than just identifying lesions or measuring features <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Decision-Making and Complex Associations
Radiologists excel at decision-making, evaluating images, and identifying subtle, seemingly irrelevant associations that are crucial for accurate diagnoses <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Current deep learning systems struggle to learn these complex associations <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The human brain, with years of medical training, possesses an irreplaceable deep knowledge that allows for these critical judgments <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Trust, Ethics, and Legal Accountability
Making life-and-death decisions, as doctors and radiologists do, requires a level of robustness and trust that current ML systems have not yet achieved <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Beyond technical limitations, there are significant legal and ethical considerations: if an AI makes a wrong diagnosis, who is to blame – the model, the company, or the doctor who used it? <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> Society has not yet progressed to a point where AI systems can fully replace human medical professionals <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. The goal, therefore, should be to provide radiologists with better tools to enhance their efficiency and accuracy, rather than replacing them <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## Technical Challenges

### Data Quality and Representativeness
A fundamental technical challenge lies in acquiring good, high-quality, and representative data <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. In the medical field, this is particularly difficult. For example, during the early stages of the COVID-19 pandemic, some AI tools for detection were built on biased datasets where positive cases came from X-rays in China and negative cases from Stanford, effectively training a classifier to distinguish between hospitals rather than disease <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

Furthermore, medical imaging modalities like ultrasounds or MRIs can show variations even from the same machine in different hospitals due to varying usage practices <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. These "unobserved confounding elements" affect the output image and, consequently, the diagnosis <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Addressing this requires thinking about data in a [[causality_in_ai | causal way]], considering which parameters influence data collection <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. [[causality_in_ai | Causality]] should be integrated throughout the entire system-building process, from data collection to modeling and robust implementation <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Managing and Explicitly Stating Assumptions
All models, whether [[causal_modeling_and_ai | causal]] or not, are built upon assumptions <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. The challenge is not avoiding assumptions, which is "practically impossible," but rather making them explicit and testable <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. A key problem in broader machine learning, especially with large non-parametric models, is "forgetting some assumptions" that still underlie these models <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

[[causal_discovery_and_inference_in_ai | Causal inference]], while criticized for relying on assumptions, explicitly states them, making them transparent for testing, challenging, and discussion <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. An example of a forgotten assumption is the belief that models operate in Euclidean latent spaces, whereas some models actually build highly complex Riemannian manifolds <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Challenging such assumptions has led to [[advancements_in_causal_modeling_and_ai | advancements in causal modeling and AI]], such as hyperbolic machine learning models <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Robustness and Generalization
For AI systems to be robust and generalize well, particularly in critical applications, it's essential to remember and account for their underlying assumptions <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. Models must be made robust, ensuring they are not relying on "spurious correlations" that could lead to failure <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

At Spotify, for instance, researchers adapted a synthetic control estimator and incorporated sensitivity analysis to challenge assumptions in real-world problems <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. This approach aims to understand when models would fail and under what circumstances, thereby creating a more robust system <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Addressing Criticisms of Causal AI

Some critics argue that [[causal_reasoning_in_artificial_intelligence | causal inference]] is in its early years and rendered useless by its reliance on assumptions <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. However, proponents point to decades of successful practice and literature in fields like econometrics and epidemiology, where [[advancements_in_causal_modeling_and_ai | causal methods]] are extensively used <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Many concepts applied in computer science today, such as the monotonicity constraint used for identifiability, derive directly from epidemiology <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.

[[causal_reasoning_in_ai | Causal thinking]] is not just a modeling tool but a fundamental "way of reasoning" about problems <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. Even without building a 100% causal model, employing [[causal_ai_and_machine_learning_intersection | causal reasoning]] – by considering what could affect outcomes and controlling for variables – leads to better models <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.

While acknowledging that models can fail (e.g., ChatGPT's hallucinations), the key is to make assumptions explicit so they can be tested, allowing practitioners to understand when a tool is appropriate <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. [[causal_modeling_and_ai | Causal modeling]] is not a "Panacea," but a valuable tool for many circumstances <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

## The Importance of Causal Discovery

[[causal_discovery_and_inference_in_ai | Causal Discovery]] is considered a "better riddle" than [[causal_discovery_and_inference_in_ai | causal inference]] because it's more challenging and exciting <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>. While [[causal_discovery_and_inference_in_ai | causal inference]] assumes knowledge of the causal graph (DAG), [[causal_discovery_and_inference_in_ai | causal discovery]] attempts to identify these causal connections from data, often without complete prior knowledge <a class="yt-timestamp" data-t="00:43:23">[00:43:23]</a>.

An example of the need for [[causal_discovery_and_inference_in_ai | causal discovery]] comes from impurities in the ionosphere affecting GNSS (Global Navigation Satellite System) signals. While the causes of these impurities are well understood near the poles, their occurrence around the equator remains a troubling mystery, requiring the discovery of new physical causal relationships <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. Similarly, in medicine, understanding a radiologist's decision-making process requires discovering the underlying causal links in their minds, often from observational data <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>.

[[causal_discovery_and_inference_in_ai | Causal discovery]] is seen as true science because it involves exploring the unknown and attempting to understand *why* things happen <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>. This drive for exploration is innate in human nature and essential for scientific progress <a class="yt-timestamp" data-t="00:48:14">[00:48:14]</a>.

## Investment in Causal Research

If given a billion dollars for [[advancements_in_causal_modeling_and_ai | causal research]], a significant portion (75%) would be invested in [[causal_discovery_and_inference_in_ai | causal discovery]] efforts across all imaginable fields of science and technology <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>. The remaining 25% would go towards education about [[causal_reasoning_in_ai | causality]] <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. Recognizing [[causality_in_ai | causality]] and being skeptical of spurious correlations can not only help science and technology but also improve society by fostering more accurate and logical thinking <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.