---
title: Connecting Notion databases with API Keys for data management
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers inbuilt formulas for various calculations, but for more Excel-like functions, an external tool can be utilized <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This approach allows users to perform complex calculations like sum functions without delving into Notion's native formulas or [[establishing_links_and_relationships_between_databases_in_notion | relations and rollups]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Utilizing MyFormulaGen.com for Notion Data Management

The `myformulagen.com` tool enables the derivation of specific values from Notion databases using a simpler interface <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### [[setting_up_notion_api_keys_for_pdf_generation | Setting Up Notion API Keys]]

To connect Notion databases with `myformulagen.com`, an API key must be set up <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

1.  **Log in to MyFormulaGen.com**: Access the tool's interface <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Access Notion API Settings**: In `myformulagen.com`, navigate to `Settings` and click on `Get API key` <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
3.  **Create a New Integration in Notion**: A new screen will load in Notion where you can create a personal API key <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Click on `New Integration` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Give it a name (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   Click `Save` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
4.  **Copy the Internal Integration Secret**: Go back to `Integrations`, click on the newly created key, and reveal the `Internal Integration Secret` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Copy this entire API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
5.  **Paste API Key in MyFormulaGen.com**: Paste the copied API key into the `Notion API key` field in `myformulagen.com` and click `Save settings` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### [[connecting_notion_databases_with_apis | Connecting Notion Databases with APIs]]

For the API key to access your databases, ensure they are placed within a connected Notion page <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

1.  **Share the Notion Page with the Integration**: In Notion, click the three dots on the page containing your databases (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   Click on `Connections` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   Search for and select the API key you just created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   Click `Confirm` <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This connects the entire page and its contents, including [[creating_and_using_databases_in_notion | databases]], to the API key <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
2.  **Copy the Database Link**: Hover over the Notion database you want to use (e.g., a "Sales database"), click the six dots, and select `Copy link` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
3.  **Paste Database Link into MyFormulaGen.com**: Paste this link into the `Notion Database Link` field in `myformulagen.com`. This will enable the `Notion Property` field <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Performing Calculations (Sum Function Example)

Once connected, you can perform calculations on your Notion data.

*   **Select Function and Property**: Choose the `sum` function and the desired property (e.g., "Revenue") from your database <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Define Scope**: Specify whether to include "all rows," "odd rows," "even rows," "custom rows," or a "range" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Add Conditions/Filters**: Apply conditions based on other properties within your database (e.g., "Date is between" March 1st and March 31st, or "Category is" "Software") <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. You can use "AND" or "OR" conditions <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Calculate**: Click `Calculate` to see the derived value <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### [[connecting_notion_database_and_templates_to_pdf_output | Adding Calculated Values Back to Notion]]

After calculation, the results can be sent back to a Notion database.

1.  **Click `Add to Notion`**: This prompts you for the target database <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
2.  **Copy Target Database URL**: Copy the link of the Notion database where you want the calculated value to appear <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
3.  **Paste URL and Select Target**: Paste the link into `myformulagen.com`. The tool will automatically read the columns <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Select the specific column (e.g., "Amount") and row (e.g., "Total Sales Revenue") where you want the value inserted <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
4.  **Click `Save to Notion`**: The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Saving and Refreshing Formulas

*   **Save Formulas**: Save your created formulas with a descriptive name (e.g., "Total Sales Revenue") within `myformulagen.com` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Refresh Values**: If data in your source Notion database changes, click `Refresh all` in the `Saved formulas` section of `myformulagen.com` to update all linked values in Notion <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. You can also refresh individual formulas <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Benefits of this Approach

This method allows for dynamic data management without needing to understand complex Notion formulas or [[establishing_links_and_relationships_between_databases_in_notion | Notion relations and rollups]] <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It's a simple and dynamic solution for generating custom formulas with multiple operators and conditions <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

For queries, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.