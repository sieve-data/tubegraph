---
title: Large Language Models and Transfer Learning
videoId: qTogNUV3CAI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article summarizes insights from Demis Hassabis, CEO of DeepMind, regarding Large Language Models (LLMs), their learning mechanisms, and the phenomenon of transfer learning.

## Understanding Intelligence and LLM Capabilities

Demis Hassabis views intelligence as likely having "high-level common algorithmic themes" that underpin how the brain processes the world, despite the existence of specialized brain parts for specific tasks <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This perspective informs the understanding of how LLMs learn and generalize.

### LLM Improvement with Domain-Specific Data
When LLMs are provided with extensive data in a specific domain, they tend to improve asymmetrically in that domain <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. However, this specialization doesn't preclude broader improvements.

## Transfer Learning in LLMs

Transfer learning refers to the phenomenon where improving a model in one specific domain can lead to surprising improvements in other, sometimes seemingly unrelated, domains <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Key Examples
A notable example of transfer learning in LLMs is the observation that when these models improve at coding, their general reasoning capabilities can also improve <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This improvement in coding and math leading to better general reasoning is a significant area of interest <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Comparison to Human Learning
Hassabis notes that this pattern of specialization and transfer mirrors human learning. Humans also tend to specialize and improve in specific areas (like chess or creative writing) through practice, even while using general learning techniques <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Mechanistic Understanding (Current Research Gaps)
Current analysis techniques are not yet sophisticated enough to precisely identify the mechanistic changes within a neural network that lead to transfer learning, such as pinpointing the exact part of a network that improves with both language and code <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Hassabis terms the needed research area "virtual brain analytics," analogous to fMRI or single-cell recording in neuroscience, to understand the representations these systems build <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. He encourages computational neuroscientists to apply their expertise to analyze large models <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## LLMs and Transfer Learning in Broader AI Systems

### LLMs as World Models for Planning Systems
LLMs are seen as a necessary, though likely insufficient, component of Artificial General Intelligence (AGI) systems <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. They can serve as increasingly accurate and reliable world models. A promising direction involves integrating LLMs with planning mechanisms, like those in AlphaZero, to make use of the LLM's model for concrete planning, chaining thoughts, and exploring possibilities through search <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This addresses a current limitation in large models, which lack robust search capabilities over massive possibility spaces <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The challenge of high compute costs for such integrated systems, potentially requiring an "LLM on each node of the tree," is acknowledged <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Role in Robotics and Multimodal Systems
The principles of LLMs and transfer learning are being applied to robotics.  
*   **Transferring Knowledge to Robotics:** Systems like Gato and RT-2 demonstrate progress in applying large model concepts to robotics, a domain often limited by data availability <a class="yt-timestamp" data-t="00:48:30">[00:48:30]</a>. The challenge of data scarcity in robotics pushes research towards data efficiency, transfer learning, and sim-to-real transfer <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>.
*   **True Multimodality and Cross-Modal Benefit:** Models like Gato treat various inputs (actions, words, pixels) as generic tokens, embodying true multimodality <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>. While harder to train initially, true multimodal systems are expected to yield more general and capable systems, as different modalities can benefit each other (e.g., understanding video might improve language capabilities) <a class="yt-timestamp" data-t="00:49:45">[00:49:45]</a>. Ideas from Gato are being incorporated into future generations of models like Gemini <a class="yt-timestamp" data-t="00:50:18">[00:50:18]</a>.

## Scaling, Generalization, and Emergent Abilities in LLMs

### The Scaling Hypothesis and LLMs
Hassabis views the extent of LLMs' effectiveness as surprising, even to those who initially worked on scaling hypotheses <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a> <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.  
*   **"Unreasonably Effective" Nature:** LLMs are considered "almost unreasonably effective" for their current architecture <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.   
*   **Emergence of Concepts and Abstractions:** These models exhibit emergent properties, including forms of concepts and abstractions, which might have previously been thought to require additional algorithmic breakthroughs <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. While explicit, neat abstract concepts might still need new algorithms, current systems can implicitly learn them <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.

### Grounding in LLMs and its Relation to Generalization
A surprising aspect of LLMs is their ability to achieve some form of grounding, even before recent multimodal models, primarily through language data <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. Hassabis hypothesizes this grounding comes from:  
*   **RLHF (Reinforcement Learning from Human Feedback):** Human raters are grounded in reality, so their feedback provides a grounding signal <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   **Language Data Itself:** Language might contain more grounding information than previously thought by linguists <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.  
Proper grounding is considered essential for systems to achieve goals in the real world <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. Multimodal models ingesting video and audiovisual data will further enhance grounding by allowing systems to correlate different types of information and understand real-world physics <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a> <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

## Current Limitations and Future Potential

### Predicting Downstream Capabilities
While core metrics like training loss can often be predicted as models scale, these do not always linearly translate to desired downstream capabilities like math proficiency or performance on benchmarks like MMLU <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. There are non-linear effects, and the mapping between optimized metrics and final capabilities is not yet perfectly understood <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a> <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

### LLMs for Scientific Discovery
Current LLMs can assist top human scientists by triaging search spaces or finding solutions (e.g., AlphaFold for protein structure) <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a> <a class="yt-timestamp" data-t="00:51:09">[00:51:09]</a>. However, they are not yet capable of formulating hypotheses or asking the "right question," which is often the hardest part of science <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>.

### Memory and Imagination in LLMs
Early criticisms of LLMs being mere memorization tools are less applicable to current systems like Gemini and GPT-4, which demonstrate generalization to new constructs <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a> <a class="yt-timestamp" data-t="00:39:48">[00:39:48]</a>. Hassabis's neuroscience research highlighted human memory as a reconstructive process, where components are reassembled. He proposed imagination as a similar process, using semantic components assembled in novel ways for purposes like planning <a class="yt-timestamp" data-t="00:39:54">[00:39:54]</a>. This kind of constructive imagination—pulling together different parts of a world model to simulate something new to aid planning—is likely still missing from current LLMs <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>.

In the context of LLMs' development and applications, challenges and methodologies in AI research can be explored further in discussions about the [[challenges_and_methodologies_in_ai_research_and_development]], and the scalability concerns tied to advancements like those seen in AlphaZero can be compared with concepts in [[alphazero_and_efficient_search_techniques]]. Additionally, the implications of AI on broader societal shifts resonate with topics in the [[impact_of_ai_on_future_technology_and_society]] and the [[economic_and_societal_impacts_of_ai_progress]]. The alignment, safety, and geopolitical implications of AGI are closely related to the discourse on the [[ai_alignment_and_safety]] and the [[the_geopolitical_stakes_of_agi_development]], while examining mechanistic interpretability links to [[mechanistic_interpretability_in_ai]]. Quantum computing breakthroughs that parallel these AI advancements can be found in discussions of [[microsofts_breakthroughs_in_ai_and_quantum_computing]].