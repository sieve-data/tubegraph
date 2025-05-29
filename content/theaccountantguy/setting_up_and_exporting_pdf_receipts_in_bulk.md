---
title: Setting up and exporting PDF receipts in bulk
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[payment_receipt_pdf_generation | generate payment receipt PDF documents]] in [[bulk_export_of_pdf_documents | bulk]] using a Notion database and a Notion template with the PDF Output tool <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, ideal for [[generating_pdf_documents_for_business_purposes | business purposes]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Accessing PDF Output and Templates

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. From the interface, click on "Templates" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This will open a new page listing all available templates <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. You can search for specific documents using the search option <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, or utilize the filter and sorting options <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. For payment receipts, select the "Payment Receipts PDF Generator" template <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Understanding the Payment Receipt Template

Once you select the template, click on the download link next to it <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This opens a new page showcasing the payment receipts PDF generator page, which includes both the Notion database and the template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The template predefines elements for PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Elements enclosed in curly braces, such as `receipt number`, `receipt date`, `customer name`, and `amount paid`, are placeholder text elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced with corresponding data from the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is crucial that the placeholder names in the template exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Duplicating the Template to Notion

If the template is not yet published to the Notion Gallery, you'll see a "start with this template" option <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Otherwise, click on the "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. You will be prompted to choose a Notion workspace to duplicate the template to <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Duplicating the template to your Notion workspace is necessary to use it with PDF Output <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Connecting the Template to PDF Output

After duplicating the template, go back to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Then, click "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Click "Select Pages" and then "Allow Access" for PDF Output to read the template and database elements <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

Once authentication is successful, give PDF Output a few seconds to load the database and template elements <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Customizing Templates

The entire template is customizable to your specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can make elements bold, add spacing, or change the layout <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. However, ensure that all placeholder elements intended for replacement from the database are enclosed in curly braces for proper syncing and output generation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The naming convention of placeholder elements must exactly match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Mapping Database Fields

In PDF Output, refresh the screen to properly fetch all elements <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Select the "Payment Receipts Database" from the dropdown <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, and correspondingly select the "Payment Receipt Template" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Give it a name, such as "Payment Receipt" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

The tool will automatically map Notion properties (database elements) to the template elements if the names match correctly <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. If any elements are mismatched, you can manually search for and select the correct element to map <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This mapping view also provides filter, search, and sorting options <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Exporting and Downloading Receipts

Once everything is set up, click on "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. PDF Output will automatically add a "PDF Status" column to your Notion database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This column denotes which rows have been generated; once a PDF is created for a row, it will be ticked <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

After a successful export, you can click "Preview Sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To [[exporting_bulk_pdfs_with_pdf_output_tool | download all generated files]], click "Download All" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a specific row in the Notion database, populating all elements in their correct places <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This enables [[bulk_exporting_and_downloading_generated_pdf_files | bulk exporting and downloading generated PDF files]] <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>, similar to [[exporting_completed_pdf_invoices | exporting completed PDF invoices]] or [[generating_sales_receipts_pdf_documents_using_online_tools | generating sales receipts PDF documents using online tools]].

## Managing Connections

Under the "Connection" section in PDF Output, you can view all past connections <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Clicking on a previous connection (e.g., "Payment Receipt") will automatically load the associated database and template, allowing you to quickly generate files again without manual setup <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This simplifies the process for [[exporting_and_managing_pdf_documents_for_business | exporting and managing PDF documents for business]].

## Additional Features and Considerations

*   **Watermarks**: Free plans will include a PDF Output watermark on generated templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Page Format**: In the settings, you can change the page format of your PDFs <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Feedback**: A feedback option is available to send messages directly to support for assistance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section**: The help section contains a demonstration video to guide you through the setup process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.