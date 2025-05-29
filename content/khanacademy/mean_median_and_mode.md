---
title: mean median and mode
videoId: uhxtUt_-GyM
---

From: [[khanacademy]] <br/> 

Statistics involves "getting your head around data" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It can be broadly classified into categories like [[descriptive_statistics | descriptive]], predictive, and inferential statistics <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

[[descriptive_statistics | Descriptive statistics]] aims to summarize a large dataset using indicative numbers without presenting all the raw data <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. One of the primary goals of [[descriptive_statistics | descriptive statistics]] is to find a number that best represents the "central tendency" or "average" of a set of numbers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This representative number gives a sense of where the data points tend to cluster <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

There are multiple ways to measure the [[measures_of_central_tendency | central tendency]] or "average" of a dataset <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The most common measures include the mean, the [[Median | median]], and the [[finding_the_mode | mode]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. These are all forms of an "average" in statistical terms <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## The Mean (Arithmetic Mean)

The [[Arithmetic mean | arithmetic mean]], often simply called the "mean," is what most people refer to when they talk about "average" in everyday conversation <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Calculating the Mean

To [[Calculating the mean | calculate the mean]], you sum all the numbers in the set and then divide by the total count of numbers in that set <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

**Example:**
For the set of numbers: 1, 1, 2, 3, 4 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>
Sum = 1 + 1 + 2 + 3 + 4 = 11 <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>
Count = 5 numbers <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>
Mean = 11 / 5 = 2.2 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>

In this example, 2.2 is considered a good representative number or the [[Mean or Central Tendency in Statistics | central tendency]] of the set <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Limitations of the Mean

The mean can be significantly affected by "outliers" – numbers that are very different from the rest of the data <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

**Example with an Outlier:**
Consider the set: 3, 3, 3, 3, 3, 100 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>
Sum = 3 + 3 + 3 + 3 + 3 + 100 = 115 <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>
Count = 6 numbers <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
Mean = 115 / 6 ≈ 19.17 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>

In this case, 19.17 does not seem very representative of a set largely composed of "3"s <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The single large number (100) "skews" the mean <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

## The Median

The [[Median | median]] is another measure of [[Mean or Central Tendency in Statistics | central tendency]] that is less affected by outliers <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### Understanding the Median

To find the [[Median | median]], you first arrange the numbers in numerical order <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The [[Median | median]] is then the middle number in that ordered set <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

**Example with Odd Number of Data Points:**
For the set: 1, 1, 2, 3, 4 (already in order) <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>
There are 5 numbers. The middle number is 2, as there are two numbers less than it and two numbers greater than it <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
The [[Median | median]] is 2 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

**Example with Even Number of Data Points:**
If the set has an even number of data points, there isn't a single middle number <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. In this case, you take the two middle numbers and calculate their [[Arithmetic mean | arithmetic mean]] <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

For the set: 1, 1, 2, 3, 4, 4 <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>
The two middle numbers are 2 and 3 <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
[[Calculating the mean | Mean]] of 2 and 3 = (2 + 3) / 2 = 2.5 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
The [[Median | median]] is 2.5 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Median's Robustness to Outliers

Let's revisit the outlier example: 3, 3, 3, 3, 3, 100 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
This set has an even number of points (6) and is already in order <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
The two middle numbers are both 3 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
[[Calculating the mean | Mean]] of 3 and 3 = (3 + 3) / 2 = 3 <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

In this case, the [[Median | median]] (3) is much more representative of the typical numbers in the set compared to the mean (19.17) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This shows how the [[Median | median]] is less affected by "outliers" – data points that stick out from the rest <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. For example, when discussing home prices, a single very expensive house (an outlier) could drastically inflate the mean, while the [[Median | median]] would provide a more accurate typical price <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## The Mode

The [[finding_the_mode | mode]] is considered the easiest measure of [[Mean or Central Tendency in Statistics | central tendency]] to determine <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Finding the Mode

The [[finding_the_mode | mode]] is simply the number that appears most frequently in a dataset <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

**Example:**
For the set: 1, 1, 2, 3, 4 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>
The number "1" appears twice, while other numbers appear only once <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
The [[finding_the_mode | mode]] is 1 <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Ambiguity with Multiple Modes

A dataset can have more than one [[finding_the_mode | mode]] if two or more numbers appear with the same highest frequency <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

**Example with Multiple Modes:**
For the set: 1, 1, 2, 3, 4, 4 <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
Both "1" and "4" appear twice, which is more than any other number <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
In this case, the modes could be 1 and 4 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Mode's Robustness to Outliers

Similar to the [[Median | median]], the [[finding_the_mode | mode]] is also not significantly affected by outliers <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
Revisiting the outlier example: 3, 3, 3, 3, 3, 100 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>
The number "3" appears five times, while "100" appears only once <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
The [[finding_the_mode | mode]] is 3 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Conclusion

The [[Arithmetic mean | mean]], [[Median | median]], and [[finding_the_mode | mode]] are all valid ways to measure the [[Mean or Central Tendency in Statistics | central tendency]] or "average" of a dataset <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. They are mathematical tools designed to help us understand large sets of data by providing a single representative number <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The choice of which measure to use often depends on the nature of the data and whether outliers are present <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

In the next discussion, we will explore other [[descriptive_statistics | descriptive statistics]], specifically [[measures_of_dispersion | measures of dispersion]], which describe how spread apart the data points are from the [[Mean or Central Tendency in Statistics | central tendency]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.