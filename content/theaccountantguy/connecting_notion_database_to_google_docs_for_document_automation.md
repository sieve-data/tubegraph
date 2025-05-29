---
title: Connecting Notion database to Google Docs for document automation
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_in_bulk_using_google_docs_and_notion | generate PDF documents in bulk]] by combining a Google Document as a template with a [[connecting_a_database_in_notion | Notion database]] to supply the data for replacement [00:00:06].

## Getting Started with PDF Output

To begin, users need to log in at PDF Output's website [00:00:19]. The interface allows for adding a Google Document and a Notion database, after which PDF documents can be exported [00:00:27].

### Adding a Google Document Template

There are two primary ways to add a Google Document to be used as a template:
1.  **Create a blank document** from scratch [00:00:40].
2.  **Choose an existing document** from Google Drive [00:00:44].

For instance, a blank document can be created by clicking the "create document" button and selecting a Google account [00:00:49]. Once created, the document can be renamed, such as "Invitation Template" [00:01:07]. This Google Document will serve as the template, containing placeholder fields (e.g., "customer name") that will be replaced with data from a [[connecting_a_database_in_notion | Notion database]] [00:01:37].

If using a pre-existing template, like an [[using_notion_database_as_an_invoice_source | invoice]] template available in PDF Output, users can make a copy to their Google workspace or copy its content into a new blank document [00:07:46].

### [[connecting_notion_database_to_pdf_output_via_api_keys | Connecting a Database in Notion]]

The next step involves [[connecting_a_database_in_notion | connecting a Notion database]] to the PDF Output tool [00:02:26].

#### Creating a Notion Database
If a database doesn't exist, one can be quickly created in Notion. For example, a new page can be set up as a table and named "Invitation List" [00:02:53]. This table will hold the data, such as "salutation" and "customer name," which will populate the Google Document template [00:04:09].

#### Linking to PDF Output
Once the database is created, it can be selected from the Notion account via PDF Output's interface [00:02:43]. After selecting the database (e.g., "invitation list") and allowing access, it will be connected to PDF Output [00:03:09].

### Mapping Notion Data to Google Doc Template

After [[connecting_a_database_in_notion | connecting the Notion database]], its properties (columns) will be displayed in PDF Output [00:03:22]. If new columns are added to the Notion database, clicking "refresh properties" will fetch the updated list [00:04:46].

To map data:
1.  Click on a Notion property (e.g., "salutation") to copy its value [00:05:02].
2.  Paste this copied value into the corresponding placeholder in the Google Document template (e.g., replacing "Mr" with the "salutation" field) [00:05:04].
3.  Repeat for other fields, such as "customer name" [00:05:12].

This process tells the system to replace the template's placeholders with the respective values from each row of the [[connecting_a_database_in_notion | Notion database]] [00:05:28].

### [[exporting_documents_from_a_notion_database | Exporting PDF Documents]]

Once the template is ready and the database is connected with mapped fields, click "export PDF" [00:05:40]. An initial Google authentication may be required [00:05:45]. After authentication, the tool will process each row of the Notion database and [[generating_pdf_documents_in_bulk_using_google_docs_and_notion | generate a separate PDF document]] for each [00:06:02]. These PDFs will then automatically download [00:06:09].

For example, if the Notion database contains three customer entries (Mr. Vikash, Mr. Sanat, Mrs. Satabdi), three distinct PDF invitations will be generated, each personalized with the correct salutation and name [00:06:21].

### Advanced Considerations

*   **Connected Databases**: If a primary Notion database is linked to other databases, ensure all connected databases are selected when granting access to PDF Output [00:07:07].
*   **Template Options**: PDF Output offers pre-built [[integrating_google_docs_templates_with_notion_database | Google Docs templates]] that users can copy and adapt [00:07:22].
*   **Search and Sort**: Users can search for specific properties within the Notion database or sort values for easier management [00:08:12].

This system streamlines the creation of personalized documents by leveraging the dynamic data storage of Notion and the formatting capabilities of Google Docs [00:06:39].