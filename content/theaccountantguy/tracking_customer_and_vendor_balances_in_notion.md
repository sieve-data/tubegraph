---
title: Tracking customer and vendor balances in Notion
videoId: IEoPwU6wLec
---

From: [[theaccountantguy]] <br/> 

This guide explains how to utilize a Notion template to [[managing_accounts_and_transactions_in_notion | track customer and vendor balances]] efficiently <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This system allows you to manage accounts receivable and payable, providing a clear overview of outstanding amounts and transaction histories <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Accounts Receivable and Payable Section

The top section of the tracker is dedicated to accounts receivable and payable, featuring four distinct views <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Accounts View

This view allows you to set up and manage details for your customers and vendors <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. You can record their opening balances and the number of invoices due against those balances <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

To add a new customer or vendor, use the quick action buttons on the left <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Clicking "Add Vendor" or "Add Customer" will create a new entry, which you can then edit by clicking the pencil icon to input details like opening balance and pending invoices <a class="yt-timestamp" data-t="00:00:40">[00:01:10]</a>.

### Receivable Section

The receivable section displays all customer accounts and their associated details <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It reflects all transactions carried out, showing invoices raised against specific customers, including the date and invoice number <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Key features include:
*   **Invoice Status:** You can change the status of an invoice (e.g., "pending," "paid") as applicable <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Paid Checkbox:** A checkbox allows you to mark an invoice as paid <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. When an invoice is marked as paid, its amount is no longer calculated in the total outstanding balance at the top <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Unchecking it will recalculate the outstanding balance <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Outstanding Balance:** For each customer, the total outstanding amount is prominently displayed at the top <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

This functionality supports [[tracking_invoice_payments_in_notion | tracking invoice payments in Notion]] and helps with [[managing_invoices_and_payment_statuses_in_notion | managing invoices and payment statuses in Notion]].

### Payable Section

Similar to the receivable section, the payable section details all vendor transactions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. It shows the invoice date, invoice number, status, and the amount raised against the invoice <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. You can use the paid checkbox to manage outstanding vendor balances, similar to customer balances <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Summary Section

This section provides an overall summary of all transactions, displaying the total receivable amount, total payable amount, and the net balance <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. These figures are calculated from the detailed transactions entered in the sections below <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Transaction Section

The transaction section is divided into three segments: Receivable, Payable, and Quarterly Summary <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This section helps with [[organizing_financial_transactions_in_notion | organizing financial transactions in Notion]] and serves as a detailed ledger for [[tracking_transactions_and_expenses_in_notion | tracking transactions and expenses in Notion]].

### Receivable Segment

In the receivable segment, you can record detailed information for each transaction:
*   **Date:** The date the transaction occurred <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Period:** You can select the specific quarter (e.g., Q1, Q2) for which the invoice was raised <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Description:** A brief description of the transaction <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Account Name:** Specifies the customer account <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Amount:** The invoice amount <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Invoice Number:** The unique invoice identifier <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Status:** The current status of the invoice <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Once these details are entered, they automatically update the relevant sections at the top of the tracker <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. A "Paid" checkbox in the first column allows you to indicate if the amount has been paid, which will prevent it from being included in total outstanding balances <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Quick action buttons on the left facilitate adding new entries: "Add Receivable Entry" automatically adds a new receivable entry with the current date, ready for input <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Transactions are bated by month, with later months appearing at the top and an indicator showing the number of transactions per month <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Payable Segment

The payable segment functions similarly to the receivable segment but is dedicated to vendor transactions <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It includes the same fields for date, period, description, account name, amount, invoice number, and status <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. You can use the "Add Payable Entry" button to quickly create a new vendor transaction <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Quarterly Summary

The quarterly summary provides a combined overview for each quarter <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For every quarter, it displays the total receivable amount, total payable amount, and the net balance <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This allows for a quick quarterly overview of financial activity and helps in [[tracking_profits_and_losses_within_notion | tracking profits and losses within Notion]] over periods <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. The total amount across all quarters is also reflected at the top <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.