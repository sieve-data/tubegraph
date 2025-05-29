---
title: Generating PDF documents from Notion
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] is a straightforward tool designed to [[generating_pdf_documents_with_notion_and_pdfoutput | generate PDF documents]] directly from a [[using_notion_as_a_database_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It functions by allowing users to select a Notion database and a Notion template to create the PDF output <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Requirements for PDF Generation

To [[generating_pdf_documents_with_notion_and_pdfoutput | generate PDF documents]] using [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]], the following are needed:

1.  **Notion Template** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>: This template (e.g., an invoice template) contains placeholder text elements, typically enclosed in curly brackets (e.g., `{client name}`, `{invoice number}`), which will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. When creating custom templates, ensure that the naming convention for placeholders exactly matches the column names in the Notion database to enable automatic mapping <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a> <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
2.  **Notion Database** <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>: This database holds the information that will populate the PDF document <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For instance, an invoice database would contain columns like "client name," "client company," "client address," and "invoice number" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Each row of information in the database is unique and will be used to generate a separate PDF <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **PDF Status Property** <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>: A checkbox property named "PDF status" must be present in the Notion database <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. If this box is unchecked, [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will [[generating_pdf_documents_with_notion_and_pdfoutput | generate the PDF]] for that specific row <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. After generation, the checkbox will automatically be ticked <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Setup and Configuration

### Accessing Settings

To configure [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]], click on the 'S' button or press 'S' on your keyboard to open the settings window <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Here, you can specify the page format, with A4 being the recommended option for best output, though other formats are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Obtaining a Notion API Key

A Notion API key is essential for connecting [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] to your Notion workspace <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Currently, the tool utilizes Notion's private integration key setup <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

To get your API key:
1.  Click the provided link in [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] to be redirected to your Notion account <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Create a "new integration" by providing a name and selecting the desired workspace <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Ensure the key type is set to "internal key" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
4.  Click "Save" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
5.  Then, click "configure internal integration settings" and select "show" to reveal your secret key <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

> [!CAUTION]
> This key is secret and applicable only to the user who creates it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Every user must create their own integration key <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Once the window is closed, the key will no longer be visible, so copy and save it immediately <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

Paste the copied key into the "Notion API key" field in [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. You can clear the API key settings by clicking the "clear" button <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Connecting Notion Pages/Databases to the Integration

After setting up the API key, you need to connect your Notion template page and database to the newly created integration:
1.  Navigate to your Notion template page or database <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
2.  Click the three dots `...` on the top right <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  Scroll down and select the "Connect" option <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
4.  Search for and select the name of the integration you created (e.g., "new integration") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
5.  Repeat this process for both the template page and the database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Generating PDF Documents

### Specifying Connection Details in PDFOutput

Once the API key is set up and Notion pages are connected:
1.  In [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]], enter a connection name (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  Select your desired [[using_notion_as_a_database_for_pdf_generation | Notion database]] from the dropdown list <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  Select your [[using_notion_for_pdf_template_creation | Notion template]] <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Mapping Properties

[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will read the information from the template and database and display the Notion properties on the left side <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. It automatically maps database columns to template placeholders if the names match exactly <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

If an element is not automatically mapped (appearing in gray), you can click on it to manually select the correct Notion property from the fetched PDF elements <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. The mapping interface includes search, sort, and filter options (for unmapped or mapped properties) to assist with this process <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Exporting and Downloading

After mapping, click "Export" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will begin processing the documents <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. During this process, the "PDF status" checkboxes in your Notion database will automatically tick as each PDF is generated <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

Once [[bulk_pdf_generation_from_notion_databases | export]] is successful <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:
*   You can click "Preview Sample" to view the PDF directly on the web interface <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Click "Download all" to [[exporting_notion_data_to_pdf | download the generated PDF documents]] to your computer <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Watermarks and Plans

On the free plan, generated PDFs will display a watermark <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Upgrading to a paid plan will remove this watermark <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Managing Connections and Subscriptions

### Saved Connections

Once a connection is successfully created and documents are downloaded, it is saved <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. You can click on the "C" (Connections) option to see a list of your saved connections <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Clicking on a saved connection will automatically load its previously defined settings, allowing for subsequent PDF generation without re-entering details <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Upgrade Options

The basic plan typically allows for a certain number of documents (e.g., 1000) before an upgrade is required <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Clicking the "Upgrade" option provides access to various monthly and yearly pricing plans (e.g., Pro Plan, Enterprise plan) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. After upgrading, click "Activate Subscription" to apply the new plan <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Support and Feedback

*   **Templates:** Future updates will include more pre-built templates under the "T" (Templates) section <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Settings:** The settings window allows for page format changes and API key management <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Feedback:** Users can submit feedback via the "Feedback" window to help improve the tool's performance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Help:** A help window will contain tutorial videos for reference <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Contact:** Contact details (e.g., email, Twitter, LinkedIn) are available for direct assistance <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.