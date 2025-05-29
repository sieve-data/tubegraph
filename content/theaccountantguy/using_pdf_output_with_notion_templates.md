---
title: Using PDF Output with Notion Templates
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article details how to generate payment receipt PDF documents by [[using_notion_database_and_templates_for_pdf_generation | using a Notion database with a Notion template]] through the PDFOutput platform <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Accessing PDFOutput and Templates

To begin, users must log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. After logging in, the main interface allows navigation to the "Templates" section <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This page lists all available templates for [[generating_pdfs_from_notion_using_pdfoutput | PDFOutput]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Templates can be searched by name or filtered and sorted <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For payment receipts, the "payment receipts PDF generator" template is used <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Understanding Notion Templates and Databases

When the "payment receipts PDF generator" template is opened, it displays both the database and the template <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

*   **Template Structure**: The Notion template contains predefined elements for PDF output <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, and `{amount paid}`, are placeholder text elements <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Database Integration**: These placeholder elements are replaced by corresponding information from columns in the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For successful syncing and output generation, the exact naming convention of the placeholder text in the template must match the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Customization**: The entire template is customizable to fit specific requirements, allowing changes to formatting (e.g., bolding elements, adding spacing) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## [[Connecting and setting up PDF output with Notion | Setting Up PDFOutput with Notion]]

To use a template with PDFOutput, it must first be duplicated to a Notion workspace <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
1.  **Duplicate Template**: If the template is not published to the Notion gallery, click the "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If it is published, click "start with this template" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Choose the desired Notion workspace for duplication <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  **Add Template to PDFOutput**: Navigate to the "Settings" section in PDFOutput <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Click "click here to add templates" to link the duplicated Notion template <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Select Workspace and Pages**: Choose the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Select the specific Notion payment receipts PDF generator file and click "allow access" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This initiates the reading of template and database elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## [[Connecting Notion database and templates to PDF output | Mapping Notion Properties]]

Once the template and database are loaded in PDFOutput, the next step is to map the properties:
1.  **Select Database and Template**: On the PDFOutput screen, select the "payment receipts database" from the dropdown and the corresponding "payment receipt template" <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  **Naming and Mapping**: Give the connection a name (e.g., "payment receipt") <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. PDFOutput automatically maps Notion properties (database columns) on the left to the template elements on the right if their names match <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
3.  **Manual Mapping/Corrections**: If any elements are mismatched, they can be manually selected and mapped <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The mapping view also includes filter, search, and sort options to manage properties <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Generating PDF Documents

With all settings configured, click "export" to generate the PDFs <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **PDF Status Column**: PDFOutput automatically adds a "PDF status" column to the Notion database <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. As each row's PDF is generated, its status in this column will be marked as "ticked" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Preview and Download**: After successful export, users can preview a sample PDF <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. All generated files can be downloaded <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Each generated PDF corresponds to a specific row in the Notion database, with all elements placed correctly <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Additional Features

*   **Connections**: The "Connections" section in PDFOutput displays all past connections, allowing users to quickly load previously configured databases and templates for regeneration without manual re-setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Templates**: Users can select and manage multiple templates <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Watermarks and Plans**: Free plans will include a PDFOutput watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Settings**: Within settings, users can change the page format of the PDFs <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Feedback**: A feedback option allows users to send messages directly to the support team <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Help**: The "Help" section provides a demonstration video to guide users through the setup process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

For any questions or assistance, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.