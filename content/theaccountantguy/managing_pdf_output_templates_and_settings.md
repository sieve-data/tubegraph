---
title: Managing PDF Output templates and settings
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to manage templates and settings within PDF Output to generate documents, using payment receipts as an example <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Accessing and Downloading Templates

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. From the interface, click on "Templates" to view a list of available templates <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. You can search for a specific document using the search option, or utilize filter and sorting options <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

For generating payment receipts, select the "payment receipts PDF generator" and click its download link <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This action opens a new page displaying both the payment receipts PDF generator database and its associated template <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Understanding Templates and Databases

The payment receipt template contains predefined elements for generating the PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, and `{amount paid}`, are placeholder text elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced by corresponding data from your Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

It is crucial that the exact naming convention of these placeholder elements in the template matches the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This ensures proper synchronization and accurate PDF generation <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Duplicating Templates to Notion

If a template is not yet published to the Notion Gallery, you will see a "Duplicate" option <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Click this to duplicate the template to your desired Notion workspace <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. If it is published, click "Start with this template" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Duplicating the template to a Notion workspace is necessary to use it with PDF Output <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Adding Templates to PDF Output

After duplicating the template to Notion, navigate to the "Settings" section in PDF Output <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. You will be prompted to choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Select the correct workspace, click "Select pages," and then "Allow access" to enable PDF Output to read your template and database elements <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## [[customizing_templates_for_pdf_document_generation | Customizing Templates]]

PDF Output templates are [[customizable_pdf_templates | customizable]] to fit your specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can modify elements like text formatting (e.g., making text bold) and spacing directly within the Notion template <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. When [[creating_and_utilizing_pdf_templates | creating and utilizing PDF templates]], ensure that all placeholder elements you intend to replace with database information remain within curly braces for proper syncing <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Mapping Database Properties to Template Elements

Once your template and database are loaded in PDF Output, the system will automatically map the Notion database properties (columns) to the corresponding template elements, provided their names match <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

If any elements are mismatched or unmapped, you can manually select the correct property by clicking on the mismatched field and searching for the appropriate element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This mapping interface also includes filter, search, and sorting options for easier management of properties <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Generating PDFs

After all elements are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. PDF Output will automatically add a "PDF Status" column to your Notion database to track which rows have been generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Once generation is complete, the "PDF Status" will update <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

You can then [[using_pdf_output_for_document_export_and_preview | preview a sample]] of the generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> or click "Download all" to get all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a row in your Notion database, with all elements placed correctly <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## [[managing_connections_and_templates_in_pdf_output | Managing Connections and Templates]]

The "Connections" section in PDF Output stores your past connections, allowing you to quickly load previously configured databases and templates without needing to manually add them each time <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This simplifies the process for generating documents repeatedly from the same setup <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## [[managing_pdfoutput_settings_and_subscriptions | PDF Output Settings and Subscriptions]]

Under "Settings," you can find options to:
*   Change the page format of your PDFs <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   Send feedback directly to the developer <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   Access a help section with a demonstration video for setup guidance <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

If you are on the free plan, generated PDFs will include a PDF Output watermark <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. You can upgrade your subscription to remove this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.