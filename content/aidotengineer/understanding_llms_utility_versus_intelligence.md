---
title: Understanding LLMs Utility versus Intelligence
videoId: u825uxb7LnA
---

From: [[aidotengineer]] <br/> 

Travis Fry Singinger, Technical Director of AI ETHLite, presents a top-down understanding of Large Language Models (LLMs), specifically addressing "the coherency trap" – why prompting feels like magic but isn't intelligence <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This perspective aims to explain why LLMs perform so effectively, even though they lack intent, desire, or true intelligence <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Initial Impressions and the GPT-4 Shift

In November 2022, the release of GPT-3.5 generated considerable hype, but Fry Singinger's initial experience was disappointing <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. While it showed advancements in tasks like improving emails, it was "very brittle in its understanding," with surface-level fluency often collapsing at edge cases due to prompt sensitivity and context limits <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

However, the release of GPT-4 in January 2023 marked an "uncanny moment" where words aligned effortlessly, creating a profound sense of understanding <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This shift was widely noticed; Microsoft Research published "Sparks of Artificial General Intelligence: Early Experiments with GPT-4," and academics like Ethan Mollick began research into this new phenomenon <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This experience of perceived utility surpassed previous AI encounters, feeling as though the output genuinely understood the input <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Fry Singinger felt there was a significant space between "very dumb chatbots" and [[general_versus_domain_specific_language_models | AGI]], which he sought to explore <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Experimental Exploration of LLM Capabilities

To understand this new behavior, Fry Singinger, an engineer and scientist, began conducting experiments <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Paired Programming with LLMs (Vibe Coding)

He started by live-streaming his work with ChatGPT, engaging in what he termed "chat assisted programming" (also known as "chat oriented programming" or "vibe coding") <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. While initially challenging to produce usable code, these sessions evolved into prototypes for what [[benchmarking_llms_for_software_development | AI pair programming]] would become <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

A key utility developed during this phase was Webcat, a Python Azure function designed to scrape web pages for content <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This tool was crucial because early ChatGPT-4 models lacked internet access, making it difficult to chat about or explore ideas from current web content <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This demonstrated the [[use_of_llms_with_browser_navigation_and_other_services | utility of LLMs]] when augmented with external services.

### Collaborative Content Creation

Further experiments involved building his blog, AIBuddy.software, with AI assistance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The goal was to lean into the collaborative essence of AI <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The AI even helped select the platform (Ghost) and, using Webcat, pulled in article snippets to aid in content generation <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. The success of this thought leadership blog demonstrated the AI's capability in content creation <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### AI-Assisted Creative Production

Fry Singinger then ventured into music production, aiming to create a concept album titled "Mr. Fluff's Reign of Tiny Terror," a feline metal album <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. He used ChatGPT for lyrics and music composition, alongside image editing to maintain consistency across interactions <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This project highlighted new prospects for [[integration_of_llm_with_creative_tools | creative partnering with LLMs]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Despite the humorous and "handicapped" nature of the project (AI-generated cat metal), the YouTube videos garnered over 3,000 views and positive comments within a month, demonstrating the AI's ability to help create valuable content beyond individual capabilities <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This indicated that LLMs could create a single, coherent concept across various modalities <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## The AI Decision Loop: Nudge and Iterate Framework

To further understand reliable interactions, Fry Singinger explored elements of decision intelligence and pairing behavior, analyzing his ChatGPT history <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. He built an analysis tool to extract qualitative and quantitative metrics around these behaviors <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This led to a 21-page research paper outlining the technique and prompts <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

The outcome was the "AI Decision Loop," later simplified into the "Nudge and Iterate" framework:
*   **Frame**: Define the problem and context (prompt engineering) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Generate**: Produce outputs, whether single or multiple <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Judge**: Evaluate the quality and fit of the output <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. (Optionally: Validate against external requirements) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Iterate**: Refine the prompt to improve the experience based on what was right or wrong <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

This cycle, "Frame, Generate, Judge, Iterate," proved crucial for achieving reliable outputs, nudging the model towards desired results <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

## Coherency Theory: The LLM Superpower

Despite understanding the mechanics, the question of *why* LLMs work so well without being intelligent remained <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Fry Singinger proposed "coherency theory," inspired by natural language processing and research from Anthropic on feature superposition and concept circuits <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

Coherence is defined as a *system property*, not a cognitive one <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. It's the underlying infrastructure through which thought navigates <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
Its four key properties are:
1.  **Relevant**: Output feels topical, connected, and purposeful <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
2.  **Consistent**: Maintains a singular tone, terminology, and structure across multiple interactions <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
3.  **Stable**: Can withstand pressure, questioning, or competing theories without collapsing; it may firm up or course-correct <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This stability was notably absent in earlier models like GPT-3.5 <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
4.  **Emergent**: A property that appears without explicit training. For example, GPT-4o was not trained to detect swine disease but can diagnose it through "coherent pattern alignment," similar to certain cancer diagnoses <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### The Mechanics of Coherence

Traditionally, neural networks were thought to store concepts in single neurons <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. However, research suggests that LLMs use *superposition*, representing complex ideas with fewer parameters by packing more nuance into the same space <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. As context accumulates, the network teases apart relevant meanings and collapses ambiguity into coherent output <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. For instance, neurons might store elements of "feline," "pet," and "animal," which can also overlap with "canine," "pet," and "animal" <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This means meaning is *constructed on demand* from distributed "sparks of possibility," rather than being simply retrieved <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

Prompts act as "force vectors" within the high-dimensional latent space of the AI model <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Each prompt sets a specific direction, causing the AI to align patterns <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. When external context is provided, conceptual "clouds" (subnetworks) in the latent space activate. For example, "storytelling" and "pets" concepts light up and merge to create a new, coherent idea based on the specific interaction <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. This demonstrates that LLMs recreate the essence of an idea and combine multiple essences to create something new, rather than just retaining compressed information <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. This is why even hallucinations can feel correct; they are compelling pattern constructions, not fact-checking <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

## Engineering for Coherence, Not Intelligence

Framing systems as coherent rather than intelligent changes how we approach LLM engineering <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>:

*   **Hallucinations as Coherence Indicators**: Hallucinations are a system feature, not a bug <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. They indicate the model's attempt to complete a pattern following its internal logic, especially when insufficient information is provided <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **RAG as Factual Anchors**: Retrieval Augmented Generation (RAG) fragments act as "factual anchors," providing contextual gravity that pulls the concept in the right direction <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. They serve as structural scaffolding for coherence <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

Fry Singinger proposes a three-layer model for LLM operation <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>:
*   **Layer 1: Latent Space**: The internal model structure (concepts, weights, activations) <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Layer 2: Execution Layer**: Tools, APIs, and retrieval mechanisms that bring extra context for Layer 1 <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Layer 3: Conversational Interface**: Where human intent and thought are passed to the machine, grounding Layer 1 and 2 to make them actionable <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

To build for coherence:
*   **Prompting as Interfaces**: Prompts are components in a system, not one-off interactions <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
*   **RAG for Grounding**: Use dense, relevant context to steer generation, acting like gravity pulling output towards reality <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Design for Emergence**: Accept that LLMs are not deterministic; build around the "Frame, Generate, Judge, Iterate" loop <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Avoid Fragile Chains**: Long reasoning chains can break coherency. Keep chains modular and reinforce context at each point <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Monitor Breakdowns**: Watch for shifts in tone, structure, or flow. These are early signs of context loss, indicating a need for intervention or debugging, such as adjusting chunk sizes in a vector database or integrating other tools <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

In conclusion, LLMs are not intelligent thinkers but "high-dimensional mirrors" that resonate through structure, not thought <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Their superpower is coherence, and the "magic" lies in the collaborative dance between human intent and the model's structured resonance <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. The focus should shift from chasing intelligence to designing for structured resonance <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.