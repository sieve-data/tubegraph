---
title: Standard deviation and its significance
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

[[standard_deviation_explained | Standard deviation]] is one of the most frequently used terms in statistics <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. It serves as a crucial [[measures_of_dispersion | measure of dispersion]] for a dataset <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Relationship to Mean and Variance

Before delving into [[standard_deviation_explained | standard deviation]], it's helpful to review related concepts:

*   **[[mean_in_statistics | Mean]]**: This is a measure of central tendency, often referred to as the average <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. For a population, the [[mean_in_statistics | mean]] (mu, μ) is the sum of all data points (xᵢ) divided by the total number of data points (N) <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. For a sample, the [[mean_in_statistics | mean]] (x-bar, x̄) is the sum of data points (xᵢ) divided by the sample size (n) <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   **[[variance_and_its_calculation | Variance]]**: This concept helps determine how spread out data points are from the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. It's calculated by taking the average of all the squared differences between each data point and the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## Defining Standard Deviation

[[standard_deviation_explained | Standard deviation]] is defined as the square root of the [[variance_and_its_calculation | variance]] <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.

### Notation and Formula

The notation for [[standard_deviation_explained | standard deviation]] varies depending on whether you are working with a population or a sample:

*   **Population Standard Deviation (σ)**:
    σ = √σ² <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>
    This means σ = √[Σ(xᵢ - μ)² / N] <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>

*   **Sample Standard Deviation (s)**:
    s = √s² <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>
    This means s = √[Σ(xᵢ - x̄)² / (n - 1)] <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

    *   **Unbiased Estimator**: When calculating the [[variance_and_its_calculation | variance]] for a sample to estimate the population [[variance_and_its_calculation | variance]], you divide by `n - 1` instead of `n` to provide an unbiased estimate <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. This is because the sample [[mean_in_statistics | mean]] is used to estimate the population [[mean_in_statistics | mean]], introducing a slight bias that `n-1` corrects <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. While the sample [[variance_and_its_calculation | variance]] (s²) is an unbiased estimator for population [[variance_and_its_calculation | variance]] (σ²), the sample [[standard_deviation_explained | standard deviation]] (s) is not an unbiased estimator for population [[standard_deviation_explained | standard deviation]] (σ) <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

## Significance of Standard Deviation

The [[standard_deviation_explained | standard deviation]] is preferred over [[variance_and_its_calculation | variance]] for several reasons:

*   **Units Compatibility**: If data points are measured in meters, the [[variance_and_its_calculation | variance]] will be in "meters squared," which can be a strange concept for [[measures_of_dispersion | dispersion]] <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Taking the square root to get the [[standard_deviation_explained | standard deviation]] returns the units to the original measurement (meters), making it more intuitive to interpret how far numbers are from the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
*   **Probability Interpretation**: If a dataset can be modeled as a bell curve (normal distribution), [[standard_deviation_explained | standard deviation]] provides insights into the probability of finding data points within certain ranges of the [[mean_in_statistics | mean]] <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This relates to [[calculating_standard_deviation_and_probability | calculating standard deviation and probability]].

## Example Calculation

Let's calculate the [[standard_deviation_explained | standard deviation]] for the population dataset: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

1.  **Calculate the [[mean_in_statistics | Mean]] (μ)**:
    Sum of data points = 1 + 2 + 3 + 8 + 7 = 21 <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>
    Number of data points (N) = 5 <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>
    μ = 21 / 5 = 4.20 <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>

2.  **Calculate the [[variance_and_its_calculation | Variance]] (σ²)**:
    The formula is σ² = Σ(xᵢ - μ)² / N <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
    *   (1 - 4.20)² = (-3.20)² = 10.24
    *   (2 - 4.20)² = (-2.20)² = 4.84
    *   (3 - 4.20)² = (-1.20)² = 1.44
    *   (8 - 4.20)² = (3.80)² = 14.44
    *   (7 - 4.20)² = (2.80)² = 7.84

    Sum of squared differences = 10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80 <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>
    σ² = 38.80 / 5 = 7.76 <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>

3.  **Calculate the [[standard_deviation_explained | Standard Deviation]] (σ)**:
    σ = √7.76 ≈ 2.79 <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>

### Sample Standard Deviation Example

If the numbers 1, 2, 3, 8, and 7 were considered a sample of a larger population, the sample [[variance_and_its_calculation | variance]] would be calculated by dividing the sum of squared differences by `n - 1` <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

*   Sample [[variance_and_its_calculation | variance]] (s²) = 38.80 / (5 - 1) = 38.80 / 4 = 9.70 <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>
*   Sample [[standard_deviation_explained | standard deviation]] (s) = √9.70 ≈ 3.11 <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>

These calculations demonstrate how [[standard_deviation_explained | standard deviation]] provides a concrete measure of how dispersed the data points are around the [[mean_in_statistics | mean]] in the original units of measurement <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.