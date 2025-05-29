---
title: Creating PDF documents with Notion templates
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_pdf_output_templates_in_notion | utilize a Notion page and template]] to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents]] using the PDFOutput tool. The process is illustrated with an invoice template, showing how to [[generating_professional_invoice_pdfs_using_notion | generate invoice PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Getting Started with PDFOutput

To begin, navigate to PDFOutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, you will see an interface from which you can proceed to the "Templates" section <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Accessing and Downloading Templates

Within the "Templates" section, a list of various templates compatible with PDFOutput is displayed <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For this demonstration, the "Invoices" template is used <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Clicking the "Download" link next to a template opens a new page displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Understanding the Notion Template and Database

The Notion template uses placeholder text elements enclosed in curly braces (e.g., `{client name}`, `{invoice number}`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. These placeholders will be replaced with data from a connected database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The corresponding Notion database contains columns (e.g., "Invoice Number", "Date", "Client Name") that match these placeholder names <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a record (e.g., an invoice) that will populate the template elements <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Duplicating the Template to Your Notion Workspace

To begin [[creating_templates_and_databases_in_notion_for_pdf_generation | your own PDF generation setup]], click "Start with this template" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This prompts you to duplicate the template to your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired workspace and click "Add to Private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Once duplicated, the template and its database will appear in your Notion account <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## [[integrating_notion_with_pdf_output_for_document_creation | Integrating Notion with PDF Output]]

After duplicating the template, return to PDFOutput and go to the "Settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, you will add the specific template you just duplicated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

1.  Click the option to add a template <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
2.  Select your Notion workspace from the list, ensuring it's the same one where you duplicated the template <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  Click "Select Pages" and choose the "Invoice Generator Template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Click "Allow Access" to authenticate and add the template to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

PDFOutput will then sync the database and template elements <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Customizing Templates and Databases

Both the Notion template and the database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It is crucial that any placeholder text elements in the template (those in curly braces) have exact matching column names in the Notion database to ensure proper mapping and output generation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Mapping Notion Properties for PDF Generation

Once the template is connected, select the database and template within PDFOutput <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Give the generation a name <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Clicking "Next" will start syncing the elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

On the mapping screen, Notion properties (database column names) are listed on the left and are automatically mapped to corresponding elements from the template <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements are indicated by a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If an element is not mapped, you can click on it and search for the correct property to link <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Sorting, searching, and filtering options (e.g., filtering for unmapped properties) are available <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## [[exporting_pdf_documents_from_notion | Generating and Exporting PDFs]]

After mapping, click "Export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. In your Notion database, a "PDF Status" column will automatically update, getting checked as each document is generated <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Once successful, you can "Preview Sample" to see a single generated PDF <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, or click "Download All" to [[generating_pdfs_in_bulk_with_notion | download all generated PDF outputs]] (e.g., all invoices from the database) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Considerations for Generation

*   Before regenerating documents, ensure the "PDF Status" column in Notion for the relevant rows is unchecked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   [[using_pdf_output_tool_with_notion | PDFs generated]] on a free plan will include a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Additional Features

*   **Connections:** After an initial export, your connection settings (database and template selections) are saved <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. You can revisit "Connections" to quickly load the same setup without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Help Section:** The "Help" section provides a detailed guide on setting up the process for the first time <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Feedback:** You can send feedback or messages via the provided feedback option <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. For questions or assistance, contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.