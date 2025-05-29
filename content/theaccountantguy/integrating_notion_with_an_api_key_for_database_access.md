---
title: Integrating Notion with an API key for database access
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

Integrating Notion with an API key allows for dynamic document generation from a Notion database using a template. This process is particularly useful for creating multiple, personalized documents, such as invoices, in bulk.

## Overview of the Process <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>
The core idea is to use a Notion page as a template, where specific fields are marked with curly brackets (e.g., `{client name}`). These marked fields will be populated with data from a Notion database. A third-party tool, like pdf4put.com, can then use a Notion API key to connect the template page and the database, generating individual PDF documents for each record in the database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

For this demonstration, a professional invoice template in Notion is used, with three database records containing different invoice-related information <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The goal is to generate a PDF document for each of these records <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Steps for Integration and Document Generation

### 1. Preparing the Notion Template Page
The Notion page serving as the template needs to be made public so it can be accessed by the generation tool <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   In Notion, open your template page.
*   Click "Share" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Click "Publish" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Confirm "Publish" again to make the page public <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   Copy the public link to the page <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

> [!INFO] Template Fields
> Ensure that all dynamic information in your Notion template (e.g., client name, invoice number, address) is enclosed in curly brackets (e.g., `{client name}`, `{invoice number}`). These bracketed fields must correspond to column names in your Notion database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### 2. [[setting_up_api_keys_for_notion | Setting Up a Notion API Key]]
An API key is essential for connecting the Notion database with the document generation tool <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Navigate to Notion's integrations page (e.g., via a link provided by the tool) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   Click "New integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Provide a name for your integration (e.g., "new key") <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Choose the associated Notion account and click "Save" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Locate the newly created integration under "Integrations" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Click on the integration name, then click "Show" to reveal the API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   Copy the API key <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### 3. [[connecting_notion_databases_via_api | Connecting the Notion Database with the API Key]]
The database containing the data for your documents needs to be connected to the API key you just created <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Go to your Notion database page.
*   Click the three dots in the top right corner of the database <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Select "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Search for the name of your API key (e.g., "new key") and select it <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   Click "Confirm" to connect the database <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### 4. Configuring the Document Generation Tool
Using a tool like pdf4put.com:
*   Paste the Notion page URL into the designated field <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   Click "Load page" to verify the template is loaded correctly <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Paste the Notion API key into its respective field <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   Paste the Notion database URL into its field <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Click "Load database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Select the column to be used for naming the generated PDF files (e.g., "invoice number") <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Choose which rows from the database to use for generation (e.g., "all rows," "custom rows," or a specific row) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### 5. Generating and Saving Documents
*   Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   The tool will process each record, populating the template with data from the database <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   Review the generated document's layout settings (paper size, orientation, pages) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Save each generated PDF document to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Important Considerations

*   **Public Page Access**: The Notion template page *must* be shared and made public for the integration to work <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Database-API Connection**: The Notion database *must* be explicitly connected to the API key you created <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Relational Properties**: If your Notion database uses relation properties to connect to other databases, those *relational databases* must also be connected with the *same API key* <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Failure to connect relational databases will prevent the proper fetching of data from those related sources <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

For any queries or assistance, you can reach out via email at notionformyuse@gmail.com or use the contact window provided by the tool <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.