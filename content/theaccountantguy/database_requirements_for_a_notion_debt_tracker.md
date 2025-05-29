---
title: Database Requirements for a Notion Debt Tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 
A Notion debt tracker is designed to help users track debt payments on time and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This minimalistic tracker provides a summary of total loan amounts, total amounts repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It also offers a detailed overview of various debt types, including student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Additionally, it features a progressive payments section outlining future due payments, their amounts, and payment status <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

To build this [[creating_a_notion_debt_tracker | Notion debt tracker]], five specific databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### Databases Required

1.  **Loan Details Database** <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>: This database stores details related to loan repayments, providing the outstanding balance <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Debt Database** <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>: This database holds comprehensive information for all debts <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
3.  **Debt Overview Database** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>: Provides a quick overview of each debt <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
4.  **Summary of Debt Database** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>: Displays a summary of total loan amount, amount repaid, interest repaid, repayment percentage, and the debt-free date for each debt type <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
5.  **Total Debt Section (Database)** <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>: Shows the combined total debt value across all debts <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Detailed Database Breakdown

#### 1. Debt Database
This is the first database to be built <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and lists all different types of debt <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Properties**:
    *   **Name**: Default property, used to specify debt types (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   **Loan Amount**: Total amount of the loan <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. (Number property, US dollars <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>)
    *   **Interest Rate**: Annual interest rate for each debt <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. (Number property, percent format <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>)
    *   **Minimum Payment**: Minimum monthly payment amount <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. (Number property, US dollars <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>)
    *   **Additional Repayment**: Amount paid during the first installment (e.g., down payment) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. (Number property, US dollars <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>)
    *   **Initial Repayment Date**: Date of the first installment payment <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. (Date property <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>)
    *   **Interest Rate Per Month (I Value)**: Calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    *   **Debt-Free Period**: Formula property that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   **Expected Debt-Free By**: Estimated debt-free date, calculated by adding the `Debt-Free Period` to the `Initial Repayment Date` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   **Net Loan Outstanding Amount**: The loan outstanding amount before the initial repayment <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Derived by deducting the `Additional Repayment` from the `Loan Amount` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This serves as the opening balance for the `Loan Details` database <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

#### 2. Loan Details Database
This database is used to fill in repayment details for each debt type <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

*   **Properties**:
    *   **Installment Number**: Specifies the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Date of Payment of Installment**: The date of debt repayment per installment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. (Date property <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>)
    *   **Category of Loan**: Related to the `Debt Overview Database`, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a> <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   **Opening Balance**: The outstanding debt amount prior to the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The first month's payment uses the `Net Loan Outstanding` from the `Debt Database` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Subsequent months copy the closing balance of the previous month as the opening balance <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   **Payment Amount**: The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. For subsequent months, it equals the minimum payment <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   **Interest Calculation**: Formula specifying the interest amount paid in each installment <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. It's calculated as `Opening Balance * (Interest Rate / 12)` <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   **Principal Value**: Calculated as `Payment Amount - Interest Amount` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   **Closing Balance**: Calculated as `Opening Balance - Principal Amount` for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   **Checkbox**: Reflects payment status (paid/not paid) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   **Total Repayment**: A formula that calculates the amount paid when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Similar logic applies to interest and principal values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

#### 3. Debt Overview Database
This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

*   **Properties**:
    *   **Loan Amount**: Rolled up from the `Loan Details` database, with a formula to derive the value <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   **Total Amount Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   **Total Principal Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   **Total Interest Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   **Outstanding Amount of Loan**: Calculated by `Loan Amount - Principal Repaid` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   **Repayment in Percentage**: Calculated as `Principal Repaid / Total Loan Amount` in percentage format <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

#### 4. Summary of Debt Database
This database calculates the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the debt-free date for each debt <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

*   **Properties**: All figures are pulled in as roll-up values from the `Debt Overview Database` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This includes:
    *   Total Loan Amount <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
    *   Total Amount Repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    *   Total Interest Repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
    *   Repayment in Percentage <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
    *   Debt-Free Date <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

#### 5. Total Debt Section (Database)
This final database reflects the combined totals for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

*   **Properties**: Values are rolled up from the `Debt Overview Database` and populated using formulas to calculate the respective totals <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This includes:
    *   Total Loan Amount <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
    *   Total Amount Repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
    *   Total Interest Repaid <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
    *   Repayment in Percentage <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>

These five databases form the backbone of the Notion debt tracker, allowing for comprehensive [[managing_debt_and_loans_in_notion | debt management and tracking]] within Notion <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The primary dashboard then links these databases to provide a summary section, a debt overview, and a debt progress section <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.