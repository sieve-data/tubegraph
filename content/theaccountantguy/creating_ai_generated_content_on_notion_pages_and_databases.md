---
title: Creating AI generated content on Notion pages and databases
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to [[integrating_aigenerated_content_into_notion | create AI-generated content]] directly on your [[creating_content_on_notion_pages | Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It supports generating content on both Notion databases and Notion pages <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Getting Started: Setting Up Visen

To begin using Visen, you need to configure a few settings in the "settings" tab <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This tab can be accessed by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### 1. Define the Connections Database

The "Connections Database" is where Visen stores all the connections you build between Visen and your Notion workspace <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

*   Click the icon next to "Connection Database" in the settings <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   This will open a new template page that you need to duplicate to your local Notion workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Click "Duplicate" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, select your desired workspace, and click "Add to Private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Once duplicated, copy the URL of this new "Connections database" and paste it into the "Connections Database" field in Visen's settings <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### 2. Select an AI Engine

Visen supports both Gemini and GPT AI engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

*   Choose your preferred AI engine from the dropdown <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   If you select Gemini, you need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. You can get this from `aistudio.google.com` by clicking "get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini offers free access with usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   If you select GPT, you need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This can be obtained from `platform.openai.com` under "API Keys" by clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The OpenAI key is a paid option <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### 3. Define the Notion Internal Integration Secret Key

This secret key connects Visen to your local Notion workspace, providing a more secure connection than a public key <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

*   Click the icon next to "Notion Internal Integration Secret Key" in the settings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open Notion's Integrations page.
*   Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   Provide a name (e.g., "Visen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, select your workspace, ensure the type is "Internal", and click "Save" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   Click "Configure integration settings" to reveal and copy your internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Paste this key into the "Notion Internal Integration Secret Key" field in Visen's settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Data Storage

All settings entered in Visen are saved in your local storage, meaning they are not stored on an external cloud <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Finalizing Settings

After defining all the required settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Connecting Notion to Visen

Before generating content, you need to connect your Notion database or page to the Visen integration you created.

*   Go to the Notion page or database you want to connect <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Type "Visen" (or the name of your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Click "Confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This step only needs to be done once per page/database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Generating AI Content on Notion Pages

Visen allows you to [[creating_content_on_notion_pages | create AI-generated content directly on Notion pages]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

1.  In Visen, click "Create" <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Provide a name for your connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to get a sample blank page template <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Duplicate this page to your local workspace, or create your own Notion page <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
5.  Connect this Notion page to your Visen integration in Notion (as described above) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
6.  Copy the URL of your Notion page and paste it into Visen's field <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, then click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
7.  Enter your AI prompt (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
8.  Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The AI-generated content will appear directly on your Notion page <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Generating AI Content on Notion Databases

Visen also allows you to [[populating_notion_databases_with_aigenerated_content | populate Notion databases with AI-generated content]] for multiple entries <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

1.  In Visen, click "Create" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Provide a name (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the provided link to get a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This template is important as it contains necessary settings <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
5.  Connect this Notion database to your Visen integration in Notion <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
6.  Copy the URL of your Notion database and paste it into Visen's field <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, then click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
7.  In the Visen interface, you can now define titles for each row in your Notion database (e.g., "Learning is fun", "Notion is best tool", "Social media is a boon") <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Ensure the checkbox next to each row is ticked for content to be generated <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
8.  Enter your AI prompt (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
9.  Click "Generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Visen will automatically generate content for each checked row in your Notion database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections

*   **Viewing Connections**: All created connections are listed in the "Connections" tab in Visen <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. They are also stored in the Notion "Connections database" you set up earlier <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Resuming Work**: You can select any connection from the "Connections" tab to resume your work from where you left off <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Deleting Connections**: To delete a connection, go to the "Connections" tab, click the three dots next to the connection, and select "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Usage and Feedback

*   **Free Prompts**: Every new signed-in user receives 10 free prompts to start <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Upgrading**: You can choose to upgrade from the "Upgrade" tab as you use more prompts <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Feedback**: You can provide feedback via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.