---
title: Setting up API keys for Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Setting up API keys for Notion allows external tools, such as `myformulagen.com`, to interact with your Notion databases and perform calculations that go beyond Notion's in-built formulas <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This process enables advanced functionalities like using Excel-like formulas (e.g., SUM) on your Notion data <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Why Use API Keys?

While Notion has built-in formulas for calculations <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, integrating with an API key via a tool like `myformulagen.com` allows for more complex operations, such as performing a sum function across a database without relying on Notion's native relation and rollup features <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This provides a dynamic way to derive values directly into your Notion databases <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Prerequisites

Before setting up your API key, ensure your Notion databases are organized within a single parent page. This simplifies the connection process, as you'll only need to connect the parent page to the API key, and all databases within that page will automatically be accessible <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

For example, a "Sales Dashboard" page could contain multiple [[setting_up_a_database_in_notion | Notion databases]] like "Sales Database," "DB_Sales_Revenue_Total," and "DB_Sales_Revenue_March_2025" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Generating a Notion API Key

To generate a personal API key for your Notion workspace:

1.  Log in to the external tool (e.g., `myformulagen.com`) <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Navigate to the settings section of the tool <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  Click "Get API Key" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This will typically open a new screen where you can [[setting_up_notion_api_keys_for_pdf_document_creation | create your own personal API key]] <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
4.  Click "New integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
5.  Give your integration a name, such as "Sum Formula Key" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
6.  Select your Notion workspace <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
7.  Click "Save" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
8.  Go back to the "Integrations" section <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
9.  Click on the newly created key <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
10. Locate the "Internal Integration Secret" and click "Show" to reveal the API key <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
11. Copy the entire API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Connecting Notion to `myformulagen.com`

Once you have your API key:

1.  Paste the copied API key into the "Notion API key" field within `myformulagen.com` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  Click "Save Settings" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This action stores the API key in the tool <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Connecting Notion Databases to the API Key

To allow the external tool to access your Notion data:

1.  In Notion, navigate to the parent page containing your databases (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
2.  Click the three dots `...` next to the page title <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  Select "Connections" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  Search for the name of the API key you created (e.g., "sum formula key") and select it <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

This connection makes the entire page, including all [[connecting_notion_databases_via_api | Notion databases]] within it, accessible to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The tool can then use the API key to retrieve information, such as total sales revenue <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

> [!NOTE]
> When using an external tool like `myformulagen.com`, you don't need to manually connect each individual Notion database to the API key if they are nested within a parent page that has already been connected <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>, <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This simplifies the [[integrating_notion_with_an_api_key_for_database_access | integration process]] significantly.