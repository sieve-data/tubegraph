---
title: Using DeepSeek V3 and R1 models
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

This article details how to utilize DeepSeek V3 and R1 models within the [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] environment, including setup, integration, and observed performance.

## Introduction to Bolt.DIY <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>
[[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] is a self-hosted version of B.new, enabling users to generate AI applications using their own API keys and local setup <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Unlike B.new, which is a fully hosted service, Bolt.DIY requires local installation, typically involving `npm install` and `npm dev` commands <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Accessing DeepSeek Models
DeepSeek V3 and R1 models can be accessed for free or at a low cost primarily through [[API integration with nvs AI Studio for model usage | NV AI Studio]] and [[Open Deep Researcher and its opensource version | Open Router]].

### NV AI Studio
[[API integration with nvs AI Studio for model usage | NV AI Studio]] is a model inference provider that offers access to DeepSeek V3 and DeepSeek R1 models, alongside other LLMs like Cohere 2.5, Qwen 53 Mini, and Meta Llama models <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Cost-Effective Access
[[API integration with nvs AI Studio for model usage | NV AI Studio]] is considered one of the cheapest providers for accessing these models <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
Users can obtain free credits:
*   Initially, signing up for [[API integration with nvs AI Studio for model usage | NV AI Studio]] grants $1 worth of credit <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   An additional $25 worth of credit can be acquired by visiting the billing tab on `n.n.a` and using the "text to image as code" voucher, which was advertised on their Twitter <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Users can also request increased rate limits in [[API integration with nvs AI Studio for model usage | NV AI Studio]] based on their requirements <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Using Open Router
[[Open Deep Researcher and its opensource version | Open Router]] acts as an intermediary to facilitate the use of DeepSeek models within [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. To integrate:
1.  Obtain API keys from [[API integration with nvs AI Studio for model usage | NV AI Studio]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
2.  In [[Open Deep Researcher and its opensource version | Open Router]], configure [[API integration with nvs AI Studio for model usage | NV AI Studio]] as a provider and paste the [[API integration with nvs AI Studio for model usage | NV AI Studio]] API key <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
3.  Create a new API key within the [[Open Deep Researcher and its opensource version | Open Router]] settings for use in [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Integration with Bolt.DIY
To run DeepSeek models in a local [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] project:
1.  Navigate to the `app/lib/modules/llm/providers` directory in your local [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] codebase <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
2.  Open the `open.ts` file <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
3.  Modify the model ID for the desired DeepSeek model (e.g., DeepSeek V3) to match the ID from [[API integration with nvs AI Studio for model usage | NV AI Studio]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
4.  Change the model's label within the `open.ts` file (e.g., to "NVus DeepSeek") for easy identification in the [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] interface <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
5.  In the [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] interface, select "Open Router" as the provider and then choose the configured [[API integration with nvs AI Studio for model usage | NV AI Studio]] model (e.g., "NVus DeepSeek") <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
6.  Input the [[Open Deep Researcher and its opensource version | Open Router]] API key into the [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] setup <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Performance and Use Cases
*   DeepSeek V3 was chosen over R1 for testing due to its perceived faster response and thinking capabilities <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   When prompted to "build a simple blog using Astro," DeepSeek V3 in [[free_access_to_nv_models_in_boltdiy | Bolt.DIY]] generated a basic app from a template <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   While DeepSeek V3 can be helpful, Claude's Sonnet 3.5 was observed to be superior for generating applications from scratch <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   DeepSeek V3 may be more effective for tasks like code fixing or answering questions related to existing code <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   A potential issue noted is that using API keys from [[Open Deep Researcher and its opensource version | Open Router]] can sometimes result in slow responses <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   [[Open Deep Researcher and its opensource version | Open Router]] allows users to monitor the activity, costs, and speed of their DeepSeek model usage <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.