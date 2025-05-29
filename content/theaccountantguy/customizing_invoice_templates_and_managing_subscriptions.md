---
title: Customizing invoice templates and managing subscriptions
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

## [[customizing_invoice_templates | Customizing Invoice Templates]]

Professional invoice PDF documents can be generated in bulk using a Notion template and a Notion database through the PDF Output platform <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Template and Database Structure
A professional invoice template defines all necessary elements, with dynamic fields placed inside curly braces (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. These elements are automatically replaced with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The Notion database should contain properties with names that exactly match the elements defined in the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Workflow for [[creating_and_customizing_invoice_templates_in_pdf | Creating and Customizing Invoice Templates in PDF]]
1.  **Access PDF Output:** Log in to PDFoutput.com <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
2.  **Duplicate Templates:** Navigate to the "Templates" section on PDF Output to find pre-added templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Search for "invoice" to locate the professional invoices template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   On the opened Notion pages, click the "Duplicate" option in the top right to copy the template and database to your local Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Select your Notion workspace (e.g., "the accountant guy" workspace) and add them <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a> <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  **Connect Notion to PDF Output:**
    *   In PDF Output, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Select your Notion workspace and then choose the duplicated professional invoice database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   Click "Allow access" to connect them to the PDF Output portal <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   Give your connection a name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
4.  **Map Database Properties to Template Elements:**
    *   PDF Output automatically displays database properties on the left and maps them to corresponding elements in the template, assuming identical names are used <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   If names differ, manual mapping is required. Click on the gray icon next to an unmapped element and search for the correct property from the database <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a> <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
5.  **[[generating_and_managing_invoice_documents | Generate and Manage Invoice Documents]]:**
    *   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   The system will generate a PDF document for each row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   You can preview a sample PDF or [[exporting_and_managing_generated_pdf_invoices | download all generated documents]] <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The generated PDFs will accurately reflect the data from the Notion database <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

> [!TIP]
> This template can be entirely customizable. Ensure that any data you want pulled from the database is enclosed in curly braces `{}` in the template and has the exact same name as the corresponding property in your Notion database for automatic mapping <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Reusing Connections
Once a database and template are connected, they appear under the "Connections" section in the sidebar, allowing for quick regeneration of PDFs without redefining the setup <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### [[customizing_invoice_elements_in_pdf_documents | Customizing Invoice Elements in PDF Documents]]
To connect a custom template and database, rather than using pre-added ones, refer to the "Help" section on the platform for detailed instructions <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a> <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

> [!IMPORTANT]
> If your Notion database uses relational properties (i.e., links to another database), ensure that the linked database is also added and connected during the setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## [[managing_and_editing_subscription_details | Managing and Editing Subscription Details]]
The "Upgrade" section in the sidebar allows you to [[managing_and_editing_subscription_details | upgrade your subscription]] <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a> <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

*   **Free Plan:** Documents generated on the free plan will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Paid Plans:** Upgrading to a paid plan removes the watermark and provides higher tiers for document generation <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

Click "Upgrade Subscription" to view available options and "Activate Subscription" after upgrading <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a> <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.