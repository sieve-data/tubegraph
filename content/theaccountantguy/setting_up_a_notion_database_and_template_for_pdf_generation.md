---
title: Setting up a Notion database and template for PDF generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[generating_pdf_documents_from_notion | generate PDF documents]] for purchase orders using a [[setting_up_a_database_in_notion | Notion database]] and a [[using_notion_for_pdf_template_creation | Notion template]] with PDFOutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started with PDFOutput

1.  **Log In**: Begin by logging into PDFOutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

2.  **Access Templates**: On the right sidebar, click on "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This will load a list of predefined templates available for [[generating_pdf_documents_from_notion | generating PDF documents]], including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   You can use the search icon to quickly find a specific template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
    *   Sorting and filtering options are also available <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

3.  **Download Desired Template**: Click the "Download" link next to the template you wish to use, such as the purchase order template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page for the PDF generator, which includes a database and a template <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Understanding the Notion Template and Database

The system uses a Notion template and a Notion database to [[using_notion_templates_and_databases_for_pdf_generation | generate PDF documents]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Notion Template

*   The template defines the layout and content of the PDF <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   Elements like purchase order number, date, supplier name, and buyer name are marked as placeholder text using curly braces (e.g., `{{purchase order number}}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders will be replaced by data from the database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Templates are fully customizable; you can add, delete, or modify values <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Ensure that values meant for replacement are within curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Notion Database

*   The database contains the actual data (e.g., supplier name, buyer name, date, purchase order number) that will populate the template <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   Each row in the database typically represents a unique document to be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Crucially, the names of the columns in the database must exactly match the placeholder names in the template (including spacing and commas) for proper linking <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Duplicating the Template to Notion Workspace

1.  **Duplicate the Page**: On the PDF generator page, click "Duplicate" (or "Start with this template" if it's already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **Select Workspace**: Choose your Notion workspace where you want to add this page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  **Confirm Addition**: Click "Add to private" (or your specific workspace name) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The purchase order PDF generator page will be added to your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## [[connecting_notion_database_to_pdf_generator | Connecting Notion Database to PDF Generator]]

1.  **Go to Settings**: Return to PDFOutput and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Page Format**: Here, you can select the desired page format for your PDFs <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Add Templates**: Click on "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  **Select Workspace and Pages**:
    *   Confirm the correct Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Click "Select Pages" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   Choose the duplicated "Purchase order PDF generator" page <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Click "Allow access" to connect the page with PDFOutput <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Wait for successful authentication and redirection <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## [[setting_up_pdfoutput_for_notion_databases | Setting up PDFOutput for Notion Databases]]

1.  **Select Database and Template**:
    *   Once redirected back to PDFOutput, refresh the page if necessary <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   From the Notion database dropdown, select the "Purchase order database" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   From the Notion template dropdown, select the "Template" page (not the generator page) <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Give your connection a name, e.g., "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

2.  **Mapping Properties**:
    *   PDFOutput will automatically match most database properties to template elements <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   Notion properties (from the database) are on the left, and template elements (from the template) are on the right <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   **Troubleshooting Unmatched Properties**: If properties remain unmatched (e.g., due to a space difference like "total amount" vs. "totalamount") <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>:
        *   Use the "Filter unmapped properties" option to quickly identify them <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
        *   Manually click on the unmatched database property and select the corresponding template element to link them <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   Ensure all necessary properties are mapped <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## [[generating_pdf_documents_from_notion | Generating PDF Documents from Notion]]

1.  **Export**: Click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
2.  **PDF Status Column**: PDFOutput will automatically add a "PDF status" column to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF is generated for a row, the checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. To regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download**: Once export is successful, you can:
    *   Click "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Click "Download all documents" to get all generated PDFs in a folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each PDF will reflect the specific data from its corresponding row in the Notion database <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional PDFOutput Features

*   **Connections Tab**: Stores previously generated PDF connections, allowing you to quickly regenerate documents without re-entering database and page details <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Upgrade**: Free plan documents include a watermark; paid plans remove it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Beyond connecting templates, this section allows defining the page format for PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: Report issues or provide suggestions using the feedback option <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help Section**: Contains demonstration videos and troubleshooting guides <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific PDF document use cases, you can reach out via email <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.