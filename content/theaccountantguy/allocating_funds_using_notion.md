---
title: Allocating Funds Using Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

The [[using_notion_for_budgeting | minimalistic budget planner]] in Notion is designed to track income and expenses in a central location, categorize expenses for improvement, and set and monitor monthly budgets <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This dashboard allows users to fix monthly income goals to assess overall performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. One of the key functionalities of this planner is the allocation of available funds <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

The dashboard consists of three primary segments: the summary segment, income details, and expense details <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The fund allocation overview is a component within the summary segment <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Setting Up Fund Allocation

Setting up the budget planner involves three simple steps <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
1.  Filling out income details <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
2.  Filling out expense details <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  Allocating available funds <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Calculating Available Funds

After entering income and expense details, the next step is to calculate the available funds. This is done by subtracting total expenses from total income for each month <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. A formula is used within a Notion database to compute "income less expenses" to determine the available funds for each month <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

### Allocating Funds to Different Heads

Once the total available funds are calculated, these funds can be allocated to various categories, such as investment, savings, and other allocations <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

The fund allocation overview provides an analysis of the remaining funds distributed among these different heads <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>:
*   **Investment Section** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>
*   **Savings Section** <a class="yt="yt-timestamp" data-t="00:20:38">[00:20:38]</a>
*   **Others Section** <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>

The allocation amounts for investments, savings, and others are typically set as number properties formatted in US Dollars <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

The "Total Allocation" is the summation of the investment, savings, and other allocations, represented by a formula <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. The "Percentage of Allocation" is calculated by dividing the total allocation by the total available funds <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. This percentage is often represented by a bar in Notion <a class="yt-timestamp" data-t="00:22:39">[00:22:39]</a>.

### Quarterly Allocation Overview

The planner also includes a quarterly allocation overview, which provides a monthly breakdown of total available funds and the proportion of funds allocated for each month <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This is detailed for each individual quarter of the year <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

### Database Linking and Properties

For the fund allocation overview, each individual fund calculation is linked to the "allocation of funds" database <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. This database is typically displayed in a gallery layout, showing properties such as "Investment Source," "Allocation Amount," and "Percentage of Allocation of Each Month" <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

The quarterly allocation overview is linked to an "available funds" database and set to a gallery mode <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. It displays the month, total available funds, and the percentage of allocation for the individual month <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Calculations for different quarters are performed accordingly <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

Linked databases are used to retrieve information from other parts of the budget planner <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. For example, the total actual income is retrieved using a roll-up property from the "month-of-income" database <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>, and actual expense data is linked to the "month of expense" database <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.