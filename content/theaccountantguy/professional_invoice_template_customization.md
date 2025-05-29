---
title: Professional invoice template customization
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

Professional invoice PDF documents can be generated in bulk using a Notion template and a Notion database with PDF Output.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Understanding the Template Structure

The professional invoice template defines all elements typically found in an invoice <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Every element placed inside curly braces `{}` in the template will be replaced with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For example, `client name`, `client company`, and `client address` are placeholders <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

A Notion database is set up with corresponding fields like `client name`, `client company`, and `client address` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For every element in the database, a corresponding element is created in the template using curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. These elements are then used to generate bulk PDF documents from the database rows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Generating Invoices in Bulk

The software used for this process is PDF Output.com <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Step-by-Step Process

1.  **Log in to PDF Output.com** <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Upon logging in, you'll see a connection details screen where you need to define the connection for PDF generation <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  **Duplicate Template and Database**:
    *   Before connecting, copy the professional invoice template and database to your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Click on "Templates" in PDF Output.com to access pre-added [[customizable_pdf_templates | templates]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Search for "invoice" to find the "Professional Invoices" template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on the "database link" and "template link" associated with it <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   In the opened Notion tabs, click the "Duplicate" option (top right) for both the template and the database, selecting your Notion workspace to copy them over <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Connect Notion to PDF Output**:
    *   Back in PDF Output.com, click "Add Template" or "Add Database" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace (e.g., "the accountant guy" workspace) <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   Choose the duplicated professional invoice template and database, then click "Allow access" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    *   PDF Output.com will automatically load both the database and template from your Notion workspace <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   Define a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
4.  **Map Database Properties to Template Elements**:
    *   The system will load the database properties on the left and automatically map them to corresponding elements in the template if their names match exactly (e.g., `invoice number` in Notion database maps to `{invoice number}` in the template) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   If names differ, an element will show a gray icon, requiring manual mapping by clicking on it and searching for the correct property <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
5.  **Generate PDFs**:
    *   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   The system will generate a PDF document for every row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   You can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Customizing Invoice Templates

The template can be entirely [[customizable_pdf_templates | customizable]] as per your requirements <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Placeholder Naming**: Ensure that any data you want to pull from the database is enclosed in curly braces `{}` in the template, and use the exact same name for the corresponding property in your Notion database <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This enables automatic mapping <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Manual Mapping**: If database property names and template placeholder names are different, you will need to manually map them during the connection process <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Relational Properties**: If your Notion database uses relational properties linked to another database, ensure that the linked database is also allowed/connected during the initial connection setup <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## PDF Output Portal Features

The sidebar provides several useful options:

*   **Connections**: Shows all previously created connections, allowing you to quickly reload them without redefining the database and template <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Templates**: Provides a list of pre-added [[customizable_pdf_templates | templates]] for various use cases, including [[customizing_invoice_templates_for_bulk_generation | invoices]], [[customizing_sales_receipts_templates | sales receipts]], and [[customizing_lease_agreement_templates | lease agreements]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Remember to duplicate the template and database to your Notion workspace first <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Upgrade**: Allows you to upgrade your subscription. The free plan includes a "Made with PDF Output" watermark, which is removed in paid plans <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Here, you can define the page format (default is A4) and add more databases and templates by following the authentication process <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This is an alternative to the initial login prompt for adding new connections <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Feedback**: Use this option to send messages or queries <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Help**: Provides detailed instructions on connecting a custom Notion database and template to generate PDF documents in bulk <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.