---
title: Setting up BoltDIY with local API keys
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

BoltDIY is a self-hosted version of B.new, allowing users to run AI applications on their local machine using their own API keys and local setup <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike B.new, which is a hosted service by Tech Le where you pay and interact with AI apps directly <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, BoltDIY requires local installation <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Installation
To install BoltDIY, you need to go to its repository and follow the provided steps <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This typically involves downloading the Git repository <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, running `npm install` for project dependencies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, and then `npm Dev` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The application can also be run using Docker <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Integrating DeepSeek Models via NV Studio and OpenRouter
This section details the process of [[using_deepseek_v3_and_r1_models_in_boltdiy | using DeepSeek V3 or R1 models]] within BoltDIY by leveraging NV Studio and OpenRouter, forming an [[integration_of_nv_studio_and_boltdiy | integration of NV Studio and BoltDIY]].

### Getting NV Studio API Keys and Credits
NV Studio is a model inference provider offering access to various large language models, including DeepSeek V3 and DeepSeek R1 <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It is considered one of the cheapest providers for free NV Studio model access <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

To obtain NV Studio API keys and credits:
1.  Go to NV Studio <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Navigate to the API key section to retrieve your NV Studio keys <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
3.  For free credits, go to `n.n.a` (presumably NV Studio's billing tab) and use the "text to image as code" option to receive $25 worth of credit <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. When signing up for NV Studio, you initially get $1 worth of credit, and applying a specific code can grant an additional $25 <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Configuring OpenRouter
OpenRouter acts as an intermediary to access DeepSeek models via NV Studio within BoltDIY <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

1.  Go to OpenRouter <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  Search for DeepSeek models, specifically DeepSeek V3, as R1 can be slower <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
3.  In OpenRouter, click on the NV Studio icon <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
4.  Paste your copied NV Studio API key into the configuration for NV Studio and save it <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Modifying BoltDIY Codebase
To enable BoltDIY to use NV Studio models via OpenRouter:
1.  Open your local BoltDIY project in a code editor like VS Code <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
2.  Navigate to `app` > `live` > `modules` > `LM` > `providers`, and open the `open.ts` file <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
3.  In this file, you can integrate NV Studio models <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
4.  Copy the model ID for DeepSeek V3 from OpenRouter <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
5.  Replace the existing model ID in `open.ts` with the DeepSeek V3 model ID <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
6.  Change the label of the model to something descriptive, like "NV Studio DeepSeek" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This name will appear in the BoltDIY interface <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### Setting OpenRouter API Keys in BoltDIY
1.  In your local BoltDIY interface, select "OpenRouter" as the provider <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Choose the DeepSeek model that was added from NV Studio <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  Go to OpenRouter settings, click on "keys," and create a new key <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
4.  This OpenRouter API key will be used in your BoltDIY setup <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Testing and Performance
Once configured, you can use BoltDIY to generate AI apps using DeepSeek V3. For example, generating a simple blog using Astro <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

You can monitor performance and cost on OpenRouter's activity page, which shows details like cost, timing, and speed of models used <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. NV Studio models are noted for being cheaper in the market <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

While DeepSeek V3 can be helpful for tasks like code fixing <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, models like Claude Sonnet 3.5 are considered better for generating apps from scratch <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Sometimes, using API keys from OpenRouter might result in slow responses <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.