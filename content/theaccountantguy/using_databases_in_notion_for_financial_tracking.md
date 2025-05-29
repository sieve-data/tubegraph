---
title: Using Databases in Notion for Financial Tracking
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This guide explains how to build a sinking funds tracker using Notion databases to manage personal finances. The tracker allows users to monitor overall savings progress, track individual fund contributions, and ensure timely financial goals are met <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Sinking Funds Tracker Overview

A Notion-based sinking funds tracker is designed to monitor:
*   The total savings required over a period <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   The cumulative amount saved <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The remaining amount to save <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   The contribution percentage over time <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Specific categories for sinking funds might include Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each fund, the tracker keeps tabs on:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   Contribution percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Targeted contribution date <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   Required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The tracker also provides an overall progress view, showing monthly contributions and indicating whether they meet the minimum required contribution <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Required Databases

To build this sinking funds tracker, five interconnected Notion databases are utilized <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  `Sinking Funds` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
2.  `Sinking Funds Details` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
3.  `Sinking Funds Overview` <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
4.  `Sinking Fund Summary` <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
5.  `Total Sinking Funds` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

This setup enables comprehensive [[utilizing_notion_databases_for_financial_tracking | financial tracking]] within Notion.

## Database Structure and Purpose

### 1. Sinking Funds Database

This database stores the core information for each individual sinking fund <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Sinking Funds Details (Categories)**: Categories like Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount**: The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance**: Initial savings at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date**: The date when saving for the fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date**: The targeted end date for reaching the fund's goal <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months**: The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown**: The required monthly payment, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account**: The account under which the fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved**: A rollup from another database (Sinking Funds Details) indicating current savings <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left**: Goal Amount - Amount Saved <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to contributions for each sinking fund <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Sinking Fund**: Links to the specific sinking fund (e.g., Education, Healthcare) to which a contribution is made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category**: Links different databases together (usually the same as the Sinking Fund name) <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date**: The date of the contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance**: The opening balance on the contribution date (closing balance of previous month, or zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount**: The amount contributed <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance**: Starting Balance + Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Contribution Required Per Month**: A rollup from the `Sinking Funds` database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a comprehensive overview of all sinking funds created <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount**: The targeted goal for the fund <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: Total contributions made so far for all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: Further contributions required (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: Minimum monthly contribution required, rolled up from another database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved / Targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The date by which the fund should be completed <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the targeted goal, saved amount, remaining amount, percentage contribution, goal date, and monthly required contribution for each individual sinking fund, with values rolled up from earlier databases <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It provides a summarized view of the entire tracker <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values for all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Targeted Sinking Funds Contribution**: Sum of all targeted goals <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **Amount Saved**: Total amount saved across all funds <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Amount Left**: Total amount remaining to save <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Contribution in Percentage**: Total Contribution / Targeted Amount for all funds combined <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
All values are rolled up from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard

The primary dashboard provides a centralized view of the sinking funds tracker:
*   **Summary Section**: Displays the total goal amount, amount saved, amount left, and overall contribution percentage, linked to the `Total Sinking Funds` database in a gallery view <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Sinking Funds Overview**: Offers an overview of all six fund types, showing their goal amount, amount saved, amount left, percentage contribution, end goal date, and required monthly contribution. This section is linked to the `Sinking Fund Summary` database in a gallery view <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Sinking Funds Progress**: Shows monthly payments for each fund and indicates if contributions meet the minimum required amount with a green tick (exceeds) or a red cross (does not meet) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This is linked to the `Sinking Funds Details` database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This [[setting_up_notion_for_personal_finance_tracking | Notion setup]] effectively allows for [[databases_setup_in_notion_for_tracking_expenses | tracking expenses]] and [[using_notion_for_debt_tracking | debt tracking]] by extension, demonstrating the power of [[creating_and_managing_databases_in_notion | creating and managing databases in Notion]] for [[setting_up_a_personal_finance_tracker_in_notion | personal finance tracking]]. A template for this tracker is available for download <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.