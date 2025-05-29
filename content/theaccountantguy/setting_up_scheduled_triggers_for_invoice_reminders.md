---
title: Setting up scheduled triggers for invoice reminders
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

## Overview
This article details how to set up an automated system for sending invoice payment reminders to customers using a Notion template and an automation tool [00:00:02]. The process ensures reminders are sent automatically based on the invoice's due status [00:00:08]. This setup allows for [[scheduling_recurring_bill_payment_notifications | scheduling recurring bill payment notifications]] to customers.

## Tools Used
The automation workflow utilizes three main applications [00:03:59]:
-   **Pabbly Connect:** A no-code automation software that orchestrates the entire workflow [00:04:01].
-   **Notion:** A note-taking and productivity application where all invoice information is stored in a database [00:04:10]. The process involves setting up a [[notion_invoice_payment_reminder_setup | Notion invoice payment reminder setup]].
-   **Gmail:** Used for sending the automated payment reminders to customers [00:04:17]. Gmail provides a free quota of 100 emails daily for this purpose [00:19:52].

## Workflow Setup Steps

The setup process involves three simple steps within Pabbly Connect [00:04:26]:

### 1. Creating a Pabbly Connect Account
First, create a free account on Pabbly Connect using the provided link [00:04:31].

### 2. Cloning the Automation Template
Once an account is created, clone the pre-built automation template onto your Pabbly dashboard [00:04:55]. This will copy the entire automation setup for your use [00:05:01]. The cloned workflow will be visible on your Pabbly dashboard, identifiable by a clock sign (trigger) and a Notion sign [00:05:41].

### 3. Enabling the Workflow
Ensure the workflow is enabled by toggling the "on" button within the workflow settings [00:06:02]. An active status will be displayed on the dashboard [00:06:20].

### Configuring Time Zone Settings
Before proceeding, set your specific time zone within the Pabbly Connect settings panel [00:06:49]. This ensures that the automation triggers at the correct local time [00:06:59].

### Setting the Daily Trigger
The automation is configured to trigger on a daily basis [00:07:34].
-   This daily trigger checks the Notion database for any invoices with a "due" status [00:07:43].
-   In the "Schedule by Pabbly" module, set the trigger frequency to "Every Day" [00:08:02].
-   Configure the specific time for the trigger, for example, 10:00 AM [00:08:19]. The time displayed will reflect your local time based on the timezone settings [00:08:48].

### Linking the Notion Database
The next step involves linking your Notion database to Pabbly Connect [00:09:12].
-   Access the Notion database template (e.g., "db-invoice payment reminder") [00:09:27].
-   In Pabbly Connect, update the connection to Notion [00:10:02].
-   Select the Notion account and choose the specific database template from your workspace that contains the invoice information [00:10:17].
-   Once connected, disable "simple response" and click "Save and Send Test Request" to pull data from your Notion database into Pabbly Connect [00:11:41].
-   Proceed through subsequent steps, clicking "Refresh Fields" and "Save and Send Test Request" for each data field (e.g., customer name, email, invoice details, amount, due date, invoice attachment URL) to ensure all information is correctly mapped [00:12:09].
-   The system automatically captures data like customer name [00:12:50], email [00:13:11], invoice details (e.g., service provided) [00:13:45], invoice number [00:14:17], invoice amount (raw number, then formatted with currency) [00:14:40], due date (formatted) [00:16:26], invoice name (e.g., Invoice 3.pdf) [00:16:55], and invoice URL [00:17:20].
-   For the invoice amount, you can [[customizing_invoice_reminders_in_notion | customize the currency symbol]] (e.g., dollar, euro) to reflect correctly in the reminder [00:15:15].

### Sending Email Reminders
The final step is to connect Gmail and configure the email sending [00:18:07].
-   Update the Gmail connection in Pabbly Connect and select the sender's email ID (your business email) [00:18:21].
-   Click "Save and Send Test Request." Pabbly Connect will check the Notion database for invoices with a "due" status and send a reminder email to the corresponding customer's email address [00:19:18].
-   As changes are made to the Notion database (e.g., updating customer names, invoice details, due dates, or status), the automated emails will reflect these changes [00:22:25]. Once a customer pays, changing the invoice status to "paid" in Notion will stop further reminders for that invoice [00:22:36].

This automated workflow is designed to continuously monitor your Notion database and send out timely invoice reminders, similar to how one might consider [[setting_up_subscription_reminders_using_a_database | setting up subscription reminders using a database]] or [[scheduling_and_repeating_notifications_monthly | scheduling and repeating notifications monthly]].