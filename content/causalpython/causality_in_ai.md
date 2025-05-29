---
title: Causality in AI
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

Causality is a double-edged sword due to existing wrong intuitions about causation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores the intersection of causality and artificial intelligence, drawing insights from an interview with a dedicated researcher in the field.

## A Researcher's Journey into Causality

The guest, a passionate researcher with interests in AI, philosophy, and neuroscience, has co-authored papers at the [[intersection_of_causality_and_ai_technologies | intersection of causality and large language models]], [[graph neural networks | graph neural networks]], and more <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. His journey into causality was sparked by Judea Pearl's book, "The Book of Why" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, which he encountered during his master's studies <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Before focusing on causality, he studied computer science at TU Darmstadt, initially aiming for computer security <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. He was later convinced to switch to robotics by Professor Jan Peters, a prominent figure in robotics and reinforcement learning <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. His academic path then broadened to include neuroscience and various topics related to intelligence <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. The common denominator across these diverse fields was a foundational question: trying to understand and operationalize what intelligence is <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This stems from a personal passion and natural scientific curiosity, particularly since intelligence remains largely undefined <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### Causality as Necessary for Intelligence
For the researcher, the best definition of intelligence is that humans are an example of it <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. He believes that [[causal reasoning in ai | causal reasoning]] is a necessary, though not necessarily sufficient, component for intelligence <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. While Judea Pearl might argue it's also sufficient, the researcher considers other factors like emotions as hard to grasp <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Causal Research: Current State and Future Directions
The field of [[causal discovery and inference in ai | causal discovery and inference in AI]] is broadly divided into two main strands:
1.  **Causal Discovery**: The problem of deriving a causal graph from data, which is more machine learning-oriented <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
2.  **Causal Inference**: Focusing on modeling assumptions and drawing sound conclusions based on an existing graph <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

A significant missing aspect in current research is the bridge between these two strands <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Additionally, the researcher's work is more philosophical in nature, aiming to broaden the horizon by asking fundamental questions that may not have been considered before <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

Other missing areas include:
*   Interfaces and broadening the horizon of inquiry <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   [[causal reasoning in artificial intelligence | Abstractions]]: The lack of sufficient work on abstractions, building on the analytical and theory-grounded work of authors like S. Beas and R. Romstein <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Connection to Logic: The NIPS 2022 workshop, "Neuro-Causal and Symbolic AI," highlighted the importance of integrating neural networks, causality, and symbolic logic, seeing them as "two sides of the same coin" <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## The Role of Abstractions in Causal Reasoning

As a computer scientist, abstraction is a key concept <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In a causal sense, abstractions involve equating two different structural causal models (SCMs) at different levels, such as low-level and high-level variables <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. A classic example is total cholesterol (high-level) versus its components, HDL and LDL (low-level), ensuring that interventions are respected when abstracting <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

A deeper philosophical question arises: "Where do the variables come from?" and "What is even a causal variable?" <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This highlights the importance of abstractions and representation learning, allowing systems to look at things at different scopes while still capturing their characteristics <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

### Causality as a "Useful Abstraction"
Judea Pearl's "Causality" book discusses Bertrand Russell's argument against causality and suggests that causality might be a "convenient shortcut" in physics <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. This aligns with the idea that causality is a "useful abstraction" <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>, as proposed by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf in "Elements of Causal Inference" <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This means kicking out unnecessary details of a model while retaining enough to answer hypotheses <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

> [!EXAMPLE] Baseball Player Analogy
> A baseball player hitting a ball doesn't calculate the physics in real-time; it's an intuitive, model-free process <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. Similarly, in reinforcement learning, the goal is often to know the best next action without needing a full model <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

This concept extends to neuroscience, where highly detailed connectome maps of the brain (neuron-level) are certainly sufficient but potentially too detailed for certain hypotheses <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. The choice of abstraction level depends on the hypothesis space one wants to cut down <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## Large Language Models (LLMs) and Causal Reasoning

The researcher is an advocate of LLMs but approaches their [[generative_ai_and_causal_reasoning | causal reasoning]] capabilities from a critical perspective, questioning whether they truly understand causality <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.

### The "Correlations of Causal Facts" Conjecture
His team proposes the conjecture that LLMs learn "correlations of causal facts" <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. If LLMs only learn correlations, then their ability to answer causal questions correctly implies that there are correlations between causal questions and causal answers within their training data <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

> [!EXAMPLE] Altitude and Temperature
> If an LLM is asked whether altitude causes temperature, and it responds "yes," it's because textbooks and encyclopedias (like Wikipedia, which contain articles on lapse rate) document this causal relationship. LLMs learn to predict the "best next word," so if altitude and temperature are mentioned, "causing" is a more probable connection in human-generated text <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>.

This intuition is formalized in their "meta SCM" framework <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. A meta SCM is a higher-level SCM that talks about insights regarding other SCMs. For instance, a regular SCM might describe the link between altitude and temperature. The meta SCM would then describe the insight *about* that link, e.g., "altitude causes temperature" <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. This means LLMs are training on correlations found in the textual representation of causal knowledge <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

This perspective highlights a conceptual difference between the textual representation of knowledge and the experimental side of things. While physicists conduct experiments to derive laws, these laws are then written down in textbooks, becoming knowledge that can be learned by LLMs without direct experimentation <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.

### Critique of LLM Causal Evaluation
The researcher expresses skepticism regarding conclusions about LLM causal capabilities based on datasets like the Tübingen pair dataset <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. While LLMs may show high accuracy, issues include:
*   **Obscure pairs**: Many pairs in the dataset are so obscure that an LLM would be guessing in a binary choice (X causes Y or Y causes X) <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.
*   **Contextual limitations**: LLMs lack real-world context for specific names or abstract concepts, rendering certain test cases invalid <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.
*   **Simple metrics**: Relying solely on accuracy for such complex tasks can be misleading <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.

### Scaling Laws and the Future of AI
The concept of "scaling laws" suggests that simply increasing model size and data leads to improved performance, similar to the vast number and connectivity of neurons in the human brain <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. While scale is certainly necessary and has shown success in deep learning, the researcher believes that [[causal reasoning in artificial intelligence | ingenuity and conceptual development]] are also crucial <a class="yt-timestamp" data-t="00:36:11">[00:36:11]</a>. He envisions a combination of both approaches, aligning with the neuro-symbolic AI paradigm <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.

## White Box vs. Black Box in Causal AI

Humans are not always effective at [[causal reasoning in ai | causal reasoning]], especially for complex topics like policy <a class="yt-timestamp" data-t="00:38:39">[00:38:39]</a>. While we are good at personal counterfactuals (e.g., "If I had come sooner, my bike would still be here") <a class="yt-timestamp" data-t="00:38:26">[00:38:26]</a>, psychological evidence, such as Michael Gazzaniga's split-brain patient experiments, suggests humans can generate plausible causal explanations without true awareness of the underlying causes <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>. This raises questions about the necessity of "white-box" models in AI.

The researcher argues that white-boxiness and explainability, though intertwined, are independent concepts <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>. Even a white-box system may not be explainable if it's too complex for human processing <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>.

> [!EXAMPLE] Linear Programs
> Linear programs are white-box models because their structure and algorithms are explicit <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>. However, when scaled up (e.g., in complex energy systems), they become too large for humans to process, making it difficult to understand the "why" behind their outputs <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. As Judea Pearl noted, humans struggle to understand even five variables, let alone thousands <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.

Therefore, the researcher's "hot take" is that black-box models can be sufficient, provided they offer faithful and useful explanations <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.

### Structural Causal Explanations (SCEs)
His work includes a recursive algorithm called Structural Causal Explanations (SCEs), which uses the graph structure and quantitative knowledge from a causal model to provide individual-level explanations <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.

> [!EXAMPLE] Patient Mobility
> In a medical case, if an elderly patient named Hans has bad mobility, an SCE algorithm could explain it by traversing the causal graph: "Hans's mobility is bad because of his bad health, and his bad health because of being elderly" <a class="yt-timestamp" data-t="00:46:19">[00:46:19]</a>. This highlights both structural knowledge (parents in the graph) and quantitative relationships (e.g., good nutrition improving health, old age decreasing health) <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>.

This approach focuses on "individualist causation" rather than population-level "type causation" or the formal "actual causation" defined by Halpern and Pearl <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. The goal is to produce sound conclusions based on the assumed causal model <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>.

## Adoption of Causality in Industry

The adoption of causality in industry is progressing rapidly <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>. From a scientific perspective, much work remains, and discussions persist around the need for benchmarks and the "myth of the objective" <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>. However, from a practical standpoint, causal inference is already "super successful" <a class="yt-timestamp" data-t="00:51:32">[00:51:32]</a>, serving as an "assistant" to human experts.

> [!NOTE] Causal AI as an Assistant
> This aligns with Judea Pearl's vision for [[causal_ai_in_medicine | personalized medicine]] and the broader concept of an AI scientist or assistant that helps uncover new insights, as seen in DeepMind's work on "science X AI" <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

## Collaborations and Hype Cycles

A notable collaboration involved Petar Veličković from DeepMind, where they explored the relationship between [[graph neural networks | graph neural networks]] and structural causal models <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>. The most important outcome of this work was building a bridge between these two hot fields, opening up a new research direction <a class="yt-timestamp" data-t="00:55:40">[00:55:40]</a>.

Regarding AI hype cycles (e.g., "AI winters"), the researcher believes the current boom is unlikely to slow down like historical cycles, which often followed a 30-year pattern <a class="yt-timestamp" data-t="00:57:34">[00:57:34]</a>. He advocates for embracing the discourse and scientific debate rather than attempting to decouple AI from machine learning, which he considers impossible <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>.

## Personal Reflections and Recommendations

### Personal Heroes
Among historical figures, Kurt Gödel is considered a personal hero due to his foundational work in logic, particularly his incompleteness theorems, and his remarkable life story <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>.

### Influential Books
1.  **"The Book of Why" by Judea Pearl**: This book was instrumental in sparking the researcher's interest in the science of cause and effect <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.
2.  While many books could be a second choice, specific mentions include:
    *   "What If?" by Randall Munroe (xkcd comics) <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>.
    *   "Thinking, Fast and Slow" by Daniel Kahneman <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>.
    *   Works by Johann Wolfgang von Goethe, such as "Faust" or "West-Eastern Divan," which reflect deep philosophical traditions <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.

### Resources for Aspiring Causal AI Researchers
For those starting in causality, the following resources are highly recommended:
*   **The Causal Discussion Group**: Their landing page (discuss.causality.link) features a comprehensive list of resources <a class="yt-timestamp" data-t="01:06:30">[01:06:30]</a>.
*   **Books**:
    *   "Causality" by Judea Pearl (a dense reference book) <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
    *   "Elements of Causal Inference" by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf (more machine learning-oriented with excellent examples) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   **Surveys**: A survey by Jean Kaddour and colleagues focusing on machine learning in causality <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>.
*   **Lectures**: Lectures by Jonas Peters and Elias Bareinboim are highly praised <a class="yt-timestamp" data-t="01:07:42">[01:07:42]</a>.

> [!TIP] Importance of Formalism
> While intuitive understanding is valuable, formalism is necessary in causality. It provides a mathematical language to discuss modeling assumptions and derive sound conclusions from data generating processes <a class="yt-timestamp" data-t="01:08:38">[01:08:38]</a>. However, it's a "double-edged sword" because intuition alone can often lead to wrong conclusions about causation <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.

For anyone passionate about causality and finding meaning in this field, the advice is simple: "Do it. Just do it" <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>.