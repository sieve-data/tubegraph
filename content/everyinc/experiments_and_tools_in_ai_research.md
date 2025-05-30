---
title: Experiments and tools in AI research
videoId: OeKEXnNP2yA
---

From: [[everyinc]] <br/> 

The development of AI tools, particularly large language models (LLMs), is viewed not as creating autonomous agents, but rather as building advanced calculators or functions that process information based on probability distributions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This perspective highlights the need to design interfaces that augment human capabilities and agency, rather than infringing upon them <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Fundamental Concepts in AI Development

### AI as a Tool or Calculator
Language models, when viewed from a lower level, are essentially functions that predict probability distributions <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. While they can be wrapped in "anthropomorphic packaging" that makes them seem to have their own will or intent, they are fundamentally statistical models <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This perspective encourages thinking of AI as a "thought calculator," providing dials and controls for manipulation rather than an entity for requests <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a> <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

### Understanding Embeddings
A core concept in AI research is embeddings, which are numerical representations (lists of numbers) that summarize the semantic content of text or images <a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a> <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>. These numbers act as coordinates in a high-dimensional space, where semantically similar items are closer together <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a> <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>. This allows for mathematical manipulation of concepts, similar to how RGB values of colors can be adjusted <a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a> <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>.

## [[tinkering_and_experimentation_with_ai_tools | Tinkering and experimentation with AI tools]]

### Varna: Exploring Embedding Space
Varna is an experimental tool designed to let users describe and generate images by adding and subtracting images and text concepts within an embedding space <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a> <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>. It leverages models like CLIP, which can describe both text and image inputs in the same semantic space <a class="yt-timestamp" data-t="01:15:45">[01:15:45]</a> <a class="yt-timestamp" data-t="01:15:51">[01:15:51]</a>.

Instead of traditional text prompting, Varna allows for "sliding" between concepts. For example, it can transform a selfie into a cartoon illustration or progressively change a young man's expression from happy to angry by sampling points along the conceptual distance in the embedding space <a class="yt-timestamp" data-t="01:17:58">[01:17:58]</a> <a class="yt-timestamp" data-t="01:19:01">[01:19:01]</a> <a class="yt-timestamp" data-t="01:19:11">[01:19:11]</a> <a class="yt-timestamp" data-t="01:19:25">[01:19:25]</a>. This approach aims to provide more precise control over AI outputs <a class="yt-timestamp" data-t="01:14:02">[01:14:02]</a>.

### Personal iMessage Chatbot
A personal iMessage chatbot, built using the LLaMA 2 13B base model, serves as a brainstorming and entertainment tool <a class="yt-timestamp" data-t="02:50:51">[02:50:51]</a> <a class="yt-timestamp" data-t="02:58:58">[02:58:58]</a>. Unlike fine-tuned models like ChatGPT or Claude, this base model is purely a text continuation model and hasn't undergone reinforcement learning for human feedback (RLHF) <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a> <a class="yt-timestamp" data-t="02:58:08">[02:58:08]</a>.

This means it generates text as if talking to a random person on the internet, offering "personal takes" on questions like "Where would you rather live: New York or London?" instead of responding with "I'm an AI language model..." <a class="yt-timestamp" data-t="03:00:59">[03:00:59]</a> <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. The user applies prompts to guide its responses, sometimes resulting in unexpected and creative answers <a class="yt-timestamp" data-t="03:10:07">[03:10:07]</a> <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

### Notion AI for [[knowledge_work_and_ai_tools | Knowledge Work and AI Tools]]
Notion AI is designed to have more context about a user's work within their workspace, leading to better suggestions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a> <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. It excels at:
*   **Transforming rough notes into structured content** <a class="yt-timestamp" data-t="00:59:33">[00:59:33]</a>. For instance, turning a "rainfall of bullet points" from meeting notes into presentable paragraphs with headings <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>.
*   **Collaborating on documents**, allowing users to edit outputs and ask the AI to revise or transform content into more complex formats like tables and databases <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a> <a class="yt-timestamp" data-t="01:01:19">[01:01:19]</a>.
*   **[[applications_of_ai_in_customer_research | Answering questions from a knowledge base]]**, particularly useful in team contexts where knowledge is vast and decentralized <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a> <a class="yt-timestamp" data-t="01:02:43">[01:02:43]</a>. It can help navigate "a forest of knowledge" to find specific meeting discussions or company policies <a class="yt-timestamp" data-t="01:03:44">[01:03:44]</a>.

## [[practical_approaches_to_ai | Practical approaches to AI]] Interaction

### Prompt Engineering vs. Scripting
There's a significant distinction between "prompt engineering" and "scripting" when interacting with LLMs <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.
*   **Prompt Engineering**: Involves writing prompts for production-ready tools (e.g., Notion AI) that are robust, resilient, well-tested, and accept diverse inputs reliably <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. This often includes techniques like few-shot prompting and structured outputs <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.
*   **Scripting/Prompting**: Refers to personal use of tools like ChatGPT, where the user can iterate, make revisions, and restart if the initial output isn't desired <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a> <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>. This encourages a trial-and-error approach, starting broad and narrowing down, or trying something simple and iteratively refining it <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a> <a class="yt-timestamp" data-t="00:43:44">[00:43:44]</a>.

### Iterative Prompting and Context
Providing more context to the model about goals and intentions generally leads to better suggestions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>. For personal use, this means starting with broad questions and progressively steering the AI towards a solution <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>. Using the "redo" button on conversational AI tools to generate multiple outputs for a broad question allows users to identify common themes and select the most relevant information, rather than relying solely on the AI's filtering <a class="yt-timestamp" data-t="00:45:21">[00:45:21]</a> <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a> <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>.

### Advanced Prompting Techniques
*   **Chain of Density Summaries**: A technique where the AI drafts a summary, then iteratively refines it by considering what was left out and making the information more dense without increasing length <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>. This improves the quality of specific outputs <a class="yt-timestamp" data-t="01:07:11">[01:07:11]</a>.
*   **Chain of Thought**: Similar to chain of density, this involves asking the AI to output its thinking steps or break down a problem into smaller steps before providing a final answer, which generally improves performance <a class="yt-timestamp" data-t="01:08:28">[01:08:28]</a>.
*   **"Putting Words in AI's Mouth"**: In platforms like OpenAI Playground, users can insert fake chat history to pretend the AI has already agreed to certain actions, making it more likely to perform a requested task <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a> <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## [[challenges_in_building_ai_tools | Challenges in Building AI Tools]]

### Model Behavior and Bias
Models like DALL-E 3 are "fundamentally unlikely" to produce "ugly" images due to their training and inherent capabilities, illustrating how tool design can limit user agency <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a> <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a> <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>. Similarly, GPT-4 Turbo has been anecdotally described as "lazy" or more efficient with compute, sometimes producing more concise outputs or being less likely to use other tools like DALL-E 3 unless explicitly commanded <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a> <a class="yt-timestamp" data-t="01:09:41">[01:09:41]</a> <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. The model's tendency to over-steer based on specific instructions can also introduce biases <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a> <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

### Anthropomorphization and Expectations
Users often anthropomorphize AI models, projecting human-like qualities and intentions onto them <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This can lead to unrealistic expectations or fears, such as concerns about AI replacing human roles like therapists <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a> <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>. The "packaging" of an AI tool, such as chat interfaces that make it feel like talking to an entity, significantly influences user perception <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a> <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

Organizations building AI tools for professional contexts generally aim for an "intelligent thought calculator" rather than a complete "simulacrum of humans" with human-like traits like daydreaming or defiance <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a> <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.