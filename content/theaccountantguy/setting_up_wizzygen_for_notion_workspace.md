---
title: Setting up Wizzygen for Notion workspace
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 
Wizzygen is a platform designed to create AI-generated content directly within your [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To begin using Wizzygen, you must first complete a few essential setup steps in its settings tab <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Accessing Settings
You can access the settings tab by clicking the gear icon on the home screen or by selecting "Settings" on the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Defining the Connections Database
The first crucial setting is defining the "Connection Database" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This database will store all the different connections you build between Wizzygen and your [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

To set up the connections database:
1.  Click the icon on the right side of the "Connection Database" setting <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
2.  A new template will open, which you need to duplicate to your local [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
3.  Click "Duplicate" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
4.  A pop-up will appear, allowing you to select the specific [[overview_of_notion_tools | Notion]] workspace where you want to duplicate the template <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
5.  Select your workspace and click "Add to private" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This will automatically duplicate the connections database to your [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
6.  Once duplicated, copy the URL of the connections database from your [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
7.  Paste this URL into the "Connections Database" field within Wizzygen's settings <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Selecting the AI Engine
The next step involves selecting your preferred AI engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Wizzygen offers both Gemini and GPT engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

*   If you choose Gemini, you'll need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This can be obtained from [AI Studio (ai.google.com)](https://ai.google.com) by clicking "Get API key" and creating a new one <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini generally offers free access with certain usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   If you select GPT, you'll need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This can be accessed from [Platform OpenAI (platform.openai.com)](https://platform.openai.com) by navigating to "API Keys" and clicking "Create new secret API key" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. OpenAI's API key is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

Once you have your API key, paste it into the designated "AI API key" field in Wizzygen settings <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Defining the Notion Internal Integration Secret Key
This key is crucial as it securely connects Wizzygen to your local [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is a more secure method than using a public key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

To create the Notion internal integration secret key:
1.  Click the icon next to the "Notion Internal Integration Secret Key" field <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This will open the "Integrations" section of your [[overview_of_notion_tools | Notion]] profile <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name for your integration, such as "Wizzygen integration" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select the [[overview_of_notion_tools | Notion]] workspace you are using <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
5.  Ensure the type is "Internal" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
7.  Click "Configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
8.  Show and copy this key <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
9.  Paste the key into the "Notion Internal Integration Secret Key" field in Wizzygen <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is specific to your local workspace and should not be shared publicly <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Saving Settings
After defining all necessary settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All settings are saved in your browser's local storage, meaning they are not stored on an external cloud, ensuring your data remains secure on your system <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. You can clear these settings at any time by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Connecting Notion Templates to Wizzygen
A crucial final step is to connect your duplicated [[overview_of_notion_tools | Notion]] templates (like the Connections Database, or any [[setting_up_and_sharing_a_notion_page_for_public_use | Notion page]] or [[setting_up_a_database_in_notion | Notion database]] you plan to use with Wizzygen) to the internal integration you just created <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

To do this:
1.  Go to the duplicated [[overview_of_notion_tools | Notion]] database or page.
2.  Click the three dots `...` in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Scroll down and find the "Connections" option <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
4.  Type "Wizzygen" (or the name you gave your integration) and select the internal connection you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This links your [[overview_of_notion_tools | Notion]] template to Wizzygen via the internal integration secret key <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This linking process generally only needs to be done once per template <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

Once these steps are complete, you are ready to [[steps_for_using_wizzygen_with_notion | create AI-generated content]] using Wizzygen in your [[overview_of_notion_tools | Notion]] workspace <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Every new user receives 10 free prompts to start with <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.