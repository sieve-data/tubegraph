---
title: Notion Template and Database Integration
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate PDF documents in bulk using a [[notion_application | Notion]] template and a [[notion_application | Notion]] database, specifically focusing on payment receipts, with the help of PDFoutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Overview of the Process

The core idea is to combine a template containing specific placeholders (elements within curly braces) with a database that holds the corresponding information for those placeholders in its columns <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This allows for automated population and bulk PDF creation.

## Setting Up Your Notion Template and Database

### Template Structure
A payment receipt template, for example, will have elements enclosed in curly braces (e.g., `{{receipt number}}`, `{{customer name}}`) which are designed to be replaced by data from a database <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Database Structure
The [[creating_a_database_in_notion | Notion database]] must have columns that directly correspond to the elements specified in the template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each row in the database, a separate PDF document will be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Duplicating Templates and Databases
Before using PDFoutput.com, you need to duplicate both the desired template and its corresponding database into your local [[notion_application | Notion]] workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This can be done by accessing the template section on PDFoutput.com, searching for the template (e.g., "payment receipts"), and clicking on both the database link and template link to open them in new windows <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Then, click "Duplicate" for both the template <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> and the database <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, selecting your [[notion_application | Notion]] workspace <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Using PDFoutput.com

### Logging In
Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### [[connecting_notion_database_and_templates | Connecting Notion Database and Templates]]
Upon logging in, you'll be prompted to [[connecting_notion_database_and_templates | connect a Notion database and a Notion template]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

1.  Click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
2.  Grant permission by selecting your [[notion_application | Notion]] workspace and clicking "Select pages" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  Choose the duplicated template and database from your workspace and click "Allow access" <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
4.  Once authenticated, PDFoutput.com will show the connected database (e.g., "Payment Receipts Database") and template (e.g., "Payment Receipt Template") <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
5.  Give your connection a name, such as "Payment Receipts" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### [[mapping_notion_database_fields_to_templates | Mapping Database Fields to Templates]]
After [[connecting_notion_database_and_templates | connecting]], the tool will load the database and template elements <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

*   If you've used the exact same naming convention (including spaces and capitalization) for your database columns as for the curly brace elements in your template, PDFoutput.com will automatically map all the elements <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   If there's a mismatch, an element might show as unmapped <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. You can manually map it by clicking on the unmapped field and searching for the correct corresponding database property <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Filter, search, and sorting options are available to manage properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Generating and Downloading PDFs
Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The tool will read each row from your database and generate a separate PDF document for each, based on the template <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

*   You can preview a sample document to ensure the mapping is correct <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   Click "Download all documents" to receive a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Additional Features and Tips

*   **Connections:** The "Connections" section in the sidebar shows a list of previously created database and template connections <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Clicking on a connection will automatically load the database and template, saving you from manually adding them again <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Refreshing:** If the database or template doesn't load immediately, try clicking the refresh button <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Templates Section:** The "Templates" section offers various predefined templates for different use cases, such as invoices <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade Options:** A free plan includes a PDF watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes the watermark and offers higher limits <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Settings:**
    *   **Page Format:** Define the output PDF page format (e.g., A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Add More Templates/Databases:** You can add additional templates and databases from the settings menu <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback:** Use the feedback window to send questions or suggestions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Custom Templates:** If you want to use a custom PDF document without a predefined template and database, refer to the "Help" section for detailed steps <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.