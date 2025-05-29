---
title: Automating invoice payment reminders using Notion
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to set up an automated system for [[managing_invoices_and_payment_statuses_in_notion|managing invoices and payment statuses]] and sending payment reminders to customers using [[using_notion_for_bill_reminders|Notion]] in conjunction with Pabbly Connect, an automation tool <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This system aims to automate the process of sending out timely reminders for due invoices <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Notion Template Overview

The core of this automation is a dedicated [[notion_template_setup_for_invoice_reminders|Notion template]] designed to [[tracking_invoice_payments_in_notion|track invoice payments]] and their statuses. The template includes the following columns:

*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** – The customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** – Specifics about the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status** – Indicates if the invoice is "Paid" (payment received) or "Due" (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
*   **Due Date** – The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice PDF** – Allows attaching the invoice as a PDF <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>

## Automated Reminder Message Structure

The automated email reminder is customizable and pulls dynamic information from the [[notion_template_setup_for_invoice_reminders|Notion database]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:

*   **Sender Name** <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   **Subject Line** – Includes the invoice number and states that the invoice is "due soon" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email ID** – Automatically populated from the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Email Body** – A professional message thanking the customer, reminding them of the due date, and requesting prompt payment <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Key details like customer name, invoice number, due date, and total amount are dynamically inserted <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The currency for the invoice amount can be customized <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Payment Options** – A section to include bank account details, Swift Code, and other relevant payment information <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This section is fully customizable to suit business needs <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Invoice Attachment** – The email automatically attaches the PDF invoice from the [[using_notion_for_invoice_template_creation|Notion database]] <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Automation Setup (Using Pabbly Connect)

The automation [[invoicing_and_workflow_management_in_notion|workflow]] utilizes three key applications:

1.  **Pabbly Connect** – A no-code automation software that orchestrates the entire workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion** – The note-taking and productivity app where invoice information is stored <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail** – Used for sending the automated payment reminders <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Setup Steps

1.  **Create a Pabbly Connect Account:** Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone the Automation Workflow:** Use the provided link to clone the pre-built invoice payment reminder automation setup directly into your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  **Configure the Workflow:**
    *   **Enable Workflow:** Ensure the workflow is active by turning the "on" button <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   **Set Time Zone:** Adjust the time zone in Pabbly Connect settings to match your specific location <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    *   **Trigger Setup:**
        *   The automation is scheduled to trigger on a daily basis <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
        *   Set the specific time each day for the automation to check the Notion database for invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For example, it can be set to run at 10:00 AM <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   **Notion Database Linkage:**
        *   Connect your Notion account and select the invoice payment reminder database that you copied to your workspace <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
        *   Crucially, disable the "simple response" option before clicking "Save and send test request" to ensure all data is captured <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
        *   Click "Save and send test request" to pull all information from your Notion database into Pabbly Connect <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   **Data Mapping:** Proceed through each subsequent step in the workflow, clicking "Refresh Fields" and then "Save and send test request" to ensure all fields (Customer Name, Email, Invoice Details, Number, Amount, Due Date, Invoice Name, and URL) are correctly mapped and captured <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
        *   For the invoice amount, Pabbly Connect initially captures only the number, so a subsequent step is used to add the desired currency symbol (e.g., "$", "€") <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
        *   The due date format can also be adjusted for better readability in the email <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
    *   **Gmail Integration:**
        *   Connect your Gmail account, which will serve as the sender's email ID for the reminders <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
        *   Click "Save and send test request" to trigger a test email. This verifies that the entire workflow, from Notion data retrieval to email sending, is functioning correctly <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
        *   Gmail provides a free quota of sending up to 100 emails per day through this automation <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

## How the Automation Functions

Once set up, the automation works as follows:

*   Every day at the specified time, Pabbly Connect checks the Notion database for any invoices listed with a "Due" status <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   If an invoice is "Due", an automated payment reminder email is sent to the customer's email address listed in the Notion database <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
*   To stop sending reminders for a particular invoice, simply change its status in the Notion database from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.
*   New invoices can be added to the database, and their status can be set to "Due" to automatically include them in the reminder system <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

This system effectively helps with [[tracking_debt_payments_using_notion|tracking debt payments]] and [[tracking_subscriptions_and_bill_payments_using_notion|tracking subscriptions and bill payments]] that are essentially recurring invoices.