---
title: Introduction to Wizzygen platform for AI generated content
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to [[ai_content_generation | create AI generated content]] on your Notion workspace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to define settings and then generate content <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Initial Setup and Settings

To begin [[using_wizzygen_to_generate_content_with_ai_prompts | using Wizzygen]], certain settings need to be defined in the settings tab <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The settings tab can be accessed by clicking the gear icon on the home screen or the settings option in the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### [[setting_up_the_wizzygen_connections_database_in_notion | Setting up the Connections Database]]

The first step in settings is defining the connections database, which stores all connections between Wizzygen and your Notion workspace <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
1.  Click on the icon in the settings tab to open a new template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Select your desired workspace and click "add to private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
3.  Once duplicated, copy the URL of the connections database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> and paste it into the connections database field in Wizzygen's settings <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### [[selection_of_ai_engines_and_api_key_configuration | AI Engine Selection and API Key Configuration]]

Next, select the AI engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Wizzygen supports Gemini and GPT (OpenAI) <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Gemini**: If selecting Gemini, define the Gemini API key. This can be obtained from `AI studio.google.com` by clicking "get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini offers free access to its engines with some usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **GPT (OpenAI)**: If selecting GPT, define the OpenAI API key <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This can be obtained from `platform.openai.com` under "API Keys" by clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The OpenAI key is a paid option <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Notion Internal Integration Secret Key

The Notion internal integration secret key securely connects your local Notion workspace to Wizzygen <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
1.  Click the icon in the settings tab to open profile integrations <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  Click "new integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
4.  Select your Notion workspace, ensure the type is "internal," and click "Save" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
5.  Click "configure integration settings" to obtain and copy the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
6.  Paste the copied key into the Notion internal integration secret key field in Wizzygen's settings <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This key is private and not shared publicly <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Saving Settings and Local Storage

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered settings are saved in the local storage of your system, ensuring privacy and security <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings from local storage at any time by clicking the "clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Connecting Notion to Wizzygen

Before [[using_wizzygen_to_generate_content_with_ai_prompts | creating content]], the Notion database must be connected to Wizzygen <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
1.  Go to the connections database (that you duplicated earlier in Notion) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Type "Wizzygen" (or the name you gave your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "confirm" to connect the Notion database to Wizzygen <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This connection is a one-time process <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## [[using_wizzygen_to_generate_content_with_ai_prompts | Creating AI Content]]

Wizzygen allows you to [[creating_and_managing_notion_pages_and_databases_with_wizzygen | create and manage content on Notion pages and databases]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### [[creating_and_managing_notion_pages_and_databases_with_wizzygen | Generating Content for a Notion Page]]

1.  Click the "create" button <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
2.  Provide a name for the connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select "Notion page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to get a sample blank page template <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Duplicate this page to your local Notion workspace <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
5.  Connect the duplicated Notion page to Wizzygen using the three dots -> connections -> select Wizzygen integration, similar to the connections database setup <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
6.  Copy the URL of the Notion page and paste it into Wizzygen, then click "next" <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
7.  Define your [[ai_content_generation | AI prompt]] (e.g., "write me a Blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
8.  Click "generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Wizzygen will then fill the Notion page with the generated content based on your prompt and chosen AI engine <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### [[creating_content_in_notion_databases | Generating Content in Notion Databases]]

1.  Click "create" again <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Provide a name (e.g., "Notion Database") and select "Notion database" <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Click the link to get a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template contains necessary settings for use <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
4.  Duplicate the template to your local Notion workspace and connect it to Wizzygen as previously described <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
5.  Copy the URL of the database and paste it into Wizzygen, then click "next" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
6.  In the database, define titles for which you want to create content (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Ensure the checkbox for each row is ticked to enable content generation for that row <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
7.  Define your [[ai_content_generation | AI prompt]] (e.g., "translate the topic to Japanese") <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
8.  Click "generate" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Wizzygen will automatically read each row's topic and generate content (e.g., translation) for it <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections and Usage

*   After generating content, the number of prompts used automatically updates <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Each new user receives 10 free prompts <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   The "connections" tab displays all created connections, showing their settings and the content generated <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   You can select any connection from this tab to resume work where you left off <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   Connections can be deleted from the connections tab by clicking the three dots and selecting "delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   All connections are also stored and manageable within the Notion connections database itself <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

Users can choose to upgrade their plan from the "upgrade" tab as they continue to use prompts <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Feedback can also be provided through the "feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.