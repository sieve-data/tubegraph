---
title: Generating AI content on Notion pages and databases
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to [[ai_content_generation_for_notion | generate AI content on your Notion workspace]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It allows users to create AI-generated content directly within their Notion pages and databases <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Initial Setup and Configuration

Before generating content, several settings need to be defined in Visen's settings tab <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This tab can be accessed via the gear icon on the home screen or the "settings" link in the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### 1. Define Connections Database

The "connections database" holds all connections built between Visen and your Notion workspace <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

*   **Duplicate Template:** Click the icon next to the "Connections database" field <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This opens a new template that needs to be duplicated to your local Notion workspace <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Select Workspace:** Click "Duplicate," then select your desired Notion workspace from the pop-up and click "Add to private" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This will automatically duplicate the connections database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Copy URL:** Once duplicated, copy the URL of the Notion connections database from the top of the Notion page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Paste URL:** Paste this URL into the "Connections database" field in Visen's settings tab <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. [[using_urls_to_link_notion_resources_with_ai_tools | Using URLs to link Notion resources with AI tools]] is a key step here.

### 2. Select AI Engine and Provide API Key

Visen supports Gemini and GPT as AI engines <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

*   **Selection:** Choose your preferred AI engine from the dropdown <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **API Keys:**
    *   **Gemini:** If selecting Gemini, you'll need to define the Gemini API key <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Obtain this from AI Studio.google.com by clicking "Get API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Gemini offers free access with certain usage limitations <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   **GPT (OpenAI):** If selecting GPT, you'll need to define the OpenAI API key <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Obtain this from platform.openai.com under "API Keys" by clicking "create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. OpenAI API keys are paid <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Paste Key:** Paste the copied API key into the corresponding field in Visen <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### 3. Define Notion Internal Integration Secret Key

This secret key connects Visen to your local Notion workspace securely <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

*   **Generate Key:** Click the icon next to "Notion internal integration secret key" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This will open Notion's Integrations page <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Create New Integration:** Click "New integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Provide a name (e.g., "Visen integration"), select your Notion workspace, ensure the type is "Internal," and click "Save" <a class="yt>timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Copy Secret Key:** Click "configure integration settings" for the newly created integration. Reveal and copy the internal integration secret key <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Paste Key:** Paste this key into the designated field in Visen's settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This key is private and specific to your workspace <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### 4. Save Settings

After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. All entered information is saved in your local storage, ensuring privacy and security, and can be cleared using the "Clear" button <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### 5. Connect Notion Database to Visen

Before generating content, the Notion connections database itself needs to be connected to the Visen integration.

*   **Share Database:** In your Notion workspace, navigate to the duplicated connections database. Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Add Connection:** Scroll down to "Connections," search for the Visen integration you created (e.g., "Visen"), select it, and click "Confirm" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This links the database to Visen via the internal integration secret key <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Generating AI Content on Notion Pages

Visen allows [[creating_content_on_notion_pages_vs_notion_databases | AI content generation on Notion pages and databases]] <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

1.  **Start Connection:** In Visen, click "Create" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  **Name & Type:** Provide a name for the connection (e.g., "Notion Page") and select "Notion Page" from the dropdown <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  **Duplicate Page:** Click the provided link to open a sample blank page. Duplicate this page to your local Notion workspace <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
4.  **Share Page:** In Notion, navigate to the duplicated page. Click the three dots at the top right, go to "Connection," and connect it to your Visen integration <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This is a one-time setup for each page <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
5.  **Copy & Paste URL:** Copy the URL of your Notion page and paste it into the URL field in Visen, then click "Next" <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
6.  **Define AI Prompt:** Provide the AI prompt for the content you want to generate (e.g., "Write me a Blog on Notion in 100 words") <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
7.  **Generate:** Click "Generate" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The blank Notion page will then be filled with the AI-generated content <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Your prompt count will update automatically <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Generating AI Content on Notion Databases

Visen also enables [[creating_a_database_in_notion | AI content generation within Notion databases]].

1.  **Start Connection:** In Visen, click "Create" again <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  **Name & Type:** Name the connection (e.g., "Notion Database") and select "Notion Database" from the dropdown <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  **Duplicate Database Template:** Click the provided link to open a sample Notion database template <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This template contains necessary settings for use with Visen <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Duplicate this template to your Notion workspace <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This is part of [[using_notion_for_templates_and_databases | using Notion for templates and databases]].
4.  **Share Database:** In Notion, navigate to the duplicated database. Click the three dots at the top right, go to "Connect," and connect it to your Visen integration <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
5.  **Copy & Paste URL:** Copy the URL of your Notion database and paste it into the URL field in Visen, then click "Next" <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
6.  **Define Titles/Topics:** In the Visen interface, you'll see a table where you can define titles or topics for each row in your Notion database (e.g., "Learning is fun," "Notion is best tool," "Social media is a boon") <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Ensure the checkbox for each row is ticked to enable content generation <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
7.  **Define AI Prompt:** Provide an AI prompt that applies to each row (e.g., "Translate the topic to Japanese") <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
8.  **Generate:** Click "Generate" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Visen will automatically read each row's topic and generate content (e.g., translation) for it in the Notion database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Managing Connections

*   **View Connections:** The "Connections" tab in Visen displays all created connections, showing their settings and linking directly to the associated Notion page or database <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Resume Work:** You can select any existing connection from the "Connections" tab to jump back to the "Create" view and continue from where you left off <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Delete Connection:** To delete a connection, go to the "Connections" tab, click the three dots next to the connection, and select "Delete" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Notion Connections Database:** The "Connections database" you duplicated in Notion also stores all created connections, allowing for sorting, filtering, or deletion directly within Notion <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This showcases how [[linking_databases_and_creating_templates_in_notion | linking databases and creating templates in Notion]] is central to Visen's functionality.

## Usage and Feedback

New signed-in users receive 10 free prompts to start <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Users can upgrade their plan from the "Upgrade" tab <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. There is also a feedback section to send messages and requests <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.