---
title: Integrating Google Docs with Notion database for PDF creation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to generate PDF documents in bulk by utilizing [[integrating_google_docs_with_notion_databases | Google Docs]] as a template and leveraging a [[using_notion_database_and_templates_for_pdf_generation | Notion database]] [00:00:02].

## Getting Started with PDFoutput.com

To begin, navigate to PDFoutput.com and click "create PDF" [00:00:10]. The platform will prompt you to sign in through a Google account [00:00:15]. After choosing your account, you must enable the checkbox that grants PDFoutput access to specific files [00:00:22]. Once enabled, click "continue" to be redirected to the homepage [00:00:29].

## Selecting a Google Docs Template

Upon reaching the homepage, you may see pre-populated PDF templates [00:00:34]. However, for custom generation, click the link next to "Google document" to access your Google Drive [00:00:42]. Here, you can select an existing document to serve as your template [00:00:46]. For instance, an "invitation letter" document can be used, requiring dynamic fields like `first name` and `last name` to be replaced with data from a [[setting_up_notion_database_for_pdf_document_templates | Notion database]] [00:00:49].

After selecting the Google Doc, it will load into PDFoutput.com [00:01:14].

## Setting Up Your Notion Database

Next, select "Notion" from the dropdown menu in PDFoutput.com [00:01:22]. The platform will request a Notion database URL and an API key [00:01:24].

To set up the Notion database:
1.  Open your Notion workspace by clicking the provided link [00:01:28].
2.  Create a new page, for example, named "PDF output database" [00:01:36].
3.  Type `/database` and select "inline" to create an inline database [00:01:47].
4.  Rename the default columns to relevant fields like "first name" and "last name" [00:01:58].
5.  Populate the database with data, such as names like Priya Sharma, Miller Stark, and John Quotes [00:02:11].

Once the database is set up:
1.  Click "share" on the Notion database page [00:02:42].
2.  Click "copy link" to copy the database URL [00:02:44].
3.  Paste this URL into the "database URL" field on PDFoutput.com [00:02:45].

## Connecting Notion to PDFoutput.com

To connect Notion:
1.  Click "add API key" on PDFoutput.com [00:02:50]. This will prompt you to create a new integration in Notion [00:02:52].
2.  Create a new internal integration, giving it a name such as "notion PDF output connection" [00:02:54].
3.  Select the desired account and click "save" [00:03:04].
4.  Go back to the integration you just created in Notion, click "show" to reveal the API key, and copy its value [00:03:12].
5.  Paste the copied API key into the "API key" field on PDFoutput.com [00:03:17].
6.  Ensure the Notion database you created is connected to this API key. In Notion, click the three dots on the database page, select "connections," and search for "PDF output connection" to confirm it [00:03:25].
7.  On PDFoutput.com, click "load properties." This action will fetch all the properties (columns) from your Notion database [00:03:42].

## Configuring PDF Output

After loading properties, configure the PDF output:
1.  **Output File Name**: Select a Notion property (e.g., "first name") from the dropdown to name the generated PDF files [00:03:51].
2.  **Output Folder**: Choose "Google Drive" as the destination [00:04:01]. You can create a new folder in Google Drive, such as "invitation docs," and then select it within PDFoutput.com [00:04:04]. Alternatively, you can opt for the "downloads folder" to save files to your local machine [00:04:34].
3.  **Mapping Fields**: In your Google Doc template within PDFoutput.com, replace placeholder text (e.g., "first name" and "last name") with the corresponding properties fetched from Notion [00:04:42]. Simply click on the Notion property in PDFoutput.com to copy it, then paste it into the Google Doc template [00:04:56].

## Generating PDFs

Once all settings are configured, click "export PDF" [00:05:15]. PDFoutput.com will begin [[generating_bulk_pdf_documents_using_google_docs_and_notion | generating the PDF documents]] in bulk, replacing the mapped fields with data from each row in your Notion database [00:05:17]. The "PDF generated" count will increase as documents are created [00:05:23].

After generation is complete, click "view in Google drive" to open the destination folder [00:05:49]. You will see individual PDF documents, each customized with the respective first and last names from your Notion database [00:05:58].

## Additional Features

PDFoutput.com also offers:
*   **Templates**: Access predefined templates for various purposes [00:06:26].
*   **History**: View a record of all previously generated documents [00:06:33].
*   **Upgrade Options**: Explore different plans for enhanced features [00:06:41].
*   **Contact Section**: Reach out for support or queries [00:06:54].