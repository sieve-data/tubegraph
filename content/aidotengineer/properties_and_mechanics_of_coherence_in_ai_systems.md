---
title: Properties and Mechanics of Coherence in AI Systems
videoId: u825uxb7LnA
---

From: [[aidotengineer]] <br/> 

Travis Fry Singinger, Technical Director of AI ETHLite, discusses the concept of coherence in Large Language Models (LLMs), explaining why prompting can feel like magic but isn't a sign of intelligence [00:00:06]. His work aims to explain why LLMs perform so well despite lacking intent or desire [00:00:20].

## The Shift to Coherence
Initially, the release of GPT-3.5 in November 2022 was met with disappointment due to its brittleness, prompt sensitivity, and context limits [00:01:02]. However, the subsequent release of GPT-4 around January 2023 marked a significant shift, with outputs feeling like understanding [00:01:22]. This prompted research from entities like Microsoft, who published "Sparks of Artificial General Intelligence: Early experiments with GPT-4" [00:01:37]. Fry Singinger, however, felt there was a space between "very dumb chatbots" and AGI, which he sought to explore through experiments [00:02:35].

His personal experiments included:
*   **Chat-assisted programming (Vibe Coding)**: Building usable code with ChatGPT in a live scenario, though it required significant effort [00:03:21]. This led to the development of Webcat, a Python Azure function for web scraping, which was useful before ChatGPT-4 had internet access [00:04:02].
*   **Collaborative blog building**: Creating AIBuddy.software by working with AI to pick the platform, build templates, and generate content, leveraging WebCAT for article snippets [00:04:37].
*   **Concept album production**: Producing a "feline metal" concept album, "Mr. Fluff's Reign of Tiny Terror," using ChatGPT for lyrics and music composition, and its image generation for consistent visuals [00:06:00]. This project demonstrated the AI's ability to create a single, coherent concept across multiple outputs [00:07:37].

These experiences led him to analyze chat histories for patterns related to decision intelligence and pairing behaviors [00:08:14]. This analysis resulted in a 21-page research paper outlining the technique and prompts, available on the AIBuddy site [00:08:53].

## The AI Decision Loop: Nudge and Iterate Framework
The analysis identified a core interaction pattern, initially termed the AI Decision Loop [00:09:20], which Fry Singinger now simplifies to a four-step "nudge and iterate" framework [00:10:40]:
1.  **Frame**: Define the problem and context (akin to prompt engineering) [00:09:35].
2.  **Generate**: Produce outputs based on the prompt [00:09:45].
3.  **Judge**: Evaluate the quality and fit of the output [00:09:57]. This includes validating against external requirements [00:10:04].
4.  **Iterate**: Refine the prompt to improve the outcome [00:10:16]. This cycle is repeated to achieve more reliable outputs [00:10:31].

This iterative process, even though not every interaction follows it, consistently leads to better outcomes when applied [00:11:00].

## Defining Coherence
Fry Singinger proposes that the perceived intelligence of LLMs is actually a "coherence theory" [00:11:47]. Coherence is a system property, not a cognitive one [00:12:01]. It acts as the "infrastructure that thought navigates" [00:12:06].

Coherence in LLMs has four key properties:
*   **Relevant**: The model's output feels topical, connected, and purposeful to the conversation [00:12:24].
*   **Consistent**: The model maintains a singular tone, terminology, and structure across multiple turns [00:12:31]. For example, consistently knowing "MCP" stands for "model context protocol" [00:12:44].
*   **Stability**: The model can withstand pressure or interrogation, such as questioning its outcome or presenting a competing theory, without collapsing [00:12:51]. Instead, it may firm up or course-correct [00:13:10]. This was a key missing element in earlier models like GPT-3.5 [00:13:15].
*   **Emergent Property**: Coherence arises unexpectedly [00:13:21]. For instance, GPT-4o was not trained to detect swine disease but can diagnose it through "coherent pattern alignment" [00:13:26]. Similarly, it can pick up patterns for certain cancer diagnoses before humans can see them [00:13:37].

## Mechanics of Coherence in the Machine
Traditional neural networks are often thought to store a concept in a single neuron [00:13:56]. However, Anthropic's research suggests that in LLMs, "superposition" allows the network to represent complex ideas with fewer parameters, packing more nuance into the same space [00:14:13]. As context accumulates, the network "teases apart the relevant meaning and collapses that ambiguity into a coherent output" [00:14:23]. This means that meaning is not simply retrieved but "constructed on demand from distributed sparks of possibility" [00:14:52].

Prompts act as "force vectors" [00:14:59] in the high-dimensional latent space of an AI model [00:15:04]. Each prompt sets a specific direction, which the AI then aligns patterns to [00:15:10]. Concepts, like "cat" or "dog," "wear grooves" in this latent space, guiding the model's responses [00:15:15].

When a model is prompted with external context, "conceptual clouds" or sub-networks in the latent space activate around the given ideas (e.g., "storytelling" and "freedom") [00:15:51]. These specialized patterns emerge during training and activate only when the context calls for them [00:16:21]. When two concepts, like "storytelling" and "pets," are merged by a prompt, the force vector causes "something new to emerge based on the sub-networks that light up" [00:16:47]. This process is about "essence reconstruction," creating compelling patterns rather than fact-checking or intelligence [00:17:29].

## Engineering for Coherence, Not Intelligence
This understanding shifts the engineering perspective:
*   [[The Coherence Trap in Large Language Models | Hallucinations]] are seen as an indicator of coherence, not a bug [00:17:45]. They are a "system feature" [00:18:00] where the model attempts to complete a pattern if not given enough information [00:17:47].
*   Retrieval Augmented Generation (RAG) is crucial. RAG fragments serve as "factual anchors" [00:18:16] that create "contextual gravity" [00:18:20], pulling the concept in the desired direction [00:18:22]. RAG provides the "structural scaffolding that shapes how coherency unfolds" [00:18:27].

### Three-Layer Model
To build for coherence, a three-layer model is proposed, relating to the [[Components of AI agents | components of AI agents]]:
*   **Layer 1: Latent Space** <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a> – The internal model structure, including concepts, weights, and activations.
*   **Layer 2: Execution Layer** <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a> – Tools, APIs, and retrieval mechanisms, which bring external context for Layer 1. This includes aspects of [[Memory Management in AI]].
*   **Layer 3: Conversational Interface** <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a> – Where human intent and thought are passed to the machine, providing grounding for layers 1 and 2 to be actionable.

### Building Principles
When building for coherence, key principles include:
*   **Prompting as Interfaces**: Prompts should not be considered "once off" but as a component in a system [00:19:19].
*   **RAG for Grounding**: Use RAG as "coherency anchors" to steer generation [00:19:26], as dense, relevant context acts like gravity [00:19:30].
*   **Design for Emergence**: Recognize that the system is not deterministic [00:19:37] and build around the "frame, generate, judge, iterate" loop [00:19:39].
*   **Avoid Fragile Chains**: Long [[Chain of Thought reasoning in AI | reasoning chains]] can break coherence [00:19:44]. Instead, keep chains modular and reinforce context at each point [00:19:47].
*   **Monitor for Breakdowns**: Watch for changes in tone, structure, or flow as early signs of context loss [00:19:53]. These breakdowns indicate where to debug the system, potentially by adjusting chunk size in a vector database or integrating other tools [00:20:01].

Ultimately, LLMs are described as a "high-dimensional mirror" [00:20:17]. They do not understand or think but resonate through structure [00:20:26]. Their superpower is coherence, not intelligence, and the "magic happens in the collaborative dance" between human intent and the model's pattern alignment [00:20:34]. The goal for developers should be to design for "structured resonance" [00:20:42].