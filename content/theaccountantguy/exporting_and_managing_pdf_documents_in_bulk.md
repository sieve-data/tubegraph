---
title: Exporting and managing PDF documents in bulk
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

[[using_pdfoutputcom_to_create_bulk_pdf_documents | Using PDFoutput.com]] allows users to [[generating_and_downloading_pdf_documents_in_bulk | generate PDF documents in bulk]] from a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process is particularly useful for creating multiple documents like purchase orders, invoices, or payment receipts <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Getting Started <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

To begin [[using_pdf_output_com_to_create_bulk_pdf_documents | generating and downloading PDF documents]]:
1.  **Log in to PDFoutput.com**: This is the first step to access the platform's features <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
2.  **Select a Template**: From the sidebar, click on "Templates" to view predefined options such as invoices, payment receipts, or purchase orders <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. A search icon is available to quickly find specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download and Duplicate the Template**: Click the "Download" link next to the desired template, which opens a new page containing both a Notion database and a template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Duplicate this page to your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Understanding the Template and Database <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>

*   **Template**: This Notion page contains placeholder elements (e.g., `{purchase order number}`, `{date}`, `{supplier name}`) enclosed in curly braces <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. These placeholders will be replaced with data from your Notion database <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Database**: This Notion database holds the actual data, with columns for elements like "supplier name," "buyer name," "date," and "purchase order number" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row in the database represents a unique document that will be generated <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Both the template and database elements are fully customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. It is crucial that the names of the database columns exactly match the placeholder names in the template (including spacing and punctuation) to ensure correct linking <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Connecting and Mapping

1.  **Connect Notion Workspace**: After duplicating the template to your Notion, return to PDFoutput.com.
    *   Navigate to "Settings" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Select your Notion workspace and the duplicated page (e.g., "Purchase Order PDF Generator") <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   Click "Allow access" to connect the page with PDFoutput.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
2.  **Select Database and Template**: Once authenticated, the database and template elements will load <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   Select the database from the dropdown (e.g., "purchase order database") <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Select the specific template page (e.g., "template") <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   Assign a connection name (e.g., "purchase order") <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> and click "Next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
3.  **Map Properties**: The system automatically matches most properties from your Notion database to the template placeholders <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Any unmatched properties (e.g., due to slight naming differences like spaces) will be highlighted <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
    *   Use the "Filter unmapped properties" option to easily identify and manually map these <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   Ensure all Notion properties (database columns) are correctly mapped to their corresponding template elements <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## [[exporting_and_downloading_pdf_documents | Exporting and Downloading]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>

1.  **Initiate Export**: Click the "Export" button <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
2.  **Tracking Status**: A "PDF Status" column is automatically added to your Notion database, which will be ticked once a PDF document for that row has been generated <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. To regenerate a document, ensure its checkbox in this column is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download**: Once the export is successful, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. All generated documents can then be downloaded in bulk into an output folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Managing Connections and Subscriptions

*   **Connections**: After [[exporting_and_downloading_generated_pdf_documents | generating PDF documents]], PDFoutput.com stores the connection settings, allowing you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Upgrading Subscription**: Free plans will include watermarks on generated PDFs <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Upgrading to a paid plan removes these watermarks <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Settings**: Configure page format options for the PDF output <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback and Help**: Options are available for sending feedback on issues and accessing a setup demonstration video for troubleshooting <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.