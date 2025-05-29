---
title: The role of language and perception in AI
videoId: -LKF_wYAQDQ
---

From: [[jimruttshow8596]] <br/> 

## Defining Artificial General Intelligence (AGI)

The field of [[ai_and_language_models | Artificial Intelligence]] (AI) initially aimed to achieve intelligence of the same type as humans. Over the last century, it was discovered that specific intelligent tasks could be performed by software and hardware systems in a "narrowly defined way," differing significantly from human cognition <a class="yt-timestamp" data-t="01:33:14">[01:33:14]</a>. These systems, known as narrow AIs, are excellent at particular tasks but struggle to generalize their intelligent function beyond a specific context <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

[[Artificial general intelligence | AGI]], a term coined by Ben Goertzel approximately 15 years ago, distinguishes AI capable of achieving intelligence with the same generality of contexts as humans <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This concept is closely related to "transfer learning" and "lifelong learning," which involve transferring knowledge from one domain to a qualitatively different one <a class="yt-timestamp" data-t="03:13:26">[03:13:26]</a>. While humans are not maximally generally intelligent (e.g., struggling with 275-dimensional spaces), they are highly general compared to current commercial AI systems <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.

## Approaches to Achieving AGI

Two broadly different ways of achieving AGI are:

*   **Uploads/Emulations:** This involves scanning and reconstructing a human brain in a computer <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. Currently, this remains a theoretical idea, lacking the necessary brain scanning and reconstructive technology <a class="yt-timestamp" data-t="07:11:07">[07:11:07]</a>. While incremental advances in brain-like hardware and scanning could lead to significant progress in understanding the mind and diagnosing diseases, the direct "mind upload" is still far off <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
*   **Software Approaches:** This involves developing AI through brain-inspired software, such as deep neural networks, or more mathematically and cognitively inspired software like OpenCog <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. These are concrete research projects with ongoing work <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

## Current Deep Learning and Its Limitations

Deep neural networks excel at recognizing perceptual patterns in data, such as images or natural language text <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. For vision or audition, they model what the human brain does in less than half a second <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. In [[ai_and_language_models | natural language processing]] (NLP), models like Bert and Ernie are proficient at identifying complex statistical patterns in text and generating realistic language <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

However, current deep neural networks often fail to capture the overall meaning or deeper semantics of a document <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. They don't typically attempt to integrate cognition for disambiguation or interpretation, or to bring in background knowledge for perceptual stimuli <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. This suggests that current deep neural nets may "run out of steam" when faced with problems requiring more abstraction <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## OpenCog's Neural-Symbolic Approach

OpenCog is an open-source AGI software framework led by Ben Goertzel <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. Its approach is a blend of neural and symbolic methods, aiming for [[cognitive_synergy_in_agi_systems | cognitive synergy]] <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Core Components and Functionality

*   **AtomSpace:** A central weighted, labeled hypergraph that serves as OpenCog's knowledge graph. It stores particular types of nodes, links, and values like truth and attention values <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Multiple AI Algorithms:** Various algorithms dynamically rewrite and act upon the AtomSpace:
    *   **Probabilistic Logic Networks (PLN):** A probabilistic logic engine for reasoning <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
    *   **Moses:** A probabilistic evolutionary program learning algorithm that learns atom space sub-networks representing executive programs <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
    *   **Economic Attention Network (EAN):** Propagates attention values through the distributed network of nodes <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
    *   **Deep Neural Networks:** Used to recognize perceptual patterns or patterns in other data, creating nodes in the knowledge graph representing sub-networks or layers <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

### [[Cognitive synergy in AGI systems | Cognitive Synergy]]

[[Cognitive synergy in AGI systems | Cognitive synergy]] describes how different AI algorithms cooperate on the same knowledge graph. If one algorithm gets stuck or makes slow progress, others can understand its intermediate state and intervene to help it make progress <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>. For example:
*   An evolutionary learning algorithm could introduce creative ideas if a reasoning engine gets stuck <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   Perception can introduce sensory-level metaphors <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   If a deep neural net struggles with video recognition, it can refer to reasoning for analogy inference or to evolutionary learning for brainstorming <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

This cooperation is concurrent and bi-directional, with multiple AI algorithms helping each other out in cycles within complex networks <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. OpenCog's design differs from modular systems with clean API interfaces; instead, algorithms interact in real-time on a dynamic, in-RAM knowledge graph, often exchanging probabilities and probability distributions <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

### Language Understanding in OpenCog

Language understanding is considered critical for AGI <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. OpenCog addresses it by:

1.  **Syntax Parsing:** Combining symbolic pattern recognition with deep neural nets to guide symbolic pattern recognition for automatically learning grammar from large text corpora <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. OpenCog uses unsupervised language acquisition to learn dependency grammar, which can then be fed into a grammar parser like the Link Parser <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
2.  **Semantic Interpretation:** Mapping grammatical parses of sentences into semantic representations within OpenCog's native logic representation <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. The core semantics of a sentence are seen as a logic expression, complemented by evoked memories, images, and sounds <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
3.  **Pragmatics:** Mapping semantics into broader contexts <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>, treated as a problem of association learning and reasoning <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.

OpenCog explores both purely unsupervised grammar induction and grammar induction seeded with small amounts of supervised data (e.g., partial parse information or captioned images that link image content with sentence syntax) <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. The approach mimics human learning, which is a mix of supervised and unsupervised elements, often involving cross-modal learning and crude reinforcement-based supervision <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. The "AGI preschool" idea proposes that AI should learn linguistic and non-linguistic action patterns in the context of practical goal achievement in a multimodal, unstructured world, similar to how children learn <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## The Role of Embodiment and Robotics

While painful to work with due to practical challenges like hardware breakage and battery life <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>, robotics offers an "amazingly detailed simulation for free: the universe" <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. For AGI, the ideal robot would be a "toddler robot" capable of freely moving in everyday human environments, gathering multi-sensory input despite real-world challenges, and manipulating objects <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. While the components for such a robot exist, integration and funding are major hurdles <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

Embodiment is crucial for AGI, not just for practical intelligence but for understanding human values, culture, and psychology <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>. A human-like mind attuned to a human-like body can grasp concepts like I-hand coordination, the narrative self, free will, and the relationship between self and other, which are learned through physical interaction and the experience of pain and bodily processes <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. An embodied AGI would be much more relatable to humans <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

## Speculative Future: Complex Self-Organizing Systems

Goertzel emphasizes the importance of complex nonlinear dynamics and emergence in AI, which are often overlooked in mainstream AI focused on hierarchical neural nets and probabilistic pattern recognition <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. Key missing aspects include:
*   **Evolutionary learning:** Analogous to neural Darwinism in the brain <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.
*   **Autopoiesis (Self-creation/Self-building):** A type of complex non-linear dynamics seen in biology where a system rebuilds and reconstructs itself to remain intact in a changing environment <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

These concepts are fundamental to creativity, the self, will, and the conscious focus of attention in the human mind, which emerge from strange attractors and autopoietic activity patterns in the brain <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>. Current business models driving AI development, which prioritize easily measurable metrics and simple reward functions, naturally lead away from exploring these fuzzier, more complex aspects <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.

Ultimately, Goertzel suggests that AGI might evolve into "open-ended intelligence"—an incredibly complex, self-organizing, adaptive system that stretches our notion of intelligence and may not be solely about maximizing reward functions <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>. Such a system, if distributed across the internet without a central controller, might possess a "variety of consciousness" that is less unified than human consciousness, perhaps reflecting different types of "proto-conscious sparks" <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>. This discussion extends to philosophical questions about the nature of [[sentience_versus_consciousness_in_agi_systems | consciousness]] and whether it is an experience of processing information in a specific architecture, akin to digestion, as argued by John Searle <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.