---
title: Automatic mapping of Notion database properties to PDF template elements
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide explains how PDF output tools facilitate [[generating_pdf_documents_from_a_notion_database | generating PDF documents]] by automatically mapping properties from a Notion database to placeholder elements in a PDF template <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process simplifies [[creating_pdf_documents_from_notion_database | creating customized PDFs]] from structured Notion data.

## [[setting_up_notion_templates_and_databases_for_pdf_generation | Preparing Notion for PDF Generation]]

Before generating PDFs, a Notion template and database must be set up:

*   **Template Design**
    A lease agreement template is used as an example <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This template contains various details related to a lease agreement, such as landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Key pieces of information are designated as placeholder text elements, typically enclosed in curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`) <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. These placeholders will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Notion Database Setup**
    A Notion database is created to hold the specific values for each PDF document <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This database includes properties like "landlord name," "tenant name," and "street address," corresponding to the placeholders in the template <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row in the database represents a unique set of values for a PDF <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## [[connecting_notion_database_and_template_for_pdfs | Connecting Notion Database and Template]]

To begin the mapping process:
1.  Log into the PDF output tool <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>.
2.  Follow the setup instructions in the help section, including setting up API keys <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a>.
3.  Specify a connection name (e.g., "lease agreement") <a class="yt-timestamp" data-t="01:29:04">[01:29:04]</a>.
4.  Select the relevant Notion database (e.g., "lease") from the connected databases <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.
5.  Select the corresponding Notion template (e.g., "lease template") <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>.
6.  Click "next" to initiate the loading and mapping process <a class="yt-timestamp" data-t="01:48:06">[01:48:06]</a>.

## [[mapping_database_elements_to_pdf_templates | Automatic Mapping Process]]

The PDF output tool automatically maps Notion database properties to PDF template elements <a class="yt-timestamp" data-t="01:54:39">[01:54:39]</a>.

*   **How it Works**
    Upon loading, the tool displays Notion properties from the database on the left side (e.g., "landlord name," "tenant name," "street address") <a class="yt-timestamp" data-t="02:03:07">[02:03:07]</a>. It then attempts to automatically match these properties with the corresponding PDF template elements (the placeholder text) <a class="yt-timestamp" data-t="02:14:39">[02:14:39]</a>. This mapping is based on matching names between the database properties and the template placeholders <a class="yt-timestamp" data-t="01:57:07">[01:57:07]</a>. For instance, "landlord name" from the database is mapped to "landlord name" in the template <a class="yt-timestamp" data-t="02:21:03">[02:21:03]</a>.

*   **Handling Unmapped Elements**
    If any elements are not automatically mapped, they will appear as a gray-colored element <a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>. Clicking on this element reveals all properties, with unmapped ones highlighted in red <a class="yt-timestamp" data-t="02:37:05">[02:37:05]</a>, allowing for manual correction.

### Best Practice for [[customizing_pdf_templates_with_notion | Customizing PDF Templates with Notion]]

> "Make sure that the naming convention of this database and the template matches exactly the same so that you don't don't find difficulty Auto automatically mapping the same in the Second Step" <a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>

For seamless [[notion_database_integration_with_pdf_generation | Notion database integration with PDF generation]], it is crucial to ensure that the naming convention of your Notion database properties and the placeholder text in your PDF template are identical <a class="yt-timestamp" data-t="02:24:08">[02:24:08]</a>. This consistency enables the tool to automatically map elements correctly, minimizing manual intervention.

## Generating and Verifying PDFs

After mapping is complete, click "export" <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. The tool will process the information and add a "PDF status" property to the Notion database <a class="yt-timestamp" data-t="02:54:02">[02:54:02]</a>. Rows that are unticked in this column will be generated, and once processed, a tick mark will appear <a class="yt-timestamp" data-t="03:05:01">[03:05:01]</a>.

A sample PDF can be previewed to verify that the information has been correctly replaced <a class="yt-timestamp" data-t="03:26:07">[03:26:07]</a>. All generated files can then be downloaded <a class="yt-timestamp" data-t="03:55:04">[03:55:04]</a>. The generated PDFs will be exact replicas of the agreement template, with data from the Notion database inserted into the correct fields <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

For detailed preliminary setup steps, consult the help section of the PDF output tool <a class="yt-timestamp" data-t="04:41:01">[04:41:01]</a>.