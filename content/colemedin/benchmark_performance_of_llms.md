---
title: Benchmark performance of LLMs
videoId: -GmEIqi0yNE
---

From: [[colemedin]] <br/> 

The landscape of Artificial Intelligence (AI) is rapidly evolving, with a current focus on **reasoning models** – large language models (LLMs) that can "think to themselves" before generating a final answer <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This approach often leads to significantly better results <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Leading Reasoning LLMs

Several reasoning LLMs are currently available:
*   OpenAI's 01 and 03 <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   QWQ, an open-source version from Quen <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   DeepSeek's R1, an open-source reasoning LLM <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>

## DeepSeek R1's Performance Benchmarks

DeepSeek's R1 has garnered significant attention for its claimed performance <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It is presented as being "more powerful than open AI 01 Claude 3.5 Sonnet it basically every llm out there" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Official Benchmarks

DeepSeek's official blog release for R1 provides benchmark comparisons. While acknowledging potential bias, the results are notable <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:
*   R1 is compared to 01, 01 Mini, and DeepSeek V3 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   It performs "as well sometimes better sometimes a little bit worse than 01 in every Benchmark" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   This performance is particularly impressive given that R1 is a smaller, open-source model with significantly lower costs <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Performance of Smaller R1 Versions

DeepSeek has created smaller versions of R1 by fine-tuning existing models like Quen and [[using_llama_for_llms | Llama]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. These can be run locally using platforms like Olama or Hugging Face <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>:
*   The 14 billion parameter Quen version of R1 is "on par with 01 mini" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   A 14 billion parameter model is generally more accessible to run on personal computers compared to larger models like Llama 70B or Claude Haiku/Sonnet <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Cost-Effectiveness

[[challenges_and_costs_of_selfhosting_local_llms | R1 is considerably cheaper]] to use compared to its competitors <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>:
*   Pricing for R1 is $0.55 for every million input tokens and $2.19 for every million output tokens <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   This makes it "dozens and dozens of times cheaper" than 01, while offering comparable performance <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   It is also cheaper than Claude 3.5 Sonnet, which costs $3 for every million input tokens <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Real-World Application and Comparison

In a practical demonstration using Bolt.DIY, an [[using_local_language_models_llm_for_code_generation | open-source AI coding assistant]], R1 was tested against Claude 3.5 Sonnet to build a complex chat interface <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

#### R1's Performance in Bolt.DIY
*   The most powerful version of R1 (671 billion parameters via DeepSeek API) was used <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   It built the full application in a "single shot" (one prompt) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   The process used only 9,000 tokens, costing less than a single penny <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   The resulting application was visually appealing and functional, including Superbase authentication and conversation history management <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   Minor issues, such as duplicate messages and missing "new conversation" and "logout" buttons, were easily fixed with a few additional prompts <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

#### Claude 3.5 Sonnet's Performance in Bolt.DIY
*   Claude 3.5 Sonnet, a model widely used by other AI coding assistants like Bolt.new and Lovable <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>, was given the exact same prompt <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   The single-shot attempt by Sonnet resulted in an app that was "not as nice looking as R1" <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   It also missed features like creating new conversations and logging out <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   Critically, the app built by Sonnet failed to communicate with the n8n agent API, meaning core functionality was broken on the first attempt <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
*   R1 was observed to perform "much much better" in this complex coding task <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

## Conclusion

DeepSeek R1 demonstrates impressive [[speed_and_performance_comparison_with_other_llms | performance]], often outperforming established models like OpenAI's 01 and Claude 3.5 Sonnet, particularly in complex tasks like code generation <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Its open-source nature, the ability to run smaller versions locally, and its cost-effectiveness make it a compelling option for developers and AI enthusiasts <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.