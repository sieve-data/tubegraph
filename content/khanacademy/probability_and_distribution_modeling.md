---
title: Probability and distribution modeling
videoId: HvDqbzu0i0E
---

From: [[khanacademy]] <br/> 

This article reviews fundamental statistical concepts and their application to both populations and samples, which are essential for understanding [[probability_distribution_functions | probability distribution functions]] and general [[probability_terminology_explained | probability terminology explained]] in data analysis <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Population vs. Sample

A key distinction in statistics is whether one is dealing with an entire **population** or a **sample** drawn from that population <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Central Tendency: The Mean

The mean is a measure of [[basic_concepts_in_probability_and_statistics | central tendency]], indicating the average of a data set <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Other measures include the median and the mode <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The mean is frequently used, especially when discussing variance and standard deviation <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Mean of a Population
The mean of a population, denoted by the Greek letter mu ($\mu$), is calculated by summing all data points ($x_i$) in the population and dividing by the total number of data points ($N$) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:

$\mu = \frac{\sum_{i=1}^{N} x_i}{N}$ <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

This is the standard average calculation: sum all points and divide by their count <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Mean of a Sample
The mean of a sample, denoted by x-bar ($\bar{x}$), is calculated similarly to the population mean <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It sums all data points ($x_i$) in the sample and divides by the total number of data points in the sample ($n$) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
It's assumed that the sample size ($n$) is typically less than the population size ($N$) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$ <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>

## Dispersion: Variance

Variance measures how spread out data points are from the mean <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. It is calculated as the average of the squared differences from the mean <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Variance of a Population
The variance of a population, denoted by sigma squared ($\sigma^2$), is calculated as the sum of the squared differences between each data point ($x_i$) and the population mean ($\mu$), divided by the total number of data points ($N$) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>:

$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$ <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>

### Variance of a Sample
The variance of a sample, often referred to as the unbiased sample variance and denoted by $s^2$, uses a slightly different denominator to provide an unbiased estimate of the population variance <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. The sum of the squared differences between each data point ($x_i$) and the sample mean ($\bar{x}$) is divided by ($n - 1$) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>:

$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}$ <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

The use of ($n-1$) is particularly important when estimating the population variance from a sample because the population mean is typically unknown and is estimated using the sample mean <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Dispersion: Standard Deviation

Standard deviation is arguably one of the most frequently used terms in statistics <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It is the square root of the variance <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, making it straightforward to calculate once the variance is known <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Standard Deviation of a Population
The standard deviation of a population, denoted by sigma ($\sigma$), is the square root of the population variance <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:

$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}$ <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>

### Standard Deviation of a Sample
The standard deviation of a sample, denoted by $s$, is the square root of the sample variance <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>:

$s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}$ <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>

While the sample variance ($s^2$) is an unbiased estimator for the population variance ($\sigma^2$), the sample standard deviation ($s$) is not necessarily an unbiased estimator for the population standard deviation ($\sigma$) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. However, it still serves as a very good estimate <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### Practicality of Standard Deviation
One advantage of standard deviation over variance is that its units are the same as the original data points <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. For example, if data is measured in meters, variance is in meters squared, whereas standard deviation is in meters <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This makes it easier to interpret the "average dispersion from the center" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

If data can be modeled as a "bell curve" (a common [[probability_distribution_functions | probability distribution function]]), standard deviation helps determine the [[area_under_probability_curves | probability]] of finding data points within specific ranges, such as one or two standard deviations from the mean <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Example Calculation

Consider a population with data points: 1, 2, 3, 8, 7 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Mean Calculation
Sum: $1 + 2 + 3 + 8 + 7 = 21$ <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>
Number of data points ($N$): 5 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>
Population Mean ($\mu$): $21 / 5 = 4.20$ <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

### Variance Calculation
Squared differences from the mean (4.20):
$(1 - 4.20)^2 = (-3.2)^2 = 10.24$
$(2 - 4.20)^2 = (-2.2)^2 = 4.84$
$(3 - 4.20)^2 = (-1.2)^2 = 1.44$
$(8 - 4.20)^2 = (3.8)^2 = 14.44$
$(7 - 4.20)^2 = (2.8)^2 = 7.84$ <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>

Sum of squared differences: $10.24 + 4.84 + 1.44 + 14.44 + 7.84 = 38.80$ <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
Population Variance ($\sigma^2$): $38.80 / 5 = 7.76$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

### Standard Deviation Calculation
Population Standard Deviation ($\sigma$): $\sqrt{7.76} \approx 2.79$ <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>, <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

If these numbers were a sample instead of a population, the sample variance would be $38.80 / (5-1) = 38.80 / 4 = 9.70$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. The sample standard deviation would then be $\sqrt{9.70} \approx 3.11$ <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.