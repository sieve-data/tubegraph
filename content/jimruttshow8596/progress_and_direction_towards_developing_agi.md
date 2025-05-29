---
title: Progress and direction towards developing AGI
videoId: Z5dompWURVo
---

From: [[jimruttshow8596]] <br/> 

The field of Artificial Intelligence (AI) is experiencing rapid advancements, particularly in the realm of [[artificial_general_intelligence_agi_challenges_and_possibilities | Artificial General Intelligence (AGI)]]. The pace of change in AI is compared to the emergence of PCs in the late 1970s and early 1980s, but happening "10 times faster" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This exponential acceleration, as projected by Ray Kurzweil, is occurring differentially across various areas of AI pursuit <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Dr. [[ben_goertzels_views_on_artificial_general_intelligence_agi | Ben Goertzel]], a leading authority on [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] and the instigator of the [[opencog_and_its_approach_to_agi | OpenCog]] project, believes the unfolding of [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] is accelerating <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. He maintains a high probability of [[the_emergence_of_agi_and_estimated_timelines | AGI]] within five years, even increasing his previous 50/50 chance to 60/40 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Defining Artificial General Intelligence (AGI)

Defining [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] is a complex and highly debated topic, similar to how biology lacks a universally agreed-upon definition for "life" <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.

One perspective, rooted in algorithmic information theory and statistical decision theory, views [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] as the ability to achieve a vast variety of goals in diverse environments <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. This can be formalized, as Marcus Hutter and Shane Leg (a co-founder of DeepMind) did, as a weighted average of how well a reinforcement learning system achieves all computable reward functions <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. However, this definition suggests humans are "complete retards" at optimizing arbitrary reward functions <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

Another philosophical approach, like Weaver's theory of open-ended intelligence, considers intelligence as complex self-organizing systems maintaining their existence, boundaries, and self-transforming <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

### Human-Level General Intelligence

When discussing human-level or human-like [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]], the focus shifts to specific human capabilities <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. While IQ tests offer a measure, they are considered imperfect for assessing true human intelligence <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. More multifactorial views, like Gardner's theory of multiple intelligences (musical, literary, physical, existential, logical), offer a closer approximation <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>. Ultimately, the field of psychology doesn't provide a rigorous, data-driven assessment of human intelligence <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

The Turing Test, which assesses an AI's ability to imitate a human in conversation, was never considered a strong measure of general intelligence, as "fooling people can be disturbingly easy" <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>. With current [[artificial_general_intelligence_agi_challenges_and_possibilities | AI]] systems approaching its capabilities without true [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]], it is no longer taken seriously as an [[comparison_of_narrow_ai_and_agi | AGI]] benchmark <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.

## Limitations of Current AI: Large Language Models (LLMs)

[[comparison_of_narrow_ai_and_agi | Large Language Models (LLMs)]] in their current form (Transformer Nets trained to predict the next token) are not expected to lead to full human-level [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. However, they are capable of many amazing and useful functions and can be valuable components of [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] systems <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

The fundamental limitations of LLMs stem from their architecture, which primarily recognizes surface-level patterns in data <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. This leads to several key weaknesses:

### Hallucination Problem

LLMs are known for "hallucinating" or making up facts, especially when asked obscure questions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. While models like GPT-4 have improved, this remains a challenge <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

[!NOTE] **Proposed Solutions for Hallucination**
*   **Probing the Network:** It may be possible to solve hallucination by analyzing the network's internal activation patterns to detect when it's hallucinating, allowing for filtering <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **Entropy/Paraphrasing:** Correct answers tend to have different entropy than incorrect ones <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Asking an LLM to paraphrase a query multiple times and comparing the consistency of answers can help detect hallucinations <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

While these solutions are useful for practical applications, they don't necessarily advance [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]], as human hallucination avoidance stems from a "reality discrimination function" and reflective self-modeling <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Lack of Complex Multi-step Reasoning

LLMs struggle with complex, multi-step reasoning required for tasks like writing an original science paper <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. While they can "turn the crank" on advanced math given an initial idea, they cannot originate novel scientific concepts or discern the "aesthetic" quality of mathematical definitions that lead to useful theorems <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>. This limitation is tied to their fundamentally derivative and imitative character <a class="yt-timestamp" data-t="00:33:20">[00:33:20]</a>.

### Lack of Original Artistic Creativity

LLMs also exhibit a "banality" in their output, as they average existing utterances <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>. While clever prompting can push them beyond their centers and produce results comparable to a professional journeyman's first draft (e.g., movie scripts, blues guitar solos), they cannot achieve the groundbreaking creativity of an Einstein, Thelonious Monk, or Jimi Hendrix <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. They cannot invent new musical styles or fundamentally surprising scientific theories <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.

Human intelligence, particularly the ability to abstract, is guided by "agentic nature" – the need to survive, reproduce, and self-transform within an environment <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>. This agentic drive leads to the development of heuristics and abstractions that allow for adaptation to new situations <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>.

## Different Paths to AGI Development

The pursuit of [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] is currently a genuine race among large companies <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Different approaches are being explored:

### Neural Net Universe (e.g., DeepMind, Google)

One promising direction involves enhancing existing neural network architectures <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>:
*   **Increased Recurrence:** Adding more recurrence into Transformer networks, similar to LSTMs, could foster deeper abstractions <a class="yt-timestamp" data-t="00:47:13">[00:47:13]</a>.
*   **Alternative Training Methods:** Replacing or complementing backpropagation with methods like predictive coding could improve training for complex recurrent networks <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>.
*   **Hybrid Architectures:** Combining elements like AlphaZero (for planning) with neural knowledge graphs (like in Differential Neural Computing) and recurrent Transformers could be powerful <a class="yt-timestamp" data-t="00:48:38">[00:48:38]</a>. Google and DeepMind are ideally suited for this due to their expertise in these areas <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>.
*   **Minimum Description Length Learning:** Yoshua Bengio's group is exploring neural nets explicitly designed to learn abstractions through minimum description length principles, coupled with Transformers <a class="yt-timestamp" data-t="00:49:49">[00:49:49]</a>.

### OpenCog/Hyperon Approach

Dr. Goertzel's [[opencog_and_its_approach_to_agi | OpenCog Hyperon]] project represents a different approach, prioritizing a self-modifying, self-rewriting metagraph at its core <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>.

[!INFO] **OpenCog Hyperon's Core Philosophy**
*   **Weighted Labeled Metagraph:** The central component is a highly flexible graph structure where links can connect multiple nodes, point to other links or subgraphs, and be typed and weighted <a class="yt-timestamp" data-t="00:54:59">[00:54:59]</a>.
*   **Knowledge Representation:** This metagraph represents various forms of knowledge (apostolic, declarative, procedural, attentional, sensory) and cognitive operations (reinforcement learning, logical reasoning, sensory pattern recognition) <a class="yt-timestamp" data-t="00:55:22">[00:55:22]</a>.
*   **Meta Programs:** Learning programs themselves are represented as sub-metagraphs within the larger graph, enabling them to act on, transform, and rewrite chunks of the same metagraph they reside in <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>.
*   **Reflection:** Unlike LLMs, [[opencog_and_its_approach_to_agi | OpenCog]] is highly oriented towards reflection, recognizing patterns within its own mind, processes, and execution traces, and representing those patterns internally <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>.
*   **Integration of AI Paradigms:** This framework naturally accommodates historical [[artificial_general_intelligence_agi_challenges_and_possibilities | AI]] paradigms like logical inference and evolutionary programming, as well as new approaches like "mutually rewriting sets of rewrite rules" <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.
*   **LLMs as Supporting Actors:** LLMs can exist on the periphery of this system, feeding into and interacting with the metagraph, but are not the central hub <a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>.

This approach is considered "least humanlike" but offers a "really short" path from human-level [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] to superhuman [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] because the system is designed for self-rewriting its own code <a class="yt-timestamp" data-t="00:59:41">[00:59:41]</a>. It is also well-suited for scientific discovery and artistic creativity due to its support for logical reasoning and evolutionary learning <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.

## Challenges and Future Outlook

A primary challenge for the [[opencog_and_its_approach_to_agi | OpenCog Hyperon]] project is [[efforts_in_creating_a_scalable_infrastructure_for_agi | scalability of infrastructure]] <a class="yt-timestamp" data-t="01:00:45">[01:00:45]</a>. Just as powerful multi-GPU servers were crucial for the advancement of LLMs, a scalable processing infrastructure is needed to validate the [[opencog_and_its_approach_to_agi | OpenCog]] approach <a class="yt-timestamp" data-t="01:01:24">[01:01:24]</a>. The project is developing a pipeline from its native language, Meta, to highly efficient languages like Rholang (designed for multi-CPU cores) and HyperVector math, eventually aiming for specialized hardware like associative processors (APUs) <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.

The hope is that this new infrastructure will enable ancient [[artificial_general_intelligence_agi_challenges_and_possibilities | AI]] paradigms like logical reasoning and evolutionary programming to operate at scale, and provide a flexible environment for experimenting with novel [[artificial_general_intelligence_agi_challenges_and_possibilities | AI]] algorithms <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. While the [[opencog_and_its_approach_to_agi | Hyperon]] project may not have advanced as rapidly as LLMs, it is meeting its technical milestones ahead of schedule, with more funding and better tooling available now than in previous decades <a class="yt-timestamp" data-t="01:05:15">[01:05:15]</a>. LLMs themselves are proving helpful for various aspects of non-LLM [[artificial_general_intelligence_agi_challenges_and_possibilities | AI]] projects, contributing to an overall acceleration in the field <a class="yt-timestamp" data-t="01:05:29">[01:05:29]</a>.