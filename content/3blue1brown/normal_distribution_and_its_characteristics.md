---
title: Normal distribution and its characteristics
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 
The **normal distribution**, also colloquially known as a **bell curve** or a [[Gaussian distribution and the role of pi | Gaussian distribution]], is one of the most prominent distributions in all of probability <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It is notably common and appears in many seemingly unrelated contexts <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Visualizing the Normal Distribution: The Galton Board

A **Galton board** is a popular demonstration that illustrates how, even with chaotic and random individual events, precise statements can be made about a large number of events, specifically how the relative proportions of different outcomes are distributed <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It specifically illustrates the normal distribution <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

A simplified model of the Galton board involves a ball falling onto a central peg with a 50-50 probability of bouncing left or right <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Each bounce can be thought of as adding one or subtracting one from its position <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. If there are five rows of pegs, the ball makes five random choices, and its final position is the sum of these numbers <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. If many balls fall, the number of balls in each bucket loosely indicates its likelihood <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

The fundamental idea is that as the "size of that sum" increases (e.g., more rows of pegs), the distribution describing where the sum will fall looks more and more like a bell curve <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Ubiquity of the Normal Distribution

The normal distribution is remarkably common <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Examples include:
*   **Human Heights**: Heights of a large group of people from a similar demographic tend to follow a normal distribution <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Prime Factors**: The number of distinct prime factors for a large swath of very big natural numbers closely tracks a certain normal distribution <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### The [[central_limit_theorem | Central Limit Theorem]]

The [[central_limit_theorem | Central Limit Theorem]] (CLT) is a cornerstone of probability theory that explains why the normal distribution is so common <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
The general idea of the CLT is that if you take multiple different samples of a random variable and add them together, as the size of that sum gets bigger, the distribution of that sum will look more and more like a bell curve <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This holds true even if the initial distribution is skewed or non-uniform <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Characteristics: Mean and Standard Deviation

To quantitatively describe the normal distribution and the [[central_limit_theorem | Central Limit Theorem]], it's essential to understand its two key parameters: [[understanding_mean_and_standard_deviation_in_probability | mean]] and [[understanding_mean_and_standard_deviation_in_probability | standard deviation]] <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

*   **[[understanding_mean_and_standard_deviation_in_probability | Mean]] (μ)**: Often denoted by the Greek letter mu, the mean captures the center of mass for a distribution <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It's calculated as the expected value of a random variable, where the probability of each outcome is multiplied by its value, and these products are summed <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. For a sum of *n* random variables, the mean of the sum is *n* times the mean of the individual variable (nμ) <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

*   **[[understanding_mean_and_standard_deviation_in_probability | Variance]] and [[understanding_mean_and_standard_deviation_in_probability | Standard Deviation]] (σ)**: These measure how spread out a distribution is <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
    *   **[[understanding_mean_and_standard_deviation_in_probability | Variance]]**: Calculated by looking at the difference between each possible value and the mean, squaring that difference, and finding its expected value <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. For the sum of two independent random variables, the variance for the sum is the sum of their individual variances <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. For *n* independent and identically distributed (IID) variables, the variance of the sum is *n* times the variance of the original variable <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
    *   **[[understanding_mean_and_standard_deviation_in_probability | Standard Deviation]]**: Denoted by the Greek letter sigma, it is the square root of the variance <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. It can be more reasonably interpreted as a distance on a probability distribution diagram <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. For a sum of *n* IID variables, the standard deviation is the square root of *n* times the original standard deviation (σ√n) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This means distributions spread out in proportion to the square root of the sum's size <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### The Normal Distribution Formula (Probability Density Function)

The normal distribution is described by a specific function, which is a type of [[probability_density_function_pdf | probability density function (PDF)]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. For a continuous distribution, the [[probability_density_function_pdf | PDF]]'s curve tells you that the probability of a value falling between two points equals the area under the curve between those points <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. The area under the entire curve must be 1, representing 100% probability <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.

The formula for a normal distribution with mean μ and standard deviation σ is:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$ <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>

Breaking down its components:
*   **Exponential Decay**: The core shape comes from `e` to the negative `x` squared ($e^{-x^2}$) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. This creates a smooth curve that decays in both directions from a central peak <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. The choice of `e` is for mathematical readability, but any other positive constant would produce the same family of curves <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   **Scaling for Width (σ)**: The constant $\sigma$ in the exponent controls the horizontal stretch and squish of the graph, determining the narrowness or width of the bell curve <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. When configured as $\frac{(x-\mu)^2}{2\sigma^2}$, this $\sigma$ directly corresponds to the [[understanding_mean_and_standard_deviation_in_probability | standard deviation]] of the distribution <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   **Normalization Factor (1 / σ√2π)**: This constant ensures the area under the curve equals 1 <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. The presence of pi (π) is intriguing and relates to the nature of the function, which will be explored in subsequent discussions <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Shifting for Mean (μ)**: Subtracting $\mu$ from `x` in the exponent ($x-\mu$) allows the graph to slide left or right, thereby prescribing the mean of the distribution <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

### Standard Normal Distribution

The special case where the [[understanding_mean_and_standard_deviation_in_probability | mean]] ($\mu$) equals 0 and the [[understanding_mean_and_standard_deviation_in_probability | standard deviation]] ($\sigma$) equals 1 is called the **standard normal distribution** <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. This form is often used by aligning distributions so their means line up and then rescaling them so their standard deviations are equal to one <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. The [[central_limit_theorem | Central Limit Theorem]] states that as the sum size increases, the distribution of the standardized sum (mean 0, standard deviation 1) approaches this universal standard normal shape, regardless of the initial distribution <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### The 68-95-99.7 Rule

For normal distributions, there's a practical rule of thumb:
*   Approximately **68%** of values fall within one [[understanding_mean_and_standard_deviation_in_probability | standard deviation]] ($\sigma$) of the [[understanding_mean_and_standard_deviation_in_probability | mean]] ($\mu$) <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   Approximately **95%** of values fall within two [[understanding_mean_and_standard_deviation_in_probability | standard deviations]] of the [[understanding_mean_and_standard_deviation_in_probability | mean]] <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.
*   Approximately **99.7%** of values fall within three [[understanding_mean_and_standard_deviation_in_probability | standard deviations]] of the [[understanding_mean_and_standard_deviation_in_probability | mean]] <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.

### Assumptions for Normality (Central Limit Theorem)

While the bell curve appears often, the [[central_limit_theorem | Central Limit Theorem]] relies on specific assumptions for its strict mathematical statement:
1.  **Independence**: The variables being added up must be independent of each other, meaning the outcome of one process does not influence others <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
2.  **Identically Distributed**: All variables must be drawn from the same distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. These first two are often summarized as **IID** (independent and identically distributed) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.
3.  **Finite Variance**: The variance computed for these variables must be finite <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. This is usually not an issue for discrete outcomes but can be for distributions with infinite sets of outcomes where the sum for variance might diverge <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

Violations of these assumptions (like in a real Galton board where bounces are not independent) can still sometimes result in a normal-like distribution, possibly due to generalizations of the theorem or other factors <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. However, it's crucial to be cautious about assuming a variable is normally distributed without justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.