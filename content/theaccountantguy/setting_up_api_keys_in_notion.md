---
title: Setting up API keys in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Setting up API keys in Notion is crucial for [[connecting_notion_databases_with_external_tools_using_API_keys | connecting Notion databases with external tools]], such as `myformulagen.com`, to perform advanced calculations like sum functions that go beyond Notion's in-built formulas <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This process allows external tools to derive values from your Notion databases <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Why Use API Keys?

While Notion has [[creating_and_saving_formulas_in_notion | inbuilt formulas]] for many calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, using external tools with API keys enables Excel-like functions, such as the sum function, for more complex data manipulation <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This method avoids the complexities of Notion's native relation and rollup features for data aggregation across databases <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## [[configuring_api_keys_for_notion_integration | Configuring API keys for Notion integration]]

To connect Notion to an external tool like `myformulagen.com`, you first need to [[setting_up_accounts_in_notion | set up]] an API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Steps to Create an API Key

1.  **Access Settings:** Navigate to the settings within the external tool you are using (e.g., `myformulagen.com`) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
2.  **Get API Key:** Click on the "Get API key" option <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This will open a new screen where you can create a personal API key <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
3.  **Create New Integration:** Select "New integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
4.  **Name the Integration:** Give your new integration a descriptive name, such as "Sum Formula Key" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
5.  **Select Workspace:** Choose the Notion workspace you wish to connect <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
6.  **Save:** Click "Save" to create the key <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
7.  **Copy the Secret:**
    *   Go to "Integrations" to see the newly created key <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Click on the key to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Click "Show" to display the full API key <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Copy the entire API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
8.  **Paste into Tool:** Paste the copied API key into the "Notion API key" field within your external tool's settings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
9.  **Save Tool Settings:** Click "Save settings" in the external tool to store the API key <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Connecting Notion Databases

Once the API key is [[utilizing_api_keys_to_connect_notion_to_pdf_generation_tools | set up in the external tool]], you need to connect your Notion databases to it.

### Granting Access to Pages/Databases

*   Ensure all relevant Notion databases are contained within a single parent page <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This simplifies the connection process, as you only need to connect the parent page to the API key, rather than each database individually <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   In Notion, hover over the parent page (e.g., "Sales Dashboard") and click the three dots (`...`) that appear <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   Select "Connections" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   Search for and select the API key you previously created (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

This action connects the entire page, and all databases within it, to your API key, allowing the external tool to access them <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a> <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Providing Database URLs to the External Tool

To perform calculations on a specific database, you need to provide its URL to the external tool.

*   In Notion, hover over the database you wish to use (e.g., "Sales Database") and click the six dots (`⋮⋮`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Click "Copy link" <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   Paste this link into the designated "Database URL" field within your external tool <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The tool should then recognize the Notion properties (columns) within that database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

This setup enables the external tool to process data from your Notion databases according to the formulas and conditions you define <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.