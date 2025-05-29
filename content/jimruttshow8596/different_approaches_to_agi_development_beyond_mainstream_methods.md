---
title: Different approaches to AGI development beyond mainstream methods
videoId: isIrLmYTdvU
---

From: [[jimruttshow8596]] <br/> 

Artificial General Intelligence (AGI) refers to computer systems capable of performing intelligent tasks they weren't specifically programmed or trained for, mimicking human-like adaptability across various domains <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. Unlike [[comparison_of_narrow_ai_and_agi | narrow AI]] that excels at particular tasks based on extensive programming or data training, AGI would possess the ability to generalize and improvise in new, loosely connected domains <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. The term [[artificial_general_intelligence_agi_challenges_and_possibilities | artificial general intelligence]] was coined by Ben Goertzel <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>, who is a leading authority in the field and the instigator behind the [[opencog_and_its_approach_to_agi | OpenCog]] project <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

While the concept of AGI is no longer considered a pariah subject, a consensus on the most viable route to achieve it is still lacking <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. Ben Goertzel's essay, "Three Viable Paths to True AGI," outlines alternative pathways beyond the current mainstream focus on deep neural networks (DNNs) <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>.

## Critique of Mainstream Deep Neural Networks for AGI

Most current AI and machine learning advancements, including [[differences_between_generative_ai_and_agi | Generative AI]] like DALL-E 2 and GPT-3, are based on deep neural networks or their close relatives <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Ben Goertzel fundamentally views these methods as "unsuited for the creation of human level AGI" <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

While deep neural networks can serve as significant components of an AGI architecture <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>, they lack crucial aspects required for human-level intelligence <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. The core limitation is their tendency to act as "very large lookup tables" that primarily identify "shallow patterns" or "surface level patterns" in data <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This means they are excellent at recognizing and extrapolating from highly specific patterns within massive datasets <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>, but struggle with genuine generalization to novel domains <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

For instance, a transformer neural network, when asked how to fit a large table through a small door, suggested using a "table saw," misinterpreting the tool based on shallow linguistic patterns rather than an underlying understanding of objects and space <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. This highlights their inability to build a robust model of reality underlying the text or data they process <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Humans, by contrast, can make "significant leaps into the unknown" based on limited experience, forming concise abstractions that enable generalization to different domains <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

> "current deep neural that's a very large lookup tables like they're just kind of recording what they saw indexing it in a clever way and then when they see a new situation they're looking up the most re the most relevant things in their history and just using them to to supply a response" <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>

The prevailing economic landscape also contributes to this focus. Current DNNs excel at tasks that offer clear commercial value, such as optimizing ad clicks or generating graphic permutations of existing styles, where predictable outcomes and measurable metrics are prioritized over imaginative creativity <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. This has led the AI industry to self-organize around approaches that best leverage these capabilities, leaving more exploratory AGI research underfunded <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

## Three Viable Paths to AGI

Beyond mainstream DNNs, Ben Goertzel outlines three promising, though currently underfunded, approaches to AGI.

### 1. Cognitive Level Approach: Hybrid Neural-Symbolic Evolutionary Metagraph-Based AGI

This approach, exemplified by the [[opencog_and_its_approach_to_agi | OpenCog]] project, seeks to emulate high-level human cognitive functions using advanced computer science algorithms, rather than attempting a low-level biological simulation <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. It draws inspiration from observed human mental processes (perception, action, planning, memory, social reasoning) and aims to implement them with effective algorithms that interact synergistically <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

Key features include:
*   **Hybrid Neuro-Symbolic System:** Combining symbolic logic for knowledge representation with neural network components <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Metagraph-Based Knowledge Representation:** Using a large, distributed knowledge graph (hypergraph/metagraph) where different nodes and links represent knowledge with varying types and weightings <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Diverse AI Algorithms:** Various AI algorithms (perception, action, reasoning, learning) act on this common knowledge graph, with internal processing transparency to enable "cognitive synergy" <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
*   **Evolutionary Aspects:** Even without explicit genetic algorithms, processes like attention-driven premise selection for uncertain logical reasoning can be described by population genetics <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Explicit genetic algorithms are also used for procedure learning and creativity <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Novel Programming Language:** [[opencog_and_its_approach_to_agi | OpenCog]] Hyperon, a new version of the system, uses a new programming language called Meta (Mettā) designed to abstract and unify different learning and reasoning algorithms <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

This approach addresses the "good old-fashioned AI" criticisms by incorporating uncertainty (e.g., fuzzy probabilistic paraconsistent intuitionist logic) and relying on learning rather than solely hand-coding common sense knowledge <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

### 2. Brain-Level Approach: Large-Scale Non-Linear Dynamical Brain Simulation

This path involves simulating the brain at a detailed biological level, focusing on the non-linear dynamics of neurons and other brain components (glia, astrocytes, cellular diffusion) <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Unlike simplified DNNs that use abstract models like ReLU transfer functions, this approach would utilize more biologically realistic neuron models, such as Hodgkin-Huxley or Izhekevich neurons, which exhibit chaotic dynamics <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

Challenges for this approach include:
*   **Measurement Limitations:** Current brain imaging instruments cannot provide sufficient time-series data of neural activity across large brain areas to fully reverse-engineer brain function <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
*   **Compute Resources:** Highly detailed simulations of a brain with billions of realistic neurons and glia require massive parallel processing capabilities, which current Von Neumann architectures struggle to provide efficiently <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Specialized chips optimized for chaotic neuron models are needed <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

Despite these hurdles, there is optimism that advancements in biologically realistic learning algorithms, like predictive coding-based learning (e.g., Alex Ororbia's work), could lead to neural networks with better generalization capabilities, potentially making them more suitable for integration into hybrid AGI systems <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

### 3. Chemistry-Level Approach: Massively Distributed AI-Optimized Artificial Chemistry Simulation

This approach goes beyond traditional genetic algorithms by simulating artificial organisms and their interactions within a simulated world, including their artificial metabolisms and biochemistry <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. It investigates how complex self-organizing dynamics, akin to those in biological chemistry, can give rise to emergent intelligence <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

The idea, inspired by work in algorithmic chemistry, involves allowing "list codelets" (small programs) to act on and produce other programs in complex chains of reactions, mimicking chemical processes <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This could potentially find more expressive representations for intelligence than purely genetic evolution, by co-evolving the underlying "chemistry" or developmental machinery with the genes <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

Challenges and considerations include:
*   **Compute Intensity:** Simulating full-scale, realistic chemistry or even highly abstracted algorithmic chemistry can demand immense compute resources, potentially exceeding even brain simulations <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Massive Parallelism:** Analogous to brain simulations, chemical processes are inherently parallel, requiring computing infrastructures beyond current Von Neumann architectures <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   **AI-Optimized Evolution:** A key innovation is to introduce an observing [[Artificial General Intelligence AGI challenges and possibilities | AI]] system that uses machine learning and pattern mining to study and direct the evolution of the chemical soup. This AI would identify promising "Vats" of evolving intelligence, kill off less promising ones, and introduce new "codelets" based on successful patterns, thereby accelerating the evolutionary process <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This creates a fascinating hybrid architecture where AGI aids in its own creation <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

## The Call for Diversified Funding and Cultural Shift

Goertzel argues for a significant re-evaluation of [[progress_and_direction_towards_developing_agi | AGI research]] funding. He notes that while global financial systems can absorb trillions for other purposes, there's a reluctance to fund AGI at a level commensurate with its potential impact <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Funding thousands of distinct AGI projects at tens of millions of dollars each would massively accelerate progress <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

> "if you believe there's decent odds that humanity is at the critical point where we're almost there to create super AGI I mean the U.S government could magically synthesize 200 billion dollars to solve world hunger you know 200 billion dollars to to vaccinate the developing World 200 billion dollars for AGI 200 billion dollars for longevity research and the bottom line is this will be absorbed into the vast corrupt chaos the Global Financial system without leading to like mass chaos" <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>

The lack of investment is partly due to the perception that AGI is "20 or 30 years off," discouraging short-term financial returns <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. However, Goertzel suggests that a cultural shift, similar to the rise of open-source software, could drive [[significance_of_interdisciplinary_methods_in_advancing_agi_research | AGI research]] forward <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. If more people recognize the viability of AGI in their lifetimes and that current large tech companies might not deliver true AGI due to its unpredictable nature, a grassroots surge in AGI research for the greater good could emerge <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. The [[the_emergence_of_agi_and_estimated_timelines | emergence of AGI]] would likely lead to a boom in both government funding and public attention, accelerating the exploration of diverse paths <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

[!INFO]+ Key Takeaways:
*   Mainstream deep neural networks, while powerful for [[artificial_general_intelligence_agi_vs_narrow_ai | narrow AI]], are considered insufficient for true AGI due to their reliance on "shallow patterns" and limited generalization capabilities.
*   Alternative approaches include:
    *   **Cognitive Level:** Hybrid neuro-symbolic systems, like [[opencog_and_its_approach_to_agi | OpenCog]], that combine logical reasoning with learning over a distributed knowledge graph.
    *   **Brain Level:** Large-scale simulations of biologically realistic neuron dynamics, which require breakthroughs in hardware and measurement.
    *   **Chemistry Level:** Massively parallel artificial chemistry simulations that leverage AI observers to guide the evolution of meta-programs towards intelligence.
*   Significant increases in funding and a cultural shift towards collaborative, diverse research are essential for accelerating [[progress_and_direction_towards_developing_agi | progress towards AGI]].