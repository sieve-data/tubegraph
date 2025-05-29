---
title: Steps for downloading and exporting PDFs
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide outlines the steps to generate and [[generating_and_downloading_pdf_documents | download PDF documents]] from a Notion database using PDF Output, focusing on a purchase order contract template example <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started

1.  **Log in to PDF Output**: Begin by logging into PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
2.  **Select a Template**:
    *   Navigate to the "Templates" section in the sidebar <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   Browse or search for desired predefined templates, such as invoices, payment receipts, or purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   Click the "download" link next to the template you wish to use, which opens a new page specifically for that PDF generator <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Understanding Template and Database Structure

Before proceeding, it's essential to understand how the template and database interact:

*   **Template Placeholders**: The template contains elements enclosed in curly braces, such as `{purchase order number}`, `{date}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. These act as placeholders for data <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Database Values**: A corresponding Notion database holds the actual data for these fields <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row in the database represents a set of data for a single PDF document <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Customization**: Both the template and database are [[customizing_and_exporting_pdf_documents | customizable]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Ensure that the names of the database properties exactly match the placeholder names in the template (case-sensitive and no extra spaces or commas) for proper linking <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Connecting Notion to PDF Output

1.  **Duplicate Template to Notion**:
    *   On the PDF generator page, click "Duplicate" (or "Start with this template" if published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   Select your Notion workspace to duplicate the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This adds the template and its associated database to your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
2.  **Connect Templates in PDF Output**:
    *   Return to PDF Output and go to "Settings" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   You can select the page format for your PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Select your Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Choose the specific template (e.g., "purchase order PDF generator") from the list and click "Allow access" <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This step connects your Notion page to PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  **Select Database and Template**:
    *   Once authenticated, choose your Notion database (e.g., "purchase order database") from the dropdown list <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Then, select the Notion template page (not the generator page) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   Give your connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Mapping Properties and Exporting

1.  **Match Properties**:
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. PDF Output will attempt to automatically match Notion database properties (on the left) with template elements (on the right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   If any properties are unmatched (e.g., due to a space difference in names), use the "Filter unmapped properties" option to identify them <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. Manually select the correct matching property for any unmapped items <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
2.  **[[generating_and_exporting_pdf_documents_for_business | Exporting and Managing PDF Documents]]**:
    *   Once all properties are mapped, click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
    *   In your Notion database, a "PDF Status" column will be automatically added and ticked as each PDF is generated <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. If you need to regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   After successful export, you can "Preview sample" to see a single [[previewing_and_downloading_generated_pdf_files | generated PDF file]] <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Click "Download all documents" to get a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Each PDF will correspond to a row in your database <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Additional Features

*   **Connections**: PDF Output saves your configurations as "connections," allowing you to quickly regenerate documents without re-filling all database and page details <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade**: Free plans include a watermark on generated templates. Paid plans remove the watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Customize page format and manage connected templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback/Help**: Options are available for providing feedback or viewing setup videos for troubleshooting <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.