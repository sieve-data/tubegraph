---
title: Using periodical income analysis in Notion
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

Effectively [[managing_finances_using_notion | managing finances using Notion]] involves [[creating_an_income_tracker_in_notion | creating an income tracker in Notion]] that includes a detailed overview of periodical income. This analysis provides insights into monthly earnings, segregated by quarters, and the proportion of these earnings to the total income <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Core Components for Periodical Income Analysis

To build this minimalistic Notion income tracker, five databases are required <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The most crucial for periodical analysis is the **Period database** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### The Period Database

The Period database is designed to [[deriving_specific_period_sales_data_in_notion | calculate periodical income]] for each month and conduct further analysis <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It also displays the percentage of each month's earnings relative to the total annual earnings <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

Key properties within the Period database include:
*   **Month**: A title-type property representing the specific month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A relation property linked to the Income Details database, showing the income earned <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This relation helps reflect monthly incomes for each income source <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Earnings**: A roll-up property derived from the Income Details database, calculating the sum of earnings for the period <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A roll-up property sourced from the Total Earnings database, displaying the overall earnings amount <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This shows the earnings for each month and the combined total earnings across all months <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Proportion of Earnings**: A formula property that calculates the percentage of each month's earnings relative to the total earnings, formatted as a green percentage bar <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Presenting Periodical Income Data

The "Overview section" of the primary dashboard is dedicated to presenting periodical income analysis <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Overview Section

The Overview section is linked to the Period database and is displayed in a gallery mode <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Quarterly Segregation**: Information is divided into four quarters, with individual months specified for each quarter <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Earnings Display**: This section shows the earnings for each month and the proportion of these earnings towards the total earnings <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Filtering**: Filters are applied to each quarter to specify the respective months <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

This setup allows for comprehensive [[monthly_and_yearly_financial_overviews_in_notion | monthly and yearly financial overviews in Notion]], enabling users to stay on top of their finances <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.