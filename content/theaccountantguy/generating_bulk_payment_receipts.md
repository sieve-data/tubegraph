---
title: Generating bulk payment receipts
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_for_sales_receipts | generate PDF documents]] in bulk from Notion templates and databases <a class="yt-timestamp" data-t="00:00:04"></a>. This process involves using a Notion payment receipt template and a Notion database to create multiple payment receipt PDF documents efficiently <a class="yt-timestamp" data-t="00:00:07"></a>.

## Key Components

To [[generating_bulk_pdfs_with_database_integration | generate bulk PDFs]] for payment receipts, two primary components are required:

*   **Notion Template:** This is a pre-designed payment receipt template with specific elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, etc. <a class="yt-timestamp" data-t="00:00:14"></a> <a class="yt-timestamp" data-t="00:00:20"></a> These elements act as placeholders to be replaced with data from your database <a class="yt-timestamp" data-t="00:00:24"></a>.
*   **Notion Database:** This database contains rows of information, where each row represents data for a single payment receipt <a class="yt-timestamp" data-t="00:00:42"></a>. Each column in the database must correspond to an element (placeholder) in the Notion template, ideally using the exact same naming convention, including spaces and capitalization, to ensure automatic mapping <a class="yt-timestamp" data-t="00:00:54"></a> <a class="yt-timestamp" data-t="00:01:00"></a> <a class="yt-timestamp" data-t="00:06:46"></a>.

## [[steps_for_creating_payment_receipt_templates | Steps for Creating Payment Receipt Templates]]

The general workflow for [[generating_payment_receipts_in_pdf_using_notion | generating payment receipts in PDF using Notion]] and PDF Output involves these steps:

### 1. Access PDF Output

Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:24"></a>. You will need to log in to access the interface <a class="yt-timestamp" data-t="00:01:29"></a>.

### 2. Duplicate Template and Database to Notion

Before connecting to PDF Output, you need to set up your Notion workspace <a class="yt-timestamp" data-t="00:03:01"></a>.
*   Go to the "Templates" section within PDF Output <a class="yt-timestamp" data-t="00:02:08"></a>.
*   Search for "payment receipts" <a class="yt-timestamp" data-t="00:02:14"></a>.
*   Locate the template, which will have both a database link and a template link <a class="yt-timestamp" data-t="00:02:39"></a>.
*   Click on both links to open them in new windows <a class="yt-timestamp" data-t="00:02:42"></a>.
*   **Duplicate the Notion Template:** Click "Duplicate" on the Notion payment receipt template page and select your desired Notion workspace (e.g., "accountant guy") <a class="yt-timestamp" data-t="00:03:27"></a> <a class="yt-timestamp" data-t="00:03:36"></a>. This will add the template to your private Notion workspace <a class="yt-timestamp" data-t="00:03:46"></a>.
*   **Duplicate the Notion Database:** Similarly, click "Duplicate" on the Notion database page and add it to your Notion workspace <a class="yt-timestamp" data-t="00:03:57"></a> <a class="yt-timestamp" data-t="00:04:14"></a>.

### 3. Connect Notion to PDF Output

Once logged into PDF Output, you will be prompted to connect your Notion database and template <a class="yt-timestamp" data-t="00:01:47"></a>.
*   Click on "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45"></a>.
*   Grant PDF Output access to your Notion pages by selecting your Notion workspace (e.g., "accountant guy") <a class="yt-timestamp" data-t="00:04:51"></a> <a class="yt-timestamp" data-t="00:04:54"></a>.
*   Select the duplicated payment receipt template and database from your Notion workspace and click "Allow access" <a class="yt-timestamp" data-t="00:05:04"></a>.
*   The system will authenticate with Notion and connect the template and database to PDF Output <a class="yt-timestamp" data-t="00:05:14"></a>. The selected database and template names will be displayed <a class="yt-timestamp" data-t="00:05:39"></a>.
*   Give the connection a name, such as "payment receipts" <a class="yt-timestamp" data-t="00:05:56"></a>.

### 4. Map Database Properties to Template Elements

After naming the connection, click "Next" <a class="yt-timestamp" data-t="00:06:02"></a>.
*   PDF Output will load all database properties (columns) and automatically attempt to map them to the corresponding elements in the template <a class="yt-timestamp" data-t="00:06:04"></a> <a class="yt-timestamp" data-t="00:06:08"></a>.
*   If your database column names exactly match the placeholders in the template (e.g., "Company Website" in the database matching `{Company Website}` in the template), the mapping will be automatic <a class="yt-timestamp" data-t="00:06:30"></a> <a class="yt-timestamp" data-t="00:06:55"></a>.
*   In case of a mismatch, you can manually map properties by clicking on the unmapped field and searching for the correct database column <a class="yt-timestamp" data-t="00:06:57"></a> <a class="yt-timestamp" data-t="00:07:04"></a>.
*   Filtering, searching, and sorting options are available to help manage properties <a class="yt-timestamp" data-t="00:07:16"></a>.

### 5. Generate PDFs

Once all properties are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27"></a>.
*   PDF Output will read the data from each row in your Notion database and populate the template, generating a separate PDF document for each row <a class="yt-timestamp" data-t="00:07:31"></a> <a class="yt-timestamp" data-t="00:07:37"></a>. For example, if your database has three rows, three PDF documents will be generated <a class="yt-timestamp" data-t="00:07:40"></a>.
*   After successful export, you can preview a sample document to check the output quality <a class="yt-timestamp" data-t="00:07:49"></a>.
*   Click "Download all documents" to download a zip file containing all generated PDF payment receipts <a class="yt-timestamp" data-t="00:08:17"></a>.

## PDF Output Features

*   **Connections:** The "Connections" section displays a list of previously created connections (database-template pairs) <a class="yt-timestamp" data-t="00:09:20"></a>. Selecting a saved connection automatically loads the database and template, eliminating the need to add them manually again <a class="yt-timestamp" data-t="00:09:33"></a>. If the connection doesn't load immediately, click "Refresh" <a class="yt-timestamp" data-t="00:09:56"></a>.
*   **Templates:** The "Templates" section provides access to a variety of pre-designed templates for different use cases, such as invoices and other documents <a class="yt-timestamp" data-t="00:10:06"></a>. This aligns with [[using_templates_in_pdf_output_for_generating_receipts | Using templates in PDF Output for generating receipts]].
*   **Upgrade Options:** The free plan includes a "Made with PDF Output" watermark on generated PDFs <a class="yt-timestamp" data-t="00:10:18"></a>. Upgrading to a paid plan removes this watermark and offers higher generation limits <a class="yt-timestamp" data-t="00:10:23"></a>.
*   **Settings:**
    *   **Page Format:** Allows you to define the page format (e.g., A4) for the generated PDFs <a class="yt-timestamp" data-t="00:10:40"></a>.
    *   **Add More Templates/Databases:** You can connect additional templates and databases via the settings <a class="yt-timestamp" data-t="00:10:49"></a>. This is useful for tasks like [[exporting_and_customizing_invoices_in_bulk | exporting and customizing invoices in bulk]] or [[exporting_bulk_purchase_order_documents | exporting bulk purchase order documents]].
*   **Feedback:** A feedback window is available for questions or suggestions <a class="yt-timestamp" data-t="00:11:08"></a>.
*   **Custom Templates:** Guidance is available for using custom PDF documents with a database, without relying on predefined templates <a class="yt-timestamp" data-t="00:11:19"></a>.

This process enables efficient [[customizing_invoice_templates_for_bulk_generation | bulk generation]] of standardized payment receipts, leveraging Notion's database capabilities with PDF Output's PDF generation functionality.