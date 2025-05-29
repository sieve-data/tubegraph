---
title: Setting up and connecting API keys for PDFexport
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[Bulk export of PDF documents using PDF Output | PDFoutput.com]] is a tool designed to [[generating_and_exporting_pdf_documents_for_business | generate PDF documents in bulk]] by utilizing Google documents as templates and a Notion database for data [00:00:02]. To begin, users must first sign in to PDFoutput with a chosen account and enable access to specific files for the application to function [00:00:15].

## Connecting a Notion Database

[[Bulk export of PDF documents using PDF Output | PDFoutput]] utilizes a Notion database to pull data, such as first and last names, for [[generating_and_exporting_pdf_documents_for_business | PDF generation]] [00:01:01].

### Steps to set up a Notion Database:
1.  Navigate to your Notion workspace via the link provided in [[Bulk export of PDF documents using PDF Output | PDFoutput]] [00:01:28].
2.  Create a new page, for example, "PDF output database" [00:01:39].
3.  Within the new page, type `/database` and select "inline" to create a database [00:01:49].
4.  Name the database (e.g., "database PDF output") and rename default columns, such as "first name" and "last name" [00:01:53].
5.  Populate the database with desired names (e.g., Priya Sharma, Miller Stark, John Roads) [00:02:11].
6.  Once the database is set up, click on "share" from the database view and "copy link" to obtain the database URL [00:02:42].
7.  Paste this URL into the "database URL" field in [[Bulk export of PDF documents using PDF Output | PDFoutput]] [00:02:45].

## [[setting_up_and_using_notion_api_keys | Setting up and Using Notion API Keys]]

To connect the Notion database to [[Bulk export of PDF documents using PDF Output | PDFoutput]], an API key is required [00:02:48].

### Steps for [[setting_up_and_using_notion_api_keys | API Key Creation and Connection]]:
1.  In [[Bulk export of PDF documents using PDF Output | PDFoutput]], click on "add API key" [00:02:50]. This will prompt you to create a new key [00:02:52].
2.  Create a new key (e.g., named "notion PDF output connection") and select the relevant account [00:02:54].
3.  Save the key [00:03:07].
4.  Go back to the newly created API key connection, click "show" to reveal the key, and copy its value [00:03:12].
5.  Paste the copied API key value into the API key field in [[Bulk export of PDF documents using PDF Output | PDFoutput]] [00:03:17].
6.  Crucially, ensure the Notion database itself is connected to this API key. In Notion, click on the three dots for the database, select "connections," and type in the name of your API key (e.g., "PDF output connection") [00:03:26]. Confirm the connection [00:03:34].

## Loading Properties and [[exporting_and_managing_pdf_documents | Exporting Documents]]

After the database URL and API key are entered and connected, click on "load properties" in [[Bulk export of PDF documents using PDF Output | PDFoutput]] [00:03:42]. This action fetches all the properties (e.g., "first name," "last name") from the Notion database [00:03:44].

Once properties are loaded, you can define the output file name (e.g., using "first name" from the dropdown) and select the output folder (e.g., a specific Google Drive folder or your desktop's downloads folder) [00:03:51].

To generate the documents, map the fetched properties to the corresponding placeholders in your Google Document template [00:04:42]. For instance, if your template has `{{first name}}` and `{{last name}}`, you would replace these with the mapped "first name" and "last name" properties from Notion [00:04:51].

Finally, click "export PDF" to begin [[exporting_and_managing_pdf_documents | generating the PDF documents]] based on the Notion database entries and the specified template [00:05:15]. The [[steps_for_downloading_and_exporting_pdfs | generated PDFs]] will be saved to your chosen output location [00:05:19]. You can view the generated documents directly in Google Drive [00:05:50].

Other features of [[Bulk export of PDF documents using PDF Output | PDFoutput]] include predefined [[creating_and_exporting_custom_pdf_templates | templates]] and a history section to track past document generations [00:06:26].