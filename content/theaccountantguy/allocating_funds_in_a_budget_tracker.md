---
title: Allocating funds in a budget tracker
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

Allocating available funds is the third step in setting up a minimalistic [[setting_up_a_personal_finance_tracker_in_notion | budget planner]] in Notion after filling out income and expense details <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This process involves distributing the funds remaining after subtracting expenses from income into various categories <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

## Calculating Available Funds

The "available funds" are calculated by subtracting total expenses from total income for each month <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. This calculation is performed using a formula within the Notion database <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## Fund Allocation Overview

The budget tracker includes a "fund allocation overview" section that analyzes how remaining funds are distributed among different allocation heads <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. Common allocation categories include:
*   **Investment** <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>
*   **Savings** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Others** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

Once specific amounts are allocated to these heads, a "total allocation" amount is calculated as the summation of investments, savings, and other allocations <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. These amounts are typically represented in a number format, such as US Dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

## Proportion of Allocation

The proportion of funds allocated to the total available funds is also calculated <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. This is determined by dividing the total allocation by the total available funds, and the result is typically converted into a percentage <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This percentage can be visually represented using a progress bar <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>.

## Quarterly Allocation Overview

A "quarterly allocation overview" provides a monthly breakdown of available funds and the proportion of funds allocated for each month, categorized by quarters <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.

## Database Linking and Properties

To facilitate these calculations and overviews, various databases are linked using Notion's relation and roll-up properties <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.

*   **Fund Allocation Overview Database:** Each individual fund allocation (investment, savings, others) is linked to an "allocation of funds" database <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This database typically displays the investment source, the allocation amount, and the percentage of allocation for each month <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
*   **Quarterly Allocation Overview Database:** This overview links to an "available funds" database and displays the month, total available funds, and the percentage of allocation for each individual month <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. Filters are applied to group data by quarters (e.g., Q1 for January, February, March) <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.
*   **Roll-up Properties:** A roll-up property is used to draw values like "total actual income" from the "month-of-income" database and "actual expense" from the "month of expense" database, setting them to sum values in the calculation part <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.