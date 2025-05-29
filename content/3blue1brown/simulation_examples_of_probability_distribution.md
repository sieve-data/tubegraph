---
title: Simulation examples of probability distribution
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

[[Galton board and probability distribution | The Galton board]] is a well-known demonstration illustrating how, even when individual events are chaotic and random, it's possible to make precise statements about a large number of events. Specifically, it shows how the relative proportions for many different outcomes are [[Normal distribution and its properties | distributed]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This demonstration particularly highlights the [[Normal distribution and its properties | normal distribution]], also known as a bell curve or [[Connection between Gaussian distribution and probability | Gaussian distribution]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The [[Normal distribution and its properties | normal distribution]] is exceptionally common and appears in many seemingly unrelated contexts, such as the heights of people within a similar demographic or the number of distinct prime factors of large natural numbers <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.

Our primary focus is the central limit theorem, a key concept explaining why this distribution is so prevalent <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. This theorem states that as the number of random variables in a sum increases, the distribution of that sum will increasingly resemble a bell curve <a class="yt-timestamp" data-t="05:01:01">[05:01:01]</a>.

## Galton Board Simulation

A simplified model of the [[Galton board and probability distribution | Galton board]] can be used to illustrate the central limit theorem <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>. In this model:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   It has a 50-50 probability of bouncing left or right <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>.
*   Bouncing left is represented as subtracting one (-1) from its position, and bouncing right as adding one (+1) <a class="yt-timestamp" data-t="02:09:09">[02:09:09]</a>.
*   The ball lands in the middle of the peg adjacent below it, facing the same 50-50 choice <a class="yt-timestamp" data-t="02:14:14">[02:14:14]</a>.

For a board with five rows of pegs, the ball makes five independent random choices (plus one or minus one), and its final position is the sum of these five numbers <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>. The buckets at the bottom are labeled with the sum they represent <a class="yt-timestamp" data-t="02:42:42">[02:42:42]</a>.

When many balls are allowed to fall (assuming they don't influence each other), the number of balls in each bucket gives an indication of the likelihood of that outcome <a class="yt-timestamp" data-t="03:10:10">[03:10:10]</a>. While the probabilities for such a simple example could be explicitly calculated (reminiscent of Pascal's triangle), simulating a large number of samples allows us to observe the distribution directly <a class="yt-timestamp" data-t="03:23:23">[03:23:23]</a>. The basic idea of the central limit theorem is that as the "size of that sum" (e.g., increasing the number of rows of pegs) gets larger, the resulting [[Probability density and distribution | distribution]] looks more and more like a bell curve <a class="yt-timestamp" data-t="03:56:56">[03:56:56]</a>.

## Dice Roll Simulation

The central limit theorem can also be illustrated using the example of rolling dice <a class="yt-timestamp" data-t="04:38:38">[04:38:38]</a>.
A random variable is defined as a random process where each outcome is associated with a number, like rolling a die where outcomes are 1-6 <a class="yt-timestamp" data-t="04:20:20">[04:20:20]</a>. The process involves taking multiple samples of this variable and adding them together, such as rolling many dice and summing the results <a class="yt-timestamp" data-t="04:45:45">[04:45:45]</a>.

The power of the central limit theorem is highlighted by showing that even with a "weighted die" (a non-uniform [[Probability density and distribution | distribution]] of outcomes), the core idea holds <a class="yt-timestamp" data-t="06:20:20">[06:20:20]</a>.
A simulation demonstrates this:
1.  Start with a [[Probability density and distribution | distribution]] skewed towards lower values (e.g., a weighted die) <a class="yt-timestamp" data-t="06:35:35">[06:35:35]</a>.
2.  Take 10 distinct samples from this [[Probability density and distribution | distribution]] and record their sum <a class="yt-timestamp" data-t="06:40:40">[06:40:40]</a>.
3.  Repeat this process many times (e.g., thousands of samples), tracking the distribution of these sums <a class="yt-timestamp" data-t="06:48:48">[06:48:48]</a>.

As the simulation runs, a bell curve shape begins to emerge, even from the initially asymmetric starting point <a class="yt-timestamp" data-t="07:07:07">[07:07:07]</a>.

### Impact of Sample Size

Running parallel simulations with varying numbers of dice added together (e.g., 2, 5, 10, and 15 dice) demonstrates the effect of sample size <a class="yt-timestamp" data-t="07:21:21">[07:21:21]</a>:
*   With only two dice, the resulting [[Probability density and distribution | distribution]] still strongly resembles the initial skewed [[Probability density and distribution | distribution]] <a class="yt-timestamp" data-t="07:42:42">[07:42:42]</a>.
*   As more dice are added to each sum, the resulting shape becomes increasingly symmetric, exhibiting the characteristic lump in the middle and fade towards the tails of a bell curve <a class="yt-timestamp" data-t="07:52:52">[07:52:52]</a>.
*   This convergence to a bell curve occurs regardless of the starting [[Probability density and distribution | distribution]] for a single die roll. Even if most of the probability is concentrated at extreme values (e.g., 1 and 6), a bell curve shape will emerge from the sums <a class="yt-timestamp" data-t="08:07:07">[08:07:07]</a>.

While simulations are insightful and demonstrate the emergence of order from chaos <a class="yt-timestamp" data-t="08:30:30">[08:30:30]</a>, they can also be imprecise (e.g., spiky appearance due to randomness) <a class="yt-timestamp" data-t="08:35:35">[08:35:35]</a>. To understand the precise shape these distributions take, a more theoretical approach using [[Applications of Convolutions in Probability | convolutions]] is necessary <a class="yt-timestamp" data-t="09:02:02">[09:02:02]</a>. [[Applications of Convolutions in Probability | Convolutions]] allow for exact calculation of the [[Probability density and distribution | distribution]] of sums, even for non-uniform initial distributions <a class="yt-timestamp" data-t="09:51:51">[09:51:51]</a>.

## Mean and Standard Deviation in Simulations

As the number of elements in the sum increases, the resulting distributions demonstrate two key changes:
1.  **Wandering to the right**: The mean of the distribution shifts <a class="yt-timestamp" data-t="11:17:17">[11:17:17]</a>. If the mean of the initial random variable is $\mu$, the mean of a sum of $n$ such variables will be $n \times \mu$ <a class="yt-timestamp" data-t="13:39:39">[13:39:39]</a>.
2.  **Getting more spread out**: The [[Normal distribution and its properties | standard deviation]] of the distribution increases <a class="yt-timestamp" data-t="11:20:20">[11:20:20]</a>. The variance of the sum of independent random variables is the sum of their variances <a class="yt-timestamp" data-t="13:53:53">[13:53:53]</a>. If the standard deviation of the initial variable is $\sigma$, the standard deviation of a sum of $n$ identical independent variables will be $\sqrt{n} \times \sigma$ <a class="yt-timestamp" data-t="14:20:20">[14:20:20]</a>. This means the spread increases, but only in proportion to the square root of the sum's size <a class="yt-timestamp" data-t="14:56:56">[14:56:56]</a>.

To make a quantitative comparison, distributions are often "realigned" so their means line up (e.g., at zero) and "rescaled" so their standard deviations equal one <a class="yt-timestamp" data-t="15:08:08">[15:08:08]</a>. When this is done, regardless of the initial distribution, the shape approaches a universal form described by the [[Normal distribution and its properties | normal distribution]] function <a class="yt-timestamp" data-t="15:21:21">[15:21:21]</a>.

This transformation is formalized by looking at the expression:
$$ \frac{S_n - n\mu}{\sqrt{n}\sigma} $$
where $S_n$ is the sum of $n$ random variables, $\mu$ is the mean of a single variable, and $\sigma$ is its standard deviation <a class="yt-timestamp" data-t="21:02:02">[21:02:02]</a>. This expression effectively asks "how many standard deviations away from the mean is this sum?" and yields a distribution with a mean of zero and a standard deviation of one <a class="yt-timestamp" data-t="21:24:24">[21:24:24]</a>.

When many random variables are added (e.g., 50 different values), and this re-scaling is applied, the initial [[Probability density and distribution | distribution]]'s nuances are "washed away," and the sum's [[Probability density and distribution | distribution]] converges to the standard [[Normal distribution and its properties | normal distribution]] <a class="yt-timestamp" data-t="23:16:16">[23:16:16]</a>. This is the essence of the central limit theorem.

## Central Limit Theorem Assumptions

The central limit theorem relies on three main assumptions:
1.  **Independence**: All variables being added are independent of each other. The outcome of one process does not influence another <a class="yt-timestamp" data-t="28:18:18">[28:18:18]</a>.
2.  **Identically Distributed**: All variables are drawn from the same [[Probability density and distribution | distribution]] <a class="yt-timestamp" data-t="28:27:27">[28:27:27]</a>. These first two are often summarized as IID (Independent and Identically Distributed) <a class="yt-timestamp" data-t="28:42:42">[28:42:42]</a>.
3.  **Finite Variance**: The variance of the variables must be finite <a class="yt-timestamp" data-t="30:06:06">[30:06:06]</a>. This is always true for discrete distributions with a finite number of outcomes (like dice rolls) <a class="yt-timestamp" data-t="30:10:10">[30:10:10]</a>. However, for certain continuous distributions with infinite outcomes, the variance might diverge, and in such cases, the sum may not converge to a [[Normal distribution and its properties | normal distribution]] <a class="yt-timestamp" data-t="30:15:15">[30:15:15]</a>.

It's important to note that the physical [[Galton board and probability distribution | Galton board]] itself often violates the independence and identically distributed assumptions, as the trajectory of a ball can influence subsequent bounces <a class="yt-timestamp" data-t="28:50:50">[28:50:50]</a>. Despite this, a [[Normal distribution and its properties | normal distribution]] still approximates its outcome, partly due to generalizations of the theorem that relax these assumptions <a class="yt-timestamp" data-t="29:38:38">[29:38:38]</a>. It's crucial to avoid assuming a variable is normally distributed without proper justification <a class="yt-timestamp" data-t="29:54:54">[29:54:54]</a>.