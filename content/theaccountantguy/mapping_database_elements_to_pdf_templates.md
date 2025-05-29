---
title: Mapping database elements to PDF templates
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[integrating_databases_with_pdf_templates | generate PDF documents in bulk]] by using a Notion page as a template and a Notion database to supply the content [00:00:03]. This process involves [[integrating_databases_with_templates | integrating databases with templates]] and specifically [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]] for automated content replacement.

## Setting Up Notion for PDF Generation

Before using PDF Output, you need to [[setting_up_notion_templates_and_databases_for_pdf_generation | set up Notion templates and databases]] as follows:

### Creating a PDF Template in Notion
The template is a Notion page that defines the structure and static content of your PDF documents [00:00:08].
*   Create a new Notion page and add your desired content [00:01:05]. For example, an "Invitation Letter Template" [00:01:11].
*   Identify the sections within your template that need to be replaced with dynamic data from a database. These sections, or placeholder texts, must be enclosed within curly braces `{}` [00:01:34].
    *   For instance, `{title}` and `{customer name}` would be used if you want to replace these specific pieces of information [00:01:40]. The curly braces signify that these elements will be replaced by database values [00:01:53].

### Creating a Notion Database for Content
The database holds all the dynamic information that will populate your PDF templates [00:00:10].
*   Create a new Notion database (e.g., a table) [00:02:06]. For example, an "Invitation Letter Database" [00:02:22].
*   Define columns in your database with names that exactly match the placeholder texts you used in your template (without the curly braces) [00:02:35].
    *   For the example above, you would have columns named `title` and `customer name` [00:02:30]. This [[mapping_database_elements_to_template_naming_conventions | exact naming convention]] is crucial for automatic mapping [00:08:00].
*   Populate the database with rows, where each row represents a unique set of data for a single PDF document [00:02:53].

## The Mapping Process in PDF Output

Once your Notion template and database are prepared, you can connect them to PDF Output:

1.  **Select Database and Template:** In PDF Output, designate your Notion database in the "Notion Database" section and your Notion template in the "Notion Template" section [00:00:30]. You'll need to allow PDF Output access to these Notion pages [00:03:44].
2.  **Define Connection Name:** Give your connection a name, for instance, "invitation letter" [00:04:27].
3.  **Automatic Mapping Screen:** After clicking "next," PDF Output displays a mapping section [00:04:32].
    *   On the left side, you'll see all the properties (column names) from your selected Notion database, such as "customer name" and "title" [00:04:43].
    *   On the right side, the tool automatically maps these database properties to the corresponding elements identified in your template (those enclosed in curly braces) [00:05:05]. This enables the [[automatic_mapping_of_notion_database_properties_to_pdf_template_elements | automatic mapping of Notion database properties to PDF template elements]].
4.  **Manual Mapping (If Needed):** If the database column names do not exactly match the template placeholder names, the mapping will not occur automatically [00:05:12]. In such cases, you will need to manually select and map the database element to its corresponding template placeholder [00:05:22].
    *   The mapping interface also offers sorting, searching, and filtering options to manage properties [00:05:29].

## Generating PDFs

After the mapping is complete, click "create PDF" [00:05:56]. PDF Output will then generate individual PDF documents for each row in your Notion database, filling in the templated placeholders with the corresponding database values [00:05:58]. Each generated PDF will contain the unique information from a specific database entry [00:06:40].

## Key Considerations for Mapping

*   **Placeholder Syntax:** Always enclose placeholder texts in your Notion template within curly braces, e.g., `{PlaceholderName}` [00:07:54].
*   **Exact Naming:** Use the exact same naming convention for your database column names as your template placeholder names (excluding curly braces) to facilitate automatic mapping [00:08:00].

## Reusing Connections and Predefined Templates

*   **Connections:** Once a connection between a template and a database is established and mapped, it is saved [00:08:22]. This allows you to quickly load previously defined setups without re-creating the connection or re-mapping the elements each time [00:08:44].
*   **Predefined Templates:** PDF Output also offers a library of predefined templates [00:09:07]. You can click "start with this template" to duplicate both the template and its associated database directly into your Notion workspace, simplifying the [[creating_and_using_templates_for_pdfs | creation and use of templates for PDFs]] and [[creating_and_exporting_custom_pdf_templates | exporting custom PDF templates]] [00:09:49].