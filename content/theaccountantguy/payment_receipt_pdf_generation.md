---
title: Payment receipt PDF generation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article discusses how to [[generating_payment_receipts_pdf_using_notion | generate payment receipt PDF documents]] in [[bulk_pdf_document_generation | bulk]] using a Notion template and database with the help of PDFoutput.com <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Components for Generation

To generate payment receipts, two main components are utilized:

### 1. Payment Receipt Template
The payment receipt template contains specific elements enclosed in curly braces (e.g., `{receipt number}`, `{receipt date}`) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These elements act as placeholders that will be replaced by data from a Notion database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### 2. Notion Database
A Notion database is used to store the information needed for each receipt <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Each column in the database corresponds to an element in the template, ensuring that the data can be accurately mapped and used to generate individual PDF documents for each row of information <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For example, if the template has `company website` in curly braces, the database should have a column named "company website" <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Exact naming conventions (including spaces and capitalization) between the template elements and database columns are crucial for automatic mapping <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Step-by-Step Generation Process with PDF Output

The process involves using the online tool PDFoutput.com to connect the Notion template and database and generate PDF documents in [[bulk_pdf_document_generation | bulk]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

1.  **Access PDFoutput.com**: Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  **Duplicate Template and Database**:
    *   From the "Templates" section on PDF Output, search for "payment receipts" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click on the template link and database link to open them in new windows <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Duplicate both the payment receipt template and its corresponding database to your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  **Connect Notion to PDF Output**:
    *   On PDFoutput.com, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Select your Notion workspace (e.g., "accountant guy workspace") and then select both the duplicated template and database pages to grant access <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   A successful authentication will connect the Notion database and template to PDF Output <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
4.  **Name Connection and Map Properties**:
    *   Provide a connection name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   PDF Output will automatically populate and map database properties to the template elements <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   If any elements are not automatically mapped due to naming mismatches, manually map them by searching for the correct database property <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   Filter, search, and sorting options are available to manage properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
5.  **Generate and Download PDFs**:
    *   Once all properties are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   The system will process each row in the database to generate a corresponding PDF document <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. For example, if there are three rows, three PDF documents will be generated <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   You can preview a sample document to check the output <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   Click "Download all documents" to receive a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Additional Features and Settings

PDF Output offers several features to streamline the [[bulk_pdf_document_generation | bulk PDF document generation]] process:

*   **Connections**: View a list of previously created connections to quickly reload database and template settings for subsequent generations <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. If the database or template doesn't load immediately, click refresh <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Templates**: Access a variety of predefined templates, including options for [[generating_pdf_invoices_using_pdf_output_service | invoices]] and other use cases <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade**: Free plans include a "Made with PDF Output" watermark, which can be removed by upgrading to a paid subscription for higher usage limits and no watermarks <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Settings**: Define page format (default is A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. You can also add more templates and databases via the settings <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback**: A dedicated window allows users to provide feedback or ask questions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Custom Templates**: A help section explains how to use custom PDF documents without relying on predefined templates and databases <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

> [!tip] Naming Convention
> Ensure that elements placed inside curly braces `{}` in your Notion template match the exact naming (including spaces and capitalization) of the corresponding columns in your Notion database to enable automatic mapping <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.