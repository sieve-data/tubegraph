---
title: Overview of Notion finance templates
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[using_notion_for_financial_management | sinking funds tracker using Notion]] to manage specific savings goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This template helps track the overall savings needed, the amount saved, the remaining amount, and the contribution percentage over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Key Metrics Tracked <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

The [[finance_templates_in_notion | Notion]] sinking funds tracker monitors several key financial metrics for each fund:
*   **Goal amount**: The total savings target <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Amount saved**: Progress towards the goal over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Amount left to save**: The remaining balance needed <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Contribution made (percentage)**: Savings progress reflected as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Targeted date**: The deadline for contributions <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Required monthly contribution**: The amount to save each month <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

It also provides an overall progress view, indicating if monthly contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Types of Sinking Funds <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

The template typically includes six predefined categories for sinking funds:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

## Database Structure for [[using_templates_in_notion_for_expense_tracking | Expense Tracking]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>

Building the sinking funds tracker in Notion requires the use of five interconnected databases <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This structure demonstrates how to [[customizing_notion_for_personal_finance_management | customize Notion for personal finance management]].

### 1. Sinking Funds Database <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>
This database holds all the detailed information for each sinking fund being created <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

Properties include:
*   **Sinking Fund Details**: Categorized (e.g., Healthcare, Transportation, Utilities, Events, Family, Education) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted total savings <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: Initial savings at the journey's start <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: When saving for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for building the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: Duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: Required monthly payment (calculated as `(Goal Amount - Starting Balance) / Months`) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The financial account where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: Rolled up from another database, indicating current total savings <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Calculated as `Goal Amount - Amount Saved`, showing the remaining balance <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

Properties include:
*   **Sinking Fund**: Links to the specific sinking fund being contributed to <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Category**: Helps link different databases together, often mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date a contribution was made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: Opening balance when contributing on a specific date (closing balance of the previous month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount**: The amount contributed on that date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This balance needs to be manually copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month**: Rolled up from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
This database provides a comprehensive overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Properties include:
*   **Goal Amount**: Targeted total for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Remaining contribution needed (`Goal Amount - Amount Saved`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: Minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution and Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target completion date for the funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
This database summarizes the targeted goal amount, saved amount, remaining amount, contribution percentage, goal date, and required monthly contribution for *each individual* sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases to provide a summarized view <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### 5. Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

It sums up:
*   **Targeted Sinking Funds Contribution** <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   **Amount Saved** <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   **Amount Left** <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   **Contribution and Percentage** (calculated as `Total Contribution / Targeted Amount`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

These values are obtained by rolling up respective totals from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>

The main dashboard for this [[managing_finances_using_notion | Notion finance template]] presents a comprehensive view of your sinking funds:

### Summary Section <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
This section displays the aggregated goal amount, amount saved, amount left, and total contribution percentage for all sinking funds combined <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. It is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Sinking Funds Overview <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>
This section provides an overview of all six types of sinking funds, showing their individual goal amount, amount saved, amount left to save, contribution percentage, goal date, and required monthly contribution <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. It is linked to the Sinking Fund Summary database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This represents an effective [[notion_templates_for_organization | Notion template for organization]] of financial goals.

### Sinking Funds Progress <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>
This section tracks monthly payments made towards each sinking fund <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. It visually indicates whether contributions meet the minimum required amount:
*   A green tick for contributions exceeding the minimum <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross for contributions that do not meet the minimum <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

This section is linked to the individual Sinking Funds Details database and presented in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This illustrates how [[managing_finances_with_notion | Notion can be used for financial management]]. The structure of this template demonstrates how to [[customizing_notion_templates_for_business_needs | customize Notion templates for business needs]] (or personal use) to achieve specific tracking outcomes.