---
title: measures of dispersion
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

[[descriptive_statistics | Descriptive statistics]] provide ways to understand and summarize data. While [[measures_of_central_tendency | measures of central tendency]] describe the "average" or center of a data set, [[measures_of_dispersion | measures of dispersion]] (also known as measures of spread) quantify how spread apart the data points are <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

Consider two distinct data sets that have the same arithmetic mean:
1.  Data Set 1: `[-10, 0, 10, 20, 30]` <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
2.  Data Set 2: `[8, 9, 10, 11, 12]` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

Both data sets have an arithmetic [[mean median and mode | mean]] of 10 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, Data Set 1 is clearly more dispersed, with numbers further away from the mean, while Data Set 2 has numbers very close to the mean <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. [[measures_of_dispersion | Measures of dispersion]] help quantify this difference.

> [!NOTE] Population vs. Sample
> When discussing statistical measures, it's important to distinguish between a **population** (the entire data set) and a **sample** (a subset of the data) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For these calculations, it is assumed that the provided data sets represent the entire population <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Types of Measures of Dispersion

### Range

The **range** is the simplest [[measures_of_dispersion | measure of dispersion]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It is calculated by subtracting the smallest number in a data set from the largest number <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

*   **Data Set 1**:
    *   Largest number: 30 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
    *   Smallest number: -10 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
    *   Range = 30 - (-10) = 40 <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>
*   **Data Set 2**:
    *   Largest number: 12 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>
    *   Smallest number: 8 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>
    *   Range = 12 - 8 = 4 <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>

In this example, the range clearly shows Data Set 1 is more dispersed (range of 40) compared to Data Set 2 (range of 4) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. However, the range does not always provide a complete picture of how numbers are bunched up within the data set <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Variance

The **variance** is a more commonly used [[measures_of_dispersion | measure of dispersion]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For a population, the symbol for variance is `σ²` (sigma squared) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

To calculate the variance:
1.  Find the difference between each data point and the mean.
2.  Square each of these differences (to make them positive and emphasize larger differences).
3.  Sum all the squared differences.
4.  Divide the sum by the total number of data points (for population variance) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Data Set 1** (Mean = 10):
    *   `σ² = [(-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²] / 5` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
    *   `σ² = [(-20)² + (-10)² + (0)² + (10)² + (20)²] / 5` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
    *   `σ² = [400 + 100 + 0 + 100 + 400] / 5` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
    *   `σ² = 1000 / 5 = 200` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
    *   The variance for Data Set 1 is 200 <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

*   **Data Set 2** (Mean = 10):
    *   `σ² = [(8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²] / 5` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
    *   `σ² = [(-2)² + (-1)² + (0)² + (1)² + (2)²] / 5` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
    *   `σ² = [4 + 1 + 0 + 1 + 4] / 5` <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
    *   `σ² = 10 / 5 = 2` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
    *   The variance for Data Set 2 is 2 <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

The smaller variance for Data Set 2 (2 vs. 200) indicates it is a much less-dispersed data set <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A drawback of variance is that if the original data has units (e.g., meters), the variance will have squared units (e.g., meters squared), which can be arbitrary <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Standard Deviation

The **standard deviation** is another widely used [[measures_of_dispersion | measure of dispersion]], often preferred over variance <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. It is simply the square root of the variance <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The symbol for population standard deviation is `σ` (sigma) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Taking the square root returns the measure to the original units of the data, making it more interpretable <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

*   **Data Set 1** (Variance = 200):
    *   `σ = √200 = √(100 * 2) = 10√2` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
*   **Data Set 2** (Variance = 2):
    *   `σ = √2` <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

Data Set 1 has a standard deviation approximately 10 times larger than Data Set 2 (10√2 ≈ 14.14 vs. √2 ≈ 1.41) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This intuitively makes sense, as Data Set 1's numbers are, on average, much further away from the mean compared to Data Set 2's numbers <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. The standard deviation provides a clearer sense of the average distance of data points from the mean <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.