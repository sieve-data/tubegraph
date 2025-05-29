---
title: variance and standard deviation
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

This article expands on understanding how spread apart data is, building on previous discussions about [[measures_of_central_tendency|central tendency]] or the average of a data set <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Measures of dispersion help quantify this spread <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>.

## Data Sets Example

Consider two data sets:
*   Data Set 1: -10, 0, 10, 20, 30 <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>
*   Data Set 2: 8, 9, 10, 11, 12 <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>

Both data sets have the exact same arithmetic mean of 10 <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
*   For Data Set 1: (-10 + 0 + 10 + 20 + 30) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>
*   For Data Set 2: (8 + 9 + 10 + 11 + 12) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>

Despite having the same mean, the sets of numbers are clearly different <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. Data Set 1 is more dispersed, as its numbers are further away from the mean of 10 than those in Data Set 2 <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

### Population vs. Sample
In statistics, there's a distinction between a population (the entire data) and a sample (a subset of data used to estimate population characteristics) <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. For these examples, it is assumed that these are the entire populations of the data sets <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>, so we are dealing with population mean and population [[measures_of_dispersion|measures of dispersion]] <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

## Measures of Dispersion

### Range
The range is the simplest way to measure dispersion <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. It is calculated by subtracting the smallest number from the largest number in a data set <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

*   **Data Set 1 Range:** 30 (largest) - (-10) (smallest) = 40 <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>
*   **Data Set 2 Range:** 12 (largest) - 8 (smallest) = 4 <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>

The range shows that Data Set 1 has a much larger spread <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. However, range may not always give the whole picture, as two data sets can have the same range but different distributions <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

### Variance
Variance is a more commonly used measure of dispersion <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Symbol:** The symbol for population variance is `σ²` (sigma squared) <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Definition:** Variance is the average of the squared differences between each data point and the mean <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Squaring the differences ensures they are positive <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

#### Calculation of Variance:
1.  Subtract the mean from each data point.
2.  Square each of these differences.
3.  Sum up all the squared differences.
4.  Divide the sum by the number of data points.

*   **Data Set 1 Variance Calculation:**
    `σ² = [(-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²] / 5` <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>
    `σ² = [(-20)² + (-10)² + (0)² + (10)² + (20)²] / 5` <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>
    `σ² = (400 + 100 + 0 + 100 + 400) / 5` <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>
    `σ² = 1000 / 5 = 200` <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>
    The variance for Data Set 1 is 200 <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

*   **Data Set 2 Variance Calculation:**
    `σ² = [(8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²] / 5` <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>
    `σ² = [(-2)² + (-1)² + (0)² + (1)² + (2)²] / 5` <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>
    `σ² = (4 + 1 + 0 + 1 + 4) / 5` <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>
    `σ² = 10 / 5 = 2` <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>
    The variance for Data Set 2 is 2 <a class="yt-timestamp" data-t="09:11:00">[09:11:11]</a>.

The smaller variance for Data Set 2 indicates it is a less-dispersed data set <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

A potential issue with variance is that if the original data points have units (e.g., meters), the variance will have squared units (e.g., meters squared), which can be an "odd set of units" <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Standard Deviation
To address the units issue and provide a more intuitive measure, statisticians use standard deviation <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.
*   **Symbol:** The symbol for standard deviation is `σ` (sigma) <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   **Definition:** Standard deviation is simply the square root of the variance <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

#### Calculation of Standard Deviation:
1.  Calculate the variance.
2.  Take the square root of the variance.

*   **Data Set 1 Standard Deviation Calculation:**
    `σ = √Variance = √200` <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>
    `σ = √(100 * 2) = 10√2` <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>
    The standard deviation for Data Set 1 is approximately 14.14.

*   **Data Set 2 Standard Deviation Calculation:**
    `σ = √Variance = √2` <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>
    The standard deviation for Data Set 2 is approximately 1.414.

Data Set 1 has a standard deviation approximately 10 times larger than Data Set 2 (10√2 vs. √2) <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. This intuitively makes sense, as the numbers in Data Set 1 are, on average, further away from the mean than those in Data Set 2 <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. Standard deviation gives a better sense of "how far away, on average, we are from the mean" <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.