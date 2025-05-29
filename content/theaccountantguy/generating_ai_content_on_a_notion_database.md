---
title: Generating AI content on a Notion database
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to [[ai_content_generation_for_notion | create AI generated content on your Notion workspace]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to generate content directly within their [[creating_content_on_notion_pages | Notion pages]] or [[generating_content_in_notion_databases | Notion databases]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Initial Setup for Visen

Before [[generating_content_in_notion_databases | generating content in Notion databases]], a few initial settings need to be configured in Visen's settings tab <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These settings can be accessed by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Define Connection Database

The first step is to define the "connections database" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This database holds all connections between Visen and your Notion workspace <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
1.  Click the icon on the right side of the "connections database" setting <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new template will open, which you need to duplicate to your local Notion workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Click "duplicate" and select your workspace <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
3.  Once duplicated, copy the URL of this new connections database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
4.  Paste the URL into the "connections database" field in Visen's settings tab <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Select AI Engine and API Key

Next, select your preferred AI engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Visen supports Gemini and GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   If selecting Gemini, define your Gemini API key <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. You can get this from `AI studio.google.com` by clicking "get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini offers free access with certain usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   If selecting GPT, define your OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Obtain this from `platform.openai.com` under API Keys by clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. OpenAI's key is a paid one <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Create Notion Internal Integration Secret Key

This key connects Visen to your local Notion workspace securely <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
1.  Click the icon next to the "notion internal integration secret key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This opens Notion's profile integrations <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click "new integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Visen integration"), select your workspace, ensure the type is "internal," and click "Save" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Click "configure integration settings" to obtain the internal secret key. Copy this key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Paste the key into the corresponding field in Visen's settings <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

> [!NOTE] Security
> This key is secret and only connects your own Notion workspace to Visen; it should not be shared publicly <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. All settings entered are saved in local storage, not on an external cloud, ensuring data privacy <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Connect Visen to your Notion Database

After defining all settings in Visen, you must connect your specific Notion database to the Visen integration.
1.  Open the Notion database you wish to use <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "Add connections" (or similar wording) <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Search for and select the Visen integration you created (e.g., "Visen integration") <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This links your Notion database to Visen <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This step is a one-time process for each database you connect <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## [[generating_ai_content_on_a_notion_database | Generating AI Content on a Notion Database]]

With the initial setup complete, you can begin [[generating_content_in_notion_databases | generating content in Notion databases]].
1.  In Visen, click "create" <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Provide a name for your connection (e.g., "Notion database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the provided link to open a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Duplicate this template to your Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
5.  After duplication, ensure this new database is connected to your Visen integration by following the "Connect Visen to your Notion Database" steps above <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
6.  Copy the URL of the duplicated Notion database and paste it into the field in Visen <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Click "next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
7.  In the Notion database, define titles or topics in separate rows for which you want to [[generating_content_in_notion_databases | generate content]] <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. For example, "learning is fun," "notion is best tool," "social media is a boon" <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
8.  Ensure the checkbox for each row is ticked if you want content generated for that row <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
9.  In Visen, define your AI prompt based on what you want the AI to do for each topic. For instance, "translate the topic to Japanese" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
10. Click "generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Visen will automatically read each row's topic and [[demonstration_of_aipowered_content_creation | generate]] the requested content in the corresponding row of your Notion database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections and Usage

*   The "connections" tab in Visen shows all created connections <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. You can click on a connection to jump back to its "create" view and continue working from where you left off <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   Connections can be deleted from the "connections" tab by clicking the three dots and selecting "delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   The connections database in Notion also displays all created connections, allowing for sorting, filtering, or deletion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   New users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, with options to upgrade for more usage <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.