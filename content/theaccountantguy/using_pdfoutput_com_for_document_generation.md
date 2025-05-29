---
title: Using PDFoutput com for document generation
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

[[using_pdfoutput_for_document_generation | PDFOutput.com]] is a service that allows users to generate PDF documents by utilizing Notion pages and templates <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves connecting a Notion database to a Notion template, where placeholder text in the template is replaced with data from the database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A common use case demonstrated is [[using_pdf_output_for_invoice_generation | invoice generation]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Accessing and Navigating PDFOutput.com

To begin, users need to log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Upon logging in, an interface appears <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The primary section for document generation is the "Templates" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Template Selection and Download

The "Templates" section displays a list of pre-created templates compatible with PDFOutput <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For [[using_pdf_output_for_invoice_generation | invoice generation]], a specific invoice template can be downloaded <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Users can also utilize search, sorting, or filtering options to locate specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Clicking on a template's download link opens a new page displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Understanding Templates and Databases

A Notion template typically includes elements like client name, company address, invoice number, date, and terms, which are enclosed in curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These are placeholder texts that will be populated by data from a connected database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

The Notion database contains corresponding columns (e.g., "invoice number," "date," "client name") that match the placeholder elements in the template <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a unique set of data for a document <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. The naming convention of placeholder text in the template must exactly match the column names in the database for proper data mapping <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## [[setting_up_and_configuring_pdfoutput | Setting Up and Configuring PDFOutput]]

### Duplicating the Template to Notion

To start, users click the "Start with this template" option on PDFOutput.com, which prompts them to duplicate the template to their Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. After selecting the desired Notion workspace, the template is added to the user's Notion account <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Connecting Notion to PDFOutput

Next, users return to PDFOutput.com and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Here, they select the specific template that was duplicated to Notion <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It's crucial to select the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. After selecting the template (e.g., "invoice generator template") and allowing access, PDFOutput authenticates and adds the template to its setup <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Customizing Templates and Databases

Both the Notion template and its associated database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Users can add, delete, or modify content within the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. The key rule is to ensure that any placeholder text elements (inside curly braces) in the template have exact matching column names in the Notion database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## [[using_pdf_outputcom_for_bulk_pdf_generation | Generating PDFs]]

After [[setting_up_and_configuring_pdfoutput | configuring PDFOutput]], users select the linked Notion database and the specific template (e.g., "professional invoice template") for generation <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. PDFOutput then syncs all elements from the database and template <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

The Notion properties (database column names) are automatically mapped to the corresponding template elements (placeholder texts) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements are typically indicated by a green bar <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If an element isn't mapped, users can manually search and select the correct corresponding property <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

Once mapping is complete, clicking "Export" initiates the document processing <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. A "PDF status" column in the Notion database will automatically update (check) as documents are generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## [[exporting_and_managing_pdfs_in_pdfoutput | Exporting and Managing PDFs]]

Upon successful export, a preview sample of a generated document can be viewed <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. To [[using_pdf_outputcom_for_bulk_pdf_creation | download all generated PDFs]], users can click "Download all" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This provides individual PDF outputs for each row of data in the database <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### Tips for Regeneration

For regenerating documents from scratch, ensure the "PDF status" row in the Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored during the generation process <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features and Considerations

*   **Other Templates**: PDFOutput offers various other templates besides invoices <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermarks**: On the free plan, generated PDFs will include a PDFOutput watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove watermarks, users need to upgrade to a paid subscription <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Feedback**: A feedback option is available for users to send messages or suggestions <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Connections**: After an initial export, connections are saved, allowing users to quickly load the same database and template without re-mapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Help and Support

The "Help" section within PDFOutput provides detailed instructions on the setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For further questions or feedback, users can contact `notionforuse@gmail.com` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.