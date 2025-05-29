---
title: Using a Notion database and templates to create PDF invoices
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to help users generate PDF documents in bulk by leveraging a [[using_notion_as_a_database_for_pdf_generation | Notion database]] and a [[using_notion_for_pdf_template_creation | Notion template]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves replacing placeholder elements within a template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## How it Works: Invoice Generation Demo

The process can be demonstrated with an invoice template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The template includes placeholders, identifiable by curly braces (e.g., `{invoice number}`, `{date}`, `{due date}`, `{terms}`), which are dynamically replaced with information from a Notion database <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Each row of the Notion database provides the data for a corresponding PDF document <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Setting Up Your Template and Database

1.  **Access PDF Output**: Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Select a Template**: Go to the "Templates" section on the right side of the interface <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Here, you can search, sort, or filter available templates <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
3.  **Duplicate to Notion**: To use a specific template, such as an [[using_notion_templates_for_invoice_pdfs | invoice template]], click the "Download link" next to it <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This opens a page with both the database and template elements <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. You must duplicate this template into your personal Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, then select your desired Notion account and workspace <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
4.  **Connect Notion to PDF Output**: Return to PDFoutput.com and go to "Settings" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Click "Click here to add templates" to be redirected to Notion <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Choose the Notion account where you duplicated the template, select the specific pages (database and template) you want to use, and click "Allow access" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Customizing and Mapping

Once connected, you can customize the Notion template. Ensure that any elements added inside curly braces in the template exactly match the column names in your [[creating_a_notion_database_for_pdfs | Notion database]] <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

1.  **Select Database and Template**: In PDF Output, choose your [[creating_a_notion_database_for_pdfs | Notion database]] (e.g., "Professional Invoice Database") and your [[using_notion_for_pdf_template_creation | Notion template]] (e.g., "Invoice Template") from the dropdowns <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  **Name Your Generation**: Provide a short name for your PDF generation process (e.g., "My Invoice Generation") <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. There is a 20-character limit <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
3.  **Map Properties**: The system will load elements from both your database and template <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. On the left, you'll see Notion properties (database columns), and on the right, template elements <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   **Automatic Mapping**: If the names match exactly, the system will automatically map the properties (shown in green) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   **Manual Mapping**: If names differ, a property might appear in gray <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Click on it to manually select the correct corresponding element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Search, sort, and filter options are available to assist with mapping <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Generating PDFs

1.  **PDF Status Column**: Before exporting, check your Notion database for a "PDF status" column <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For a row to be included in the PDF output, this checkbox *must* be unchecked <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. After generation, it will automatically become checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. If you need to regenerate a specific row, uncheck its "PDF status" box <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
2.  **Export**: Click "Export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
3.  **Preview and Download**: Once the export is successful, you have two options:
    *   **Preview Sample**: View a single sample invoice generated from the database <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, showing how Notion data replaces template placeholders <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
    *   **Download All**: Download all generated PDF documents <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The system will generate a separate PDF for each applicable row in your Notion database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Managing Connections and Features

*   **Connections Window**: After a successful export, your setup is saved as a "Connection" <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. The next time you need to [[generating_pdf_invoices_from_notion_data | generate PDF invoices from Notion data]] using the same database and template, simply go to the "Connections" window and select your saved connection <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This will automatically load all elements for quick regeneration <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Upgrade Options**: Users on paid plans (e.g., Enterprise) will not see a watermark in the PDF output <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, unlike new or free users <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. You can upgrade your subscription and activate it within the platform <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Page Format**: Under the "Settings" tab, you can select different page formats (e.g., A4, Letter) for your PDF documents <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Feedback and Help**: A feedback option allows users to send messages directly to the developer for assistance <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. The help section provides access to demonstration videos like this one <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

This system facilitates [[using_notion_templates_and_databases_for_pdf_generation | setting up a Notion database and template for PDF generation]] efficiently <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, making it straightforward to create and use [[creating_and_using_invoice_templates_in_notion | invoice templates in Notion]] for bulk PDF creation <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.