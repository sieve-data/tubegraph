---
title: Setting up the Wizzygen application and configuring settings
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

[[wizzygen_overview_and_functionality | Wizzygen]] is a platform designed to create AI-generated content directly within your [[notion_workspace | Notion workspace]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. To begin using [[wizzygen_overview_and_functionality | Wizzygen]], essential initial settings must be configured within the application's "Settings" tab <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accessing the Settings Tab
The "Settings" tab can be accessed in two ways:
*   By clicking the gear icon on the home screen <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   By selecting "Settings" from the sidebar <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Configuring Essential Settings

Once in the "Settings" tab, several key configurations are required to establish [[creating_connections_and_integrations_between_wizzygen_and_notion | connections and integrations]] between [[wizzygen_overview_and_functionality | Wizzygen]] and [[notion_workspace | Notion]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### 1. Connection Database
The "Connections Database" defines where all the different [[creating_connections_and_integrations_between_wizzygen_and_notion | connections]] built between [[wizzygen_overview_and_functionality | Wizzygen]] and your [[notion_workspace | Notion workspace]] are held <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

To set up the Connection Database:
1.  Click the icon on the right side of the "Connection Database" field <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This will open a new Notion template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
2.  Duplicate this template to your local [[notion_workspace | Notion workspace]] by clicking "Duplicate" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
3.  Select your desired workspace in the pop-up and click "Add to private" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The database will automatically duplicate <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  Once duplicated, copy the URL of the Notion Connections Database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste the copied URL into the "Connections Database" field in the [[wizzygen_overview_and_functionality | Wizzygen]] settings <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### 2. Selection of AI Engine
[[wizzygen_overview_and_functionality | Wizzygen]] supports different AI engines, including Gemini and GPT <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

*   **Gemini**: If you select Gemini, you must define the Gemini API key <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   Access the Gemini API key by heading to `AI studio.google.com` and clicking "Get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Gemini offers free access to its engines with some usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **GPT (OpenAI)**: If you select GPT, you must define the OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
    *   Access the OpenAI API key by heading to `platform.openai.com`, navigating to "API Keys", and clicking "Create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   OpenAI API keys are paid <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

Paste your chosen API key into the "AI API Key" field in the [[wizzygen_overview_and_functionality | Wizzygen]] settings <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### 3. Notion Internal Integration Secret Key
This key securely connects your local [[notion_workspace | Notion workspace]] with [[wizzygen_overview_and_functionality | Wizzygen]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is more secure than using a public key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

To create the Notion Internal Integration Secret Key:
1.  Click the icon next to the "Notion Internal Integration Secret Key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open Notion's profile integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "[[wizzygen_overview_and_functionality | Wizzygen]] integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select the workspace you are using <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
7.  Click "Configure integration settings" to obtain the secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
8.  Copy this key and paste it into the "Notion Internal Integration Secret Key" field in [[wizzygen_overview_and_functionality | Wizzygen]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This key is specific to your local workspace and should not be shared <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Saving Settings and Local Storage
After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered information is saved in your local storage, meaning it's accessible only from the system you're using and is not stored on any external cloud <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear all defined settings from local storage by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Notion Templates to Wizzygen Integration

After setting up the internal integration secret, it's crucial to connect your Notion databases and pages to the [[wizzygen_overview_and_functionality | Wizzygen]] integration you created. This only needs to be done once per Notion database or page <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### For the Connections Database and Content Pages/Databases:
1.  Navigate to the duplicated Notion database (e.g., the Connections Database or a new page/database for AI content) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  Click the three dots in the top right corner of the Notion page/database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  Type "[[wizzygen_overview_and_functionality | Wizzygen]]" and select the internal [[wizzygen_overview_and_functionality | Wizzygen]] integration you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

Once these settings and connections are established, you are ready to begin [[using_wizzygen_to_create_aigenerated_content_in_notion | generating AI-generated content]] in your Notion workspace <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. New users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.