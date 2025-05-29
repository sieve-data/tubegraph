---
title: RealLife Calculations and Examples of Statistical Measures
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

This article reviews fundamental statistical concepts and demonstrates their calculation using real numbers <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The goal is to integrate learned concepts and apply them practically <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Key Statistical Concepts

Statistical concepts are often categorized based on whether they pertain to a [[introduction_to_statistics | population]] or a [[introduction_to_statistics | sample]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Mean (Central Tendency)

The mean is a measure of the average or central tendency of a data set <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Other measures of central tendency include the median and the mode, but the mean is more frequently used, especially when discussing variance and standard deviation <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

#### Population Mean (μ)
For a [[introduction_to_statistics | population]], the mean (μ, the Greek letter mu) is calculated by summing each data point (`xi`) in the [[introduction_to_statistics | population]] from the first (`i=1`) to the Nth data point, and then dividing by the total number of data points (N) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:

```
μ = (Σ xi) / N
```
This is the familiar average calculation: [[addition_with_real_life_examples | add up all the data points]] and divide by their count <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

#### Sample Mean (x̄)
For a [[introduction_to_statistics | sample]], the mean (x̄, read as "x-bar") is calculated similarly but uses lowercase 'n' to denote the number of data points in the [[introduction_to_statistics | sample]], implying `n` is less than `N` <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>:

```
x̄ = (Σ xi) / n
```
If the sample size (`n`) were equal to the population size (`N`), it would simply be the mean of the entire [[introduction_to_statistics | population]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Variance

Variance measures how spread out the data points are from the mean <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It quantifies the average of the squared distances from the mean <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

#### Population Variance (σ²)
For a [[introduction_to_statistics | population]], the variance (σ², sigma squared) is calculated by taking each data point (`xi`), subtracting the population mean (μ), squaring the result, summing all these squared differences, and then dividing by the total number of data points (N) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:

```
σ² = Σ(xi - μ)² / N
```

#### Sample Variance (s²)
For a [[introduction_to_statistics | sample]], the sample variance (s², also known as unbiased sample variance) is used to estimate the variance of the underlying [[introduction_to_statistics | population]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. To provide an unbiased estimate, the sum of squared differences is divided by `n - 1` instead of `n` <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This adjustment accounts for using the sample mean (x̄) as an estimate for the unknown population mean (μ) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>:

```
s² = Σ(xi - x̄)² / (n - 1)
```
The reason for dividing by `n-1` for an unbiased estimator can be formally proven <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Standard Deviation

The standard deviation is one of the most commonly used terms in [[introduction_to_statistics | statistics]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It is simply the square root of the variance <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

#### Population Standard Deviation (σ)
For a [[introduction_to_statistics | population]], the standard deviation (σ, sigma) is the square root of the population variance <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:

```
σ = √σ² = √(Σ(xi - μ)² / N)
```
The units of standard deviation are the same as the original measurements, making it easier to interpret than variance (e.g., if measurements are in meters, variance is in meters squared, but standard deviation is in meters) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. If data can be modeled as a [[application_of_central_limit_theorem_in_real_life | bell curve]] (normal distribution), standard deviation provides insights into the [[probability_calculation | probability]] of finding data points within certain ranges of the mean <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

#### Sample Standard Deviation (s)
For a [[introduction_to_statistics | sample]], the sample standard deviation (s) is the square root of the sample variance <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>:

```
s = √s² = √(Σ(xi - x̄)² / (n - 1))
```
While `s²` is an unbiased estimator for `σ²`, `s` itself is not an unbiased estimator for `σ`, though it serves as a very good estimate <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Real-Life Calculation Example

Let's calculate the mean, variance, and standard deviation for the data set: `1, 2, 3, 8, 7` <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### 1. Assuming the Data is a Population (N=5)

#### Calculate Mean (μ)
Sum the data points: `1 + 2 + 3 + 8 + 7 = 21` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
Divide by the number of data points (N=5):
`μ = 21 / 5 = 4.20` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

#### Calculate Variance (σ²)
1.  Subtract the mean (4.20) from each data point and square the result:
    *   `(1 - 4.20)² = (-3.20)² = 10.24`
    *   `(2 - 4.20)² = (-2.20)² = 4.84`
    *   `(3 - 4.20)² = (-1.20)² = 1.44`
    *   `(8 - 4.20)² = (3.80)² = 14.44`
    *   `(7 - 4.20)² = (2.80)² = 7.84` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>
2.  Sum these squared differences:
    `10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
3.  Divide the sum by N (5):
    `σ² = 38.80 / 5 = 7.76` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

#### Calculate Standard Deviation (σ)
Take the square root of the variance:
`σ = √7.76 ≈ 2.79` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
This value gives a measure of how far, on average, the numbers are from the mean of 4.20 <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

### 2. Briefly, Assuming the Data is a Sample (n=5)

If this data set (`1, 2, 3, 8, 7`) were considered a [[introduction_to_statistics | sample]] from a larger distribution <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>:

#### Calculate Sample Variance (s²)
Instead of dividing the sum of squared differences (38.80) by `n` (5), divide by `n - 1` (4):
`s² = 38.80 / 4 = 9.70` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

#### Calculate Sample Standard Deviation (s)
Take the square root of the sample variance:
`s = √9.70 ≈ 3.11` <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

These calculations demonstrate that while the formulas use sigma notation and variables, applying them with actual numbers makes the process more concrete and understandable <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.