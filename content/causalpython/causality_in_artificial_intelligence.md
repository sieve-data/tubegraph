---
title: Causality in Artificial Intelligence
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

Causality is a crucial area of focus in Artificial Intelligence (AI) and [[causality_and_machine_learning | machine learning]], with a passionate community exploring its depths <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Personal Journey into Causality <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>

The guest's initial studies at TU Darmstadt focused on computer science, with an early interest in computer security <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This shifted to robotics and reinforcement learning under Professor Jan Peters, and later into neuroscience <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. The common thread across these diverse fields was a fundamental question about intelligence: attempting to understand and operationalize what intelligence is <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a> <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

A pivotal moment was discovering Judea Pearl's "Book of Why" during master's studies, which ignited a profound interest in causality <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a> <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. From this perspective, reasoning causally is considered a necessary component for intelligence, even if not necessarily sufficient <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a> <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

## Current and Future Directions in Causal Research <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>

The field of causality research can be broadly divided into two main areas:
*   **Causal Discovery:** The process of deriving a causal graph from data <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. This aspect is more closely aligned with [[causal_ai_and_machine_learning | machine learning]] <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.
*   **Causal Inference:** Focusing on modeling assumptions to draw sound conclusions based on an existing graph <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

Beyond these, critical missing aspects include:
*   **Bridging the Gap:** Creating stronger connections between causal discovery and causal inference <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>.
*   **Philosophical Inquiry:** Broadening the horizon by asking fundamental questions that may not have been posed before <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
*   **Abstractions:** Understanding and developing formalisms for different levels of causal representation <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
*   **Connection to Logic:** Integrating causal reasoning with logic-based and neuro-symbolic AI <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.

### The Role of Abstractions <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>

In [[causal_ai_and_machine_learning | causal AI and machine learning]], abstractions are a key concept for computer scientists <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. Seminal work by Rin et al. (2017) explored "causal consistency of structural causal models," which involves equating two different structural causal models at different levels of abstraction <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.

An example of this is the difference between total cholesterol (a high-level variable) and its components like HDL and LDL (low-level variables) <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. The challenge in causal abstraction lies in respecting interventions across these levels <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.

The concept extends to fundamental questions like "where do variables come from?" or "what is even a causal variable?" <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>. Abstractions allow for looking at phenomena at different scopes while still capturing their essential characteristics <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.

### Causality as a "Useful Shortcut" <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>

Bertrand Russell argued against causality, suggesting it might be a convenient shortcut <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>. Pearl, as well as Peters, Bachoc, and others, also consider causality a "useful abstraction" <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a> <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>. This means it kicks out unnecessary detail while remaining sufficient and necessary to answer a given hypothesis <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a> <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. For instance, a baseball player doesn't calculate complex physics to hit a ball; they rely on an intuitive, "model-free" understanding <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>. Similarly, studying the brain at the extremely fine-grained neuron level (connectomics) might be too detailed for understanding broader brain functions, even if theoretically sufficient <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.

## Large Language Models (LLMs) and Causality <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>

When discussing LLMs, it's important to consider their philosophical grounding and whether they learn true causation or merely correlations <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>. The "correlations of causal facts" conjecture suggests that LLMs might be training on existing causal knowledge encoded in textual form, which then allows them to answer causal questions correctly <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a> <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>.

### Meta Structural Causal Models (Meta SCMs) <a class="yt-timestamp" data-t="20:36:00">[20:36:00]</a>

The "correlations of causal facts" conjecture led to the development of Meta SCMs. This formalism proposes a hierarchical structure where an SCM (Structural Causal Model) exists on a "meta-level" above a regular SCM <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a> <a class="yt-timestamp" data-t="26:15:00">[26:15:00]</a>.

The idea is that humans perform experiments, gain causal insights, and then record this knowledge in textual representations (e.g., textbooks, Wikipedia) <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>. These textual statements about causal relationships become variables in the Meta SCM. LLMs, by predicting the best next word, learn these correlations within causal knowledge, allowing them to formulate causally correct answers in our world <a class="yt-timestamp" data-t="22:10:00">[22:10:00]</a> <a class="yt-timestamp" data-t="23:33:00">[23:33:00]</a>.

### Scaling Laws and LLMs <a class="yt-timestamp" data-t="29:16:00">[29:16:00]</a>

While larger models like GPT-4 show improved performance on causal queries <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>, it's crucial to critically evaluate the benchmarks used. For instance, datasets like the Tübingen data set, while showing high accuracy, might contain obscure pairs or rely on common knowledge that LLMs could pick up from their vast training data <a class="yt-timestamp" data-t="31:09:00">[31:09:00]</a> <a class="yt-timestamp" data-t="32:51:00">[32:51:00]</a>.

The "scaling hypothesis" — the idea that simply increasing model size and data will lead to intelligence — is a significant debate. While scale (like the vast number and connectivity of neurons in the human brain) is certainly a necessary factor <a class="yt-timestamp" data-t="34:40:00">[34:40:00]</a>, the guest believes that [[causal_ai_and_its_connection_to_machine_learning | Causal AI and its connection to machine learning]] still requires ingenuity and conceptual development, suggesting a combination of both scale and symbolic reasoning <a class="yt-timestamp" data-t="36:09:00">[36:09:00]</a> <a class="yt-timestamp" data-t="36:43:00">[36:43:00]</a>.

### White Box vs. Black Box Models <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>

While humans are good at [[causality_and_ai_challenges_and_opportunities | causal reasoning]] in personal experiences (e.g., counterfactuals like "if I had come sooner, my bike would still be here") <a class="yt-timestamp" data-t="38:00:00">[38:00:00]</a>, they are not always white-box reasoners themselves and can construct plausible but inaccurate causal explanations <a class="yt-timestamp" data-t="39:01:00">[39:01:00]</a>.

The desire for "white-boxiness" in AI comes from the aim to understand these systems <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>. However, a white-box model does not automatically equate to explainability. For example, large linear programs are white-box in nature (their structure and algorithms are explicit), but their scale can make them impossible for humans to process and understand <a class="yt-timestamp" data-t="42:35:00">[42:35:00]</a> <a class="yt-timestamp" data-t="43:57:00">[43:57:00]</a>. The definition of "explanation" itself is not universally agreed upon <a class="yt-timestamp" data-t="42:11:00">[42:11:00]</a>. Therefore, black-box models can be acceptable as long as they provide faithful and useful explanations <a class="yt-timestamp" data-t="44:51:00">[44:51:00]</a>.

An example of explainable [[causal_ai_and_machine_learning | causal AI and machine learning]] is the "structural causal explanations" algorithm <a class="yt-timestamp" data-t="45:17:00">[45:17:00]</a>. This recursive algorithm utilizes a causal graph structure and quantitative knowledge (e.g., coefficients in linear models) to provide individual-level causal explanations. For instance, in a medical context, it could explain why a patient's mobility is poor by tracing back through their health and age <a class="yt-timestamp" data-t="45:39:00">[45:39:00]</a> <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>. This focuses on individualist causation rather than population-level "type causation" or formal "actual causation" <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>.

## Adoption of Causality in Industry <a class="yt-timestamp" data-t="49:28:00">[49:28:00]</a>

Progress in industrial adoption of [[causality_and_ai_challenges_and_opportunities | causality and AI challenges and opportunities]] is rapid <a class="yt-timestamp" data-t="49:37:00">[49:37:00]</a>. However, the scientific perspective still sees many unresolved issues and a lack of universal gold standards or [[benchmarking_causal_reasoning_in_ai | benchmarking causal reasoning in AI]] <a class="yt-timestamp" data-t="49:55:00">[49:55:00]</a>. Despite this, the application of causal inference is already yielding surprising and valuable results, for example, in biomedicine with large, expert-validated causal graphs <a class="yt-timestamp" data-t="52:28:00">[52:28:00]</a>. This suggests that [[causal_ai_in_medicine | Causal AI in medicine]] can serve as a powerful assistant, helping scientists discover new insights <a class="yt-timestamp" data-t="53:25:00">[53:25:00]</a>.

## Hype Cycles in Machine Learning <a class="yt-timestamp" data-t="57:09:00">[57:09:00]</a>

The field of [[machine_learning_and_causality | machine learning and causality]] often experiences "hype cycles" and "AI winters" <a class="yt-timestamp" data-t="57:12:00">[57:12:00]</a>. Historically, there have been periods of "early dramatic success followed by sudden, unexpected difficulties" <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>. However, the current pace of development, particularly with GPUs and large models, feels like it's accelerating rather than slowing down <a class="yt-timestamp" data-t="58:55:00">[58:55:00]</a>. While some advocate for toning down the hype to maintain scientific values, it's also argued that discourse and debate are essential, and attempting to separate AI from [[causal_ai_and_machine_learning | machine learning]] is unproductive <a class="yt-timestamp" data-t="59:41:00">[59:41:00]</a>.

## Recommended Resources for Studying Causality <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>

For those beginning their journey in causality:
*   The Causal Bandits discussion group website (discuss.causality.link) offers a comprehensive list of resources <a class="yt-timestamp" data-t="01:06:30">[01:06:30]</a>.
*   **Books:**
    *   Judea Pearl's "Causality" (dense, best used as a reference) <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
    *   Jonas Peters, Bernhard Schölkopf, and Dominik Janzing's "Elements of Causal Inference" (great for a [[causal_ai_and_machine_learning | machine learning]] perspective) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   **Surveys:** Jean Kaddour and colleagues' survey on [[causal_ai_and_machine_learning | causal AI and machine learning]] for papers in the area <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>.
*   **Lectures:** Jonas Peters and Elias Bareinboim are highly recommended lecturers <a class="yt-timestamp" data-t="01:07:42">[01:07:42]</a>.

While the formal aspects of causality can be daunting, they are considered necessary as a language to discuss modeling assumptions and derive sound conclusions from data <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a> <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a>. However, relying solely on intuition about causation can be misleading <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.