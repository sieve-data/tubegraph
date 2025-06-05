---
title: Consequences of software glitches in financial systems
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

Software glitches within financial systems can lead to significant monetary losses, legal ramifications, and systemic disruptions. These issues highlight the critical need for robust testing, clear user interfaces, and careful management of software updates.

## Notable Incidents

### 2024 Chase ATM Glitch
In 2024, a glitch affected JP Morgan Chase's ATM system. Banking systems often rely on proprietary code, some written decades ago in languages like COBOL <a class="yt-timestamp" data-t="03:23">[03:23]</a>. Typically, deposited checks require several days to clear before funds can be withdrawn <a class="yt-timestamp" data-t="03:29">[03:29]</a>. However, a software error prevented this safeguard, allowing individuals to deposit fake checks and immediately withdraw tens of thousands of dollars from ATMs <a class="yt-timestamp" data-t="03:34">[03:34]</a>. This act, constituting check fraud <a class="yt-timestamp" data-t="03:47">[03:47]</a>, resulted in individuals' bank accounts going deep into the red, leading to lawsuits and potential criminal charges <a class="yt-timestamp" data-t="03:51">[03:51]</a>.

### 1982 Vancouver Stock Exchange Rounding Error
In 1982, the Vancouver Stock Exchange's index began to gradually decrease in value due to a subtle rounding error <a class="yt-timestamp" data-t="06:42">[06:42]</a>. The error was so minor that it went unnoticed for two years <a class="yt-timestamp" data-t="06:48">[06:48]</a>. The index, which started at 1,000, dropped to 520 over this period <a class="yt-timestamp" data-t="06:50">[06:50]</a>. The software was truncating each stock price change to two decimal places instead of rounding <a class="yt-timestamp" data-t="07:03">[07:03]</a>. While the impact of a single stock on an index of thousands is minor, the cumulative rounding error over time significantly distorted the index's value <a class="yt-timestamp" data-t="07:07">[07:07]</a>. Ultimately, the entire index had to be recalculated from scratch <a class="yt-timestamp" data-t="07:14">[07:14]</a>.

### 2014 Knight Capital Trading Algorithm Error
Knight Capital, a company that used algorithms for stock market trades, experienced a severe financial loss due to a software error <a class="yt-timestamp" data-t="10:44">[10:44]</a>. Developers accidentally linked a variable name to an outdated testing algorithm called "Power Peg," which had been inactive since 2003 <a class="yt-timestamp" data-t="10:47">[10:47]</a>. This algorithm was designed to manipulate virtual markets by buying high and selling low, the opposite of profitable trading <a class="yt-timestamp" data-t="10:53">[10:53]</a>. When deployed to production, the algorithm malfunctioned, flooding the New York Stock Exchange with 4 million incorrect trades in just 45 minutes <a class="yt-timestamp" data-t="11:06">[11:06]</a>. This resulted in Knight Capital losing $440 million in a single day, wiping out 75% of investors' equity <a class="yt-timestamp" data-t="11:13">[11:13]</a>.

### 2020 City Bank UI Disaster
In 2020, Citibank faced a significant issue due to a poorly designed user interface (UI) <a class="yt-timestamp" data-t="09:30">[09:30]</a>. The bank intended to make an interest payment of $8 million but inadvertently transferred the full loan amount of approximately $900 million <a class="yt-timestamp" data-t="09:34">[09:34]</a>. The software's confusing three-screen payment process and ambiguous checkboxes led operators to believe they were only authorizing interest payments, when in reality, they were initiating the transfer of the full principal <a class="yt-timestamp" data-t="09:44">[09:44]</a>. When Citibank attempted to reclaim the mistakenly transferred funds, the lenders refused, and a court ultimately ruled in favor of the lenders, allowing them to keep the $900 million <a class="yt-timestamp" data-t="09:53">[09:53]</a>.