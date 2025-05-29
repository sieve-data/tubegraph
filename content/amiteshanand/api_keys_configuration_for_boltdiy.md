---
title: API keys configuration for BoltDIY
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

[[boltdiy_setup_and_installation | BoltDIY]] is a hosted version of B.new that allows users to utilize their own API keys and local setup to [[generating_ai_apps_using_boltdiy | generate AI apps]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike B.new, which is a fully hosted service by TechLe, [[boltdiy_setup_and_installation | BoltDIY]] runs on a local machine <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This guide explains how to configure API keys to access DeepSeek v3 or DeepSeek R1 models within [[boltdiy_setup_and_installation | BoltDIY]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## BoltDIY Setup
To begin, users need to install [[boltdiy_setup_and_installation | BoltDIY]] on their device by following the steps in the [[boltdiy_setup_and_installation | BoltDIY]] repository <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This typically involves downloading the Git repository, running `npm install` for project dependencies, and then `npm dev` to start the application <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Docker can also be used to run the application <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Integrating Nebius AI Studio Models
[[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]] is a model inference provider that offers various LLM models, including DeepSeek v3 and DeepSeek R1 <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Other models like Cohere Command R 2.5, Mixtral 8x7B mini, and Meta Llama models are also available <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Obtaining Nebius AI Studio API Keys
To use DeepSeek models in [[boltdiy_setup_and_installation | BoltDIY]], users must first obtain their API keys from [[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. [[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]] is highlighted as one of the cheapest providers for `[[free_access_to_nv_models_in_boltdiy | free Nebius models]]` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

Users can obtain `[[free_access_to_nv_models_in_boltdiy | free Nebius model]]` access by:
*   Signing up for [[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]], which provides an initial $1 credit <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Applying a promotional code (e.g., found on their Twitter, or by using a "text to image as code" voucher) to receive an additional $25 worth of credit <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Configuring OpenRouter with Nebius AI Studio Keys
OpenRouter acts as an intermediary, allowing [[boltdiy_setup_and_installation | BoltDIY]] to access DeepSeek models <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
1.  Navigate to OpenRouter and search for DeepSeek v3 <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. DeepSeek v3 is preferred over R1 due to its speed <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Click on the Nebius AI icon within OpenRouter's configuration <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Paste the `[[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]]` API key copied earlier into the designated field and save it <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Obtaining OpenRouter API Keys for BoltDIY
After configuring OpenRouter with Nebius AI Studio keys, a new OpenRouter API key needs to be created for use in [[boltdiy_setup_and_installation | BoltDIY]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
1.  Go to OpenRouter settings.
2.  Click on "Keys" and create a new key <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
3.  This key will be used in the [[boltdiy_setup_and_installation | BoltDIY]] setup <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Modifying BoltDIY Codebase
To enable the use of Nebius AI Studio models (like DeepSeek v3) through OpenRouter within [[boltdiy_setup_and_installation | BoltDIY]], a specific file in the [[boltdiy_setup_and_installation | BoltDIY]] codebase needs to be modified <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
1.  Open the [[boltdiy_setup_and_installation | BoltDIY]] project in a code editor (e.g., VS Code) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  Navigate to `app/live/modules/lm/providers` <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
3.  Open the `open.ts` file <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  Within `open.ts`, locate and replace the existing model ID with the DeepSeek v3 model ID copied from OpenRouter <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
5.  Change the model label to "Nebius DeepSeek" (or a similar descriptive name) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This name will appear in the [[boltdiy_setup_and_installation | BoltDIY]] interface <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Using Configured Models in BoltDIY
Once the API keys are configured and the `open.ts` file is updated:
1.  In [[boltdiy_setup_and_installation | BoltDIY]], select "OpenRouter" as the provider <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Choose "Nebius DeepSeek" (the custom label) as the model <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  Input the OpenRouter API key into the [[boltdiy_setup_and_installation | BoltDIY]] setup <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
4.  The system is now ready to `[[generating_ai_apps_using_boltdiy | build applications]]` using the configured DeepSeek v3 model <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Performance Notes
DeepSeek v3 can `[[generating_ai_apps_using_boltdiy | generate applications]]` from a single prompt, like a simple blog using Astro <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   Users can monitor performance, cost, and speed of API calls through OpenRouter's activity section <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   While DeepSeek v3 can be helpful, Sonnet 3.5 by Cloud is noted as better for `[[generating_ai_apps_using_boltdiy | generating apps]]` from scratch, based on comparisons across platforms like Cursor, WindSurf, and `[[using_lovable_ai_app_builder | Lovable]]` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   DeepSeek v3 might be more effective for code-fixing or answering questions related to existing code <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Occasionally, slow responses might occur when using API keys from OpenRouter <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

By following these steps, users can leverage `[[free_access_to_nv_models_in_boltdiy | free DeepSeek v3 and R1]]` access from [[api_and_model_integration_with_nebius_ai_studio | Nebius AI Studio]] through OpenRouter within their [[boltdiy_setup_and_installation | BoltDIY]] projects <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.