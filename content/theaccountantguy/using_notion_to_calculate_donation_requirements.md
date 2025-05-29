---
title: Using Notion to calculate donation requirements
videoId: Go6-UEvlOcI
---

From: [[theaccountantguy]] <br/> 

Notion can be utilized as a [[setting_up_a_charity_donation_tracker_in_notion | charity donation tracker]] to monitor all contributions towards charitable causes <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This system is divided into three main sections: Fund Setup, Donations Overview, and Summary <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Fund Setup

The initial step involves setting up the funds within Notion.

### Categories
Donations are categorized to help organize tracking <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Common categories include Health, Environment, and Education <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Editing Existing Categories:** Categories can be edited by clicking on them and typing new names <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Adding New Categories:** A new category can be added by sliding the bottom slider to the right and clicking the plus icon to create a new group <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Adding New Funds
Under each category, specific funds (e.g., American Red Cross, WHO, Care funds under Health; Sierra Club, The Nature Conservancy under Environment) are listed <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   To add a new fund, click the "Add Funds" button <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   New funds are initially unclassified and can be moved to an appropriate category using the three dots icon <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Fund Details
Once a fund is added or selected for editing (via the pencil icon), specific details can be inputted <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Fund Name:** Enter the name of the charity or fund <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Opening Balance:** This represents donations made to the fund at the start of the financial year <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Targeted Donation:** This is the desired total donation amount for the specific fund <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Start Date:** The date from which donations to this fund began <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Target Date:** The end date by which the targeted donation amount is aimed to be reached <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

Funds can also be deleted by clicking the three dots icon and selecting "delete" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Recent Donations

This section tracks individual donations, split month-wise with the latest month appearing on top <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Date:** When the donation was made <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Description:** Details of the donation <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Period:** The month and year of the donation <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. New periods can be created if needed <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Fund:** Select the specific fund from the ones set up <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Recomment:** This figure calculates the average monthly contribution needed from the start date to the end date to reach the targeted donation amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This calculation uses [[using_formulas_in_notion | Notion formulas]] for financial planning.
*   **Amount:** The actual amount donated for the month <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Checkmark/Crossmark:** A checkmark appears if the donation meets or exceeds the "recomment" figure, indicating sufficient contribution. A crossmark appears if the donation falls short <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   To add a new donation entry, click the "Add Donation" button <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Quarterly Overview

This section breaks down donations by month within quarters (Q1: January-March, Q2: April-June, etc.) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Each month shows the total donations made versus the total requirement <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Color Coding:**
    *   **Red:** Indicates donations are falling short of the requirement <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   **Green:** Indicates enough donations have been made <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Blue:** Indicates the total donation is equal to the donation requirement <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   A percentage indicates how much of the requirement has been met <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   The total donation for all months combined within a quarter is displayed at the top of each quarter section <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## Donations Overview

This view provides a specific overview for each fund, detailing its progress <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Total Donation:** Includes the opening balance and any subsequent donations <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Target Amount:** The goal for the specific fund <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   **Percentage Reached:** Shows the progress towards the targeted amount <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Months Left:** Calculates the remaining time until the target date, updating automatically as time passes <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. This feature showcases [[using_formulas_to_calculate_differences_in_notion | using formulas to calculate differences in Notion]].
*   **Contribution Required Per Month:** Re-iterates the monthly contribution needed from the start date to the end date to meet the target donation amount <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Summary Section

The summary provides a quick overall view of all donations <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Total Donation Required:** The sum of all individual fund requirements <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Total Donation Made:** The sum of all contributions made so far <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Shortfall/Surplus:** The difference between required and made donations <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Overall Percentage Reached:** The total donations made as a percentage of the total required donations <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

This [[using_notion_for_budgeting | Notion budgeting]] system, which also serves as a [[allocating_funds_using_notion | fund allocation]] and [[using_notion_for_tracking_tax_payments | tax tracking]] tool, supports various currencies, which can be adjusted within Notion settings <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This process involves [[using_formulas_for_financial_calculations_in_notion | using formulas for financial calculations in Notion]] to monitor [[using_notion_for_budgeting_and_savings | budgeting and savings]] and even for [[using_notion_for_debt_tracking | debt tracking]].