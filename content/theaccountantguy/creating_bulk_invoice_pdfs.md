---
title: Creating bulk invoice PDFs
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

[[Using PDF Output tool for invoice generation | Generating professional invoice PDF documents]] in bulk is possible using a Notion template and a Notion database in conjunction with the PDF Output tool <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method allows for efficient [[generating_and_managing_invoice_documents | invoice generation]] for multiple clients or transactions at once <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Template and Database Structure

The process relies on a professional invoice template and a corresponding Notion database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

*   **Template:** The template defines all the elements of a standard invoice <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Elements that are intended to be dynamic and populated from the database are placed inside curly braces, such as `{client name}`, `{client company}`, and `{client address}` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Database:** The Notion database contains the specific information for each invoice, with properties (columns) that correspond to the elements defined in the template (e.g., `client name`, `client company`, `client address`) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For every element in the database, there should be a corresponding element in the template enclosed in curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Each row in the database will generate a separate PDF invoice <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Steps for Bulk PDF Generation with PDF Output

The primary tool for [[using_pdf_output_tool_for_bulk_pdf_generation | bulk PDF generation]] is PDFoutput.com <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### 1. Log in to PDF Output
Navigate to PDFoutput.com and log in to your account <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Upon logging in, you'll see a connection details screen where you need to define the connection for your PDF generation <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### 2. Duplicate Notion Template and Database
Before connecting, you need to copy the desired template and database from PDF Output's pre-added list to your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Click on "Templates" in PDF Output to view available templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   Search for "invoice" to find the professional invoices template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Click on both the "database link" and "template link" associated with the invoice template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This will open them in new Notion tabs <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   In each Notion tab, click the "Duplicate" option (typically in the top right) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Select your desired Notion workspace (e.g., "the accountant guy workspace") and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This will copy the template and database to your Notion workspace <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### 3. Connect Notion to PDF Output
Once duplicated, connect your Notion database and template within the PDF Output portal <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   In PDF Output, click "Add Database" or "Add Template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Choose your Notion workspace where the duplicated items are located <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Select both the professional invoice database and template you just duplicated <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   PDF Output will automatically load and display your selected database and template <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   Define a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   Click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### 4. Map Database Properties to Template Elements
PDF Output will automatically map database properties to template elements if they have the exact same names <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Database properties will appear on the left, and mapped template elements on the right <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   If names differ, an element might show a grey icon <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Manually click on the grey icon and search for the correct element to map it <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Ensure all elements are correctly mapped before proceeding <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### 5. Generate and Download PDFs
Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   PDF Output will start [[generating_purchase_order_pdfs_in_bulk | generating PDF documents]] for every row in your Notion database <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   After generation, you can "Preview Sample" of a generated PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> or "Download All" documents <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The downloaded file will be a zip archive containing all individual PDF invoices <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Customization and Additional Features

*   **Template Customization:** The template is fully customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Ensure that any elements you want to populate from the database are enclosed in curly braces `{}` and match the exact names of your database properties <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **Connections:** The "Connections" sidebar option shows all previously created connections, allowing you to quickly reload a setup without re-defining the template and database <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Templates Library:** PDF Output provides a library of pre-added templates for various use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Upgrade Options:** The "Upgrade" section allows you to manage your subscription. The free plan includes a "Made with PDF Output" watermark on generated PDFs, which is removed with a paid subscription <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Settings:** The "Settings" window allows you to define the page format (e.g., A4 size) and add more databases and templates <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Custom Templates:** You can use your own custom Notion template and database instead of the pre-added ones <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Relational Properties:** If your Notion database uses relational properties (linking to other databases), ensure all relevant databases are connected in PDF Output when setting up the connection <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

This process simplifies [[creating_bulk_invoices_with_notion | creating bulk invoices with Notion]] and the [[exporting_and_managing_generated_pdf_invoices | export and management of generated PDF invoices]] <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.