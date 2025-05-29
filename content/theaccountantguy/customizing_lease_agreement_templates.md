---
title: Customizing lease agreement templates
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

Customizing lease agreement templates involves using a template with placeholder text elements that are automatically replaced by data from a Notion database to generate personalized PDF documents <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process facilitates the bulk generation of customized [[customizable_pdf_templates | PDF templates]] for documents like lease agreements <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template Structure and Placeholders

A typical lease agreement template includes various details such as landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. For customization, these details are embedded as placeholder text elements, often enclosed in curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These placeholders are then replaced by actual values from a Notion database <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Utilizing Notion Database for Data

A Notion database stores the specific information for each lease agreement, such as landlord name, tenant name, and street address, with each row representing a unique agreement <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The values from these individual rows are imported into the template to replace the placeholder text elements <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Steps for Generating Lease Agreements

To generate lease agreements using a PDF output tool connected to Notion:

1.  **Initial Setup**: Log into the PDF output tool and access the help section for preliminary setup instructions, including configuring API keys <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This ensures the tool can connect to your Notion workspace <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
2.  **Specify Connection Details**:
    *   Enter a connection name, such as "Lease Agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Select the relevant Notion database (e.g., "Lease") from the dropdown menu <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Choose the corresponding lease template (e.g., "Lease Template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Map Database Properties to Template Elements**:
    *   After clicking "Next," the system loads the database and template elements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   It automatically maps Notion properties (e.g., "Landlord Name," "Tenant Name," "Street Address") from the database to their corresponding PDF elements/template elements <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   If a mapping is missing or incorrect (indicated by a gray element), you can manually select the correct property from a list, where unmapped items appear in red <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
4.  **Export and Generate**:
    *   Click "Export" to begin the generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   A "PDF status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Rows that are unticked in this column will be processed, and once their PDF is generated, they will be marked with a tick <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
5.  **Review and Download**:
    *   After generation, you can preview a sample PDF file to verify the data replacement <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. For instance, a sample might show "Tom Green" as landlord and "Sarah Blue" as tenant, accurately populated from the database <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   Click "Download All" to download all the generated PDF files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Individual files within the downloaded archive can then be opened to view the fully populated agreements <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Important Considerations

*   **Naming Convention**: Ensure that the naming convention of the properties in your Notion database exactly matches the placeholder names in your template <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This ensures accurate and automatic mapping, reducing manual effort <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Customization**: The template can be customized to suit various use cases, provided the database structure aligns with the template's placeholder needs <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

For any further assistance, you can contact the support team at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.