---
title: OpenCog and its approach to AGI
videoId: -LKF_wYAQDQ
---

From: [[jimruttshow8596]] <br/> 

[[ben_goertzels_views_on_artificial_general_intelligence_agi | Ben Goertzel]], a leading figure in the pursuit of [[Artificial General Intelligence AGI challenges and possibilities | Artificial General Intelligence]] (AGI), coined the term "AGI" approximately 15 years ago <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. He is the leader of the OpenCog open-source AGI software framework <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> and CEO of SingularityNET, a distributed network for creating, sharing, and monetizing AI services <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Defining AGI and Distinguishing from Narrow AI

In the mid-20th century, the informal goal of the AI field was to achieve human-like intelligence <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. However, over decades, researchers found it possible to create software and hardware systems that performed specific intelligent tasks, but in ways very different from humans and within narrowly defined contexts <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. For example, a chess program could play like a grandmaster but couldn't play Scrabble without reprogramming <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This led to the "narrow AI revolution," where systems excel at particular tasks but cannot generalize their intelligent function beyond their specific, narrow contexts <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. [[comparison_of_narrow_ai_and_agi | AGI]], by contrast, refers to AI capable of achieving intelligence with at least the same generality of contexts as humans <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Concepts like transfer learning and lifelong learning are closely related, as they involve transferring knowledge across qualitatively different domains <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. While humans are not "maximally generally intelligent" (e.g., struggling with high-dimensional spaces), they are far more general than current commercial AI systems <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Timeline for Human-Level AGI

[[progress_and_direction_towards_developing_AGI | Estimates for achieving human-level AGI]] vary, but Goertzel's stock answer is five to thirty years from now <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. A substantial plurality, possibly a majority, of AI researchers believe it will arrive within the next century <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. A small minority believes digital computers cannot achieve human-level AGI due to assumptions about the human brain being a quantum computer <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Approaches to AGI Development

Goertzel broadly categorizes [[different_approaches_to_agi_development_beyond_mainstream_methods | AGI development approaches]] into two main types:

1.  **Uploads/Emulations**: This involves directly scanning and emulating a human brain <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Goertzel considers this "just an idea" currently, scientifically feasible in theory but lacking the necessary brain scanning or reconstructive technology for direct work <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. While advances in supporting technologies (brain-like hardware, accurate scanning) could bring incremental benefits for other areas like understanding the human mind or diagnosing diseases, it requires a "radical breakthrough" in imaging or extrapolation <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
2.  **Software Approaches**: This involves creating AGI through software, either broadly brain-inspired (like deep neural nets) or more mathematically and cognitively inspired (like OpenCog) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This is where active, concrete research projects are focused <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Goertzel favors "heterogeneous approaches" that leverage existing hardware and knowledge, including insights from brain function, in an opportunistic way <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### OpenCog's Core Design

OpenCog is a software-based approach to AGI, distinct from mainstream deep learning <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

> "OpenCog... then the singularity network each of these reflects different aspects of what we were trying to do in web mind so web mind was really a bunch of agents which was sort of heterogeneous that we're supposed to cooperate to form an emergently intelligence system now OpenCog we tried to control things a lot more" <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>

OpenCog's [[history_and_evolution_of_the_opencog_project | history]] dates back to the mid-90s with the "Webmind" project, inspired by Marvin Minsky's "society of mind" concept, but with a greater focus on emergence and self-organizing complex systems <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. After Webmind's commercial failure, Goertzel started building the "Novamente Cognition Engine," much of which became OpenCog <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

OpenCog's architecture includes:
*   **Atomspace**: A knowledge graph that is a weighted, labeled hypergraph with specific node and link types, and values like truth values and attention values <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   **Multiple AI Algorithms**: These algorithms dynamically rewrite the Atomspace and assist each other. Key examples include:
    *   **Probabilistic Logic Networks (PLN)**: A probabilistic logic engine for reasoning <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
    *   **MOSES**: A probabilistic evolutionary program learning algorithm that learns Atomspace subnetworks representing programs <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
    *   **Economic Attention Networks**: Propagates attention values through the distributed network of nodes <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
    *   **Deep Neural Networks**: Used for recognizing perceptual patterns and creating nodes in the knowledge graph from deep neural network layers <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

### [[cognitive_synergy_in_agi_systems | Cognitive Synergy]]

The core concept in OpenCog is [[cognitive_synergy_in_agi_systems | cognitive synergy]] <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. This refers to the process where different AI algorithms cooperate to help each other when one gets stuck or makes slow progress <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. For example, if a reasoning engine is stuck, evolutionary learning might introduce creative ideas, or perception could introduce sensory-level metaphors <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. This cooperation is concurrent, with algorithms acting on the same dynamic knowledge graph, rather than through clean API interfaces of modular systems <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. The algorithms are "uncertainty savvy" and exchange probabilities <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

This bi-directional, multi-level processing is a key advantage of OpenCog. For instance, high-level clues can flow back from higher mind levels to the perceptual system to aid in object identification, a feature not typically seen in current deep learning projects <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

> "I think this sort of neural symbolic approach to AI is gonna be very big three or four years from now because deep neural Nets in their current form we're gonna run out of steam" <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>

Goertzel predicts a convergence between symbolic logic systems and neural networks, with more powerful logic engines interacting with knowledge graphs and deep neural nets <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

## Language Understanding

Language understanding is considered critical for the AGI project, second only to meta-reasoning (reasoning about reasoning) <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. OpenCog is working on hybridizing its symbolic language understanding with deep neural nets.

OpenCog's approach to language understanding involves:
1.  **Syntax Parsing**: Using a combination of symbolic pattern recognition and deep neural nets to automatically learn grammar from large text corpora <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
2.  **Semantic Interpretation**: Mapping grammatical parses of sentences into logical expressions within OpenCog's native logic representation, supplemented by links to images, episodic memories, and sounds <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
3.  **Pragmatics**: Mapping semantics into a broader context, treated as a problem of association learning and reasoning <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.

OpenCog focuses on unsupervised language acquisition, aiming for a system that automatically learns dependency grammar <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>. Progress is being made, with the system improving its parsing capabilities <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>. Interestingly, even a small amount of "partial parse information" from supervised data (like mappings of word links to semantic relations) can significantly improve unsupervised learning results <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This reflects how humans learn, combining linguistic productions with non-linguistic environments <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>.

## Robotics and Embodiment in AGI

Robotics provides an "amazingly detailed simulation for free" – the universe itself <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. While working with robots presents practical challenges (e.g., stuff breaks, battery life), the main issue for AGI is the current limitation of robots in performing what an AGI needs, such as moving freely in everyday human worlds, gathering multi-sensory input robustly, and manipulating objects like a toddler <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.

Although components exist (e.g., Boston Dynamics for movement, Hanson Robotics for expression, iCub for coordination), an "artificial toddler" robot integrating all these parts is not yet funded or realized <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>. Goertzel believes it's years, not decades, away from being resolved, primarily an integration challenge <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.

While AGI doesn't strictly *need* a robot body (a "superhuman supermind living on the internet" is conceivable <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>), a human-like body is valuable because many aspects of the human mind are attuned to it. Embodiment helps in understanding human values, culture, and psychology <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.

## SingularityNET: A Decentralized AI Ecosystem

SingularityNET is a [[efforts_in_creating_a_scalable_infrastructure_for_agi | distributed network]] that allows anyone to create, share, and monetize AI services at scale <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. It reflects Goertzel's long-held ideas from the Webmind project (late 1990s) about a distributed network of autonomous agents cooperating to manifest emergent intelligence <a class="yt-timestamp" data-t="00:49:29">[00:49:29]</a>. Unlike OpenCog, which tightly controls AI algorithms on a common knowledge store, SingularityNET is a "society of minds" where diverse AI agents can interact via APIs without needing to understand each other's internal workings <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

Key features of SingularityNET include:
*   **Economy of Mind**: A payment system where AIs pay each other for work or get paid by external agents <a class="yt-timestamp" data-t="00:50:21">[00:50:21]</a>. This economic aspect contributes to emergent AI by facilitating value assessment and credit assignment <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.
*   **Decentralized Infrastructure**: Uses blockchain technology as plumbing to enable AI agents to interact without a central controller, promoting a participatory, democratic interaction <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>.

### Importance of Decentralized AI

Goertzel emphasizes the multi-fold importance of a decentralized and open approach to AI:
*   **Enabling Good**: It can allow AI to do more good in the world than a centralized, hegemonic approach <a class="yt-timestamp" data-t="00:53:45">[00:53:45]</a>. Current centralized AIs are predominantly focused on "selling, spying, killing, and gambling" <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a> (advertising, surveillance, weapons, financial prediction) <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>. A decentralized approach could foster AIs focused on "educating, curing diseases, doing science, helping old people, creating art" <a class="yt-timestamp" data-t="00:54:43">[00:54:43]</a>.
*   **Future AGI Values**: If narrow AIs evolve into AGIs, decentralized development increases the likelihood that these AGIs will pursue "compassionate and aesthetically creative" goals <a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>.
*   **Countering Concentration**: SingularityNET aims to be a counter-trend to the increasing concentration of deep AI progress in the hands of a few large corporations <a class="yt-timestamp" data-t="00:53:19">[00:53:19]</a>. This concentration is driven by powerful network effects (accumulation of money, data, processing power) that favor early success in widely deployed narrow AI tasks <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>. SingularityNET seeks to leverage similar two-sided platform network effects (AI supply from developers, AI demand from product developers and end users) to scale a decentralized network <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>. The ambition is to have a major impact like Linux did, even if it doesn't entirely displace big tech <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>.

### Go-to-Market Strategy for SingularityNET

SingularityNET focuses on building the demand side of its market first, while training supply internally <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>:
*   **Singularity Studio**: A for-profit company aimed at building commercial products (initially in FinTech, then IoT, health tech) on top of the SingularityNET platform <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>. Licensing fees for these products will convert fiat currency into AGIX tokens to drive the network's market <a class="yt-timestamp" data-t="01:02:36">[01:02:36]</a>.
*   **SingularityNET X-lab Accelerator**: Recruits community projects to build software products for niche markets, leveraging AI on SingularityNET. These projects contribute to both demand and supply <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>.

The goal is to achieve significant utilization of the AGIX token, creating a "utility token with actual utility," which is rare in the blockchain space <a class="yt-timestamp" data-t="01:04:39">[01:04:39]</a>. This will attract more AI developers to the platform due to the combination of financial incentives and the cool, democratizing vision <a class="yt-timestamp" data-t="01:05:09">[01:05:09]</a>.

## Complex Self-Organizing Systems and Emergence

Goertzel's approach to AGI is deeply rooted in complex nonlinear dynamics and emergence, setting it apart from mainstream AI <a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a>. He argues that current hierarchical neural networks, while important, miss crucial aspects of intelligence like:
*   **Evolutionary Learning**: Present in the brain (e.g., sensory-motor Darwinism) <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>.
*   **Nonlinear Dynamics and Emergence**: Including strange attractors, which are key to how the brain synchronizes and coordinates its parts <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a>.
*   **Autopoiesis (Self-Creation)**: The self-building and self-reconstruction of systems, evident in biology and the immune system <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.

> "If you leave out ecology slash other places in evolution and you have only hierarchical pattern recognition you're leaving out a whole lot of what makes the even mind interesting like creativity is evolution and you know the self and the will and all these and you know the conscious focus of attention which is binding together different parts of the mind into a perceived impractical unity this is all about strange attractors emerging in the brain building you know autopoietic systems of activity pattern so you're leaving out all this like you do in modern deep learning systems well you're leaving out a of a lot about what makes the human minds interesting" <a class="yt-timestamp" data-t="01:09:25">[01:09:25]</a>

Goertzel views AGI ultimately as a "self-organizing complex adaptive dynamical system" <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. This "open-ended intelligence" might stretch our current notion of intelligence, possessing more generality than humans but not necessarily maximizing simple reward functions <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>. The nature of consciousness in such a system is an open question; it may not have the unified human-like consciousness tied to a single body but could involve a complex, diffuse pattern of "proto-conscious sparks" across a distributed network <a class="yt-timestamp" data-t="01:14:12">[01:14:12]</a>.

Goertzel's background as a panpsychist means he takes the concept of *qualia* seriously, believing elementary qualia are associated with every entity and can organize into collective system-level qualia differently based on the system's organization <a class="yt-timestamp" data-t="01:20:53">[01:20:53]</a>. He suggests that human-like consciousness is one specific variety of experience associated with systems organized like a human <a class="yt-timestamp" data-t="01:21:13">[01:21:13]</a>.