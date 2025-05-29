---
title: Managing PDF Export and Connections in Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate payment receipt PDF documents using a Notion database and template, specifically leveraging the PDFOutput.com service <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It covers the process from logging in to generating and managing PDF exports.

## Getting Started with PDFOutput.com

To begin, log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The interface will display a list of available templates <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Accessing Templates

You can navigate to the "Templates" section by clicking the corresponding option on the screen <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Templates can be searched by name or filtered and sorted <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For payment receipts, select the "payment receipts PDF generator" and download its link <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This download opens a new page displaying both the payment receipts database and the template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Duplicating Templates to Notion

If the template is not yet published to the Notion Gallery, you will see a "start with this template" option or a "duplicate" option <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Click "duplicate" to add the template to your chosen Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Duplicating the template to a Notion workspace is essential for [[using_pdf_output_with_notion_templates | using PDF Output with Notion templates]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Preparing Your Notion Template and Database

The payment receipt template contains predefined elements for PDF output <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Understanding Placeholders

Elements enclosed in curly braces, such as `receipt number`, `receipt date`, `customer name`, and `customer email`, are placeholder texts <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These placeholders are replaced by corresponding information from your Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

For instance, the `customer name` placeholder will be populated from the `customer name` column in your Notion database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It is crucial that the exact information in the curly braces matches the corresponding column name in the database <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Customizing Your Template

The template is fully [[customizing_pdf_documents_using_notion_database_elements | customizable]] to fit your specific requirements <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. You can modify text, add spacing, or make elements bold <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. When [[setting_up_notion_database_for_pdf_document_templates | setting up Notion database for PDF document templates]], ensure that any placeholder elements intended for replacement from the database are correctly placed inside curly braces for proper syncing and error-free output <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The exact naming convention between the placeholder elements and database columns must match <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## [[connecting_notion_database_and_templates_to_pdf_output | Connecting Notion Database and Templates to PDFOutput]]

After duplicating the template to Notion, navigate to the "Settings" section within PDFOutput <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Adding Templates to PDFOutput

Click "click here to add templates" to integrate your Notion template with PDFOutput <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Grant access to allow PDFOutput to read your template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Successful authentication will lead you back to PDFOutput, where it will load the database and template elements <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Mapping Notion Properties to Template Elements

Once loaded, select your database (e.g., "payment receipts database") and its corresponding template (e.g., "payment receipt template") from the dropdown menus <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Give the connection a name and proceed <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

PDFOutput will then load and automatically map Notion database properties (on the left) to the template elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Automatic mapping occurs when names are correctly matched <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. If any elements are mismatched, you can manually search for and select the correct mapping <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This view also includes filter, search, and sort options for properties <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

> [!TIP]
> Ensure the exact naming convention for your Notion database columns matches the placeholder elements in your template for seamless automatic mapping <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Generating PDFs

With everything set up, you can now generate your PDF documents.

### Exporting Documents

Click "Export" to begin the [[generating_pdfs_from_notion_using_pdfoutput | generating PDFs from Notion using PDFOutput]] process <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. A "PDF status" column will automatically be added to your Notion database, denoting which rows need to be generated <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. As each row's PDF is generated, its corresponding checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Reviewing Generated PDFs

Upon successful export, you can click "Preview sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. You can also click "Download all" to download all generated files <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated file corresponds to a specific row in your Notion database, with all elements placed correctly <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Managing Connections and Settings

PDFOutput provides options to manage past connections and customize general settings.

### Accessing Past Connections

In the "Connection" section, you can view all previously created connections <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Clicking on a past connection will automatically load the associated database and template, allowing you to quickly resume [[integration_of_notion_with_pdf_generation | integration of Notion with PDF generation]] without manually adding them each time <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. You can also select multiple templates under the template section <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Subscription and Watermarks

Users on the free plan will notice a PDFOutput watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. To remove the watermark, you can upgrade to a paid subscription plan <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Page Format and Feedback

Under "Settings," you can change the page format of your PDFs <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. There is also a feedback option to send messages directly to the service provider <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The "Help" section provides a demonstration video to guide you through the setup process <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. For further assistance, you can reach out via email to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.