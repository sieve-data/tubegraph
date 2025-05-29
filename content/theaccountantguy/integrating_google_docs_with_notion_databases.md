---
title: Integrating Google Docs with Notion databases
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents in bulk by [[using Notion templates and databases for PDF creation | using a Google Document as a template]] and a [[creating_and_using_databases_in_notion | Notion database]] to supply the data for replacement [00:00:06].

## Core Process
The general steps to generate documents are [00:00:27]:
1.  Add a Google Document.
2.  Add a [[creating_and_using_databases_in_notion | Notion database]].
3.  Export PDFs.

## Adding a Google Document Template
A Google Document serves as the template for the PDF output [00:00:08].
There are two methods to add a Google Document [00:00:39]:
*   Create a blank document from scratch [00:00:40].
*   Choose an existing document from Google Drive [00:00:44].

### Creating a Blank Document
1.  Select the option to "create document" [00:00:51].
2.  Choose the Google account to connect [00:00:53].
3.  Once created, rename the document (e.g., "invitation template") [00:01:07].
4.  Paste or type content into the blank Google Document [00:01:28].
5.  Identify the fields that need to be replaced with data from the Notion database, such as `salutation` and `customer name` [00:02:14].

### Using an Existing Document
1.  Click "add Google Document" and select the desired Google account [00:03:36].
2.  Search for the specific document by name (e.g., "invitation template") [00:03:45].

### Using Pre-Added Templates
PDF Output offers pre-designed templates, such as an [[using databases in Notion for invoice tracking | invoice template]] [00:07:35].
To use these [00:07:44]:
*   Click "File" then "Make a copy" to save it to your Google Workspace [00:07:46].
*   Alternatively, copy all content (`Ctrl+A`, `Ctrl+C`) and paste it into a new blank Google Document [00:07:53].

## Adding a Notion Database
A [[creating and using databases in Notion | Notion database]] holds the specific data elements that will replace placeholders in the Google Document template [00:00:13].

### Steps to Connect a Database
1.  Click "add Notion database" [00:02:26].
2.  Connect using Notion credentials [00:02:27].
3.  Select the desired pages from your Notion account [00:02:35].
4.  If a database does not exist, [[creating_and_using_databases_in_notion | create a new page]] in Notion and select "table" to form a database (e.g., "invitation list") [00:02:46].
5.  After [[creating_and_using_databases_in_notion | creating the database]] in Notion, it will appear in the selection list [00:03:08].
6.  Click on the database and "allow access" to connect it to PDF Output [00:03:11].
7.  The connected database will show its properties (columns), with 'Name' as a default [00:03:22].
8.  Add new properties (columns) in the Notion database as needed (e.g., `salutation`, `customer name`) [00:04:12].
9.  If new columns are added in Notion, click "refresh properties" in PDF Output to fetch the updated list [00:04:45].

### Populating the Notion Database
Enter data into the Notion database rows. For an invitation template, this might include `salutation` (e.g., Mr., Mrs.) and `customer name` (e.g., Vikash, Sanat, Satabdi) [00:04:25].

### Mapping Notion Properties to Google Doc Template
1.  From the PDF Output interface, click on a Notion property (e.g., `salutation`) to copy its value [00:05:02].
2.  Go to the Google Document template and paste the copied property into the corresponding placeholder [00:05:05].
3.  Repeat for all other properties (e.g., copy `customer name` and paste it into the `customer name` placeholder in the Google Doc) [00:05:12].
*   Changes made in the PDF Output interface are reflected live in the linked Google Document [00:06:51].

### Handling Connected Databases
If your primary Notion database has [[connecting_notion_databases_with_apis | connections to other databases]], ensure you select all connected databases while approving the database list [00:07:07]. You only need to add the main database in PDF Output, but all connected databases must be allowed access to ensure data is pulled correctly [00:07:17].

## Exporting PDFs
Once the Google Document template is ready and the Notion database is connected and mapped [00:05:38]:
1.  Click "export PDF" [00:05:43].
2.  Complete the Google authentication process [00:05:47].
3.  The system will read each row in the Notion database and generate a separate PDF document for each [00:06:02].
4.  The generated PDFs will automatically download [00:06:09]. For example, if there are three customer entries, three personalized invitation PDFs will be created [00:05:38].

## Other Features
*   **Search Properties**: Search for specific properties within the Notion database [00:08:12].
*   **Sorting**: Sort all values for convenience [00:08:20].
*   **Refresh Properties**: Updates the list of Notion database properties if new columns are added [00:04:45].

For further questions, contact notionforuse@gmail.com [00:09:00].