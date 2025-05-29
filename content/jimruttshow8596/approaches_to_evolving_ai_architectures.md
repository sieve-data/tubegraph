---
title: Approaches to evolving AI architectures
videoId: Z5dompWURVo
---

From: [[jimruttshow8596]] <br/> 

The field of artificial intelligence (AI) is experiencing rapid evolution, with significant discussions revolving around the most effective architectural approaches for achieving [[Possibilities for achieving humanlevel AGI | Artificial General Intelligence (AGI)]] <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. While Large Language Models (LLMs) have demonstrated impressive capabilities, there's a consensus among some experts, like Ben Goertzel, that current LLMs in their narrow form are unlikely to lead to full human-level AGI <a class="yt-timestamp" data-t="04:49:53">[04:49:53]</a>. This has led to exploring various architectural and training innovations beyond the current LLM paradigm.

## Limitations of Current LLMs

Current LLMs, primarily based on Transformer networks, are trained to predict the next token in a sequence <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. While useful for many functions and capable of passing the Turing test in some contexts <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>, they exhibit several key limitations that suggest they won't achieve AGI:

*   **Hallucination Problem**
    LLMs are prone to "hallucinating" or making up facts, especially for obscure queries <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>. While technical solutions like probing the network for activation patterns might mitigate this for applications <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>, it doesn't indicate a human-like "reality discrimination function" or reflective self-understanding <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. Repeated queries with paraphrased inputs can sometimes reduce hallucinations by identifying lower-entropy (more consistent) correct answers versus higher-entropy (more varied) incorrect ones <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Banality and Lack of Original Creativity**
    The natural output of LLMs tends towards banality, as they essentially average known utterances <a class="yt-timestamp" data-t="34:14:00">[34:14:00]</a>. While clever prompting can push them beyond their typical output <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>, they generally cannot achieve the level of "great creative human" output systematically <a class="yt-timestamp" data-t="34:39:00">[34:39:00]</a>. This impacts artistic creativity, preventing the invention of new musical styles or truly original compositions <a class="yt-timestamp" data-t="30:17:00">[30:17:00]</a>.
*   **Inability for Complex Multi-Step Reasoning**
    LLMs struggle with complex, multi-step reasoning required for tasks like writing original science papers or conducting frontier science <a class="yt-timestamp" data-t="30:04:00">[30:04:00]</a>. While they can "turn the crank" on advanced math given an initial idea, they cannot originate novel concepts or discern the "aesthetics" of a mathematical direction that leads to interesting theorems versus dead ends <a class="yt-timestamp" data-t="38:48:00">[38:48:00]</a>.
*   **Fundamentally Derivative and Imitative**
    At their core, LLMs recognize surface-level patterns in data, creating a vast, indexed library of these patterns <a class="yt-timestamp" data-t="32:33:00">[32:33:35]</a>. They do not appear to learn abstractions in the way humans do, which is crucial for systems smarter than people or for optimizing arbitrary computable reward functions <a class="yt-timestamp" data-t="32:47:00">[32:47:00]</a>.

## Proposed Architectural Evolutions

Recognizing the limitations, various approaches are being explored to build more robust and generally intelligent AI systems. These approaches often fall into hybrid models or fundamental changes in neural network design and training.

### Hybrid Systems

Many believe that AGI will emerge from hybrid systems, where LLMs play a role but are not necessarily the central hub:

*   **LLMs as Components (OpenAI's approach)**
    OpenAI is seen as pursuing an AGI architecture that integrates several LLMs with other non-LLM systems like DALL-E or Wolfram Alpha, where LLMs serve as the "integration hub" <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Non-LLM Hub with LLM Support (OpenCog Hyperon's approach)**
    In contrast, the [[OpenCog and its approach to AI | OpenCog Hyperon]] approach uses a different core—a weighted labeled metagraph—as the central hub, with LLMs acting as peripheral components that feed into and interact with it <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   **LLMs Plus External Tools**
    Many current applications combine LLMs with external tools like vector semantic databases or agent software to overcome their limitations <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. This involves application logic "sky hooking" by sending prompts, getting responses, and creating additional prompts based on the LLM's output <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

### Core Neural Network Enhancements

[[The limitations of current AI architectures | Current AI architectures]] are being re-evaluated to address their inherent weaknesses:

*   **Increased Recurrence in Neural Networks**
    One promising direction is to introduce more recurrence into Transformer networks, similar to, but more sophisticated than, older LSTM models <a class="yt-timestamp" data-t="46:49:00">[46:49:00]</a>. Recurrence is considered a natural way to achieve interesting abstractions in neural networks <a class="yt-timestamp" data-t="47:08:00">[47:08:00]</a>.
*   **Alternative Training Methods**
    Backpropagation, while effective, might be limiting for highly recurrent or complex networks.
    *   **Predictive Coding-Based Training:** Alex Tsia's work from RIT explores predictive coding as an alternative to backpropagation <a class="yt-timestamp" data-t="47:36:00">[47:36:00]</a>. This method is localized and conceptually better suited for richly recurrent networks <a class="yt-timestamp" data-t="52:10:00">[52:10:00]</a>.
    *   **Evolutionary Algorithms:** [[Development and evolution of programming languages for AI | Evolutionary learning]], particularly floating-point evolutionary algorithms, is seen as an under-explored method for training complex neural networks, especially those with radical recurrence <a class="yt-timestamp" data-t="48:55:00">[48:55:00]</a>. The increasing affordability of computation makes this more feasible <a class="yt-timestamp" data-t="51:06:00">[51:06:00]</a>.
    *   **Minimum Description Length Learning:** Yoshua Bengio's group is researching neural networks that explicitly learn abstractions by pursuing minimum description length learning, coupling them with Transformers <a class="yt-timestamp" data-t="49:36:00">[49:36:00]</a>.

### Integrated Architectures (e.g., Google/DeepMind's Potential)

Google and DeepMind are well-positioned to pursue sophisticated integrated architectures due to their existing assets:

*   **Gemini-type Architecture:** This could combine systems like AlphaZero (for planning and strategic thinking), a neural knowledge graph (like in Differential Neural Computing or DNC), and a Transformer with increased recurrence <a class="yt-timestamp" data-t="48:17:00">[48:17:00]</a>. This approach leverages multiple strengths to address AGI <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>.

## [[OpenCog and its approach to AI | OpenCog Hyperon]]: A Different Paradigm

Ben Goertzel's [[OpenCog and its approach to AI | OpenCog Hyperon]] project represents an alternative approach to AGI, focusing on a self-modifying, self-rewriting system:

*   **Weighted Labeled Metagraph:** The core component of Hyperon is a weighted labeled metagraph. This graph allows links to span multiple nodes (hypergraph) and for links to point to other links or subgraphs (metagraph). Each link can be typed, and its type can also be represented as a sub-metagraph <a class="yt-timestamp" data-t="54:38:00">[54:38:00]</a>.
*   **Knowledge Representation:** This metagraph is designed to represent various kinds of knowledge: a priori, declarative, procedural, attentional, and sensory <a class="yt-timestamp" data-t="55:02:00">[55:02:00]</a>.
*   **Meta-programming and Self-Reflection:** Cognitive operations like reinforcement learning, procedural learning, logical reasoning, and sensory pattern recognition are represented as "meta-programs" within this hypergraph <a class="yt-timestamp" data-t="55:23:00">[55:23:00]</a>. These meta-programs act on, transform, and rewrite chunks of the very metagraph they exist within <a class="yt-timestamp" data-t="55:46:00">[55:46:00]</a>. This inherent self-reflection—recognizing patterns in its own mind and processes—is a key distinction from LLMs <a class="yt-timestamp" data-t="56:51:00">[56:51:00]</a>.
*   **Integration with Other Paradigms:** While LLMs can exist on the periphery, the [[OpenCog and its approach to AI | OpenCog]] framework naturally supports historical AI paradigms like logical inference and evolutionary programming, as well as novel self-organizing rewrite rule sets <a class="yt-timestamp" data-t="57:55:00">[57:55:00]</a>.
*   **Path to Superhuman AGI:** This architecture is considered less human-like but offers a very short path to superhuman AGI once human-level is achieved, as the system is fundamentally based on rewriting its own code <a class="yt-timestamp" data-t="59:13:00">[59:13:00]</a>. It is also inherently well-suited for scientific discovery due to its capacity for logical reasoning and precise procedural description <a class="yt-timestamp" data-t="59:48:00">[59:48:00]</a>.
*   **Scalability Challenges:** The primary challenge for [[OpenCog and its approach to AI | OpenCog Hyperon]] is scalability of its infrastructure, requiring efficient use of multiple CPU cores and hyperthreads, potentially through specialized hardware like APUs <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>. The project is focused on building this scalable infrastructure, which includes distributed atom space backing onto MongoDB and Redis, and integrating with blockchain-based infrastructure for decentralization <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>.

These varied approaches highlight the ongoing [[Innovative approaches in AI research | innovative approaches in AI research]] and the diverse perspectives on [[Potential trajectories of AI advancements | future directions and challenges for AI and AGI]], moving beyond the limitations of current LLM-centric systems.