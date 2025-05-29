---
title: Connecting relational databases with Notion API
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details how to leverage the Notion API to generate documents from Notion templates using data from Notion databases, specifically highlighting the connection of relational databases. The process involves using a third-party tool like pdf4put.com to facilitate bulk PDF generation from a Notion invoice template and its associated database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Preparing Your Notion Template and Database

To begin, ensure your Notion template is set up to receive dynamic data:
*   Create a professional invoice template within a Notion page <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
*   Place placeholders for information that will be dynamically replaced from the database within curly brackets, e.g., `{client name}`, `{client company}`, `{client address}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. These placeholders must correspond to the column names in your Notion database <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Ensure the Notion page containing the template is public and accessible by clicking "Share" then "Publish" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   Copy the URL of the published Notion template page <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Setting Up the Notion API Key

The API key acts as a bridge between your Notion databases and the document generation tool.
1.  Navigate to the integration settings (e.g., via a provided link in pdf4put.com) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
2.  Click "New integration," provide a name (e.g., "new key"), and select your Notion account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Save the integration to generate the API key <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  Copy the generated API key <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## [[connecting_notion_databases_with_templates | Connecting Notion Databases]]

To link your database to the API key for data retrieval:
1.  Go to the Notion database you intend to use for document generation <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  Click the three dots at the top right of the database view, then select "Connections" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  Search for the API key you created (e.g., "new key") and confirm the connection <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This step is crucial for the API to access your database <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
4.  Copy the URL of the Notion database <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Integrating with the Document Generation Tool (pdf4put.com)

Once the template and database are prepared and linked to the API, you can use the tool:
1.  Paste the copied Notion template page URL into the designated field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  Paste the Notion API key into its respective field <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  Paste the Notion database URL into its field <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
4.  Click "Load database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
5.  Select a column from your database (e.g., "Invoice Number") to name the generated PDF files <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
6.  Choose to generate documents for specific rows or all rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
7.  Click "Generate PDF" to begin the process <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The tool will populate the template with data from each record in your database, replacing the curly bracket placeholders <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
8.  Adjust layout settings like paper size or orientation if needed <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
9.  Save the generated PDF documents <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## [[establishing_relationships_between_databases_in_notion | Connecting Relational Databases]] with the API

A critical point for more complex Notion setups: if your primary database uses "relation properties" to link to other databases, **all related databases must also be connected to the same Notion API key** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This ensures seamless data fetching across all linked Notion databases for accurate document generation <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Reminders for Successful Generation

*   Ensure your Notion page is shared and publicly accessible <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   Confirm the database is connected to the API key you've added <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   For [[establishing_relationships_between_databases_in_notion | relational databases]], all linked databases must also be connected to the same API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

For any queries or assistance, you can reach out via email to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a> or use the contact window on the pdf4put.com website <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.