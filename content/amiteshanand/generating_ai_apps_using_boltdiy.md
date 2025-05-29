---
title: Generating AI apps using BoltDIY
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

[[boltdiy_setup_and_installation | BoltDIY]] is a self-hosted version of b.new that allows users to generate AI applications using their own API keys and local setup <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike the hosted b.new version by TechLe, which requires no setup <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, [[boltdiy_setup_and_installation | BoltDIY]] provides control over the environment and model usage <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## BoltDIY Setup

To use [[boltdiy_setup_and_installation | BoltDIY]], users must first install it on their local machine <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The installation process involves:
*   Cloning the [[boltdiy_setup_and_installation | BoltDIY]] repository <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Running `npm install` to set up project dependencies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   Running `npm Dev` to start the application, often using Docker <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Initial setup might show errors if [[api_keys_configuration_for_boltdiy | API keys]] are not configured <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Integrating Free DeepSeek Models (V3 & R1)

To leverage free DeepSeek V3 or R1 models within [[boltdiy_setup_and_installation | BoltDIY]], a specific configuration involving NV Studio and OpenRouter is required.

### Accessing NV Models

NV Studio is a model inference provider that offers access to various LLM models, including DeepSeek V3 and R1, Coho 2.5, and Meta Llama models <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. NV is noted for being one of the cheapest providers <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Users can get free access to these models:
*   Signing up for NV Studio provides $1 worth of credit <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Applying a specific code (e.g., "text to image as code" voucher mentioned on their Twitter) can grant an additional $25 worth of credit <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

To use NV models, users need to obtain their NV API keys from the API key section within NV Studio <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Configuring OpenRouter

OpenRouter acts as an intermediary service to access DeepSeek models through NV Studio <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
1.  Go to OpenRouter and search for DeepSeek V3 or R1 <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
2.  In OpenRouter's settings, click the NV icon to configure it <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Paste the copied NV API key into the designated field in OpenRouter and save it <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

OpenRouter allows users to monitor the performance, activity, and cost of their model usage <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Modifying BoltDIY Codebase

To enable [[free_access_to_nv_models_in_boltdiy | free access to NV models in BoltDIY]], a specific file in the local [[boltdiy_setup_and_installation | BoltDIY]] project needs modification:
1.  Navigate to `app/live/modules/LLM/providers` within the [[boltdiy_setup_and_installation | BoltDIY]] project in a code editor like VS Code <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
2.  Open the `open.ts` file <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
3.  Identify the desired DeepSeek model (e.g., DeepSeek V3) from OpenRouter and copy its model ID <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
4.  Replace the existing model ID in `open.ts` with the copied DeepSeek model ID <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
5.  Change the model's label in the code (e.g., to "NV DeepSeek") so it appears correctly in the [[boltdiy_setup_and_installation | BoltDIY]] interface <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Configuring API Keys in BoltDIY

Finally, [[api_keys_configuration_for_boltdiy | API keys]] from OpenRouter need to be added to [[boltdiy_setup_and_installation | BoltDIY]]:
1.  Go to OpenRouter settings, click "Keys," and create a new key <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  This OpenRouter key will be used in the [[boltdiy_setup_and_installation | BoltDIY]] setup <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Generating AI Applications

With the setup complete, users can start [[building_an_aipowered_app_in_under_10_minutes | building an AI-powered app in under 10 minutes]] using [[boltdiy_setup_and_installation | BoltDIY]]:
1.  In the [[boltdiy_setup_and_installation | BoltDIY]] interface, select "OpenRouter" as the provider <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  Choose the configured NV DeepSeek model <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  Provide a prompt, such as "build a simple blog using Astro," and [[boltdiy_setup_and_installation | BoltDIY]] will generate the application <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

While DeepSeek V3 can generate functional apps <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>, models like Claude's Sonnet 3.5 are noted as being better at generating apps from scratch <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. DeepSeek V3 may be more helpful for tasks like code fixing <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

**Note on Performance**: When using [[api_keys_configuration_for_boltdiy | API keys]] from OpenRouter, responses can sometimes be slow <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.