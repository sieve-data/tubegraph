---
title: Customizing invoice reminders in Notion
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[notion_invoice_payment_reminder_setup | set up automated invoice payment reminders]] for customers using a [[creating_and_using_an_invoice_template_in_notion | Notion template]] and Pabbly Connect for automation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This system allows for significant [[customizing_notion_templates | customization]] of the reminder process and message content <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Notion Invoice Template Overview

The core of this automation is a [[creating_professional_invoice_templates_in_notion | Notion invoice template]] with specific columns for tracking <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** (e.g., service provided) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status** (e.g., "Paid" or "Due"). "Due" status triggers the reminder <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Due Date** <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice PDF Attachment** <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>

By changing the `Status` to "Paid," reminders for that invoice will cease <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This [[tracking_invoice_payments_in_notion | tracking invoice payments]] functionality is key to managing reminders.

## Automated Reminder Message Details

The automated reminder email is designed to be comprehensive and customizable <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Sender Name:** Configurable <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line:** Includes the invoice number and a call to action, e.g., "Invoice number three is due soon and action is required on this" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email ID:** Pulled directly from the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Body Content:**
    *   Starts with a personalized greeting, using the customer name from Notion <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Highlights the invoice number and due date <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Provides a summary of invoice details: number, service (from Invoice Details), due date, and total amount <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Includes a customizable message urging prompt payment <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   Offers a section for payment options like bank account details and Swift Code, which are fully customizable <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment:** The PDF invoice linked in Notion is automatically attached <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Setting Up the Automation for Customization

The automation is built using Pabbly Connect, Notion, and Gmail <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Initial Setup Steps
1.  **Create Pabbly Connect Account:** Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone Automation Workflow:** Use a provided link to clone the pre-built invoice payment reminder workflow into your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  **Enable Workflow:** Ensure the workflow is set to "On" or "Active" in your Pabbly dashboard <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  **Set Time Zone:** Configure your local time zone in Pabbly Connect settings <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Triggering the Automation
The automation is scheduled to run daily at a specified time (e.g., 10:00 a.m. local time) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. At the set time, it checks the Notion database for invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Linking Notion Database
1.  **Connect Notion:** Update the Notion connection in Pabbly Connect. Select your Notion account and grant access to the specific database (e.g., "db-invoice payment reminders") that you've copied to your workspace <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
2.  **Test Connection:** Disable "Simple Response" and click "Save and send test request" to pull data from Notion <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

### Mapping Notion Fields to Email Content
This is where significant [[customizing_notion_invoice_templates | customizing Notion invoice templates]] is achieved by mapping the data fields. For each field in the Pabbly Connect workflow, perform the following steps:
1.  Click "Refresh Fields" <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
2.  Click "Save and send test request" to ensure data is captured correctly <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
This process applies to:
*   Customer Name <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>
*   Customer Email <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>
*   Invoice Details <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>
*   Invoice Number <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>
*   Invoice Amount: The raw number is captured first <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. A separate step then allows adding a currency symbol (e.g., `$`, `€`) before the amount, which can be customized <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   Due Date: Captured and formatted into a readable date string (e.g., "February 6 2024") <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   Invoice Name (from PDF attachment) <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>
*   Invoice URL (from PDF attachment) <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>

### Connecting Gmail
1.  **Connect Gmail Account:** In the Gmail action step, connect the specific Gmail account from which you want to send the reminders (your business email ID) <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
2.  **Grant Access:** Allow Pabbly Connect access to your Gmail <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
3.  **Test Sending Email:** Click "Save and send test request" to send a test email. Gmail has a free quota of 100 emails per day <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

## Customization Options

*   **Reminder Frequency and Time:** The automation can be set to trigger daily, at regular intervals, or on specific days/dates <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Currency Symbol:** The currency symbol associated with the invoice amount can be changed (e.g., from `$` to `€`) in Pabbly Connect <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. This allows for [[customizing_budget_templates_in_notion | customizing budget templates]] and other financial documents.
*   **Email Content:** The entire body of the automated reminder message, including the payment options section (bank account details, Swift Code), can be completely customized to suit business needs <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Invoice Data:** Any changes made in the Notion database (customer name, invoice details, amount, due date, attachments) will be reflected in subsequent automated reminders <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

[!TIP]
Once a customer pays, update the invoice status in Notion to "Paid" to stop further reminders for that invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This is part of a broader system for [[generating_professional_invoices_using_notion | generating professional invoices using Notion]].