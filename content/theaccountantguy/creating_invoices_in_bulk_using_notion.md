---
title: Creating invoices in bulk using Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 
The following article details how to create invoices in bulk using a Notion database and PDFOutput.

## Creating Invoices in Bulk Using Notion

This process demonstrates how to utilize a Notion page and Notion template to generate PDF documents, specifically focusing on [[generating_invoices_from_a_notion_database | invoices PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Getting Started with PDFOutput

The first step is to log in to PDFOutput.com, which is the platform used to create these documents <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

### Template and Database Setup

1.  **Accessing Templates**: Navigate to the "template" section on PDFOutput.com <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Here, you'll find a list of pre-created templates <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For invoices, select and download the [[creating_a_professional_invoice_template_in_notion | invoices template]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Understanding the Template and Database**: Once downloaded, the template and its corresponding database will be displayed <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
    *   The template includes elements like client name, company, address, invoice number, date, and terms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   Elements enclosed in curly braces (e.g., `{client name}`) are placeholder texts that will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   The database columns (e.g., "Invoice Number", "Date", "Client Name") must match the naming conventions of the placeholder texts in the template exactly <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Each row in the database corresponds to a unique invoice PDF that will be generated <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
3.  **Duplicating the Template to Notion**: Click the "start with this template" option on PDFOutput, which will prompt you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Select your desired Notion workspace and click "add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The template and its associated database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Connecting Notion to PDFOutput

1.  **Add Template in PDFOutput Settings**: Go back to PDFOutput and click on "settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Select "add template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Select Notion Template**: Choose the specific Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Then, select the "Invoice Generator Template" from the list of available pages and click "allow access" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This authenticates and adds the template to your PDFOutput setup <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Synchronization**: Allow a few seconds for PDFOutput to sync all database and template elements <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Customizing and Mapping Data

*   **Template Customization**: The template in Notion is fully customizable. You can add, delete, or modify values. Ensure that all placeholder text elements remain inside curly braces and that their names precisely match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Data Mapping**: Once synced, PDFOutput will display Notion properties (database columns) on the left, automatically mapping them to the corresponding template elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Mapped elements will be indicated by a green bar <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If any property is not mapped, you can manually select and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Selecting Database and Template**: On the PDFOutput screen, select the synced Notion database and the "professional invoice template" you added <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Give your generation a name and click "next" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Generating PDF Invoices

1.  **Exporting**: Click "export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
2.  **PDF Status Column**: In your Notion database, a "PDF status" column will appear. As each document is generated, the corresponding row in Notion will automatically get checked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download**: After successful export, you can preview a sample invoice <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Then, click "download all" to get all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Considerations

*   Before generating new documents, ensure the "PDF status" column for the relevant rows in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   On the free plan, generated PDFs will include a watermark. To remove it, an upgrade to a paid plan is required <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   Previously configured connections (database and template pairings) are saved under the "connections" section, allowing for quick regeneration without re-mapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   Additional help and setup instructions can be found in the "help" section of PDFOutput <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   For questions or feedback, contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.