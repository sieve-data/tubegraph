---
title: Generating payment receipts in PDF using Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate PDF payment receipt documents using a Notion database and a Notion template with PDFOutput.com <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Step 1: Access PDFOutput.com

First, log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Once logged in, you'll see the interface and can click on "Templates" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This will open a new page listing available templates for [[generating_pdf_documents_with_notion_and_pdfoutput | PDF generation with PDFOutput]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

You can search for specific templates, such as "payment receipts PDF generator," using the search option <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, or use the filter and sorting options <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Step 2: Download and Duplicate the Template

Select the "payment receipts PDF generator" template and click the "Download" link next to it <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This will open a new page featuring the payment receipts PDF generator page, including the database and template <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

If the template isn't published to the Notion Gallery, you'll see a "Start with this template" option <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Otherwise, click the "Duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. You will then be prompted to choose which Notion workspace you want to duplicate the template to <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Duplicate the template to your Notion workspace to enable its use with PDFOutput <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Step 3: Understand the Notion Template and Database

After duplicating, you will have both the payment receipt template and the corresponding database in your Notion workspace <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The template contains predefined elements for generating the PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Elements enclosed in curly braces, like `{receipt number}`, `{receipt date}`, `{customer name}`, and `{amount paid}`, are placeholder text elements <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders will be replaced with corresponding data from columns in your Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

> **Important**: Ensure that the exact naming convention of the placeholder text in the template matches the corresponding column names in your Notion database for proper syncing <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

You can customize the template's format, such as making text bold or adjusting spacing, to meet your specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Just remember to keep placeholder elements within curly braces <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Step 4: Connect Notion to PDFOutput

Return to PDFOutput.com and navigate to "Settings" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Click "Click here to add templates" to add the Notion template to PDFOutput <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

You'll need to select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Click "Select pages" and choose the "payment receipts PDF generator" file <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Then, click "Allow access" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. PDFOutput will authenticate and begin reading your template and database elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Step 5: Map Database Properties to Template Elements

Once authentication is successful, you will be taken back to PDFOutput <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Refresh the screen to ensure all elements are properly fetched <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

1.  Select the "payment receipts database" from the first dropdown <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  Select the "payment receipt template" from the second dropdown <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
3.  Give your export a name, e.g., "payment receipt" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

PDFOutput will automatically map the Notion properties (database columns) to the template elements if the names match correctly <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. If any element is mismatched, you can manually select the correct corresponding element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The mapping view also offers filter, search, and sorting options <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Step 6: Generate the PDF Receipts

With everything set up, click "Export" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

PDFOutput will add a "PDF Status" column to your Notion database <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This column will be ticked for each row as its corresponding PDF is generated <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

Once the export is successful <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, you can:
*   Click "Preview sample" to view a sample of the generated PDF receipt <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Click "Download all" to download all the generated PDF files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each downloaded file corresponds to a row in your Notion database <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features and Tips

*   **Connections**: The "Connections" section in PDFOutput allows you to quickly load previously configured database and template pairs, eliminating the need to manually add them each time <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Watermark**: The free plan will include a PDFOutput watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Page Format**: In "Settings," you can change the PDF page format (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Feedback**: A feedback option is available to send messages directly to the support team <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help Section**: The help section provides a demonstration video to guide you through the setup process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, specifically on [[generating_pdf_documents_from_notion | Generating PDF documents from Notion]].

For further assistance, you can reach out via email <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.