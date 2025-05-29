---
title: Machine learning and causal inference methodologies
videoId: Q7sinHrknC8
---

From: [[causalpython]] <br/> 

The intersection of [[machine_learning_and_causality | machine learning and causality]] is a dynamic field, with discussions around the challenges and opportunities for integrating these disciplines. While deep learning has revolutionized predictive modeling, its impact on [[causal inference and machine learning | causal inference]] has sometimes been seen as detrimental <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Challenges and Differences

A fundamental challenge in [[causal inference and machine learning | causal inference]] is the "fundamental problem of causal inference," meaning there are no ground truth labels for causal effects, making direct model evaluation difficult <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Unlike predictive [[causal_inference_and_machine_learning | machine learning]], where performance metrics like AUC are common, convincing stakeholders of a causal model's validity requires different approaches <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

The rise of deep learning, particularly post-2012, fostered an expectation that raw data could be fed into a model to "figure it out" automatically <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. However, [[causal discovery and inference in AI | causal identification]] and [[causal discovery and learning | causal discovery]] cannot be fully automated in this way; they always require metadata and rigorous understanding of the underlying data generating processes <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>. This contrasts with older [[machine learning versus causal models in business | machine learning]] approaches, like SVMs, which incentivized feature engineering and careful consideration of input data and temporal relations <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## The Role of Code and Software

Good code is considered essential in science and research because it is definitive and transparent about its operations <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. Today, empirical research is inseparable from computation and coding <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Confidence in research conclusions relies on confidence in the underlying code, making code testing crucial <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>. Designing testable code often leads to better-designed code and a deeper understanding of the research questions <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>.

## CausalLib: A Tool for Causal Inference

`CausalLib` is a Python package designed to provide a consistent and coherent framework for [[causal inference and machine learning | causal inference]] methods, particularly for causal estimation <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.

### Modules within CausalLib
`CausalLib` includes several key modules:
*   **Estimation Module**: Features common models like IPW (Inverse Probability Weighting), S-learner (standardization), and T-learner (stratified standardization) <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>.
*   **Survival Estimation Module**: For time-to-event analysis <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Evaluation Module**: Addresses the lack of ground truth labels in [[causal inference and machine learning | causal inference]] by providing graphical and numerical methods for model validation <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Metrics Module**: Offers scores compatible with components like grid search for automated model selection <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Feature Selection Module**: Includes methods specific to confounder selection <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Contrib Module**: Contains more state-of-the-art or community-contributed models <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

The design of `CausalLib` is modular, reflecting the different ways causal effects and counterfactual outcomes can be estimated <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. This modularity allows for natural scaling and easy reuse of components, facilitating the creation of complex models and helping to reduce residual confounding bias <a class="yt-timestamp" data-t="00:41:38">[00:41:38]</a>. It also helps users conceptually grasp the difference between a regression model and a counterfactual regression model <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>.

### Origins of CausalLib
`CausalLib` began at IBM Research around early 2017 <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. Initially, it was a way to organize scattered fragments of code from previous projects that needed [[causal inference and machine learning | causal inference]] methods <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. The developer, Ehud Karavani, organized these into a consistent Python package with a Sci-kit learn-like API, making it installable and reusable across projects <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Recognizing its broader utility, the team open-sourced it despite corporate bureaucracy <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

In 2017, when `CausalLib` was developed, the field of [[causal machine learning and causality | causal machine learning]] was still niche, with many foundational papers like those on double [[causal_inference_and_machine_learning | machine learning]] not yet published <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. Learning resources were limited and not digitized, often requiring a deep dive into complex theoretical texts like the Hernan and Robbins book, which was challenging for beginners <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

## Making Causal Inference More Accessible

Despite [[advances in causal machine learning research | advances in causal machine learning research]] and software, a major hurdle remains in making [[causal inference and machine learning | causal inference]] more accessible: **data preparation** <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Transforming raw data from diverse sources (like insurance claims, electronic health records, or website events) into a format suitable for causal analysis is complex <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. This process requires deep causal knowledge to select appropriate covariates, establish time zero, and define follow-up times <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. Tools that automate this data shaping and repurposing phase would significantly advance the field <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

## Practical Applications in Healthcare

Working on healthcare projects at IBM Research has highlighted the intricacies of real-world [[application of causal machine learning in medicine | causal machine learning]] endeavors.

### Understanding the Domain
The first step in any project is to deeply understand the domain <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This involves interviewing domain experts (e.g., doctors) to identify research questions, understand problem complexities, and determine necessary data <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. Extracting their knowledge and distilling it into a sensible structure for causal analysis, like a Directed Acyclic Graph (DAG), is a slow and complex process <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. For example, physicians often better understand treatment decision processes than outcome determinants <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.

### Drug Repurposing
Drug repurposing, finding new uses for existing drugs, is a promising area for [[causal_inference_and_machine_learning | causal inference]]. It bypasses much of the traditional drug discovery funnel because existing drugs are already approved and relatively safe <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>. By analyzing electronic health records or insurance claims, researchers can compare outcomes for patients who took a drug versus those who did not, using [[causal inference and machine learning | causal inference]] to de-confound the comparison and isolate the drug's effect <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

IBM developed a system for this, taking high-level configurations from physicians and translating them into data matrices for [[causal_inference_and_machine_learning | causal inference engines]] <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>. This high-throughput analysis, often comparing hundreds of drug candidates, requires robust data and sometimes approximations to avoid tailoring a specific DAG for each drug-outcome pair <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>. The results from observational studies, however, need **triangulation** with other sources (e.g., pre-clinical studies, molecular data) to build confidence <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Large Language Models (LLMs) trained on scientific literature could potentially assist in this triangulation by identifying relevant articles <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>.

### Challenges with Practitioners
Working with practitioners can present challenges:
*   **Communication Gap**: Distilling complex natural language knowledge into a formal causal structure (like a DAG) is a communication-heavy process <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.
*   **Disappointment**: Practitioners often come with high expectations based on popular science, hoping for an easy-to-use tool to "get causal effects" <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. They become disengaged when confronted with the necessary rigor, discussions about estimates, causal roadmaps, target trial emulation, and biases <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. They may perceive [[causal inference and machine learning | causal inference]] as a "bait and switch scheme" because the underlying machinery often uses standard regression or [[causal_inference_and_machine_learning | machine learning]] models, requiring careful thought about data structure rather than simply "letting the model figure it out" <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

## Advice for Aspiring Causal Inference Researchers

The hardest part for [[causal_inference_and_machine_learning | machine learning]] researchers transitioning to [[causal inference and machine learning | causal inference]] is understanding **identification** <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>. They must realize that the "kitchen sink approach" of dumping all data into a model and letting it decide does not work in causality <a class="yt-timestamp" data-t="00:50:39">[00:50:39]</a>. Each problem has an inherent structure that must be respected <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>. While resources for learning [[causal inference and machine learning | causal inference]] were limited in the past, there are now many more accessible books and tools available to help newcomers <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>.

## Conclusion

The [[integration of Causal Thinking in Machine Learning | integration of causal thinking in machine learning]] is evolving. While challenges remain, particularly in data preparation and managing stakeholder expectations, the development of robust, open-source software like `CausalLib` is making [[causal_ai_and_machine_learning_intersection | causal AI and machine learning intersection]] more accessible <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>. The emphasis on open science, transparent code, and a thoughtful approach to data analysis is crucial for building trustworthy scientific conclusions that can be built upon by the broader community <a class="yt-timestamp" data-t="00:44:08">[00:44:08]</a>.