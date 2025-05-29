---
title: Bulk PDF document generation
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[creating_pdf_documents_for_business_needs | Bulk PDF document generation]] is a process that enables the creation of numerous PDF files by leveraging a template and a database [00:00:04]. This guide focuses on using PDFoutput.com with Google Documents as templates and Notion databases as data sources [00:00:07].

## PDFoutput.com Overview

PDFoutput.com is a tool designed to [[generating_pdf_documents_for_business_purposes | generate PDF documents in bulk]] [00:00:04]. It integrates with Google Documents for templating and Notion for data management [00:00:07].

### [[pdfoutput_software_setup_for_document_generation | PDFOutput Software Setup]]

To begin, navigate to PDFoutput.com and click "create PDF" [00:00:12].

1.  **Sign In**: Sign in using a Google account [00:00:15].
2.  **Grant Access**: Enable the checkbox to give PDFoutput access to specific files [00:00:22]. This step is necessary for the tool to function [00:00:27]. After enabling, click "continue" to be redirected to the homepage [00:00:29].

## Setting Up the Template

PDFoutput allows the use of pre-populated templates, but a raw Google Document can also be used for customization [00:00:37].

1.  **Select Google Document**: Click the link next to "Google document" to view documents from your Google Drive [00:00:42]. Choose the desired document to serve as the template, such as an "invitation letter" [00:00:49].
2.  **Identify Placeholders**: In the Google Document template, identify placeholders that will be replaced by data from the Notion database (e.g., `first name`, `last name`) [00:00:57].
3.  **Map Placeholders**: Within PDFoutput, after loading the Notion database properties, map these placeholders (e.g., `first name`, `last name`) to their corresponding properties from the Notion database [00:04:41]. These mapped properties will then be replaced in the generated PDF [00:05:10].

## Connecting to a Notion Database

A Notion database serves as the data source for [[bulk_pdf_document_generation_using_notion | bulk PDF document generation]] [00:01:01].

### Creating the Notion Database

1.  **Create a New Page**: In your Notion workspace, create a new page, for example, named "PDF output database" [00:01:39].
2.  **Create an Inline Database**: Type `/database` and select "inline" to create a new database [00:01:49]. Name the database (e.g., "database PDF output") [00:01:53].
3.  **Define Columns**: Rename default columns to match your placeholders, such as "first name" and "last name" [00:02:01].
4.  **Populate Data**: Add entries with relevant data into the columns (e.g., "Priya Sharma", "Miller Stark", "John Rhodes") [00:02:11].

### Obtaining Database URL

1.  **Share Database**: While viewing the database in Notion, click "share" [00:02:42].
2.  **Copy Link**: Click "copy link" to copy the database URL [00:02:44].
3.  **Paste URL**: Paste the copied database URL into the "database URL" field in PDFoutput [00:02:47].

### Generating Notion API Key

An API key is required to connect the Notion database to PDFoutput [00:02:48].

1.  **Create New Key**: In Notion, create a new integration or API key [00:02:52]. Name it (e.g., "notion PDF output connection") [00:02:57].
2.  **Copy Key**: Once created, view the key and copy its value [00:03:13].
3.  **Paste Key**: Paste the copied API key into the "API key" field in PDFoutput [00:03:19].

### Connecting Database to API Key

Ensure the Notion database is connected to the newly created API key.
1.  **Add Connection**: In the Notion database, click the three dots, then "connections" [00:03:26].
2.  **Select API Key**: Type and select the "PDF output connection" (or your API key name) and click "confirm" [00:03:28].

## Configuring Output

After connecting the Notion database, load its properties into PDFoutput [00:03:42].

1.  **Load Properties**: Click "load properties" in PDFoutput to fetch all columns from your Notion database [00:03:42].
2.  **Define Output File Name**: Select a property (e.g., "first name") from the dropdown to be used for naming the generated PDF files [00:03:51].
3.  **Choose Output Location**:
    *   **Google Drive**: Select "Google drive" and create a new folder (e.g., "invitation documents") in your Google Drive [00:04:01]. Then, select this folder within PDFoutput [00:04:26].
    *   **Downloads Folder**: Alternatively, choose "downloads folder" to save files directly to your desktop's download directory [00:04:35].

## [[bulk_pdf_document_export_process | Bulk PDF Document Export Process]]

Once all settings are configured, the [[bulk_export_of_pdf_documents | bulk export of PDF documents]] can begin.

1.  **Initiate Export**: Click "export PDF" to start the [[exporting_bulk_pdf_documents_from_a_database | document generation process]] [00:05:15].
2.  **Monitor Progress**: The "PDF generated count" will increase as documents are created [00:05:23].
3.  **Verify Generated Documents**: After generation, click "view in Google drive" (if selected) to open the output folder [00:05:50]. Verify that the placeholders in the documents have been replaced with the corresponding data from the Notion database (e.g., "Jonty Rhodes", "Miller Stark", "Priya Sharma") [00:05:58].

This process allows for [[bulk exporting and downloading generated PDF files | generating PDF documents in bulk]] based on the information added to the Notion database [00:06:21].

## Additional Features

PDFoutput also provides other useful features:

*   **Predefined Templates**: Access a selection of predefined PDF templates for various purposes [00:06:26].
*   **Export History**: View a history of all previously generated documents [00:06:33].
*   **Upgrade Options**: Options to upgrade to a specific plan are available [00:06:41].
*   **Contact Support**: A contact section is provided for any questions or queries [00:06:54].