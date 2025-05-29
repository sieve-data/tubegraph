---
title: Integration of NV Studio and BoltDIY
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

[[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] is a self-hosted version of B.new, allowing users to run AI applications locally with their own API keys and setup <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This provides a similar app generation experience to the hosted B.new, but with local control <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. NV Studio is a model inference provider that offers access to various large language models, including DeepSeek V3 and DeepSeek R1 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Setting up BoltDIY

To use [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]], you need to install it on your device <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
Installation steps typically involve:
*   Downloading the repository (e.g., via Git) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   Running `npm install` for project dependencies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   Running `npm Dev` to start the application <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
Docker can also be used to run [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Acquiring and Using Free NV Studio Credits

NV Studio provides various LLM models, including DeepSeek V3, DeepSeek R1, Cohere, Llama models, and more <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It is considered one of the cheapest providers for accessing free models <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

To obtain free credits for NV Studio:
1.  Sign up for NV Studio to receive $1 worth of credit <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
2.  Go to the "Billing" tab on the NV Studio website <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
3.  Use the "text to image as code" voucher to get an additional $25 worth of credit <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a><a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This information can often be found on their Twitter <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Integrating NV Studio with BoltDIY via OpenRouter

To use [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] or [[using_deepseek_v3_and_r1_models_in_boltdiy | R1 models]] from NV Studio within [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]], OpenRouter serves as an intermediary <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a><a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a><a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Steps for Integration:

1.  **Get NV Studio API Key**: Navigate to the API key section in NV Studio and obtain your NVUs keys <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
2.  **Configure OpenRouter**:
    *   Go to OpenRouter and search for DeepSeek models <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   Select NV Studio as the provider <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste the copied NV Studio API key into the OpenRouter configuration for NV Studio <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
3.  **Modify BoltDIY Codebase**:
    *   Open your local [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] project in a code editor like VS Code <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   Locate the file `app/live/modules/lm/providers/open.ts` <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   Copy the model ID for [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] (or R1) from NV Studio <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
    *   Replace the existing model ID in the `open.ts` file with the copied DeepSeek model ID <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Change the model label (name) in the `open.ts` file to something descriptive like "NVUs DeepSeek" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
4.  **Add OpenRouter API Key to BoltDIY**:
    *   In the [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] interface, select "OpenRouter" as the provider <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Go to OpenRouter settings, create a new API key <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Paste this newly created OpenRouter key into the [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] setup <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

Once configured, the [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek model]] from NV Studio will appear in the [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] model selection <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Performance and Use Cases

The integration allows for the generation of AI applications, such as a simple blog using Astro <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. OpenRouter's activity section allows users to monitor costs, timing, and speed of model usage <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

While [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] can be helpful, its performance in generating full applications from scratch may not match models like Claude Sonnet 3.5 <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. However, [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] might be more effective for tasks like code fixing or answering questions about existing code <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

Users may experience slow response times when using OpenRouter API keys, though the cause is not always clear <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Using free credits from NV Studio makes [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] and [[using_deepseek_v3_and_r1_models_in_boltdiy | R1]] accessible for experimentation within [[using_deepseek_v3_and_r1_models_in_boltdiy | Bolt.DIY]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.