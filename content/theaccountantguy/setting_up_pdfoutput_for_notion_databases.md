---
title: Setting up PDFOutput for Notion databases
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] is a straightforward tool designed to [[generating_pdf_documents_from_notion | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This guide explains how to set it up and use it for your PDF generation needs.

## Initial Interface and Requirements

The [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] interface requires specifying connection details, selecting a [[connecting_notion_database_with_pdf_output | Notion database]], and choosing a [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion template]] for PDF creation <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Before starting, you need two main components:
*   A template for PDF output, such as an invoice template with placeholder text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Placeholder text elements (e.g., `client name`, `client company`, `invoice number`) are enclosed in curly brackets and will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   A [[creating_a_notion_database_for_pdfs | Notion database]] that contains the information to populate the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each row in the database should contain unique information corresponding to the template's placeholders <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Configuring PDFOutput Settings

The first step in [[connecting_notion_database_with_pdf_output | connecting Notion database with PDF output]] is to access the settings menu by clicking 'S' or pressing 's' on your keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Page Format
The ideal page format for the best output is A4, though other options are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### API Key Setup
Currently, [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] uses the Notion private integration key <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

> [!NOTE] Obtaining the Notion API Key
> To obtain your Notion API key:
> 1.  Click the link in [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] to be redirected to your Notion account <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
> 2.  Click on "New integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
> 3.  Add a name for your integration (e.g., "new integration window") <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
> 4.  Select the workspace you want to link <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
> 5.  Keep the key as "internal" and click "Save" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
> 6.  Click "Configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
> 7.  Click "Show" to reveal your secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
> 8.  Copy this key and save it immediately, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
> 9.  Paste the copied key into the Notion API key field in [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
> Every user must create their own integration key, as it is secret and unique to their system <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Connecting Notion Databases and Templates

After setting up the API key, you need to connect your [[using_notion_as_a_database_for_pdf_generation | Notion database]] and template to the integration:
1.  In your Notion template page, click the three dots in the top right corner <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  Scroll down and select "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
3.  Type the name of the integration you created (e.g., "new integration") and select it to link <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
4.  Repeat the same steps for your [[creating_a_notion_database_for_pdfs | Notion database]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Database Property for PDF Generation

In your [[using_notion_as_a_database_for_pdf_generation | Notion database]], ensure there is a property named "PDF status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   If this checkbox is ticked, [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will *not* generate a PDF for that specific row of information <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   To generate a PDF for a row, this checkbox must be unchecked <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Generating PDF Documents

1.  Return to [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] and enter a connection name (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  Select your desired [[creating_a_notion_database_for_pdfs | Notion database]] and [[using_notion_templates_and_databases_for_pdf_generation | Notion template]] from the dropdown lists <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Property Mapping
[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] reads information from the template and database, automatically mapping Notion properties (database column names) to the corresponding placeholder elements in the template <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Recommendation**: Ensure that the naming convention for template placeholders (within curly brackets) exactly matches the column names in your [[using_notion_as_a_database_for_pdf_generation | Notion database]] for automatic mapping <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   If an element is not automatically mapped (it will appear in gray), you can manually click on it and select the correct Notion property from the fetched PDF elements <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   Sorting and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Exporting and Downloading
1.  Click "Export" to start the PDF generation process <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
2.  During processing, the "PDF status" checkbox in your [[creating_a_notion_database_for_pdfs | Notion database]] will automatically tick for rows as their PDFs are generated <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
3.  Once the export is successful, you have two options:
    *   "Preview sample": View the generated PDF directly in the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   "Download all": Download the generated PDF files to your local machine <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

> [!INFO] Watermark
> Users on the free plan will see a watermark on generated PDFs, which is removed for paid plans <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Managing Connections and Subscriptions

### Saved Connections
Once a connection is successfully created, you can access it again by clicking 'C' <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This loads previously defined settings, allowing for subsequent [[generating_pdf_documents_from_notion | PDF document generation]] without re-entering details <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### Upgrade Options
The basic plan allows for a limited number of document downloads (e.g., 1000) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. To exceed this limit, you can upgrade your subscription by choosing from various monthly or yearly Pro and Enterprise plans <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Additional Features

*   **Templates Section**: Future updates will add more pre-built templates under the 'T' section <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback**: Users can submit feedback directly to the developer through the feedback window <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Help**: A help window will include tutorial videos for reference <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Sign Out**: An option to sign out is available via the profile icon <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

> [!IMPORTANT] Future API Access
> Currently, Notion API access requires a private key, meaning each user needs to create their own. Future updates may introduce public API key access, simplifying the setup process <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

## Customizing Templates and Databases

You can customize your own [[using_notion_templates_and_databases_for_pdf_generation | Notion templates]] and databases <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The key is to ensure that placeholder names within curly braces in your template exactly match the column names in your [[creating_a_notion_database_for_pdfs | Notion database]] <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This ensures that [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] can accurately read and import the values from your database rows into the corresponding template placeholders <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.