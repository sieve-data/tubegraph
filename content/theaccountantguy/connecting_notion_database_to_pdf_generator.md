---
title: Connecting Notion database to PDF generator
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate professional invoice PDF documents in bulk by [[using_notion_templates_and_databases_for_pdf_generation | using a Notion template and a Notion database]] with PDFOutput.com <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Preparing Notion for PDF Generation

To begin [[setting_up_a_notion_database_and_template_for_pdf_generation | setting up a Notion database and template for PDF generation]], a template should be designed with elements placed inside curly braces, such as `{Client Name}`, `{Client Company}`, and `{Client Address}` <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A corresponding Notion database is then created with properties matching these curly-braced elements, like "Client Name," "Client Company," and "Client Address" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This precise naming convention allows for automatic mapping between the database properties and the template elements <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

The template is entirely customizable <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. For data from the database to be used, it must be enclosed in curly braces within the template, and the exact same name must be used for the corresponding property in the database <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. If different names are used, manual mapping will be required <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Duplicating Pre-added Templates

PDFOutput.com provides pre-added templates for various use cases <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. To use these, navigate to the "Templates" section on PDFOutput.com and search for the desired template, such as "invoice" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Each template typically has a database link and a template link <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

1.  Click on both the database link and the template link to open them in new tabs <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  In each new tab, click the "Duplicate" option in the top right corner <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
3.  Select your Notion workspace to duplicate the template and database into your local Notion environment <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This process copies the template and database to your personal Notion workspace <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Connecting Notion to PDFOutput.com

[[Setting up PDFOutput for Notion databases | Setting up PDFOutput for Notion databases]] involves defining a connection between your Notion workspace and the PDFOutput portal.

1.  Access PDFOutput.com and log in <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
2.  Upon logging in, you will see a "Connection Details" screen asking to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Click on "Add Database" or "Add Template" <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
4.  Select your Notion workspace (e.g., "the accountant guy workspace") <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Select Pages" and choose both the duplicated template and database <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
6.  Click "Allow Access" <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This will add the database and template to your PDFOutput portal <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
7.  Define a connection name (e.g., "invoice template") and click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

Once connected, PDFOutput.com will load the database and template, automatically mapping properties if names match <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Handling Relational Properties

If your Notion database uses relational properties (meaning elements are connected to another database), ensure that the related database is also added during the connection setup process <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## Generating PDFs

After the database and template are connected and mapped:

1.  All database properties will be reflected on the left side of the screen <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  If property names in the database and template don't match, they will appear in gray <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Click on these to manually search and select the correct element to map <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
3.  Once all elements are correctly mapped, click on "Create PDF" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
4.  The system will generate a PDF document for every row in the database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
5.  Upon successful export, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

The generated PDFs will accurately populate the template with data from each row of your Notion database <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. As more items are added to the Notion database, subsequent generations will create PDFs for the new entries <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

## PDFOutput.com Features

### Connections
The "Connections" section displays all previously used connections, allowing you to quickly reload a database and template without re-authenticating with Notion <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Templates
The "Templates" section provides a list of pre-added templates for various needs <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Upgrade Subscription
Under the "Upgrade" section, you can manage your subscription <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The free plan includes a "Made with PDFOutput" watermark on generated PDFs, which is removed with a paid subscription <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Settings
The "Settings" window allows you to:
*   Define the specific page format (e.g., A4 size) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   Add more databases and templates after the initial setup <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### Feedback
A feedback option is available to send messages or queries <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Custom Templates and Databases
For information on [[connecting_notion_databases_with_pdf_generation_tools | connecting your custom PDF document and a database]] instead of using pre-added templates, refer to the "Help" section <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.