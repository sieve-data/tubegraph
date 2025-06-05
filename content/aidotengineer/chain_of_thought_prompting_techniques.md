---
title: Chain of thought prompting techniques
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

[[chain_of_thought_reasoning_in_ai | Chain of Thought prompting]] is a revolutionary technique in prompt engineering, particularly impactful for its efficiency in test time compute <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is Chain of Thought Prompting?

[[chain_of_thought_reasoning_in_ai | Chain of Thought prompting]] involves instructing a language model to reason or "think" about a problem or solution before directly providing the final answer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This approach breaks down complex problems into smaller, manageable sub-problems <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Benefits of Chain of Thought Prompting

*   **Troubleshooting Insights:** It provides a glimpse into the model's thought process, which can be valuable for troubleshooting and understanding its output <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Wide Applicability:** It is widely applicable across various models <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Ease of Implementation:** This technique is relatively easy to implement <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Built-in Capability:** It is so powerful that it is now being integrated into [[reasoning_models_and_their_unique_prompting_requirements | reasoning models]], making explicit instruction often unnecessary for those models <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Implementation Methods

#### Zero-Shot Chain of Thought

The classic zero-shot method involves adding a simple phrase to your prompt that encourages the model to think before generating the output <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This prompts the model to generate a "reasoning token" beforehand <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Common phrases include:
*   "think step by step" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
*   "take a breath and take it through things" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

#### [[fewshot_prompting_strategies | Few-Shot Chain of Thought]]

Another popular method is to provide [[fewshot_prompting_strategies | few-shot examples]] that demonstrate the desired reasoning steps <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. For instance, when solving math problems, you can include another math problem in the prompt, showing the step-by-step reasoning process you want the model to mimic <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

#### Automated Chain of Thought

Large Language Models (LLMs) can also be used to generate these reasoning chains automatically <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Automatic Chain of Thought:** A more involved framework that uses LLMs to generate reasoning chains <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Auto-Reason:** A single prompt where you pass your task or question, and it generates reasoning chains, often including [[fewshot_prompting_strategies | few-shot examples]] of these chains <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This can be tried out on Prompt Hub <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Training Templates:** DeepSeek's R1 model training template generated its thinking process within "think" tags, then used these generated reasoning chains to train the model for effective [[chain_of_thought_reasoning_in_ai | Chain of Thought]] capabilities <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This template is also available on Prompt Hub <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### When to Use Chain of Thought Prompting

[[chain_of_thought_reasoning_in_ai | Chain of Thought prompting]] is especially helpful when dealing with complex problems <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Chain of Thought with [[reasoning_models_and_their_unique_prompting_requirements | Reasoning Models]]

[[reasoning_models_and_their_unique_prompting_requirements | Reasoning models]] are different in how they work and how they are prompted <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. While [[chain_of_thought_reasoning_in_ai | Chain of Thought prompting]] is beneficial, providing additional examples (as in [[fewshot_prompting_strategies | few-shot prompting]]) can sometimes degrade performance with these models <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Researchers at Microsoft (with their MedPrompt framework) and DeepSeek (with R1) observed this phenomenon, where [[fewshot_prompting_strategies | few-shot]] examples led to worse performance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. OpenAI also noted that overcomplicating context can confuse the model <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

For [[reasoning_models_and_their_unique_prompting_requirements | reasoning models]], strategies include:
*   **Minimal Prompting:** Focus on a clear task description <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Encourage Reasoning:** If encountering performance issues, encouraging the model to reason more can be helpful <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Research shows that more reasoning often leads to better output and increased accuracy <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Avoid Excessive Few-Shot Prompting:** If using [[fewshot_prompting_strategies | few-shot examples]], start with only one or two <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **No Explicit Reasoning Instructions:** Avoid instructing the model *how* to reason, as it's built-in, and doing so can hurt performance <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Resources

A wide range of [[chain_of_thought_reasoning_in_ai | Chain of Thought]] and other [[role_of_reasoning_models_in_application_development | reasoning model]] templates are available for free on Prompt Hub <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. There are also articles on the Prompt Engineering Substack and blog posts that provide further information <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.