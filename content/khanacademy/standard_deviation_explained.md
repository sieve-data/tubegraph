---
title: Standard deviation explained
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

In statistics, beyond understanding the [[Mean in statistics | central tendency]] or [[Mean in statistics | average]] of a data set, it's crucial to understand how spread apart the data points are <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept is known as [[Measures of dispersion | dispersion]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Comparing Data Sets with the Same Mean

Consider two data sets:
*   Data Set 1: -10, 0, 10, 20, 30 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Data Set 2: 8, 9, 10, 11, 12 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

Let's calculate the [[Mean in statistics | arithmetic mean]] for both. Assuming these are entire populations, we're calculating the population [[Mean in statistics | mean]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

*   **Data Set 1 Mean**:
    (-10 + 0 + 10 + 20 + 30) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   **Data Set 2 Mean**:
    (8 + 9 + 10 + 11 + 12) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>

Both data sets have the exact same [[Mean in statistics | arithmetic mean]] of 10 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, visually, it's clear these sets are different <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. The numbers in Data Set 2 are very close to 10 (the furthest is only two away) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, while numbers in Data Set 1 are much further from 10 (some are 10 or 20 away) <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This indicates that Data Set 1 is "more disperse" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## [[Measures of dispersion | Measures of Dispersion]]

To quantify how spread out data is, we use [[Measures of dispersion | measures of dispersion]].

### [[Range as a measure of dispersion | Range]]

The simplest [[Measures of dispersion | measure of dispersion]] is the [[Range as a measure of dispersion | range]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It's calculated by subtracting the smallest number from the largest number in the data set <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

*   **Data Set 1 Range**:
    30 (largest) - (-10) (smallest) = 40 <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   **Data Set 2 Range**:
    12 (largest) - 8 (smallest) = 4 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>

Here, the [[Range as a measure of dispersion | range]] clearly shows Data Set 1 is more disperse <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. However, [[Range as a measure of dispersion | range]] doesn't always tell the whole story, as two data sets can have the same [[Range as a measure of dispersion | range]] but different distributions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### [[Variance and its calculation | Variance]]

A more commonly used [[Measures of dispersion | measure of dispersion]] is the [[Variance and its calculation | variance]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For a population, the symbol for [[Variance and its calculation | variance]] is sigma squared (σ²) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

To calculate [[Variance and its calculation | variance]]:
1.  Find the difference between each data point and the [[Mean in statistics | mean]].
2.  Square each of these differences.
3.  Take the average of these squared differences <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Let's calculate the [[Variance and its calculation | variance]] for our data sets (mean for both is 10):

*   **Data Set 1 [[Variance and its calculation | Variance]]**:
    ((-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²) / 5 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
    = ((-20)² + (-10)² + (0)² + (10)² + (20)²) / 5 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
    = (400 + 100 + 0 + 100 + 400) / 5 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
    = 1000 / 5 = 200 <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
    So, the [[Variance and its calculation | variance]] for Data Set 1 is 200 <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

*   **Data Set 2 [[Variance and its calculation | Variance]]**:
    ((8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²) / 5 <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
    = ((-2)² + (-1)² + (0)² + (1)² + (2)²) / 5 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
    = (4 + 1 + 0 + 1 + 4) / 5 <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>
    = 10 / 5 = 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
    So, the [[Variance and its calculation | variance]] for Data Set 2 is 2 <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The [[Variance and its calculation | variance]] clearly shows Data Set 2 is much less dispersed than Data Set 1 <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. One issue with [[Variance and its calculation | variance]] is that if your data has units (e.g., meters), the [[Variance and its calculation | variance]] will be in squared units (e.g., meters squared), which can be an "odd set of units" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### [[Standard deviation and its significance | Standard Deviation]]

To address the unit issue and make the [[Measures of dispersion | measure of dispersion]] more intuitive, statisticians often use [[Standard deviation and its significance | standard deviation]] <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The [[Standard deviation and its significance | standard deviation]] is simply the square root of the [[Variance and its calculation | variance]] <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Its symbol for a population is sigma (σ) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Data Set 1 [[Standard deviation and its significance | Standard Deviation]]**:
    √200 = √(100 * 2) = 10√2 ≈ 14.14 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>
*   **Data Set 2 [[Standard deviation and its significance | Standard Deviation]]**:
    √2 ≈ 1.41 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>

Data Set 1 has a [[Standard deviation and its significance | standard deviation]] that is approximately 10 times larger than Data Set 2's [[Standard deviation and its significance | standard deviation]] (10√2 vs. √2) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This intuitively makes sense, as the numbers in Data Set 1 are, on average, much further away from the mean of 10 compared to Data Set 2 <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

The [[Standard deviation and its significance | standard deviation]] provides a "much better sense of how far away, on [[Mean in statistics | average]], we are from the [[Mean in statistics | mean]]" <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.