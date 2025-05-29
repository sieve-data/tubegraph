---
title: Setting up Notion templates and databases for PDF generation
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate professional PDF documents, such as invoices, in bulk using a Notion template and a Notion database, facilitated by the PDF Output tool <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Core Concept: Notion Template and Database

The process relies on two main components within Notion:
*   A Notion template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>: This template defines the structure of your PDF document. Elements within the template that are enclosed in curly braces (e.g., `{client name}`) act as placeholders <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   A Notion database <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>: This database contains the data that will replace the placeholders in the template. Each column in the database should correspond to a placeholder in the template (e.g., "Client Name" column for `{client name}`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

For automatic mapping of data, it is crucial that the names of the database properties (columns) exactly match the placeholder names in curly braces within the template <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. If the names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Generating PDFs with PDF Output

The PDF Output website (pdfoutput.com) is used to connect your Notion data and template to generate PDFs <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Steps to Generate PDFs:

1.  **Log In**: Navigate to PDF output.com and log in to your account <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Duplicate Templates and Databases**:
    *   Before connecting, you need to duplicate the desired Notion template and database into your own Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   PDF Output provides a "Templates" section with pre-added templates, each with a database link and a template link <a class="yt-timestamp" data-t="00:01:51">[00:02:00]</a>.
    *   Search for the required template (e.g., "invoice") <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on the database link and the template link, then click the "Duplicate" option in the top right corner of Notion to copy them to your Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Connect Notion Database and Template**:
    *   Back in PDF Output, click "Add Database" or "Add Template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace and then choose the duplicated template and database pages <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   Click "Allow Access" to link them to PDF Output <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   Once connected, the selected database and template will be visible <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
4.  **Define Connection Name**: Give your connection a name (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
5.  **Map Properties**:
    *   The software will display database properties on the left and template elements on the right <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   If database properties and template placeholders have identical names, they will be automatically mapped <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   If names differ, you will need to manually click on the grey icon next to a property and search for the corresponding template element to map it <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
6.  **Generate PDF**: Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The tool will generate a PDF document for each row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
7.  **Preview and Download**: After generation, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The downloaded files will be in a ZIP archive <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Additional Features and Tips

*   **Customization**: The template can be entirely customized. Ensure that any data you want pulled from the database is enclosed in curly braces with the exact matching name of the database property <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Reusing Connections**: Once a connection is set up, it will appear under the "Connections" section in the sidebar. You can select it to quickly re-load your database and template and regenerate PDFs without going through the setup process again <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Relational Properties**: If your Notion database uses relational properties linked to other Notion databases, ensure that you also connect those related databases during the initial connection setup <a class="yt-timestamp" data-t="00:10:50">[00:11:13]</a>.
*   **Upgrade Options**: Free plans include a "Made with PDF Output" watermark on generated PDFs. Upgrading to a paid plan removes this watermark and offers higher document generation tiers <a class="yt-timestamp" data-t="00:09:01">[00:09:12]</a>.
*   **Page Format**: Under "Settings," you can define the specific page format (e.g., A4 size) for your PDF documents <a class="yt-timestamp" data-t="00:09:24">[00:09:32]</a>.
*   **Support and Feedback**: A feedback option is available for queries or messages, and a help section demonstrates how to connect custom PDF documents and databases <a class="yt-timestamp" data-t="00:09:59">[00:10:16]</a>.