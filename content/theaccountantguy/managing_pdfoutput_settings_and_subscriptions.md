---
title: Managing PDFOutput settings and subscriptions
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[managing_and_exporting_pdfs_with_pdfoutput | generate PDF documents in bulk]] by integrating a Notion database with a Notion template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It replaces placeholder text elements (within curly braces) in a template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Getting Started with PDFOutput

To begin, navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Accessing and Duplicating Templates
PDFOutput provides pre-built templates for various use cases.
1.  **Browse Templates**: In the PDFOutput interface, locate and click on the "Templates" section <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This page lists all available templates <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
2.  **Search and Filter**: You can use the search option, sorting, and filtration options to find specific templates <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
3.  **Download Template**: Click the "download link" next to a desired template to open it in a new tab, displaying both the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
4.  **Duplicate to Notion**: To use a template, you must duplicate it to your own Notion workspace. Click "Start with this template" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Choose your Notion account/workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### [[setting_up_pdfoutput_with_api_keys | Setting Up PDFOutput with Notion]]

After duplicating the template to your Notion workspace:
1.  **Access Settings**: Return to PDFoutput.com and go to the settings <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
2.  **Add Templates**: Click "click here to add templates" to redirect to Notion <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Select Pages**: Ensure you select the Notion account where you duplicated the templates <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Click "Select Pages" <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. You will see the pages from your Notion workspace; select the necessary ones (e.g., the invoice generator template) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  **Allow Access**: Click "Allow access" to authenticate the connection between PDF Output and Notion <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### [[managing_pdf_output_templates_and_settings | Mapping Notion Data to Templates]]

Once connected, you will configure the mapping:
1.  **Select Database and Template**: Choose the professional invoice database and the invoice template from the respective dropdowns <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  **Name Connection**: Assign a name to your connection (e.g., "My Invoice Generation"). This name has a 20-character limit <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Click "Next" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
3.  **Review Mapping**: PDF Output automatically loads and maps Notion properties (from database columns) to template elements (placeholders in curly braces) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   **Naming Convention**: For automatic mapping, Notion property names must exactly match the template element names <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   **Manual Mapping**: If a mapping appears in gray, it means it's unmapped. You can click on it to manually select the correct Notion property <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   **Mapping Tools**: Search, sorting, and filtration options are available to help manage mappings <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. You can filter to quickly assess unmapped properties <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### [[managing_and_exporting_pdfs_with_pdfoutput | Generating PDF Documents]]

Before exporting:
1.  **PDF Status Column**: In your Notion database, ensure the "PDF Status" column is unchecked for the rows you want to generate PDFs for <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. If a row is checked, it will not be generated <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This column is unchecked by default on the first integration and becomes checked after generation <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
2.  **Export**: Click "Export" to start the process <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. The "PDF Status" column in Notion will tick as documents are generated <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
3.  **Preview and Download**: Once export is successful, you have two options:
    *   **Preview Sample**: View a sample PDF generated from one row of the database <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Download All**: Download all generated PDF documents in a single go <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### [[managing_connections_and_templates_in_pdf_output | Managing Connections]]

After a successful export, your connection is saved:
*   **Connections Window**: Go to the "Connections" window in PDFOutput to find your saved connection (e.g., "My Invoice Generation") <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Reuse Connection**: To reuse the same database and template, simply select the connection from this window <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. It will automatically load all elements for export <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Regenerating PDFs**: Remember to untick the "PDF Status" checkbox in Notion for any specific row you wish to regenerate <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## [[subscription_plans_and_features_of_pdf_output | Subscription and Features]]

*   **Upgrade Option**: The "Upgrade" option shows your current plan (e.g., Enterprise), renewal date, and number of files downloaded <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Upgrading Plan**: Click "Upgrade Subscription" and then "Activate Subscription" once upgraded <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Watermarks**: New users or those on free plans will see a watermark in the PDF output <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Watermarks are not visible on any paid plans <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## [[managing_pdf_output_templates_and_settings | Output Settings]]

Under the "Settings" tab:
*   **Page Format**: You can select different page formats (e.g., A4, Letter) from a list <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. You can also search for a specific format <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Click "Save" to apply the chosen page format to your PDF output <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Support and Help

*   **Feedback**: For questions or issues, use the "Feedback" option to send a direct message <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Help Window**: The "Help" window provides access to the demonstration video for rewatching if needed <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Direct Contact**: For assistance, you can also reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.