---
title: The Coherence Trap in Large Language Models
videoId: u825uxb7LnA
---

From: [[aidotengineer]] <br/> 

Travis Fry Singer, Technical Director of AI ETHLite, discusses the "coherency trap," explaining why prompting [[current_and_future_trends_in_large_language_models | Large Language Models]] (LLMs) feels like magic but isn't true intelligence <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. His top-down talk aims to explain the perceived effectiveness of LLMs despite their lack of intelligence, intent, or desire <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Initial Encounters with LLMs

In November 2022, upon the release of GPT-3.5, the speaker was initially disappointed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. While it offered some advancements, such as improving emails, its understanding was brittle, its fluency often collapsed at edge cases, and it suffered from prompt sensitivity and context limits <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

However, the release of GPT-4 in January 2023 marked a significant shift <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The output felt like understanding, transcending mere text generation to display something eerily similar to comprehension <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This experience was shared by others, including Microsoft Research, who published "Sparks of Artificial General Intelligence: Early Experiments with GPT-4" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The speaker felt there was an unexplored space between "very dumb chatbots" and AGI <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Experimental Exploration of LLM Capabilities

To understand this shift, the speaker, an engineer and scientist, began conducting [[experiments_with_large_language_models_and_ai_assisted_work | experiments]] <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Vibe Coding and Utility Development
Starting with a live stream, he engaged in "chat assisted programming" (also known as "vibe coding" or "chat oriented programming") with ChatGPT <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This process, though effort-intensive for a few hundred lines of code, served as a prototype for [[large_language_models_in_code_generation | AI pair programming]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

From these sessions, he developed `Webcat`, a Python Azure function that scraped web pages for content <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This was crucial because early ChatGPT-4 lacked internet access, making `Webcat` useful for feeding web content to the model <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Collaborative Projects
Using `Webcat` and working collaboratively with AI, the speaker built his blog, AIBuddy.software <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The AI selected the Ghost platform and provided instructions for setting up the template <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This collaborative approach proved successful for generating content <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Expanding on creative collaboration, he used LLMs to produce a concept album titled "Mr. Fluff's Reign of Tiny Terror," a "feline metal album" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. ChatGPT was used for lyrics and music composition, and its image generation capabilities were employed for consistent visuals <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Despite the humorous concept, the project garnered over 3,000 views and positive feedback on YouTube, demonstrating AI's ability to assist in creating valuable content beyond his individual capabilities <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## The AI Decision Loop

These successful collaborative experiences led the speaker to investigate whether concepts like decision intelligence and pairing behaviors could explain the LLM's perceived utility <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. He built an analysis tool using his "vibe coding" skills to parse his ChatGPT history, looking for qualitative and quantitative metrics related to decision intelligence and pairing <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This analysis culminated in a 21-page research paper available on his AIBuddy site <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

The findings revealed a cyclical process, which he termed the **AI Decision Loop**:

*   **Frame**: Define the problem and provide context (akin to prompt engineering) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Generate**: Produce outputs, potentially multiple options <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Judge**: Evaluate the quality and fit of the output <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Validate**: Optionally, ensure external requirements are met <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Iterate**: Refine the prompt to improve the output based on what was right or wrong <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

A less academic version of this process is the "nudge and iterate" framework: **Frame, Generate, Judge, Iterate** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This iterative prompting and nudging was found to be at the heart of reliable LLM interactions <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## [[properties_and_mechanics_of_coherence_in_ai_systems | Coherence]] Theory

Despite these mechanics, the question remained: why did LLMs work so well if they weren't intelligent? The speaker turned to the concept of [[properties_and_mechanics_of_coherence_in_ai_systems | coherence]] from natural language processing, aligning with research like Anthropic's work on feature superposition and concept circuits <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

### What is [[properties_and_mechanics_of_coherence_in_ai_systems | Coherence]]?
[[properties_and_mechanics_of_coherence_in_ai_systems | Coherence]] is described as a system property, not a cognitive one, serving as the "infrastructure that thought navigates" <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. It has four key properties:

*   **Relevant**: The model's output feels topical, connected, and purposeful <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Consistent**: The model maintains a singular tone, terminology, and structure across multiple turns <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Stable**: The model can withstand pressure and interrogation, not collapsing but firming up or course-correcting <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This stability was a key differentiator from earlier models like GPT-3.5 <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Emergent**: It's an emergent property. For example, GPT-4o, without explicit training, can diagnose swine disease or certain cancers through "coherent pattern alignment" <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### Mechanics of [[properties_and_mechanics_of_coherence_in_ai_systems | Coherence]]
Traditional neural networks typically store concepts in single neurons <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. However, research suggests that in LLMs, **superposition** allows the network to represent complex ideas with fewer parameters, packing more nuance into the same space <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. As context accumulates, the network "teases apart the relevant meaning and collapses that ambiguity into a coherent output" <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. An idea isn't stored in a single neuron or set of neurons; rather, a set of neurons can hold multiple ideas <a class="yt-timestamp" data-t="00:14:43">[01:14:43]</a>.

This implies that meaning isn't retrieved but constructed on demand from "distributed sparks of possibility" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Prompts act as "force vectors" in the high-dimensional latent space of the AI model, setting a specific direction that the AI aligns patterns to <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. When a prompt is given, external context activates conceptual clouds (sub-networks) in the latent space that are relevant to the query <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. These specialized patterns emerge during training and activate when the context calls for them, merging concepts to create new, coherent ideas <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

## Engineering for [[properties_and_mechanics_of_coherence_in_ai_systems | Coherence]], Not Intelligence

This understanding leads to a new kind of utility for LLMs, focusing on their ability to recreate the essence of an idea and combine multiple essences to create something new <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. When LLMs "hallucinate," they are creating a compelling pattern based on essence reconstruction, not fact-checking or intelligence <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

### Hallucinations as Features
From an engineering perspective, hallucinations are seen as an indicator of [[properties_and_mechanics_of_coherence_in_ai_systems | coherence]], as the model fills gaps predictably following an internal logic <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. They are an emergent system feature, not a bug <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

### Retrieval Augmented Generation (RAG)
To mitigate hallucinations, [[building_and_scaling_large_language_models | Retrieval Augmented Generation (RAG)]] is used <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. RAG fragments act as "factual anchors" or "structural scaffolding" <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. Dense, relevant context from RAG creates "contextual gravity" that pulls the concept in the right direction, providing infrastructure for human intent to navigate the latent space <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

### Three-Layer Model for LLM Systems
The speaker proposes a three-layer model for LLM systems:
1.  **Layer One: The Latent Space** <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>: The internal model structure (concepts, weights, activations).
2.  **Layer Two: The Execution Layer** <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>: Tools, APIs, and retrieval mechanisms that bring external context for Layer One.
3.  **Layer Three: The Conversational Interface** <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>: Where human intent (thought) passes to the machine, grounding Layers One and Two in actionable value.

### Design Principles for Coherent Systems
*   **Prompting as Interfaces**: Prompts should be viewed as components in a system, not one-off interactions <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
*   **RAG for Coherency Anchors**: Use RAG to steer generation with dense, relevant context <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Design for Emergence, Not Control**: Embrace the non-deterministic nature of LLMs, building around the Frame, Generate, Judge, Iterate loop <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Avoid Fragile Chains**: Long reasoning chains can break [[properties_and_mechanics_of_coherence_in_ai_systems | coherence]]; keep chains modular and reinforce context at each point <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Watch for Breakdowns**: Monitor changes in tone, structure, or flow as early signs of the model losing context, using them as debugging points <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

In conclusion, LLMs are best understood as "high-dimensional mirrors" <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. They don't understand or think but resonate through structure, reflecting back patterns that can appear sharper than the input <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Their superpower is [[properties_and_mechanics_of_coherence_in_ai_systems | coherence]], not intelligence, and the true "magic" lies in the collaborative dance between human intent and the model's structural resonance <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.