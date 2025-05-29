---
title: outliers in statistical data
videoId: uhxtUt_-GyM
---

From: [[khanacademy]] <br/> 

In the field of [[introduction_to_statistics | statistics]], an outlier is a data point that significantly differs from other observations within a dataset <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. While there isn't a single formal definition, an outlier is generally understood as a number that "really sticks out" from the rest of the data <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Such values can sometimes result from measurement errors or other anomalies <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## Impact on [[Mean or Central Tendency in Statistics | Central Tendency]] Measures

Outliers can have a considerable impact on various [[Mean or Central Tendency in Statistics | measures of central tendency]], which are values that represent the center or typical value of a dataset.

### Arithmetic Mean

The [[mean median and mode | arithmetic mean]] is particularly sensitive to outliers <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
For example, consider a dataset: 3, 3, 3, 3, 3, 100 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The number 100 acts as an outlier in this set <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
The [[mean median and mode | arithmetic mean]] is calculated as the sum of all numbers divided by the count of numbers <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. For this set, the sum is 115, and there are 6 numbers, yielding a mean of approximately 19.17 (115/6) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This value might not feel truly representative of a set largely composed of 3s <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. In this scenario, the [[mean median and mode | arithmetic mean]] is "skewed" by the outlier <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

### Median

The [[mean median and mode | median]] is less affected by outliers compared to the [[mean median and mode | arithmetic mean]] <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. The [[mean median and mode | median]] is the middle number in a sorted dataset <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
For the dataset 3, 3, 3, 3, 3, 100, the numbers are already in order <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Since there is an even number of data points (6), the median is the [[mean median and mode | arithmetic mean]] of the two middle numbers <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>, which are both 3 <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The median is therefore 3 <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This provides a more indicative measure of the data's [[Mean or Central Tendency in Statistics | central tendency]] when an outlier is present <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Mode

The [[mean median and mode | mode]] is the number that appears most frequently in a dataset <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Like the [[mean median and mode | median]], the [[mean median and mode | mode]] is generally robust to the presence of outliers.
For the dataset 3, 3, 3, 3, 3, 100, the number 3 appears five times, while 100 appears only once <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Thus, the [[mean median and mode | mode]] is 3 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

In the presence of an outlier, the [[mean median and mode | median]] and [[mean median and mode | mode]] often provide a better indication of what the numbers in a set truly represent compared to the [[mean median and mode | arithmetic mean]] <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

## Real-Life Example

Consider average home prices in a city <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. If most houses cost $100,000, but there's one house priced at a trillion dollars, the [[mean median and mode | arithmetic mean]] might suggest an average house price of a million dollars <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. This figure would give a very misleading perception of the city's housing market <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. In contrast, the [[mean median and mode | median]] house price would remain $100,000, offering a more accurate understanding of typical home values <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

## Further Exploration

Understanding [[descriptive_statistics | descriptive statistics]] involves analyzing not only [[Mean or Central Tendency in Statistics | central tendency]] but also how spread apart data points are <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. This concept is explored further through [[measures of dispersion | measures of dispersion]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.