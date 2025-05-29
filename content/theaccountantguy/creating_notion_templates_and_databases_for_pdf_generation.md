---
title: Creating Notion templates and databases for PDF generation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that enables users to generate PDF documents in bulk by utilizing a Notion page as a template and a Notion database to supply the content [00:00:03]. The core function of PDF Output is to replace specific elements within a Notion template with corresponding data from a Notion database [00:00:08].

## Setting Up in PDF Output

Upon logging into PDF Output, users will find sections for Notion databases and Notion templates [00:00:22]. Here, you define the Notion database to be used for PDF generation and select the template for document creation [00:00:30].

## Creating Notion Templates and Databases from Scratch

Before [[connecting_notion_database_and_templates_to_pdf_output | connecting your Notion database and templates to PDF Output]], you need to create them within Notion itself [00:00:42].

1.  **Access Notion Workspace:** Open your Notion account dashboard [00:00:50].
2.  **Create a New Page:** Click the "create a new page" icon on the left sidebar [00:01:05]. This will open a blank page [00:01:09].
3.  **Design Your Template Page:**
    *   Give your template a title (e.g., "Invitation Letter Template") [00:01:11].
    *   Set the page to "full width" mode for optimal layout [00:01:20].
    *   Define the content of your template [00:01:22].
    *   **Important:** Any sections in the template that you wish to replace with data from your database *must* be enclosed in curly braces (e.g., `{title}`, `{customer name}`) [00:01:34, 00:01:51, 00:05:04, 00:07:56]. These are your placeholder elements [00:01:40].

4.  **Create Your Database:**
    *   Click on "create a new page" again [00:02:08].
    *   Select the "table" option to create a database [00:02:19].
    *   Name your database (e.g., "Invitation Letter Database") [00:02:22].
    *   **Crucial Naming Convention:** The column names in your database *must exactly match* the placeholder names defined in curly braces within your template [00:02:12, 00:02:35, 00:02:40, 00:08:00]. For instance, if your template uses `{title}` and `{customer name}`, your database columns should be named "title" and "customer name" [00:02:12].
    *   Populate your database with rows of unique information for each PDF you want to generate [00:02:53].

> If you create different element names in the template and database, you will need to manually map them later in the mapping section [00:08:06].

## [[Connecting Notion Database and Templates to PDF Output|Connecting Notion Database and Templates to PDF Output]]

Once your Notion template and database are prepared:

1.  **Initiate Connection in PDF Output:** In the PDF Output interface, click either "click here to add database" or "add template" [00:03:11].
2.  **Select Notion Account:** You will be redirected to Notion to select the account or workspace you are using [00:03:20].
3.  **Grant Access to Pages:** Click "select pages" and choose both your created template and database pages from the list [00:03:33, 00:03:44]. Then click "Allow access" [00:03:46].
4.  **Automatic Sync:** PDF Output will then begin the authorization process, automatically fetching and syncing the selected database and template [00:03:48, 00:04:00].
5.  **Define Connection Name:** Upon redirection back to PDF Output, provide a connection name (e.g., "invitation letter") [00:04:25]. Then click "next" [00:04:32].

## Mapping Properties and Generating PDFs

After [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion templates with PDF output]], PDF Output loads the template and database for mapping [00:04:34].

1.  **Review Mapping:**
    *   The left side of the screen displays all properties (column headers) from your Notion database [00:04:43].
    *   The right side shows the corresponding elements from your Notion template, which were defined within curly braces [00:04:52, 00:05:04].
    *   If your database column names exactly match your template placeholder names, PDF Output will automatically map them [00:05:06].
    *   If names do not match, or if a property is unmapped, you will need to manually select the correct element for mapping [00:05:12, 00:05:20].
    *   Sorting, searching, and filtering options are available to help manage properties [00:05:31].
2.  **Create PDF:** Once all mappings are correctly defined, click "create PDF" [00:05:56]. PDF Output will then generate the bulk documents [00:05:58].

## Review and Download

After generation, you can preview a sample PDF to ensure it meets your expectations [00:06:31, 00:06:33]. Clicking "download all" will download all generated PDFs [00:06:50]. Each PDF will reflect the content of the template with data dynamically pulled from each row of your Notion database [00:06:56, 00:07:00].

## Managing Connections and Templates

*   **Saved Connections:** PDF Output stores your connections. You can access previously created connections via the "connections" sidebar option to quickly reload predefined databases and templates for future use without needing to recreate a new connection every time [00:08:22, 00:08:42].
*   **Predefined Templates:** The "templates" sidebar option provides a list of predefined templates available for use [00:08:57]. Each template has a database link and a template link [00:09:15]. To use a predefined template, click "start with this template" and duplicate both the database and the template into your Notion workspace [00:09:49, 00:10:26].
*   **Adding More Templates/Databases:** After initial setup, you can add more templates and databases by going to the "settings" tab and clicking "click here to add more templates" [00:11:13, 00:11:23].
*   **Page Format:** Under the "settings" tab, you can also select your desired page format for the generated PDFs [00:11:01].

## Free Plan Limitations

The free plan includes a "made with PDF Output" watermark on generated documents and may have certain limitations [00:10:39, 00:10:43]. Users can upgrade their subscription plan to remove watermarks and access full features [00:10:47].