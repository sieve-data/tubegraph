---
title: Development of calculus by Isaac Newton
videoId: gMlf1ELvRzc
---

From: [[veritasium]] <br/> 

For two millennia, the calculation of [[History of calculating Pi | Pi]] was a painstakingly slow and tedious process, primarily relying on the Archimedean method of bisecting polygons <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. However, Isaac Newton revolutionized this process by introducing new mathematical techniques, including his development of calculus <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Understanding Pi and Circle Area
[[History of calculating Pi | Pi]] is the ratio of a circle's circumference to its diameter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is also related to a circle's area, given by the formula $\pi R^2$ <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The area formula can be visualized by cutting a circle into thin slices and rearranging them into a rectangle, where the length is half the circumference ($\pi R$) and the width is the radius ($R$), resulting in an area of $\pi R^2$ <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. For a unit circle (radius $R=1$), the area is simply $\pi$ <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Traditional Methods of Calculating Pi
Before Newton, the most common method to estimate [[History of calculating Pi | Pi]] involved inscribing and circumscribing regular polygons around a circle to bound its circumference <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   An inscribed hexagon shows $\pi > 3$ <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   A circumscribed square shows $\pi < 4$ <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

Around 250 BC, Archimedes refined this method by repeatedly bisecting polygons <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Starting with a hexagon, he would derive a 12-gon, then a 24-gon, and so on, calculating their perimeters to get tighter bounds for [[History of calculating Pi | Pi]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. His calculations involved complex square roots and fractions <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. By the time he reached a 96-gon, he determined [[History of calculating Pi | Pi]] was between 3.1408 and 3.1429 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

This method was used for the next 2000 years by [[Mathematical breakthroughs in the Renaissance | Chinese]], Indian, Persian, and Arab mathematicians, each contributing to improved bounds <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Notable examples include:
*   **Francois Viete (late 16th century):** Computed the perimeter of a polygon with 393,216 sides <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Ludolph van Ceulen (early 17th century):** Spent 25 years calculating the perimeter of a polygon with $2^{62}$ (over 4 quintillion) sides, achieving 35 correct decimal places of [[History of calculating Pi | Pi]], which were inscribed on his tombstone <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Christoph Grienberger:** Surpassed van Ceulen 20 years later, reaching 38 correct decimal places <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Newton's Breakthrough: The Generalized Binomial Theorem
In 1666, at just 23 years old, Isaac Newton, while quarantining during a bubonic plague outbreak, was experimenting with polynomial expansions like $(1+X)^2$ and $(1+X)^3$ <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. He observed that the coefficients in these expansions followed a pattern found in [[Euclids Elements and Its Influence on Mathematics | Pascal's triangle]] <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This triangle, known across ancient Greek, Indian, and Chinese cultures, generates coefficients for $(1+X)^N$ where N is a positive integer <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

A general formula for these coefficients, known as the binomial theorem, was already established:
$(1+X)^N = 1 + NX + \frac{N(N-1)}{2!}X^2 + \frac{N(N-1)(N-2)}{3!}X^3 + \dots$ <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

### Extending the Theorem to Non-Integers
The standard binomial theorem applied only when $N$ was a positive integer <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Newton's profound insight was to apply this formula to *non-integer* values of $N$, effectively "breaking" the rule <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

For example, when $N=-1$, $(1+X)^{-1} = \frac{1}{1+X}$:
Plugging $N=-1$ into the binomial theorem yields an infinite series: $1 - X + X^2 - X^3 + X^4 - X^5 + \dots$ <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This occurs because when $N$ is not a positive integer, the $N(N-1)\dots(N-k)$ term never reaches zero, unlike when $N$ is a positive integer and eventually $N-N=0$ <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

Newton justified the validity of this infinite series by demonstrating that multiplying the series by $(1+X)$ resulted in 1, confirming that it was indeed equal to $\frac{1}{1+X}$ <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This generalization implies that [[Euclids Elements and Its Influence on Mathematics | Pascal's triangle]] can be extended "above" its traditional structure, with rows corresponding to negative and fractional powers <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

Newton then applied this generalized binomial theorem to *fractional powers*, such as $N=1/2$, which corresponds to square roots <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. For instance, he could rapidly and efficiently calculate the square root of three by writing it as $\sqrt{4-1} = 2\sqrt{1-\frac{1}{4}}$ and then expanding $\sqrt{1-\frac{1}{4}}$ using the binomial series with $X = -\frac{1}{4}$ and $N=\frac{1}{2}$ <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. This results in a rapidly converging series <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Application to Pi Calculation
Newton recognized the connection between the binomial expansion for fractional powers and the equation of a unit circle <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. The equation for a unit circle is $X^2 + Y^2 = 1$ <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. Solving for $Y$, the upper half of the circle is given by $Y = \sqrt{1-X^2}$ or $(1-X^2)^{1/2}$ <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. By substituting $-X^2$ for $X$ in the binomial expansion for $N=1/2$, Newton obtained an infinite series for the circle's equation <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

### Integration using Fluxions (Calculus)
Crucially, Newton had also just invented [[applications of calculus in physics | calculus]], which he referred to as the theory of Fluxions <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. He realized that integrating the series for $Y$ from $X=0$ to $X=1$ would yield the area of a quarter of the unit circle <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Since the area of a unit circle is $\pi$, the area of a quarter circle is $\pi/4$ <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

Newton knew how to integrate each term of the series (e.g., integrating $X^N$ by increasing the power by one and dividing by the new power) <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This resulted in an infinite series of terms involving simple arithmetic with fractions, which could be evaluated by plugging in $X=1$ to calculate [[History of calculating Pi | Pi]] to arbitrarily high precision <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

### Optimizing Convergence
Newton further refined his method by integrating from $X=0$ to $X=1/2$ instead of $0$ to $1$ <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This choice significantly improved the convergence rate of the infinite series, meaning fewer terms were needed to achieve high accuracy <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. When $X=1/2$, each term shrinks by an additional factor of $X^2$, which is $1/4$ <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

The area computed by integrating from $0$ to $1/2$ is a specific part of the circle that can be broken down into a 30-degree sector (area $\pi/12$) and a right triangle with base $1/2$ and height $\sqrt{3}/2$ <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. By equating this sum to the integrated series and rearranging, Newton derived a new formula for [[History of calculating Pi | Pi]] <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

Using only the first five terms of this optimized series, Newton could calculate $\pi$ to 3.14161, an accuracy off by just two parts in 100,000 <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. To match the 35 decimal places achieved by Ludolph van Ceulen's years of laborious polygon bisection, Newton's method would only require computing 50 terms, taking days instead of years <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

Newton's innovative approach, combining the generalized binomial theorem with his newly developed [[applications of calculus in physics | calculus]], marked a paradigm shift in the history of [[history of physics and mathematics discoveries | mathematical discoveries]] and the calculation of constants like [[History of calculating Pi | Pi]] <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. His method rendered the traditional polygon bisection obsolete <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.