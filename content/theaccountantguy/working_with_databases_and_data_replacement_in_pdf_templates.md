---
title: Working with databases and data replacement in PDF templates
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 
PDF Output is a tool designed to [[generating_bulk_pdfs_with_database_integration | generate PDF documents in bulk]] by using a Google Document as a template and a Notion database to supply the data for replacement within that template <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## How PDF Output Works <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

The process involves three main steps after logging into PDF Output:
1.  Adding a Google Document to serve as the template <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Connecting a Notion database that holds the data for the PDF generation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
3.  Exporting the PDFs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## [[creating_and_using_templates_for_pdf_generation | Creating and using templates for PDF generation]]

To begin, you need to add a Google Document that will serve as your PDF template.
You have two options for adding a document:
*   **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This option creates a new Google Doc connected to your account <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. You can rename it (e.g., "Invitation template") <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. You can search for specific documents by name <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

Within the Google Document, you will define the fields that need to be replaced with data from your database. These fields are typically placeholders (e.g., `salutation`, `customer name`) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

PDF Output also offers pre-added templates (e.g., an invoice template) that you can use. To utilize them, you can either:
*   Make a copy of the template into your Google workspace by going to File > Make a copy <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   Copy all content (Ctrl+A, Ctrl+C) from the template and paste it into a blank Google Document you've created <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## [[managing_templates_and_databases_in_pdfoutput | Managing Templates and Databases in PDFOutput]]

### Connecting a Notion Database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>

After setting up your template, the next step is to connect a Notion database:
1.  Click "add notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Authenticate with your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Select the specific Notion pages or databases you want to grant access to <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For example, you might create a new database called "invitation list" in Notion <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
4.  Once connected, the database and its properties (columns) will be displayed in PDF Output <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

If you add new columns (properties) to your Notion database after connecting it, click the "refresh properties" button in PDF Output to fetch the new properties <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### [[mapping_database_elements_to_templates_for_pdf_generation | Mapping database elements to templates for PDF generation]]

To link your Notion database fields to your Google Doc template:
1.  In PDF Output, select the Notion database property you want to use (e.g., "salutation" or "customer name") <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Clicking on a property name copies its value <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
2.  Go to your Google Document template and paste the copied property value into the desired placeholder <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. For example, you would paste `{{salutation}}` and `{{customer name}}` into your template <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

The connection between the template and the database is live, meaning any changes made to the database fields will be reflected when generating PDFs <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Working with Connected Databases <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>

If your Notion database has connections to other databases, ensure you choose all connected databases when approving the database list to allow PDF Output to access all necessary data <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## [[generating_pdfs_from_database_entries | Generating PDFs from database entries]]

Once your template and database are connected and the fields are mapped, you can generate the PDFs:
1.  Click "export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  Complete the Google authentication process if prompted <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
3.  The tool will read every row in your Notion database and generate a separate PDF document for each entry <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  The generated PDFs will then be downloaded to your device <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. For example, if your database has three entries, three distinct PDFs will be created, each personalized with the data from a specific row <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.