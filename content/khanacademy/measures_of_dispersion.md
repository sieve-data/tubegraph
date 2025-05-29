---
title: Measures of dispersion
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

While [[measures_of_central_tendency | central tendency measures]] like the mean describe the average of a data set, [[descriptive_statistics | descriptive statistics]] also requires understanding how spread out the data is <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This is where measures of dispersion come into play <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Illustrative Data Sets

Consider two distinct data sets that share the same [[mean_and_central_tendency | arithmetic mean]]:

1.  **Data Set 1**: -10, 0, 10, 20, 30 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
    *   **Mean Calculation**: (-10 + 0 + 10 + 20 + 30) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
2.  **Data Set 2**: 8, 9, 10, 11, 12 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
    *   **Mean Calculation**: (8 + 9 + 10 + 11 + 12) / 5 = 50 / 5 = 10 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>

Both data sets have an arithmetic mean of 10 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, it is clear that the numbers in Data Set 1 are much more spread out than those in Data Set 2, where numbers are very close to 10 <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This difference in spread highlights the need for measures of dispersion <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

> [!NOTE] Population vs. Sample
> For these calculations, it's assumed that the given data represents the entire population rather than a sample <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Measures of Dispersion

### [[range_as_a_measure_of_dispersion | Range]]

The [[range_as_a_measure_of_dispersion | range]] is the simplest measure of dispersion <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It is calculated by subtracting the smallest number from the largest number in a data set <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

*   **Data Set 1**: Largest number (30) - Smallest number (-10) = 30 - (-10) = 40 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
*   **Data Set 2**: Largest number (12) - Smallest number (8) = 12 - 8 = 4 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>

The range effectively shows that Data Set 1 has a much larger spread than Data Set 2 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. However, the [[range_as_a_measure_of_dispersion | range]] doesn't always provide a complete picture, as two data sets could have the same range but different internal distributions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Variance

The variance is a more robust measure of dispersion <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For a population, its symbol is sigma squared (σ²) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. It is defined as the average of the squared differences between each data point and the mean <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Squaring the differences ensures that all values contribute positively to the measure of spread <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

#### Calculation for Data Set 1 (Mean = 10):

σ² = [(-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²] / 5 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
σ² = [(-20)² + (-10)² + (0)² + (10)² + (20)²] / 5 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
σ² = [400 + 100 + 0 + 100 + 400] / 5 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
σ² = 1000 / 5 = 200 <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>

#### Calculation for Data Set 2 (Mean = 10):

σ² = [(8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²] / 5 <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
σ² = [(-2)² + (-1)² + (0)² + (1)² + (2)²] / 5 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
σ² = [4 + 1 + 0 + 1 + 4] / 5 <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>
σ² = 10 / 5 = 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>

The variance of Data Set 1 (200) is significantly larger than Data Set 2 (2), indicating a much greater spread <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A drawback of variance is that its units are squared (e.g., if data is in meters, variance is in meters squared), which can be counter-intuitive <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### [[standard_deviation_explained | Standard Deviation]]

The [[standard_deviation_and_its_significance | standard deviation]] is the most commonly used measure of dispersion <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. It is simply the square root of the variance <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Its symbol for a population is sigma (σ) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Taking the square root brings the units back to the original scale of the data, making it more interpretable <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

#### Calculation for Data Set 1:

σ = √Variance = √200 <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>
σ = √(100 * 2) = 10√2 ≈ 14.14 <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>

#### Calculation for Data Set 2:

σ = √Variance = √2 ≈ 1.41 <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

[[sampling_distribution_and_standard_deviation | Standard deviation]] provides a more intuitive sense of the average distance of data points from the mean <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Data Set 1 has a standard deviation approximately 10 times larger than Data Set 2 (10√2 vs. √2) <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>, which aligns with the observation that its values are much further from the mean on average <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.