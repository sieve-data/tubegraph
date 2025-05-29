---
title: Debt payment tracking in Google Sheets
videoId: r6C5tHcfAes
---

From: [[theaccountantguy]] <br/> 

A personal finance tracker developed in [[using_google_sheets_for_finance | Google Sheets]] includes a dedicated tab for [[overview_of_debt_payment_tracker | debt payment tracking]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, allowing users to monitor their financial liabilities. This feature enables a clear overview of total debts, interest and principal payments made, and remaining outstanding loan amounts <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Key Inputs for Debt Tracking

To utilize the [[debt_tracker | debt payment]] feature, users need to input specific information:
*   **Debt Information** <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>
*   **Loan Amount** <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   **Interest Rate** <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
*   **Minimum EMI Payment** (Equated Monthly Installment) to be made each month <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
*   **Additional Down Payment** (if any, made at the time of obtaining the loan) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
*   **Initial Repayment Date** (the first date a repayment was made towards the loan) <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>

## Automated Calculations

Once the initial data is entered, the tracker automatically calculates several key metrics:
*   **Loan Outstanding** at the beginning of the period <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **Debt-Free Date**: The estimated date when the debt will be fully repaid if minimum EMI payments are consistently made <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Interest Repayment**: Total interest paid so far <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Principal Repaid**: Total principal amount paid so far <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Total Repayment Value** <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Repayment Percentage**: The percentage of the loan that has been repaid <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Entering Debt Transactions

On the right side of the debt payment tab, users can log individual transactions:
*   Specify the **Date** of the payment <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   Select the **Debt** from a dropdown list of previously added debts <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   Enter the **EMI Amount** paid <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

Upon entering the EMI amount, the sheet automatically computes the interest value, principal value, and the updated loan outstanding for that payment <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. As payments are made, the loan outstanding amount will continuously reduce <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## Debt Payment Overview

The left side of the debt payment tab provides a comprehensive overview:
*   **Amount Paid**: Represented visually in green <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Amount Left** to repay <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Total Amount Repaid**, broken down into principal and interest amounts <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Amount Outstanding** (Total loan amount less the amount repaid) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Total Repayment Percentage** <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Number of Loans** taken <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Total Minimum EMI** required for all combined loans <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Graphical Representation

A graph on the right side of the overview visually depicts:
*   **Green Bar**: Total savings made <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Black Bar**: Savings still needed for a particular fund <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   This visual aid helps in understanding the progress of savings for each fund <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Dynamic Reporting

The [[dynamic_financial_reporting_with_google_sheets | reporting section]] of the personal finance tracker allows users to generate dynamic reports for debt payment details. Users can select "debt details" from a dropdown menu and choose a specific month to view updated values and a pie chart reflecting the allocation of payments <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This feature provides a quick and dynamic representation of financial status <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.