---
title: Using PDF output com to create bulk PDF documents
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

PDF Output.com is a tool designed to [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generate PDF documents in bulk]] by leveraging Notion templates and databases <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process allows users to automate the creation of numerous documents, such as payment receipts, by replacing specific elements in a template with data from a database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Core Components
The system relies on two main components within Notion:
*   **Notion Template:** This is a pre-designed document containing elements enclosed in curly braces (e.g., `{receipt number}`). These elements act as placeholders for information that will be dynamically inserted <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Notion Database:** This database stores the actual data for each document to be generated <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Each column in the database ideally corresponds to an element in the template, ensuring a smooth mapping process <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

For example, a payment receipt template might have placeholders for `{receipt number}`, `{receipt date}`, `{receipt time}`, `{customer name}`, and `{company website}` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The corresponding Notion database would contain rows of information, with each row representing a unique payment receipt, and columns for each of those elements <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Step-by-Step Process for Bulk PDF Generation

To [[generating_and_downloading_pdf_documents_in_bulk | generate and download PDF documents in bulk]] using PDF Output.com:

1.  **Access PDF Output.com:** Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Log In:** Log in to your account <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The interface will prompt you to connect a Notion database and template <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
3.  **Duplicate Notion Templates and Databases:**
    *   Go to the "Template" section within PDF Output.com to find predefined templates, such as "Payment Receipts" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   For each template, there will be a "database link" and a "template link" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   Click these links to open them in new windows and then use the "Duplicate" option within Notion to copy both the template and the corresponding database to your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
4.  **Connect Notion to PDF Output.com:**
    *   Back on PDF Output.com, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Grant permission to PDF Output.com to access your Notion pages by selecting your Notion workspace (e.g., "accountant guy") and the duplicated template and database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Once authenticated, the connected database and template will be displayed <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
    *   Assign a connection name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
5.  **Map Database Properties to Template Elements:**
    *   PDF Output.com will load the database properties and attempt to automatically map them to the template elements <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   If the database column names exactly match the template elements (including spaces and capitalization), the mapping will be automatic <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   For any unmapped properties, you can manually select the correct corresponding element from a dropdown menu <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Filtering and sorting options are available to manage properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
6.  **Generate and Download PDFs:**
    *   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   The system will process each row in the database, reading the data and inserting it into the template to create individual PDF documents <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
    *   After successful export, you can "Preview a sample" PDF to check the output <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   Click "Download all documents" to receive a zip file containing all the generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Each document will be clean and accurate, reflecting the data from the corresponding database row <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Important Considerations

*   **Naming Convention:** To ensure automatic mapping, it is crucial that the column names in your Notion database exactly match the names of the elements in curly braces within your Notion template (including spaces and capitalization) <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Refresh:** If the database and template don't load immediately, click the "refresh" button <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## PDF Output.com Sidebar Features

The sidebar in PDF Output.com provides several useful features:

*   **Connections:** Displays a list of previously created connections for [[exporting_and_managing_pdf_documents_in_bulk | exporting and managing PDF documents in bulk]] <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Selecting an existing connection will automatically load the associated database and template, eliminating the need to manually re-add them <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Templates:** Provides access to various predefined templates for different use cases, such as invoices <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade:** Explains the free plan limitations (e.g., PDF Watermark "made with PDF output") and options to upgrade to paid plans for watermark removal and higher usage limits <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Settings:** Allows users to:
    *   Define the **page format** for generated PDFs (e.g., A4 is default) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   Add more templates and databases for subsequent use <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback:** A window to submit questions or feedback <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Help:** Explains how to use a custom template and database if a predefined template is not suitable <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

For any questions or issues, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.