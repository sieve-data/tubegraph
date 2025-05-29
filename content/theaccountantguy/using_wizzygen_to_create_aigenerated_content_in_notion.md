---
title: Using Wizzygen to create AIgenerated content in Notion
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to [[creating_aigenerated_content_in_notion | create AI-generated content on your Notion workspace]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It allows users to [[generating_content_using_ai_prompts_for_notion_pages_and_databases | generate content using AI prompts for Notion pages and databases]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Getting Started with Wizzygen

To begin [[creating_aigenerated_content_in_notion | using Wizzygen]], certain settings must be defined in the settings tab <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The settings tab can be accessed by clicking the gear icon on the home screen or "Settings" on the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

Once in the settings tab, the following configurations are required:

### 1. Define Connections Database

The connections database holds all the different [[creating_connections_and_integrations_between_wizzygen_and_notion | connections]] built between Wizzygen and your Notion workspace <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

*   Click the icon next to "Connection Database" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   A new template will open, which needs to be duplicated to your local Notion workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Click "Duplicate" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Select your desired workspace from the pop-up and click "Add to Private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Once duplicated, copy the URL of this new [[creating_a_database_in_notion | connections database]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Paste the URL into the "Connections Database" field in Wizzygen's settings <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### 2. Select AI Engine

Wizzygen offers different AI engines, including Gemini and GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

*   **Gemini**: Requires a Gemini API key. Gemini offers free access to its engines with some usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. API keys can be obtained from `aistudio.google.com` by clicking "Get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **GPT**: Requires an OpenAI API key. This is a paid option <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. API keys can be obtained from `platform.openai.com` under "API Keys" by clicking "Create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Once you have the chosen API key, paste it into the corresponding field in Wizzygen settings <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### 3. Define Notion Internal Integration Secret Key

This secret key connects Wizzygen with your local Notion workspace, providing a more secure connection than a public key <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   Click the icon next to "Notion Internal Integration Secret Key" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   This will open the Notion profile integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   Add a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   Ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Click "Configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Copy the key and paste it into the "Notion Internal Integration Secret Key" field in Wizzygen <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is secret and applicable only to your own local workspace <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### 4. Save Settings

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All settings are saved in local storage, not on an external cloud, ensuring data security <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Wizzygen to Notion

Before [[generating_content_using_ai_prompts_for_notion_pages_and_databases | generating content]], you must connect your Notion connections database to the Wizzygen integration.

*   Go back to the Notion connections database you duplicated <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Type "Wizzygen" (or the name you gave your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Click "Confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This step connects your Notion template to Wizzygen and only needs to be done once <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Creating AI Content

Wizzygen can [[ai_content_automation_in_notion_workspace | generate AI content]] for both [[using_notion_pages_for_ai_content | Notion pages]] and [[utilizing_notion_databases_for_ai_content | Notion databases]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### For Notion Pages

1.  Click "Create" in Wizzygen <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  Enter a name for the connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the link to get a sample blank page template <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
5.  Duplicate this page to your local Notion workspace (similar to the connections database) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
6.  Connect this duplicated page to the Wizzygen integration (similar to the connections database) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
7.  Copy the URL of the duplicated Notion page and paste it into the Wizzygen "Create" section <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
9.  Define your [[generating_content_using_ai_prompts_for_notion_pages_and_databases | AI prompt]] (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
10. Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The Notion page will then be populated with AI-generated content based on your prompt <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### For Notion Databases

1.  Click "Create" again <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Enter a name (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the link to get a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template is important as it has required settings <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
5.  Duplicate this database template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
6.  Connect this duplicated database to the Wizzygen integration <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
7.  Copy the URL of the duplicated Notion database and paste it into the Wizzygen "Create" section <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
9.  In the database, define titles for each row you want to generate content for (e.g., "Learning is fun", "Notion is best tool", "Social media is a boon") <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Ensure the checkbox for each row is ticked to enable data addition <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
10. Define your [[generating_content_using_ai_prompts_for_notion_pages_and_databases | AI prompt]] (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
11. Click "Generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Wizzygen will automatically read each row's topic and generate content or translations for it <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

## Managing Connections

*   **View Connections**: All created [[creating_connections_and_integrations_between_wizzygen_and_notion | connections]] are displayed in the "Connections" tab, showing all defined settings <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can filter and sort connections from here <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Resume Work**: Select any connection from the "Connections" tab to jump back to the "Create" view and continue from where you left off <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Delete Connections**: Click the three dots next to a connection in the "Connections" tab and select "Delete" to remove it <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. The Notion connections database also stores all connections, allowing for sorting and deletion directly within Notion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Usage and Feedback

New signed-in users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Users can choose to upgrade via the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Feedback can be provided through the "Feedback" section <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.