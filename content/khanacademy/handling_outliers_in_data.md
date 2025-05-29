---
title: Handling outliers in data
videoId: uhxtUt_-GyM
---

From: [[khanacademy]] <br/> 

When analyzing data, some values may significantly differ from others. These extreme values are known as outliers <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. While there isn't a strict formal definition, an outlier is generally considered a number that "really sticks out" from the rest of the dataset <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Outliers can sometimes be due to measurement errors <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## Impact on Measures of Central Tendency

Different measures of central tendency are affected by outliers in varying ways. These measures aim to find a single number that is most indicative or representative of an entire set of numbers <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

Consider the following set of numbers: `3, 3, 3, 3, 3, 100` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Here, `100` acts as an outlier.

### Arithmetic Mean

The arithmetic mean (often simply called the "average" in everyday conversation <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>) is calculated by adding all numbers in a set and dividing by the count of numbers <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

For the set `3, 3, 3, 3, 3, 100`:
*   Sum = `3 + 3 + 3 + 3 + 3 + 100 = 115` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>
*   Count = `6`
*   Mean = `115 / 6 = 19 1/6` (approximately 19.17) <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>

The arithmetic mean is highly sensitive to outliers <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. In this example, 19 1/6 does not seem very representative of a set largely composed of 3s <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For instance, if discussing average home prices where most houses are $100,000 but one costs a trillion dollars, the mean would give a misleadingly high average price, like a million dollars, which wouldn't accurately reflect the city's housing market <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Median

The [[understanding_median | median]] is the middle number in a dataset after [[ordering_data_sets | putting the numbers in order]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. If there's an even number of data points, the median is the arithmetic mean of the two middle numbers <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

For the ordered set `3, 3, 3, 3, 3, 100`:
*   Since there are six numbers (an even count), the middle two numbers are `3` and `3` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   Median = `(3 + 3) / 2 = 3` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>

The median is more robust to outliers because it only considers the position of values rather than their absolute magnitudes <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. In the house price example, the median house price would remain $100,000, providing a much better sense of typical home values <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

### Mode

The mode is the number that appears most frequently in a set <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

For the set `3, 3, 3, 3, 3, 100`:
*   The number `3` appears five times, while `100` appears only once <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   Mode = `3` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>

Like the median, the mode is less affected by outliers, as it focuses on the most common value. If there are multiple numbers with the same highest frequency, a dataset can have multiple modes <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Choosing the Right Measure

When an outlier is present, the median and mode often provide a better indication of the dataset's central tendency compared to the arithmetic mean <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. This is particularly true in contexts like house prices, where a few extremely expensive properties can skew the mean <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

However, the "best" measure depends on the specific application:
*   If the dataset represents scores on a test, and one student performed exceptionally well while others struggled, the mean might still be useful if the goal is to understand the overall class performance, including that high score <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   If the outlier is suspected to be a genuine error, or if the aim is to describe the typical value, the median or mode might be preferred <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

Ultimately, these measures are human constructs designed to help understand large datasets <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The choice of which measure to use depends on what aspect of the central tendency one wishes to represent <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.