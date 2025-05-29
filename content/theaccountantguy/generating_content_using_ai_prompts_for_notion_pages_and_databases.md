---
title: Generating content using AI prompts for Notion pages and databases
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

[[using_wizzygen_to_create_aigenerated_content_in_notion | Wizzygen]] is a platform designed to [[creating_aigenerated_content_in_notion | create AI-generated content]] directly within your [[ai_content_automation_in_notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It supports generating content for both [[using_notion_pages_for_ai_content | Notion pages]] and [[utilizing_notion_databases_for_ai_content | Notion databases]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Initial Setup for Wizzygen

Before [[creating_aigenerated_content_in_notion | generating content]], you need to configure a few settings in Wizzygen. You can access the settings tab by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### 1. Define Connection Database

The connection database stores all connections built between Wizzygen and your Notion workspace <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
To set it up:
1.  Click the icon next to "connection database" in the settings <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new template will open; duplicate it to your local Notion workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
3.  Select your desired workspace and click "add to private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
4.  Once duplicated, copy the URL of the connections database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste this URL into the "connections database" field in Wizzygen's settings <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### 2. Select AI Engine and API Keys

Wizzygen supports Gemini and GPT AI engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Gemini**: Offers free access with some usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   To get a Gemini API key, go to `AI studio.google.com` and click "get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Copy the generated key and paste it into the "Gemini API Key" field <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **GPT (OpenAI)**: This is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   To get an OpenAI API key, go to `platform.openai.com`, navigate to "API Keys," and click "create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the secret key and paste it into the "OpenAI API Key" field <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### 3. Define Notion Internal Integration Secret Key

This secret key securely connects Wizzygen with your local Notion workspace <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
To create it:
1.  Click the icon next to "notion internal integration secret key" in settings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  This opens Notion's "Integrations" page; click "New integration" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
3.  Give it a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select your workspace and ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "configure integration settings" to view and copy the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Paste this key into the corresponding field in Wizzygen settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   **Note**: This key is specific to your workspace and should not be shared <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### 4. Save Settings and Data Storage

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered settings are saved in your local storage, ensuring data privacy as it's not stored on an external cloud <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Notion to Wizzygen

Before [[creating_aigenerated_content_in_notion | generating content]], you must connect your Notion page or database to the Wizzygen integration you created.
1.  Go to the Notion page or database you want to connect <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Click the three dots `...` in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Type "Wizzygen" (or the name you gave your integration) and select it <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   This only needs to be done once per Notion page or database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Generating Content on Notion Pages

To [[using_notion_pages_for_ai_content | generate AI content on a Notion page]]:
1.  In Wizzygen, click "Create" <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Give the connection a name (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the link to open a sample blank page template <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Duplicate this page to your local Notion workspace, or use your own page <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
5.  Connect the duplicated page to Wizzygen (as described in the "Connecting Notion to Wizzygen" section above) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
6.  Copy the URL of your Notion page and paste it into the URL field in Wizzygen <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
7.  Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
8.  Enter your desired AI prompt (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
9.  Click "Generate." The AI will start [[creating_aigenerated_content_in_notion | filling the Notion page with content]] based on your prompt <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Generating Content on Notion Databases

To [[utilizing_notion_databases_for_ai_content | generate AI content on a Notion database]] for bulk creation:
1.  In Wizzygen, click "Create" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Give the connection a name (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the link to open a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template is important as it has required settings for bulk generation <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
5.  Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
6.  Connect the duplicated database to Wizzygen (as described in the "Connecting Notion to Wizzygen" section) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
7.  Copy the URL of your Notion database and paste it into the URL field in Wizzygen <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
9.  In Wizzygen, you will see fields corresponding to your database columns. Enter titles or topics for which you want to generate content in the appropriate rows (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   Ensure the checkbox next to each row is ticked to include it for generation <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
10. Enter your AI prompt (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
11. Click "Generate." Wizzygen will read each ticked row and generate content based on your prompt, [[using_notion_for_bulk_document_creation | filling each corresponding field in the Notion database]] <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Managing Connections and Usage

*   **View Connections**: In Wizzygen, navigate to the "Connections" tab to see all created connections <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Clicking on a connection will jump you to the create view, allowing you to resume work <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Delete Connections**: To delete a connection, go to the "Connections" tab, click the three dots `...` next to it, and select "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Connections Database in Notion**: The connections database you duplicated in Notion also lists all your created connections, allowing for sorting and deletion directly from Notion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Prompts**: New signed-in users receive 10 free prompts <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Your prompt usage updates automatically <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. You can upgrade your plan from the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Feedback**: You can provide feedback via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.