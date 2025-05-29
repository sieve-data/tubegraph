---
title: Generating payment receipts PDF using Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_payment_receipts_pdf_in_bulk | generate payment receipt documents]] using a [[using_notion_with_pdf_output | Notion database]] and a Notion template with PDF Output.

## Accessing PDF Output and Templates

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. From the interface, click on "Templates" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This will open a new page listing all available templates <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For payment receipts, you can use the search option to find "payment receipts PDF generator" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. There are also filter and sorting options available <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

Once found, click the "download link" next to the "payment receipts PDF generator" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This opens a new page displaying both the payment receipts database and template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Understanding the Notion Template and Database

The payment receipt template contains predefined elements for PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, and `{amount paid}`, are placeholder text <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced by corresponding data from your Notion database columns <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. It's crucial that the placeholder names in the template exactly match the column names in your Notion database for proper syncing and [[pdf_document_generation_from_notion | PDF document generation]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Duplicating the Template to Notion

If the template isn't yet published to the Notion Gallery, you'll see a "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If it is published, click "start with this template" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. In either case, you'll be prompted to choose a Notion workspace to duplicate the template into <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. This step is necessary to integrate it with PDF Output <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Connecting Notion to PDF Output

After duplicating the template to your Notion workspace, navigate to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Then, click "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. You'll need to select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Select the "payment receipts PDF generator" file and click "allow access" <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. PDF Output will then read the template and database elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Customizing the Template

The entire template is customizable to your specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can format text (e.g., make elements bold), add spacing, or make other design changes <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. The key is to ensure that any placeholder elements intended to be replaced from your database remain inside curly braces and that their names precisely match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This ensures proper syncing and error-free PDF generation <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Mapping Database Properties to Template Elements

In PDF Output, select the "payment receipts database" from the dropdown, and correspondingly, select the "payment receipt template" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Give the export a name, such as "payment receipt", and click "next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

PDF Output will automatically map the Notion database properties (columns) to the template elements if their names match correctly <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. If there are any mismatches, you can manually select the correct element from a search bar <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The interface also provides filter, search, and sorting options to help manage properties <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Generating the PDFs

Once everything is set up, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. PDF Output will automatically add a "PDF status" column to your Notion database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. As each row's PDF is generated, its corresponding "PDF status" will be ticked <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

After successful export, you can click "Preview sample" to view a single generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, or "Download all" to get all generated files in a zip archive <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a row in your Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional PDF Output Features

*   **Connections**: In the "Connection" section, you can view past connections, allowing you to quickly load previously used databases and templates without manual setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Multiple Templates**: You can select multiple templates if needed <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermark**: On the free plan, generated PDFs will include a PDF Output watermark <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Page Format**: Under "Settings", you can change the page format of the PDF output <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Feedback**: A feedback option is available to send messages directly to support <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help**: The "Help" section contains a demonstration video to guide you through the setup process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Contact

For any questions, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.