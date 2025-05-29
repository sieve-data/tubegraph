---
title: Generating PDF documents in bulk
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_for_business_needs | Generating PDF documents in bulk]] is a process that can be automated using tools like PDFoutput.com, which leverages Google Documents as templates and Notion databases for dynamic data [00:00:02]. This method allows for the creation of numerous personalized PDF files efficiently.

## Using PDFoutput.com

PDFoutput.com is a tool designed to [[using_pdf_output_com_for_bulk_pdf_generation | generate PDF documents in bulk]] by combining Google Docs templates with data from a Notion database [00:00:02].

### Getting Started
1.  **Access the Tool**: Navigate to PDFoutput.com [00:00:10].
2.  **Create PDF**: Click on "create PDF" [00:00:12].
3.  **Sign In**: Sign in with a particular Google account [00:00:15].
4.  **Grant Access**: Enable the checkbox to give PDFoutput access to specific files for its use [00:00:22]. After enabling, click "continue" to be redirected to the homepage [00:00:29].

### Setting up the Template

PDFoutput.com allows users to either use pre-populated PDF templates or add a raw Google Document [00:00:34].
*   **Selecting a Google Document**: Click the link next to "Google document" to browse documents from Google Drive [00:00:42]. For example, an "invitation letter PDF output invitation letter" document can be selected for use [00:00:49]. This document can include references for dynamic data like "first name" and "last name" [00:00:57].
*   **Adding the Document**: Within PDFoutput, click to add the chosen Google Document [00:01:08].

### Integrating with Notion

To [[generating_pdfs_in_bulk_with_notion | generate PDFs in bulk with Notion]], a Notion database is used to store the dynamic data that will populate the Google Document template [00:01:01].

#### Notion Database Setup
1.  **Select Notion**: Choose "Notion" from the dropdown menu in PDFoutput [00:01:22].
2.  **Create a Notion Database**:
    *   Open the Notion workspace by clicking the provided link [00:01:28].
    *   Create a new page, for example, "PDF output database" [00:01:39].
    *   Inside the new page, type `/database` and select "inline" to create a new database [00:01:49].
    *   Name the database (e.g., "database PDF output") [00:01:53].
    *   Rename default columns to match the dynamic fields in the Google Document (e.g., "first name" and "last name") [00:02:01].
    *   Add data entries (e.g., Priya Sharma, Miller Stark, John Quotes) [00:02:11].
3.  **Get Database URL**: Once the database view is active, click "share" and then "copy link" to obtain the database URL [00:02:42]. Paste this URL into PDFoutput [00:02:45].
4.  **Create API Key**:
    *   Click "add API key" in PDFoutput [00:02:50].
    *   Create a new API key (e.g., "notion PDF output connection") [00:02:54].
    *   Copy the generated API key value [00:03:13]. Paste this key into PDFoutput [00:03:19].
5.  **Connect Database to API Key**: In Notion, for the created database, click the three dots, then "connections," and select the "PDF output connection" API key [00:03:26]. Confirm the connection [00:03:34].

### Configuring PDF Generation

After connecting Notion, load the database properties and configure the output settings for the bulk PDF generation.
1.  **Load Properties**: Click "load properties" in PDFoutput to fetch all properties (columns) from the Notion database [00:03:42].
2.  **Define Output File Name**: Select a property (e.g., "first name") from the dropdown to use as the output file name [00:03:51].
3.  **Choose Output Folder**:
    *   **Google Drive**: Select "Google drive" and create a new folder (e.g., "invitation documents from invitation docs") in your Google Drive [00:04:01]. Add this folder in PDFoutput by clicking "add folder" and selecting it [00:04:26].
    *   **Downloads Folder**: Alternatively, choose the "downloads folder" to save files directly to your desktop's downloads [00:04:35].
4.  **Map Fields**: Replace placeholders in the Google Document template with the fetched Notion properties [00:04:42]. Copy the property names (e.g., `first name`, `last name`) directly from PDFoutput's fetched properties and paste them into the corresponding locations in the Google Doc [00:04:51].

### Exporting and Managing Generated Documents

Once all settings are configured, the [[bulk_pdf_document_exportation | bulk PDF document exportation]] process can begin.
1.  **Export PDF**: Click "export PDF" to start [[using_pdf_outputcom_for_bulk_pdf_creation | generating the documents]] [00:05:15].
2.  **Monitor Generation**: The "PDF generated" count will increase as documents are created [00:05:23].
3.  **View Generated PDFs**: Once complete, click "view in Google drive" to open the folder containing the newly generated PDFs [00:05:50]. Each PDF will have the dynamic data (e.g., Jonty Roads, Mirror Stark, Priya Sharma) correctly replaced in the template [00:05:58].

### Additional Features

*   **Templates**: PDFoutput.com offers predefined templates that can be used [00:06:26].
*   **History**: A history feature allows users to view all documents generated in the past [00:06:33].
*   **Upgrade**: Users can upgrade to specific plans [00:06:41].
*   **Contact**: A contact section is available for questions or queries [00:06:54].