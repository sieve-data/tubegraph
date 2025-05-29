---
title: Comparison of model performance in app generation
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

This article compares the performance of different AI models, specifically DeepSeek B3 and Sonnet 3.5, in the context of generating AI applications, using the `b.new` DIY platform.

## `b.new` DIY Overview

`b.new` DIY is a hosted version of `b.new` that allows users to utilize their own API keys and local setup to generate AI applications <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike `b.new`, which is a fully hosted version by Tech Le, `b.new` DIY requires local installation and setup <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. DeepSeek B3 and DeepSeek R1 models can be integrated into `b.new` DIY via Nebius AI Studio and OpenRouter <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Nebius AI Studio is noted as a cost-effective model inference provider, offering access to models like DeepSeek B3, DeepSeek R1, Cohere 2.5, and Meta Llama models <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Users can obtain credits, such as $25 worth of credit, when signing up for Nebius AI Studio <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Model Performance in App Generation

### DeepSeek B3

DeepSeek B3 was used in a demonstration to generate a simple blog application using Astro framework within `b.new` DIY <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The model successfully generated a simple app <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a> <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. While it created a functional project, the generated app appeared to be a "Simple app as like from template" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

Further attempts to refine the UI part of the app with DeepSeek B3 resulted in "nothing useful" and "just the same thing with few extra Edition" <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. The demonstrator noted they were "not impressed by the results" when given a one-liner prompt, suggesting that a more detailed or "good prompt" might yield better outcomes <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

It was suggested that DeepSeek B3 "can be helpful" <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, especially in the [[using_ai_models_for_coding_assistance | code fixing part]] or for asking questions about existing code <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### DeepSeek R1

DeepSeek R1 was mentioned as an alternative to DeepSeek B3 available through Nebius AI Studio <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. However, it was not used for the app generation demonstration because it "takes time" due to its "speed and the thinking capabilities" compared to DeepSeek B3 <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Sonnet 3.5 by Claude

In a direct comparison, Sonnet 3.5 by Claude was stated to be "still better in generating app from a scratch" than DeepSeek B3 <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This observation was based on tests conducted in various environments including Cursor, Wind Surf, and Lovable <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

## Conclusion

While DeepSeek B3 can generate simple applications, its performance in generating complex or refined apps from scratch, especially with brief prompts, is not as impressive as Sonnet 3.5 by Claude <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. DeepSeek B3 might be more suitable for tasks like [[using_ai_models_for_coding_assistance | code fixing]] or query-based code assistance <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. DeepSeek R1 is noted for slower performance than B3, making it less ideal for rapid app generation during demonstrations <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

Users integrating these models via OpenRouter should be aware that "sometimes you feel that it's giving very slow response" <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. For general [[benchmarking_ai_models | model comparison]], Nebius AI Studio provides tools to [[comparing_ai_models_using_nebius_ai_studio | compare models]] like B3 and R1 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.