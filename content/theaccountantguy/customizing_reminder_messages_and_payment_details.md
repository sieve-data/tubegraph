---
title: Customizing reminder messages and payment details
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to customize invoice payment reminder messages and payment details using a [[notion_template_for_invoice_payment_reminders | Notion template]] and automation tools. This process allows for tailored communication with customers regarding due invoices <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Notion Template Fields for Reminders

The core of this automation relies on a Notion template structured with specific columns to capture essential invoice information <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These fields populate the automated reminder messages:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Customer Email**: To enter the customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details**: To specify details related to the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: The unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount of the invoice <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates whether the invoice is "Paid" or "Due" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Only invoices with a "Due" status trigger reminders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Due Date**: The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice Attachment**: Allows attaching the invoice as a PDF <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Customizing Reminder Message Content

The automated reminder message is highly customizable, allowing users to tailor the content to their specific needs <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Sender Name**: The name of the sender is visible <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Automatically includes the invoice number and states that the invoice is due soon, e.g., "Invoice number three is due soon and action is required on this" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Customer Name**: The customer's name, as specified in the Notion database, is automatically inserted into the message body <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Invoice Details**: The body of the message dynamically pulls in the invoice number, service details, due date, and total amount from the Notion database <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Overall Message Body**: The entire body of the message can be entirely customized as per user requirements; the provided message is a sample template <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Customizing Payment Options and Details

Payment options and currency can also be tailored within the reminder message:
*   **Payment Options**: Users can include bank account details, Swift Code, and other relevant payment information in a dedicated section of the reminder message <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This section can be customized according to business needs <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Currency Customization**: While the Notion database captures the raw invoice amount, the system allows users to specify their preferred currency symbol (e.g., Dollar, Euro) to appear alongside the amount in the reminder message <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Invoice Attachment

For convenience, the system automatically attaches the invoice PDF (e.g., "invoice3.pdf") that was uploaded to the Notion database to the reminder email <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Automation Workflow

The customization of reminders is facilitated through an automated workflow involving:
*   **Pabbly Connect**: A no-code automation software that orchestrates the entire workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Notion**: Used as a note-taking and productivity app to store all invoice-related information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This is where the [[creating_and_customizing_reminder_templates_in_databases | reminder templates]] are created and customized.
*   **Gmail**: Used to send the automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

This setup enables [[automating_bill_payment_reminders_using_templates | automating bill payment reminders using templates]] by triggering daily checks on the Notion database for invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Upon identifying a due invoice, the system dynamically populates and sends a customized email reminder to the respective customer <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. Once a customer pays, changing the invoice status to "Paid" in Notion prevents further reminders from being sent for that invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.