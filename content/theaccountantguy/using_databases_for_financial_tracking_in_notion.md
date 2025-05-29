---
title: Using databases for financial tracking in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details how to build a [[setting_up_a_personal_finance_tracker_using_notion | Notion]]-based tracker for managing "sinking funds," which are savings allocated for specific future expenses. This system leverages multiple [[creating_and_using_databases_in_notion | Notion databases]] to provide a comprehensive overview of savings goals and progress.

## Sinking Funds Tracker Overview

The sinking funds tracker is designed to monitor several key metrics for individual savings goals [00:00:48]:
*   **Overall Amount of Savings Needed**: The total target amount to save over a defined period [00:00:49].
*   **Amount Saved Over Time**: The cumulative amount contributed to date [00:00:51].
*   **Amount Left to Save**: The remaining balance needed to reach the goal [00:00:53].
*   **Contribution Made in Percentage**: The progress towards the goal as a percentage [00:00:55].

Specific categories of sinking funds demonstrated include education, events, family, healthcare, transportation, and utilities [00:01:00]. For each fund, the tracker monitors [00:01:08]:
*   Goal amount
*   Amount saved over time
*   Amount left to save
*   Contribution made over time (in percentage)
*   Targeted date for contribution completion
*   Required monthly contribution

The tracker also provides an overall progress view, showing monthly contributions and indicating whether they meet the minimum contribution criteria [00:01:22].

## Database Structure for Sinking Funds

Building this [[using_notion_for_financial_management | financial management]] system requires the use of five interconnected [[creating_and_using_databases_in_notion | Notion databases]] [00:01:39]:
1.  Sinking Funds
2.  Sinking Funds Details
3.  Sinking Funds Overview
4.  Sinking Fund Summary
5.  Total Sinking Funds

### 1. Sinking Funds Database

This database serves as the central repository for all specific details related to each sinking fund [00:01:44].

Columns in this database include:
*   **Sinking Funds Details**: Categorizes funds (e.g., Healthcare, Transportation, Utilities, Events, Family, Education) [00:02:04].
*   **Goal Amount**: The targeted savings amount [00:02:12].
*   **Starting Balance**: The initial amount of savings at the start of the journey [00:02:17].
*   **Start Date**: The date when saving began for the fund [00:02:23].
*   **Goal Date**: The targeted end date by which the fund should be built [00:02:30].
*   **Months**: The duration in months between the start and goal dates [00:02:35].
*   **Payment Breakdown**: The required monthly payment towards the fund, calculated as (Goal Amount - Starting Balance) / Months [00:02:45].
*   **Account**: The financial account where the sinking fund is held [00:02:56].
*   **Amount Saved**: A rolled-up value from another database, showing the current total savings [00:03:00].
*   **Amount Left**: Calculated as (Goal Amount - Amount Saved), showing the remaining balance needed [00:03:10].

### 2. Sinking Funds Details Database

This database stores information about each individual contribution made towards the sinking funds [00:03:24].

Key columns include:
*   **Sinking Fund**: Links to the specific sinking fund being contributed to [00:03:32].
*   **Category**: Helps link different databases together, typically duplicating the Sinking Fund name [00:03:47].
*   **Contribution Date**: The date of a specific contribution [00:03:58].
*   **Starting Balance**: The opening balance when a contribution is made. For the first month, this is zero; otherwise, it's the closing balance of the previous month [00:04:02].
*   **Contribution Amount**: The amount contributed on that specific date [00:04:21].
*   **Closing Balance**: Calculated as (Starting Balance + Contribution Amount) [00:04:27].
    *   *Note*: The closing balance of one month needs to be manually copied to the next month's opening balance [00:04:33].
*   **Contribution Required Per Month**: Rolled up from the Sinking Funds database [00:04:41].

### 3. Sinking Funds Overview Database

This database provides a summarized view of all types of sinking funds created [00:04:54].

It displays:
*   **Goal Amount**: The targeted savings for all funds combined [00:05:00].
*   **Amount Saved**: The total contributions made across all funds [00:05:05].
*   **Amount Left**: The remaining total contribution required (Goal Amount - Amount Saved) [00:05:12].
*   **Targeted Savings**: The minimum total contribution required each month, rolled up from other databases [00:05:22].
*   **Contribution in Percentage**: The total amount saved divided by the total targeted amount [00:05:29].
*   **Goal Date**: The target date by which the sinking funds should be fully accumulated [00:05:35].

### 4. Sinking Fund Summary Database

This database offers a summarized view for *each individual* sinking fund, similar to the overview but broken down per fund [00:05:42].

It includes:
*   **Targeted Goal Amount**: For the specific fund [00:05:44].
*   **Amount Saved So Far**: For the specific fund [00:05:46].
*   **Amount Left to Contribute Further**: For the specific fund [00:05:48].
*   **Contribution Made in Percentage**: For the specific fund [00:05:50].
*   **Targeted Goal Date**: For the specific fund [00:05:52].
*   **Contribution Required for Each Month**: For the specific fund [00:05:52].

All amounts in this summary are rolled up from the previously discussed databases [00:06:03]. This helps create a condensed form of the entire tracker [00:06:07].

### 5. Total Sinking Funds Database

This final database calculates the combined total values across *all* sinking funds [00:06:14].

It calculates:
*   **Targeted Sinking Funds Contribution** [00:06:19].
*   **Amount Saved** [00:06:21].
*   **Amount Left** [00:06:23].
*   **Contribution in Percentage**: Total contribution divided by the total targeted amount [00:06:23].

These values represent the sum total of all sinking funds combined [00:06:29] and are derived by rolling up respective values from the preceding databases [00:06:39].

## Primary Dashboard

The primary dashboard provides a user-friendly interface to view the aggregated information from these databases.

Key sections of the dashboard include:
*   **Summary Section**: Displays the total goal amount, amount saved, amount left, and contribution in percentage, representing the sum total of all sinking funds combined [00:06:53]. This section is linked to the "Total Sinking Funds" database and displayed in a gallery view [00:07:04].
*   **Sinking Funds Overview**: Provides a summary of all six types of sinking funds, showing their goal amount, amount saved, amount left, contribution percentage, end goal date, and required monthly contribution [00:07:08]. This is linked to the "Sinking Fund Summary" database in a gallery view [00:07:22].
*   **Sinking Funds Progress**: Shows monthly payments made towards each sinking fund and indicates if the contribution met the minimum required amount [00:07:27].
    *   A green tick indicates the contribution exceeded the minimum [00:07:38].
    *   A red cross indicates the contribution did not meet the minimum [00:07:40].
    *   This section is linked to the "Sinking Funds Details" database and displayed in a list format [00:07:45].

This comprehensive setup allows users to effectively track and manage their financial goals through a [[creating_and_using_databases_in_notion | structured database approach in Notion]].