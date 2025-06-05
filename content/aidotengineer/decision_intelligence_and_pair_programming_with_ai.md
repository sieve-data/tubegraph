---
title: Decision Intelligence and Pair Programming with AI
videoId: u825uxb7LnA
---

From: [[aidotengineer]] <br/> 

Travis Fry Singinger, Technical Director of AI ETHLite, has explored the perceived "magic" of large language models (LLMs) and why prompting feels powerful despite LLMs lacking true intelligence or intent <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. His journey, marked by experiments and analysis, led to a theory explaining the effectiveness of LLMs through "coherency" and the development of frameworks for more reliable human-AI collaboration <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Uncanny Shift: GPT-3.5 to GPT-4

Initially, the release of GPT-3.5 in November 2022 brought disappointment due to its brittle understanding, prompt sensitivity, and surface-level fluency that collapsed at edge cases <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. However, the subsequent release of GPT-4 around January 2023 presented an "uncanny moment" where the output felt like understanding, transcending mere text generation <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This shift was widely noticed, with Microsoft Research publishing a paper on "sparks of artificial general intelligence" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Fry Singinger felt there was a space between "very dumb chatbots" and AGI that needed further exploration <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Early Experiments in AI-Assisted Programming

Driven by his background as an engineer and scientist, Fry Singinger began conducting experiments to understand this new phenomenon <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. He started with live stream "chat assisted programming," also known as "chat oriented programming" or "vibe coding" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. While initially requiring significant effort to produce usable code, these sessions evolved into prototypes for [[integration_of_ai_into_development_environments_and_editors | AI pair programming]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

A key utility developed during this phase was Webcat, a Python Azure function that scraped web pages to provide content to ChatGPT-4, which at the time lacked internet access <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This utility was crucial for overcoming the model's limitations and making it useful for real-world problems <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Collaborative Projects and [[design_process_improvements_with_ai | Design Process Improvements with AI]]

The success of Webcat led to deeper collaborative experiments:

*   **AIBuddy.software Blog:** Fry Singinger collaborated with AI to build his blog, AIBuddy.software, demonstrating a "collaborative essence" rather than treating AI as a source of all answers <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The AI assisted with platform selection, instructions, and template building <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Webcat was used to pull in article snippets for discussion and blog generation <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **"Mr. Fluff's Reign of Tiny Terror" Concept Album:** Leveraging his music background, he aimed to produce an AI-assisted feline metal concept album <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This project used ChatGPT for lyrics and music composition, alongside image editing, noting the new ability of ChatGPT's image generation to refine outputs rather than acting like a "slot machine" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The album, uploaded to YouTube without promotion, garnered over 3,000 views and significant positive feedback within a month, demonstrating the ability to create valuable content beyond individual capabilities <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

These projects indicated that LLMs could help create a single, coherent concept across various domains <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Discovering the AI Decision Loop

To understand the underlying behaviors, Fry Singinger hypothesized that traditional [[using_reasoning_models_and_tool_calls_in_ai | decision intelligence]] and pair programming might hold the "secret sauce" <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. He built an analysis tool using his "vibe coding" skills to process his ChatGPT history, looking for qualitative and quantitative metrics related to decision intelligence and pairing behaviors <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

This research culminated in a 21-page [[case_study_of_ai_interview_agent_development | case study of AI interview agent development]] outlining the technique and prompts used, available on his AI Buddy site <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

The study revealed the **AI Decision Loop**, which he condensed into a four-step process, or "nudge and iterate" framework <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>:

1.  **Frame:** Define the problem and context (prompt engineering) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
2.  **Generate:** Produce one or many outputs <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
3.  **Judge:** Evaluate the quality and fit of the output. This includes validating against external requirements and asking further questions <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  **Iterate:** Refine the prompt and nudge the model based on what was right or wrong, continuing the cycle to produce more reliable outputs <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

> "This isn't a once-off prompt and accept type scenario." <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>

Following this loop led to significantly better outcomes in his interactions with AI <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## Coherency: The LLM Superpower

Despite the effective mechanics, the question remained: why do LLMs work so well if they aren't intelligent? Fry Singinger proposes a "coherence theory" based on natural language processing and research into feature superposition and concept circuits <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

**Coherence is a system property, not a cognitive one** <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. It's the infrastructure thought navigates <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. It has four key properties:

*   **Relevant:** Outputs feel topical, connected, and purposeful <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Consistent:** The model maintains a singular tone, terminology, and structure across multiple turns <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Stability:** The model can withstand pressure and interrogation, firming up or course-correcting rather than collapsing <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This was a significant improvement over earlier models <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Emergent Property:** Coherence allows for abilities not explicitly trained, like GPT-4o diagnosing swine disease through "coherent pattern alignment" <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### Mechanics of Coherence: Force Vectors in Latent Space

Instead of concepts being stored in single neurons, LLMs use **superposition**, representing complex ideas with fewer parameters by packing more nuance into the same space <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Meaning is "constructed on demand from distributed sparks of possibility" <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

A prompt acts as a **"force vector"** in the high-dimensional latent space of the AI model <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This vector sets a specific direction, causing the AI to align patterns <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. When a prompt is given, relevant "conceptual clouds" or sub-networks in the latent space activate and merge, causing new ideas to emerge based on the combined context <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

This leads to a new kind of utility: LLMs don't just compress and retrieve knowledge; they recreate the essence of ideas and combine multiple essences to create something new <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This explains why hallucinations can still *feel* correct—they are creating a compelling pattern, not fact-checking <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

## Building for Coherence, Not Intelligence

Understanding LLMs as coherent systems rather than intelligent ones changes the engineering approach:

*   **Hallucinations as Indicators:** Hallucinations are a system feature, an emergent behavior of coherence, indicating where the model fills gaps due to insufficient information <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. They follow internal logic and coherency vectors <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **[[using_reasoning_models_and_tool_calls_in_ai | Retrieval Augmented Generation (RAG)]] as Factual Anchors:** RAG fragments act as "factual anchors" providing "contextual gravity" to steer generation towards reality, forming a "structural scaffolding" for coherence <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Three-Layer Model:**
    1.  **Latent Space:** Internal model structure (concepts, weights, activations) <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
    2.  **Execution Layer:** Tools, APIs, and retrieval mechanisms that bring external context to Layer 1 <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    3.  **Conversational Interface:** Where human intent and thought are passed to the machine, grounding Layers 1 and 2 in human needs <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   **Design Principles for Coherence:**
    *   **Prompts as Interfaces:** Treat prompts not as one-off commands but as components within a larger system <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
    *   **[[using_reasoning_models_and_tool_calls_in_ai | RAG]] for Grounding:** Dense, relevant context acts like gravity, pulling output towards reality <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
    *   **Design for Emergence, Not Control:** LLMs are not deterministic; build around the "Frame, Generate, Judge, Iterate" loop <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
    *   **Avoid Fragile Chains:** Long reasoning chains often break coherency. Keep chains modular and reinforce context at each point <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
    *   **Watch for Breakdowns:** Early signs like breakdowns in tone, structure, or flow indicate the model is losing context. These serve as debugging points to adjust chunk size, vector database, or integrate other tools <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

In conclusion, LLMs are best understood as "high-dimensional mirrors" that resonate with human intent through structure, not thought <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Their superpower is coherence, and the "magic" lies in the collaborative dance between human and machine <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. The focus should shift from chasing intelligence to [[efficiency_and_smart_execution_in_ai_systems | designing for structured resonance]] <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.