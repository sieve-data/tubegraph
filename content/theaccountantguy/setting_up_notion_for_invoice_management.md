---
title: Setting up Notion for Invoice Management
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to [[using_notion_for_financial_management | use Notion]] to [[tracking_invoice_payments_in_notion | set up invoice payment reminders]] for customers through automation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process leverages a pre-built [[creating_a_professional_invoice_template_in_notion | Notion template]] and an automation tool.

## Notion Template Structure for Invoice Management

The Notion template designed for invoice management includes several key columns to track all necessary information <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Email**: The customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details**: Specific details about the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: A unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount due for the invoice <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates whether the invoice is 'Paid' (payment completed) or 'Due' (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Due Date**: The deadline for the invoice payment <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice (PDF)**: A field to attach the invoice as a PDF file <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

This [[database_setup_for_notion_bills_tracker | database setup]] allows for comprehensive [[generating_invoices_from_a_notion_database | invoice generation]] and [[tracking_invoice_payments_in_notion | tracking]].

### Automated Reminder Message Structure

The automated reminder message sent to customers is customizable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> and includes:
*   **Sender Name**: Customizable sender name <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Dynamically includes the invoice number and status, e.g., "Invoice number three is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Body Content**:
    *   Personalized greeting using the customer's name <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Reminder of the invoice due date <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Detailed invoice information: invoice number, service/details, due date, and total amount <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Call to action for prompt payment <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   Customizable payment options (bank account, Swift Code, etc.) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Attachment of the invoice PDF for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Setting Up Automation for Invoice Reminders

To set up automated invoice payment reminders, three applications are used <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>:
1.  **Pabbly Connect**: A no-code automation software <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion**: The note-taking and productivity app for storing invoice information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail**: For sending automated payment reminders <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

The setup involves three main steps <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:

### Step 1: Create an Account in Pabbly Connect
Sign up for a free account on Pabbly Connect <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Step 2: Clone the Automation Workflow
Once signed up, clone the pre-built invoice payment reminder automation workflow to your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This will copy the entire setup for you to configure <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Step 3: Configure the Automation Workflow
Before starting, ensure the workflow is enabled by toggling the "on" button <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

#### Configure Pabbly Connect Settings
1.  **Set Time Zone**: Go to settings in Pabbly Connect and set your preferred time zone <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

#### Configure the Automation Workflow Steps

1.  **Trigger (Scheduler)**:
    *   Set the automation to trigger on a daily basis <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   Specify the exact time of day for the trigger (e.g., 10:00 AM) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This trigger will check the Notion database for invoices with a 'Due' status <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

2.  **Notion Database Connection**:
    *   Connect your Notion database (the `db_invoice payment reminder` template) to Pabbly Connect <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Click "Connect with Notion," select your Notion account, choose the specific database (e.g., `db_invoice payment reminder`), and allow access <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   Disable "Simple Response" and click "Save and Send Test Request" to capture initial data from Notion <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

3.  **Data Capture & Mapping (Iterators)**:
    *   For each field in the Notion database (customer name, email, invoice details, invoice number, invoice amount, due date, invoice name, invoice URL), click "Refresh Fields" and then "Save and Send Test Request" <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This ensures Pabbly Connect correctly maps and captures the dynamic data <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
    *   For the "Invoice Amount," Pabbly Connect captures only the number; you can then specify the currency symbol (e.g., '$' or '€') to be added automatically <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   The "Due Date" format can be modified to your preferred display (e.g., "February 6 2024") <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

4.  **Gmail Connection (Action)**:
    *   Connect your Gmail account from which reminders will be sent <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This will be the sender's email ID <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
    *   Select your business or desired sending email ID and grant Pabbly Connect access <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
    *   Click "Save and Send Test Request" <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. This will send a test email for any invoice currently marked as 'Due' in your Notion database <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

### Gmail Quota
Gmail provides a free quota of sending up to 100 emails daily through this automation <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

## Automation in Action
Once set up, the automation will run daily at the specified time <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. Any changes to the Notion database, such as updating invoice details or setting an invoice status to 'Due', will trigger an automated email reminder to the respective customer <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### Stopping Reminders
To stop sending reminders for a specific invoice, simply change its status in the Notion database from 'Due' to 'Paid' <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. The automation will then cease sending emails for that invoice <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.

This setup allows for efficient and automated [[tracking_invoice_payments_in_notion | invoice payment tracking]] and reminders, streamlining financial management for small businesses using Notion. For help [[customizing_invoice_templates_in_notion | customizing invoice templates]] or [[creating_invoices_in_bulk_using_notion | creating invoices in bulk]], further assistance may be needed.