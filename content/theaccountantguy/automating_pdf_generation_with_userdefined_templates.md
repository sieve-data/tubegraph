---
title: Automating PDF generation with userdefined templates
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that allows users to [[automating_data_entry_and_pdf_generation | automate data entry and PDF generation]], specifically by using a Notion page and a Notion database to [[bulk_pdf_document_generation | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process leverages user-defined templates to populate dynamic information from a database into PDF documents <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Overview

The core functionality involves using a template where specific fields are marked with curly braces (e.g., `{purchase order number}`, `{date field}`, `{supplier name}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These bracketed items are then replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This enables the efficient creation of documents like [[working_with_purchase_order_templates_in_pdf_generation | purchase order PDFs]] for each row in a database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## How it Works: Templates and Databases

1.  **Template Structure:** A Notion page serves as the template. Within this page, placeholders for dynamic data are enclosed in curly braces <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These placeholders correspond to column names in your Notion database <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
2.  **Database Integration:** A Notion database holds the specific data for each PDF document <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Each row in the database will correspond to one generated PDF, with the column headers matching the curly-braced placeholders in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This ensures automatic mapping of data during the generation process <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Step-by-Step Guide

### 1. Accessing PDF Output

*   Navigate to PDF Output's website (PDF output.com) <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   Upon logging in, you will see an interface prompting you to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 2. Duplicating Templates and Databases

*   Go to the "Template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Search for a predefined template (e.g., "purchase order") <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   Select "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   Choose your desired Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 3. Connecting Notion to PDF Output

*   Return to PDF Output and click on "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   You will be prompted to give permissions <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Select your Notion workspace and choose the duplicated database and template <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. PDF Output will then connect to your Notion database and template <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. If they don't appear immediately, click the refresh button <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 4. Mapping Data Fields

*   Define a name for your PDF generation process (e.g., "purchase order") <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   The tool will load the database elements and template elements <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   If the naming conventions between your Notion database columns and your template placeholders (curly braces) are identical, the elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   If not, you may need to manually map fields by clicking on greyed-out elements and choosing the correct corresponding field <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### 5. Generating and Downloading PDFs

*   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process all the documents based on the rows in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Once the export is successful, you can preview a sample PDF <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   Click "Download All" to get all generated PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Customization and Features

### Template Customization
You can edit and modify the duplicated Notion template after it's in your workspace <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any dynamic data you want to replace with database content remains inside curly braces and uses the exact same naming convention as your database columns <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Managing Connections
Under the "Connections" section, you can view previously created connections, like a "purchase order" connection <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a saved connection will automatically load the associated database and template, allowing for quick re-exports without needing to re-fill details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Settings
*   **Page Format:** The default page format for PDFs is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Adding More Databases/Templates:** After your initial setup, you can add more databases and templates via the settings menu <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Upgrading Your Plan
If you are on the free plan, generated documents will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading your subscription removes this watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Support and Feedback

*   **Feedback:** If you encounter any difficulties or have suggestions, use the feedback option within the tool <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help Section:** The help section provides a video demonstrating how to use a custom template from scratch, if you prefer not to use the predefined ones <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Direct Contact:** For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## Important Considerations

*   **Relational Properties:** If your Notion database uses any relation properties, ensure you grant access to those related databases when connecting Notion to PDF Output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   This method facilitates [[creating_and_using_templates_for_pdf_generation_in_notion | creating and using templates for PDF generation in Notion]], making it suitable for [[generating_pdf_documents_for_business_purposes | generating PDF documents for business purposes]] and [[creating_pdf_documents_for_business_needs | creating PDF documents for business needs]]. While [[managing_pdf_templates_and_storing_documents_in_google_drive | managing PDF templates and storing documents in Google Drive]] is not explicitly mentioned as a feature, the output can easily be stored there. The process described is an example of [[using_templates_to_generate_pdf_invoices | using templates to generate PDF invoices]] and other similar documents.