---
title: Standard Deviation and its Relation to Variance
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

This article will review concepts related to [[Mean or Central Tendency in Statistics | mean]] and [[variance_and_its_calculation_for_population_and_sample | variance]], and introduce the [[Standard deviation and sampling distribution | standard deviation]], explaining its relationship to [[variance_and_its_calculation_for_population_and_sample | variance]] and how these are calculated for both populations and samples <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Key Statistical Concepts: Population vs. Sample <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

When dealing with statistical concepts, it's important to distinguish between a **population** (the entire group of interest) and a **sample** (a subset of the population) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Mean (Central Tendency) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
The [[Mean or Central Tendency in Statistics | mean]] is a common way to measure the average or [[Mean or Central Tendency in Statistics | central tendency]] of a data set, alongside the median and mode <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The [[Mean or Central Tendency in Statistics | mean]] is frequently used, especially when discussing [[variance_and_its_calculation_for_population_and_sample | variances]] and [[Standard deviation and sampling distribution | standard deviation]] <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

*   **Population Mean (μ)**:
    The [[Mean or Central Tendency in Statistics | mean]] of a population (mu, μ) is calculated by summing each data point (xᵢ) in the population from the first to the Nth (where N is the total number of data points in the population) and dividing by N <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
    <div style="text-align: center;">μ = Σxᵢ / N</div>
    This is the traditional average calculation <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

*   **Sample Mean (x̄)**:
    The [[Mean or Central Tendency in Statistics | mean]] of a sample (x-bar, x̄) is calculated similarly, but using data points from the sample (xᵢ) summed from the first to the nth (where n is the number of data points in the sample, typically n < N) and dividing by n <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>:
    <div style="text-align: center;">x̄ = Σxᵢ / n</div>
    If 'n' were equal to 'N', it would simply be the [[Mean or Central Tendency in Statistics | mean]] of the entire population <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Variance <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
[[variance_and_its_calculation_for_population_and_sample | Variance]] measures how far, on average, data points are from the [[Mean or Central Tendency in Statistics | mean]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It quantifies the average of the squared distances from the [[Mean or Central Tendency in Statistics | mean]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Population Variance (σ²)**:
    The [[variance_and_its_calculation_for_population_and_sample | variance]] of a population (sigma squared, σ²) is calculated by taking each data point (xᵢ), finding the difference between it and the population [[Mean or Central Tendency in Statistics | mean]] (μ), squaring that difference, summing all these squared differences, and then dividing by the total number of data points (N) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>:
    <div style="text-align: center;">σ² = Σ(xᵢ - μ)² / N</div>

*   **Sample Variance (s²)**:
    The sample [[variance_and_its_calculation_for_population_and_sample | variance]] (s²) is an unbiased estimator for the population [[variance_and_its_calculation_for_population_and_sample | variance]] <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. It is calculated by taking each data point in the sample (xᵢ), finding the difference between it and the sample [[Mean or Central Tendency in Statistics | mean]] (x̄), squaring that difference, summing all these squared differences, and then dividing by (n - 1) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The use of (n - 1) in the denominator provides an unbiased estimate, especially when the population [[Mean or Central Tendency in Statistics | mean]] is unknown and estimated by the sample [[Mean or Central Tendency in Statistics | mean]] <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    <div style="text-align: center;">s² = Σ(xᵢ - x̄)² / (n - 1)</div>

### Standard Deviation <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
The [[Standard deviation and sampling distribution | standard deviation]] is one of the most frequently used terms in statistics <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It is straightforward to calculate once the [[variance_and_its_calculation_for_population_and_sample | variance]] is known <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

*   **Relationship to Variance**:
    The [[Standard deviation and sampling distribution | standard deviation]] is simply the square root of the [[variance_and_its_calculation_for_population_and_sample | variance]] <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This is why [[variance_and_its_calculation_for_population_and_sample | variance]] is often denoted as sigma squared (σ²) <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

*   **Population Standard Deviation (σ)**:
    The [[Standard deviation and sampling distribution | standard deviation]] of a population (sigma, σ) is the square root of the population [[variance_and_its_calculation_for_population_and_sample | variance]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:
    <div style="text-align: center;">σ = √[Σ(xᵢ - μ)² / N]</div>

*   **Sample Standard Deviation (s)**:
    The [[Standard deviation and sampling distribution | standard deviation]] of a sample (s) is the square root of the sample [[variance_and_its_calculation_for_population_and_sample | variance]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>:
    <div style="text-align: center;">s = √[Σ(xᵢ - x̄)² / (n - 1)]</div>
    While the sample [[variance_and_its_calculation_for_population_and_sample | variance]] is an unbiased estimator for the population [[variance_and_its_calculation_for_population_and_sample | variance]], the sample [[Standard deviation and sampling distribution | standard deviation]] (s) is not an unbiased estimator for the population [[Standard deviation and sampling distribution | standard deviation]] (σ) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. However, it still serves as a very good estimate <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

*   **Why use Standard Deviation?**
    One key advantage of [[Standard deviation and sampling distribution | standard deviation]] is that its units are the same as the original data points <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. For example, if data points are in meters, [[variance_and_its_calculation_for_population_and_sample | variance]] would be in meter squared, which is a strange concept for dispersion. Taking the square root brings the units back to meters, making it more intuitive <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Additionally, for data that can be modeled as a bell curve (normal distribution), [[Standard deviation and sampling distribution | standard deviation]] provides insights into the probability of finding data points within a certain range from the [[Mean or Central Tendency in Statistics | mean]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Example Calculation: Population Data <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
Let's calculate the [[Mean or Central Tendency in Statistics | mean]], [[variance_and_its_calculation_for_population_and_sample | variance]], and [[Standard deviation and sampling distribution | standard deviation]] for a given population data set: **1, 2, 3, 8, 7** <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

1.  **Calculate the Population Mean (μ)**:
    Sum the data points: 1 + 2 + 3 + 8 + 7 = 21 <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    There are 5 data points (N=5) <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
    μ = 21 / 5 = 4.20 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

2.  **Calculate the Population Variance (σ²)**:
    Find the squared difference of each data point from the mean (4.20):
    *   (1 - 4.20)² = (-3.20)² = 10.24 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
    *   (2 - 4.20)² = (-2.20)² = 4.84 <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>
    *   (3 - 4.20)² = (-1.20)² = 1.44 <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>
    *   (8 - 4.20)² = (3.80)² = 14.44 <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>
    *   (7 - 4.20)² = (2.80)² = 7.84 <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

    Sum these squared differences: 10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80 <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
    Divide the sum by N (5):
    σ² = 38.80 / 5 = 7.76 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

3.  **Calculate the Population Standard Deviation (σ)**:
    Take the square root of the population [[variance_and_its_calculation_for_population_and_sample | variance]]:
    σ = √7.76 ≈ 2.7856, which rounds to 2.79 <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

*   **Note on Sample Calculation**:
    If the given numbers (1, 2, 3, 8, 7) were considered a sample instead of an entire population, the sample [[variance_and_its_calculation_for_population_and_sample | variance]] (s²) would be calculated by dividing the sum of squared differences (38.80) by (n - 1), which is (5 - 1 = 4) <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
    s² = 38.80 / 4 = 9.70 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    The sample [[Standard deviation and sampling distribution | standard deviation]] (s) would then be the square root of 9.70, which is approximately 3.11 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

These calculations demonstrate how [[Mean or Central Tendency in Statistics | mean]], [[variance_and_its_calculation_for_population_and_sample | variance]], and [[Standard deviation and sampling distribution | standard deviation]] provide measures of [[measures_of_dispersion | central tendency]] and dispersion within a dataset <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.