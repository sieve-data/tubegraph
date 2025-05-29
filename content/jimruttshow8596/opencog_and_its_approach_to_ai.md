---
title: OpenCog and its approach to AI
videoId: -LKF_wYAQDQ
---

From: [[jimruttshow8596]] <br/> 

[[opencog_hyperon_framework_for_agi | OpenCog]] is an open-source Artificial General Intelligence (AGI) software framework and a leading effort in the pursuit of AI at and beyond human levels <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. It is led by Ben Goertzel, a prominent figure in AGI research <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. AGI refers to AI capable of achieving intelligence with the same generality of contexts that people can <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.

## Philosophy and Origins

[[opencog_hyperon_framework_for_agi | OpenCog]]'s history predates the formal project name, tracing back to the mid-90s when Ben Goertzel conceived of an AI as an agent system, a "society of mind" as described by Marvin Minsky, but with a stronger focus on emergence <a class="yt-timestamp" data-t="01:13:03">[01:13:03]</a>. While Minsky viewed the human mind as a collection of AI agents interacting like people in a society, Goertzel emphasized the emergent level of dynamics and the emergence of overall structures in the network of agents as equally important to individual agent intelligence <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

Initial efforts in the late 1990s involved a system called WebMind, envisioned as heterogeneous agents distributed across the internet, coordinating to yield emergent intelligence <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. After WebMind's commercial failure, the Novamente Cognition Engine was developed, much of which was later open-sourced into the [[opencog_hyperon_framework_for_agi | OpenCog]] system <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## OpenCog Architecture

[[opencog_hyperon_framework_for_agi | OpenCog]]'s design focuses on controlled emergence within a carefully structured framework, unlike the more loosely coupled WebMind <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Its core components include:

*   **Knowledge Graph (AtomSpace)**: A weighted, labeled hypergraph that contains particular types of nodes and links, with values such as truth and attention attached <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Multiple AI Algorithms**: These algorithms dynamically rewrite and interact with the AtomSpace, often monitoring and assisting each other <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Examples include:
    *   **Probabilistic Logic Networks (PLN)**: A probabilistic logic engine described in a 2006 book <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
    *   **MOSES**: A probabilistic evolutionary program learning algorithm that learns AtomSpace sub-networks representing executive programs <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
    *   **Economic Attention Networks (ECAN)**: Propagates attention values through the distributed network of nodes <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
    *   **Deep Neural Networks**: Used to recognize perceptual patterns or patterns in other data, creating nodes in the knowledge graph representing sub-networks or layers in the deep neural networks <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

### [[cognitive_synergy_in_agi_development | Cognitive Synergy]]

A core concept in [[opencog_hyperon_framework_for_agi | OpenCog]] is [[cognitive_synergy_in_agi_development | cognitive synergy]], which describes how different AI algorithms cooperate <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. When one algorithm gets stuck or makes slow progress, other algorithms can understand its intermediate state and goals, then intervene to help make new progress <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. For example, if a reasoning engine is stuck, evolutionary learning might introduce creative ideas, or perception could introduce sensory-level metaphors <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This bi-directional and concurrent cooperation on the same dynamic knowledge graph distinguishes it from modular systems with clean API interfaces <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Distinction from Narrow AI and Deep Learning

Ben Goertzel coined the term AGI about 15 years prior to the discussion to differentiate it from "narrow AI," which excels at specific tasks in narrowly defined ways, often very differently from humans, and struggles to generalize beyond specific contexts <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. While narrow AI has led to a "narrow AI revolution" with astounding varieties of intelligent systems <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>, [[opencog_hyperon_framework_for_agi | OpenCog]] aims for intelligence with generality of contexts similar to humans <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. This goal necessitates capabilities like [[approaches_to_evolving_ai_architectures | transfer learning]] and lifelong learning <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

[[opencog_hyperon_framework_for_agi | OpenCog]] employs a "neural symbolic approach," combining deep neural networks for perceptual patterns with a symbolic cognitive engine (AtomSpace, PLN) <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This contrasts with many current deep learning projects that typically lack bidirectional processing and don't deeply integrate symbolic knowledge <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Key Research Areas within OpenCog

### Cognitively Informed Perception
[[opencog_hyperon_framework_for_agi | OpenCog]] aims for "cognitively informed perception," where high-level clues from the mind flow back to the perceptual system to disambiguate or interpret stimuli using background knowledge <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This is something current deep neural networks typically don't attempt <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Experiments are underway in [[opencog_hyperon_framework_for_agi | OpenCog]] to enable symbolic cognitive engines to interact in real-time with deep neural networks for perception <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

### Language Understanding
[[opencog_hyperon_framework_for_agi | OpenCog]] views language understanding as critical for AGI <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Its approach involves:
*   **Syntax Parsing**: Combining symbolic pattern recognition and deep neural nets to automatically learn grammar from large text corpora <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Semantic Interpretation**: Mapping grammatical parses of sentences into logical expressions within the AtomSpace, which can be linked to other modalities like images and episodic memories <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Pragmatics**: Mapping semantics into broader contexts through association learning and reasoning <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

Research focuses on unsupervised language acquisition, which aims to learn dependency grammar automatically <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. There is also exploration into mixed approaches, such as seeding unsupervised learning with small amounts of supervised data, like partial parse information or captioned images, mimicking how humans learn language through a mixture of supervised and unsupervised cross-modal learning <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. The "AGI preschool" idea suggests systems learning linguistic and non-linguistic patterns in the context of practical goal achievement in multimodal environments <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

### Meta-Reasoning
Goertzel identifies meta-reasoning (reasoning about reasoning) as the most critical area currently being worked on towards AGI <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Relation to Robotics and Embodiment

While AGI in principle doesn't *require* a robot, an [[opencog_hyperon_framework_for_agi | OpenCog]] system with a human-like body would be valuable <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Many aspects of the human mind, from hand-eye coordination to concepts of self and free will, are attuned to having a body that interacts with the physical world and experiences pain and perception <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Embodiment is seen as important for an AGI to understand human values, culture, and psychology and to empathize with humans <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Current robotics faces challenges in providing truly versatile "toddler robots" that can freely move and gather multi-sensory input in everyday human worlds <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## SingularityNet

[[opencog_hyperon_framework_for_agi | OpenCog]] is closely related to SingularityNet, a distributed network that allows anyone to create, share, and monetize AI services at scale <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. SingularityNet embodies the idea of a "society of minds" where different AI agents, each doing AI in their own way, interact via APIs <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This network features a payment system where AIs can charge each other or external agents for services, creating an "economy of mind" that enables emergent AI and a viable commercial ecosystem <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. The infrastructure uses blockchain to enable a self-organizing agent system without a central controller <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

SingularityNet is positioned as a counter-trend to the increasing concentration of AI development in a few large corporations <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. It aims to enable AI to do more good in the world and, if current narrow AIs evolve into AGIs, to ensure they develop compassionate and aesthetically creative goals <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Like Linux in the operating system world, SingularityNet aims to be a major force in decentralized AI, providing an open, democratically governed platform with a genuine market for AI services <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Broader Philosophical Context

Ben Goertzel's approach to AI is rooted in [[innovative_approaches_in_ai_research | complex self-organizing systems]], emergence, chaos, and strange attractors <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. He argues that mainstream AI, particularly deep learning, misses key aspects of how the brain works by focusing primarily on hierarchical pattern recognition and maximizing simply formulated reward functions <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

He highlights two fundamental forces underlying intelligent systems:
*   **Evolution**: Creation of the new from the old, driving creativity <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Autopoiesis (Self-Creation/Self-Building)**: A form of complex nonlinear dynamics seen in biology where a system continually rebuilds and reconstructs itself, maintaining integrity in a changing environment <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This relates to ecology and concepts like neural Darwinism and cell assembly theory in the brain <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

These nonlinear dynamics are crucial for aspects of [[mind_and_artificial_intelligence | mind]] like creativity, self, will, and conscious attention, which he believes are largely overlooked in modern deep learning <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

### [[debate_on_ai_understanding_and_consciousness | Consciousness]] and [[mind_and_artificial_intelligence | Mind]]

Goertzel distinguishes between human-like consciousness and broader forms of awareness or experience <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. He aligns with panpsychism, suggesting that "elementary qualia" (the subjective qualities of experience) are associated with every entity and can organize into collective system-level qualia depending on the system's organization <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Human-like consciousness, with its unity, is seen as driven by the need to control a unified, mobile body to achieve goals like survival <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

He acknowledges that a distributed, self-organizing dynamical system across the internet might have a "variety of consciousness" or a "conglomeration of proto-conscious sparks" that is far less unified than human consciousness <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This leads to the concept of "open-ended intelligence," which may stretch traditional notions of intelligence and not be primarily about maximizing reward functions <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. While the speaker and Goertzel have some differing views on the precise definition of [[debate_on_ai_understanding_and_consciousness | consciousness]] (e.g., John Searle's "Chinese Room" argument and the analogy to digestion), they agree that understanding human-like consciousness is a specific problem distinct from the broader nature of [[mind_and_artificial_intelligence | mind]] and awareness in complex systems <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Prospects for AGI

Ben Goertzel's stock answer for when human-level AGI might appear is five to thirty years from the time of the discussion <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. He notes that the mean and variance of such estimates within the AI community have significantly decreased over the past decade, with a substantial plurality now believing it will arrive within the next century <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. He emphasizes that achieving [[possibilities_for_achieving_humanlevel_agi | human-level AGI]] might require substantially new approaches beyond incrementally improving current narrow AI systems <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

He identifies two broad paths to AGI:
1.  **Software Approaches**: Loosely brain-inspired software (like deep neural nets) or more math and cognitive science-inspired software (like [[opencog_hyperon_framework_for_agi | OpenCog]]) <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. This path is currently the subject of concrete research projects <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.
2.  **Brain Uploads/Emulations**: Directly scanning and representing a human brain's neural system (connectome) in a computer <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. While scientifically feasible according to known physics, this is currently "just an idea" due to the lack of necessary brain scanning and reconstructive technology <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. Incremental progress in brain-like hardware and accurate brain scanning would still yield valuable advancements for understanding the [[mind_and_artificial_intelligence | human mind]] and diagnosing diseases <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. However, Goertzel believes that [[opencog_hyperon_framework_for_agi | OpenCog]]'s [[integration_of_neuroscience_in_ai_development | heterogeneous and opportunistic]] approach to AGI, leveraging existing hardware and knowledge while drawing from brain science, is more practical <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. He anticipates a convergence of symbolic (like OpenCog) and neural (like deep learning) approaches in the coming years <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.