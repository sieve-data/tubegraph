---
title: Integrating P connect for workflow automation
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

[[Using Public Connect for automation | P Connect]] is a no-code automation software designed to help users set up entire workflows <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It facilitates the integration of various applications to automate tasks, such as sending invoice payment reminders using Notion and Gmail <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Getting Started with P Connect
To begin setting up automation with P Connect, follow these steps:
1.  **Create an account** <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Users can sign up for a free account <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Clone the automation setup** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. After signing up, users can clone pre-built automation workflows directly onto their P Connect dashboard <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
3.  **Enable the workflow** <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Ensure the automation workflow is set to "on" or "active" status in the dashboard to function correctly <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
4.  **Configure time zone settings** <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Users can adjust the time zone in the P Connect settings panel to align with their local time <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Setting Up Automation Triggers
P Connect workflows are initiated by triggers, which can be configured for various frequencies <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Daily Basis**: Automations can be set to trigger every day, checking databases for specific conditions at a set time (e.g., 10:00 AM local time) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Other Options**: Triggers can also be set for regular intervals, once, specific days of the week, or particular dates of the month <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Integrating Databases and Applications

### [[Notion Workspace Integration | Connecting Notion Databases]]
P Connect can connect to Notion databases to retrieve and process information.
1.  **Update Connection**: In the P Connect interface, navigate to the Notion step and select "Update connection" <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
2.  **Connect with Notion**: Choose "Connect with Notion" and select the desired Notion account <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
3.  **Select Pages/Templates**: Choose the specific Notion templates or pages enabled on your workspace (e.g., 'DB_Invoice Payment Reminder') and allow access <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
4.  **Test Connection**: Once connected, use "Save and send test request" to verify that data from the Notion database is being captured by P Connect <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. This ensures that P Connect can query the database for specific conditions, such as an invoice status being "due" <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

### Connecting Gmail
P Connect can also connect with Gmail to send automated emails.
1.  **Update Connection**: In the Gmail action step, select "Update connection" <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
2.  **Connect with Gmail**: Choose "Connect with Gmail" and select the specific Gmail account that will serve as the sender's email ID for automated messages <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>, <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
3.  **Allow Access**: Grant P Connect the necessary access to your Gmail account <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
4.  **Test Email Sending**: Click "Save and send test request" to confirm that emails are being sent from the configured Gmail account to the intended recipients <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>, <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. Gmail provides a free quota of sending up to 100 emails daily <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>, <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

## Workflow Execution and Data Mapping
Once configured, the workflow in P Connect automatically captures and maps data from the connected applications.
*   **Data Capture**: P Connect captures various data fields from the Notion database, such as customer name, email, invoice details, invoice number, invoice amount, and due date <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>, <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>, <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>, <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>, <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Data Transformation**: The system can transform data, such as adding currency symbols to invoice amounts <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>, <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>, or reformatting dates <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>, <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Automated Email Content**: The captured and transformed data is then dynamically inserted into the automated email content, including the subject line, customer name, invoice details, due date, and amount <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Invoice Attachments**: The workflow can also attach PDF invoices to the emails, capturing the invoice name and URL from the Notion database <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>, <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### Customization and Ongoing Management
Users can customize the email message content and the status of invoices in Notion. When an invoice status is changed to "paid" in Notion, P Connect will cease sending reminders for that particular invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>, <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.