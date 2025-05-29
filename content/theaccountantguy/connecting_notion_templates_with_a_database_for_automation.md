---
title: Connecting Notion templates with a database for automation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to [[integrating_databases_with_templates_in_notion | integrate a Notion database with a Notion template]] to automatically generate PDF documents, such as purchase orders, using PDF output.com. This process allows for efficient document automation by populating predefined templates with data from your Notion database.

## Getting Started

To begin, you need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Selecting a Predefined Template

1.  Navigate to the "Templates" sidebar element on the right <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  Browse through the list of predefined templates, which may include invoices, payment receipts, or purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  You can use the search icon to find a specific template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
4.  Once you find the desired template, click on its "Download" link to open a new page that contains both the database and the template <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Understanding the Template and Database Structure

Before connecting, it's crucial to understand how the Notion template and database interact:

*   **Template:** The template (e.g., a purchase order) contains predefined elements like purchase order number, date, supplier, buyer, and item descriptions <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Key fields that will be populated by the database are indicated by **curly braces** (e.g., `{purchase order number}`, `{supplier name}`) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Database:** The Notion database holds the actual data for each document, with columns corresponding to the placeholder names in the template (e.g., "Supplier Name," "Buyer Name," "Purchase Order Number") <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Each row in the database represents a unique document to be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

The goal is to replace the placeholder text elements in the template with the corresponding column values from the database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Customization

You can [[customizing_templates_and_databases_in_notion | customize these templates and databases]] by adding, deleting, or modifying values to fit your specific requirements <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Ensure that all values intended for replacement are enclosed in curly braces within the template, and that the column names in the database precisely match these placeholder names (avoid extra commas or spaces) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Connecting Notion to PDF output.com

1.  **Duplicate the Template Page:** On the opened purchase order PDF generator page, find the "Duplicate" option (or "Start with this template" if already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Click it to duplicate the page into your Notion workspace <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Select your Notion workspace where you want to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  **Connect in PDF output.com Settings:**
    *   Return to PDF output.com and go to the "Settings" section <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   You can select the desired PDF page format <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Select your Notion workspace (the same one where you duplicated the template) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Choose the duplicated "Purchase Order PDF Generator" page from the list of templates <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Click "Allow access" to [[connecting_a_database_in_notion | connect this Notion page]] with PDF output.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  **Select Database and Template:**
    *   After successful authentication, PDF output.com will redirect you back <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Select your Notion database (e.g., "Purchase Order Database") from the dropdown menu <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Select the specific template page (e.g., the purchase order template) from the template dropdown <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   Give your connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Mapping Database Properties to Template Elements

PDF output.com will attempt to automatically match Notion database properties (on the left) with template elements (on the right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Troubleshooting Unmatched Properties:** If some elements remain unmatched (often due to slight naming discrepancies like extra spaces), use the "Filter unmapped properties" option <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Manually select the corresponding database property for the unmatched template element <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Generating PDF Documents

1.  Once all properties are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  PDF output.com will add a "PDF status" column to your Notion database and tick it once a PDF document for that row has been generated <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. If you need to regenerate a document, untick this checkbox <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  Upon successful export, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
4.  Download all generated documents; they will be saved in an output folder <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

For example, if [[using_notion_database_for_invoice_templates | using a Notion database for invoice templates]], each row would generate a unique invoice PDF.

## Additional Features and Support

*   **Connections:** PDF output.com saves your connection settings (database and template) so you can easily regenerate documents without reconfiguring everything <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Upgrade:** Free plans include watermarks on generated PDFs; paid plans remove them <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Feedback:** If you encounter any issues, use the feedback option to send details and receive assistance <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help Section:** A complete demonstration video is available for troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific use cases, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.