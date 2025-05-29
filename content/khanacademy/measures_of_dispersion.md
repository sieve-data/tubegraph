---
title: Measures of Dispersion
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

[[Descriptive statistics | Descriptive statistics]] involves understanding not only the [[measures_of_central_tendency | central tendency]] or average of a data set, but also how spread apart the data points are <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Measures of dispersion quantify this spread, or how far data points are from the center, on average <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Why Measures of Dispersion are Important

Consider two data sets:
*   Data Set 1: -10, 0, 10, 20, 30 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Data Set 2: 8, 9, 10, 11, 12 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

Both data sets have the same [[mean and central tendency | arithmetic mean]] of 10 <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. However, the numbers in Data Set 2 are much closer to 10 compared to Data Set 1, where values can be significantly further away <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Data Set 1 is considered "more disperse" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

> [!NOTE] Population vs. Sample
> When discussing [[measures_of_central_tendency | measures of central tendency]] and dispersion, a distinction is made between a "population" (the entire data set) and a "sample" (a subset of the data) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. In this context, we assume we are dealing with the entire population, and thus use formulas for population mean and population measures of dispersion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. In advanced [[descriptive_statistics | statistics]], samples are often used to estimate population characteristics <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Types of Measures of Dispersion

### Range
The simplest measure of dispersion is the range, which is the difference between the largest and the smallest number in a data set <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Data Set 1:** Range = 30 - (-10) = 40 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
*   **Data Set 2:** Range = 12 - 8 = 4 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>

In this example, the range effectively shows that Data Set 1 is much more disperse <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. However, the range may not always provide a complete picture of how numbers are distributed <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Variance
[[Variance | Variance]] is a commonly used measure of dispersion <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For a population, the symbol for [[variance | variance]] is `σ²` (sigma squared) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

To calculate the [[variance | variance]]:
1.  Find the difference between each data point and the [[mean and central tendency | mean]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
2.  Square each of these differences <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This step ensures that all differences are positive <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
3.  Sum all the squared differences <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
4.  Divide the sum by the total number of data points (N) to find the average of the squared distances <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

#### Calculation for Data Set 1 (Mean = 10)
`σ² = [(-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²] / 5` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
`σ² = [(-20)² + (-10)² + (0)² + (10)² + (20)²] / 5` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
`σ² = [400 + 100 + 0 + 100 + 400] / 5` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
`σ² = 1000 / 5 = 200` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
The [[variance | variance]] for Data Set 1 is 200 <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

#### Calculation for Data Set 2 (Mean = 10)
`σ² = [(8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²] / 5` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
`σ² = [(-2)² + (-1)² + (0)² + (1)² + (2)²] / 5` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
`σ² = [4 + 1 + 0 + 1 + 4] / 5` <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
`σ² = 10 / 5 = 2` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
The [[variance | variance]] for Data Set 2 is 2 <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

The significantly smaller [[variance | variance]] for Data Set 2 indicates it is a much less-dispersed data set <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A drawback of [[variance | variance]] is that its units are squared (e.g., meters squared if the original data was in meters), which can be an "odd set of units" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Standard Deviation
The [[standard_deviation | standard deviation]] is the most commonly used measure of dispersion and is directly related to [[variance | variance]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The [[standard_deviation | standard deviation]] is simply the square root of the [[variance | variance]] <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The symbol for [[standard_deviation | standard deviation]] is `σ` (sigma) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Taking the square root converts the units back to the original units of the data <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

#### Calculation for Data Set 1
[[standard_deviation | Standard Deviation]] (`σ`) = `√(Variance)` = `√200` <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>
`σ = √(100 * 2) = 10√2` <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>

#### Calculation for Data Set 2
[[standard_deviation | Standard Deviation]] (`σ`) = `√(Variance)` = `√2` <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>

Data Set 1 has a [[standard_deviation | standard deviation]] approximately 10 times larger than Data Set 2 (10√2 ≈ 14.14, while √2 ≈ 1.41) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This intuitively makes sense, as the numbers in Data Set 1 are, on average, much further away from the mean than those in Data Set 2 <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. The [[standard_deviation | standard deviation]] provides a better sense of how far away, on average, data points are from the [[mean and central tendency | mean]] <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.