---
title: Mapping Database Properties to Templates
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[using_templates_and_databases_to_create_professional_pdfs | generating professional PDF documents]] in bulk by [[integrating_databases_with_templates_in_notion | integrating Notion databases with Notion templates]] and [[mapping_database_elements_to_invoice_templates | mapping database elements to invoice templates]] using PDFoutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Overview: Professional Invoices with Notion
The process involves using a professional invoice template in Notion where elements are defined within curly braces <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These elements are designed to be replaced by corresponding items from a Notion database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For example, `client name`, `client company`, and `client address` are placed in curly braces in the template and matched with properties of the same name in the database <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This allows for the bulk generation of PDF documents for each row in the database <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## The Tool: PDFoutput.com
PDFoutput.com is the software used for this process <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. After logging in, users connect their Notion database and Notion template <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Setting up Your Notion Workspace
Before connecting, users must duplicate the desired template and database from PDFoutput.com's pre-added templates onto their local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
1.  Navigate to the "Templates" section on PDFoutput.com to view available pre-added templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
2.  Search for the specific template, such as "invoice" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Click on the provided database link and template link for the chosen template <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
4.  Once opened in new tabs, click the "Duplicate" option in the top right of each Notion page <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
5.  Select your Notion workspace to duplicate the template and database to your private Notion environment <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Connecting Notion to PDFoutput.com
Once duplicated, the database and template can be added to PDFoutput.com:
1.  On the "Connection Details" screen, click "Add Database" or "Add Template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  Choose your Notion workspace (e.g., "the accountant guy" workspace) and click "Select Pages" <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
3.  Select both the duplicated template and database, then click "Allow Access" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
4.  PDFoutput.com will automatically load both the database and template <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
5.  Define a connection name (e.g., "invoice template") and click "Next" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## [[mapping_database_elements_to_template_placeholders | Mapping Database Elements to Template Placeholders]]
After connecting, the system proceeds to [[mapping_database_properties_to_template_placeholders | map database properties to template placeholders]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   All database properties are reflected on the left side of the screen <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   If the names in the template (inside curly braces) exactly match the property names in the database, mapping occurs automatically <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   If names differ, manual mapping is required <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. An unmapped element will show a gray icon, prompting the user to click and search for the correct element to map <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Generating the PDFs
Once all elements are correctly mapped, click "Create PDF" to begin the generation process <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The system generates a PDF document for each row in the database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. After successful export, users can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## [[customizing_templates_and_databases_in_notion | Customizing Templates and Databases in Notion]]
The template is entirely [[customizing_templates_and_databases_in_notion | customizable]] <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For proper mapping, ensure that any data you want pulled from the database is enclosed in curly braces within the template, and that the name inside the curly braces exactly matches the property name in the Notion database <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This ensures automatic mapping and reduces manual effort <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### [[managing_relational_properties_in_notion_databases | Managing Relational Properties in Notion Databases]]
If your database uses [[managing_relational_properties_in_notion_databases | relational properties]] (i.e., elements in one database are connected to another database), ensure that all related databases are also connected when setting up the connection in PDFoutput.com <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. For example, if an invoice database is related to another database, that second database must also be added during the connection setup <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## PDFoutput.com Features
*   **Connections:** The "Connections" sidebar option shows all previously created connections, allowing users to quickly load and regenerate PDFs without re-defining templates and databases <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Templates:** Provides access to a library of pre-added templates for various requirements, each with corresponding database and template links for duplication <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Upgrade:** Offers subscription options to remove the "Made with PDFoutput" watermark and access higher tiers of document generation <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Settings:** Allows customization of page format (default A4 size) and facilitates adding more databases and templates <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Feedback:** A dedicated option to send messages or queries for assistance <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Custom Templates:** Users can use their own custom templates and databases. Detailed instructions for this are available via the "Help" option <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.