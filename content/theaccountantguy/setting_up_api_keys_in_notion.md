---
title: Setting up API keys in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Setting up API keys in Notion is crucial for integrating your Notion databases with external tools, allowing for advanced functionalities beyond Notion's native capabilities <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This process enables tools to connect to your Notion workspace and interact with your data <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Connecting to MyFormulaGen.com

This guide uses `myformula.com` as an example of an external tool that integrates with Notion via API keys <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Step 1: Generate an API Key in Notion

To create a personal API key for your Notion workspace:
1.  Navigate to `myformula.com` <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Click on "Settings" within the `myformula.com` interface <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  Click "Get API Key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This will open a new screen where you can create a personal API key <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
4.  Click "New Integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
5.  Provide a name for your integration (e.g., "sum formula key") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
6.  Select your Notion workspace (e.g., "the accountant guy workspace") <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
7.  Click "Save" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. A new key will be created <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
8.  Go back to the "Integrations" section in Notion <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
9.  Click on the newly created key <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
10. Locate the "internal integration secret" that appears <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
11. Click "Show" and then "Copy" to copy the entire API key <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Step 2: Input API Key into MyFormulaGen.com

1.  Return to `myformula.com`.
2.  Paste the copied API key into the "Notion API key" field <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
3.  Click "Save Settings" to store the API key within the tool <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a> <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Step 3: Connect Notion Page to the API Key

For the API key to access your databases, the Notion page containing them must be connected to the integration:
1.  Ensure all relevant databases are located within a single Notion page (e.g., a "sales dashboard page") <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
2.  On this Notion page, click the three dots (`...`) located in the top right corner <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a> <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  Select "Connections" from the dropdown menu <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  Search for the name you gave your API key (e.g., "sum") <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
5.  Select the API key from the results and click "Confirm" <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a> <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

This step connects the entire page, and by extension, all [[creating_databases_in_notion | databases]] and [[setting_up_a_database_in_notion | Notion databases]] within it, to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a> <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This simplifies the process as you won't need to connect each database individually <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a> <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

### Post-Setup

Once the API key is set up and connected, you can start using it to fetch data from your [[creating_a_database_in_notion | Notion databases]] and perform calculations or other operations using the external tool <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. For example, you can calculate the sum of values from a specific property in a Notion database <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a> <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This method offers an alternative to [[using_formulas_in_notion | Notion's inbuilt formulas]] and the relation/rollup features for deriving values <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.