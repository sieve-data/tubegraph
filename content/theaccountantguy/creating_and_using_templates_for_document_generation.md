---
title: Creating and using templates for document generation
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool designed to [[using_templates_to_generate_pdf_documents | generate PDF documents in bulk]] by leveraging a Notion database and a Notion template <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This process involves replacing placeholder elements within a template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

## How it Works: Invoice Generation Example

Using an invoice template as an example, elements within curly braces (e.g., `{Invoice Number}`, `{Date}`, `{Due Date}`) are treated as placeholders <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. These placeholders are then replaced by the corresponding information from each row of a Notion database <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. The tool fetches information for corresponding columns in the database and uses it to populate the template, generating individual PDF documents <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. This demonstrates [[using_templates_and_placeholders_for_document_creation | using templates and placeholders for document creation]].

## Step-by-Step Guide to Using PDFOutput

### 1. Accessing PDFOutput

Begin by navigating to PDFOutput.com <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. After logging in, you will see a section for templates on the right side of the interface <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This area lists various pre-added templates for different use cases <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Templates can be searched, sorted, or filtered for easier navigation <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### 2. Duplicating Templates to Notion

When selecting a template (e.g., an invoice template), click the "download link" to open its page <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This page will display both the database and template elements <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. To use a template, you must duplicate it to your own Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. Choose your desired Notion workspace and click "Add to private" to complete the duplication <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

### 3. Connecting Notion Workspace to PDFOutput

Once templates are duplicated, return to PDFOutput.com and go to "Settings" <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Click "click here to add templates," which will redirect you to your Notion workspace <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. Select the Notion account where you duplicated the templates <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. Choose the specific pages (templates and databases) you want to use and click "Allow access" <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. Successful authentication will redirect you back to PDFOutput <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. This is a crucial step in [[setting_up_notion_templates_and_databases_for_pdf_generation | setting up Notion templates and databases for PDF generation]] and [[creating_notion_templates_and_databases_for_pdf_generation | creating Notion templates and databases for PDF generation]].

### 4. Selecting Database and Template

After authentication, PDFOutput will allow you to fetch the Notion database and template <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. Select the appropriate Notion database (e.g., "Professional Invoice Database") and the Notion template (e.g., "Invoice Template") <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. Provide a short name for the generation process (under 20 characters) and click "Next" <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. This initiates [[using_notion_database_and_templates_for_pdf_generation | using Notion database and templates for PDF generation]] and [[using_notion_templates_and_databases_for_pdf_creation | using Notion templates and databases for PDF creation]].

### 5. Mapping Notion Properties to Template Elements

PDFOutput will load all elements from the database and template <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. In "Step 2," you'll see Notion properties (database column names) on the left and template elements (placeholders) on the right <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

> "Make sure the name that you specify over here exactly matches the name that you specify over in the database" <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

Automatic mapping occurs if names match; otherwise, unmapped elements will appear in gray <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. You can manually map elements, and search, sort, or filter options are available for convenience <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. All mapped elements will be shown in green <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.

### 6. Exporting Documents

Before exporting, ensure the "PDF Status" column in your Notion database is unchecked for the rows you wish to generate <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. If checked, that particular row will not be generated <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. By default, this column is unchecked initially <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. Once documents are generated, this status will automatically update to checked <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. Click "Export" to begin processing <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

### 7. Previewing and Downloading Generated PDFs

Upon successful export, you have options to "Preview sample" or "Download all documents" <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. Previewing a sample allows you to verify that data from the Notion database (e.g., client name, address, invoice number, date) has correctly replaced the template placeholders <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. Clicking "Download all" will provide a folder containing all generated PDF files, with each file corresponding to a row in your Notion database <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.

## Additional Features and Considerations

*   **Customization**: Templates can be customized by adding, deleting, or modifying elements, as long as new placeholders match column names in your Notion database <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Connections**: Once an export is generated, the connection (database and template pairing) is saved in the "Connections" window <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. This allows for easy regeneration of documents using the same setup by simply selecting the saved connection <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. This is part of [[managing_templates_and_databases_within_pdfoutput | managing templates and databases within PDFOutput]].
*   **Regeneration**: To regenerate specific rows, ensure their "PDF Status" checkboxes in the Notion database are unticked <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.
*   **Subscription Plans**: New users on free plans may see a watermark on generated PDFs <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. Paid plans remove this watermark <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.
*   **Page Format**: Under the "Settings" tab, users can choose different page formats for their documents <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
*   **Support**: A feedback option allows users to send messages for assistance <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>, and a "Help" window provides access to demonstration videos <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>.