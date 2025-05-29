---
title: Setting up Wizzygen platform in Notion
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to create AI-generated content directly within your [[notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To begin using Wizzygen, you need to configure a few settings in the platform's settings tab <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accessing Settings <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>

You can access the settings tab by clicking the gear icon on the home screen or by selecting "Settings" from the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Defining Connections Database <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>

The "Connections Database" setting is crucial as it stores all the connections built between Wizzygen and your [[notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Steps to Define the Connections Database:

1.  Click the icon on the right side of the "Connections Database" field in Wizzygen settings <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This will open a new [[creating_templates_and_databases_in_notion | Notion template]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
2.  Duplicate this template to your local [[notion | Notion]] workspace by clicking "Duplicate" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  Select your desired workspace in the popup and click "Add to private" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The connections database will be automatically duplicated to your [[notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  Once duplicated, copy the URL of the connections database from your [[notion | Notion]] page <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste this URL into the "Connections Database" field in Wizzygen's settings tab <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Selecting the AI Engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

Wizzygen supports both Gemini and GPT (OpenAI) as AI engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Steps to Define the AI Engine:

1.  From the dropdown, select either Gemini or GPT <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  **For Gemini**: You need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Obtain this by heading to `AI studio.google.com`, clicking "Get API key", and copying your key <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Paste it into the "AI API Key" field <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  **For GPT (OpenAI)**: You need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Go to `platform.openai.com`, navigate to "API Keys", and click "Create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Copy the generated key and paste it <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   **Note**: Gemini offers free access with some usage limitations, while OpenAI is a paid service <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Defining Notion Internal Integration Secret Key <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>

This secret key securely connects your local [[notion | Notion]] workspace with Wizzygen <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. It's more secure than using a public key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Steps to Create and Use the Notion Internal Integration Secret Key:

1.  In Wizzygen settings, click the icon next to the "Notion Internal Integration Secret Key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open [[notion | Notion]]'s "Profile Integrations" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select your [[notion | Notion]] workspace <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
7.  Click "Configure integration settings" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
8.  Copy the key <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> and paste it into the "Notion Internal Integration Secret Key" field in Wizzygen <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is unique to your workspace and should not be shared <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Saving Settings <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All settings are saved in your local storage, not on an external cloud, ensuring security <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Notion Databases/Pages to Wizzygen <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>

Before creating AI content, the specific Notion page or database you intend to use must be connected to the Wizzygen integration.

### Steps to Connect:

1.  In your [[notion | Notion]] connections database (or any new page/database you create), click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
3.  Type "Wizzygen" (or the name of your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
4.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This connects your Notion page/database to Wizzygen <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This step needs to be done once per Notion page or database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Creating Your First Connection (Notion Page) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

Wizzygen supports [[ai_content_generation_for_notion | AI content generation]] for both Notion databases and Notion pages <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Steps to Create a Notion Page Connection:

1.  In Wizzygen, click "Create" <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Enter a name for your connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to open a sample blank page template <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
5.  Duplicate this page to your local workspace <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
6.  Connect this duplicated page to your Wizzygen integration within Notion (as described above) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
7.  Copy the URL of your Notion page and paste it into the URL field in Wizzygen <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, then click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
8.  Define your AI prompt (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
9.  Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The AI-generated content will appear directly on your selected Notion page <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Creating a Notion Database Connection <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>

### Steps to Create a Notion Database Connection:

1.  In Wizzygen, click "Create" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Enter a name (e.g., "Notion Database") <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
4.  Click the provided link to open a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template contains necessary settings for your use case <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
5.  Duplicate this template to your local Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
6.  Connect this duplicated database to your Wizzygen integration within Notion (as described previously) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
7.  Copy the URL of your Notion database and paste it into the URL field in Wizzygen <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, then click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
8.  In the Wizzygen interface, you will see the database rows. Enter titles or topics for which you want to generate content in the database (e.g., "Learning is fun", "Notion is best tool", "Social media is a boon") <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Ensure the checkbox next to each row is ticked to enable content generation for that row <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
9.  Define your AI prompt (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
10. Click "Generate" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Wizzygen will automatically read each row and generate content based on your prompt, populating the database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>

The "Connections" tab in Wizzygen displays all created connections, allowing you to view their settings or resume work from where you left off <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Connections can also be deleted from this tab by clicking the three dots next to a connection and selecting "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. All connections are also stored in the connections database created in [[notion | Notion]] <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Usage and Feedback <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>

New signed-in users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. You can choose to upgrade your plan from the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. There is also a "Feedback" tab where you can send messages to the developer <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.