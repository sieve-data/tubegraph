---
title: Creating internal integration secret for Notion
videoId: xVDZUeFdpVc
---

From: [[theaccountantguy]] <br/> 

Visen is a platform designed to create AI-generated content directly within your [[Creating and managing a database in Notion | Notion]] workspace <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To begin using Visen, you need to configure a few settings, including [[setting_up_api_for_integrating_notion_with_myformulagen_tool | setting up API]] access for [[Creating and managing a database in Notion | Notion]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accessing Visen Settings
You can access the settings tab by clicking the gear icon on the home screen or selecting "settings" from the sidebar <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Notion Internal Integration Secret
The [[Setting up and using Notion API key | Notion internal integration secret]] is crucial as it facilitates the connection between your local [[Creating and managing a database in Notion | Notion]] workspace and Visen <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This method is more secure than using a public key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Steps to Create a Notion Internal Integration Secret
1.  **Navigate to Integrations**: In Visen's settings, click on the icon next to the "Notion Internal Integration Secret" field <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This will open the profile integrations page in your web browser <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
2.  **Create New Integration**: Click on "New Integration" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  **Name the Integration**: Provide a name for your integration, such as "Visen Integration" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  **Select Workspace**: Choose the [[Creating and managing a database in Notion | Notion]] workspace you are using <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  **Set Type**: Ensure the type is set to "Internal" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
6.  **Save and Configure**: Click "Save" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, then click "Configure integration settings" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
7.  **Obtain Secret Key**: Reveal and copy the internal integration secret key <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
8.  **Paste into Visen**: Return to Visen and paste the copied key into the "Notion Internal Integration Secret" field <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Key Security Information
The key generated is secret and is only applicable to your own local workspace, meaning it should not be shared publicly <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This ensures a secure connection between your [[Creating and managing a database in Notion | Notion]] workspace and Visen <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Saving and Local Storage
After defining all settings, click "Save" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. All entered information is saved in your browser's local storage, not on an external cloud, ensuring data safety and security <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. You can also clear all stored settings by clicking the "Clear" button <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting Notion Database or Page to Visen
Before proceeding with [[Creating a database in Notion | AI content generation]], you must connect your specific [[Creating a database in Notion | Notion database]] or page to the Visen integration you created <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Steps to Connect a Notion Database/Page
1.  **Open Notion Database/Page**: Go to the [[Creating a database in Notion | Notion database]] or page you intend to use for content generation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
2.  **Access Connections**: Click on the three dots in the top right corner of the [[Creating a database in Notion | Notion]] page <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  **Add Connection**: Scroll down and select "Connections" <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  **Search for Integration**: Type "Visen" to find the internal integration you created <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  **Confirm Connection**: Select the "Visen" integration and click "Confirm" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

Once connected, your [[Creating and managing a database in Notion | Notion]] template is linked to Visen through the internal integration secret key <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This connection only needs to be established once for each page/database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.