---
title: Creating connections and integrations between Wizzygen and Notion
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to create AI-generated content directly within a [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To begin [[using_wizzygen_to_create_aigenerated_content_in_notion | using Wizzygen]], initial settings need to be configured <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## [[setting_up_the_wizzygen_application_and_configuring_settings | Setting Up Wizzygen]]

Configuration is done in the "Settings" tab, accessible via a gear icon on the home screen or the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Defining the [[creating_and_connecting_databases_in_notion | Connections Database]]

The first step is to define the "Connection Database," which stores all integrations built between Wizzygen and a [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

1.  Click the icon on the right side of the "Connection Database" setting <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new template will open, which needs to be duplicated to your local workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
3.  Click "Duplicate" and select your desired [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
4.  Once duplicated, copy the URL of the newly duplicated [[creating_and_connecting_databases_in_notion | Connections Database]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste this URL into the "Connections Database" field within Wizzygen's settings <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Selecting the AI Engine

Next, select the AI engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Wizzygen supports:

*   **Gemini:** Requires a Gemini API key. Gemini offers free access with some user limitations <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. API keys can be obtained from AI Studio (ai.google.com) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **GPT:** Requires an OpenAI API key. OpenAI is a paid service <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. API keys can be obtained from the OpenAI platform (platform.openai.com) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Defining the Notion Internal Integration Secret Key

This secret key establishes a secure connection between Wizzygen and your local [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is a private key not to be shared <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

1.  Click the icon next to the "Notion Internal Integration Secret Key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  This will open Notion's Integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
3.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Provide a name (e.g., "Wizzygen integration") and select the [[notion_workspace | Notion workspace]] you are using <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
5.  Ensure the type is "Internal" and click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "Configure integration settings" to obtain the secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Copy the key and paste it into the "Notion Internal Integration Secret Key" field in Wizzygen's settings <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

All settings entered are saved in local storage, not on an external cloud, ensuring data privacy <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. These settings can be cleared using the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## [[linking_databases_in_notion | Connecting Notion Databases]]

Before generating AI content, ensure your Notion pages or databases are connected to Wizzygen. This is done by granting access to the Wizzygen integration you created.

1.  Go to the [[creating_and_connecting_databases_in_notion | Connections Database]] (or any Notion page/database you want to connect) <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
3.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Search for and select the Wizzygen integration you created (e.g., "Wizzygen") and click "Confirm" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   This connection process only needs to be done once per Notion page or database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## [[using_wizzygen_to_create_aigenerated_content_in_notion | Creating AI-Generated Content]]

Wizzygen can generate AI content on both [[notion_database | Notion databases]] and Notion pages <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Creating AI Content on a Notion Page

1.  Click the "Create" tab in Wizzygen <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Provide a name for the connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to access a sample blank page template <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
5.  Duplicate this sample page to your local [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
6.  Connect this duplicated page to the Wizzygen integration in Notion (as described in [[linking_databases_in_notion | Connecting Notion Databases]]) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
7.  Copy the URL of the duplicated Notion page and paste it into the Wizzygen "Create" interface <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
9.  Define your AI prompt (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
10. Click "Generate" to have AI content populate the specified Notion page <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### [[using_wizzygen_to_create_aigenerated_content_in_notion | Creating AI Content on a Notion Database]]

1.  From the "Create" tab, provide a name (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
3.  Click the provided link to access a sample [[creating_a_database_in_notion | Notion database]] template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template contains necessary settings for use <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
4.  Duplicate this database template to your local [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
5.  Connect this duplicated database to the Wizzygen integration in Notion (as described in [[linking_databases_in_notion | Connecting Notion Databases]]) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
6.  Copy the URL of the duplicated [[notion_database | Notion database]] and paste it into the Wizzygen "Create" interface <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
7.  Click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
8.  In the Wizzygen interface, you'll see the database rows. Enter titles or topics into the designated columns (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   Ensure the checkbox next to each row is ticked for content generation <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
9.  Define your AI prompt (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
10. Click "Generate." Wizzygen will automatically read each row and generate content based on the prompt within the database <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Managing Connections

The "Connections" tab displays all created connections, allowing for sorting and filtering <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

*   Clicking on an existing connection will jump back to the "Create" view, allowing you to resume work <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   Connections can be deleted by clicking the three dots next to a connection and selecting "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   The [[creating_and_connecting_databases_in_notion | Connections Database]] in Notion also reflects and allows management of all created connections <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

New signed-in users receive 10 free prompts <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Users can upgrade their plan via the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> and provide feedback through the "Feedback" section <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.