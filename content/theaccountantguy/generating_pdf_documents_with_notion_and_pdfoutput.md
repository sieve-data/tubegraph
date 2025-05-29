---
title: Generating PDF documents with Notion and PDFOutput
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool designed to [[bulk_pdf_generation_from_notion_databases | generate PDF documents in bulk]] using data from a [[using_notion_as_a_database_for_pdf_generation | Notion database]] and a Notion template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves mapping elements from your Notion database to placeholders in a template, enabling the quick [[generating_pdf_documents_from_notion | creation of multiple PDFs]] like [[generating_pdf_invoices_from_notion_data | invoices]] or [[generating_payment_receipts_in_pdf_using_notion | payment receipts]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## How PDFOutput Works

PDFOutput functions by replacing placeholder text within a Notion template with corresponding data from rows in a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Template and Database Interaction
The template uses elements enclosed in curly braces (e.g., `{invoice_number}`, `{date}`, `{due_date}`) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Each row in your Notion database provides the specific information for these placeholders, allowing PDFOutput to fetch and insert the correct data for each document generated <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Customizing Templates
Templates can be customized by adding, deleting, or modifying elements, as long as any new bracketed elements correspond to existing columns in your Notion database <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Setting Up PDFOutput for Notion
[[setting_up_pdfoutput_for_notion_databases | Setting up PDFOutput]] involves several steps to connect your Notion workspace and prepare your templates and databases for PDF generation.

### 1. Accessing PDFOutput
Navigate to PDFOutput.com to begin <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### 2. Duplicating a Notion Template
1.  **Browse Templates**: On the PDFOutput platform, go to the "Templates" section <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. You can search, sort, or filter available templates <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  **Download Template**: Click the "Download" link next to your chosen template (e.g., an invoice template) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This will open the template in a new tab <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Duplicate to Notion**: Click "Start with this template" to duplicate the template and its associated database to your own Notion workspace <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Select Workspace**: Choose the Notion workspace where you want to add the template and click "Add to Private" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### 3. Connecting Notion Workspace to PDFOutput
1.  **Go to Settings**: In PDFOutput, navigate to the "Settings" tab <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
2.  **Add Templates**: Click on "Click here to add templates" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Choose Pages**: You will be redirected to Notion to select the specific pages (templates and databases) you want to grant PDFOutput access to <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Ensure you select the Notion account where you duplicated the template <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  **Allow Access**: Select the duplicated template page and click "Allow Access" <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. PDFOutput will then authenticate and configure the connection <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### 4. Selecting Database and Template
1.  **Choose Database**: Back in PDFOutput, select your Notion database from the dropdown menu <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  **Choose Template**: Select your Notion template from the template dropdown <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
3.  **Name the Connection**: Give your connection a name (max 20 characters) and click "Next" <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### 5. Mapping Notion Properties to Template Elements
PDFOutput will load all elements from your database and template <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Automatic Mapping**: Notion properties (column headers) on the left are automatically mapped to template elements on the right <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Manual Mapping**: If a property isn't automatically mapped (shown in gray), you can click on it to manually select the correct template element from a list <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Matching Names**: Ensure that the names of your template elements (inside curly braces) exactly match the column names in your Notion database for successful automatic mapping <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Search, Sort, Filter**: Tools are available to help manage mapping, including search, sorting, and filtering options for unmapped properties <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### 6. Exporting and Generating PDFs
1.  **PDF Status Column**: A "PDF Status" column is automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Ensure that the checkboxes in this column are *unchecked* for the rows you want to [[exporting_notion_data_to_pdf | generate PDFs]] from <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Once a PDF is generated for a row, its checkbox will automatically be checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
2.  **Export**: Click "Export" to start the [[bulk_pdf_generation_from_notion_databases | PDF generation process]] <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
3.  **Preview and Download**:
    *   **Preview Sample**: After successful export, you can preview a sample PDF generated from one row <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   **Download All**: Click "Download all" to download a ZIP file containing all the generated PDFs <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Each PDF will correspond to a row in your Notion database, with all placeholder data correctly replaced <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

## Managing Connections

Once a connection is set up, it will appear in the "Connections" window in PDFOutput <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Reuse Connections**: For subsequent PDF generations using the same database and template, simply select the existing connection from this list <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Regenerating PDFs**: To regenerate a PDF for a specific row, ensure its "PDF Status" checkbox in Notion is *unchecked* before initiating the export <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Subscription and Watermarks

*   **Paid Plans**: Users on a paid plan will not see a watermark on their generated PDFs <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **New/Free Users**: New users or those not on a paid plan will have a watermark on their PDF output <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Upgrade**: You can upgrade your subscription from the "Upgrade Subscription" option within the platform <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## Settings and Support

*   **Page Format**: Under the "Settings" tab, you can choose different page formats for your documents (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Feedback**: For questions or issues, use the feedback option to send a message directly to support <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Help**: The "Help" section provides access to demonstration videos for guidance <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Contact**: For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.