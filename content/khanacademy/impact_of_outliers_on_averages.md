---
title: Impact of outliers on averages
videoId: uhxtUt_-GyM
---

From: [[khanacademy]] <br/> 

Statistics is broadly about "getting your head around data" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> and can be classified into descriptive, predictive, and [[inferential_statistics | inferential statistics]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Descriptive statistics involves finding indicative numbers that represent a large set of data without needing to examine every single piece of information <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

One of the primary goals in descriptive statistics is to describe the [[central_tendency_in_statistics | central tendency]] of a dataset <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This is often referred to as the "average" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> and aims to find a number most representative of the entire set <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Measures of [[central_tendency_measures | Central Tendency]]

There are several ways to measure [[central_tendency_in_statistics | central tendency]] or the average of a set of numbers <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>:

*   **[[mean_median_and_mode | Mean]] (Arithmetic Mean)**: This is the most common understanding of "average" in everyday speech <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. It is calculated by adding all the numbers in a set and dividing by the total count of numbers <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. For example, for the set {1, 1, 2, 3, 4}, the [[mean_in_statistics | mean]] is (1+1+2+3+4) / 5 = 11/5 = 2.2 <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

*   **[[mean_median_and_mode | Median]]**: This is the middle number in a dataset after it has been sorted in order <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. For a set with an odd number of data points, it's the single middle value <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. For a set with an even number of data points, the median is the arithmetic [[mean_in_statistics | mean]] of the two middle numbers <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. For {1, 1, 2, 3, 4}, the median is 2 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

*   **[[mean_median_and_mode | Mode]]**: This represents the most common number in a set <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. For {1, 1, 2, 3, 4}, the mode is 1 because it appears twice, more than any other number <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. A set can have multiple modes if several numbers share the highest frequency <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## The Impact of Outliers

While all three measures describe [[central_tendency_in_statistics | central tendency]], they react differently to "outliers"—numbers that "really stick out" from the rest of the data <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

Consider the dataset: {3, 3, 3, 3, 3, 100} <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

*   **Impact on the [[mean_in_statistics | Mean]]**:
    The arithmetic [[mean_in_statistics | mean]] for this set is (3+3+3+3+3+100) / 6 = 115 / 6 = 19 and 1/6 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This value of 19 and 1/6 "doesn't really seem indicative of this set" <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> because most numbers are 3, but the single value of 100 significantly "skews" the [[mean_in_statistics | mean]] away from the cluster of 3s <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

*   **Impact on the [[mean_median_and_mode | Median]]**:
    For the same set {3, 3, 3, 3, 3, 100}, the middle two numbers are 3 and 3 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The [[mean_in_statistics | mean]] of these two is (3+3)/2 = 3 <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. The median, 3, is "a better measurement of the [[central_tendency_in_statistics | central tendency]]" <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a> because it is "not so much affected by this really large number" <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

*   **Impact on the [[mean_median_and_mode | Mode]]**:
    In the set {3, 3, 3, 3, 3, 100}, the number 3 appears five times, while 100 appears only once <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Therefore, the [[mean_median_and_mode | mode]] is 3 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Like the median, the [[mean_median_and_mode | mode]] also provides a good indication of the typical values in the set, unaffected by the outlier <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Practical Implications

The choice of which measure of [[central_tendency_in_statistics | central tendency]] to use can depend on the presence of outliers and the specific context <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

> [!example] Average Home Prices
> If you're looking at average home prices in a city where most houses are $100,000 but one house costs a trillion dollars, the arithmetic [[mean_in_statistics | mean]] might be a million dollars, creating "a very wrong perception of that city" <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. In such a scenario, the median house price would remain $100,000, offering "a better sense of what the houses in that city are like" <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

The median and [[mean_median_and_mode | mode]] tend to be more robust to outliers than the arithmetic [[mean_in_statistics | mean]], providing a more representative picture of the data's [[central_tendency_in_statistics | central tendency]] when extreme values are present <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. These measures serve as "mathematical tools for getting our heads around numbers" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> and large datasets <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

In upcoming discussions, further descriptive statistics will explore how spread out numbers are from the [[central_tendency_in_statistics | central tendency]] <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.