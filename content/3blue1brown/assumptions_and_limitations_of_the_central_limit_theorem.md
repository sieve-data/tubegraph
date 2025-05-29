---
title: Assumptions and limitations of the Central Limit Theorem
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

The [[central_limit_theorem_fundamentals | Central Limit Theorem]] (CLT) is a cornerstone of probability theory, explaining why the [[normal_distribution_and_its_properties | normal distribution]] (also known as the bell curve or [[herschel_maxwells_derivation_and_its_impact_on_understanding_gaussian_distribution | Gaussian distribution]]) appears so frequently in various contexts <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While powerful, the theorem relies on specific assumptions that are crucial for its applicability <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## Core Idea of the Central Limit Theorem

The [[central_limit_theorem_fundamentals | Central Limit Theorem]] states that if you take a large number of independent samples from *any* random variable and sum them together, the distribution of that sum will increasingly resemble a [[normal_distribution_and_its_properties | bell curve]] <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This holds true regardless of the initial distribution of the individual random variable <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. The more variables included in the sum, the more pronounced this bell curve shape becomes <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Quantitatively, if we consider a sum of `n` different instances of a random variable, let `mu` be the mean and `sigma` be the standard deviation of the underlying random variable <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   The mean of the sum will be `n * mu` <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   The standard deviation of the sum will be `sqrt(n) * sigma` <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

When these sums are rescaled so their mean is zero and standard deviation is one, they approach a universal shape described by the standard [[normal_distribution_and_its_properties | normal distribution]] function: `1 / (sigma * sqrt(2 * pi)) * e^(-(x - mu)^2 / (2 * sigma^2))` <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>, <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. The formal statement of the theorem involves the limit of probabilities of values falling within a range, matching the area under the standard normal distribution function <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.

## Assumptions of the Central Limit Theorem

There are three key assumptions that must be true for the [[central_limit_theorem_fundamentals | Central Limit Theorem]] to apply <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>:

1.  ### Independence of Variables
    The random variables being summed must be independent of each other <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. This means the outcome of one process does not influence the outcome of any other process <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
    *   **Example:** In a dice rolling scenario, each roll is considered independent of the others <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

2.  ### Identically Distributed Variables
    All the random variables must be drawn from the same probability distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. This implies that each variable has the same mean and standard deviation <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
    *   **Literature Term:** These first two assumptions are often grouped under the acronym **IID** (Independent and Identically Distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.

3.  ### Finite Variance
    The variance of the underlying distribution from which the variables are drawn must be finite <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. This is typically not an issue for distributions with a finite number of outcomes, like a die roll <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. However, for certain situations with an infinite set of outcomes, the calculated variance might diverge to infinity <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

## Limitations and Violations

Understanding these assumptions is crucial because violating them can lead to situations where the [[normal_distribution_and_its_properties | normal distribution]] does not emerge for sums of variables.

### The Galton Board Example
The Galton board, a popular demonstration of the [[normal_distribution_and_its_properties | normal distribution]], actually violates two of the CLT's assumptions in its physical operation <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.
*   **Lack of Independence:** The way a ball bounces off one peg influences how it bounces off the next, due to changing trajectories <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.
*   **Not Identically Distributed:** The distribution of outcomes (left/right bounce probability) might not be the same for each peg, as the ball might hit pegs at different angles <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

Despite these violations, a bell curve often appears in real Galton boards <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. This might be due to generalizations of the theorem that relax these assumptions, or simply that the idealization provides a good approximation for certain physical phenomena <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>.

### Practical Implications
It is important to exercise caution and avoid assuming a variable is normally distributed without proper justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>. If the assumptions of the CLT are not met, the distribution of sums or averages may not converge to a [[normal_distribution_and_its_properties | normal distribution]] <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. In particular, if the variance is infinite, the sum might not tend towards a normal distribution even if the other two assumptions hold <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>.