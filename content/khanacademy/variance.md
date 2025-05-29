---
title: Variance
videoId: E4HAYd0QnRc
---

From: [[khanacademy]] <br/> 

While previous discussions focused on central tendency or the average of a data set <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, [[measures_of_dispersion | measures of dispersion]] like variance help to understand how spread apart the data is <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This is crucial because different data sets can have the same mean but vastly different spreads <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. For example, two data sets, `{-10, 0, 10, 20, 30}` and `{8, 9, 10, 11, 12}`, both have an arithmetic mean of 10 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, the first set is more [[measures_of_dispersion | dispersed]] than the second <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

The discussion here assumes calculations for an entire population's data, thus referring to "population variance" rather than "sample variance" <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Symbol for Variance

The symbol for variance is the Greek letter sigma squared (σ²) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This symbol's relationship to sigma (σ), the symbol for [[standard_deviation | standard deviation]], is intentional <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Definition and Calculation

[[concept_of_variance | Variance]] is defined as the average of the squared differences between each data point and the mean of the data set <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The squaring of differences ensures all values contribute positively to the measure of spread <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

The general formula for population variance (σ²) is:
σ² = Σ (xᵢ - μ)² / N
Where:
*   xᵢ = each individual data point
*   μ = the population mean
*   N = the total number of data points in the population

### Example 1: Calculation for Dispersed Data Set

Let's calculate the variance for the data set `{-10, 0, 10, 20, 30}`. The mean (μ) for this set is 10 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The calculation is as follows:
σ² = ((-10 - 10)² + (0 - 10)² + (10 - 10)² + (20 - 10)² + (30 - 10)²) / 5 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
σ² = ((-20)² + (-10)² + (0)² + (10)² + (20)²) / 5 <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>
σ² = (400 + 100 + 0 + 100 + 400) / 5 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
σ² = 1000 / 5 <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
σ² = 200 <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>

So, the variance for the first data set is 200 <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Example 2: Calculation for Less Dispersed Data Set

Now, let's calculate the variance for the data set `{8, 9, 10, 11, 12}`. The mean (μ) for this set is also 10 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The calculation is as follows:
σ² = ((8 - 10)² + (9 - 10)² + (10 - 10)² + (11 - 10)² + (12 - 10)²) / 5 <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
σ² = ((-2)² + (-1)² + (0)² + (1)² + (2)²) / 5 <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
σ² = (4 + 1 + 0 + 1 + 4) / 5 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
σ² = 10 / 5 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
σ² = 2 <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>

The variance for the second data set is 2 <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This much smaller variance indicates a significantly less [[measures_of_dispersion | dispersed]] data set compared to the first <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

## Limitations and Relationship to Standard Deviation

While variance effectively quantifies dispersion, it can result in an "arbitrary number" <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. If the original data has units (e.g., meters), the variance will have squared units (e.g., meters squared), which can be an "odd set of units" and difficult to interpret intuitively <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

To address this, statisticians often use [[standard_deviation | standard deviation]], which is simply the square root of the variance <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The symbol for [[standard_deviation | standard deviation]] is sigma (σ) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Taking the square root converts the units back to the original scale, making it more interpretable <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

For the first data set, the [[standard_deviation | standard deviation]] (σ) is √200, which simplifies to 10√2 <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. For the second data set, the [[standard_deviation | standard deviation]] (σ) is √2 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The fact that the first data set has approximately 10 times the [[standard_deviation | standard deviation]] of the second intuitively makes sense, as its data points are, on average, much further from the mean <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.