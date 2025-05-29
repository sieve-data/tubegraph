---
title: Using P Connect for workflow automation
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

P Connect is a no-code automation software designed to help users set up and manage automated workflows between various applications <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It facilitates connecting different tools, such as Notion and Gmail, to create seamless, automated processes like sending invoice payment reminders <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Setting Up Automation with [[using_automation_with_public_connect | P Connect]]

To set up an automation workflow using [[using_automation_with_public_connect | P Connect]], the process generally involves three simple steps <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:

### 1. Create a [[using_automation_with_public_connect | P Connect]] Account
The first step is to create a free account on [[using_automation_with_public_connect | P Connect]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. After signing up, users can access their dashboard to manage automations <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### 2. Clone an Existing Automation Workflow
Users can clone pre-built automation setups directly onto their [[using_automation_with_public_connect | P Connect]] dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This allows for quick deployment of common workflows, such as the invoice payment reminder system <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Once cloned, the workflow appears on the [[using_automation_with_public_connect | P Connect]] dashboard <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### 3. Configure and Enable the Workflow
Before configuring the workflow, ensure the automation is enabled to allow it to run correctly <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This is done by toggling a specific button within the workflow settings <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

#### Adjusting Time Zone
It's important to set the correct time zone in [[using_automation_with_public_connect | P Connect]]'s settings, as this affects when scheduled automations will run <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. The time displayed for triggers will reflect the local time zone set by the user <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

#### Scheduling the Automation
Workflows can be scheduled to run on a daily basis, at regular intervals, once, or on specific days of the week or month <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. For invoice payment reminders, setting the automation to trigger daily is recommended to check for due invoices <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Users can specify the exact time of day for the trigger <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

#### Connecting Notion Database
The [[connecting_notion_databases_and_templates_for_pdf_creation | Notion database]] containing invoice information needs to be linked to [[using_automation_with_public_connect | P Connect]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This involves:
*   Updating the connection within [[using_automation_with_public_connect | P Connect]] <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   Selecting the specific Notion account and the relevant invoice payment reminder database <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   Allowing [[using_automation_with_public_connect | P Connect]] access to the selected Notion pages <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
Once connected, [[using_automation_with_public_connect | P Connect]] can query the database to identify invoices with a "due" status <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>, <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

#### Mapping Data Fields
After connecting Notion, various fields from the database, such as customer name, email, invoice details, invoice number, invoice amount, and due date, are captured and mapped within the [[using_automation_with_public_connect | P Connect]] workflow <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>, <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. This ensures that the correct dynamic data is used in the automated emails <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Invoice Amount**: The raw numerical amount is captured first, and then a currency symbol (e.g., "$", "€") can be added <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   **Due Date**: The due date from Notion is formatted to be suitable for email communication <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Invoice Attachment**: The name and URL of the attached invoice PDF from Notion are also captured <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>, <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

#### Connecting Gmail for Email Automation
The final step in this specific workflow is to connect [[gmail_email_automation_for_invoices | Gmail]] <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   Users specify the Gmail account from which payment reminders will be sent <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   [[using_automation_with_public_connect | P Connect]] gains access to send emails from this account <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
Once connected, [[using_automation_with_public_connect | P Connect]] can then send automated emails to customers whose invoices are marked as "due" in the Notion database <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## Example: Automated Invoice Payment Reminders

The demonstrated automation uses [[using_automation_with_public_connect | P Connect]] to link Notion and Gmail to send automated invoice payment reminders <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Notion Template Structure
The Notion template used for this automation includes columns for:
*   Customer Name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Customer Email <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   Invoice Details <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   Invoice Number <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   Invoice Amount <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   Status (Paid/Due) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
*   Due Date <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   Invoice (as PDF attachment) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

### Automated Email Content
When an invoice status is "due," [[using_automation_with_public_connect | P Connect]] triggers an email containing dynamically populated information from the Notion database <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   **Sender Name**: Customizable <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   **Subject Line**: Includes the invoice number and "is due soon, action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   **Recipient**: Customer email from the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Body**: Addresses the customer by name and states the invoice number, due date, and amount <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The body can be entirely customized <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Payment Options**: Includes sections for bank account details or Swift Code, customizable for business needs <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Attachment**: The invoice PDF from Notion is attached for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Workflow Logic
The automation runs daily, checking the Notion database for invoices marked as "due" <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. If an invoice is "due," the system proceeds to gather its details and send an email reminder <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. Once a customer pays, changing the invoice status to "paid" in Notion will stop further reminders for that invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.

## Quotas and Support
[[gmail_email_automation_for_invoices | Gmail]] provides a free quota of sending up to 100 emails daily through this automation <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. For any issues during setup or workflow configuration, [[using_automation_with_public_connect | P Connect]]'s automation team can be reached for support <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.