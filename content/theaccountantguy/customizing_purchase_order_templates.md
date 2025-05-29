---
title: Customizing purchase order templates
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[customizing_pdf_templates_for_specific_needs | customize]] and generate [[generating_purchase_order_pdfs | purchase order PDFs]] using a Notion database and template through PDF output.com <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Accessing Predefined Templates

To begin, log into PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. On the interface, navigate to the "templates" option in the sidebar <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This section lists predefined templates for various documents, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. You can use the search icon to quickly find the "purchase order" template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Understanding the Purchase Order Template and Database

After downloading the desired template, a new page will open, featuring both a purchase order database and a template <a class="yt-timestamp" data-t="01:06:29">[01:06:29]</a>.

### Template Structure
The purchase order template includes elements such as purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="01:29:06">[01:29:06]</a>. Key elements designed for replacement are enclosed within curly braces (e.g., `{purchase order number}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>. These are placeholder texts that will be populated from the database <a class="yt-timestamp" data-t="02:00:41">[02:00:41]</a>.

### Database Role
The accompanying [[database_setup_for_purchase_orders | database]] contains predefined fields for supplier name, buyer name, date, and purchase order number, with multiple rows of information <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. The system will use these column values to replace the placeholder text in the template <a class="yt-timestamp" data-t="02:00:41">[02:00:41]</a>.

## Duplicating the Template to Notion

To work with the template, you must first duplicate it to your Notion workspace <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. On the PDF generator page, look for the "Duplicate" option (or "Start with this template" if already published) <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Select your Notion workspace to add the purchase order PDF generator page to it <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

## Connecting to PDF Output

After duplicating the template to Notion, return to PDF output.com <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.

1.  **Settings**: Go to "Settings" in the sidebar <a class="yt-timestamp" data-t="03:10:97">[03:10:97]</a>. Here, you can select the desired page format for your PDF <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
2.  **Add Templates**: Click "click here to add templates" <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
3.  **Select Workspace and Page**: Choose your Notion workspace (the same one where you duplicated the template) <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. Then, select the "Purchase order PDF generator" page from the list of templates and allow access <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. This connects the Notion page with PDF output.com <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
4.  **Connect Database and Template**: Once authenticated, refresh the PDF output page <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. Select the "purchase order database" from the drop-down menu and then select the "template page" <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. Assign a name to the connection, such as "purchase order" <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.

### Customization Rules for Templates
Both the template and the database are entirely [[customizing_pdf_templates_for_specific_needs | customizable]] <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>. You can add, delete, or modify any values in the template <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. However, it is crucial to ensure that all values intended for replacement are enclosed within curly braces `{}` <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. Furthermore, the name of the database property must exactly match the name inside the curly braces in the template, without any extra commas or spaces, to ensure proper linking <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

### Mapping Properties
After connecting, the system attempts to automatically match the database properties (Notion properties) with the template elements <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. If any properties remain unmapped (e.g., due to a mismatch in spacing like "total amount" vs. "total amount "), you can manually filter for unmapped properties and select the correct match <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>. The left side shows database properties, and the right side shows template elements <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

## Exporting and Generating PDFs

Once all properties are mapped, click "Export" <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. During export, a "PDF status" column will be automatically added to your database <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. A ticked checkbox in this column indicates that the PDF document has been generated <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. To regenerate a page, ensure this checkbox is unticked <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.

You can preview a sample of the generated PDF <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>. The generated documents will accurately reflect the data from the database, matching elements like purchase order numbers, supplier names, and buyer names <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. All generated documents can then be downloaded <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

## Additional Features and Support

*   **Connections**: Once a PDF document is generated, a connection is created and stored <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. This allows you to regenerate documents directly by clicking the connection, without needing to re-fill database and page information <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.
*   **Templates**: Access other predefined templates like [[customizing_sales_receipt_templates | sales receipt templates]], [[customizing_invoice_templates_with_placeholders | invoice templates]], or [[customizing_budget_templates | budget templates]] <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Upgrade**: Documents generated on the free plan will have a watermark, which is removed on paid plans <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Settings**: Besides page format, this is where you add templates duplicated to your workspace <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.
*   **Feedback/Help**: If you encounter issues, use the feedback option <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>. A complete setup demonstration video is available under the help section for troubleshooting <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.

For specific PDF document use cases or further assistance, you can reach out to notionformyuse@gmail <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.