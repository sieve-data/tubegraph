---
title: Customizing Invoice Details in Notion
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

Notion can be utilized to set up invoice payment reminders for customers, all on automation, by [[customizing_notion_templates | customizing]] a pre-built template <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This template is designed to manage and send automated reminders based on invoice details stored within Notion <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Template Columns for Invoice Details

The Notion template for invoice management includes several key columns to capture comprehensive invoice information <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:

*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>: To enter the name of the customer <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Email of the Customer** <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>: For the desired customer's email address <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Invoice Details** <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>: Allows for specifying the details related to the invoice, such as a description of the service <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>: A unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>: The total amount of the invoice <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Status of the Invoice** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>:
    *   **Paid**: Indicates payment has been received <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
    *   **Due**: Means the payment is still pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>: The deadline for the invoice payment <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Invoice Attachment** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>: An option to attach the invoice as a PDF <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Automated Reminder Message Customization

The details entered into the Notion template are dynamically used to create and send automated invoice reminder emails.

### Message Content and Structure

The automated email message includes various details pulled directly from the Notion database <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:

*   **Sender Name**: Displayed as the sender <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Subject Line**: Automatically includes the invoice number and states it's "due soon" (e.g., "Invoice number three is due soon") <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email ID**: Pulled from the customer's email ID in the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Body Greeting**: Personalizes the greeting with the customer's name (e.g., "Dear customer 3") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Invoice Details in Body**: The message body reiterates the invoice number, the due date, the service/details the invoice is for, and the total amount <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Payment Options**: A section is provided where bank account details, Swift Code, and other relevant payment information can be included <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These can be [[customizing_invoice_templates_in_notion | customized]] as per business needs <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Invoice Attachment**: The PDF invoice attached in Notion is also sent with the reminder email <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The system captures the invoice URL for attachment <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### Customizing Message Content

*   **Entire Message Body**: The complete text of the reminder message can be entirely [[customizing_the_notion_template_for_specific_needs | customized]] to suit specific requirements <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The provided message is just a sample template <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Customizing Invoice Amount Currency

The currency symbol associated with the invoice amount can be changed <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. While the raw invoice amount is captured as a number, a preferred currency symbol (e.g., Dollar, Euro) can be specified to appear alongside it in the email <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

> [!TIP] Currency Display
> The invoice amount field in Notion only reflects the number, not the currency symbol directly. The automation allows you to define which currency symbol (e.g., "$", "€") should be displayed with the amount in the reminder emails <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

## How Details Drive Automation

The automation runs daily, checking the Notion database for any invoices with a "due" status <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>, <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. When an invoice's status is changed to "paid" in Notion, the automation will no longer send reminders for that specific invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This ensures that customers only receive reminders for outstanding payments <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. By [[setting_up_notion_for_invoice_management | setting up Notion for invoice management]] with these customizable details, businesses can streamline their payment reminder process.