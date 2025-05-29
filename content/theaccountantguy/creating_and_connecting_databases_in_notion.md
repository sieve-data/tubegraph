---
title: Creating and Connecting Databases in Notion
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF output is a tool that allows users to generate PDF documents in bulk by combining a Google Document template with data from a [[creating_a_database_in_notion | Notion database]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process involves [[setting_up_a_database_in_notion | setting up a database in Notion]] and [[connecting_notion_databases_and_templates | connecting Notion databases and templates]].

## Overview of the Process
To generate documents, you need to log into PDF output.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The main steps involve:
1.  Adding a Google Document as a template <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  [[setting_up_a_database_in_notion | Setting up a database in Notion]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
3.  [[connecting_notion_databases_and_templates | Connecting Notion databases and templates]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
4.  Exporting PDFs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Preparing the Google Document Template
A Google Document serves as the template for the PDF output <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. You can either create a blank document from scratch or choose an existing document from Google Drive <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
For example, an "invitation template" Google Document can be used, with specific fields like "customer name" marked for replacement <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Placeholders like `salutation` and `customer name` are typed directly into the Google Doc where the dynamic data should appear <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## [[creating_a_database_in_notion | Creating a Database in Notion]]
To [[creating_a_database_in_notion | create a database in Notion]] for use with PDF output:
1.  Open your Notion account on a separate tab <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
2.  Click on `New Page` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
3.  Select `Table` as the type of database <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
4.  Rename the database (e.g., "invitation list") <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
5.  Add necessary columns (properties) to your Notion database, such as "salutation" and "customer name" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
6.  Populate the database with your data, for example, customer names and their corresponding salutations <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## [[connecting_notion_databases_and_templates | Connecting Notion Databases and Templates]]
After [[creating_a_database_in_notion | creating a database in Notion]], the next step is to connect it to the PDF output tool:
1.  In the PDF output interface, click on the `Add Notion Database` button <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Authenticate with your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Select the specific pages (databases) from your Notion account workspace that you wish to connect <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
4.  Once selected, click `Allow Access` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
5.  The connected Notion database (e.g., "invitation list") will show its default "Name" property <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
6.  If you add more columns to your Notion database after initial connection, click the `Refresh Properties` button in the PDF output tool to fetch the new properties <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### Mapping Data from Notion to Google Docs
Once the database is connected and properties are refreshed:
1.  Click on any property name in the PDF output interface (e.g., `salutation` or `customer name`) to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  In the Google Document template, select the placeholder text you want to replace (e.g., `salutation` or `customer name`) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  Paste the copied property value into the selected placeholder <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## [[linking_databases_in_notion | Linking Databases in Notion]]
If your Notion database has columns connected to other databases (i.e., [[linking_databases_in_notion | linked databases]]), ensure you select **all** connected databases when approving the database list in PDF output <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Then, add the main database and proceed to copy and paste values as usual <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Generating PDFs
With the Google Document template prepared and the Notion database connected and mapped:
1.  Click on `Export PDF` in the PDF output tool <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  Complete any required Google authentication <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
3.  The tool will read each row in the Notion database and generate a separate PDF document for each entry <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

The generated PDFs will reflect the data from each row of your Notion database within the Google Document template <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.