---
title: Comparison with Claude 35 Sonet
videoId: -GmEIqi0yNE
---

From: [[colemedin]] <br/> 

DeepSeek R1, an open-source reasoning Large Language Model (LLM), has been positioned as a strong competitor to existing LLMs, including [[speed_and_performance_comparison_with_other_llms | Claude 3.5 Sonet]]. It is described as being "literally more powerful than Open AI 01, Claude 3.5 Sonet, and basically every LLM out there" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Cost Efficiency
One of the most significant advantages of DeepSeek R1 is its cost-effectiveness. The pricing for R1 is substantially lower than that of Claude 3.5 Sonet and other leading models <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. While Claude 3.5 Sonet costs $3 for every million input tokens <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, DeepSeek R1 is priced at 55 cents for every million input tokens and $2.19 for every million output tokens <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This makes R1 "dozens and dozens of times cheaper" while offering comparable or superior performance <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Model Size
While models like Llama 70B, Claude Haiku, or Claude Sonet are "so much bigger" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, DeepSeek R1 offers smaller versions, such as a 14 billion parameter model, which is capable of running on most personal computers <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Even this smaller version is noted to be "on par with 01 mini" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, indicating its efficiency despite its size.

## Performance as an AI Coding Assistant

DeepSeek R1 was directly compared to Claude 3.5 Sonet in a practical demonstration using [[building_ai_apps_with_v0_and_claude | bolt.DIY]], an open-source AI coding assistant <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The objective was to build a chat interface that interacts with an n8n AI agent, including features like conversation history management and Superbase authentication <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This task is considered "reasonably complex" and something many LLMs struggle with <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

Historically, Claude 3.5 Sonet has been "usually the king of AI coding" <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>, with platforms like [[comparison_of_windsurf_with_other_ai_tools_and_platforms | lovable]] and `bolt.new` optimizing for it <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### DeepSeek R1 Results
Using the most powerful 671 billion parameter version of DeepSeek R1 via the DeepSeek API <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, the application was built in a "single shot" (single prompt) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. The entire process used only 9,000 tokens, costing "multitudes less than a single penny" <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

The initial output from DeepSeek R1 was highly functional and visually appealing, outperforming a similar app built with [[comparison_of_windsurf_with_other_ai_tools_and_platforms | lovable]] (which uses Claude 3.5 Sonet) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. While the initial build had minor issues like message duplication and missing "new conversation" and "logout" buttons <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>, these were easily fixed with "a couple of messages" <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

### Claude 3.5 Sonet Results
When the exact same prompt was used with Claude 3.5 Sonet, the initial result was "decent overall but... definitely not as nice looking as R1" <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. It also missed functionalities like creating a new conversation and logging out <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Crucially, Claude 3.5 Sonet failed to communicate with the n8n agent in the first attempt, meaning it did not work "right out the gate" <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. This highlighted that "even other really good LLMs like Sonet can fall apart when we have more complex requests for apps" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

In conclusion, DeepSeek R1 demonstrated a "much much better" performance in building the application compared to Claude 3.5 Sonet <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>, providing a more refined and functional output initially and proving easier to refine.