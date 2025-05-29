---
title: Customizing Notion Invoice Templates
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

Professional invoices can be generated in bulk as PDF documents using a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This process involves setting up a template with specific elements and linking it to a corresponding Notion database.

## Template Structure

A professional invoice template is designed to include all necessary elements of a standard invoice <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. For effective [[customizing_notion_templates | customizing Notion templates]], any element that needs to be replaced with data from a Notion database must be enclosed within curly braces `{}` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples of such elements include `{client name}`, `{client company}`, and `{client address}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Database Integration

To ensure seamless data population, a Notion database is created with corresponding fields that match the names of the elements in the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For every element placed in curly braces within the template, there should be a matching property in the Notion database <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This setup is crucial for [[setting_up_and_customizing_notion_database_for_invoices | setting up and customizing a Notion database for invoices]] effectively.

## Generating Invoices Using PDF Output

The PDF output.com software facilitates the process of [[generating_professional_invoices_using_notion | generating professional invoices using Notion]].

### Initial Setup

1.  **Login:** Access the PDF output.com portal <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
2.  **Duplicate Template and Database:** Before connecting, copy the desired invoice template and database to your local Notion workspace <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This can be done by searching for the "invoice" template on the PDF output templates page, clicking on its database link and template link, and then using the "Duplicate" option in the top right corner of the opened Notion pages <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Select your Notion workspace (e.g., "the accountant guy workspace") to duplicate them <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Connecting Notion to PDF Output

1.  **Add Database and Template:** On the PDF output connection details screen, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  **Select Workspace and Pages:** Choose your Notion workspace (e.g., "the accountant guy") and then select the duplicated professional invoice database and template <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
3.  **Connection Name:** Define a connection name, such as "invoice template" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Mapping Properties and Generating PDFs

1.  **Automatic Mapping:** If the property names in your Notion database exactly match the elements within curly braces in your template, PDF output will automatically map them <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
2.  **Manual Mapping:** If names differ, properties will appear with a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on the gray icon to manually search for and select the correct corresponding element <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **Create PDF:** Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The software will generate a PDF document for each row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
4.  **Preview and Download:** After successful generation, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Customization and Best Practices

The invoice template is entirely [[customizing_notion_templates | customizable]] to your specific needs <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. To ensure automatic mapping and avoid manual steps when [[creating_and_using_an_invoice_template_in_notion | creating and using an invoice template in Notion]]:

*   **Consistent Naming:** Ensure that any element you wish to populate from the database is placed inside curly braces `{}` in the template and uses the exact same name as the corresponding property in the Notion database <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Relational Properties:** If your invoice database includes relational properties linked to other Notion databases, make sure to also add and allow access to those related databases during the connection setup process <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

### Managing Connections and Settings

*   **Connections Tab:** The "Connections" tab in PDF output shows all previously created connections, allowing you to quickly reload the database and template without re-authenticating each time <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Templates Tab:** Provides access to a variety of pre-added templates for different use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Upgrade Section:** For professional use, upgrading your subscription removes the "Made with PDF output" watermark and provides higher tiers for document generation <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings Window:** Allows you to define specific page formats (e.g., A4 size) for your PDF documents <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. You can also add more databases and templates here after the initial setup <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Custom Templates:** If you prefer to use your own custom Notion template and database, a detailed guide is available in the help section <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.