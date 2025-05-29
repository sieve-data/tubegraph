---
title: Customizing invoice reminder messages
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

Automated invoice payment reminders sent to customers can be extensively customized to suit specific business requirements and maintain a professional tone <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. The process involves modifying various elements within the Pabbly Connect automation workflow, which integrates with a [[notion_template_setup_for_invoice_reminders | Notion template]] where invoice details are stored <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## Customizable Elements

The following components of an automated invoice reminder email can be customized:

### Sender Name
The name of the sender, visible in the email, can be configured. For example, it might appear as "Notion Automation" <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

### Subject Line
The subject line dynamically pulls information, such as the invoice number, to clearly state the email's purpose. A sample subject line might read: "Invoice number three is due soon and action is required" <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This ensures the recipient immediately understands the urgency and context <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### Email Body Content
The main body of the reminder message is fully customizable <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. It is designed to dynamically insert specific invoice details from the Notion database.

Key details that are automatically pulled and can be integrated into the message include:
*   **Customer Name**: The name of the customer (e.g., "Customer 3") is inserted into the greeting <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
*   **Invoice Number**: The specific invoice number (e.g., "Invoice 3") is included in the reminder <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
*   **Invoice Details**: Information about what the invoice is for (e.g., "service 3") is included <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Due Date**: The exact due date for the payment (e.g., "February 6, 2024") is clearly stated <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   **Total Amount**: The total amount due for the invoice (e.g., "$150") is displayed <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

A sample template message might be:
> We hope this message finds you well. We greatly appreciate your business and would like to remind you that invoice 3 is due for payment on February 6, 2024.
>
> Invoice Details:
> *   Invoice Number: [Invoice Number]
> *   Invoice is raised for: [Invoice Details]
> *   Due Date of the invoice: [Due Date]
> *   Total Amount of the invoice: [Total Amount]
>
> To ensure a smooth and uninterrupted partnership, we kindly request that you process the payment by the due date mentioned above. Prompt payment helps us maintain the high level of service you expect <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

### Currency for Invoice Amount
While the Notion database stores only the numerical value of the invoice amount, the automation workflow allows for the addition of any preferred currency symbol (e.g., '$' or '€') alongside the amount in the email <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This ensures the correct currency is displayed in the reminder.

### Payment Options and Business Details
Sections for payment options, such as bank account details and Swift codes, can be included and customized according to business needs <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Additionally, any other relevant business details can be added or edited within the email body <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

### Invoice Attachment
The automation workflow ensures that the relevant invoice PDF, attached in the Notion database, is automatically included as an attachment in the reminder email for the customer's convenience <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. For example, if "invoice 3.pdf" is attached in Notion, it will be included in the email <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.

## How to Customize
The customization of these elements is primarily done within the Pabbly Connect workflow, which acts as the automation tool <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. After setting up the connection between Notion and Gmail through Pabbly Connect, users can:
*   Modify the content for fields like sender name, subject line structure, and email body text <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   Adjust the format for dynamic data like due dates to ensure they appear as desired (e.g., "February 6, 2024") <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   Add specific currency symbols to invoice amounts <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   Update payment details or business information that is included in the email <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

Once the workflow is configured and saved, the automated reminders will be sent daily at a scheduled time, dynamically pulling the updated details from the Notion database for any invoices marked with a "due" status <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. When an invoice payment is received, changing its status to "paid" in Notion will stop further reminders for that specific invoice <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.