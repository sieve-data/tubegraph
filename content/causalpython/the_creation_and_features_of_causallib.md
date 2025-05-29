---
title: The creation and features of CausalLib
videoId: Q7sinHrknC8
---

From: [[causalpython]] <br/> 

CausalLib is an [[open_source_causal_ai_libraries | open-source causal AI library]] created by Ehud Karavani, a research staff member at IBM Research <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The library was developed to address the unique challenges of [[causal_discovery_and_learning | causal inference]] compared to traditional machine learning, particularly the lack of ground truth labels for direct model evaluation <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Motivation and Initial Development

The development of CausalLib began when Ehud Karavani joined IBM Research and found scattered fragments of causal inference code across different projects <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Each project might have needed specific methods like IPW or S-learner, leading to copy-pasting and tweaking files without a coherent structure <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

Ehud, seeing the importance of building tools for others, started organizing these fragments into a consistent, coherent Python package <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. He designed it with a reasonable, scikit-learn-like API, combining functionalities from various sources to create a unified library for [[practical_applications_of_causal_methods | causal estimation methods]] that could be easily installed and passed around projects <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. The internal development of CausalLib began around early 2017 <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Recognizing its broader utility, the team decided to open-source CausalLib. This required navigating corporate bureaucracy and politics, which Ehud, then a student, successfully managed with the support of his mentor, Shai Shimoni <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This initiative was notable because, in 2017, the field of [[causal_ai_and_its_role_in_experiments | causal machine learning]] was still incredibly niche, with many foundational papers not yet published, and few existing software resources <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## Core Features and Modules

CausalLib is structured with several key modules:

*   **Estimation Module** <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
    *   Includes common [[practical_applications_of_causal_methods | causal inference]] models such as Inverse Probability Weighting (IPW), S-learner (referred to as standardization at the time), and T-learner (stratify standardization) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. The naming conventions for these models in CausalLib predate the 2019 Kunzel paper <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Survival Estimation Module** <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
    *   Designed for time-to-event analysis <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Evaluation Module** <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
    *   Addresses the fundamental problem of causal inference: the absence of ground truth labels for direct model evaluation <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   Initially driven by the need to visually convince stakeholders that the modeling process was sound, it features many graphical plots and colors for compelling presentations <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   Later, these graphical insights were converted into numeric values to enable automatic model selection <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   It tries to replicate scikit-learn's structure and includes a metrics module with compatible scores <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Feature Selection Module** <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
    *   Also mirrors scikit-learn, offering specific methods for confounder selection <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Contrib Module** <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>
    *   Contains more state-of-the-art models or those contributed by the community, which might not be as thoroughly tested as the core models <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

## Design Philosophy

CausalLib emphasizes **good code** and **modularity** <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>. Ehud believes that "the code is God" because it definitively shows what it does and how it does it, making it inseparable from science and crucial for gaining confidence in research conclusions <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>. Testing code is paramount as it leads to better design, allowing complex problems to be broken down into manageable components <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>.

This modular design offers several practical implications:

*   **Learning Aid**: Clean and simple code allows people new to [[causal_discovery_and_learning | causal inference methods]] to learn directly by examining the code <a class="yt-timestamp" data-t="00:41:28">[00:41:28]</a>.
*   **Scalability**: The modularity enables natural and easy scaling. Changing from a logistic regression to a gradient boosting tree model with hyperparameter tuning, for example, is a matter of changing a single word in the code <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.
*   **Component Reuse**: CausalLib allows users to easily reuse components, for instance, combining treatment and outcome models to create double-robust models, which helps in reducing residual confounding bias <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.
*   **Explicit Counterfactual Prediction**: While the underlying machinery might use regular regression or machine learning models, CausalLib makes the counterfactual prediction explicit. This helps users conceptually grasp the difference between what a regression model would do versus a counterfactual regression model <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.

## CausalLib's Impact and the Future of Causal AI

CausalLib aims to make [[causal_ai_and_its_role_in_experiments | causal inference]] more accessible to a broader public. Ehud notes that while [[open_source_causal_ai_libraries | excellent software]] and [[writing_and_maintaining_opensource_books_on_causality | learning resources]] are abundant today, a significant challenge remains in preparing raw data for causal analysis <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This often involves transforming event-based databases (like insurance claims or electronic health records) that were not originally created with research in mind <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

CausalLib's development aligns with the need for better tools in this data preparation phase, which requires significant causal knowledge to correctly identify covariates, time points, and establish concepts like "Time Zero" <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. An automated solution for this data pre-processing would be more beneficial than another causal inference methodology package <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

Ehud Karavani emphasizes that the biggest hurdle for machine learning researchers transitioning to [[causal_discovery_and_learning | causal inference]] is understanding "identification"—the realization that a "kitchen sink" approach of feeding all data to a model does not work <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>. Every causal problem has a specific structure that must be respected, and CausalLib helps to make this structure explicit and manageable within a software framework <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.