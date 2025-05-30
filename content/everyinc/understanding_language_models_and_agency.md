---
title: Understanding language models and agency
videoId: OeKEXnNP2yA
---

From: [[everyinc]] <br/> 

Understanding the [[nature_of_language_models_and_language | nature of language models]] (LMs) and the concept of [[managing_agency_in_the_age_of_ai | agency]] within their development and use is crucial for navigating the evolving landscape of artificial intelligence <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Rather than viewing LMs as independent agents, they can be understood as sophisticated calculators that provide better suggestions with more context about user goals <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Agency in AI Development and Use

A core philosophy in AI development is to create tools that augment human capabilities and lead to a more human future, rather than replacing human roles or infringing on human agency <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Language Models: Statistical Models, Not Agents
While LMs, especially those based on language, often feel human-like <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> and can be wrapped in "anthropomorphic packaging" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>, they are fundamentally statistical models that predict probability distributions <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This perspective views them more as "thought calculators" than entities with their own will or intent <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

### How Tools Constrain Agency
The design of AI tools can inadvertently limit user agency <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **DALL-E Example**: It is difficult to generate an "ugly image" with DALL-E, as the tool's design constrains the output search space towards what is typically considered aesthetic <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a> <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This contrasts with tools like Photoshop, which allow direct pixel manipulation without limiting creative agency <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Stylistic Bias**: Even seemingly simple tools like Instagram filters or Keynote's background masking can subtly shape the output style, demonstrating how features make certain results easier to achieve, thus guiding the user's creative choices <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## [[mechanistic_interpretability_of_language_models | Mechanistic Interpretability of Language Models]] through Embeddings

Viewing the output space of LMs spatially, through the lens of [[mechanistic_interpretability_of_language_models | embeddings]], offers a concrete way to understand their capabilities and gain more control <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### What are Embeddings?
An embedding is a quantitative summary of text or image content, represented as a list of numbers <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. These numbers act as coordinates in a high-dimensional space where semantic similarity is reflected by proximity <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. For example, sentences with similar meanings will have their embeddings located closer together in this space <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Manipulating Concepts with Embeddings
Embeddings allow for mathematical manipulation of concepts, similar to how RGB values allow for precise color adjustments <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a> <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This suggests new ways to interact with AI beyond simple chat prompts.

#### Varna: A Spatial Exploration Tool
Varna is an experimental tool that allows users to create images by "adding and subtracting" images and text in an embedding space <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. It leverages models like CLIP to describe both text and image inputs in the same coordinate space <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

*   **Conceptual Blending**: By picking points between two concepts (e.g., a butterfly and a French flag), Varna can generate images that blend these ideas <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **"Sliders" for Concepts**: This allows for "sliding" along conceptual scales, such as gradually transforming a headshot into a vectorized drawing <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a> or manipulating emotions in an image <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   **LM as a Calculator**: This approach emphasizes the LM as a concrete mathematical tool rather than an agent, fostering more user agency and control <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

## AI as a Tool vs. Simulacrum

There's a divergence between developing AI as a functional tool (an "intelligence kind of engine" <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a> or "thought calculator" <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>) and building a "simulacrum of humans" with agency and goals <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>. For practical applications like knowledge work, certain human traits (e.g., daydreaming) may be counterproductive <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### Anthropomorphic Packaging
The way an AI is presented (its "packaging") significantly influences how people perceive and use it <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>. Features like "read" receipts or notifications can make an AI feel more human-like, even if it's just a statistical model <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

### Personal Chatbot Example
A personal chatbot built on a raw base model (like Llama 2) without fine-tuning can provide more "personal" or "vibey" responses because it hasn't been constrained to act as a typical "AI language model" <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. This allows for outputs that feel more like talking to "a rando on the internet" <a class="yt-timestamp" data-t="00:31:03">[00:31:03]</a>.

## Prompting and User Agency

Prompting LMs can be categorized similarly to programming:
*   **Prompt Engineering**: Analogous to robust "software engineering" for products, where prompts are heavily tested and designed to be resilient to diverse inputs for millions of users <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Prompt Scripting**: Analogous to quick "scripting" or "running commands" for personal use, where users iterate and fix mistakes in real-time until they get the desired output <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

In personal use, "banging away" at the tool and iterating is often more effective than trying to craft perfect prompts from the start <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. Users should not be reluctant to ask for re-dos, revisions, or start new chats <a class="yt-timestamp" data-t="00:38:02">[00:38:02]</a>.

### Practical Examples of Prompting
*   **"What's the vibe of this file?"**: A casual prompt for data analysis, demonstrating the LM's ability to understand context without overly precise instructions <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>.
*   **Programming Help**: LMs can provide high-level conceptual guidance and initial implementations for complex problems (e.g., streaming data processing) that standard coding tools like CoPilot cannot <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>.
*   **Trip Planning**: Instead of asking for the "best" places, repeatedly asking for general recommendations and then identifying overlapping suggestions across multiple outputs allows the user to retain more agency in their choice, rather than relying on the AI's filtering <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a> <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>.
    *   **Custom Instructions**: While some users find custom instructions helpful for biasing outputs towards their preferences, others prefer to keep prompts broad to avoid the AI over-steering or connecting irrelevant aspects to the instructions <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>.
*   **Notion AI for [[role_of_language_models_in_knowledge_work | Knowledge Work]]**:
    *   **"Continue writing"**: A simple, "brain dead" prompt that asks the model to simply extend existing text, useful for brainstorming or listing ideas <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
    *   **Collaborative Document Editing**: Notion AI can transform rough notes into well-formatted, presentable documents by turning bullet points into paragraphs or adding headings <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>. This collaborative workflow allows users to edit the AI's output and continue iterating <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>.
    *   **Q&A**: In team contexts, Notion AI's Q&A feature can answer questions by retrieving information from a "forest of knowledge" (e.g., meeting docs, policies), reducing repetitive questions <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

### Advanced Prompting Techniques
*   **Chain of Density**: A technique where the LM is instructed to generate multiple drafts of a summary, iteratively increasing information density without increasing length. This can be generalized to any desired output property like concision or specific formatting <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>.
*   **Chain of Thought**: Similar to Chain of Density, this involves asking the AI to output its thinking steps before the final answer, which generally improves performance and quality <a class="yt-timestamp" data-t="01:08:28">[01:08:28]</a>.
*   **"Putting Words in the AI's Mouth"**: In platforms like OpenAI's Playground, users can insert fake chat history where the AI "agrees" to a request, making it more likely to comply with a subsequent real request <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>. This trick can be used to bypass "guard rails" <a class="yt-timestamp" data-t="01:13:18">[01:13:18]</a>.

### GPT-4 Turbo's "Laziness"
Anecdotal evidence suggests that GPT-4 Turbo tends to be "lazy" <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a> or more "efficient with compute" <a class="yt-timestamp" data-t="01:09:44">[01:09:44]</a>. This means it often produces shorter, more concise outputs and may require more explicit instructions to use tools like DALL-E or generate multiple results <a class="yt-timestamp" data-t="01:09:51">[01:10:14]</a>. Interestingly, it might be more likely to say "no" if asked politely, suggesting that commanding it yields better results <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.