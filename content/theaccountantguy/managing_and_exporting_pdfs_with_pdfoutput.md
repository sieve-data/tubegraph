---
title: Managing and exporting PDFs with PDFOutput
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] is a straightforward tool designed to [[generating_pdf_documents_with_notion_and_pdfoutput | generate PDF documents]] directly from a Notion database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Its interface allows users to specify connection details, select a Notion database, and choose a Notion template to create the PDF document <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Requirements for PDF Generation

To use [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]], you need a template and a Notion database <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
For example, an invoice template might include placeholder text elements within curly brackets, such as `{client name}` or `{invoice number}` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders are then replaced by data from a corresponding Notion database that contains columns like "Client Name", "Client Company", and "Invoice Number" <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Each row in the database represents unique information that will populate a separate PDF <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Setting Up PDFOutput

### Accessing Settings
The settings window can be opened by clicking the 'S' button or pressing 's' on your keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Here, you can specify the page format, with A4 being the recommended ideal output, though other formats are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### [[setting_up_pdfoutput_with_api_keys | Setting up API Keys]]
A crucial first step is to [[setting_up_pdfoutput_with_api_keys | set up the Notion API key]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Currently, this involves using a Notion private integration key <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

To obtain the key:
1.  Click the "Click here to get the Notion API key" link <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
2.  On the Notion account page, create a new integration <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Add a name for the integration (e.g., "new integration window"), select the workspace, and keep it as an internal key <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
4.  Click "Save" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
5.  Click "Configure internal integration settings" and then "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
6.  Copy this key and save it somewhere, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
7.  Paste the copied key into the "Notion API key" field in [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. You can clear the API key settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Connecting Notion to the API
After [[setting_up_pdfoutput_with_api_keys | setting up the API key]], you must connect both your Notion template and your Notion database to the integration <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
1.  In Notion, navigate to the template page or database <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  Click the three dots at the top right <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  Scroll down to "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
4.  Type the name of the integration you created (e.g., "new integration") and select it to link your template/database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Repeat this for both the template and the database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## [[workflow_for_exporting_and_downloading_pdf_documents | Generating PDF Documents]]

Before generating, ensure your Notion database includes a "PDF status" property (a checkbox) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For a PDF to be generated for a specific row, this checkbox must be unchecked <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Once the PDF is generated, [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will automatically tick this box <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Process Steps:
1.  In [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]], enter a connection name (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  Select the connected Notion database from the dropdown list (search functionality is available) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  Select the Notion template from its dropdown list <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
5.  [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] will read information from both the template and database and automatically map Notion properties to template placeholders <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. It's recommended that Notion column names exactly match the placeholder names in the template (e.g., "client name" column maps to `{client name}`) for automatic mapping <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
6.  If elements are not automatically mapped (appearing in gray), you can manually click them to select the corresponding PDF element fetched from the template <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Search, sort, and filter options are available to help manage properties <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
7.  Click "Export" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The system will process the documents, and the "PDF status" checkboxes in your Notion database will tick automatically as PDFs are generated <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Reviewing and Downloading PDFs

Once export is successful, you have two options:
*   **[[using_pdf_output_for_document_export_and_preview | Preview Sample]]**: This displays a preview of the generated PDF directly on the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. The preview will show how data from the Notion database has replaced all the placeholder elements in the template <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **Download**: [[bulk_exporting_pdf_documents | Clicking "Download all"]] will automatically download the generated PDF files to your downloads folder <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Each row from the Notion database will result in a separate PDF document <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

On the free plan, generated PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This watermark is removed on paid plans <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## [[managing_pdfoutput_settings_and_subscriptions | Managing Connections and Subscriptions]]

### Loading Saved Connections
After creating a connection, you can easily load its settings by clicking the 'C' button <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This will show previously created connections (e.g., "invoice generation"), allowing you to load them and generate more documents without re-specifying settings <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Upgrading Subscriptions
The "Upgrade" option allows you to view and change your subscription plan <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. The basic plan typically includes a limit (e.g., 1000 documents) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Once this limit is reached, you need to upgrade to a Pro or Enterprise plan, available monthly or yearly, to continue generating documents <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. After upgrading, click "Activate Subscription" to apply the new plan <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Other Features
*   **Templates (T)**: This section will display more templates as they are added <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback**: You can submit feedback directly through the feedback window to help improve [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]]'s performance <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Help**: The help window will contain tutorial videos for reference <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Profile Icon**: Provides an option to sign out <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Customizing Templates
You can customize your own templates for use with [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The key is to use curly braces for placeholder names (e.g., `{Invoice Number}`) and ensure these names exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This enables [[generating_pdf_documents_with_notion_and_pdfoutput | PDFOutput]] to automatically import values from the database and populate the template's placeholder text elements for each row of data <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

## Contact Information
For questions or assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>, or connect on Twitter or LinkedIn <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.