---
title: Personalizing Templates with Notion Data
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents in bulk by combining a Google Document as a template with a Notion database that holds the data for replacement <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Getting Started

To begin, users need to log in at pdfoutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The main steps involve adding a Google Document, connecting a Notion database, and then exporting the PDF <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Adding a Google Document Template

There are two primary methods to add a Google Document as a template:
1.  **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Choose an existing document** from Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Once created or selected, the document can be renamed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Within this Google Document, users define dynamic fields (placeholders) that will be replaced by data from Notion <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For example, an invitation template might include fields like "salutation" and "customer name" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Connecting a Notion Database

The next step is to connect a Notion database to PDF Output <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This requires authenticating with Notion and selecting the relevant pages/databases <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If a database doesn't exist, it can be created directly in Notion (e.g., an "Invitation List" table) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Once connected, PDF Output displays the properties (columns) of the Notion database <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. If new columns are added to the Notion database, users should click "refresh properties" in PDF Output to ensure they are recognized <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Mapping Notion Data to Google Doc Fields

With both the Google Document template and Notion database linked, users can map the Notion properties to the placeholders in the Google Document:
1.  Click on a Notion property (e.g., "salutation") in PDF Output to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Paste this copied value into the corresponding placeholder in the Google Document <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
This process is repeated for all dynamic fields, such as "customer name" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The changes made in the Google Document through PDF Output are live and reflected immediately <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Generating PDFs

After setting up the template and linking the data, click "Export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This initiates Google authentication <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, and then PDF Output reads each row from the Notion database to generate a unique PDF document for each entry <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs are then downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Advanced Considerations

*   **Linked Databases**: If the main Notion database is connected to other databases, users should ensure all relevant databases are selected during the Notion connection process to ensure proper data fetching <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-made Templates**: PDF Output offers pre-made templates, such as an [[customizing_notion_invoice_templates | invoice template]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Users can make a copy of these templates to their Google Workspace or copy and paste the content into a new blank document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This simplifies [[creating_and_using_notion_templates_for_pdfs | creating and using Notion templates for PDFs]] and [[creating_and_using_templates_for_pdf_generation_in_notion | creating and using templates for PDF generation in Notion]].
*   **Search and Sort**: The interface includes search and sorting options for properties <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   [[using_templates_in_notion_for_pdf_generation | Using Templates in Notion for PDF Generation]] allows for [[customizing_notion_templates_for_business_needs | customizing Notion templates for business needs]] or [[customizable_templates_for_personal_or_business_expenses in Notion | customizable templates for personal or business expenses in Notion]]. This process supports [[customizing_notion_templates | customizing Notion templates]], including [[customizing_notion_templates_for_pdf_documents | customizing Notion templates for PDF documents]], and generally streamlines [[using_templates_and_buttons_in_notion | using templates and buttons in Notion]].

For questions or assistance, users can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.