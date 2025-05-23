---
title: Mechanistic interpretability in AI
videoId: UTuuTTnjxMQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Mechanistic interpretability aims to understand the internal workings of AI models, particularly large language models (LLMs), by identifying and analyzing their fundamental components and how they interact. This field seeks to move beyond treating models as black boxes and to build a precise, engineering-style understanding of their internal computations. This article outlines key concepts, techniques, goals, and challenges in mechanistic interpretability as discussed by researchers Trenton Bricken (Anthropic) and Sholto Douglas (Google DeepMind).

## Core Concepts

Mechanistic interpretability revolves around several core ideas that attempt to deconstruct how models process information and arrive at their outputs.

### Features
Features are considered fundamental units of what is happening within a model <a class="yt-timestamp" data-t="02:09:55">[02:09:55]</a>. They can be defined as directions in the model's activation space or latent variables that have a causal influence on the system <a class="yt-timestamp" data-t="02:11:18">[02:11:18]</a>.
*   **Hierarchy and Abstraction:** Features can exist at various levels of abstraction. For example, early layers of a model might have a feature for the word "park," while deeper layers might distinguish between "park" as a last name (e.g., Lincoln Park) and "park" as a grassy area <a class="yt-timestamp" data-t="02:58:23">[02:58:23]</a>. Publicly shared examples of high-level features include those related to "love" or "sudden changes in scene, particularly associated with wars being declared" <a class="yt-timestamp" data-t="02:58:03">[02:58:03]</a>.
*   **Feature Splitting:** Models can learn a varying number of features depending on the capacity provided during interpretability analysis. For instance, with less capacity, a model might learn a general "bird" feature. With more capacity (e.g., projecting to a higher-dimensional space), this can split into more specific features like "ravens," "eagles," and "sparrows" <a class="yt-timestamp" data-t="02:12:13">[02:12:13]</a>, <a class="yt-timestamp" data-t="02:36:43">[02:36:43]</a>. This suggests a semantic tree of concepts, where a coarse "biology" feature might recursively expand into "cells" vs. "whole body biology," and further down to highly specific concepts like "anthrax" <a class="yt-timestamp" data-t="02:40:51">[02:40:51]</a>.
*   **Universality:** There's evidence that some features are universal across different models trained on similar data. The "Base64" encoding feature, for instance, has been observed across multiple models with high cosine similarity, even when models are trained with different random seeds <a class="yt-timestamp" data-t="02:26:31">[02:26:31]</a>. This supports the "quantum theory of neural scaling," which hypothesizes that models learn similar features in a similar order (e.g., n-grams, then induction heads) [[large_language_models_and_transfer_learning | Large Language Models and Transfer Learning]] <a class="yt-timestamp" data-t="02:27:15">[02:27:15]</a>.
*   **Alien Features:** Models can develop features for concepts in ways that are non-human-like due to their training data and objectives. An example is the model learning three distinct Base64 features: one for numbers, one for letters, and a third, more obscure one for the subset of Base64 that is ASCII decodable. It took some effort to understand this third feature, highlighting the "Shoggoth-esque" nature of model representations <a class="yt-timestamp" data-t="02:32:57">[02:32:57]</a>.

### Superposition
Superposition is a key concept explaining how models can represent more features than they have apparent parameters (e.g., neurons).
*   **Definition:** Models learn a compression strategy called superposition when dealing with high-dimensional and sparse data, which is characteristic of real-world data like the internet <a class="yt-timestamp" data-t="01:08:32">[01:08:32]</a>. This allows them to pack many features into their activations. This is why models are often considered "dramatically underparameterized" given the complexity of the tasks they perform <a class="yt-timestamp" data-t="01:10:52">[01:10:52]</a>.
*   **Interpretation Challenge:** Superposition makes networks hard to interpret because individual neurons become "polysemantic," meaning they fire for a confusing mix of seemingly unrelated inputs (e.g., "Chinese," "fish," "trees," and full stops in URLs) <a class="yt-timestamp" data-t="01:09:24">[01:09:24]</a>.
*   **Disentangling Superposition:** The "Towards Monosemanticity" paper by Anthropic demonstrated that by projecting neuron activations into a higher-dimensional space and applying a sparsity penalty, one can recover "clean" or "monosemantic" features, effectively undoing the compression <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>.
*   **Superposition in the Brain:** Neuroscientist Bruno Olshausen speculates that brain regions not well understood (like V2 in the visual cortex, compared to the more interpretable V1) might be doing significant computation in superposition <a class="yt-timestamp" data-t="02:48:18">[02:48:18]</a>.
*   **Mechanism:** Superposition is not an artifact of a single neuron but rather of the space created by combinations of neuron activations—a "combinatorial code" <a class="yt-timestamp" data-t="02:49:30">[02:49:30]</a>.

### Circuits
Circuits are formed by features interacting across layers to perform specific computations or reasoning steps.
*   **Simple Circuits:**
    *   **Induction Heads:** A basic reasoning circuit, often two layers, that learns to complete patterns by looking for previous occurrences of a token and copying the token that followed it (e.g., predicting "Dursley" after "Mr." if "Mr. Dursley" appeared earlier) <a class="yt-timestamp" data-t="02:17:52">[02:17:52]</a>.
    *   **IOI Circuit (Indirect Object Identification):** Identifies indirect objects in sentences (e.g., in "Mary and Jim went to the store, Jim gave the object to ____," it predicts "Mary") <a class="yt-timestamp" data-t="02:19:49">[02:19:49]</a>.
    *   **Copying/Suppressing Heads:** Some heads might always try to copy a previous token, while others learn to suppress this copying behavior in certain contexts <a class="yt-timestamp" data-t="02:20:19">[02:20:19]</a>.
*   **Complex Circuits (Goals):** A major goal is to identify more complex circuits, such as a "deception circuit" that activates when a model is being intentionally misleading, particularly in malicious ways [[ai_developments_in_hardware_and_software_advancements | AI Developments in Hardware and Software Advancements]] <a class="yt-timestamp" data-t="02:53:16">[02:53:16]</a>, <a class="yt-timestamp" data-t="02:17:29">[02:17:29]</a>. The hope is that such circuits would offer more specificity and sensitivity than individual features alone <a class="yt-timestamp" data-t="02:54:51">[02:54:51]</a>.

## Techniques in Mechanistic Interpretability

Several techniques are employed to uncover and understand the internal mechanisms of AI models.

### Dictionary Learning / Sparse Autoencoders
This is an unsupervised method where model activations (from many inputs) are projected into a higher-dimensional space and then projected back down, with a constraint to reconstruct the original activity sparsely <a class="yt-timestamp" data-t="02:37:48">[02:37:48]</a>, <a class="yt-timestamp" data-t="02:53:50">[02:53:50]</a>.
*   **Goal:** To find a set of sparse, interpretable features that span the model's representational space <a class="yt-timestamp" data-t="02:34:48">[02:34:48]</a>.
*   **Scalability:** The cost depends on expansion factors (how much higher the dimension is) and the amount of data needed <a class="yt-timestamp" data-t="02:40:08">[02:40:08]</a>. Feature splitting allows for a "depth-first search" approach: start with coarse features and recursively expand specific semantic areas (e.g., explore the "biology" feature space for more specific sub-features like "anthrax") rather than a costly "breadth-first" expansion of all features at high resolution <a class="yt-timestamp" data-t="02:41:22">[02:41:22]</a>.
*   **Application:** Anthropic is applying dictionary learning to their "sleeper agents" work to detect hidden malicious behaviors <a class="yt-timestamp" data-t="02:24:19">[02:24:19]</a>.

### Probing (e.g., Linear Probes)
Probes, such as linear classifiers, are trained on model activations to predict certain properties (e.g., whether a statement is true or false) <a class="yt-timestamp" data-t="02:54:08">[02:54:08]</a>.
*   **Limitations:** Recent work (e.g., on CCS, contrast-consistent search) has shown that linear probes may not reliably find "truth directions" <a class="yt-timestamp" data-t="02:53:25">[02:53:25]</a>. They require knowing what you are looking for in advance, and in a high-dimensional space, it's easy to find spurious correlations <a class="yt-timestamp" data-t="02:53:35">[02:53:35]</a>. Dictionary learning is preferred as it's unsupervised in finding features, with labeling done post hoc.

### Ablation Studies
Given that models are deterministic <a class="yt-timestamp" data-t="02:22:36">[02:22:36]</a> (when sampling temperature is zero), researchers can systematically remove or alter ("ablate") parts of the model (neurons, features, circuits) and observe the effect on behavior. This helps to:
*   Pinpoint causally responsible components.
*   Identify backup circuits and redundancy <a class="yt-timestamp" data-t="02:22:57">[02:22:57]</a>.
*   Confirm the function of identified features/circuits <a class="yt-timestamp" data-t="03:01:27">[03:01:27]</a>.

### Automated Interpretability
As models become more complex, there's a growing need for automated interpretability tools.
*   **Models Interpreting Models:** Using LLMs to label features found by dictionary learning or to run interpretability experiments at scale <a class="yt-timestamp" data-t="02:23:07">[02:23:07]</a>. Models can sometimes provide more nuanced labels for features than humans (e.g., "Latin words that define plants" vs. just "Latin words") [[challenges_and_limitations_in_ai_interpretability_and_safety | Challenges and Limitations in AI Interpretability and Safety]] <a class="yt-timestamp" data-t="02:35:19">[02:35:19]</a>.
*   **Adversarial Search:** A model could actively edit input text to determine what makes a specific feature fire or not, systematically searching the input space <a class="yt-timestamp" data-t="02:36:03">[02:36:03]</a>.
*   **Debate Setups:** Imagining scenarios where two models debate the function of a feature, potentially making edits to test hypotheses <a class="yt-timestamp" data-t="02:52:54">[02:52:54]</a>.

## Goals and Applications

Mechanistic interpretability is pursued for several critical reasons, primarily related to safety and reliability.

*   **Identifying Malicious Behavior:** A key goal is to detect and understand harmful behaviors like deception or "sleeper agent" triggers (where a model exhibits malicious behavior when a specific condition is met, as explored in Anthropic's "sleeper agents" paper <a class="yt-timestamp" data-t="01:19:29">[01:19:29]</a>). The aim is to find, for example, a "deception circuit" that activates when the model is being intentionally untruthful [[potential_ai_takeover_scenarios_and_implications | Potential AI Takeover Scenarios and Implications]] <a class="yt-timestamp" data-t="02:17:29">[02:17:29]</a>.
*   **Enhancing Model Safety:** If successful, interpretability could allow for precise interventions, such as ablating features or circuits responsible for undesirable behaviors like sycophancy or malice <a class="yt-timestamp" data-t="03:00:36">[03:00:36]</a>. This offers a more targeted approach to safety than methods like RLHF, which can be vulnerable to "black swan" failures in unobserved scenarios <a class="yt-timestamp" data-t="03:01:44">[03:01:44]</a>.
*   **Understanding Model Generalization and Learning:** Interpretability helps reveal how models learn and generalize. For example, the Othello-GPT work showed models can learn an internal representation of the game board without ever explicitly seeing one [[ai_alignment_challenges_and_ethical_considerations | AI Alignment Challenges and Ethical Considerations]] <a class="yt-timestamp" data-t="01:33:50">[01:33:50]</a>.
*   **Verifying Model Reasoning:** For complex outputs like a million-line pull request, interpretability could help flag features associated with deceptive or malicious intent <a class="yt-timestamp" data-t="02:17:29">[02:17:29]</a>.
*   **Understanding Fine-tuning:** Research is exploring what changes internally when a model is fine-tuned or undergoes RLHF [[reinforcement_learning_from_human_feedback_rlhf | Reinforcement Learning from Human Feedback (RLHF)]] <a class="yt-timestamp" data-t="03:00:14">[03:00:14]</a>.

## Challenges and Open Questions

Despite progress, mechanistic interpretability faces significant challenges.

*   **Scaling to Superhuman Models:** As models like a hypothetical GPT-7 become vastly more capable, interpreting their potentially "superhuman" features and reasoning will be a major hurdle [[ai_scalability_and_breakthroughs | AI Scalability and Breakthroughs]] <a class="yt-timestamp" data-t="02:23:18">[02:23:18]</a>. It's an open question if human-understandable labels can be applied to all features in such models, especially if they reason in alien ways (e.g., the esoteric knowledge needed for the Base64 feature variants <a class="yt-timestamp" data-t="02:33:42">[02:33:42]</a>).
*   **Feature Splitting and Geometry:** The hierarchical nature of feature splitting needs further exploration. It's hoped that semantic relationships are somewhat preserved (e.g., an "anthrax" feature would be found within a broader "biology" feature space, not under an unrelated concept like "coffee cans" <a class="yt-timestamp" data-t="02:43:23">[02:43:23]</a>). The actual geometry of feature space is an active research area <a class="yt-timestamp" data-t="02:43:20">[02:43:20]</a>.
*   **Redundancy and Robustness:** Models exhibit redundancy, where multiple circuits might perform similar functions, or backup circuits can take over if a primary one is ablated <a class="yt-timestamp" data-t="02:20:19">[02:20:19]</a>, <a class="yt-timestamp" data-t="02:22:08">[02:22:08]</a>. Comprehensive identification is difficult.
*   **Interpreting Weights vs. Activations:** Current methods largely focus on interpreting activations (transient states of the model during a call). The "dream" is to also understand the model's weights (the permanent connections) independently of specific data inputs, though this is a very hard problem [[ai_alignment_and_safety_concerns | AI Alignment and Safety Concerns]] <a class="yt-timestamp" data-t="02:38:42">[02:38:42]</a>.
*   **Lack of Null Hypotheses:** One concern is the difficulty in formulating clear alternative hypotheses for how intelligence works if the current feature-centric view is incorrect. This makes it harder to know if the field is fundamentally on the right track <a class="yt-timestamp" data-t="02:29:31">[02:29:31]</a>, although current approaches have high explanatory power for many phenomena <a class="yt-timestamp" data-t="02:30:15">[02:30:15]</a>.

## The State of the Field and Future Directions

Mechanistic interpretability is an active and growing research area.
*   **Key Research Groups:** Anthropic has a dedicated interpretability team, led by Chris Olah <a class="yt-timestamp" data-t="00:46:31">[00:46:31]</a>, which has grown significantly <a class="yt-timestamp" data-t="01:36:36">[01:36:36]</a> and publishes its research openly <a class="yt-timestamp" data-t="03:08:22">[03:08:22]</a>. Current focuses include scaling dictionary learning, identifying circuits, and achieving similar interpretability success for attention heads [[ai_safety_and_alignment | AI Safety and Alignment]] <a class="yt-timestamp" data-t="02:56:49">[02:56:49]</a>.
*   **Call for Academic Involvement:** There's a desire for more academic research in interpretability, as it often doesn't require the massive compute resources of frontier model training and tackles fundamental scientific questions [[scientific_and_technological_developments_in_ai | Scientific and Technological Developments in AI]] <a class="yt-timestamp" data-t="03:08:19">[03:08:19]</a>. The field is becoming more receptive, with figures like Neel Nanda promoting this work <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Interpretability and GOFAI:** The idea of features being manipulated by operations bears resemblance to Good Old-Fashioned AI (GOFAI), particularly Vector Symbolic Architectures (VSAs). VSAs use distributed representations (vectors), superposition (summation), and binding operations (like XOR for binary vectors, analogous to key-value attention) to form Turing-complete systems capable of representing complex data structures [[mechanistic_interpretability_and_neural_network_reasoning | Mechanistic Interpretability and Neural Network Reasoning]] <a class="yt-timestamp" data-t="02:50:33">[02:50:33]</a>.

## Societal Implications

The success of mechanistic interpretability could grant significant control over AI systems. This raises concerns about who wields this control and for what purposes, such as "locking in" certain values or behaviors [[ethics_in_ai_development | Ethics in AI Development]] <a class="yt-timestamp" data-t="03:03:09">[03:03:09]</a>. Transparency, such as publishing the "constitutions" or ethical guidelines models are expected to follow, and allowing public feedback, are considered important mitigating factors <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

Overall, mechanistic interpretability is seen as a crucial path toward building safer, more reliable, and trustworthy AI systems, even as the complexity and capability of these systems continue to grow.