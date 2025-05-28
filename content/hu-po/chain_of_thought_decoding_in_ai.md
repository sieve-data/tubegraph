---
title: Chain of Thought Decoding in AI
videoId: H5yd-uh9acY
---

From: [[hu-po]] <br/> 

[[Chain of Thought in AI Reasoning | Chain of Thought]] (CoT) refers to a technique where a large language model (LLM) explicitly thinks out loud or provides a sequence of reasoning steps before arriving at a final answer <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>. This internal monologue allows the LLM to process information more effectively and often leads to more accurate results <a class="yt-timestamp" data-t="01:20:54">[01:20:54]</a>.

## Decoding Process in LLMs
The process of "decoding" in LLMs refers to how the model selects the next token to output from its vocabulary <a class="yt-timestamp" data-t="01:14:37">[01:14:37]</a>. When an LLM predicts the next token, it assigns a probability to every possible token in its vocabulary (e.g., 30,000 different tokens) <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>.

Common decoding strategies include:
*   **Greedy Decoding**
    *   This method simply picks the token with the highest probability at each step <a class="yt-timestamp" data-t="01:14:52">[01:14:52]</a>.
    *   While straightforward, it can sometimes lead to incorrect answers because it doesn't explore alternative, potentially better, paths <a class="yt-timestamp" data-t="01:17:05">[01:17:05]</a>.
*   **Temperature Sampling**
    *   This is what users typically experience with LLMs <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a>.
    *   Instead of strictly picking the highest probability token, it samples from the probability distribution, allowing for more varied and "random" outputs <a class="yt-timestamp" data-t="01:19:01">[01:19:01]</a>. Higher temperatures make the probabilities of different tokens more equal, leading to more diverse responses <a class="yt-timestamp" data-t="01:22:52">[01:22:52]</a>.

## Chain of Thought Decoding
[[Structured chain of thought in AI models | Chain of Thought Decoding]] is a strategy that goes beyond simple greedy decoding by investigating multiple alternative tokens (the "top K" tokens) at each step of the decoding process <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. It uncovers [[Chain of Thought in AI Reasoning | Chain of Thought]] paths that are often inherently present within the LLM's potential sequences <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.

By exploring these alternative paths, particularly those that result in a longer [[Chain of Thought in AI Reasoning | Chain of Thought]], the model can arrive at the correct answer with higher confidence <a class="yt-timestamp" data-t="01:17:57">[01:17:57]</a>. The principle is that longer decoding paths are more likely to contain deeper reasoning <a class="yt-timestamp" data-t="01:20:40">[01:20:40]</a>.

### Advantages of Chain of Thought Decoding
*   **Improved Performance**: [[Structured chain of thought in AI models | Chain of Thought Decoding]] substantially outperforms standard greedy decoding, sometimes achieving twice the performance on benchmarks like mathematical reasoning tasks <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>, <a class="yt-timestamp" data-t="01:24:33">[01:24:33]</a>.
*   **Revealing Intrinsic Strategy**: It can better reveal the LLM's intrinsic strategy for solving a problem without external prompts <a class="yt-timestamp" data-t="01:25:59">[01:25:59]</a>. This is because it doesn't require explicit "think step by step" prompts, as the reasoning paths are elicited from the model's own decoding space <a class="yt-timestamp" data-t="01:27:43">[01:27:43]</a>.
*   **Higher Confidence**: Paths that incorporate [[Chain of Thought in AI Reasoning | Chain of Thought]] often lead to final answers with higher associated probabilities, indicating greater model confidence <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.

### Relationship to Prompt Engineering
Previously, prompt engineering techniques, such as instructing an LLM to "think step by step," were crucial to elicit [[Chain of Thought in AI Reasoning | Chain of Thought]] and improve answers <a class="yt-timestamp" data-t="01:21:11">[01:21:11]</a>. However, [[Structured chain of thought in AI models | Chain of Thought Decoding]] suggests that as the technique matures, the reliance on explicit prompting might decrease because the system can internally search for and utilize those reasoning paths <a class="yt-timestamp" data-t="01:26:58">[01:26:58]</a>.

### Computational Considerations
Exploring multiple decoding paths naturally incurs additional computational costs <a class="yt-timestamp" data-t="01:31:07">[01:31:07]</a>. Despite this, the performance gains, especially for smaller models, can be significant <a class="yt-timestamp" data-t="01:24:33">[01:24:33]</a>.

## Future Outlook
The concept of searching through the decoding space aligns with Rich Sutton's "bitter lesson," which emphasizes the power of learning and search in scaling AI performance <a class="yt-timestamp" data-t="01:30:10">[01:30:10]</a>. This approach offers an orthogonal path of improvement for LLMs and can potentially be combined with other techniques, such as using an [[Meta AI research | ensemble]] of LLMs, to achieve even greater accuracy <a class="yt-timestamp" data-t="01:43:05">[01:43:05]</a>. As models become larger and more capable, the need for complex, explicitly engineered [[Chain of Thought in AI Reasoning | Chain of Thought]] frameworks may diminish, with future models directly producing high-quality reasoning through advanced decoding <a class="yt-timestamp" data-t="01:25:03">[01:25:03]</a>.