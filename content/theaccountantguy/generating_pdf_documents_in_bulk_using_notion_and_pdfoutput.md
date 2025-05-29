---
title: Generating PDF documents in bulk using Notion and PDFOutput
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

[[Using PDFoutputcom to generate PDF documents in bulk | PDFOutput]] is a simple tool designed to help users [[using_pdfoutputcom_to_generate_pdf_documents_in_bulk | generate PDF documents in bulk]] using a [[Notion database | Notion database]] with the help of a [[Using PDF Output with Notion Templates | Notion template]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process involves replacing placeholder elements, typically enclosed in curly braces within a template, with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## How PDFOutput Works

[[Integrating Notion with PDF4put for bulk document generation | PDFOutput]] fetches information from every row and corresponding column of a Notion database <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. It then replaces placeholder text elements within a Notion template with this data, allowing for the [[generating_bulk_pdf_documents_using_google_docs_and_notion | bulk generation of PDF documents]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

For example, an invoice template might have placeholders for `{{invoice number}}`, `{{date}}`, `{{due date}}`, and `{{terms}}` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These placeholders will be dynamically populated from the database for each generated PDF <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Getting Started with PDFOutput

To begin [[generating_pdfs_from_notion_using_pdfoutput | generating PDFs from Notion using PDFOutput]]:

### Accessing the Platform
Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Duplicating Templates to Notion
1.  After logging in, click on the "Templates" option on the right side <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  A new page will display various templates, which can be searched, sorted, or filtered <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
3.  Click the "Download link" next to the desired template (e.g., an invoice template) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This will open the template and its associated database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
4.  To use the template, it must be duplicated to your own Notion workspace. Click "Start with this template" and choose your Notion account and workspace to add it <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The template and database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Connecting and Setting Up Notion
1.  Return to PDFoutput.com and go to the "Settings" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This will redirect to Notion to choose the templates <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  Select the Notion account where you duplicated the templates and click "Select Pages" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  Choose the specific Notion page containing the template and database (e.g., "Invoice PDF Generator") <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  Click "Allow access" to authenticate the connection <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. You will then be redirected back to PDFOutput <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Generating PDF Documents

Once connected, you can configure and generate your PDFs:

### Selecting Database and Template
1.  In PDFOutput, select your Notion database (e.g., "Professional Invoice Database") and your Notion template (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  Give a name to this generation process (max 20 characters) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  Click "Next" to load elements from the database and template <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Mapping Notion Properties to Template Elements
*   The system automatically maps Notion properties (database column names) to the template elements (placeholders) <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   Ensure that property names in Notion exactly match the placeholder names in the template for automatic mapping to occur <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   If a property is unmapped (appears in gray), you can manually click on it to select the correct template element <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Search, sort, and filter options are available for mapping <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   A "PDF Status" column is automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Ensure that the checkboxes in this column are unchecked for the rows you want to generate. Checked rows will not be included in the PDF output <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This column is unchecked by default upon initial integration <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### Exporting and Downloading
1.  Click "Export" to start processing the documents <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
2.  As documents are generated, the "PDF Status" column in your Notion database will automatically update with a tick mark <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
3.  Upon successful export, you have two options:
    *   **Preview Sample**: View a single generated PDF to verify its contents <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This shows how database entries (e.g., client name, address, invoice number) are replaced in the template <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   **Download All**: Download all generated PDF documents <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The number of documents generated will correspond to the number of rows in your Notion database <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## Managing Connections and Account Settings

### Connections
After the first successful export, your configuration (database, template, mappings) is saved as a "Connection" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   Access saved connections via the "Connections" window <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   Select a previously named connection to quickly load its settings for future bulk generations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   Remember to untick the "PDF Status" checkboxes in Notion if you want to regenerate specific rows <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Upgrade Options and Features
*   The "Upgrade" section displays your current plan, renewal date, and download count <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   New users on free plans may see a watermark in the PDF output. Paid plans remove this watermark <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### Page Format
Under the "Settings" tab, you can choose different page formats for your PDFs (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Select a format and click "Save" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Feedback and Help
*   The "Feedback" option allows users to send messages directly to the support team for assistance <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   The "Help" window provides access to demonstration videos and tutorials <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

For any questions or further assistance with [[generating_payment_receipt_pdfs_in_bulk_using_notion | PDFOutput generations]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.