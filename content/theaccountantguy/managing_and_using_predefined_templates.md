---
title: Managing and Using Predefined Templates
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[automating_pdf_generation_with_userdefined_templates | generate PDF documents in bulk]] using a Google Document as a template and a Notion database to supply the elements for replacement within the template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Adding and Managing Google Document Templates

To use PDF Output, the initial step involves adding a Google Document that will serve as the template <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. There are several ways to add a template, which facilitates [[managing_pdf_templates_and_storing_documents_in_google_drive | managing PDF templates and storing documents in Google Drive]]:

*   **Create a blank document** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>: A new, empty Google Document can be created directly from the PDF Output interface <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Once created, it can be renamed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Choose an existing document from Google Drive** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>: Users can select any pre-existing Google Document stored in their Google Drive <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   Documents can be searched for by name using the search bar <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Using Predefined Templates** <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>: PDF Output provides a library of pre-made templates, such as an [[using_templates_to_generate_pdf_invoices | invoice template]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   These predefined templates are often restricted for direct editing <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. To use them, users can either:
        *   Make a copy of the template in their own Google Workspace <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
        *   Copy all content from the predefined template and paste it into a newly created blank document <a class="yt-timestamp" data-t="00:07:52">[00:08:01]</a>.

## Customizing Templates for Data Replacement

Templates are customized by inserting placeholders for the data that will be pulled from a Notion database. This process is crucial for [[customizing_templates_and_calculating_sales_data | customizing templates]].

1.  **Identify replaceable fields**: Within the Google Document template, identify the specific text segments that need to be replaced by dynamic data (e.g., "customer name" or "salutation") <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
2.  **Set up Notion Database**: Create or select a Notion database that contains the data corresponding to the placeholders in the Google Document <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
    *   Connect the Notion database to PDF Output, ensuring the necessary pages are selected and access is allowed <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Ensure the Notion database has columns (properties) that match the intended placeholders in your Google Document template <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
    *   If new columns are added to the Notion database, click "refresh properties" in PDF Output to fetch them <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   For databases connected to other Notion databases, it is important to select all connected databases during the approval process to ensure all necessary data is available <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Mapping Database Properties to Template Placeholders

This is where [[mapping_database_properties_to_template_placeholders | mapping database properties to template placeholders]] and [[automatically_mapping_database_properties_to_template_elements | automatically mapping database properties to template elements]] takes place:

1.  From the PDF Output interface, click on the desired Notion database property name (e.g., "salutation" or "customer name"); this action copies the property's placeholder value <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  Navigate to the Google Document template and paste the copied placeholder directly over the text you wish to replace <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This ensures that the system knows which Notion database property maps to which part of the document <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Generating PDF Documents

Once the template is prepared and the Notion database is connected and mapped, PDF documents can be generated:

1.  Click the "Export PDF" button in the PDF Output interface <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  Complete any necessary Google authentication <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
3.  PDF Output will read each row of data in the Notion database, apply the mapped properties to the Google Document template, and generate individual PDF files <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  The generated PDFs will automatically download, with each document reflecting the specific data from a corresponding row in the Notion database <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Additional Template Management Features

*   **Search Properties**: A search bar is available to quickly find specific properties within your connected database <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Sorting**: Properties can be sorted for easier management <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Refresh Properties**: This function updates the available properties from the Notion database, particularly useful after adding new columns <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.