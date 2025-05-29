---
title: Analyzing income frequency with databases
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

Analyzing income frequency is a crucial aspect of the Notion income tracker, providing insight into how often income is earned. This analysis helps in [[tracking_income_expenses_and_cash_flow_movements | tracking income]], [[using_periodical_income_analysis_in_notion | periodical income analysis]], and overall financial management <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Frequency of Income Section in the Tracker

Within the main Notion income tracker, a dedicated "Frequency of income" section displays:
*   How frequently income is earned <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   The total earnings for each frequency <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   The number of sources for each frequency of income <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Frequency of Income Database

To enable this analysis, a specific "Frequency of income database" is utilized <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This database offers a complete overview of how frequently income is earned over a given period <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Database Properties

The [[frequency_of_income_database | Frequency of Income Database]] includes the following key properties:

*   **Frequency** <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
    *   A title column that indicates the income frequency, such as:
        *   Monthly income <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
        *   Annual income <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>
        *   Quarterly income <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
        *   Half-yearly income <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>
        *   One-time income <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>

*   **Earnings Associated to Each Frequency of Income** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>
    *   A roll-up property derived from a related column <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Calculates the sum of the earnings amount for each frequency <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Represents the earnings associated with all forms of income for each mode of frequency <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

*   **Relation to Income Details Database** <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
    *   A relation property linked to the [[income_details_database | Income Details Database]] <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   Automatically generated, this property defines all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

*   **Sources of Income** <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>
    *   A formula property that calculates the number of sources for each frequency <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
    *   It defines the source count as "one source," "two sources," "three sources," or "no source" based on the number <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Integration and Presentation

The "frequency" property in the [[income_source_database | Income Source Database]] is a roll-up property that extracts the "frequency of income" from the [[income_details_database | Income Details Database]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

In the primary dashboard, the frequency analysis is presented by linking to the [[frequency_of_income_database | Frequency of Income Database]] and displaying it in a gallery layout <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This view shows the total earnings and the sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.