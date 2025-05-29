---
title: Setting up PDFOutput with API keys
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This tutorial focuses on using PDF Output to [[Using PDF output to generate invoices | generate lease agreement documents]] (PDFs) from a Notion database and page <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Preparing Your Notion Template and Database

### Template Structure
The lease agreement template utilizes placeholder text elements, such as `landlord name`, `tenant name`, and `street address`, enclosed in curly braces. These placeholders will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Database Structure
A Notion database holds the values for each placeholder, including fields like "landlord name," "tenant name," and "street address." These values from individual rows will be imported into the template to replace the placeholder text elements <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Initial PDFOutput Setup

Before generating documents, it's crucial to set up PDF Output.
1.  **Log in to PDF Output** <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
2.  Navigate to the **Help section** within the PDF Output interface <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Follow the instructions provided in the Help section to complete the preliminary steps, especially for [[Utilizing API keys to connect Notion to PDF generation tools | setting up API keys]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Connecting and Mapping Data

Once the initial setup is complete, you can begin [[Setting up PDFOutput for Notion databases | configuring PDFOutput for your Notion databases]].

1.  **Specify Connection Details**:
    *   Enter a connection name (e.g., "Lease Agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Select your Notion database from the dropdown menu, which displays all databases connected via your [[Using API keys to connect databases for PDF generation | API key]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select the corresponding lease template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
2.  **Automatic Mapping**: After clicking "Next," PDF Output loads the database and template elements, automatically mapping them if their names match <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   The left side displays Notion properties (e.g., "landlord name," "tenant name," "street address") from your database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   PDF Output automatically maps these properties to the corresponding template elements <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  **Manual Mapping (if needed)**: If any properties are not automatically mapped (indicated by a gray element), click on the element to view all properties. Unmapped items will be listed in red, allowing you to manually select the correct mapping <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Generating and Exporting PDFs

1.  **Export**: Click "Export" to begin processing the information <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Property**: PDF Output will add a "PDF status" column to your Notion database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Rows that are unticked in this column will be generated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   Once a PDF is generated for a row, PDF Output automatically places a tick mark in the "PDF status" column <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Preview and Download**:
    *   After generation, a "Preview Sample" option becomes available to view a sample PDF <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Click "Download All" to download all generated files in a zip format <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. You can re-download files by clicking "Download" again <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Best Practices for PDF Generation

*   **Customization**: [[Managing PDF Output templates and settings | Customize the agreement template]] and database as per your specific use case <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Naming Conventions**: Ensure the naming convention of your Notion database properties and the template placeholders matches exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

For any questions, reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.