---
title: Generating professional invoices using Notion
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_bulk_invoices_with_notion | generate professional invoice PDF documents in bulk]] using a [[professional_invoice_template_in_notion | Notion template]] and a Notion database, facilitated by the PDF output.com software <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Components of the Invoice System

### [[professional_invoice_template_in_notion | Professional Invoice Template in Notion]]
The [[professional_invoice_template_in_notion | professional invoice template]] defines all elements typically found in an invoice <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Elements placed inside curly braces, such as `{client name}`, `{client company}`, and `{client address}`, are placeholders that will be replaced by corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Notion Database
A Notion database is used to store the information needed for the invoices <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For every element in the [[professional_invoice_template_in_notion | Notion template]] (e.g., `{client name}`), there must be a corresponding property in the Notion database (e.g., 'Client Name') <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Each row in the database represents a distinct invoice to be generated <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Step-by-Step Process for [[generating_pdf_documents_with_notion | PDF Document Generation from Notion]]

### 1. Accessing PDF output.com
Navigate to PDF output.com and log in <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Upon logging in, you will be directed to a "connection details" screen requiring you to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### 2. Duplicating Templates and Databases
Before connecting, you need to copy the pre-added [[creating_and_using_invoice_templates_in_notion | invoice templates]] and databases to your local Notion workspace <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   Go to the "Templates" section on PDF output.com <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   Search for "invoice" to find the professional invoices template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Click on both the database link and the template link <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   In the new tabs that open, click the "Duplicate" option (usually in the top right) for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Select your Notion workspace to duplicate them <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This will add the [[professional_invoice_template_in_notion | template]] and database to your personal Notion space <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### 3. Connecting Notion to PDF output.com
*   Back on PDF output.com, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Choose your Notion workspace (e.g., "the accountant guy" workspace) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Select the duplicated [[professional_invoice_template_in_notion | invoice template]] and database, then click "Allow access" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   The system will automatically load the database and template from your Notion workspace <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Define a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a> and click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### 4. Mapping Database Properties to Template Elements
*   The system will display Notion database properties on the left <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   If the database property names exactly match the template placeholders (e.g., `invoice number` in the database matches `{invoice number}` in the template), the elements will be automatically mapped <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   If names differ, an element might show a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on it to manually search and select the correct database property for mapping <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### 5. [[generating_pdf_documents_with_notion | Generating PDF Documents]]
*   The software will begin [[pdf_document_generation_from_notion | generating PDF documents]] for every row in your Notion database using the connected template <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   Once successful, you can "Preview sample" of a generated PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> or "Download all documents" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The downloaded file will be a zip archive containing individual PDF invoices for each database entry <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Customization and Best Practices for [[adding_and_managing_invoices_in_notion | Invoice Management]]

*   **Template Customization:** The invoice template is fully customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Ensure that any data you want to pull from the database is enclosed in curly braces (e.g., `{Invoice Number}`) within the template <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Naming Consistency:** For automatic mapping, the names inside the curly braces in the template should exactly match the property names in your Notion database (e.g., `{Client Name}` in template and 'Client Name' property in Notion) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Relational Properties:** If your Notion database uses relational properties linked to other databases, ensure you also allow access to those related databases during the connection setup with PDF output.com <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## Additional Features of PDF output.com

### Connections
The "Connections" sidebar option shows all previously saved database and template configurations <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. You can reuse these connections to quickly [[creating_bulk_invoices_with_notion | generate more PDF documents]] without re-defining the setup <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Templates
The "Templates" section provides a variety of pre-added templates for different use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Upgrade Section
This section allows users to upgrade their subscription <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Free plans include a "Made with PDF output" watermark on generated PDFs, which is removed with a paid subscription <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Settings
The "Settings" window allows you to:
*   Define the page format (e.g., A4 size) for your PDF documents <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   Add more databases and templates beyond the initial connection setup <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   Connect custom templates and databases if you prefer not to use the pre-added ones <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Feedback
A feedback option is available to send messages or queries for assistance <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
