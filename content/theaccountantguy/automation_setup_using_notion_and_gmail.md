---
title: Automation setup using Notion and Gmail
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to set up an automated system for sending invoice payment reminders to customers using a [[setting_up_a_database_in_notion | Notion database]] and Gmail, facilitated by Pabbly Connect for automation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Template Overview
The automation utilizes a specific Notion template, which includes the following columns to manage invoice information <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Customer Name:** To enter the customer's name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Email:** For the customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details:** To specify details related to the invoice, such as "service 3" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number:** The unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount:** The total amount of the invoice, which can be in any preferred currency <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a> <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Status:** Indicates whether the invoice is "Paid" (payment done) or "Due" (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Due Date:** The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice (PDF attachment):** Allows attaching the invoice as a PDF file <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Automated Reminder Message Example
The automated reminder message sent to customers includes several dynamic fields pulled directly from the [[setting_up_a_database_in_notion | Notion database]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
*   **Sender Name:** Visible when the email is opened <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line:** Includes the invoice number and status, e.g., "Invoice number three is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email ID:** The customer's email from the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Greeting:** Personalized with the customer's name, e.g., "Dear Customer 3" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Body Content:**
    *   Reminds the customer that "Invoice 3" is due for payment on a specific date (e.g., February 6, 2024) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Lists invoice details: Invoice Number, Invoice Details (e.g., "service 3"), Due Date, and Total Amount (e.g., "$150") <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   The message body is fully customizable <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Payment Options:** A section for bank account details, Swift Code, and other relevant information, which can be customized for business needs <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment:** The PDF invoice is attached for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Automation Tools Required
This automation requires three applications <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>:
1.  **Pabbly Connect:** A no-code automation software that orchestrates the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion:** Used as a note-taking and productivity app to store all invoice-related information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail:** Used to send the automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## General Setup Steps
To set up this automation, follow three simple steps <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:
1.  **Create an Account in Pabbly Connect:** This initiates the automation process <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone the Automation Workflow:** Use a provided link to clone the pre-built automation setup onto your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  **Configure the Cloned Workflow:** Customize the settings within Pabbly Connect to link your Notion and Gmail accounts <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Detailed Pabbly Connect Setup

#### Account Creation and Workflow Cloning
*   Sign up for a free account on Pabbly Connect <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Once signed up, click the provided link to clone the "invoice payment reminder" automation onto your Pabbly dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Click "Try Now" to create a clone of the automation on your account <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

#### Enabling and Configuring Workflow
*   Ensure the automation workflow is set to "On" (active status) on your Pabbly dashboard <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a> <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   Go to Pabbly Connect settings and set your preferred time zone. For example, 5 hours 30 minutes GMT <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This ensures timings are adjusted to your local time <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Notion Database Connection
The first step in the workflow involves scheduling a daily trigger <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Pabbly Connect will automatically check the [[setting_up_a_database_in_notion | Notion database]] daily to see if any invoice is under "Due" status <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   The schedule can be set to run daily, at regular intervals, once, or on specific days/dates <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. For this use case, "Every Day" is selected, with a customizable time (e.g., 10:00 AM) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

#### Linking the Notion Database
*   Click "Connect" in the Notion step of the workflow <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   Select "Update Connection" and check the checkbox to connect with Notion <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   Log in to your Notion account and select the specific [[connecting_notion_templates_with_a_database_for_automation | template]] (e.g., "db_invoice payment reminder") that you have copied to your workspace <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   Allow access to connect the database <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   Once connected, save the connection. The database name (e.g., "db_invoice payment reminders") should now be reflected <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   Before proceeding, ensure the "Simple Response" option is disabled <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   Click "Save and send test request" to send all information from the Notion database to Pabbly Connect <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

#### Capturing and Mapping Data
*   For each data field (Customer Name, Email, Invoice Details, Invoice Number, Invoice Amount, Due Date, Invoice Name, Invoice URL), click "Refresh Fields" and then "Save and send test request" <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This ensures Pabbly Connect correctly captures and maps the data from Notion <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   For the invoice amount, the raw number is captured first, and then a separate step allows adding a currency symbol (e.g., '$' or '€') to the number <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   The due date format can also be modified to a more readable format (e.g., "February 6, 2024") <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   The invoice URL will capture the link to the attached PDF <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### Gmail Integration
The final step is to send the email to the customer <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   In the Gmail step, ensure the action event is set to "Send Email" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   Click "Connect" and then "Update connection" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   Select the Gmail account from which you want to send the emails (this will be the sender's email ID) and grant access <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   Click "Save" once connected <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   Click "Refresh Fields" and then "Save and send test request" to confirm the integration. Pabbly Connect will then send an email to the customer's email address specified in the Notion database, for any invoice marked as 'due' <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
*   Gmail provides a free quota of 100 emails per day for this automation <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

## Live Demonstration and Workflow
Once the automation is set up, any changes made in the Notion database, such as updating customer details, invoice amounts, or due dates for invoices with a "Due" status, will trigger a new email reminder at the scheduled time <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

For instance, changing a customer's name, invoice details, invoice number (e.g., to 157), and amount (e.g., to $350) and setting a new due date (e.g., February 29) in Notion will result in a new automated email reflecting these updated details when the workflow runs <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

To stop sending reminders for a specific invoice, simply change its status in the Notion database from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.

## Support and Assistance
If any issues arise during the workflow setup, Pabbly Connect's automation team can provide quick assistance <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. Support email IDs may be provided for further help <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.