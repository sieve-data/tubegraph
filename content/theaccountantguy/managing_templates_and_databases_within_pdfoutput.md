---
title: Managing templates and databases within PDFOutput
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[Introduction to PDFOutput tool | PDFOutput]] is a tool designed to [[using_pdfoutputcom_to_generate_pdf_documents_in_bulk | generate PDF documents in bulk]] by leveraging a Notion page as a template and a Notion database to supply the content for replacement [00:00:03].

## [[Setting up Notion templates and databases for PDF generation | Setting Up Notion Templates and Databases]]

Before [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion to PDFOutput]], users must [[creating_notion_templates_and_databases_for_pdf_generation | create a template and a database in Notion]] [00:00:43].

### [[Creating Notion templates and databases for PDF generation | Creating a Notion Template]]

To create a template in Notion:
1.  Click on the "create a new page" icon in Notion [01:05:05].
2.  Name the template page (e.g., "Invitation Letter Template") [01:15:00].
3.  Set the page to "full width mode" [01:20:00].
4.  Define the content of the template [01:22:00].
5.  Crucially, any sections of the template intended for replacement with database information must be enclosed within curly braces `{}` [01:34:00]. For example, `{title}` and `{customer name}` signify placeholders that will be replaced by data from the database [01:44:00].

### [[Creating Notion templates and databases for PDF generation | Creating a Notion Database]]

To create a database in Notion:
1.  Click on the "create a new page" icon [02:08:00].
2.  Select "Table" to create a new table database [02:19:00].
3.  Name the database (e.g., "Invitation Letter Database") [02:22:00].
4.  Define columns in the database [02:30:00]. The column names in the database **must exactly match** the placeholder names used in the template (e.g., "Title" and "Customer Name" if the template uses `{title}` and `{customer name}`) [02:35:00].
5.  Populate the database with rows of unique information [02:54:00]. Each row will typically correspond to one generated PDF document.

## [[Connecting Notion database and templates to PDF output | Connecting Notion to PDFOutput]]

Once the Notion template and database are prepared, connect them to PDFOutput:
1.  Log in to PDFOutput [00:22:00].
2.  Click "click here to add database" or "add template" to initiate the connection process [03:11:00].
3.  You will be redirected to Notion's authorization screen [03:20:00].
4.  Select the specific Notion account/workspace being used [03:26:00].
5.  Click "Select pages" and then choose both the template page and the database page created earlier [03:33:00].
6.  Click "Allow access" to authorize PDFOutput to access the selected Notion pages [03:46:00].
7.  PDFOutput will automatically fetch and sync the database and template [03:51:00].
8.  Define a "connection name" for this specific setup (e.g., "Invitation Letter") [04:26:00].
9.  Click "Next" to proceed to the mapping section [04:32:00].

## Mapping Properties

In the mapping section:
*   The left side displays all database properties (columns) [04:43:00].
*   The right side shows the corresponding elements identified from the template [04:52:00].
*   If the database column names perfectly match the curly-braced placeholders in the template, PDFOutput will automatically map them [05:06:00].
*   If names do not match, or if a manual selection is preferred, users can click on each element and manually select the corresponding database property for mapping [05:22:00].
*   Sorting, searching, and filtration options are available to help manage properties, especially in larger setups [05:31:00].

## [[Using templates to generate PDF documents | Generating PDFs]]

After mapping is complete:
1.  Click on "Create PDF" [05:56:00].
2.  PDFOutput will process the request and generate the PDF documents [05:57:00].
3.  Users can preview a sample PDF document [06:33:00].
4.  Click "Download all" to download all generated PDF documents [06:50:00]. Each row in the Notion database will result in a separate PDF document, with the placeholder text replaced by the corresponding database entry [06:56:00].

## Key Considerations for Templates and Databases

*   **Placeholder Format**: Always enclose placeholder text elements in the Notion template within curly braces, e.g., `{customer name}` [07:54:00].
*   **Naming Convention**: Use the exact same naming convention for database column headers as for the placeholder text in the template for automatic mapping [08:00:00]. If names differ, manual mapping will be required [08:06:00].

## Managing Connections and Templates within PDFOutput

PDFOutput provides features for managing established connections and accessing pre-defined templates:

### Connections Tab
*   The "Connections" tab on the sidebar shows all previously created connections [08:22:00].
*   Selecting a connection (e.g., "Invitation Letter") will automatically load the associated database and template, allowing users to quickly regenerate documents without setting up a new connection each time [08:30:00].

### Templates Tab
*   The "Templates" tab displays a list of pre-added templates provided by PDFOutput [09:07:00].
*   Each template entry includes a database link and a template link [09:15:00].
*   To use any of these templates, click on the "Start with this template" option [09:49:00].
*   This will prompt the user to duplicate both the database and the template file to their Notion workspace [09:50:00]. Select the desired Notion workspace and click "Add to private" to import the template and database pages [10:05:00].

### Settings
*   Under the "Settings" tab, users can manage the page format for PDFs (e.g., A4, Letter) [11:01:00].
*   This section also provides an option to "click here to add more templates" for subsequent additions of databases and templates after initial setup [11:13:00].