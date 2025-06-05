---
title: Importance of prompt engineering
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

[[prompt_engineering_and_management | Prompt engineering]] is a crucial aspect of working with large language models (LLMs), focusing on crafting effective inputs to achieve desired outputs <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Dan, co-founder of Prompt Hub, emphasizes its significance for anyone building AI-based features <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Why Prompt Engineering is Still Important

Despite a common misconception that one can "just tell the model to do" something, [[prompt_engineering_and_management | prompt engineering]] is far more nuanced in practice <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Accessibility and Output Quality**: It is the easiest and most accessible way to obtain better outputs from LLMs <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Competitive Advantage**: While everyone has access to the same models, the prompts, architecture, and surrounding systems provide a competitive advantage in product development <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Simplicity and Management**: Spending time to refine prompts can lead to much simpler and more manageable solutions compared to immediately resorting to complex methods like Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. If a problem can be solved via [[prompt_engineering_and_management | prompt engineering]], it is often the more straightforward path <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Key Prompt Engineering Techniques

Various [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | techniques and patterns]] are used to enhance LLM performance.

### Chain of Thought Prompting
[[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | Chain of Thought prompting]] involves instructing the model to reason or "think about the problem" before providing an answer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Process**: It breaks down problems into sub-problems, allowing insight into the model's thinking process, which aids troubleshooting <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Applicability**: It is widely applicable across models and easy to implement <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Implementation**:
    *   **Zero-shot**: Adding phrases like "think step by step" or "take a breath and take it through" encourages reasoning <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   **Few-shot**: Providing examples of reasoning steps within the prompt can guide the model <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   **Automatic Generation**: LLMs can generate these reasoning chains themselves, such as through frameworks like Automatic Chain of Thought or AutoReason <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. DeepSeek's R1 model training also involved generating thinking processes within "think tags" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Use Case**: Highly helpful for complex problems <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Few-Shot Prompting
[[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | Few-shot prompting]] involves including examples for the model to mimic or understand, effectively "showing rather than telling" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Benefit**: This teaches the model a client's tone or style through input/output examples (e.g., a brief and related content) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Efficiency**: Most performance gains are achieved with just one or two examples <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Performance can even degrade with too many examples <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Best Practice**: Builders should select one or two diverse examples that cover different expected inputs <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Meta Prompting
[[prompt_engineering_and_management | Meta prompting]] is the practice of using LLMs to create, refine, or improve prompts <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Frameworks and Tools**: Various frameworks exist, some requiring voting knowledge, others more user-friendly <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Tools from Anthropic, OpenAI's playground, and Prompt Hub offer this functionality <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Model-Specific Optimization**: Prompt Hub's tool, for example, tailors the meta prompt based on the selected model provider (e.g., OpenAI vs. Anthropic) because optimal prompts can differ between models <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. An iterative co-pilot feature allows users to run prompts and provide feedback <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Prompting Reasoning Models

Reasoning models like GPT-4 are fundamentally different in how they operate and how they should be prompted <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Caution with Examples**: Research by Microsoft (MedPrompt framework) and DeepSeek (R1 model) found that adding examples can lead to *worse* performance with these models <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. OpenAI also cautioned that providing additional context can overcomplicate things and confuse the model <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. If few-shot prompting is used, start with one or two examples at most <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Encourage Reasoning**: The more reasoning a model performs, the better its output can be <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Encouraging extended reasoning leads to better results and increased accuracy <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Phrases to encourage reasoning are often built into these models, so explicit instruction to reason might hurt performance <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Minimal Prompting**: For reasoning models, minimal [[prompt_engineering_and_management | prompting]] with a clear task description is often most effective <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Resources
Numerous free resources are available for [[prompt_engineering_and_management | prompt engineering]], including Prompt Engineering Substack, blogs, and community prompts on platforms like Prompt Hub <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.