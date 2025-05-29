---
title: Challenges and advancements in causal AI
videoId: 8yWKQqNFrmY
---

From: [[causalpython]] <br/> 

[[causality_and_ai_challenges_and_opportunities | Causality in AI]] is becoming increasingly important, especially as AI agents begin to interact more extensively with the real and web worlds <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This shift brings core causal abstractions to the forefront, such as notions of action, reward, and behavior optimization or penalization <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Causality in AI Agents

While [[causality_and_machine_learning | causality]] may not always be explicitly apparent during the training of agents, becoming more like plain reinforcement learning <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, its role becomes critical the moment agents interact with human agents or collaborate <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. New causal questions emerge regarding:
*   Identifying the most useful agents <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Determining which agents should be rewarded <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   Counterfactual notions of blame for underperforming agents <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

Research from Google DeepMind, including a paper by Riches and Everett, explores how agents can learn robust world models, primarily through interventional distributions and learning responses from environmental interventions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. These studies suggest that if an agent operates in sufficiently diverse environments, even without explicit world models, it can learn actions that mimic a true causal agent <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Large Language Models (LLMs) and Causality

The rapid [[the_evolution_of_ai_technologies_deep_learning_vs_causal_ai | evolution of AI technologies]], particularly Large Language Models (LLMs), has highlighted that [[history_and_development_of_causality_in_ai | causality]] traditionally required both domain knowledge and the ability for discovery and reasoning <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. While the field spent considerable effort on discovery and reasoning from datasets, domain knowledge was often vaguely assumed to be provided externally <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

LLMs have demonstrated a capacity to learn this domain knowledge, and in many cases, this knowledge can enable reasoning even without data <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This suggests that the future of [[causal_ai_and_its_connection_to_machine_learning | causal inference]] must integrate both domain knowledge acquisition and robust reasoning <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

A key insight from the LLM era is that there are multiple paths to achieve a causal agent <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Previously, consensus leaned towards explicitly designing mechanisms, graphs, and inductive biases from causal principles <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. However, new evidence shows other effective strategies:
*   **Diverse Data Collection**: Gathering large amounts of diverse data can enable models to generalize and learn causal actions even without explicit causal models <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Leveraging Domain Knowledge and Axioms**: Building a foundation on established domain knowledge, theorems, and axioms (e.g., physics laws) allows models to perform causally consistent actions by applying learned rules rather than discovering them from first principles <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

## Advancements and Tools: The DoWhy Library

Dr. Amit Sharma, principal researcher at Microsoft Research India and creator of DoWhy, notes that his journey with computational causality began with the DoWhy library <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Genesis of DoWhy

The development of DoWhy was born out of frustration with existing tools that were often fragmented and difficult for beginners to navigate <a class="yt-timestamp" data-t="00:57:49">[00:57:49]</a>. Libraries were often specific to certain steps (e.g., matching or multi-level regression) and lacked a unified workflow <a class="yt-timestamp" data-t="00:57:54">[00:57:54]</a>. A primary motivation was to create a tool that made the process of [[causal_ai_and_machine_learning | causal inference]] more accessible and API-driven, similar to how computer scientists learn by doing <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.

Another key realization was the compatibility of graphical models and potential outcomes frameworks <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. While graphical models excel at framing problems and communicating assumptions, methods from potential outcomes literature (like propensity score-based methods) are excellent for estimation <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. DoWhy aimed to combine these strengths into a single, seamless tool <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.

### The Four Steps of DoWhy

DoWhy structures [[causal_ai_and_machine_learning | causal inference]] into four clear, sequential steps:
1.  **Model**: Defining the causal graph. This step emphasizes domain knowledge and can be done without data <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>.
2.  **Identify**: Determining if the causal effect can be identified from the given graph, also without requiring data <a class="yt-timestamp" data-t="00:59:20">[00:59:20]</a>.
3.  **Estimate**: Computing the causal effect using data <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>.
4.  **Refute**: Testing the robustness of the causal estimate.

### Verification and Refutation

The refutation step was heavily influenced by practices in economics and social sciences, where studies undergo rigorous feedback sessions and robustness checks <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. It also draws from biomedical literature's concept of negative controls, ensuring observed effects are due to the intended cause and not other factors <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

DoWhy includes:
*   **Sensitivity Analysis**: Exploring the impact of unobserved confounders <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Objective Tests**: Significance tests, such as adding a random common cause or replacing treatment with a placebo <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Dummy Outcomes**: Creating an outcome variable known *not* to be caused by the treatment, to check if the method correctly yields a zero causal effect <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
*   **Graph Verification**: More recently, tests have been added to verify the causal graph itself, comparing its information content to random graphs <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

## LLMs and DoWhy Integration

The integration of LLMs with DoWhy, particularly through the new `PY LLM` library, aims to make [[causal_ai_in_medicine | causal inference]] accessible even to non-experts, such as the general public <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.

### Addressing Bottlenecks

The biggest bottleneck in [[trends_in_causal_ai | causal AI]] has historically been generating a plausible or credible causal graph <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>. LLMs are proving useful in streamlining this process, offering suggestions for graph structures that experts can then critique and refine <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

Another challenge is in designing effective reputation tests <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. LLMs can assist by suggesting suitable tests (e.g., identifying dummy outcomes based on context) and helping interpret their results <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.

## Causality for LLM Robustness

Beyond using LLMs to aid [[causal_ai_and_machine_learning | causal inference]], a significant research direction explores how [[causal_ai_and_its_connection_to_machine_learning | causality can enhance machine learning]] and LLMs themselves <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>. The focus is on imparting how to *learn* causal knowledge, rather than just direct causal knowledge <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>.

Research shows that training LLMs on fundamental causal axioms, such as transitivity and d-separation, can significantly improve their performance on new causal tasks and lead to better generalization <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>. For example, a Llama model trained on synthetic axiomatic data showed a substantial improvement (around 20 percentage points) on a causal reasoning benchmark like CotoC <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>. This suggests that models can learn to compose and apply these axioms at test time, a hallmark of intelligence <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.

However, a tension exists: LLMs might learn statistical shortcuts from observational data, which do not generalize, even if initially programmed with correct algorithms <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>. The hope is that scaling diverse training data can constrain the space of these shortcuts, pushing models towards learning genuine causal principles <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.

## Future Challenges and Directions

### Technical Challenges

A major technical challenge lies in achieving a "model-free revolution" in [[causality_and_ai_challenges_and_opportunities | causality]], similar to model-free reinforcement learning <a class="yt-timestamp" data-t="00:48:23">[00:48:23]</a>. This involves extracting maximum information from diverse datasets while still providing the theoretical guarantees expected from model-based approaches <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.

The concept of "exchangeable distributions," where data comes from multiple environments and is mixed, offers a promising avenue for causal discovery and learning causal directions, especially as the diversity of environments increases <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.

### Sociological Challenges

The field of [[causality_and_ai_challenges_and_opportunities | causality]] has historically gravitated towards principles-based methods <a class="yt-timestamp" data-t="00:51:24">[00:51:24]</a>. However, a "bitter lesson" for causality might be that while causality is the desired end result, it may not always be the sole means to achieve it <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>. In some systems (e.g., industrial root cause analysis), causal means and ends align perfectly, but in many other cases, alternative approaches (like data augmentation) might also lead to causal outcomes <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

This relates to the idea of finding the "still point in the turning world"—identifying what remains static (e.g., causal mechanisms) across different distributions or environments <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>. This perspective, evident in contrastive learning and concepts like testable implications, emphasizes learning invariants from diverse data <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>.

### Future Outlook

The landscape for [[causality_and_ai_challenges_and_opportunities | causality in AI]] has vastly expanded with LLMs <a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a>. There are exciting opportunities to:
*   Make language models more robust through causal principles <a class="yt-timestamp" data-t="01:07:11">[01:07:11]</a>.
*   Develop tools that leverage LLMs to accelerate the scientific cycle, from generating literature reviews and causal graphs from text to planning new experiments <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.

The goal for libraries like DoWhy is to become a comprehensive causal ecosystem (`py-why`), offering seamless causal inference workflows from data input to robust analysis, and eventually enabling non-experts to engage with complex causal questions through natural language interfaces <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. This broader view of causality encompasses not just data-driven analysis but also synthesizing existing research and domain knowledge to provide causal insights <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>.

## Community Involvement

The `py-why` organization operates with an MIT license, making all its software open-source <a class="yt-timestamp" data-t="01:09:22">[01:09:22]</a>. Researchers and practitioners are encouraged to contribute methods, provide feedback, and share real-world use cases to further develop the field <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>.