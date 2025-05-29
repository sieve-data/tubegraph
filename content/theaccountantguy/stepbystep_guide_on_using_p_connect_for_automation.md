---
title: Stepbystep guide on using P Connect for automation
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to set up an automated invoice payment reminder system using [[notion_templates_and_automation_features | Notion]] as a database and [[automating_notifications_with_pabbly_connect | Pabbly Connect]] as the automation tool to send reminders via Gmail <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Overview of the Automation Workflow

The automation checks a [[notion_templates_and_automation_features | Notion]] database daily for invoices with a "due" status and automatically sends email reminders to customers <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Required Applications <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>
1.  **[[automating_notifications_with_pabbly_connect | Pabbly Connect]]**: A no-code automation software to set up the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **[[notion_templates_and_automation_features | Notion]]**: A note-taking and productivity app used to store invoice information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail**: Used for sending automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Notion Template Structure <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
The [[notion_templates_and_automation_features | Notion]] template includes the following columns:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Email**: The customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details**: Specific details about the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: The invoice's unique identifier <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount due <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates if the invoice is "paid" or "due" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   "Paid" means payment is complete <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   "Due" means payment is pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date**: The payment deadline for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice**: An attached PDF of the invoice <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Setting Up the Automation with Pabbly Connect

### Step 1: Create a Pabbly Connect Account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
*   Sign up for a free account on the [[automating_notifications_with_pabbly_connect | Pabbly Connect]] website <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Step 2: Clone the Automation Setup <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>
*   Access a pre-built automation clone on your [[automating_notifications_with_pabbly_connect | Pabbly Connect]] dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Click the "Try now" button to clone the workflow onto your account <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Step 3: Enable the Workflow <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
*   Navigate to the invoice payment reminder automation in your [[automating_notifications_with_pabbly_connect | Pabbly Connect]] dashboard <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   Ensure the toggle button for the workflow is switched to "on" to enable it <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. An active workflow will show "active status" on the dashboard <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Step 4: Configure Time Zone <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
*   Go to the "Settings" panel in your [[automating_notifications_with_pabbly_connect | Pabbly Connect]] dashboard <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   Set your desired time zone from the dropdown menu <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Click "Save" to apply the changes <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Configuring the Automation Workflow Steps

### 1. Trigger: Schedule by Pabbly <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>
*   This step enables the automation to run on a daily basis <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   It checks the [[notion_templates_and_automation_features | Notion]] database every day for invoices with a "due" status <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   Set the trigger to "Every Day" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Configure the desired time for the automation to run, e.g., 10:00 a.m. <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   Click "Save" <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### 2. Connect Notion Database <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>
*   In the workflow, click on the [[notion_templates_and_automation_features | Notion]] step labeled "Query a database" <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   Click "Connected", then the three dots, and select "Update connection" <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   Check the box and click "Connect with Notion" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   Select your [[notion_templates_and_automation_features | Notion]] account and then choose the specific invoice payment reminder template (e.g., "db-invoice payment reminders" or "notion automations") from your workspace <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Once connected, click "Update" <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Important**: Before proceeding, disable "Simple response" <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   Click "Save and send test request" to fetch data from [[notion_templates_and_automation_features | Notion]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This will capture all information from your [[notion_templates_and_automation_features | Notion]] database <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

### 3. Iterate and Map Data (Multiple Steps) <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>
For each subsequent step in the workflow (Iterator, Customer Name, Customer Email, Invoice Details, Invoice Number, Invoice Amount, Due Date, Invoice Name, Invoice URL), perform the following actions:
*   Click "Refresh Fields" to capture the latest data <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   Click "Save and send test request" to process and map the data <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
*   Click "Save" to store the configuration <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

#### Specific Data Mapping Notes:
*   **Invoice Amount**: The raw invoice amount will be captured as a number <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. In a subsequent step, you can configure it to add a currency symbol (e.g., "$", "€") to the number <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   **Due Date**: The date format can be modified in a separate step to display as desired (e.g., "February 6 2024") <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

### 4. Gmail Integration: Send Email <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>
*   Click on the Gmail step in the workflow, where the action event is set to "Send Email" <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   Click "Connected", then the three dots, and select "Update connection" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   Check the box and click "Connect with Gmail" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   Select the specific Gmail account from which you want to send the invoice reminders (this will be the sender's email ID) <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
*   Grant all necessary access permissions <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   Click "Update" <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   Click "Refresh Fields" to ensure all information is captured <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
*   Click "Save and send test request" to send a test email based on the data in the Notion database <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

> [!NOTE] Gmail Free Quota
> Gmail provides a free quota of sending up to 100 emails per day through this automation <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

### Automation Functionality and Customization
The email content, including sender name, subject line, invoice number, due date, amount, and invoice details, is dynamically pulled from the [[notion_templates_and_automation_features | Notion]] database <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The message body and payment options can be entirely customized <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

The automation automatically attaches the invoice PDF from the [[notion_templates_and_automation_features | Notion]] database to the email <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

Once a customer pays an invoice, simply change its "Status" in the [[notion_templates_and_automation_features | Notion]] database from "Due" to "Paid" to stop further reminders for that invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.

## Support and Troubleshooting
If you encounter any issues while setting up the workflow, you can reach out to the [[automating_notifications_with_pabbly_connect | Pabbly Connect]] automation team for assistance <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. Support email IDs may be provided alongside the video <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.