---
title: Application of integrals in real world problems
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

One common application of [[derivatives_and_integrals | integration]] is finding the average of a continuous variable <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This concept also offers a different perspective on why [[relationship_between_integrals_and_derivatives | integrals and derivatives are inverses of each other]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Finding the Average of a Continuous Variable

Consider the average height of a graph, such as `sin(x)` between 0 and π <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is relevant because many cyclic phenomena, like the number of hours the sun is up per day, are modeled using sine waves <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For instance, to predict the average effectiveness of solar panels during summer versus winter months, one would need to find the average value of a sine function over a specific period <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

Calculating the average of a continuous variable poses a unique challenge because there are infinitely many values <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Unlike with a finite number of variables where one can sum them up and divide by the count, this approach doesn't work with an infinite continuum <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

When faced with the vague sense of wanting to sum infinitely many values associated with a continuum, the key is almost always to use an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. A good first step is to approximate the situation with a finite sum <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For example, sampling a finite number of evenly spaced points allows for a traditional average calculation. As more points are sampled, the average of that sample approaches the actual average of the continuous variable <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## The Average Value Formula

The average value of a continuous function `f(x)` on an interval `[a, b]` is calculated by taking the integral of `f(x)` over that interval and dividing it by the width of the interval `(b - a)` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

$$ \text{Average Value} = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx $$
This can be intuitively understood as the area under the graph divided by its width, which results in an average height <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. When approximating with finite samples, the sum of `f(x)` values multiplied by `dx` (the spacing between samples) is divided by the total width of the interval. As `dx` approaches 0, this sum becomes the integral, representing the true average <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

### Example: Average Height of `sin(x)`

To find the average height of `sin(x)` between 0 and π:
1.  Find an [[antiderivatives_and_solving_integrals | antiderivative]] of `sin(x)`. The [[antiderivatives_and_solving_integrals | antiderivative]] of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  [[evaluating_integrals_and_the_role_of_the_convergence_point | Evaluate the integral]] of `sin(x)` from 0 to π:
    `[-cos(π)] - [-cos(0)]` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
    `[-(-1)] - [-(1)] = 1 - (-1) = 2` <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>
    The area under the sine graph from 0 to π is 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  Divide the integral result by the width of the interval (π - 0 = π):
    `Average Height = 2 / π` ≈ 0.64 <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Connection to [[relationship_between_integrals_and_derivatives | Antiderivatives and Derivatives]]

Finding the average value of a function also highlights the [[relationship_between_integrals_and_derivatives | inverse relationship between integrals and derivatives]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. The calculated average value is the change in the [[integration_and_antiderivatives | antiderivative]] over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This fraction represents the "rise over run" slope of the [[integration_and_antiderivatives | antiderivative]] graph between the start and end points <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since `f(x)` is the derivative of its [[integration_and_antiderivatives | antiderivative]] `F(x)`, `f(x)` gives the slope of `F(x)` at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Therefore, the average value of `f(x)` can be viewed as the average slope over all tangent lines within the interval <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It makes intuitive sense that the average slope of a graph over a certain range should equal the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Recognizing Problems Solved by Integrals

Two key "sensations" should bring integrals to mind:
1.  If a problem can be approximated by breaking it up and adding a large number of small things <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
2.  If an idea understood in a finite context, involving summing multiple values (like taking an average), needs to be generalized to an infinite continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This sensation arises frequently, especially in [[applications_of_probability_density_function | probability]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.