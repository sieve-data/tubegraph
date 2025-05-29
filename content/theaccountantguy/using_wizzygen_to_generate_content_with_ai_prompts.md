---
title: Using Wizzygen to generate content with AI prompts
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

[[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] is a platform designed to create [[ai_content_generation | AI-generated content]] directly within your Notion workspace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It supports content creation on both Notion pages and Notion databases <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Initial Setup for Content Generation

Before generating content, several settings need to be configured in the Wizzygen platform:

### Accessing Settings
The settings tab can be accessed by clicking the gear icon on the home screen or the "Settings" option on the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Defining the [[setting_up_the_wizzygen_connections_database_in_notion | Connections Database]]
The connections database stores all connections built between Wizzygen and your Notion workspace <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
1.  Click the icon next to "Connection database" in the settings tab <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new template will open, which you need to duplicate to your local Notion workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
3.  Click "Duplicate" and select your desired Notion workspace, then "Add to private" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
4.  Once duplicated, copy the URL of the Notion connections database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste this URL into the connections database field in Wizzygen's settings <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### [[selection_of_ai_engines_and_api_key_configuration | Selection of AI Engines and API Key Configuration]]
Wizzygen supports Gemini and GPT [[using_gpt_models_with_the_chatbot | models]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Gemini**: If selected, define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. You can obtain this from [AI Studio Google](https://aistudio.google.com) by clicking "Get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini offers free access with user limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **GPT (OpenAI)**: If selected, define the [[generating_an_openai_api_key | OpenAI API key]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Obtain this from [platform.openai.com](https://platform.openai.com) by navigating to "API Keys" and clicking "Create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The [[generating_an_openai_api_key | OpenAI API key]] is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Defining the Notion Internal Integration Secret Key
This key securely connects your local Notion workspace to Wizzygen <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
1.  Click the icon next to "Notion internal integration secret key" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Wizzygen integration"), select your workspace, ensure the type is "Internal," and click "Save" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Click "Configure integration settings" to obtain and copy the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Paste this key into the Notion internal integration secret key field in Wizzygen settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is secret and only connects your own Notion workspace to Wizzygen <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

> [!INFO] Local Storage
> All entered settings are saved in the local storage of your web app, ensuring privacy and security as they are not stored on external clouds <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Connecting Notion Workspace to Wizzygen
After defining all settings, ensure your Notion database/page is connected to the Wizzygen integration:
1.  Go to the Notion page or database you want to use.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Type "Wizzygen" and select the integration you created, then click "Confirm" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This step is only required once per Notion page or database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## [[creating_and_managing_notion_pages_and_databases_with_wizzygen | Creating Content in Notion Pages]]

1.  Click the "Create" tab in Wizzygen <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
2.  Enter a name for your connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to access a sample blank page template, then duplicate it to your Notion workspace <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
5.  Connect this duplicated Notion page to the Wizzygen integration (as described above) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
6.  Copy the URL of your Notion page and paste it into the Wizzygen input field, then click "Next" <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
7.  Provide your [[ai_content_generation | AI prompt]] in the text box (e.g., "Write me a Blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
8.  Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The [[ai_content_generation | AI-generated content]] will appear directly on your Notion page <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## [[creating_and_managing_notion_pages_and_databases_with_wizzygen | Creating Content in Notion Databases]]

1.  Click the "Create" tab in Wizzygen <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
2.  Enter a name for your connection (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
3.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the provided link to access a sample Notion database template, which includes necessary settings for use <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
5.  Connect this duplicated Notion database to the Wizzygen integration (as described above) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
6.  Copy the URL of your Notion database and paste it into the Wizzygen input field, then click "Next" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
7.  In the Wizzygen interface, define titles for the content you want to generate in your database (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Ensure the checkbox next to each row is ticked to include it in content generation <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
8.  Provide your [[ai_content_generation | AI prompt]] (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
9.  Click "Generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Wizzygen will automatically read each row's title and generate the requested content/translation within that row in the Notion database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections and Usage

*   **Viewing Connections**: All created connections are displayed in the "Connections" tab, showing their settings and allowing sorting/filtering <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Clicking on a connection will jump back to the "Create" view, allowing you to resume work <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Deleting Connections**: Connections can be deleted by clicking the three dots next to a connection in the "Connections" tab and selecting "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Connections Database in Notion**: The Notion database linked as the connections database also stores all connections created, allowing for sorting or deletion directly from Notion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Prompt Usage**: Every new signed-in user receives 10 free prompts to start <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. You can choose to upgrade from the "Upgrade" tab as you use more prompts <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Feedback**: Users can provide feedback via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.