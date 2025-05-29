---
title: Generating payment receipts PDF in bulk
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_payment_receipts_pdf_using_notion | generate payment receipt PDF documents in bulk]] using a Notion template and a Notion database with the PDFoutput.com tool <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Understanding the Notion Template and Database

To [[generating_payment_receipts_pdf_using_notion | generate payment receipt PDFs]], two main components are required: a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Payment Receipt Template
The payment receipt template contains specific elements enclosed within curly braces <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These elements act as placeholders that will be replaced with information from the database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Notion Database
The Notion database holds the information that will populate the template <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Each column in the database corresponds to an element in curly braces within the template, such as receipt number, receipt date, receipt time, and company website <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Each row in the database represents a separate document to be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It's crucial for the database columns to have the exact same naming convention, including spacing and capitalization, as the elements in the template to ensure automatic mapping <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## [[using_pdfoutput_tool_for_bulk_pdf_generation | Using PDFoutput.com for Bulk PDF Generation]]

The PDFoutput.com tool facilitates the [[generating_pdf_documents_for_business_needs | bulk generation of PDF documents]] from your Notion data <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Step-by-Step Process

1.  **Access PDFoutput.com**: Navigate to the website PDFoutput.com <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Login**: Log in to your account <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Find and Duplicate Templates**:
    *   After logging in, go to the "Template" section <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Search for "payment receipts" to find the specific template <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Each template has a "database link" and a "template link" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click on both links to open the Notion template and its corresponding database <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Duplicate both the template and the database to your local Notion workspace by clicking "Duplicate" and selecting your desired workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
4.  **Connect Notion Database and Template**:
    *   On the PDFoutput.com interface, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Grant access to your Notion workspace and select the duplicated Notion template and database <a class="yt="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   Once authentication is successful, the connected database (e.g., "Payment Receipts Database") and template (e.g., "Payment Receipt Template") will be displayed <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Give the connection a name, for example, "Payment Receipts", and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
5.  **Map Database Properties to Template Elements**:
    *   The tool will load database properties and attempt to automatically map them to the template elements if naming conventions are consistent <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   If there are mismatches, you can manually search for and select the correct corresponding element <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   You can also filter for unmapped or mapped properties and use search/sorting options <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
6.  **[[using_pdfoutput_tool_for_bulk_pdf_generation | Generate the PDFs]]**:
    *   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   The tool will read the database rows and the template to [[generating_pdf_documents_for_business_needs | generate a PDF document]] for each row <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
    *   After export is successful, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Output Example
The generated PDF documents will be clean and accurately populated with data from each row of your Notion database <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. For instance, if the database has three rows, three distinct PDF payment receipts will be generated (e.g., for Alice Brown, John Doe, and Jam Smith) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>, <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Additional Features and Settings

PDFoutput.com offers several features to streamline your [[generating_pdf_documents_for_business_needs | PDF generation]] workflow:

*   **Connections**: The "Connections" section displays a list of previously created database-template connections, allowing you to quickly reload them without manual re-addition <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. If data isn't loading, click "refresh" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Templates**: The "Templates" section provides a variety of predefined templates for different use cases, including [[creating_bulk_invoice_pdfs | invoices]], [[generating_sales_receipt_pdfs | sales receipts]], and [[generating_purchase_order_pdfs in bulk | purchase orders]], with more being added over time <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade**: The free plan includes a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes this watermark and provides higher generation limits <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Settings**: This section allows you to define the page format (default is A4) for your PDF documents <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. You can also add more templates and databases from here after initial setup <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback**: A dedicated window is available to provide feedback or ask questions to the support team <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Help for Custom Templates**: If you wish to use a custom PDF document format without relying on the predefined Notion template and database, the "Help" section explains the steps <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Sidebar Toggle**: The sidebar can be collapsed or expanded using the arrow icon <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.