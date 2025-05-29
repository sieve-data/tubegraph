---
title: Efforts in creating a scalable infrastructure for AGI
videoId: Z5dompWURVo
---

From: [[jimruttshow8596]] <br/> 

The field of [[progress_and_direction_towards_developing_agi | AI development]] is experiencing rapid change, with new developments emerging at an accelerated pace, often compared to the personal computer revolution of the late 1970s and early 1980s, but "10 times faster" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This acceleration is particularly evident in the [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI space]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The ongoing upheavals are expected to continue with larger magnitude and even greater speed, leading towards a potential singularity, as projected by Ray Kurzweil <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Current State of Large Language Models (LLMs) and AGI

Ben Goertzel, a leading authority on [[artificial_general_intelligence_agi_challenges_and_possibilities | Artificial General Intelligence (AGI)]] and credited with coining the term <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, believes that current forms of Large Language Models (LLMs), primarily Transformer networks trained to predict the next token, will not lead to a "full-on human level AGI" <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. However, he asserts that LLMs can perform "many amazing useful functions" <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> and serve as "valuable components of systems that can achieve AGI" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### LLM Limitations Driving AGI Infrastructure Research

LLMs exhibit several limitations that highlight the need for new architectural approaches to achieve [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]]. These include:

*   **Hallucination Problem**: LLMs tend to "make up" information when asked relatively obscure questions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. While techniques like probing internal network states might filter these out for practical applications <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, this doesn't address the underlying issue of lacking a human-like "reality discrimination function" <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Banality and Derivative Output**: The natural state of LLM output is often described as "banality," an average of every utterance <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>. While clever prompting can move them beyond their "centers," they still struggle to match the "great creative human" <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.
*   **Complex Multi-step Reasoning**: LLMs lack the ability to perform complex, multi-step reasoning required for original scientific papers or advanced mathematical derivations <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.
*   **Original Artistic Creativity**: They struggle with fundamental aesthetic creativity needed for new musical styles or truly original songs <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. LLMs recognize "surface level patterns" in data but don't show strong evidence of learning human-like abstractions <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>.

These limitations underscore that current LLMs are fundamentally "derivative and imitative" <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>, needing human guidance for original seeding and curation <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>.

## Different Approaches to AGI Infrastructure Development

The push towards [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] involves various architectural strategies:

### OpenAI's Hybrid Approach
OpenAI is pursuing an [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI architecture]] where a "number different LLMs" act as a "mixture of experts" and serve as the "integration hub" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This hub then calls upon other specialized systems like DALL-E or Wolfram Alpha <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Google/DeepMind's Neural Net Universe
Google and DeepMind are well-suited to explore a "Gemini type architecture" <a class="yt-timestamp" data-t="00:48:14">[00:48:14]</a>. This approach could involve combining:
*   **AlphaZero**: For planning and strategic thinking <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>.
*   **Neural Knowledge Graphs**: Such as those found in Differential Neural Computing (DNC) <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
*   **Transformers with Recurrence**: Reintroducing more recurrence into the network architecture, replacing attention heads with more sophisticated elements, as it's an "obvious way to get interesting abstractions" <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>.
*   **Alternative Training Methods**: Exploring methods like predictive coding-based training instead of backpropagation <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>, or leveraging evolutionary learning algorithms <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a> for more complex architectures.

### [[OpenCog and its approach to AGI | OpenCog Hyperon's]] Metagraph-Centric Design

Goertzel's own project, [[OpenCog and its approach to AGI | OpenCog Hyperon]], offers a contrasting approach, where a "weighted labeled metagraph" serves as the central "hub for everything" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. LLMs, DALL-E, and other neural networks act as peripheral components, feeding into and interacting with this core <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

#### Key Features of the Hyperon Architecture:

*   **Self-Modifying Metagraph**: The core is a "big potentially distributed self-modifying self-rewriting metagraph" <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   **Knowledge Representation**: It aims to represent various types of knowledge—apostolic, declarative, procedural, attentional, and sensory—within this hypergraph and linked representations <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>.
*   **Cognitive Operations**: Different [[cognitive_synergy_in_agi_systems | cognitive operations]], such as reinforcement learning, procedural learning, logical reasoning, and sensory pattern recognition, are represented as "Little Learning programs" within the metagraph itself <a class="yt-timestamp" data-t="00:55:15">[00:55:15]</a>.
*   **Meta Language**: A new programming language, "Meta," allows programs to be represented as "Sub metagraphs" that act on, transform, and rewrite chunks of the same metagraph in which they exist <a class="yt-timestamp" data-t="00:55:33">[00:55:33]</a>.
*   **Reflection-Oriented**: Unlike LLMs that predict tokens, [[OpenCog and its approach to AGI | OpenCog]] is designed for "recognizing patterns in its own mind, in its own process and its own execution traces" and representing those patterns internally <a class="yt-timestamp" data-t="00:56:54">[00:56:54]</a>.
*   **Compatibility with AI Paradigms**: It integrates various historical AI paradigms like logical inference and evolutionary programming, as well as new ideas such as "self-organizing mutually rewriting sets of rewrite rules" <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>.
*   **Path to Superhuman AGI**: This architecture is considered less human-like initially but offers a "really short" path from human-level [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI]] to superhuman AGI, as the system is based on "rewriting its own code" <a class="yt-timestamp" data-t="00:59:35">[00:59:35]</a>.
*   **Science and Creativity**: It is well-suited for science due to its focus on logical reasoning and precise procedures <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>, and for creativity through evolutionary programming <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.

#### Scaling [[OpenCog and its approach to AGI | OpenCog Hyperon]]:
The main challenge for [[OpenCog and its approach to AGI | OpenCog Hyperon]] is the "scalability of infrastructure" <a class="yt-timestamp" data-t="01:00:43">[01:00:43]</a>. The project decided to rewrite the old OpenCog version from the ground up to address both usability and scalability issues <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>.

Key components of the scalability pipeline include:
*   **Compiler Pipeline**: A compiler from Meta (Hyperon's native language) to "Rang," a language developed by Greg Meredith for "extremely efficient use of multiple CPU cores and hyper-threads" <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a>.
*   **HyperVector Math**: Translating Rang into "HyperVector math," which deals with "very high dimensional sparse bit vectors" <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.
*   **Specialized Hardware**: Placing HyperVector math on "APU associative processing units" (e.g., from GSI) <a class="yt-timestamp" data-t="01:02:31">[01:02:31]</a>, rather than just GPUs.
*   **Distributed Atom Space**: The distributed atom space backend uses MongoDB to store atoms and Redis to store indexes, designed to scale as well as these databases <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>.
*   **Blockchain Integration**: Integration with a secure, blockchain-based atom space module called RChain DB and the SingularityNET HyperCycle infrastructure allows for decentralized as well as distributed operations, without significant slowdown <a class="yt-timestamp" data-t="01:06:53">[01:06:53]</a>.

Goertzel likens this to the breakthrough of deep neural networks, which only realized their potential when "long existing algorithms hit hard infrastructure that would let them finally do their thing" <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. The hope is that this scalable processing infrastructure for [[OpenCog and its approach to AGI | Hyperon]] will enable "ancient historical AI paradigms" like logical reasoning and evolutionary programming to operate at great scale <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.

> "If my cognitive theory is right... this metagraph system representing different kinds of memory and learning and reasoning in this self-modifying metagraph... is conceptually a great route to AGI, then basically our obstacle to validating or refuting my hypothesis here is having a scalable enough system" <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.

### Other Notable Players

*   **Anthropic (Claude)**: Founded by ex-OpenAI/Google Brain individuals <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, Claude is noted for being "much better than GPT-4 in many things" <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>, particularly in science, mathematics, and medicine domains, and at writing dialogue <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>.
*   **Character.ai**: Described as number two in revenue after ChatGPT <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>, it was founded by two Google Brain researchers <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

The **AGI race** is "now genuinely" underway, with major companies investing significant resources <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. This includes dedicated AGI teams within larger organizations, even if they are often piggybacking on teams doing more immediate, applied work <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. The overall [[progress_and_direction_towards_developing_agi | acceleration in AI]] also positively impacts non-LLM [[artificial_general_intelligence_agi_challenges_and_possibilities | AGI projects]], even if less transparently <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>.