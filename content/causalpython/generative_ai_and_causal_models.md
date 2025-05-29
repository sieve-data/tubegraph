---
title: Generative AI and Causal Models
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

The intersection of [[causal_ai_and_machine_learning | Causal AI]] and Generative AI presents significant opportunities for developing more robust and human-like AI systems.

## Causal AI and AGI
From a causal perspective, an Artificial General Intelligence (AGI) model would be capable of reasoning about cause and effect <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>. This contrasts with traditional machine learning models that primarily identify statistical patterns in data <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. Humans often reason by imagining hypothetical scenarios and conditioning on potential outcomes, which [[causal_inference_models_and_ai_workshops | causal inference]] calls "potential outcomes" <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. Causal models provide the semantic framework and language to build algorithms that emulate this human-like reasoning, allowing for more sample-efficient learning and opening up new capabilities previously unavailable <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

Dr. Robert Ness suggests that a step towards AGI involves building models with the specific reasoning capabilities observed in humans, including causal abilities <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>. This approach differs from traditional [[causal_inference_models_and_ai_workshops | causal inference]] research, which typically focuses on answering objective questions about external cause-and-effect relationships (e.g., "does smoking cause cancer?") <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. Instead, it aims to align algorithms with how humans reason, even if that reasoning includes cognitive biases or inefficient heuristics <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

## Bridging Probabilistic Machine Learning and Causal Inference
A recent paper by Dr. Ness and co-authors demonstrated that probabilistic programming frameworks (like PyMC or Pyro), commonly used for latent variable modeling, can be effectively applied for [[causal_inference_models_and_ai_workshops | causal inference]] tasks if the intervention distribution is identifiable <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. This means if a quantity can be identified using tools like the "do-calculus," a probabilistic programming implementation is guaranteed to provide an unbiased estimate of the causal effect <a class="yt-timestamp" data-t="00:42:03">[00:42:03]</a>. This opens up causal reasoning to those familiar with latent variable models that can be represented as graphs <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

Libraries like Cairo (built on Pyro) are designed to abstract away the complex inference engineering often required for [[causal_inference_models_and_ai_workshops | causal inference]] tasks that don't mesh well with existing probabilistic machine learning abstractions <a class="yt-timestamp" data-t="00:47:39">[00:47:39]</a>. This allows researchers to focus more on the causal aspects of the problem rather than the intricacies of inference <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. Cairo also aligns with the philosophy that causal uncertainty can be modeled with probability, and system uncertainty can be addressed with causal assumptions <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.

## [[applications_and_challenges_of_causality_in_generative_modeling | Applications and challenges of causality in generative modeling]]
One of the most significant [[future_directions_for_causal_ai_and_generative_models | future directions for causal AI and generative models]] is **causal representation learning** <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. This involves learning latent representations that correspond to actual causes within the data-generating process <a class="yt-timestamp" data-t="00:50:12">[00:50:12]</a>.

### Generative AI Example: Image Generation
Current generative AI models like Midjourney or Stable Diffusion struggle with precise, localized edits based on causal reasoning <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>. For instance, if a user wants to change glasses from blue to red in an image, the model often introduces unintended artifacts or changes other unrelated elements <a class="yt-timestamp" data-t="00:52:17">[00:52:17]</a>. This is because the underlying representations do not inherently respect causal relationships.

Ideally, a causal model would allow for counterfactual questions where only causally downstream elements change <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>. If the model could operate semantically on learned causal abstractions, it would enable users to turn "knobs" for specific adjustments without affecting unrelated parts of the output <a class="yt-timestamp" data-t="00:52:40">[00:52:40]</a>. This is analogous to editing text in a large language model, where changes are localized and predictable <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>. Better causal representations could significantly improve the utility and control of generative AI models, especially for images and video <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>.

### Large Language Models and Causal Reasoning
A key question for large language models (LLMs) is whether they "learn a world model," which Dr. Ness interprets as a Causal Model <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. This relates to Pearl's Causal Hierarchy Theorem (or Causal Ladder), which outlines three levels of reasoning:
1.  **Associational**: Observational statistics (e.g., "What is?") <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
2.  **Interventional**: Causal effects (e.g., "What if I do X?") <a class="yt-timestamp" data-t="00:56:08">[00:56:08]</a>.
3.  **Counterfactual**: Reasoning across hypothetical worlds (e.g., "What if things had been different?") <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.

To reliably answer questions at a certain level, assumptions at that same level are required <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>. While LLMs can empirically answer causal and counterfactual questions (e.g., "does smoking cause cancer?" or "what would have happened if...?") <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>, they are prone to "hallucinations," meaning they may generate false information <a class="yt-timestamp" data-t="00:57:44">[00:57:44]</a>.

The challenge is to ensure that LLMs reliably produce causally correct answers. The required level-three assumptions (for counterfactuals) must exist somewhere:
*   In the training data (unlikely given current training methods) <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
*   In the model architecture itself <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>.
*   Learned in the parameterization of the trained model <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>.
*   In the prompt <a class="yt-timestamp" data-t="00:59:13">[00:59:13]</a>.

Incorporating causal information directly into the Transformer architecture itself could provide theoretical guarantees for reliable causal query answering, similar to how the do-calculus provides guarantees for latent variable models <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. This approach aims to build models that are aligned with human abstract thinking and creative processes, offering greater control and predictability in generated content <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>.

Rather than solely scaling models to ever-larger datasets, a [[future_directions_for_causal_ai_and_generative_models | future direction for causal AI and generative models]] involves leveraging inherent structure in data (e.g., historical repos, informative git commits, executable code examples) to improve model capabilities with smaller datasets <a class="yt-timestamp" data-t="01:03:13">[01:03:13]</a>. This focus on "depth" over "breadth" in training data can lead to more efficient and capable models <a class="yt-timestamp" data-t="01:05:17">[01:05:17]</a>.

The speaker believes that the questions surrounding causality will not become obsolete with new deep learning architectures <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>.