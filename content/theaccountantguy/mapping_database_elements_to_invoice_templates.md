---
title: Mapping database elements to invoice templates
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_professional_invoices_from_a_database | generate professional invoices]] directly from a Notion database by [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]] using PDF output. <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>

## Invoice Template Structure

An invoice template is designed with specific placeholders to be replaced by data from a database.
These placeholders are text elements enclosed in curly braces, such as `{{client name}}`, `{{client company}}`, `{{client address}}`, `{{city}}`, `{{state}}`, and `{{zip}}`. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> Any element in the template placed within curly braces is intended to be replaced from a database. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

For example, a template might include sections for "from" and "to" information, where the "to" section contains these client-specific placeholders. <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>

## [[database_setup_for_invoice_details | Database Setup for Invoice Details]]

The Notion database serves as the source for the invoice details. <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> It contains columns that correspond to the placeholders in the template. Examples of database columns include:
*   Client Name <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Amount <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Bank Name <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Client Address <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   Client Company <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

For every row of information in the database, the corresponding data will populate the template and generate a PDF. <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

## [[integrating_databases_with_templates_in_notion | Integrating Databases with Templates in Notion]] using PDF output

To perform the mapping and generation, a tool like "PDF output" is utilized. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

### Initial Setup

1.  **Log in to PDF output:** Upon logging in, you will see a specific interface. <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>
2.  **Enable API keys:** Navigate to the help section (by clicking 'H') to complete the necessary steps for enabling API keys, which are required for the setup. <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>

### Defining the Connection

Once API keys are enabled, define a new connection:
1.  **Name the connection:** Provide a name for the connection, such as "invoice generation". <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
2.  **Select the Database:** From a dropdown, select the specific Notion database (e.g., "professional invoice database"). <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
3.  **Select the Template:** Similarly, select the corresponding Notion template (e.g., "professional invoice template"). <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
4.  **Proceed:** Click "Next". <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>

### [[mapping_database_properties_to_templates | Automatic and Manual Mapping]]

After clicking "Next", the system loads all elements and values from both the database and the template. <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
It then automatically attempts to [[mapping_database_properties_to_template_placeholders | map each database element to its corresponding template placeholder]]. <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

*   The left side of the interface lists database properties (column names). <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Each database property is connected to a template element. <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   For example, "Client Address" from the database is connected to the "Client Address" placeholder in the template. <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

> The system automatically maps elements where the placeholder name matches the column name in the database. <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a> If a match isn't found, the mapping will appear in gray. <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> In such cases, you can manually click on the grayed-out element and search for the correct database value to map it. <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>

### Generating the Invoices

1.  **Export:** Click on the "Export" button. <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
2.  **PDF Status Column:** In the Notion database, a "PDF status" column will appear, initially unticked. As PDF files are generated, this column will automatically tick, indicating completion. <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>
3.  **Preview and Download:**
    *   After generation, you can click "Preview Sample" to view a clean, generated invoice. <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
    *   To download all generated files, click "Download All". <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> This will download a zip file containing all the individual PDF invoices. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>

## [[Customizing invoice templates with placeholders | Customization and Best Practices]]

All elements in the template are customizable according to specific requirements. <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
When [[customizing_invoice_templates_with_placeholders | customizing invoice templates with placeholders]], ensure that:
*   All placeholder text elements are enclosed within curly braces (e.g., `{{PlaceholderName}}`). <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>
*   The names used for placeholders in the template exactly match the column names in your Notion database. <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>

By following these instructions, you can effectively [[using_notion_database_as_an_invoice_source | use a Notion database as an invoice source]] and [[using_notion_database_for_invoice_templates | generate professional PDF invoices]]. <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>