---
title: Using Notion templates for invoice PDFs
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[generating_pdf_invoices_from_notion_data | generate professional invoice PDF documents in bulk]] using a [[using_notion_templates_and_databases_for_pdf_generation | Notion template]] and a [[using_notion_templates_and_databases_for_pdf_generation | Notion database]] with the help of PDF output.com. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

## Understanding the Notion Template and Database

A [[creating_professional_invoices_using_notion | professional invoice]] PDF can be generated using a Notion template where elements enclosed in curly braces, such as `{client name}`, `{client company}`, and `{client address}`, are placeholders. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> These placeholders are automatically replaced by corresponding items from a [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]]. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

The [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]] should contain columns that exactly match the names of the elements in the template (e.g., "Client Name", "Client Company", "Client Address"). <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> For every element in the database, a corresponding element must be defined in the template within curly braces. <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> This setup allows for the bulk [[generating_pdf_invoices_from_notion_data | generation of PDF documents]] for each row in the database. <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>

> [!info] Mapping Tip
> If the names in your template (within curly braces) and your database columns are identical, PDF output.com will automatically map them. <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> If names differ, manual mapping will be required. <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>

## Step-by-Step PDF Generation

The process involves using PDF output.com to connect your Notion data and template for bulk PDF generation. <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>

### 1. Accessing PDF output.com

*   Go to PDF output.com and log in. <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   Upon login, you'll see a connection details screen where you define connections for PDF generation. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>

### 2. Duplicating Notion Templates and Databases

Before connecting, you need to copy the desired template and database to your local Notion workspace:
1.  On PDF output.com, navigate to the "Templates" section. <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
2.  Search for "invoice" to find the [[creating_professional_invoices_using_notion | professional invoices]] template. <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
3.  Click on both the "Database link" and the "Template link." <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> This will open them in new tabs. <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
4.  For both the Notion template and the [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]], click the "Duplicate" option in the top right. <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
5.  Select your desired Notion workspace (e.g., "the accountant guy workspace") to duplicate the template and database into. <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>

### 3. Connecting Notion to PDF output.com

1.  Back on PDF output.com's connection details screen, click on "Add Database" or "Add Template." <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
2.  Select your Notion workspace again. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
3.  Choose the duplicated [[creating_and_using_invoice_templates_in_notion | Notion template]] and [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]] from your workspace. <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
4.  Click "Allow access." <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a> The portal will automatically load both. <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
5.  Define a connection name (e.g., "invoice template"). <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>
6.  Click "Next." <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>

### 4. Mapping and Generating PDFs

1.  PDF output.com will automatically display database properties on the left and map them to corresponding template elements on the right. <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>
2.  If any elements are not automatically mapped (indicated by a gray icon), click on them and search for the correct property from your [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]] to map it manually. <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
3.  Once all elements are correctly mapped, click "Create PDF." <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
4.  The system will generate a PDF document for each row in your database. <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>

### 5. Reviewing and Downloading Generated PDFs

*   After generation, you can "Preview sample" to see one of the generated invoices (e.g., for John Doe). <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
*   Click "Download all" to download a zip file containing all the generated PDF documents. <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>

## Customization and Additional Features

*   **Customizable Templates:** The [[using_notion_for_invoice_template_creation | invoice template]] is entirely customizable. <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> Ensure that any data you want to pull from the database is enclosed in curly braces and uses the exact same name as the database property. <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>
*   **Relational Properties:** If your [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]] uses relational properties connected to other databases, make sure to add those related databases during the connection setup as well. <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>
*   **Connections:** The "Connections" section in the sidebar allows you to quickly load previously created connections to [[generating_pdf_invoices_from_notion_data | generate PDF documents]] without re-defining the template and database every time. <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>
*   **Templates:** The "Templates" section provides a variety of pre-added templates for different use cases. <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>
*   **Upgrade:** Under the "Upgrade" section, you can manage your subscription. The free plan includes a "Made with PDF output" watermark, which is removed with a paid subscription. <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>
*   **Settings:** The "Settings" window allows you to define page format (default is A4) and add more databases and templates. <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
*   **Feedback:** Use the "Feedback" option to send messages or queries for assistance. <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **Help:** The "Help" section provides detailed instructions on connecting custom PDF documents and databases to [[generating_pdf_invoices_from_notion_data | generate PDF documents]] in bulk. <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>