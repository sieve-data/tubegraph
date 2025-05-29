---
title: Managing connections and templates in PDF Output
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that allows users to generate PDF documents, such as purchase orders, from a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The first step to using PDF Output is to log in at pdfoutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Getting Started with Templates

The PDF Output interface features a sidebar on the right side, where you can find various elements, including "Templates" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Accessing Predefined Templates
Clicking on "Templates" loads a list of predefined templates available for generating PDF documents <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These include common documents like invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Users can quickly search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. There are also sorting and filtering options available <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

To add a desired template to PDF Output, click the "download link" next to it <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This will open a new page, for example, the purchase order PDF generator page, which contains both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Template Structure and Customization
A template defines the structure of the PDF document <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Elements intended to be replaced by database values are enclosed in curly braces, such as `{purchase order number}`, `{date}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These "placeholder text elements" are designed to be replaced by corresponding values from a Notion database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Users can customize these templates by adding, deleting, or modifying values <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. It's crucial that any value meant to be replaced is placed inside curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, and the name of the database column must exactly match the placeholder name in the template, without extra commas or spaces, to ensure correct linking <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Duplicating Templates to Notion
Before connecting the template to PDF Output, you must duplicate the template page onto your Notion workspace <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This can be done by clicking the "duplicate" option on the template page or "start with this template" if it's already published <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. You will need to select your Notion workspace to which the page will be added <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Connecting Templates and Databases

### Connecting to PDF Output
Once the template has been duplicated to your Notion workspace, navigate to the "Settings" part of PDF Output <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Here, you can select the desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Then, click "click here to add templates" to connect the Notion template to PDF Output <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

A new window will open, prompting you to select your Notion workspace and then choose the specific template page (e.g., "purchase order PDF generator") <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Clicking "allow access" connects this page with PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. After successful authentication, you will be redirected back to the PDF Output page <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Now, in the main interface, you can select the Notion database from the dropdown (e.g., "purchase order database") <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Below this, select the specific template page that was just connected (e.g., "purchase order PDF generator" or the template page itself if nested) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. You can also give the connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Mapping Data Fields
After selecting the database and template, click "next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. PDF Output will load the database and template elements and attempt to automatically match them <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

*   **Notion Properties** (from the database) are displayed on the left <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Template Elements** (placeholders from the template) are on the right <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

If any elements are unmatched, it's typically due to a mismatch in naming (e.g., "total amount" in the template vs. "total amount" with a space in the database) <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. You can use the "filter unmapped properties" option to quickly identify these <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. To fix a mismatch, click on the unmatched item and search for the correct corresponding field from the other side to link them <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Search and sorting options are available to help with mapping <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

Once all elements are correctly mapped, click "export" to generate the PDFs <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. A "PDF Status" column will be automatically added to your Notion database, indicating that PDF generation is in progress. Once a PDF is generated for a row, its checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a PDF for a specific row, you must untick this checkbox <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Managing Connections

The "Connections" tab in the sidebar is used to manage previously generated PDF documents <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Using Stored Connections
When a PDF document is generated, PDF Output creates and stores a connection <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This allows users to regenerate documents directly by clicking on the stored connection, without needing to refill the database and page information <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. It automatically populates the database and template elements, allowing you to proceed directly to the export step <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Other Settings
In addition to managing templates and connections, the "Settings" section allows users to:
*   Define the page format for their PDFs <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   Add templates that have been duplicated to their Notion workspace <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   Manage [[managing_pdfoutput_settings_and_subscriptions | subscriptions]] and remove watermarks from generated templates by upgrading from the free plan <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

For any issues or feedback, users can utilize the feedback option in the sidebar, or refer to the help section for a complete demonstration of the setup video <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.