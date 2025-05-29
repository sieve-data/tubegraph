---
title: Acquiring and using free credits for NV Studio
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

This article explains how to obtain and utilize free credits for NV Studio, an AI model inference provider, particularly for use with Bolt.DIY projects <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. NV Studio allows access to various large language models (LLMs) and offers a cost-effective way to experiment with AI applications <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## What is NV Studio?
[[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] (also referred to as "n Studio" or "nvus") acts as a model inference provider, offering access to multiple LLM models <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. Available models include DeepSeek P3, DeepSeek R1, Coho 2.5, Coho 53 mini, and Meta Llama models <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Users can also [[comparing_ai_models_using_nebius_ai_studio | compare models]] like DeepSeek P3 and DeepSeek R1 within the platform <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. It is highlighted as one of the cheapest providers for obtaining free model access <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

## Acquiring Free NV Studio Credits
To acquire free credits for [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]]:
1.  **Initial Signup Credit**: Upon signing up for [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]], you will receive $1 worth of credit <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
2.  **Additional Credit via Voucher**: Visit the `n.n.ai` website, navigate to the `building` tab, and use the "text-to-image as code" voucher <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. This provides an additional $25 worth of credit, bringing the total to $26 <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>, <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. This offer was found on their Twitter <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

### Increasing Rate Limits
For better rate limiting in [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]], users can request increased access limits based on their requirements <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## Using NV Studio Models in Bolt.DIY
To use [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] models like DeepSeek P3 or R1 within Bolt.DIY, follow these steps:

1.  **Obtain NV Studio API Keys**:
    *   Go to the API key section within [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] to retrieve your keys <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

2.  **Configure OpenRouter**:
    *   Access OpenRouter, which serves as a gateway to DeepSeek models in Bolt.DIY <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
    *   Search for "deep seek" and select a model like DeepSeek P3 (recommended over R1 for speed) <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
    *   In OpenRouter settings, locate the [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] icon and paste your copied [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] API key there <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>, <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
    *   Create a new API key in OpenRouter settings to be used in the Bolt.DIY setup <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

3.  **Modify Bolt.DIY Project Code**:
    *   Open your local Bolt.DIY project in VS Code <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
    *   Navigate to `app/live/modules/lm/providers/open.ts` <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
    *   In this `open.ts` file, you can utilize existing OpenRouter models or integrate [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] models for free credit usage <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
    *   Copy the model ID for your chosen DeepSeek model (e.g., DeepSeek P3) from [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
    *   Replace an existing model's ID in `open.ts` with the [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] model ID <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
    *   Change the model's `label` and `name` to reflect "nvus deep seek" (or a similar descriptive name) <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. This name will appear in Bolt.DIY <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

4.  **Run Bolt.DIY**:
    *   Start the Bolt.DIY application (e.g., using Docker) <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.
    *   In Bolt.DIY, select OpenRouter as the provider and choose the newly configured [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] model <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
    *   Enter the OpenRouter API key into Bolt.DIY <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

After these steps, you can use the [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] model via OpenRouter in your Bolt.DIY projects <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### Performance and Use Cases
*   OpenRouter activity shows the cost, timing, and speed of models <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] models are generally cheaper <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
*   Note that using API keys from OpenRouter might sometimes result in slow responses <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
*   While DeepSeek P3 can generate apps (e.g., a simple blog in Astro), Sonnet 3.5 by Cloud is noted as potentially better for generating apps from scratch <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.
*   DeepSeek P3 could be particularly helpful for code-fixing tasks or asking questions about existing code <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.

In summary, for [[integration_of_nv_studio_and_boltdiy | running DeepSeek P3 or R1 inside a Bolt.DIY project]], you only need an OpenRouter account, [[leveraging_nebas_ai_studio_for_open_source_model_access | NV Studio]] models, and to modify the `open.ts` file in your Bolt.DIY codebase <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.