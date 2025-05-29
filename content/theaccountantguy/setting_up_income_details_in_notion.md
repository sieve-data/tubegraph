---
title: Setting Up Income Details in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

This article details how to [[Creating a Notion Income Tracker | create]] and manage your income data within a Notion budget planner, enabling you to [[Tracking income and expenses in Notion | track income and expenses]] in one central location <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It focuses on the initial setup of income details, which is the first of three steps to [[Setting up Notion for personal finance tracking | setting up a personal finance tracker in Notion]] <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a>.

## Components of the Income Details Setup

The income details setup involves creating an inline database and populating it with specific columns to capture comprehensive income information <a class="yt-timestamp" data-t="02:46:46">[02:46:46]</a>.

### Creating the Income Details Database

To begin, you need to sign up for a Notion account <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>. Then, create an inline database by typing `/` (forward slash) and selecting "database inline" from the options <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>. You can name this database by clicking on the three dots, selecting "layout options," and then "show database title" to make it visible and editable <a class="yt-timestamp" data-t="04:13:13">[04:13:13]</a>. A suggested name for this database is "Expected Income Source Details" <a class="yt-timestamp" data-t="04:11:11">[04:11:11]</a>.

### Database Columns

The income details database includes the following columns:

*   **Income Details** (Title Property): This is the default property and specifies each individual income earned in a particular month <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a> <a class="yt-timestamp" data-t="04:04:04">[04:04:04]</a>.
*   **Source of Income** (Relation Property): This column categorizes each income (e.g., salary, side hustle, other sources) and is linked to a separate "Income Type Database" <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> <a class="yt-timestamp" data-t="04:40:40">[04:40:40]</a> <a class="yt-timestamp" data-t="08:03:03">[08:03:03]</a>.
*   **Month of Income** (Relation Property): Specifies the month when income is earned, linked to a "Month of Income" database <a class="yt-timestamp" data-t="03:20:20">[03:20:20]</a> <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a> <a class="yt-timestamp" data-t="09:51:51">[09:51:51]</a>.
*   **Frequency of Income** (Relation Property): Indicates how frequently income is earned (e.g., recurring, one-time), linked to a "Frequency of Income" database <a class="yt-timestamp" data-t="03:25:25">[03:25:25]</a> <a class="yt-timestamp" data-t="05:10:10">[05:10:10]</a> <a class="yt-timestamp" data-t="11:23:23">[11:23:23]</a>.
*   **Expected Income** (Number Property): Represents the anticipated income for a month. The number format can be set to US Dollars or any preferred currency <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a> <a class="yt-timestamp" data-t="05:25:25">[05:25:25]</a>.
*   **Actual Income** (Number Property): Records the actual income earned at the end of a month. This also uses a number property with a currency format <a class="yt-timestamp" data-t="03:46:46">[03:46:46]</a> <a class="yt-timestamp" data-t="05:43:43">[05:43:43]</a>.
*   **Difference** (Formula Property): Calculates the difference between actual income and expected income for any given month <a class="yt-timestamp" data-t="03:53:53">[03:53:53]</a> <a class="yt-timestamp" data-t="06:03:03">[06:03:03]</a>.

### Analyzing Income Data with Linked Databases and Roll-ups

To gain deeper insights and display various summaries, the income details database is linked to other databases using "relation" and "roll-up" properties <a class="yt-timestamp" data-t="06:22:22">[06:22:22]</a>.

#### Actual vs. Estimated Income Overview

This section provides an overview of actual versus estimated income for different income sources (salary, side hustle, others) <a class="yt-timestamp" data-t="06:41:41">[06:41:41]</a>. It is powered by linking to an "Income Type Database" <a class="yt-timestamp" data-t="08:07:07">[08:07:07]</a> and utilizing roll-up properties:

*   **Roll-up Property**: Used to pull the desired properties (e.g., actual income, expected income) from the original income details database based on the established relation <a class="yt-timestamp" data-t="08:39:39">[08:39:39]</a>.
*   **Calculations**: Sums are calculated for total actual income and total budgeted income for each source <a class="yt-timestamp" data-t="08:49:49">[08:49:49]</a>. Differences and percentage changes are also calculated using formulas <a class="yt-timestamp" data-t="08:24:24">[08:24:24]</a>.

#### Quarterly Income Overview

This section shows the total actual income and the proportion of actual income to budgeted income for each month, divided into four quarters <a class="yt-timestamp" data-t="06:57:57">[06:57:57]</a>. This view links to the "Month of Income" database <a class="yt-timestamp" data-t="09:57:57">[09:57:57]</a>:

*   **Roll-up for Monthly Data**: Roll-up properties are used to calculate expected income, actual income, and the proportion of actual to budgeted income for each month <a class="yt-timestamp" data-t="10:11:11">[10:11:11]</a>.
*   **Percentage Calculation**: A formula calculates the percentage of budgeted income by dividing total actual income by total expected income and converting it to a percentage format, which can also be represented by a bar <a class="yt-timestamp" data-t="10:54:54">[10:54:54]</a>.
*   **Quarterly Filtering**: On the main dashboard, this linked database is set to a "gallery motive view" and filtered for each quarter (e.g., Q1 for Jan, Feb, March) <a class="yt-timestamp" data-t="15:40:40">[15:40:40]</a>.

#### Frequency of Income Overview

This section displays how frequently income is earned (recurring or one-time) and the total actual income and proportion for each type <a class="yt-timestamp" data-t="07:08:08">[07:08:08]</a>. It links to the "Frequency of Income" database <a class="yt-timestamp" data-t="11:35:35">[11:35:35]</a>:

*   **Roll-up for Frequency Data**: Roll-up properties are used to find the total actual and expected income for recurring and one-time income <a class="yt-timestamp" data-t="11:43:43">[11:43:43]</a>.
*   **Proportion Calculation**: A formula calculates the total proportion of each form of income to the overall total actual income <a class="yt-timestamp" data-t="12:37:37">[12:37:37]</a>.

#### Income Variance Distribution

A separate database, "Income Variance Distribution," is used to provide a summary of total estimated income, total actual income, the difference, and the percentage change for each income head <a class="yt-timestamp" data-t="13:08:08">[13:08:08]</a>. This database links to the "Income Type Database" and uses roll-up properties combined with IF formulas to display the relevant values based on the income type <a class="yt-timestamp" data-t="13:22:22">[13:22:22]</a>.

### Linking Income Details to the Main Dashboard

On the primary budget planner dashboard, the various income overviews (actual vs. estimated, quarterly, frequency) are displayed by [[setting_up_a_personal_finance_tracker_in_notion | linking databases]] <a class="yt-timestamp" data-t="14:45:45">[14:45:45]</a>.

To link a database, type `/` (forward slash) and select "link database" <a class="yt-timestamp" data-t="15:02:02">[15:02:02]</a>. You then select the specific database you want to display (e.g., Income Variance Distribution for actual vs. estimated income, Month of Income for quarterly overview, Frequency of Income for frequency breakdown) <a class="yt-timestamp" data-t="15:22:22">[15:22:22]</a>. For quarterly views, filters are applied to show specific months for each quarter (e.g., Q1 filters for January, February, and March) <a class="yt-timestamp" data-t="15:46:46">[15:46:46]</a>. Properties can be hidden or displayed to show only the most relevant information <a class="yt-timestamp" data-t="16:02:02">[16:02:02]</a>.

This comprehensive setup ensures that your income is meticulously tracked and analyzed within Notion <a class="yt-timestamp" data-t="16:28:28">[16:28:28]</a>.