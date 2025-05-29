---
title: population versus sample in statistics
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

This article reviews key statistical concepts, differentiating between their application to a **population** versus a **sample**. The goal is to clarify how calculations for central tendency and dispersion vary depending on whether the entire set of data or a subset is being analyzed <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Concepts and Terminology

In [[introduction_to_statistics|statistics]], data can either represent an entire group (population) or a smaller, representative portion of that group (sample) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

| Concept | Population | Sample |
| :---------------- | :----------------------------- | :---------------------------------- |
| **Data Set Size** | Denoted by `N` | Denoted by `n` (where `n < N`) |

## Mean (Central Tendency)

The mean is a measure of [[introduction_to_statistics|central tendency]], indicating the average of a dataset <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Other measures of central tendency include the median and the mode, but the mean is frequently used, especially when dealing with variance and standard deviation <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Population Mean
The mean of a population is denoted by the Greek letter mu (μ) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It is calculated by summing all data points in the population and dividing by the total number of data points <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:

> μ = (Σxi) / N <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
> Where:
> *   `Σxi` is the sum of each data point `xi` from `i=1` to `N` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
> *   `N` is the total number of data points in the population <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

### Sample Mean
The mean of a sample is denoted as x-bar (x̄) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. It is calculated similarly to the population mean, by summing all data points in the sample and dividing by the sample size <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>:

> x̄ = (Σxi) / n <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
> Where:
> *   `Σxi` is the sum of each data point `xi` from `i=1` to `n` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
> *   `n` is the total number of data points in the sample <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

## Variance

Variance measures the average dispersion of data points from the mean <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It quantifies how far, on average, data points are from the mean <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Population Variance
The variance of a population is denoted by sigma squared (σ²) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. It is the average of the squared differences between each data point and the population mean <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>:

> σ² = Σ(xi - μ)² / N <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
> Where:
> *   `Σ(xi - μ)²` is the sum of the squared differences between each data point `xi` and the population mean `μ` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
> *   `N` is the total number of data points in the population <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

### Sample Variance
The variance of a sample is denoted by s-squared (s²) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. When calculating sample variance, the goal is often to provide an [[unbiased_estimators_in_statistics|unbiased estimate]] of the population variance <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. To achieve this, the sum of squared differences is divided by `n-1` instead of `n` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>:

> s² = Σ(xi - x̄)² / (n - 1) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>
> Where:
> *   `Σ(xi - x̄)²` is the sum of the squared differences between each data point `xi` and the sample mean `x̄` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
> *   `n - 1` is used as the denominator to ensure an [[unbiased_estimators_in_statistics|unbiased estimator]] for the population variance <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

## Standard Deviation

Standard deviation is arguably one of the most used terms in statistics <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It is the square root of the variance <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Standard deviation is often preferred over variance because its units are the same as the original data points, making it easier to interpret the spread <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. For example, if measurements are in meters, variance would be in meters squared, while standard deviation would be in meters <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Population Standard Deviation
The standard deviation of a population is denoted by sigma (σ) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>:

> σ = √σ² = √(Σ(xi - μ)² / N) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>

### Sample Standard Deviation
The standard deviation of a sample is denoted by s <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>:

> s = √s² = √(Σ(xi - x̄)² / (n - 1)) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

It's noted that while `s²` is an [[unbiased_estimators_in_statistics|unbiased estimator]] for `σ²`, `s` is not quite an unbiased estimator for `σ`, though it is a very good estimate <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Example Calculation

Consider the dataset: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Scenario 1: Data as a Population
If this dataset is considered the entire population (`N=5`):

1.  **Mean (μ):**
    *   Sum = 1 + 2 + 3 + 8 + 7 = 21 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   μ = 21 / 5 = 4.20 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

2.  **Variance (σ²):**
    *   Sum of squared differences (Σ(xi - μ)²):
        *   (1 - 4.20)² = (-3.2)² = 10.24
        *   (2 - 4.20)² = (-2.2)² = 4.84
        *   (3 - 4.20)² = (-1.2)² = 1.44
        *   (8 - 4.20)² = (3.8)² = 14.44
        *   (7 - 4.20)² = (2.8)² = 7.84
    *   Total sum of squared differences = 10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80 <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>
    *   σ² = 38.80 / 5 = 7.76 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

3.  **Standard Deviation (σ):**
    *   σ = √7.76 ≈ 2.78 <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>

### Scenario 2: Data as a Sample
If this dataset is considered a sample from a larger population (`n=5`):

1.  **Mean (x̄):**
    *   The sample mean remains the same as the population mean in this specific calculation: x̄ = 4.20 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

2.  **Variance (s²):**
    *   The sum of squared differences (Σ(xi - x̄)²) is still 38.80 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   However, for a sample, the sum is divided by `n-1` (5-1=4) for an [[unbiased_estimators_in_statistics|unbiased estimate]] <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
    *   s² = 38.80 / 4 = 9.70 <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

3.  **Standard Deviation (s):**
    *   s = √9.70 ≈ 3.11 <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>

This example illustrates how the denominator changes for variance and standard deviation calculations when dealing with a sample versus a population, specifically to provide an unbiased estimate of the population variance from sample data <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.