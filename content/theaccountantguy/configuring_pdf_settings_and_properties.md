---
title: Configuring PDF settings and properties
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_for_businesses | generate PDF documents]] directly from a Notion database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Configuring its settings is essential for successful PDF generation.

## Accessing Settings <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

To access the settings window, click on the 'S' button or press 'S' on your keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Page Format <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>

Within the settings, you can specify the page format for your PDF output <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While a list of formats is available, A4 is generally recommended for the best output <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Notion API Key Setup <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

A crucial step in configuration is specifying the Notion API key <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. At the time of this recording, the Notion private integration key setup is used, though future public API access might change this <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Steps to Set Up a Private API Key:

1.  Click the provided link in PDF Output to obtain the Notion API key <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This will redirect you to your Notion account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
2.  Create a new integration by clicking "New integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Add a name for your integration, select the desired workspace, and keep it as an internal key <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
4.  Click "Save" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
5.  Access the "Configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
6.  Click "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This key is secret and applicable only to the user who creates it <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
7.  Copy the secret key and save it somewhere secure, as it won't be visible once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
8.  Return to the PDF Output window and paste the copied key into the "Notion API key" field <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
9.  Click "Save" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
10. To clear the API key settings, click the "Clear" button <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Connecting Notion Databases and Templates <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>

After setting up the API key, you need to connect your Notion template and database to the integration <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

1.  In Notion, navigate to your template and database pages <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
2.  On the top right, click the three dots <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  Scroll down and select "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
4.  Type the name of the integration you created (e.g., "New integration") and select it to establish the connection <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
5.  Repeat this process for both your Notion template and your Notion database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### PDF Status Property in Database <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>

Ensure your Notion database has a property named "PDF status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For PDF generation, this checkbox property must be unchecked for the rows you want to process <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. When a PDF is successfully generated for a row, this box will automatically be ticked <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Configuring PDF Output Interface <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

In the PDF Output application:

1.  Enter a connection name (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  Select your Notion database from the dropdown list <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. You can search for it or select it directly <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
3.  Select your Notion template from the dropdown list <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Mapping Properties <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>

After clicking next, PDF Output reads information from your template and database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

*   On the left, you'll see all your Notion database properties <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   The tool automatically maps these properties to the placeholder text elements (enclosed in curly brackets) in your Notion template <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   For automatic mapping to work correctly, ensure the naming convention in your Notion template's placeholder text exactly matches the column names in your Notion database <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Manual Mapping and Tools:

*   If elements are not automatically mapped (appearing in gray), you can click on them to manually select the correct Notion property from the fetched PDF elements list <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   The interface provides search, sort, and filter options (e.g., to view unmapped or mapped properties) to help manage mappings <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Exporting and Managing Generated PDFs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>

Once properties are mapped, click "Export" to start the PDF generation process <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

*   The 'PDF status' checkboxes in your Notion database will automatically tick once the PDFs are generated <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   You have two options after export:
    *   **Preview Sample**: View the generated PDF directly on the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   **Download All**: Download all generated PDF files to your local system <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. You can download multiple times if needed <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### Watermarks

*   On the free plan, generated PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   [[options_for_upgrading_pdf_output_features_and_settings | Upgrading to a paid plan]] will remove this watermark <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### Reusing Connections <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>

After creating a connection, it will be saved <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. You can click on the 'C' button to see your saved connections, which will automatically load the previously defined settings, allowing for quick subsequent PDF generation <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## Subscription and Upgrade Options <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>

To access more features or increase document limits, you can [[using_pdfoutput_settings_and_subscription_options | upgrade your subscription]] <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. The basic plan has a limit (e.g., 1000 documents) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. You can choose between monthly and yearly Pro or Enterprise plans <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. After upgrading, click "Activate subscription" to apply the new plan <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

## Feedback and Help <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>

*   **Feedback**: You can submit feedback through the "Feedback" window <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Help**: The "Help" window will contain tutorial videos for reference <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

## Customizing Templates <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>

When [[customizing_and_exporting_generated_pdf_files | creating your own PDF templates]], ensure that placeholder text elements are enclosed in curly brackets (e.g., `{Client Name}`) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. The names within these brackets must exactly match the column names in your Notion database for correct data mapping <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.