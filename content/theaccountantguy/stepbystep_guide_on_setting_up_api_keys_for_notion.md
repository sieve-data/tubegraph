---
title: Stepbystep guide on setting up API keys for Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This guide outlines the process of setting up API keys to connect a Notion [[creating_and_setting_up_a_notion_database | database]] with an external tool, such as MyFormulaGen, for advanced calculations and data manipulation.

## Initial Setup with MyFormulaGen

To begin, navigate to MyFormulaGen.com, log in, and create an account if you haven't already <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The first step involves fetching the URL of the Notion [[creating_and_setting_up_a_notion_database | database]] you wish to use for calculations <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Obtaining the Notion Database URL

1.  If your [[creating_and_setting_up_a_notion_database | database]] is an inline [[creating_and_setting_up_a_notion_database | database]], click on the six dots next to the database title <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
2.  Select "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  Paste this URL into the designated field in MyFormulaGen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Setting Up the API Key

The API key is confidential and exclusively for your use <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

1.  In MyFormulaGen, click on `Settings` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Click on `Get API key` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This will redirect you to Notion's API page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  On the Notion API page, click `+ New integration` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
4.  Define a name for your integration (e.g., "My API Key") <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
5.  Select the workspace you are currently using (e.g., "accountant guy workspace") <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
6.  Click `Save` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. An API key will be created <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
7.  Click on the newly created API key <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
8.  Locate "Internal Integration Secret" and click `Show` to reveal the full API key <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
9.  Copy this value <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
10. Paste the copied API key into the designated field in MyFormulaGen settings <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
11. Click `Save changes` <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Connecting Notion Page to the API Key

Once the API key is set up in MyFormulaGen, you need to connect your Notion page (containing the [[creating_and_setting_up_a_notion_database | database]]) to this API key <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

1.  Go back to the Notion page where your [[creating_and_setting_up_a_notion_database | database]] is located <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
2.  Click on the three dots in the top right corner of the Notion page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  Select `Connections` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  Search for the name of the API key you created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
5.  Click on the API key name <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
6.  Click `Confirm` <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Your Notion page and the [[creating_and_setting_up_a_notion_database | database]] within it are now connected to the API key, allowing external tools to interact with your data <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This connection is essential for proceeding with custom formulas and data manipulation <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.