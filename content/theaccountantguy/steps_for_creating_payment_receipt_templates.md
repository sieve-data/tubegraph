---
title: Steps for creating payment receipt templates
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This guide outlines the process for [[customizing_receipt_templates_with_placeholders | creating and customizing payment receipt templates]] using Notion and PDF Output, allowing for [[generating_bulk_payment_receipts | bulk generation of payment receipts]] in PDF format. The system leverages a Notion template with placeholders and a corresponding Notion database for dynamic data insertion <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Core Components

The process relies on two main components:
1.  **Payment Receipt Template**: This is a Notion page containing the structure and design of the receipt <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It includes specific elements enclosed in curly braces (e.g., `{receipt number}`) that act as placeholders for information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  **Notion Database**: This database holds the actual data for each receipt, with columns that correspond exactly to the placeholder names in the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Setup Steps

To set up and utilize [[using_templates_in_pdf_output_for_generating_receipts | templates for generating receipts]]:

### 1. Access PDF Output

*   Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   Log in to your account <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### 2. Duplicate the Template and Database

Before connecting, you need to duplicate the provided template and database to your Notion workspace:
*   Go to the "Templates" section within PDF Output <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   Search for "payment receipts" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   Locate the payment receipt template and its corresponding database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Click on the "Template link" to open the template in Notion <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   Inside Notion, click "Duplicate" to copy the template to your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Select your desired Notion workspace (e.g., "accountant guy workspace") <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   Repeat the process for the "Database link" to duplicate the database to your Notion workspace <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### 3. Connect Notion to PDF Output

Once the template and database are duplicated in your Notion workspace:
*   Return to PDF Output.
*   Click "Click here to add database" or "Add template" on the main interface <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   When prompted for permissions, select your Notion workspace (e.g., "accountant guy workspace") <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   Select both the duplicated payment receipt template and the payment receipts database from the list <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. PDF Output will authenticate and connect to both <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### 4. Map Database Properties to Template Elements

*   Give your connection a name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   PDF Output will load and display the database properties (columns) and attempt to automatically map them to the corresponding elements in the template <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Important**: For automatic mapping, ensure that the names of your database columns exactly match the text inside the curly braces in your template, including spacing and capitalization (e.g., "Company Website" in the template and database) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   If any properties are unmapped due to a mismatch, you can manually select the correct corresponding element from the dropdown <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### 5. Generate PDF Documents

*   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   The tool will read data from each row in your database and generate a separate PDF document for each, replacing the placeholders in the template with the corresponding data <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   You can then preview a sample document or download all generated PDFs as a zip file <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

### Additional Features

*   **Connections**: View a list of your previously created connections, allowing you to quickly reload them without re-adding the database and template manually <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Templates**: Explore other predefined templates available for different use cases, such as invoices <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Upgrade**: Access paid plans to remove watermarks and increase usage limits <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Settings**: Define page format (e.g., A4) and add more Notion templates and databases to PDF Output <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Feedback**: Provide feedback or ask questions directly <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Help**: Find instructions on [[customizing_sales_receipts_templates | how to use a custom template]] that is not predefined <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.