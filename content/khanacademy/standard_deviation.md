---
title: standard deviation
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

The [[standard_deviation | Standard Deviation]] is a widely used statistical measure, often considered one of the most important concepts in statistics <a class="yt-timestamp" data-t="04:53">[04:53]</a>. It quantifies the average dispersion or spread of data points around the [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="02:21">[02:21]</a>.

## Relationship to Variance

The [[standard_deviation | standard deviation]] is derived directly from the [[variance | variance]] <a class="yt-timestamp" data-t="05:23">[05:23]</a>. It is defined as the [[square_root_symbol_and_terminology | square root]] of the [[variance | variance]] <a class="yt-timestamp" data-t="05:23">[05:23]</a>.

### Population Standard Deviation

For a population, the [[standard_deviation | standard deviation]] is denoted by the Greek letter sigma (σ) <a class="yt-timestamp" data-t="05:30">[05:30]</a>. It is calculated as the [[square_root_symbol_and_terminology | square root]] of the population [[variance | variance]] (σ²) <a class="yt-timestamp" data-t="05:30">[05:30]</a>:

> > [!MATH] Population Standard Deviation
> > $σ = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}$
> > Where:
> > *   $x_i$ represents each data point <a class="yt-timestamp" data-t="02:44">[02:44]</a>
> > *   μ is the [[mean_and_central_tendency | population mean]] <a class="yt-timestamp" data-t="02:50">[02:50]</a>
> > *   $N$ is the total number of data points in the population <a class="yt-timestamp" data-t="01:17">[01:17]</a>

### Sample Standard Deviation

For a sample, the [[standard_deviation | standard deviation]] is denoted by 's' <a class="yt-timestamp" data-t="06:03">[06:03]</a>. It is calculated as the [[square_root_symbol_and_terminology | square root]] of the sample [[variance | variance]] (s²) <a class="yt-timestamp" data-t="06:08">[06:08]</a>. When estimating population [[variance | variance]] from a sample, the denominator used for [[variance | variance]] is $n-1$ to provide an unbiased estimate <a class="yt-timestamp" data-t="03:25">[03:25]</a>:

> > [!MATH] Sample Standard Deviation
> > $s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$
> > Where:
> > *   $x_i$ represents each data point in the sample <a class="yt-timestamp" data-t="03:48">[03:48]</a>
> > *   $\bar{x}$ is the [[mean_and_central_tendency | sample mean]] <a class="yt-timestamp" data-t="03:48">[03:48]</a>
> > *   $n$ is the total number of data points in the sample <a class="yt-timestamp" data-t="01:57">[01:57]</a>

It's worth noting that while the sample [[variance | variance]] ($s^2$) is an unbiased estimator for the population [[variance | variance]], the sample [[standard_deviation | standard deviation]] (s) is not necessarily an unbiased estimator for the population [[standard_deviation | standard deviation]] (σ) <a class="yt-timestamp" data-t="06:09">[06:09]</a>.

## Why Standard Deviation?

The [[standard_deviation | standard deviation]] is particularly useful for two main reasons:

1.  **Units:** If the original data points are measured in a certain unit (e.g., meters), the [[variance | variance]] will be in that unit squared (e.g., meters squared) <a class="yt-timestamp" data-t="06:37">[06:37]</a>. Taking the [[square_root_symbol_and_terminology | square root]] to get the [[standard_deviation | standard deviation]] returns the units to the original measurement, making the measure of dispersion more intuitive (e.g., "the average dispersion from the center is x meters") <a class="yt-timestamp" data-t="06:57">[06:57]</a>.
2.  **Data Distribution:** When data can be modeled as a [[normal_distribution | bell curve]] or [[normal_distribution | normal distribution]], the [[standard_deviation | standard deviation]] provides insight into the probability of finding data points within specific ranges from the [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="07:08">[07:08]</a>.

## Calculation Example

Let's calculate the [[mean_and_central_tendency | mean]], [[variance | variance]], and [[standard_deviation | standard deviation]] for the following set of numbers, assuming they represent a **population**: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="07:28">[07:28]</a>.

### 1. Calculate the Mean (μ)

The [[mean_and_central_tendency | mean]] is the sum of all data points divided by the number of data points <a class="yt-timestamp" data-t="01:27">[01:27]</a>.
Sum = 1 + 2 + 3 + 8 + 7 = 21 <a class="yt-timestamp" data-t="07:51">[07:51]</a>
Number of data points ($N$) = 5 <a class="yt-timestamp" data-t="08:01">[08:01]</a>
μ = 21 / 5 = 4.20 <a class="yt-timestamp" data-t="08:01">[08:01]</a>

### 2. Calculate the Variance (σ²)

The [[variance | variance]] is the average of the squared differences from the [[mean_and_central_tendency | mean]] <a class="yt-timestamp" data-t="03:00">[03:00]</a>.
1.  (1 - 4.20)² = (-3.20)² = 10.24
2.  (2 - 4.20)² = (-2.20)² = 4.84
3.  (3 - 4.20)² = (-1.20)² = 1.44
4.  (8 - 4.20)² = (3.80)² = 14.44
5.  (7 - 4.20)² = (2.80)² = 7.84 <a class="yt-timestamp" data-t="08:22">[08:22]</a>

Sum of squared differences = 10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80 <a class="yt-timestamp" data-t="10:12">[10:12]</a>
σ² = 38.80 / 5 = 7.76 <a class="yt-timestamp" data-t="10:58">[10:58]</a>

### 3. Calculate the Standard Deviation (σ)

The [[standard_deviation | standard deviation]] is the [[square_root_symbol_and_terminology | square root]] of the [[variance | variance]] <a class="yt-timestamp" data-t="05:23">[05:23]</a>.
σ = $\sqrt{7.76}$ ≈ 2.79 <a class="yt-timestamp" data-t="11:59">[11:59]</a>

### Sample Variance and Standard Deviation (for comparison)

If the given numbers (1, 2, 3, 8, 7) were considered a **sample** from a larger population instead of the entire population <a class="yt-timestamp" data-t="11:19">[11:19]</a>:

*   **Sample Variance ($s^2$):** We would divide the sum of squared differences by $n-1$ (where $n=5$, so $n-1=4$) <a class="yt-timestamp" data-t="11:30">[11:30]</a>.
    $s^2$ = 38.80 / 4 = 9.70 <a class="yt-timestamp" data-t="11:45">[11:45]</a>
*   **Sample Standard Deviation (s):**
    $s$ = $\sqrt{9.70}$ ≈ 3.11 <a class="yt-timestamp" data-t="12:46">[12:46]</a>

These calculations help make the concepts of [[mean_and_central_tendency | mean]], [[concept_of_variance | variance]], and [[standard_deviation | standard deviation]] more concrete with real numbers <a class="yt-timestamp" data-t="12:53">[12:53]</a>.