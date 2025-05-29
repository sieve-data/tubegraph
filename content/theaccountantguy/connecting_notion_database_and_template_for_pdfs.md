---
title: Connecting Notion database and template for PDFs
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate PDF documents, such as purchase orders, using a [[using_notion_as_a_template_and_database_for_pdfs | Notion database]] and a Notion template via PDF output.com <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Initial Setup

1.  **Log In to PDF output.com**
    *   Navigate to PDF output.com and log in <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
    *   The interface displays options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

2.  **Select a Predefined Template**
    *   On the right sidebar, click on "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   This loads a list of predefined templates like invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   You can use the search icon to find a specific template <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
    *   Click the "Download" link next to your desired template, such as the purchase order template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Understanding Notion Templates and Databases

When you download a template, it opens a specific "PDF generator page" that includes both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. These will be [[connecting_notion_with_pdf_output_via_api | connected to PDF output]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Notion Template Structure
*   The template defines the layout and fixed text of your PDF document, including elements like purchase order, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   Placeholder elements that will be replaced by database values are enclosed in curly braces, e.g., `{{Purchase Order Number}}`, `{{Date}}`, `{{Supplier Name}}`, `{{Buyer Name}}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Notion Database Structure
*   The database contains the variable data that will populate the template <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   It has columns corresponding to the placeholder names in the template (e.g., supplier name, buyer name, date, purchase order number) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Each row in the database represents a unique PDF document to be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The system [[creating_pdf_documents_from_notion_database | generates PDF documents]] for each row, replacing the template's placeholder text with the corresponding column values <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Customization Notes
*   Both the template and the database elements are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Ensure that all values intended for replacement are placed inside curly braces in the template <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   The name of the database column must exactly match the name of the placeholder in the template (e.g., no extra commas or spaces) for automatic linking <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## [[Setting up Notion templates and databases for PDF generation | Setting Up Notion Templates and Databases for PDF Generation]]

1.  **Duplicate the Template to Your Notion Workspace**
    *   On the PDF generator page, find the "Duplicate" or "Start with this template" option at the top <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   Clicking "Duplicate" will prompt you to select your Notion workspace to add the page <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Once added, the "Purchase Order PDF Generator" page will appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

2.  **Connect Notion Workspace to PDF Output**
    *   Go back to PDF output.com <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Click on "Settings" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   You can set the desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   A new window will open, showing your connected Notion workspaces <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Select the workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   Click "Select Pages" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   Choose the "Purchase Order PDF Generator" page and click "Allow access" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This authenticates and [[connecting_notion_with_pdf_output_via_api | connects the Notion page with PDF output]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Wait for successful authentication and redirection back to the PDF output page <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## [[Linking databases and creating templates in Notion | Linking Databases and Creating Templates in Notion]]

1.  **Select Database and Template in PDF Output**
    *   Once redirected, refresh the PDF output page if necessary <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
    *   From the Notion database dropdown, select your "Purchase Order" database <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   From the Notion template dropdown, select the specific "template page" within the "Purchase Order PDF Generator" <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Give your connection a name, e.g., "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

2.  **Map Properties**
    *   The system will load the database and template elements and attempt to automatically match them <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   Notion properties (from your database) are displayed on the left, and template elements (from your template) are on the right <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   If any elements are unmatched (e.g., due to a mismatch in naming like a space in one but not the other), you can manually map them <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
        *   Use the "Filter unmapped properties" option to quickly find unmatched items <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
        *   Click on the unmatched element and select the corresponding item from the other list to link them <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   You can also use the search or sorting options <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## [[Generating PDF documents from a Notion database | Generating PDF Documents from a Notion Database]]

1.  **Export**
    *   Once all properties are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
    *   A "PDF Status" column will automatically be added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF is generated for a row, this checkbox will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a PDF, ensure this box is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   After successful export, you will be able to preview a sample <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The preview will show how the database values have populated the template <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

2.  **Download Documents**
    *   Click "Download all documents" to get all generated PDFs <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   The documents will be saved in an output folder, typically named according to a unique identifier from your database (e.g., "Purchase Order Number Two") <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## Additional Features

*   **Connections:** After generating a PDF, the system creates a connection that stores your database and template selections <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. You can click on this connection to quickly regenerate documents without re-filling all details <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Upgrade:** Free plans will have a watermark on generated PDFs; paid plans remove it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Define your desired page format for PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** If you encounter issues, use the feedback option to report problems <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help:** The help section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific use cases, you can reach out via email <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.