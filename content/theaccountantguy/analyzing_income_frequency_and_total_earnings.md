---
title: Analyzing income frequency and total earnings
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 
This article explains how to analyze income frequency and total earnings using a Notion-based tracking system. The system helps users stay on top of their finances <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Notion Income Tracker Overview
The [[notion_income_tracker_setup | Notion income tracker]] consists of four main sections <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
*   **Total Earnings** Shows the total amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Sources of Income** Displays total earnings for each individual income source (e.g., salary, side hustle) and their percentage of the total income <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Frequency of Income** Illustrates how frequently income is earned, including total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Overview Section** Provides [[monthly_and_yearly_budget_overviews | monthly income]] segregated into [[analyzing_savings_with_quarterly_and_summary_reviews | four quarters]], along with the percentage of [[monthly_and_yearly_budget_overviews | monthly earnings]] relative to total earnings <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Database Foundation
Building this minimalistic [[notion_income_tracker_setup | notion income tracker]] requires five databases <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:
*   [[using_notion_databases_for_income_details | Income details database]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
*   Income Source database <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Frequency of income database <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   Total earnings database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   Period database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

### Income Details Database
This database is used to feed the details related to income <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Key properties include:
*   **Income Details Property** (Title property): Specifies different sources of income received during the year <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Period of Income** (Relation property): Linked to the Period database, reflecting [[monthly_and_yearly_budget_overviews | monthly incomes]] for each income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source** (Relation property): Linked to the Income Source database, defining sources like salary or side hustle <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income** (Relation property): Linked to the Frequency of income database, specifying how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount** Shows the income earned for a specific period, with a sum of income at the end <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Frequency of Income Database
This database analyzes how frequently income is earned <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It includes:
*   **Frequency Column** (Title column): Indicates income frequency such as [[monthly_and_yearly_budget_overviews | monthly income]], annual, quarterly, half-yearly, or one-time income <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated** (Roll-up property): Derived from a related property in the [[using_notion_databases_for_income_details | Income details database]], calculating the sum of earnings for each frequency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property** Linked to the [[using_notion_databases_for_income_details | Income details database]], defining sources of income related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income** (Formula property): Calculates the number of sources based on the count, defining them as "one source," "two sources," "three sources," or "no source" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database
This database relates total earnings to all income sources <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Properties include:
*   **Total Earnings** (Title property): Describes the total earnings <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source** (Relation property): Established with the Income Source database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings** (Roll-up property): Rolls up values from income sources to calculate the sum of total earnings associated with them <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Dashboard Presentation
The primary [[dashboard_analysis_for_personal_finance | dashboard]] presents the total earnings <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>:
*   **Total Earnings Display** This is a linked view of the Total Earnings database, represented in a list format, showing the total income earned during the period <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Sources of Income Display** Presented in a three-column layout, linked to the Income Source database in a gallery format <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. It shows actual income and the percentage of each source relative to total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency Display** Derived from the Frequency of income database and displayed in a gallery format <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It presents total earnings and sources for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section Display** Linked to the Period database with a gallery presentation mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into [[analyzing_savings_with_quarterly_and_summary_reviews | four quarters]], with individual months specified for each <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. It shows earnings per month and the proportion of earnings to total earnings, with filters applied for respective months in each quarter <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.