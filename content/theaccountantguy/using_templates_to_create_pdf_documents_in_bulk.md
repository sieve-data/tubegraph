---
title: Using templates to create PDF documents in bulk
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate payment receipt PDF documents in bulk using a Notion database and a Notion template, leveraging the [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] tool <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process can be applied to generate various types of bulk documents <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with [[using_pdfoutputcom_for_bulk_pdf_generation | PDF output.com]]

To begin, log in to [[using_pdfoutputcom_for_bulk_pdf_generation | PDF output.com]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Accessing Templates

Once logged in, navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This page lists all available templates for [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

> [!TIP] Search and Filter Options
> You can quickly find a specific template using the search option <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Additionally, filter and sorting options are available to help locate the desired template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

For payment receipts, select the "payment receipts PDF generator" template <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Click the download link next to it to open a new page displaying the database and template <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Understanding the Template and Database

The system utilizes two main components: a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

*   **Template:** This is a pre-defined document (e.g., a payment receipt form) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Database:** This holds all the variable information (e.g., customer name, amount paid, receipt date) that will populate the template <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Within the template, elements enclosed in curly braces (e.g., `{{receipt number}}`, `{{customer name}}`, `{{amount paid}}`) are placeholder text elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be automatically replaced with corresponding data from the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It's crucial that the placeholder names in the template exactly match the column names in your database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

> [!INFO] Customizing Templates
> You can [[customizing_templates_for_pdf_generation | customize templates for PDF generation]] by making elements bold, adding spacing, or rearranging content to fit your requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Ensure that any placeholder elements intended for replacement from the database are kept within curly braces <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Duplicating the Template to Notion

To use the template, it must be duplicated to your Notion workspace <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

1.  Click the "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  Choose the Notion workspace where you want to duplicate the template <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  Click "add to private" or "start with this template" if it's published to the Notion Gallery <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Once duplicated, the template file will appear in your Notion workspace <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Keep both the Notion database and the Notion template open for the next steps <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Connecting Notion to [[using_pdf_output_tool_for_efficient_document_creation | PDF output]]

After duplicating the template, you need to connect your Notion workspace to [[using_pdf_output_tool_for_efficient_document_creation | PDF output]].

1.  Go to the "Settings" section within [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
4.  Click "select pages" and then "allow access" for the "payment receipts PDF generator" file <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This allows [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] to read your template and database elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Mapping Database Properties to Template Elements

After successful authentication, [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] will load the database and template elements <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

1.  From the drop-down menus, select your payment receipts database and corresponding payment receipt template <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Give your export a name (e.g., "payment receipt") <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
3.  The tool will automatically map the Notion database properties (columns) to the template elements if the names match correctly <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
4.  If any elements are mismatched, you can manually search for and select the correct corresponding element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
5.  You can filter to see unmapped properties, search for specific elements, or sort the properties for easier mapping <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## [[utilizing_pdf_output_for_bulk_pdf_generation | Generating Single and Bulk PDF Documents]]

Once everything is set up and mapped correctly, you can generate your PDFs.

1.  Click the "Export" button <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
2.  [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] will automatically add a "PDF status" column to your Notion database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. As each row's PDF is generated, its status will be ticked <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
3.  A success message will appear in [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
4.  You can preview a sample PDF file <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> or click "Download all" to get all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
5.  Each generated PDF corresponds to a specific row in your Notion database, with all placeholder elements populated correctly <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features

*   **Connections:** In the "Connections" section, you can view past connections and quickly reload a previously configured database and template for future [[using_pdfoutput_for_bulk_document_generation | bulk document generation]] without manual setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Templates:** You can select and manage multiple templates <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Page Format:** Under "Settings," you can change the PDF page format (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Watermark:** Free plans include a [[using_pdf_output_tool_for_efficient_document_creation | PDF output]] watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Feedback:** A feedback option is available to send messages directly to support <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section:** Find demonstration videos to assist with setup and usage <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

For any questions, you can reach out via email <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.