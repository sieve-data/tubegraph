---
title: Applications of Taylor series in physics and engineering
videoId: 3d6DsjIBzJ4
---

From: [[3blue1brown]] <br/> 

Taylor series are an incredibly powerful mathematical tool, widely used in various fields including mathematics, physics, and many areas of engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Their primary utility lies in their ability to [[approximating_functions_using_taylor_series | approximate functions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Approximating Functions with Polynomials

The study of Taylor series primarily involves taking non-polynomial functions and finding polynomials that can accurately approximate them near a specific input <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This approximation is crucial because polynomials are generally much easier to work with than other types of functions <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. They are simpler to compute, differentiate, and integrate, making them more "friendly" for mathematical operations <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### The Pendulum Problem in Physics

A classic example of Taylor series' application in physics involves the potential energy of a pendulum <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The expression for the pendulum's height above its lowest point is proportional to `1 minus the cosine of the angle` between the pendulum and the vertical <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The cosine function within this expression can make the problem awkward and unwieldy, obscuring the relationship between pendulums and other oscillating phenomena <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, by [[approximating_functions_using_taylor_series | approximating cosine of theta as 1 minus theta squared over 2]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, the problem becomes much more manageable <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This quadratic approximation for cosine is particularly effective for small angles near 0 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Even more advanced approximations, such as `1 minus ½ x² plus 1/24 times x to the fourth`, provide an even closer fit for `cosine(x)` around `x = 0` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. In physics problems involving the cosine of a small angle, substituting these Taylor polynomials for `cosine(x)` yields predictions that are almost unnoticeably different from those using the original function <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### General Engineering Applications

Beyond specific examples, Taylor series are broadly used in engineering fields <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Their ability to simplify complex functions into more manageable polynomial forms makes them invaluable for modeling, analysis, and simulation in diverse engineering disciplines.