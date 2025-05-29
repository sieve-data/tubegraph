---
title: Evaluating limits using numerical methods
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

Evaluating limits using numerical methods involves observing the behavior of a function's output as its input approaches a specific value. This approach complements graphical analysis and provides a quantitative understanding of the limit <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.

## How to Apply Numerical Methods

To numerically evaluate a limit, one can calculate the function's value for input (`x`) values that get progressively closer to the target point from both sides (below and above) <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. If the function's output approaches the same value from both directions, that value is the limit <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

### Example: Approaching from Below

Consider a function `g(x)` defined as `x²` when `x` does not equal 2, and `1` when `x` equals 2 <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. To find the limit as `x` approaches 2, we can choose `x` values increasingly close to 2 but less than 2:

*   For `x = 1.9`, `g(x) = 1.9² = 3.61` <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.
*   For `x = 1.99`, `g(x) = 1.99² = 3.9601` <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   For `x = 1.999`, `g(x) = 1.999² = 3.996001` <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
*   As `x` gets closer to 2 (e.g., `1.9999999999`), `g(x)` gets very, very close to 4 <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

### Example: Approaching from Above

Next, we choose `x` values increasingly close to 2 but greater than 2:

*   For `x = 2.1`, `g(x) = 2.1² = 4.41` <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
*   For `x = 2.01`, `g(x) = 2.01² = 4.0401` <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   As `x` gets closer to 2, `g(x)` seems to get closer to 4 <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>.

### Conclusion from Numerical Data

Since the function's values approach 4 from both sides of `x = 2`, the limit as `x` approaches 2 of `g(x)` is 4 <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. This occurs even though the function's actual value at `x = 2` (`g(2)`) is 1, highlighting a discontinuity <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.

Numerical methods provide a strong indication of a limit's value and can be particularly useful when [[evaluating_functions | evaluating functions]] with complex definitions or discontinuities <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. This method helps to understand what the function is *approaching* rather than its exact value at the point of interest <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.