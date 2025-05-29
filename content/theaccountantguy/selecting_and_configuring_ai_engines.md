---
title: Selecting and configuring AI engines
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to [[generating_ai_content_on_notion_pages_and_databases | create AI-generated content on your Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. To begin using Visen, initial settings need to be configured, particularly related to the AI engine <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accessing Settings <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>

The settings tab can be accessed by clicking the gear icon on the home screen or by selecting "settings" from the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Configuring AI Engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

Once in the settings tab, one of the crucial steps is the selection and configuration of the AI engine <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Available AI Engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
Visen offers a dropdown menu with different AI engines, including:
*   **Gemini** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   **GPT (OpenAI)** <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

### Defining API Keys <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
Based on the selected AI engine, you need to provide the corresponding API key:

*   **For Gemini:** Define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   To obtain a Gemini API key, navigate to `AI studio.google.com` and click on "get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. You can then create or copy an existing key <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **For GPT:** Define the OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
    *   To obtain an OpenAI API key, go to `platform.openai.com`, then to "API Keys," and click on "create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Cost Considerations <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Gemini** generally offers free access to its engines with some usage limitations <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **OpenAI** is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Notion Internal Integration Secret Key <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
Beyond the AI engine, you need to define the Notion internal integration secret key <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This key securely connects Visen with your local Notion workspace <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

#### Creating the Secret Key <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
1.  Click the icon next to the Notion internal integration secret field in Visen's settings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open Notion's profile integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click on "new integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Visen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select your Notion workspace <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Ensure the type is "internal" and click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "configure integration settings" to obtain and copy the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Paste this key into the Visen settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Connecting Notion Databases/Pages <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
After defining the integration secret, you must connect the specific Notion database or page to Visen.
1.  Go to the connections database (or the specific Notion page/database you want to use) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Click on the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down to "connections" (or "add connections") <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Search for and select the Visen internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This links your Notion resource to Visen <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   This connection step needs to be done once per Notion database or page <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Saving and Managing Settings <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
Once all settings are defined, click "Save" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. All entered settings are saved in the local storage of your web app <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. They are not stored on external cloud services, ensuring security and privacy <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. You can clear all saved settings by clicking the "clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Using AI Prompts <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
After setup, you can provide an AI prompt to [[writing_content_blocks_with_ai_for_specific_topics | generate content]] on Notion pages or databases <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. For example, to generate a 100-word blog on Notion, you might write "write me a Blog on Notion in 100 words" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

Users receive 10 free prompts to start, and usage is tracked <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Users can upgrade their plan from the "upgrade" tab if more prompts are needed <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.