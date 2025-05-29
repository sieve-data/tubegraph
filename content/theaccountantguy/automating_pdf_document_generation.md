---
title: Automating PDF document generation
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

[[pdf_output_tool_for_document_generation|PDF Output]] enables users to generate PDF documents in bulk by leveraging a Notion page template and a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process streamlines the creation of numerous documents, such as purchase orders, from structured data <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Core Components

The system relies on two primary components from Notion:

1.  **Notion Template**: This is a Notion page that serves as the design for your PDF document <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It includes placeholders for dynamic content, which are defined by enclosing text within curly braces (e.g., `{purchase order number}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  **Notion Database**: This database holds the specific data that will populate the placeholders in your template <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Each row in the database represents a unique document to be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The column names in the database must exactly match the placeholder names in the template for automatic mapping <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

For instance, a purchase order template might include fields like `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The corresponding Notion database would then have columns with these exact names, populated with the relevant data for each purchase order <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Step-by-Step Guide to [[utilizing_pdf_output_for_document_generation|Utilizing PDF Output for Document Generation]]

The following steps outline how to [[using_pdfoutput_tool_for_bulk_pdf_generation|use the PDF Output tool for bulk PDF generation]]:

### 1. Log In to PDF Output

Access the service by logging in at PDFOutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface will prompt you to connect a Notion database and template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 2. Access Predefined Templates

*   Navigate to the "Template" section in the right-hand sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Clicking on "Templates" will display a list of predefined templates <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   Use the search field to find specific templates, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Once found, you will see a database link and a template link <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### 3. Duplicate Templates to Your Notion Workspace

*   Click on both the database and template links <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Select the "Start with this template" option to duplicate them into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   Choose your desired Notion workspace and click "Add to private" when prompted for duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   Repeat this process for both the database and the template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### 4. Connect Notion to PDF Output

*   After duplication, return to PDF Output and click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Select your Notion workspace, then "Select pages", and choose the duplicated database and template <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Once authenticated, the database and template will appear on the PDF Output screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If they don't, click "Refresh" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   You can also select from multiple added databases or templates using a dropdown menu <a class="yt-timestamp" data-t="00:03:59">[00:04:06]</a>.

### 5. Map Database and Template Elements

*   Provide a name for your generation task (e.g., "purchase order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   The system will automatically load and map database properties to template placeholders if the naming convention is exact <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   If manual mapping is required (indicated by gray text), click on the placeholder and select the corresponding database element <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### 6. [[generating_and_downloading_pdf_documents|Generating and Downloading PDF Documents]]

*   Click "Create PDF" to initiate the document generation process <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   After processing, you can "Preview sample" to review a generated PDF <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Download all" to download all the generated PDF files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   If you miss the initial download, you can click "Download PDF" again <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Customization and Naming Conventions

The templates are customizable; you can edit or modify them after duplication <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. However, it is crucial to ensure that any data you want to replace from the database is enclosed in curly braces within the template and that the naming convention matches exactly between the template and the database columns <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Additional Features and Considerations

*   **Connections**: The "Connections" option allows you to view previously created tasks, like the purchase order generation. Clicking on a connection will automatically load the associated database and template for subsequent exports, eliminating the need to re-enter them <a class="yt-timestamp" data-t="00:06:57">[00:07:27]</a>.
*   **Upgrade Option**: Free plans include a "Made with PDF Output" watermark on generated documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes this watermark and any generation limits <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Settings**:
    *   The default page format is A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   You can add more databases and templates through the settings menu after the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:08:08]</a>.
*   **Feedback**: For any issues or suggestions, use the feedback option within the application <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help Section**: A video tutorial is available in the help section to guide users on creating custom templates from scratch if predefined ones are not suitable <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Relation Properties**: If your Notion database uses relation properties, ensure you grant access to all related databases when connecting to PDF Output to ensure all elements are correctly reflected in the PDF <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

For further assistance, you can contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.