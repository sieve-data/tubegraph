---
title: Free access to NV models in BoltDIY
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

This article details how to utilize free [[using_deepseek_v3_and_r1_models | DeepSeek V3]] or [[using_deepseek_v3_and_r1_models | DeepSeek R1]] models within [[boltdiy_setup_and_installation | BoltDIY]] by leveraging [[features_of_nebas_ai_studio | N Studio]] (also referred to as [[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]]) and OpenRouter. [[boltdiy_setup_and_installation | BoltDIY]] is a hosted version of B.new that allows users to deploy and manage their own AI applications locally using their own [[api_keys_configuration_for_boltdiy | API keys]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This contrasts with B.new, which is a fully hosted service by TechLe <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is BoltDIY?

[[boltdiy_setup_and_installation | BoltDIY]] is a version of B.new that runs on a user's local machine with a local setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It enables users to [[generating_ai_apps_using_boltdiy | generate AI apps]] using a similar interface to B.new <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Setting up BoltDIY

To install [[boltdiy_setup_and_installation | BoltDIY]], follow these steps from its GitHub repository:
1.  Download or clone the repository <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
2.  Run `npm install` to install project dependencies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
3.  Run `npm dev` to start the application <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
The application can also be run using Docker <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Accessing NV Models (DeepSeek V3/R1)

[[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] is a model inference provider that offers access to various large language models, including [[using_deepseek_v3_and_r1_models | DeepSeek V3]] and [[using_deepseek_v3_and_r1_models | DeepSeek R1]], as well as Cohere 2.5, Qwen 53 Mini, and Meta Llama models <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Obtaining Free Credits for NV Models
[[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] is noted as one of the cheapest providers <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Users can obtain free credits:
*   Signing up for [[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] provides $1 worth of credit <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   By going to the "Building Tab" and using the "text to image as code" option, users can receive an additional $25 worth of credit <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This promotion was found on their Twitter <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Retrieving NV API Keys
To use NV models, obtain your [[api_keys_configuration_for_boltdiy | API keys]] from the "API Key section" in [[features_of_nebas_ai_studio | N Studio]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Integrating NV Models with OpenRouter in BoltDIY

To use [[using_deepseek_v3_and_r1_models | DeepSeek]] models from [[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] within [[boltdiy_setup_and_installation | BoltDIY]], OpenRouter acts as an intermediary <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Configuring OpenRouter with NV API Key
1.  Navigate to OpenRouter <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  Click on the settings icon and select "nvs" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Paste the [[api_keys_configuration_for_boltdiy | nvs API key]] copied from [[features_of_nebas_ai_studio | N Studio]] into the designated field and save <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Modifying BoltDIY Codebase
1.  Open your local [[boltdiy_setup_and_installation | BoltDIY]] project in VS Code <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
2.  Navigate to `app/live/modules/LM/providers/open.ts` <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
3.  Within this file, you can configure OpenRouter models. To integrate [[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] models, replace the existing model ID with the copied model ID for [[using_deepseek_v3_and_r1_models | DeepSeek V3]] (e.g., `deepseek/deepseek-v3`) <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
4.  Change the model's label to something identifiable, such as "nvus DeepSeek" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This name will appear in the [[boltdiy_setup_and_installation | BoltDIY]] interface <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### Adding OpenRouter API Keys in BoltDIY
1.  In [[boltdiy_setup_and_installation | BoltDIY]], go to "Open Settings" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  Click on "Keys" and create a new key <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
3.  This key will be used for your [[boltdiy_setup_and_installation | BoltDIY]] setup <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## Using DeepSeek V3/R1 Models in BoltDIY

Once configured, you can select "OpenRouter" as the provider in [[boltdiy_setup_and_installation | BoltDIY]], then choose the "nvus DeepSeek" model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Performance and Use Cases
When using [[using_deepseek_v3_and_r1_models | DeepSeek V3]] or [[using_deepseek_v3_and_r1_models | R1]] models via OpenRouter in [[boltdiy_setup_and_installation | BoltDIY]], responses might sometimes be slow <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

For generating full applications from scratch, Cloud's Sonnet 3.5 is considered superior to [[using_deepseek_v3_and_r1_models | DeepSeek V3]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. However, [[using_deepseek_v3_and_r1_models | DeepSeek V3]] can be helpful for code fixing and asking questions about existing code within a project <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

To use [[using_deepseek_v3_and_r1_models | DeepSeek V3]] or [[using_deepseek_v3_and_r1_models | R1]] in your [[boltdiy_setup_and_installation | BoltDIY]] project, you need an OpenRouter account, [[api_integration_with_nvs_ai_studio_for_model_usage | nvs AI Studio]] models, and to modify the `open.ts` file in the [[boltdiy_setup_and_installation | BoltDIY]] codebase <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.