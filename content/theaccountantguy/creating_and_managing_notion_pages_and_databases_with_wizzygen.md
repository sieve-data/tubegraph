---
title: Creating and managing Notion pages and databases with Wizzygen
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to create AI-generated content directly within your [[Notion workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. To begin using Wizzygen, you must complete a few initial settings, after which you can click "create" to start content generation <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Initial Setup in Wizzygen

Access the settings tab by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Defining the Connection Database

The first step in settings is to define the "connection database" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This database stores all connections between Wizzygen and your Notion workspace <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

To define it:
1.  Click the icon on the right within the settings tab <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  A new template will open, which you need to duplicate to your local Notion workspace <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
3.  Click "Duplicate" <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
4.  A pop-up will appear, allowing you to select the specific Notion workspace for duplication <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
5.  Select your workspace and click "Add to private" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This automatically duplicates the connections database <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, which is essential for [[setting_up_the_wizzygen_connections_database_in_notion | setting up the Wizzygen connections database in Notion]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
6.  Once duplicated, copy the URL of this new connections database <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
7.  Paste this URL into the connections database field in Wizzygen's settings tab <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Selecting the AI Engine

After defining the connections database, select your preferred AI engine <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Wizzygen offers Gemini and GPT <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   If selecting Gemini, define the Gemini API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> by heading to `AI studio.google.com` and clicking "get API key" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   If selecting GPT, define the OpenAI API key <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> by visiting `platform.openai.com`, navigating to "API Keys", and clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Note**: Gemini offers free access with some usage limitations, while OpenAI is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Defining the Notion Internal Integration Secret Key

The Notion internal integration secret key is crucial for securely connecting your local Notion workspace with Wizzygen <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

To create it:
1.  In Wizzygen settings, click the icon next to the Notion internal integration secret field <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This opens Notion's integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
3.  Add a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
4.  Select your workspace <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
5.  Ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
7.  Click "Configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
8.  Copy this key and paste it into the Notion internal integration secret key field in Wizzygen <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is private and should not be shared <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Saving Settings

Once all settings are defined, click "Save" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. All settings are stored in your local storage, not on an external cloud, ensuring data safety <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. You can clear these settings at any time by clicking the "clear" button <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

## Connecting Notion Elements to Wizzygen

Before creating AI content, you need to connect your Notion pages or databases to the Wizzygen integration.

### Connecting the Connections Database

1.  Go to the connections database you duplicated earlier in Notion <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  Scroll down and find the "Connections" option <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
4.  Type "Wizzygen" (or the name you gave your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This connects your Notion template to Wizzygen via the internal integration secret key <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## Creating AI Content

Wizzygen allows you to create AI content on both Notion pages and Notion databases <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### [[Creating Content on Notion Pages | Creating Content on Notion Pages]]

1.  In Wizzygen, click "Create" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  Provide a name for the connection (e.g., "Notion page") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select "Notion page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the link to get a sample blank page <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. You can also create your own page <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
5.  Duplicate this page to your local Notion workspace (similar to the connections database) <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
6.  Once duplicated, go to the page in Notion, click the three dots, go to "Connections", and connect it to your Wizzygen integration <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This is a one-time process for each page/database <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
7.  Copy the URL of the duplicated Notion page and paste it into the link field in Wizzygen <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
9.  Define your AI prompt (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
10. Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The AI-generated content will fill the Notion page <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

*   Each user receives 10 free prompts to start <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Your prompt count updates automatically <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### [[Creating Content in Notion Databases | Creating Content in Notion Databases]]

Wizzygen can also create content within a [[creating_a_database_in_notion | Notion database]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This is part of [[creating_and_managing_databases_in_notion | creating and managing databases in Notion]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> and [[creating_databases_in_notion | creating databases in Notion]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

1.  Click "Create" again <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Provide a name (e.g., "Notion database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion database" from the dropdown <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
4.  Click the link to access a sample Notion database template provided with Wizzygen <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. This template contains necessary settings for use <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This is part of [[setting_up_a_database_in_notion | setting up a database in Notion]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a> and [[setting_up_and_managing_notion_databases_for_pdf_generation | setting up and managing Notion databases for PDF generation]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
5.  Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
6.  Once duplicated, go to the database in Notion, click the three dots, go to "Connect", and connect it to your Wizzygen integration <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
7.  Copy the URL of the Notion database and paste it into the link field in Wizzygen <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
9.  In the Wizzygen interface, you can define different titles that correspond to rows in your Notion database (e.g., "Learning is fun", "Notion is best tool", "Social media is a boon") <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
10. Ensure the checkbox next to each row is ticked to enable content generation for that row <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
11. Define an AI prompt (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
12. Click "Generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Wizzygen will automatically read each row and generate content for it based on the prompt <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

## Managing Connections

### Connections Tab

The "Connections" tab in Wizzygen displays all the different connections you have created, allowing for sorting and filtering <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   You can select any connection to jump back to its create view and continue working from where you left off <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   To delete a connection, go to the connections tab, click the three dots next to it, and select "Delete" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### Notion Connections Database

The initial connections database you set up also lists all your created connections in Notion <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. This allows for further sorting or deletion within Notion <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>, enabling [[creating_and_linking_notion_databases | creating and linking Notion databases]] <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

## Additional Features

*   **Prompts**: Newly signed-in users receive 10 free prompts <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Additional prompts can be obtained by upgrading via the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Feedback**: Users can send feedback messages via the "Feedback" tab <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.