---
title: How to set up Wizzygen in Notion
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Wizzygen is a platform designed to create [[ai_content_generation_for_notion | AI-generated content]] directly within your [[creating_a_database_in_notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. To begin [[using_wizzygen_for_notion | using Wizzygen]], certain settings need to be configured in the settings tab <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accessing Settings

The settings tab can be accessed by clicking the gear icon on the home screen or by selecting "Settings" from the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Defining the Connections Database

The first setting to define is the "Connections Database" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This database holds all the connections built between Wizzygen and your [[creating_a_database_in_notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Steps to Set up the Connections Database

1.  Click the icon to the right of "Connection Database" in the settings tab <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This will open a new template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
2.  Duplicate this template onto your local [[creating_a_database_in_notion | Notion]] workspace by clicking "Duplicate" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  A pop-up will appear, allowing you to select your desired [[creating_a_database_in_notion | Notion]] workspace for duplication <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Click "Add to private" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
4.  Once duplicated, copy the URL of the connections database from your [[creating_a_database_in_notion | Notion]] workspace <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
5.  Paste this URL into the "Connections Database" field within the Wizzygen settings tab <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Selecting the AI Engine and API Key

The next step is to select your preferred [[ai_content_generation_for_notion | AI engine]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Wizzygen offers Gemini and GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

*   If you select Gemini, you need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. You can obtain this by heading to `AI studio.google.com` and clicking "Get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   If you select GPT, you need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This can be obtained from `platform.openai.com` by navigating to "API Keys" and clicking "Create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Note that Gemini offers free access with some usage limitations, while the OpenAI key is a paid option <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Setting up the Notion Internal Integration Secret Key

The [[notion_integration | Notion]] internal integration secret key connects your local [[creating_a_database_in_notion | Notion]] workspace with Wizzygen, offering a more secure connection than a public key <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Steps to Create and Use the Integration Key

1.  Click the icon next to "Notion Internal Integration Secret Key" in the settings tab <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open the profile integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Provide a name (e.g., "Wizzygen integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select the [[creating_a_database_in_notion | Notion]] workspace where you want to create this integration <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The type should be "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
6.  Click "Configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Copy this key and paste it into the "Notion Internal Integration Secret Key" field in Wizzygen settings <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
8.  After defining all settings in Wizzygen, navigate back to the Connections Database in [[creating_a_database_in_notion | Notion]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
9.  Click the three dots in the top right, scroll down, and select "Connections" <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
10. Type "Wizzygen" (or the name you gave your integration) and select the internal connection you just created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Click "Confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This connects your [[creating_a_database_in_notion | Notion]] template to Wizzygen <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Saving Settings

Once all settings are defined, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All settings are saved in local storage, meaning they are accessible only from your system and not on an external cloud <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can clear these settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## Creating Your First AI Connection

Wizzygen works with both [[creating_a_database_in_notion | Notion]] databases and [[creating_a_database_in_notion | Notion]] pages <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### Connecting a Notion Page

1.  Click "Create" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
2.  Provide a name for the connection (e.g., "Notion Page") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select "Notion page" from the dropdown <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Click the provided link to access a sample blank page <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Duplicate this page to your local workspace <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
5.  In the duplicated [[creating_a_database_in_notion | Notion]] page, click the three dots in the top right, go to "Connection," and connect it to the Wizzygen integration you created earlier <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This only needs to be done once <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
6.  Copy the URL of the [[creating_a_database_in_notion | Notion]] page and paste it into the Wizzygen connection setup <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Click "Next" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
7.  Define your [[ai_content_generation_for_notion | AI prompt]] (e.g., "Write me a blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
8.  Click "Generate" to see the content appear on your [[creating_a_database_in_notion | Notion]] page <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Connecting a Notion Database

1.  Click "Create" again <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  Provide a name (e.g., "Notion Database") and select "Notion database" from the dropdown <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Click the provided link to access a sample [[creating_and_setting_up_a_notion_database | Notion database template]] <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Duplicate this template to your local [[creating_a_database_in_notion | Notion]] workspace <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
4.  In the duplicated [[creating_a_database_in_notion | Notion]] database, click the three dots, go to "Connect," and link it to your Wizzygen integration <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
5.  Copy the URL of the database and paste it into the Wizzygen connection setup <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Click "Next" <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
6.  You can now define titles in your [[creating_a_database_in_notion | Notion]] database (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Ensure the checkbox for each row is ticked to enable content generation for that row <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
7.  Define your [[ai_content_generation_for_notion | AI prompt]] (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:09:59">[00:10:00]</a>.
8.  Click "Generate." Wizzygen will automatically read each row and generate content based on the prompt within the database <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Managing Connections

The "Connections" tab displays all created connections, allowing for sorting and filtering <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. You can select any connection to resume work from where you left off <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Connections can also be deleted by clicking the three dots next to a connection and selecting "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. The connections database in [[creating_a_database_in_notion | Notion]] also mirrors these connections, allowing for direct management within [[creating_a_database_in_notion | Notion]] <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Usage and Feedback

New users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Additional prompts can be obtained from the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Feedback can be provided via the "Feedback" tab <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.