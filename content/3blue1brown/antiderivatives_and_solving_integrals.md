---
title: Antiderivatives and solving integrals
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

One common application of [[Integration and antiderivatives | integration]] is finding the average of a continuous variable <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This concept offers a different perspective on why [[Derivatives and integrals | integrals]] and [[Derivatives and integrals | derivatives]] are inverses of each other <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Averaging a Continuous Variable

Consider the graph of sin(x) between 0 and pi, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A practical question could be finding the average height of this graph on that interval <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This applies to real-world cyclic phenomena, such as modeling the average effectiveness of solar panels based on the number of daylight hours, which follows a sine wave pattern <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

The challenge in finding the average of a continuous variable like sin(x) over an interval (e.g., 0 to pi) is that there are infinitely many values <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It's not possible to simply add them all up and divide by infinity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Approximating with Finite Sums

When faced with the desire to sum infinitely many values associated with a continuum, the key is almost always to use an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. A good first step is to approximate the situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

Imagine sampling a finite number of evenly spaced points along the range [0, pi] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The average height of these sampled points can be found by summing their heights (sin(x) at each point) and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. As more points are sampled, this approximation should get closer to the actual average of the continuous variable <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Connecting to Integrals

This process is related to taking an [[Derivatives and integrals | integral]] of sin(x) between 0 and pi <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. While a finite sum for an average adds heights and divides by the count, an integral adds sin(x) times `dx` (the spacing between samples), which represents little areas, not just heights <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The integral is the limit of this sum as `dx` approaches 0 <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

To reframe the finite sum average (sum of heights / number of points) in terms of `dx`:
1.  The number of samples (`N`) in an interval of length `L` (e.g., pi) with spacing `dx` is approximately `L / dx` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. So, `N = pi / dx` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  Substitute `N` into the average formula: `(sum(sin(x)) / (pi / dx))` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  Rearrange: `(sum(sin(x) * dx) / pi)` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

As the number of samples increases (i.e., `dx` approaches 0), the sum `sum(sin(x) * dx)` approaches the actual integral of sin(x) between 0 and pi <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Therefore, the average height of the graph approaches the integral of sin(x) between 0 and pi, divided by the length of the interval (pi) <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

> Average Height = (Area under graph) / Width <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>

## Solving the Integral: Example with sin(x)

To compute an [[Derivatives and integrals | integral]], one must find an [[Integration and antiderivatives | antiderivative]] of the function inside the integral <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. An [[Integration and antiderivatives | antiderivative]] of sin(x) is a function whose [[Derivatives and integrals | derivative]] is sin(x) <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Since the [[Derivatives and integrals | derivative]] of cos(x) is -sin(x), the [[Integration and antiderivatives | antiderivative]] of sin(x) is -cos(x) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

To evaluate the integral of sin(x) between 0 and pi:
1.  Evaluate the [[Integration and antiderivatives | antiderivative]] (-cos(x)) at the upper bound (pi): `-cos(pi) = -(-1) = 1` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
2.  Evaluate the [[Integration and antiderivatives | antiderivative]] (-cos(x)) at the lower bound (0): `-cos(0) = -1` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
3.  Subtract the lower bound value from the upper bound value: `1 - (-1) = 2` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

Thus, the area under the sine graph from 0 to pi is exactly 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The average height problem's solution is this integral (2) divided by the width of the region (pi) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. So, the average height is `2/pi`, which is approximately 0.64 <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Alternate Perspective: Integrals and Derivatives as Inverses

This problem also highlights the [[Relationship between integrals and derivatives | relationship between integrals and derivatives as inverses]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. The average value (2/pi) was found by looking at the change in the [[Integration and antiderivatives | antiderivative]] (-cos(x)) over the input range (0 to pi), divided by the length of that range (pi) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

This fraction can be viewed as the "rise over run" slope between the points of the [[Integration and antiderivatives | antiderivative]] graph at 0 and pi <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Since sin(x) is, by definition, the [[Derivatives and integrals | derivative]] of its [[Integration and antiderivatives | antiderivative]] (negative cosine), sin(x) gives the slope of the negative cosine graph at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Therefore, the average value of sin(x) can be thought of as the average slope over all tangent lines between 0 and pi <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It makes intuitive sense that the average slope of a graph over a range should equal the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Generalizing the Average Value Formula

For any function `f(x)`, its average value on an interval `[a, b]` is given by:

Average Value = `(Integral of f(x) from a to b) / (b - a)` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>

This can be thought of as the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

To evaluate this [[Derivatives and integrals | integral]], one finds an [[Integration and antiderivatives | antiderivative]] of `f(x)`, often denoted as `F(x)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The integral's value is the change in this [[Integration and antiderivatives | antiderivative]] between `b` and `a`, i.e., `F(b) - F(a)` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

Thus, the solution to the average value problem is `(F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This represents the slope of the [[Integration and antiderivatives | antiderivative]] graph between the two endpoints <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This makes sense because `f(x)` is the [[Derivatives and integrals | derivative]] of `F(x)`, providing the slope of the tangent line to `F(x)` at each point <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Key Takeaways for Integrals

[[Integration and antiderivatives | Antiderivatives]] are central to solving [[Derivatives and integrals | integrals]] because when reframing the average of a continuous value as the average slope of many tangent lines, the answer can be seen by comparing just the endpoints of the [[Integration and antiderivatives | antiderivative]] graph <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

Two key sensations should bring [[Derivatives and integrals | integrals]] to mind:
1.  If a problem can be approximated by breaking it up and summing many small things <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
2.  If an idea understood in a finite context (like averaging numbers) needs to be generalized to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. In such cases, try phrasing it in terms of an integral <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.