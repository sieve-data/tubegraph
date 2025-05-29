---
title: Generating purchase order PDFs using Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[generating_pdf_documents_for_purchase_orders | generate purchase order PDF documents]] using a Notion database and template with PDF output.com <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDF Output

1.  **Log in to PDF output.com**: The first step is to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The interface will display fields for a connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
2.  **Select a Predefined Template**:
    *   Navigate to the "Templates" section in the sidebar <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   This section lists predefined templates for generating PDF documents, including invoices, payment receipts, and [[generating_pdf_documents_for_purchase_orders | purchase orders]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   Use the search icon to quickly find the "Purchase Order" template <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   Click the "Download" link next to the desired template to open a new page <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Understanding the Notion Template and Database

The page opened after downloading the template serves as the [[generating_pdf_documents_for_purchase_orders | purchase order PDF generator]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It contains both a database and a template that will be connected to PDF output <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

*   **Template Structure**: The Notion template defines elements such as purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Key elements meant for replacement are enclosed in curly braces (e.g., `{Purchase Order Number}`, `{Date}`, `{Supplier Name}`, `{Buyer Name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Database Structure**: The Notion database contains the actual data, with fields like supplier name, buyer name, date, and purchase order number, corresponding to the template's placeholders <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. PDF documents will be generated for each row of information in the database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Customization**: Both the template and the database are fully customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Ensure that values intended for dynamic replacement in the template are placed inside curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, and that the names in the template exactly match the column names in the database to ensure proper linking <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Connecting Notion to PDF Output

1.  **Duplicate the Notion Page**:
    *   On the [[generating_pdf_documents_for_purchase_orders | purchase order PDF generator]] page in Notion, click "Duplicate" (or "Start with this template" if published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   Select your Notion workspace to duplicate the page <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
2.  **Configure PDF Output Settings**:
    *   Return to PDF output.com and go to "Settings" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Choose your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Click "Click here to add templates" to connect your Notion pages <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Select the correct Notion workspace and then the "Purchase Order PDF Generator" page <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   Click "Allow Access" to establish the connection <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  **Select Database and Template**:
    *   Once authenticated, PDF output will load the available Notion databases and templates <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   From the dropdowns, select the "Purchase Order database" and the corresponding "Template page" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Give your connection a name, such as "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Mapping Properties and Exporting PDFs

1.  **Map Database Properties to Template Elements**:
    *   PDF output will attempt to automatically match Notion database properties (left side) with template elements (right side) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   If any properties are unmatched (e.g., due to a space difference in names), you can manually map them <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Use the "Filter unmapped properties" option to identify these <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   Ensure all elements are correctly matched <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
2.  **Export the Documents**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   During export, a "PDF Status" column will be automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. A tick in this column indicates that the PDF document has been generated <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   Once successful, you can "Preview Sample" of the generated PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Click "Download All Documents" to retrieve the generated PDFs, which will be saved in an "output" folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each PDF will correspond to a row in your Notion database <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Additional Features and Support

*   **Connections Tab**: After [[generating_pdf_documents_using_notion | generating a PDF document]], a connection is saved <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This allows you to regenerate documents directly by clicking the connection, without re-entering database and page information <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Templates Tab**: Displays available templates (already discussed) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Upgrade**: Free plans will have a watermark on generated PDFs, while paid plans will not <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Define your default page format for PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This is also where you add duplicated Notion templates to your workspace <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **Feedback**: Use the feedback option if you encounter any issues <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help Section**: Provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or other PDF document solutions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.