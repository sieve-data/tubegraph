---
title: Customizing receipt templates with placeholders
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate payment receipt documents using a Notion database and a Notion template, focusing on [[customizing_invoice_elements_using_placeholders | customizing template elements]] with placeholders for PDF output. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Accessing and Downloading Templates

To begin, log in to PDF output.com. <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> From the main interface, click on "Templates" to open a new page listing all available templates. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

You can use the search option to find specific documents, such as "payment receipts PDF generator." <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a> Filter and sorting options are also available. <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> Once located, click the "download link" next to the desired template. <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> This will open a page displaying both the payment receipts PDF generator database and its associated template. <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

## Understanding Template Structure and Placeholders

The payment receipt template contains predefined elements for PDF output. <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a> Elements enclosed in curly braces, such as `{receipt number}`, `{receipt date}`, `{customer name}`, and `{customer email}`, are **placeholder text elements**. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> These placeholders will be replaced with corresponding information from the Notion database. <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

For example, the `{customer name}` placeholder in the template will be populated by the "customer name" column in your database. <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> Similarly, details like "amount paid," "company address," and "company email" will replace their respective placeholders. <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

**Crucially, the exact naming convention for the placeholder text within the curly braces must match the corresponding column name in your Notion database.** <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> This ensures proper synchronization and accurate PDF generation. <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>

## Customizing the Template

The entire template is [[customizing_sales_receipts_templates | customizable]] to fit specific requirements. <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> Users can:
*   Make elements bold. <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>
*   Add desired spacings. <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>

When customizing, always ensure that any placeholder elements intended for replacement from the database remain within curly braces. <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>

## Duplicating and Connecting the Template to Notion

1.  From the payment receipts PDF generator page, if the template isn't yet published to the Notion Gallery, click "Duplicate." <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> If it is published, click "Start with this template." <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>
2.  Choose the Notion workspace where you want to duplicate the template. <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a> It needs to be duplicated to a Notion workspace to be used with PDF Output. <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>

After duplication, navigate to PDF Output and click on "Settings." <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> Click "Click here to add templates" to add the duplicated template. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> Select the specific Notion workspace where the template was duplicated and grant access. <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a> PDF Output will then read the template and database elements. <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>

## Mapping Database Properties to Template Elements

Once the template is added, you can select the "Payment Receipts Database" and the "Payment Receipt Template" from the respective dropdowns. <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> Give the export a name, such as "Payment Receipt," and click "Next." <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>

PDF Output will automatically map Notion properties (database columns) to the corresponding template elements if the names match correctly. <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>

*   If an element is mismatched or unmapped, it will be indicated, and you can manually search for and select the correct element to map it. <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
*   Filter options allow viewing unmapped properties, and sorting options help organize properties. <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>

## Generating and Downloading Payment Receipts

With everything mapped, click "Export." <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a> PDF Output will automatically add a "PDF Status" column to your Notion database. <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> This column will be ticked for each row (receipt) as it is generated. <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>

After a successful export, you can:
*   Click "Preview sample" to view a sample of the generated PDF. <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
*   Click "Download all" to download all the generated receipt files. <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> Each downloaded file corresponds to a row in the Notion database. <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

## Additional Features and Tips

*   **Connections**: The "Connections" section in PDF Output stores past successful connections, allowing you to quickly load the database and template without manually adding them each time. <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
*   **Watermarks**: On the free plan, generated PDF templates will include a "PDF output" watermark. Upgrading to a paid plan removes this watermark. <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
*   **Page Format**: Under "Settings," you can change the page format of the output PDFs. <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
*   **Feedback**: A feedback option allows you to send direct messages for assistance. <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>
*   **Help Section**: The "Help" section provides a demonstration video to guide setup and PDF generation. <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

This process facilitates [[using_templates_in_pdf_output_for_generating_receipts | using templates in PDF Output for generating receipts]] and [[steps_for_creating_payment_receipt_templates | creating payment receipt templates]] efficiently. <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>