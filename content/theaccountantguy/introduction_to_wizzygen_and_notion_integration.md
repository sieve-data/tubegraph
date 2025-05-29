---
title: Introduction to Wizzygen and Notion integration
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to create AI-generated content directly within your [[notion_application | Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It allows users to generate content for both [[notion_application | Notion]] pages and [[creating_and_setting_up_a_notion_database | Notion databases]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## [[how_to_set_up_wizzygen_in_notion | Setting Up Wizzygen]]

To begin [[using_wizzygen_for_notion | using Wizzygen]], a few initial settings must be defined in the settings tab <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The settings can be accessed by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Define the Connections Database

The connections database holds all the various connections built between Wizzygen and your [[notion_application | Notion workspace]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
To set this up:
1.  Click on the icon next to the "Connection Database" field <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new [[notion_template_and_database_integration | template]] will open, which needs to be duplicated to your local [[notion_application | Notion workspace]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Click "Duplicate" and select your preferred workspace <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
3.  Once duplicated, copy the URL of this [[creating_and_setting_up_a_notion_database | connections database]] from your browser's address bar <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
4.  Paste this URL into the "Connection Database" field in Wizzygen's settings <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Select AI Engine

Wizzygen supports different AI engines, including Gemini and GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   If Gemini is selected, you need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This can be obtained from `AI studio.google.com` by clicking "get API key" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Gemini offers free access with certain usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   If GPT is selected, you need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This can be obtained from `platform.openai.com` under "API Keys" by clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. OpenAI keys are part of a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Define Notion Internal Integration Secret

This key connects Wizzygen with your local [[notion_application | Notion workspace]] securely, as it is not a public key <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
To create this secret:
1.  Click on the icon next to the "Notion Internal Integration Secret Key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  This will open the profile integrations page in Notion <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
3.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Add a name (e.g., "Wizzygen integration") and select your [[notion_application | Notion workspace]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The type will be "internal" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Then, click "Configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Copy this key and paste it into the "Notion Internal Integration Secret Key" field in Wizzygen's settings <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Saving Settings

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered settings are saved in the local storage of your web app, ensuring privacy and security as they are not saved on an external cloud <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Connecting Notion to Wizzygen

After [[how_to_set_up_wizzygen_in_notion | setting up Wizzygen]], you need to ensure your Notion database or page is connected to the integration.
1.  Navigate to your connections database (or the Notion page/database you wish to integrate) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Search for and select the Wizzygen integration you created (e.g., "Wizzygen Integration") <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This step only needs to be done once per page/database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Generating AI Content

Wizzygen can generate AI content for both individual [[notion_application | Notion]] pages and [[creating_and_setting_up_a_notion_database | Notion databases]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

To create a new connection for content generation:
1.  Click on "Create" in Wizzygen <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Provide a name for the connection <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select either "Notion Database" or "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
4.  Click the provided link to duplicate a sample blank page or database [[notion_template_and_database_integration | template]] to your [[notion_application | Notion workspace]], or use your own <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a> <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
5.  Copy the URL of your chosen Notion page or database and paste it into Wizzygen <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a> <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
6.  Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Generating Content on a Notion Page

For a Notion page, you can define a specific AI prompt. For example, to create a blog:
*   Enter a prompt like "Write me a blog on Notion in 100 words" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   Click "Generate," and the [[notion_application | Notion]] page will be filled with AI-generated content based on your prompt and chosen AI engine <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Generating Content on a Notion Database

For a [[creating_and_setting_up_a_notion_database | Notion database]], you can define multiple titles (rows) for which you want to create content <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   Ensure the checkbox next to each row is ticked to enable content generation for that specific row <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   Define your AI prompt, such as "Translate the topic to Japanese" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Click "Generate," and Wizzygen will automatically read each row and provide the requested content (e.g., translation) for each <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   Users can generate blogs or any other type of content for [[notion_application | Notion]] pages and [[creating_and_setting_up_a_notion_database | Notion databases]] <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Managing Connections

The "Connections" tab displays all the different connections you have created <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   You can sort and filter connections from here <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Clicking on a specific connection automatically jumps you to the "Create" view, allowing you to resume your work <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
*   To delete a connection, go to the "Connections" tab, click the three dots next to the connection, and select "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   All connections are also stored in the [[creating_and_setting_up_a_notion_database | connections database]] within your [[notion_application | Notion workspace]], where you can manage them as well <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Usage and Feedback

New signed-in users receive 10 free prompts to start [[using_wizzygen_for_notion | using Wizzygen]] <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Users can choose to upgrade their plan from the "Upgrade" tab as they use more prompts <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Feedback can be submitted via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.