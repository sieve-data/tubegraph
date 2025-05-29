---
title: BoltDIY setup and installation
videoId: zbPwWEoM0dc
---

From: [[amiteshanand]] <br/> 

BoltDIY is a self-hosted version of b.new, designed for local machine setup where users can integrate their own API keys to [[generating_ai_apps_using_boltdiy | generate AI applications]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Unlike b.new, which is a fully hosted service by Tech Le where users simply pay and sign in <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, BoltDIY provides the flexibility to run the application on your local device with a local setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Installation Steps

To install BoltDIY, you need to follow the steps provided in the BoltDIY repository <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

1.  **Download and Run**: You can perform a quick download using "Gip" and start running the application <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
2.  **Dependencies**: Install project dependencies using `npm install` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
3.  **Start Development Server**: Run the development server using `npm Dev` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
4.  **Docker (Optional)**: Docker can also be used to run BoltDIY <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Once installed, it will be running on your local device <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Initial Setup and API Key Configuration

Upon initial launch, BoltDIY might display errors, for example, if an LMS Studio provider is selected without API keys being set up <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. To use BoltDIY effectively, you need to set up the necessary [[api_keys_configuration_for_boltdiy | API keys]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Integrating Free DeepSeek Models with BoltDIY

This process involves using Open Router and NV Studio to access models like DeepSeek B3 or R1 within BoltDIY <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

1.  **Obtain NV Studio API Keys**:
    *   Go to NV Studio <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, which is described as one of the cheapest providers for free NV models <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   In the billing tab, use "text to image as code" to receive $25 worth of credit <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. You initially get $1 credit upon signing up, and an additional $25 when applying a specific code (e.g., from a Twitter post or voucher) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   Go to the API key section in NV Studio and obtain your NV API keys <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

2.  **Configure Open Router with NV Studio Keys**:
    *   Navigate to Open Router <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   In Open Router, find the NV configuration <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Click on the configuration icon and paste the copied NV Studio API key into Open Router, then save it <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

3.  **Modify BoltDIY Codebase**:
    *   Open your local BoltDIY project in a code editor like VS Code <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   Locate the file `app/live/modules/lm/providers/open.ts` <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Inside `open.ts`, you can find configurations for various Open Router models, including DeepSeek Coder and DeepSeek Flash <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   To use [[free_access_to_nv_models_in_boltdiy | NV Studio models]] (e.g., DeepSeek B3), copy the model ID (e.g., for `dcp3`) from NV Studio <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
    *   Replace an existing model ID in `open.ts` with the copied DeepSeek B3 model ID <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Change the corresponding `label` (name) for the model to "NVUS DeepSeek" (or similar) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This name will appear in the BoltDIY interface <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

4.  **Add Open Router API Keys in BoltDIY**:
    *   In the BoltDIY application, select "Open Router" as the provider <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Choose the configured NVUS DeepSeek model <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   Go to Open Router settings, create a new API key, and paste this key into the BoltDIY setup <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

With these steps complete, you can begin using DeepSeek models (like DeepSeek B3 or R1) within your local BoltDIY project <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Although DeepSeek B3 can generate simple apps <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>, Claude Sonnet 3.5 is considered superior for generating apps from scratch <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, while DeepSeek B3 might be more helpful for code fixing and answering questions about existing code <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Be aware that using API keys from Open Router might sometimes result in slow responses <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.