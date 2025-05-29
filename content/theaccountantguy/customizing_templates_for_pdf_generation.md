---
title: Customizing templates for PDF generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

[[Utilizing PDF output for document generation | PDF Output.com]] is a platform that facilitates the generation of PDF documents from Notion databases using predefined or custom templates <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves connecting a Notion database and a Notion template to [[Utilizing PDF output for document generation | PDF Output.com]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Template Selection and Preparation

To begin, users log into PDF Output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface displays options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

1.  **Access Templates:** Navigate to the "Templates" section in the sidebar <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
2.  **Choose or Search:** A list of predefined templates is available, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Users can use the search icon to find specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download Template:** Click the "Download" link next to the desired template (e.g., Purchase Order) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This action opens a new page containing both the database and the template for the selected document type <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
4.  **Duplicate to Notion:** Duplicate the entire page (containing both the template and its associated database) to your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Template Customization

The core of [[Customizing and exporting PDF documents | customizing PDF documents]] lies in modifying the template and ensuring its elements correspond with your Notion database.

### Understanding Template Elements
A template typically includes elements like purchase order number, date, supplier, buyer, and item descriptions <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

-   **Placeholders:** Elements intended to be populated by data from the Notion database are placed within curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These serve as placeholder texts <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
-   **Database Correspondence:** The values from the Notion database (e.g., supplier name, buyer name, date, purchase order number) will replace these placeholder texts <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Customization Guidelines
All template and database elements are [[Customizing invoice elements in PDF documents | customizable]] to fit specific requirements <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

-   **Modification:** Users can add, delete, or modify any values within the template <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
-   **Curly Braces:** Ensure that all values meant to be replaced from the database are enclosed in curly braces <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This identifies them as elements to be replaced <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
-   **Exact Matching:** Crucially, the name of the placeholder within the curly braces must exactly match the name of the corresponding column in the Notion database <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Avoid adding extra commas or spaces, as this can prevent proper linking <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Any mismatches will need to be manually linked in a later step <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Connecting and Mapping

After [[customizing_pdf_templates_in_notion | customizing PDF templates with Notion]], the next step is to connect them within PDF Output.com.

1.  **Settings:** Go to the "Settings" section within PDF Output.com <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Page Format:** Select the desired page format for your PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  **Add Templates:** Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  **Connect Notion Workspace:** Select your Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  **Select Pages:** Choose the duplicated Notion page (e.g., "Purchase Order PDF Generator") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
6.  **Allow Access:** Click "Allow Access" to connect the Notion page with PDF Output.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
7.  **Select Database and Template:** Once authenticated, select the Notion database (e.g., "Purchase Order database") and the template page (e.g., the template page itself, not the generator page) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Give your connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
8.  **Mapping:** The system will attempt to automatically match database properties (left side) with template elements (right side) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   **Unmatched Properties:** If a property is unmatched (e.g., due to a space difference in names), use the "Filter unmapped properties" option to identify it <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Manually select the correct corresponding element <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Search/Sort:** Search and sort options are available to help manage properties <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Generating and Exporting PDFs

Once the template and database are properly mapped, you can generate your PDFs.

1.  **Export:** Click "Export" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
2.  **PDF Status Column:** A "PDF Status" column will be automatically added to your Notion database. A ticked checkbox in this column indicates that a PDF document has been generated for that row <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a PDF for a specific entry, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download:** After successful export, you can preview a sample of the generated file <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, and then [[customizing_and_exporting_pdf_documents | download all generated PDF documents]] <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Each row in the Notion database will result in a separate PDF <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Advanced Features

*   **Connections Tab:** The "Connections" tab stores generated PDF document connections, allowing for quick regeneration without re-entering database and page information <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Upgrade:** Free plans include a watermark on generated templates, which can be removed by upgrading to a paid plan <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Feedback/Help:** Options are available for feedback and a complete demonstration video for troubleshooting <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.