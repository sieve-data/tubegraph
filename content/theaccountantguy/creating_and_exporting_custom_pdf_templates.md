---
title: Creating and exporting custom PDF templates
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

PDFoutput.com is a tool designed to [[generating_and_exporting_pdf_documents_for_business | generate PDF documents]] in bulk by utilizing Google Docs as [[creating_and_using_templates_for_pdfs | templates]] with the assistance of a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started

To begin, navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
1.  Click on "create PDF" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
2.  Sign in through your Google account <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
3.  Enable the checkbox to grant PDFoutput access to specific files <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
4.  Click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Selecting a Google Doc Template

While PDFoutput offers pre-populated PDF [[creating_and_using_templates_for_pdfs | templates]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, you can also use your own Google Document as a raw template <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

1.  Click the link next to "Google document" to view documents listed on your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  Select the desired Google Doc, such as an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  This document will serve as the base template, where specific fields (e.g., first name, last name) will be replaced with data <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Connecting to a Notion Database

Data for your PDF [[customizing_templates_for_pdf_generation | templates]] can be sourced from a Notion database <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

1.  From the dropdown menu, select "Notion" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  You will need a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Setting up Notion Database

1.  Click the provided link to open your Notion workspace <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  Inside the new page, type `/database` and select "inline" to create a database <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
4.  Rename columns as needed, for example, "first name" and "last name" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
5.  Populate the database with your data (e.g., names like Priya Sharma, Miller Stark, John Quotes) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
6.  Once the database view is active, click "share" and then "copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into PDFoutput <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Creating and Connecting Notion API Key

1.  Click the "add API key" link in PDFoutput <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Create a new key, naming it something descriptive like "Notion PDF output connection" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
3.  Select your Notion account and click "save" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  Go back to the API key you just created, click "show," and copy the key's value <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Paste this key into PDFoutput <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
5.  Crucially, ensure your Notion database is connected to this API key <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. In Notion, click the three dots on your database, select "connections," and type in "PDF output connection" to confirm the link <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Loading Database Properties

After connecting the database URL and API key, click "load properties" in PDFoutput <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This action will fetch all the properties (columns) from your Notion database and display them <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Customizing and Exporting PDF Documents

### Defining Output Settings

1.  **Output File Name**: Select a property from your Notion database (e.g., "first name") to use as the generated PDF's file name <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Save Location**: Choose "Google Drive" to save the documents to a specified folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Alternatively, select "downloads folder" to save them to your desktop <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
    *   To create a new Google Drive folder, navigate to your Drive, click "new," then "new folder," and name it (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   In PDFoutput, click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Mapping Template Fields

To replace placeholders in your Google Doc template with data from Notion:
1.  Copy the property names (e.g., `{{first name}}`, `{{last name}}`) directly from the properties fetched in PDFoutput <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
2.  Paste these property names into your Google Doc where you want the corresponding data to appear <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   You can format these placeholders (e.g., bold, red) within the Google Doc <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   The first name and last name fields are now mapped to the Notion database properties <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Exporting PDFs in Bulk

Once all settings are defined, click "export PDF" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   PDFoutput will begin [[exporting_and_managing_pdf_documents | generating PDF documents]] in bulk, saving them to your specified Google Drive folder or local downloads <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   A counter will show the number of PDFs generated <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   After completion, you can click "view in Google drive" to open the folder and verify the generated documents <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

For example, if the Notion database contained "Jonty Roads," "Mirror Stark," and "Priya Sharma," three separate PDF documents would be generated, each personalized with the respective name <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. The more information added to the Notion database, the more documents will be generated <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates**: PDFoutput includes predefined [[creating_and_using_templates_for_pdfs | templates]] that can be used directly <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: The history section allows you to view all documents generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade**: Options to upgrade to a specific plan are available <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

For any questions or queries, a contact section is available at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.