---
title: Selection of AI engines and API key configuration
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

To begin [[introduction_to_wizzygen_platform_for_ai_generated_content | using Wizzygen]], essential settings must be defined in the settings tab, which can be accessed by clicking the gear icon on the home screen or "settings" on the sidebar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Defining the Connections Database

The first setting to define is the connection database, which holds all connections built between [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] and the Notion workspace <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. To define it:
1.  Click the icon on the right in the settings tab <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This opens a new template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
2.  Duplicate the template to your local Notion workspace by clicking "duplicate" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  Select the desired workspace and click "add to private" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This will automatically duplicate the connections database to your Notion workspace <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  Once duplicated, copy the URL of the connections database from the top of the Notion page and paste it into the connections database field in the [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] settings tab <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Selecting the AI Engine and Defining API Keys

After defining the connections database, the next step is to select the AI engine <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Available AI Engines
[[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] offers different AI engines, including Gemini and GPT <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   If Gemini is selected, a Gemini API key is required <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   If GPT is selected, an [[generating_an_openai_api_key | OpenAI API key]] is required <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Obtaining API Keys
*   **Gemini API Key**: Head to `AI studio.google.com` and click "get API key" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Create or copy an existing API key and paste it into the "AI API key" field in [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **[[generating_an_openai_api_key | OpenAI API Key]]**: Go to `platform.openai.com`, navigate to "API Keys," and click "create new secret API key" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Define settings as prompted to generate the secret key <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Cost Considerations
*   Gemini offers free access to its engines with some usage limitations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   The [[generating_an_openai_api_key | OpenAI key]] is a paid service <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For testing, Gemini can be chosen as a free option <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Defining the Notion Internal Integration Secret Key

The Notion internal integration secret key is crucial for connecting your local Notion workspace with [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] securely, as it is more secure than using a public key <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
1.  In [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] settings, click the icon next to the Notion internal integration secret field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This opens the profile integrations page <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
2.  Click "new integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Add a name for the integration (e.g., "[[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] integration") <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Select the workspace where you want to create this integration <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Ensure the type is "internal" and click "Save" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  Click "configure integration settings" to obtain the internal secret key <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  Show and copy the key <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
8.  Return to [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] and paste the key into the Notion internal integration secret key field <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

This key is secret and applicable only to your local workspace, not shared publicly, enhancing security and accessibility <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Saving Settings

Once all settings are defined, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered information is saved in the local storage, meaning it's used by the [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] web app and not stored on any external cloud, ensuring complete safety and security <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. You can also clear these settings by clicking the "clear" button <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Connecting Notion Workspace to Wizzygen Integration

Before creating AI integrations, go back to the connections database created earlier in Notion <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
1.  Click the three dots in the top right corner of the Notion connections database page <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  Scroll down and select "connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
3.  Type "[[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]]" and select the internal connection created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
4.  Click "confirm" to connect the Notion template to [[introduction_to_wizzygen_platform_for_ai_generated_content | Wizzygen]] via the internal integration secret key <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This connection only needs to be done once <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.