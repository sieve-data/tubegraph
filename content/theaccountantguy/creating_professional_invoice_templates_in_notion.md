---
title: Creating professional invoice templates in Notion
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_professional_invoices_using_notion | generate professional invoices]] in bulk using a Notion page as a template and data from a Notion database, by leveraging the third-party tool pdf4put.com <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Preparing Your Notion Assets

To begin, you will need two main components in Notion:

1.  **Professional Invoice Template**:
    *   This is a Notion page designed as an invoice document <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
    *   Information that needs to be dynamically replaced from the database should be placed within curly brackets (e.g., `{client name}`, `{invoice number}`). These bracketed fields will be populated with data from your database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
    *   Ensure your template includes all necessary invoice information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

2.  **Invoice Database**:
    *   This Notion database contains all the varying information for each invoice <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
    *   Each record (row) in the database represents a unique invoice <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
    *   Column headers in your database must precisely match the names used within the curly brackets in your template (e.g., a column named `Client Name` will populate `{client name}` in the template) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Generating PDFs in Bulk Using pdf4put.com

The process of [[creating_invoices_in_bulk_using_notion | generating PDF invoices in bulk]] involves connecting your Notion template and database to pdf4put.com.

### Step-by-Step Guide

1.  **Access pdf4put.com**: Navigate to pdf4put.com and sign in <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

2.  **Publish Your Notion Template Page**:
    *   Open your Notion invoice template page.
    *   Click `Share`, then `Publish`, and `Publish to web` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This makes the page publicly accessible for pdf4put.com to use <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    *   Copy the public link of the page <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Paste this URL into the 'Page URL' field on pdf4put.com and click `Load page` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. You should see your template appear on the right side of the screen <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

3.  **Generate a Notion API Key**:
    *   In pdf4put.com, click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   This will open Notion's Integrations page. Click `New Integration`, provide a name (e.g., "New Key"), choose your account, and save <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Locate your new integration, click on it, select `Show`, and copy the API key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   Paste this API key into the 'API Key' field on pdf4put.com <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

4.  **Connect Your Notion Database**:
    *   Go to your Notion invoice database.
    *   Click the three dots in the top right corner, then `Connections` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Search for and select the API key you just created (e.g., "New Key") to connect the database to it <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   Paste this URL into the 'Database URL' field on pdf4put.com <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

5.  **Load Database and Configure Generation**:
    *   Click `Load database` on pdf4put.com <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   Choose a column to name the generated PDF files (e.g., `invoice number`) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   Select which rows from the database to use for PDF generation. You can choose `All rows`, a `Custom Range`, or `Specific rows` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

6.  **Generate PDFs**:
    *   Click `Generate PDF` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The tool will begin processing each record, dynamically replacing the bracketed fields in the template with data from the database <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   For each PDF, you can review its appearance, adjust layout settings (paper size, orientation, pages to print) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, and then save the file to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be named according to the column you selected (e.g., "Invoice Number 1", "Invoice Number 2") <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Important Considerations

*   **Public Notion Page**: Ensure your Notion invoice template page is publicly shared for the tool to access it <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Database-API Connection**: The database must be connected to the specific API key you created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Field Naming Consistency**: The names within the curly brackets in your template must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Relational Properties**: If your database uses [[using_templates_in_notion_for_pdf_generation | relational properties]] connecting to *other* databases, those related databases must also be connected to the *same* API key for data to be fetched correctly <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

For any queries or assistance, you can reach out to notionformyuse@gmail.com or use the contact window available on the pdf4put.com website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.