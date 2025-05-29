---
title: Automapping Notion database properties
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

Automapping streamlines the process of generating documents by automatically connecting properties from a [[Notion database setup for calculations | Notion database]] to corresponding elements within a PDF template <a class="yt-timestamp" data-t="01:54:33">[01:54:33]</a>. This technique is particularly useful for tasks like generating [[mapping_notion_database_to_pdf_templates | lease agreement documents]] from a [[setting_up_a_database_in_Notion | Notion database]] and a [[mapping_notion_database_elements_to_pdf_templates | Notion page]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Overview of the Process

The core idea is to replace placeholder text elements in a PDF template with actual data from a Notion database <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. For example, a lease agreement template might have placeholders like `{landlord_name}`, `{tenant_name}`, and `{street_address}` <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. These placeholders are then populated by the corresponding values from each row in a [[customizing_databases_in_Notion | Notion database]] <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.

## Setting Up for Automapping

Before automapping can occur, preliminary steps must be completed:
*   **API Key Setup**: Ensure the necessary API keys are configured for the PDF output tool <a class="yt-timestamp" data-t="01:23:08">[01:23:08]</a>. Instructions for this are typically found in the tool's help section <a class="yt-timestamp" data-t="01:42:31">[01:42:31]</a>.
*   **Connection Naming**: Assign a name for the connection (e.g., "Lease Agreement") <a class="yt-timestamp" data-t="01:29:13">[01:29:13]</a>.
*   **Database and Template Selection**: Select the relevant [[customizing_databases_in_Notion | Notion database]] and PDF template from the connected options <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>. The database will show all properties, such as landlord name, tenant name, and street address <a class="yt-timestamp" data-t="02:08:04">[02:08:04]</a>.

## How Automapping Works

Once the database and template are selected, the tool automatically maps [[adding_properties_in_a_notion_database | Notion database properties]] to the PDF template elements <a class="yt-timestamp" data-t="01:54:33">[01:54:33]</a>.

*   **Matching by Name**: The primary mechanism for automapping is matching property names in the Notion database with placeholder text names in the PDF template <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>. For example, a Notion property named "Landlord Name" will automatically map to a placeholder named "landlord name" in the template <a class="yt-timestamp" data-t="02:21:03">[02:21:03]</a>.
*   **Manual Adjustment**: If a property is not automatically mapped, it will be highlighted (e.g., in gray or red) <a class="yt-timestamp" data-t="02:29:05">[02:29:05]</a>. Users can then manually select the correct corresponding property from a list of available options <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>.

> "If something is not mapped you will be able to see a gray uh uh Gray colored element over here and once you click on this you'll able to see all the properties and if anything's not mapped that is listed on the red color" <a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>

## Exporting and Verification

After mapping, documents can be generated:
*   **Export Process**: Clicking "Export" initiates the processing of information <a class="yt-timestamp" data-t="02:57:04">[02:57:04]</a>.
*   **PDF Status Property**: During export, a "PDF Status" property may appear in the [[customizing_databases_in_Notion | Notion database]] <a class="yt-timestamp" data-t="03:00:18">[03:00:18]</a>. This column indicates which rows need to be generated (unticked) and automatically gets ticked once the PDF for that row is created <a class="yt-timestamp" data-t="03:03:09">[03:03:09]</a>.
*   **Preview and Download**: A sample preview of a generated PDF is available <a class="yt-timestamp" data-t="03:26:01">[03:26:01]</a>. Users can also choose to download all generated files in a single go <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. The generated PDFs will be exact replicas of the agreement template, populated with the specific data from each Notion database row <a class="yt-timestamp" data-t="04:08:14">[04:08:14]</a>.

## Best Practices for Automapping

To ensure seamless automapping:
*   **Consistent Naming Conventions**: It is crucial that the naming convention of the Notion database properties and the template placeholders match exactly <a class="yt-timestamp" data-t="04:24:26">[04:24:26]</a>. This consistency prevents mapping difficulties in the second step of the process <a class="yt-timestamp" data-t="04:29:05">[04:29:05]</a>.
*   **Customization**: Both the template and the database can be customized to suit specific use cases <a class="yt-timestamp" data-t="04:19:04">[04:19:04]</a>.