---
title: Causal AI and its role in experiments
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

[[Causal AI and its application in different sciences | Causal AI]] focuses on understanding cause-and-effect relationships, a crucial aspect for making informed decisions and predictions in a world of constant change <a class="yt-timestamp" data-t="02:49:52">[02:49:52]</a>. Unlike traditional machine learning that identifies correlations, [[causal_ai_and_machine_learning_intersection | Causal AI]] seeks to model the underlying causal mechanisms, enabling models to adapt when the environment changes <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## The Nature and Cost of Assumptions in [[Causal Reasoning in AI | Causal Inference]]

Assumptions in [[causal_reasoning_in_ai | causal inference]] are not binary (true or false) but exist on a spectrum, akin to a slider that can be adjusted <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. These assumptions are fundamental and necessary for performing [[causal_reasoning_in_ai | causal inference]] <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

### Cost of Assumptions
Every assumption comes with a cost <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>:
*   **Randomization (e.g., Clinical Trials)**: Considered the "best" assumption for achieving certainty about a causal effect <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>, but it is often very expensive, costing millions or even billions in industries like pharmaceuticals <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Observational Studies**: Assumptions here, like "no unmeasured confounding," might appear "free" as they are simply stated <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. However, they carry a significant risk of being wrong <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Purely observational data is "freaking cheap" <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

Investing in discussions and verification of assumptions for observational studies, such as those conducted at Harvard's Public Health School, can help reduce the risk of making incorrect assumptions, albeit at a financial cost <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. This highlights the "no free lunch" principle in statistics and machine learning <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

### Partial Identification and Causal Bounds
Instead of a binary "all or nothing" approach to [[causal_reasoning_in_ai | causal inference]], partial identification offers a more flexible perspective <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. This method, explored in the speaker's PhD work under Ricardo Silva, provides lower and upper bounds on the true causal effect rather than a single point estimate <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>, <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. As more assumptions are added, these bounds become tighter, eventually collapsing into a single point identification <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.

Partial identification is related to sensitivity analysis, which involves introducing a subjective parameter to see how results change <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>. While partial identification itself is not subjective by design, it can be combined with sensitivity analysis <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

## Experiments and Optimal Experimentation

Randomized Controlled Trials (RCTs) are powerful tools for understanding [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. However, they have limitations:
*   **Effect Heterogeneity**: RCTs may not fully capture how different individuals or units react to a treatment <a class="yt-timestamp" data-t="18:13:00">[18:13:13]</a>.
*   **Counterfactual Scenarios**: RCTs primarily inform about average treatment effects and struggle to answer counterfactual queries, which require even stronger assumptions beyond interventional data <a class="yt-timestamp" data-t="22:41:00">[22:41:00]</a>. Counterfactual data is generally rare, unless very specific studies like twin studies are conducted, which also come with their own assumptions and costs <a class="yt-timestamp" data-t="23:44:00">[23:44:00]</a>.

### The [[Causal Reasoning in Artificial Intelligence | Causal Hierarchy]]
The [[causal_reasoning_in_artificial_intelligence | causal hierarchy]] (or "ladder of [[causal_reasoning_in_ai | causality]]" as Pearl calls it) is a critical concept, clarifying the limitations of what can be inferred from different types of data <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>, <a class="yt-timestamp" data-t="21:31:00">[21:31:00]</a>.
*   **Level 1 (Association)**: Purely observational data can only reveal associations.
*   **Level 2 (Intervention)**: Making statements about interventions from observational data requires strong, often hard-to-defend, assumptions <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.
*   **Level 3 (Counterfactuals)**: Moving from interventional data (like RCTs) to counterfactual conclusions also requires additional, often very strong, assumptions <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>.

The cost of justifying assumptions increases significantly as one moves up the [[causal_reasoning_in_artificial_intelligence | causal hierarchy]] <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.

### Optimal Experimentation
[[Causal AI and its role in experiments | Optimal experimentation]] aims to intelligently select where to acquire the next data point or run the next experiment, rather than relying on random drilling or brute-force grid approaches <a class="yt-timestamp" data-t="50:50:00">[50:50:00]</a>. This approach is inspired by techniques like Kriging, used in resource exploration (e.g., finding gold pockets) <a class="yt-timestamp" data-t="51:50:00">[51:50:50]</a>.

Bayesian optimization is a method used in [[causal_ai_and_its_application_in_different_sciences | optimal experimentation]], where a predictor with uncertainty guides the decision for the next data acquisition point <a class="yt-timestamp" data-t="52:09:00">[52:09:00]</a>. This applies to both correlational and [[causal_reasoning_in_ai | causal analysis]] <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>.

## The Role of Expert Knowledge

Integrating expert knowledge is a main challenge and crucial aspect of [[causal_ai_and_its_application_in_different_sciences | optimal experimentation]] <a class="yt-timestamp" data-t="53:03:00">[53:03:00]</a>. Expert knowledge can help:
*   **Refine Surrogate Models**: Tune parameters in models used for predictions and experiment design <a class="yt-timestamp" data-t="53:14:00">[53:14:00]</a>.
*   **Limit Search Space**: Exclude physically nonsensical areas in the parameter space, similar to how it helps in [[root_cause_analysis_in_causal_ai | causal discovery]] by eliminating impossible edges in a graph <a class="yt-timestamp" data-t="55:48:00">[55:48:00]</a>, <a class="yt-timestamp" data-t="56:01:00">[56:01:00]</a>.
*   **Constrain Causal Bounds**: In methods like the [[causal_ai_and_machine_learning_intersection | causal marginal polytope]], expert knowledge about graph edges (directed or bidirected) can "slice" the polytope, making the bounds tighter and closer to the true causal effect <a class="yt-timestamp" data-t="57:46:00">[57:46:00]</a>.

However, acquiring expert knowledge also has a "cost," as a good expert might be expensive, and incorrect expert knowledge can lead to wrong assumptions <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>. Bayesian approaches can recover from wrong expert knowledge by collecting more true data, but this also incurs a cost <a class="yt-timestamp" data-t="58:27:00">[58:27:00]</a>.

## Practical Applications and Future Directions

The concept of representing synthetic control methods with Directed Acyclic Graphs (DAGs) was a key step in understanding their assumptions and providing non-parametric identification results <a class="yt-timestamp" data-t="34:30:00">[34:30:00]</a>. This approach was successfully applied at Spotify to estimate the causal impact of promotions on time series data, bridging econometrics and graphical models <a class="yt-timestamp" data-t="33:40:00">[33:40:00]</a>.

[[Causality in AI | Causality]] will continue to be a crucial aspect of the future <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>, as the fundamental relationship between cause and effect is undeniable <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. For those entering the field of [[causality_in_ai | causality]], it is advised to:
*   Read resources like Pearl's "Causal Primer" <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>.
*   Learn from practical examples <a class="yt-timestamp" data-t="01:17:23">[01:17:23]</a>.
*   Emphasize quality over quantity in understanding concepts, focusing on well-established methods like the instrumental variable model <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>.
*   Critically evaluate research, as not all published code or methods are fully verified <a class="yt-timestamp" data-t="01:17:53">[01:17:53]</a>.
*   "Erase your brain" about old statistical teachings that ignored [[causality_in_ai | causality]] and seek out good resources <a class="yt-timestamp" data-t="01:18:15">[01:18:15]</a>.

Jacob Sidler's key message to the [[causal_ai_and_machine_learning_intersection | Causal Python Community]] is to always question the cost of [[causal_ai_in_business_applications | causal assumptions]] <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>. While some assumptions are cheaper, others are very expensive. Researchers and practitioners should consider when experimentation is a good choice to verify results from observational studies, rather than relying solely on them <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>. By focusing on the cost of assumptions, one can make more justifiable and reliable statements <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.