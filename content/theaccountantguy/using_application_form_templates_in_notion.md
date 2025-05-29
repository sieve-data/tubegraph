---
title: Using Application Form Templates in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to leverage Notion databases and templates to automatically generate PDF documents, such as application forms, using an external tool called PDF Output. This method allows for bulk creation of documents without manual data entry for each file <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up the Notion Database and Template

The process begins with an application form database in Notion that tracks various requirements, including candidate profiles and education details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Designing the Template

An application form template is created to match the database structure <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Key data fields within this template, such as "Full Name," "Date of Birth," "Gender," and "Phone Number," are enclosed in curly brackets (e.g., `{Full Name}`) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields correspond directly to the column names in your Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Populating Database Rows with the Template

Initially, you would manually copy the template content and paste it into each row (page) within your Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Automating Template Population

To avoid manual copying for new entries, you can create a default template within your Notion database <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
1.  Click the dropdown next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the template content (with curly bracket placeholders) into this new template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  Click outside to save.
6.  Click the three dots next to the new template name <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "Set as default" and choose "For all views" within your specific application form database <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Now, whenever a new row is added to your database, the template content will automatically populate the page <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This is a form of [[configuring_notion_templates_for_automation | configuring Notion templates for automation]].

## Integrating with PDF Output

The PDF Output tool facilitates bulk PDF generation from Notion databases <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Connecting Notion to PDF Output

1.  **Copy Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  **Generate API Key**: Your Notion database must be connected to PDF Output via an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   In Notion, go to Settings & Members > Integrations > Develop your own integrations <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   Click "New integration," provide a name, select your workspace, and save <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a> and paste it into PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  **Connect Database to Key**: In your Notion database, click the three dots menu, select "Connections," and choose the integration (API key) you just created <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
4.  **Publish Database**: For PDF Output to access your database, it must be published. Click "Share," then "Publish," and confirm "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This is crucial for the tool to fetch pages within the database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDF Documents

1.  **Load Database**: In PDF Output, click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a column from your database (e.g., "Full Name") to be used as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
3.  **Choose Rows**: Select whether to generate PDFs for "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

The tool will process each selected row. The data from the database fields will automatically populate the corresponding curly-bracketed placeholders in the template <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. You can adjust settings like paper size and layout on the right side of the PDF Output interface <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. The generated PDFs will have professional-looking formats and will be named according to your selected column <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Alternative Template Usage

Instead of embedding the template within each database row, you can also link a standalone Notion page containing your template directly to PDF Output <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of the standalone template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  Paste this URL into the "Notion Page" section in PDF Output <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load page" to load the template content <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed to load your database and generate PDFs as usual <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. The data from the database rows will still populate the placeholders in the external template.

## General Considerations for [[creating_templates_and_databases_in_notion | Creating Templates and Databases in Notion]]

*   Ensure that the fields in your template (inside curly brackets) exactly match the column names in your database <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   It is vital that the template content is available within each database page (either manually copied or, preferably, via a default template) or linked as an external page for PDF generation to work <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   While placeholder elements matching database fields are useful for dynamic content, you can also use this method to generate PDFs from any Notion page content, even if it doesn't strictly adhere to the placeholder format <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tool will simply convert the page content to PDF <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   This method is broadly applicable for [[customizing_notion_templates_for_business_needs | customizing Notion templates for business needs]] or personal use, such as [[creating_and_using_invoice_templates_in_notion | generating invoices from an invoice database]] <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

For additional resources on [[customizing_notion_templates | customizing Notion templates]], PDF Output offers a template section with predefined templates and accompanying instructional videos <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. If you require further assistance, a contact section is available on the PDF Output homepage <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.