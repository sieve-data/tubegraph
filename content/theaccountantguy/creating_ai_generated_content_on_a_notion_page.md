---
title: Creating AI generated content on a Notion page
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to [[ai_content_generation_for_notion | create AI generated content on your Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. To begin [[generating_ai_content_on_a_notion_database | generating content]], you first need to configure a few settings within Visen.

## Initial Setup and Settings

Access the settings tab by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Define Connection Database

The connections database stores all connections built between Visen and your Notion workspace <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
1.  Click the icon next to "Connection Database" to open a new template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  Duplicate this template onto your local Notion workspace by clicking "Duplicate" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  Select your desired workspace and click "Add to private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This will automatically duplicate the connections database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  Once duplicated, copy the URL of the connections database and paste it into the "Connections Database" field in Visen's settings <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Select AI Engine

Choose your preferred AI engine: Gemini or GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   If you select Gemini, you'll need to define your Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Gemini offers free access with user limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   If you select GPT, you'll need to define your OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The OpenAI key is a paid option <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   You can obtain API keys from `AI studio.google.com` (for Gemini) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> or `platform.openai.com` (for OpenAI) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Define Notion Internal Integration Secret Key

This key connects Visen to your local Notion workspace, offering a more secure connection than a public key <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
1.  Click the icon next to "Notion Internal Integration Secret Key" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  In Notion, click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Visen integration"), select your workspace, ensure the type is "Internal," and click "Save" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Click "Configure integration settings" to obtain the secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Copy this key and paste it into the corresponding field in Visen <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This key is secret and only connects your Notion workspace to Visen <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Save Settings and Connect Notion Database

Once all settings are defined, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered data is saved in local storage, not on an external cloud, ensuring security <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Finally, go back to the Notion connections database you duplicated. Click the three dots in the top right, select "Connections," type "Visen," and choose the integration you created, then click "Confirm" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This connects your Notion template to Visen <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[Creating Content on Notion Pages | Creating AI Content on a Notion Page]]

### Creating a Notion Page Connection
1.  Click "Create" in Visen <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  Provide a name for the connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to open a sample blank page template <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
5.  Duplicate this page to your local Notion workspace <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
6.  Once duplicated, click the three dots on the Notion page, go to "Connect," and select the Visen integration <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This connection is a one-time step <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
7.  Copy the URL of the duplicated Notion page and paste it into Visen's connection setup, then click "Next" <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Defining the AI Prompt and Generation
1.  On the next screen, define your AI prompt for the content <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. For example, to create a blog about Notion: "Write me a Blog on Notion in 100 words" <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
2.  Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The blank Notion page will automatically be filled with the AI-generated content based on your settings <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## Managing Connections and Usage

*   After generation, the number of prompts used automatically updates <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. New users receive 10 free prompts <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   You can view details of created connections in the "Connections" tab <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Clicking on a connection shows the page and generated content <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   From the "Connections" tab, you can select any particular connection to resume work <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   Connections can be deleted by clicking the three dots next to them in the "Connections" tab and selecting "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   The connections database in Notion itself also stores all created connections, allowing for sorting or deletion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   Users can upgrade their prompt limit from the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> and provide feedback via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.