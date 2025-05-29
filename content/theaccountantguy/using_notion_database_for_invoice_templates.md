---
title: Using Notion Database for Invoice Templates
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[using_notion_for_invoice_generation | generate professional invoice PDF documents in bulk]] using a [[creating_professional_invoice_templates_in_notion | Notion template]] and a [[using_notion_database_as_an_invoice_source | Notion database]] with the help of PDFoutput.com <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Template and Database Structure

A professional invoice template defines all necessary elements, with placeholders for dynamic data enclosed in curly braces (e.g., `{{client name}}`, `{{client company}}`, `{{client address}}`) <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The [[using_notion_database_as_an_invoice_source | Notion database]] contains corresponding information for each of these elements, enabling bulk PDF generation <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Each row in the database represents a unique invoice to be generated <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Generating Invoices with PDFoutput.com

The process utilizes PDFoutput.com to [[connecting_notion_templates_with_a_database_for_automation | connect Notion templates with a database for automation]] and generate PDFs <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Step 1: Duplicate Template and Database

Before connecting, users must copy the professional invoice template and its corresponding database to their local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
1.  Log in to PDFoutput.com <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
2.  Navigate to the "Templates" section on the PDFoutput.com portal <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  Search for "invoice" to find the professional invoices template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
4.  Click on both the database link and the template link <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This will open them in new Notion tabs <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
5.  In Notion, click the "Duplicate" option (usually in the top right) for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
6.  Select your Notion workspace to duplicate them to <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This will add the [[creating_professional_invoice_templates_in_notion | professional invoice template]] and the [[using_notion_database_as_an_invoice_source | professional invoice database]] to your Notion workspace <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Step 2: Connect Notion to PDFoutput.com

After duplication, connect your Notion workspace to PDFoutput.com:
1.  On the PDFoutput.com connection details screen, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  Choose your Notion workspace <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
3.  Select both the duplicated invoice template and database, then click "Allow access" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
4.  PDFoutput.com will load the selected database and template, displaying them as connected <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
5.  Define a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
6.  Click "Next" to proceed to mapping <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Step 3: Map Database Properties to Template Elements

PDFoutput.com automatically maps database properties to template elements if their names are identical (e.g., "Client Name" in the database corresponds to `{{Client Name}}` in the template) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   If names differ, properties will appear with a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on the gray icon and search for the correct template element to map manually <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Ensure all elements are correctly mapped before proceeding <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Step 4: Generate and Download PDFs

Once mapping is complete:
1.  Click "Create PDF" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  PDFoutput.com will generate a separate PDF document for each row in your [[using_notion_database_as_an_invoice_source | Notion database]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
3.  After generation, you can preview a sample PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> or download all generated documents as a zip file <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
4.  The generated PDFs will reflect the data from each corresponding database row, with all placeholders replaced <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Customization and Advanced Options

*   **Template Customization**: The template can be entirely customized. Ensure that any data intended to be replaced from the database is enclosed in curly braces (`{{ }}`) and matches the exact property name in your [[using_notion_database_as_an_invoice_source | Notion database]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Existing Connections**: Once a connection is established, you can reuse it from the "Connections" sidebar option, eliminating the need to redefine the template and database every time <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Adding More Databases/Templates**: Use the "Settings" window or the initial login prompts to connect additional databases and templates to your PDFoutput.com portal <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Relational Properties**: If your [[using_notion_database_as_an_invoice_source | Notion database]] uses relational properties connected to other databases, ensure those linked databases are also added during the connection setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Subscription Options**: Free plans include a "Made with PDFoutput" watermark on generated PDFs. Upgrading to a paid subscription removes this watermark and offers higher document generation tiers <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Page Format**: In the settings, you can define the specific page format for your PDFs (e.g., A4 size is default) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

This process enables efficient [[using_notion_for_invoice_generation | bulk invoice generation]] by [[integrating_databases_with_templates_in_notion | integrating Notion databases with templates]] to create professional PDF documents.