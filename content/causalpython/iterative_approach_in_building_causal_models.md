---
title: Iterative approach in building causal models
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

The development of [[structural_causal_models_and_causal_discovery | causal models]] often benefits from an iterative approach, particularly in real-world business settings <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This method contrasts with the idea of defining all parameters upfront and then performing computations <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## The Iterative Strategy

Instead of striving for a perfect model from the outset, the iterative approach suggests:
*   **Starting Small and Simple** It is a "good strategy" to begin with an "overly simplified" model that is reliable <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This initial simplicity helps build trust with stakeholders <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Iterating and Refining** The process involves continuously improving the model by triangulating its results with real-world data and incorporating more expert knowledge over time <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Providing Tangible Value Early** While starting simple, it's crucial to offer "something extra" to stakeholders to demonstrate value beyond what they already know from basic trends <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

Models may not be perfect initially but "eventually they do become" better as management trusts them and desires further improvements <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This approach encourages a mindset of "learning by doing" and applying causal thinking to existing [[machine_learning_and_causal_inference_methodologies | machine learning]] use cases <a class="yt-timestamp" data-t="00:56:58">[00:56:58]</a>.

## Integrating Expert Knowledge

A crucial aspect of iterative model building is the continuous integration of expert knowledge. This is particularly vital because:
*   **Reducing Human Biases** [[structural_causal_models_and_causal_discovery | Causal discovery]] methods help reduce human biases in understanding cause-and-effect relationships <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Validating Findings** Experts can validate the relationships identified by algorithms, correcting edges or even prompting new insights <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Capturing Tribal Knowledge** Interviewing experts allows for the creation of a "tribal knowledge graph," which can serve as a ground truth for testing [[structural_causal_models_and_causal_discovery | causal discovery]] algorithms <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **Building a Knowledge Monument** The graphical structure of [[structural_causal_models_and_causal_discovery | causal models]] can act as a "monument for the knowledge of people in the organization," preserving expertise even if individuals leave the company <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

It is recommended to interview multiple experts to mitigate individual biases <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a> and use methods like Multi-Criteria Decision Making (MCDM), such as AHP (Analytic Hierarchy Process) or TOPSIS, to ensure consistency and reduce bias in expert interviews <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

## The Role of Generative AI

[[applications_of_generative_modeling_in_causality | Generative AI]], particularly Large Language Models (LLMs), can significantly expedite the initial phase of [[structural_causal_models_and_causal_discovery | causal discovery]] <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.
*   **Efficiency Booster** Instead of starting from scratch with experts, LLMs can generate a preliminary [[structural_causal_models_and_causal_discovery | causal discovery]] graph based on available information <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>. This drastically reduces the time needed for initial knowledge gathering, as a few prompts can yield results very close to a human-derived ground truth <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **Motivation for Experts** Presenting a pre-built (even if imperfect) graph encourages experts to engage, criticize, and refine it, showcasing their unique knowledge and experiences <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. This dynamic interaction fosters trust in the models <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.
*   **Future Applications** The combination of causal AI and LLMs is seen as the future of dashboarding, enabling users to ask causal questions and receive quantifiable impacts directly from their applications <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>.

## Evaluation and Trust

Even in the [[evaluation_and_systematic_testing_of_causal_models | causal world]], [[challenges_in_evaluating_causal_models | evaluation]] remains a challenge <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>. However, the iterative approach makes the process more accessible to stakeholders:
*   **Visualizations and Simulations** [[structural_causal_models_and_causal_discovery | Causal discovery]] visualizations and the ability to run "what-if" (counterfactual) simulations build trust with management <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Stakeholder Involvement** The role of business experts is amplified in [[evaluation_and_systematic_testing_of_causal_models | evaluation]]. By involving them in the process, they see the model as an extension of their own knowledge, leading to greater acceptance and willingness to improve it <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.
*   **Beyond Metrics** While metrics like Hamming distance and number of indirect edges exist for [[structural_causal_models_and_causal_discovery | causal discovery]] methods, relying solely on numbers is insufficient. The business expert's validation and "makes sense" factor are paramount <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
*   **Addressing the "Fundamental Fear"** For those worried about the correctness of their causal graphs, the iterative process involving both metrics and continuous expert validation helps alleviate concerns <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>.

## Limitations and Future Directions

Even with iterative development, [[causal models]] have limitations, akin to scientific theories <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>. They are not ultimate solutions but rather embodiments of the scientific method <a class="yt-timestamp" data-t="00:53:41">[00:53:41]</a>. Challenges arise with unprecedented events like an "alien attack" where no expert knowledge or historical data exists <a class="yt-timestamp" data-t="00:49:44">[00:49:44]</a>.

However, advanced strategies can mitigate these:
*   **Sensitivity Analysis and Partial Identification** These methods allow for exploring hidden variables and expanding the scope of valid [[machine_learning_and_causal_inference_methodologies | causal inferences]] <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.
*   **Optimal Experimentation Theory** This field helps determine what actions to take to minimize uncertainty in an optimal way, such as through Active Bayesian [[machine_learning_and_causal_inference_methodologies | Causal Inference]] (ABCI) <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>.
*   **Causal Data Fusion** Combining experimental and observational data can lead to robust [[machine_learning_and_causal_inference_methodologies | causal conclusions]] <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>.

Ultimately, the iterative approach, combined with human expertise and emerging technologies like [[applications_of_generative_modeling_in_causality | generative AI]], helps bridge the trust deficit in data-driven decision-making, moving towards a future where actionable, causal intelligence is paramount <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.