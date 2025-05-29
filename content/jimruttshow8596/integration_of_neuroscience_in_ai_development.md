---
title: Integration of neuroscience in AI development
videoId: isIrLmYTdvU
---

From: [[jimruttshow8596]] <br/> 

The development of Artificial General Intelligence (AGI) aims to create computer systems that can perform tasks considered intelligent when done by humans, especially those they were not specifically programmed or trained for <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Ben Goertzel, who coined the term AGI <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, believes that current mainstream AI, primarily [[interfacing_ai_with_deep_neural_networks_and_transformers | deep neural networks]] (DNNs) and machine learning (ML) algorithms, are fundamentally unsuited for achieving human-level AGI <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

## [[The limitations of current AI architectures | Limitations of Current AI Architectures]]

Current AI approaches, largely dominated by DNNs, excel at narrow tasks based on extensive data-driven training <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Examples like AlphaFold, which predicts protein folding based on training data, struggle with variations outside their specific training sets, such as "floppy proteins" or entirely new classes of molecules <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Humans, by contrast, can improvise and generalize to loosely connected or new domains <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The core issue is that DNNs primarily recognize "shallow patterns" in data, acting like sophisticated lookup tables <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. They don't build a model of the underlying reality <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. For example, a DNN might suggest using a "table saw" to fit a table through a door, assuming it's a saw for tables, despite having documentation in its training data that explains its true function <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This reliance on vast data and processing power for particular patterns limits their ability to generalize to domains without that specific data <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. The ability to generalize to different domains relies on finding concise abstractions of experience <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

This focus on narrow AI is driven by commercial viability; businesses often need AI that can repeat well-understood operations to maximize metrics, rather than systems that are creative and unpredictable <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.

## Three Viable Paths to AGI

Ben Goertzel's essay, "Three Viable Paths to True AGI," outlines alternative [[innovative_approaches_in_ai_research | approaches in AI research]]. While he believes current DNNs can be significant components of an AGI system, they are incomplete <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### 1. Cognitive Level Approach: Hybrid Neural-Symbolic Evolutionary Metagraph Based AGI

This approach, exemplified by the OpenCog project and its new version, OpenCog Hyperon <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>, is inspired by how the [[mind_and_artificial_intelligence | human mind]] functions at a high level <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>. It involves identifying various cognitive functions like perception, action, planning, [[role_of_emotions_and_longterm_memory_in_ai_and_human_cognition | working memory]], and [[role_of_emotions_and_longterm_memory_in_ai_and_human_cognition | long-term memory]] <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>. The goal is to implement each of these functions using the best available computer science algorithms and then integrate them into a coherent architecture <a class="yt-timestamp" data-t="00:35:51">[00:35:51]</a>.

A key aspect is "cognitive synergy," where neural subnetworks carrying out distinct cognitive functions transparently help each other at a deep level <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. OpenCog uses a large, distributed knowledge graph (hypergraph or metagraph) where different AI algorithms interact on this common knowledge base <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

Addressing the "good old-fashioned AI" (GOFAI) critique, Goertzel argues that his approach differs by:
*   Using fuzzy, probabilistic, paraconsistent intuitionistic logic, allowing for uncertainty and contradictions <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>.
*   Not relying on hand-coding common sense knowledge, but rather on learning <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.
*   Integrating [[approaches_to_evolving_ai_architectures | evolutionary learning]] and other AI ideas alongside logic <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>.

Evolutionary aspects are present implicitly through attention-driven premise selection and uncertain logical reasoning, where importance acts as a fitness value <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>. Explicit [[approaches_to_evolving_ai_architectures | genetic algorithms]] are also used for procedure learning and creativity, like evolving new logical predicates <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>.

### 2. Brain Level Approach: Large-Scale Non-linear Dynamical Brain Simulation

This path involves direct simulation of the brain's complex non-linear dynamics <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. Unlike simplified DNNs, this aims for biological realism, considering various cell types (neurons, glia, astrocytes) and processes like cellular and charge diffusion, and even potential "wet quantum biology" <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>.

A major challenge is the lack of adequate measuring instruments to fully understand brain processes, particularly abstraction formation <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a>. Early efforts like the Blue Brain Project aimed in this direction, and work by Gerald Edelman and Eugene Izhikevich explored chaos theory-based neuron models for holistic brain simulation <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

Recent developments include Alex Ororbia's predictive coding-based learning mechanism, which could replace backpropagation in DNNs <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>. This method allows for more biologically realistic neurons (e.g., Izhikevich neurons with sub-threshold spreading of activation) and potentially better generalization, as it can learn structured semantic representations that interface more cleanly with logic-based systems like OpenCog <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

Hardware poses another challenge, as the inherently parallel nature of the brain is poorly matched by current Von Neumann (serial) computing architectures <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. While GPUs offered parallelization for DNNs, more sophisticated parallel hardware is needed for full brain simulations <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a>. Specialized chips optimized for Izhikevich neurons or graph pattern matching (like the one Goertzel is working on) are being developed <a class="yt-timestamp" data-t="01:04:27">[01:04:27]</a>. The viability of custom hardware development is increasing, potentially leading to AGI boards with various specialized chips within three to five years <a class="yt-timestamp" data-t="01:07:25">[01:07:25]</a>.

### 3. Chemistry Level Approach: Massively Distributed AI Optimized Artificial Chemistry Simulation

Inspired by artificial life and biochemistry, this approach explores the emergence of intelligence from simulated chemical reactions <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>. Pioneering work includes Walter Fontana's "algorithmic chemistry," where abstract programs act on each other to produce new programs in complex reaction chains <a class="yt-timestamp" data-t="01:18:43">[01:18:43]</a>.

The idea is to go beyond merely simulating biological evolution and instead evolve the underlying "chemistry" or gene expression machinery itself, to find more expressive representations for intelligence <a class="yt-timestamp" data-t="01:20:19">[01:20:19]</a>. This involves making artificial life models more fine-grained, leading to artificial biochemistry <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>.

A significant hurdle is the immense computational resources required for simulating realistic chemistry <a class="yt-timestamp" data-t="01:26:24">[01:26:24]</a>. An abstracted approach, such as algorithmic chemistry using a modern programming language like Meta, might circumvent some of these computational costs <a class="yt-timestamp" data-t="01:27:01">[01:27:01]</a>.

An [[approaches_to_evolving_ai_architectures | innovative approach]] is "directed chemical evolution," where machine learning algorithms observe the evolving chemical soup, identify promising "vats," and then generate new chemical configurations based on successful ones <a class="yt-timestamp" data-t="01:29:08">[01:29:08]</a>. This could be implemented in a decentralized manner, with millions of users running virtual algorithmic chemistry soups on their machines <a class="yt-timestamp" data-t="01:32:13">[01:32:13]</a>.

## Funding and Future Outlook

Currently, [[artificial_intelligence_risk | AGI research]], especially in these less mainstream areas, is significantly underfunded compared to narrow AI or other global expenditures <a class="yt-timestamp" data-t="01:25:17">[01:25:17]</a>. This is partly due to the long-term, uncertain nature of AGI development, which doesn't offer quick commercial returns <a class="yt-timestamp" data-t="01:29:27">[01:29:27]</a>. There's also a cultural tendency among newer AI researchers to focus on short-term results <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>.

Goertzel suggests that a breakthrough in AGI could catalyze both government funding and a grassroots cultural shift, similar to the rise of open-source software <a class="yt-timestamp" data-t="01:47:01">[01:47:01]</a>. While big tech companies may continue to prioritize controllable AI for financial return, a more open and collaborative research environment could accelerate AGI development <a class="yt-timestamp" data-t="01:48:51">[01:48:51]</a>. The first viable path to AGI may be a hybrid approach, capable of integrating ideas from other paradigms, such as biologically realistic neural nets for perception or algorithmic chemistry for creative idea generation <a class="yt-timestamp" data-t="01:38:40">[01:38:40]</a>.