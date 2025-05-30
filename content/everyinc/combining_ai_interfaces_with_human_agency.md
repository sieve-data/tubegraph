---
title: Combining AI interfaces with human agency
videoId: OeKEXnNP2yA
---

From: [[everyinc]] <br/> 

The integration of artificial intelligence into daily life, particularly through large language models (LLMs), presents a paradigm shift in how humans interact with technology and engage in creative work. A key philosophy guiding this integration is the notion of building interfaces that enable AI to assist and guide users without diminishing their [[managing_agency_in_the_age_of_ai | agency]] <a class="yt-timestamp" data-t="03:49:52">[03:49:52]</a>. This approach aims to foster a "human future" where AI augments human capabilities, rather than replacing them <a class="yt-timestamp" data-t="03:31:47">[03:31:47]</a>.

## AI as a Tool, Not an Agent

Language models, when viewed from a fundamental perspective, are less like agents with their own will and more like sophisticated calculators <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. They function as statistical models predicting probability distributions, which can be seen as a form of "thought calculator" <a class="yt-timestamp" data-t="05:17:34">[05:17:34]</a>, <a class="yt-timestamp" data-t="21:01:21">[21:01:21]</a>. This perspective helps in understanding that while AI can be packaged to appear human-like <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>, its core nature is mathematical and functional <a class="yt-timestamp" data-t="05:15:23">[05:15:23]</a>.

## Preserving Human Agency in AI Design

Despite AI being a function, its design can unintentionally or intentionally influence user [[managing_agency_in_the_age_of_ai | agency]] <a class="yt-timestamp" data-t="05:37:37">[05:37:37]</a>. For example, image generation tools like DALL-E 3 are fundamentally unlikely to output "ugly" images due to their training <a class="yt-timestamp" data-t="06:37:04">[06:37:04]</a>, <a class="yt-timestamp" data-t="06:42:04">[06:42:04]</a>. This constraint, while aiming for generally aesthetic results, can limit a user's creative control, effectively taking away some of their [[managing_agency_in_the_age_of_ai | agency]] <a class="yt-timestamp" data-t="07:08:44">[07:08:44]</a>. Similarly, established tools like Photoshop or Instagram, through their specific features, tend to shape the output style, influencing what can be easily created <a class="yt-timestamp" data-t="09:42:06">[09:42:06]</a>. The challenge lies in designing interfaces that offer powerful capabilities without disempowering the user <a class="yt-timestamp" data-t="07:18:29">[07:18:29]</a>.

## Understanding AI's Underlying Mechanism: Embeddings

A deeper understanding of how AI models process information can inform better interface design. Concepts like "embeddings" provide a "spatial" way of thinking about the possibility space of AI outputs <a class="yt-timestamp" data-t="10:41:43">[10:41:43]</a>. An embedding is a quantitative summary, a list of numbers, that represents the semantic content of text or images <a class="yt-timestamp" data-t="10:50:57">[10:50:57]</a>. These numbers can be viewed as coordinates in a high-dimensional space, where semantically similar items are closer together <a class="yt-timestamp" data-t="11:47:58">[11:47:58]</a>.

This numerical representation allows for mathematical manipulation <a class="yt-timestamp" data-t="13:15:06">[13:15:06]</a>. For instance, just as an RGB value allows for precise control over color (making it lighter, more blue), embeddings can be manipulated to modify text or images with greater precision than simple chat prompts <a class="yt-timestamp" data-t="13:27:06">[13:27:06]</a>, <a class="yt-timestamp" data-t="14:08:52">[14:08:52]</a>.

### Designing for Agency: The "Varna" Demo

A prototype tool called "Varna" exemplifies this approach by allowing users to describe images through adding and subtracting concepts represented in an embedding space <a class="yt-timestamp" data-t="14:44:48">[14:44:48]</a>. Using models like CLIP, which can describe both text and image inputs in the same embedding space <a class="yt-timestamp" data-t="15:43:08">[15:43:08]</a>, Varna enables users to blend images or concepts by selecting points along a "slider" in this conceptual space <a class="yt-timestamp" data-t="18:41:14">[18:41:14]</a>. This allows for exploration of stylistic or emotional scales, offering fine-grained control over the generated output <a class="yt-timestamp" data-t="19:09:07">[19:09:07]</a>.

This type of interface transforms the interaction from asking an "agent" to a more direct manipulation of a "calculator for images and concepts" <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. It makes the AI feel more like a tool, allowing the user to retain greater [[managing_agency_in_the_age_of_ai | agency]] <a class="yt-timestamp" data-t="21:30:17">[21:30:17]</a>.

## Prompt Engineering vs. Scripting

The way users interact with AI models, especially through prompts, can be compared to different approaches in programming:

*   **Prompt Engineering (Software Engineering):** This involves crafting robust, resilient prompts for widespread product use (e.g., in Notion AI) <a class="yt-timestamp" data-t="34:45:00">[34:45:00]</a>. These prompts must handle diverse inputs reliably and are heavily tested and evaluated <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a>.
*   **Prompt Scripting (Personal Use):** When interacting with tools like ChatGPT, users can adopt a more experimental, iterative approach, similar to writing quick scripts <a class="yt-timestamp" data-t="35:26:00">[35:26:00]</a>. If the initial output isn't perfect, the user can revise, ask follow-up questions, or restart, without the need for the same robustness as product-level prompts <a class="yt-timestamp" data-t="36:14:00">[36:14:00]</a>. This encourages a "bang away" method to explore the tool's capabilities and limits <a class="yt-timestamp" data-t="37:32:00">[37:32:00]</a>.

## Leveraging Iteration and Context for Better Results

Effective interaction with AI, particularly in personal use, benefits from providing more context and embracing iterative refinement:

*   **More Context, Better Suggestions:** AI tools generally provide better suggestions when they have more context about the user's goals <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="40:37:00">[40:37:00]</a>. Instead of narrow questions, broad inquiries that include background information (e.g., "I'm trying to read an 80GB dataset on a 40GB RAM Linux machine running Python X.Y, how should I approach this problem?") lead to more relevant approaches <a class="yt-timestamp" data-t="44:17:00">[44:17:00]</a>.
*   **Iterative Refinement:** For tasks like travel planning, asking broad questions and generating multiple outputs allows the user to identify common suggestions and apply their own "last-mile filtering" based on personal preferences, rather than solely trusting the AI's "best" recommendation <a class="yt-timestamp" data-t="47:05:00">[47:05:00]</a>. This is because current models, even with custom instructions, may still over-steer based on specific words in a prompt <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>.

### Practical Applications
*   **Programming Help:** LLMs can assist with high-level programming problems, such as understanding new libraries or approaches to complex data processing, beyond what code completion tools like GitHub Copilot offer <a class="yt-timestamp" data-t="41:15:00">[41:15:00]</a>.
*   **Creative Content Generation:** Tools like Notion AI can transform rough notes into structured, presentable documents, adding headings, summarizing content, and reformatting into tables or databases <a class="yt-timestamp" data-t="59:33:00">[59:33:00]</a>. This workflow facilitates [[integrating_ai_with_creative_processes | integrating AI with creative processes]].
*   **Personalized Recommendations:** By iteratively providing lists of liked items (e.g., books) and asking for a "vibe" analysis before requesting recommendations, users can guide the AI towards more tailored suggestions, even asking for "off the beaten path" options to avoid common recommendations <a class="yt-timestamp" data-t="53:36:00">[53:36:00]</a>.

## Advanced Prompting Techniques

For highly specific or robust outputs, more advanced prompting techniques are employed:

*   **Chain-of-Density:** This technique involves asking the model to write multiple drafts of a summary, with each subsequent draft prompted to include more detail or be more concise without increasing length <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>. This ensures a dense, information-rich final output.
*   **Chain-of-Thought:** Similar to Chain-of-Density, this involves instructing the AI to output its intermediate thinking steps before providing a final answer <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>. This improves the quality of the final output by forcing the model to "think through" the problem <a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>.
*   **Manipulating AI Behavior:** In developer playgrounds (e.g., `platform.openai.com`), users have full control over parameters and can even insert "fake chat history" to "put words in the AI's mouth" <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>. This can be used to bypass "guardrails" or influence the AI to produce specific outputs that might otherwise be difficult to elicit <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.

## AI in Collaborative Contexts

AI tools also offer significant benefits in collaborative environments. Notion's Q&A bot, for example, allows users to ask questions about internal company knowledge (e.g., HR policies, project details) <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This is particularly useful in large organizations with vast, constantly changing knowledge bases, reducing repetitive questions for individuals and making information more accessible <a class="yt-timestamp" data-t="01:04:39">[01:04:39]</a>. This represents an important step in [[human_ai_collaboration | human AI collaboration]] for knowledge management.

In summary, the ongoing evolution of AI interfaces emphasizes [[managing_agency_in_the_age_of_ai | managing agency in the age of AI]] by viewing AI as a powerful, manipulable tool rather than an autonomous agent. By understanding its underlying mechanisms, designing precise interfaces, and applying iterative prompting techniques, users can leverage AI to augment their capabilities and achieve more specific, tailored outcomes, fostering a more effective [[the_future_of_ai_and_human_interaction | future of AI and human interaction]].