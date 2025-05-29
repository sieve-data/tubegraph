---
title: Generating payment receipt PDFs with Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_pdf_documents_using_notion | generate payment receipt documents]] using a Notion database and a Notion template, in conjunction with PDF output.com <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDF output.com

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Finding and Downloading Templates

Upon logging in, navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Here, you'll find a list of available templates <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For payment receipts, specifically look for and click on the "Payment Receipts PDF Generator" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. You can use the search option to find specific templates <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, and there are also filter and sorting options available <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

Click the download link next to the "Payment Receipts PDF Generator" to open a new page displaying the payment receipt's Notion database and template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Understanding the Notion Template and Database

The system utilizes a Notion template and a Notion database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Template Structure

The payment receipt template has predefined elements for the PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, and `{amount paid}`, are placeholder texts <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced by corresponding data from your Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Database Column Names

The information in the curly braces of the template must exactly match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For instance, if the template has `{customer name}`, your database must have a column named "customer name" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This ensures proper syncing and error-free PDF generation <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Duplicating the Template to Notion

If the template isn't yet published to the Notion Gallery, click the "Duplicate" option <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This will prompt you to select a Notion workspace where you want to duplicate the template <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Duplicating the template to your Notion workspace is essential for use with PDF output.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Connecting Notion to PDF output.com

After duplicating the template to your Notion workspace, go to the "Settings" section in PDF output.com <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

1.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
3.  Select the specific "Payment Receipts PDF Generator" file you added <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
4.  Click "Allow access" to enable PDF output.com to read your template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Mapping Database Properties to Template Elements

Once authentication is successful, PDF output.com will load your database and template elements <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

1.  From the dropdown menus, select your "Payment Receipts Database" and the "Payment Receipt Template" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Give your export a name, e.g., "payment receipt" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
3.  Click "Next" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

PDF output.com will automatically map the Notion database properties (columns) to the template elements if the naming conventions match correctly <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. If any elements are mismatched, you can manually search for and select the correct mapping <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Generating the PDF

Once everything is set up and mapped correctly, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

PDF output.com will automatically add a "PDF Status" column to your Notion database <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. As each row's PDF is generated, the corresponding checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### Viewing and Downloading Generated PDFs

After a successful export <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, you can:
*   Click "Preview sample" to see a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Click "Download all" to download all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a specific row in your Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Customizing Your Template

The provided template is fully customizable <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can:
*   Make elements bold <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Adjust spacing <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Change the page format in the settings <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

[!CAUTION] Ensure that any placeholder elements you want to replace from your database remain inside curly braces to ensure proper syncing <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Remember to keep the exact naming conventions between your template's placeholder elements and your Notion database column names <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Additional Features of PDF output.com

*   **Connections**: The "Connection" section shows all past connections, allowing you to quickly reload your database and template without re-adding them manually <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Multiple Templates**: You can select multiple templates if needed <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Free Plan Limitations**: The free plan includes a watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Feedback**: A feedback option allows you to send messages directly to the support team <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section**: The "Help" section provides a demonstration video to assist with setup for [[generating_pdf_documents_using_notion | generating PDF documents]] without issues <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

For any questions, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.