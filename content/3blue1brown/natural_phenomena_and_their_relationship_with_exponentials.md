---
title: Natural phenomena and their relationship with exponentials
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

Many natural phenomena exhibit a specific characteristic: their rate of change is directly proportional to the current quantity of the phenomenon itself <a class="yt-timestamp" data-t="00:11:56">[11:56]</a>. When a variable's rate of change is proportional to itself, the function describing that variable over time will be an [[exponential_growth | exponential]] function <a class="yt-timestamp" data-t="00:12:39">[12:39]</a>.

## Examples in Nature and Finance

Several real-world examples illustrate this relationship:

*   **Population Growth:** The rate of growth of a population tends to be proportional to its current size, assuming no resource limitations <a class="yt-timestamp" data-t="00:12:03">[12:03]</a>.
*   **Cooling of Water:** When a hot object (like a cup of hot water) is placed in a cooler environment, its rate of cooling is proportional to the temperature difference between the object and the room <a class="yt-timestamp" data-t="00:12:14">[12:14]</a>. In other words, the rate at which the temperature difference changes is proportional to itself <a class="yt-timestamp" data-t="00:12:26">[12:26]</a>.
*   **Financial Investment:** The rate at which an investment grows is proportional to the amount of money currently invested <a class="yt-timestamp" data-t="00:13:31">[13:31]</a>.

## The Role of the Constant 'e'

While any [[exponential_growth | exponential]] function can describe these phenomena, it is common practice in calculus and its applications to express them using the mathematical constant *e* (approximately 2.71828) <a class="yt-timestamp" data-t="00:11:08">[11:08]</a>, <a class="yt-timestamp" data-t="00:12:51">[12:51]</a>.

This preference for *e* stems from its unique derivative property:
*   The derivative of *e*<sup>t</sup> is *e*<sup>t</sup> <a class="yt-timestamp" data-t="00:08:22">[08:22]</a>. This means the proportionality constant between the function and its derivative is 1 <a class="yt-timestamp" data-t="00:08:26">[08:26]</a>.
*   For other bases, such as 2<sup>t</sup> or 3<sup>t</sup>, the derivative is proportional to the function itself, but with a different constant <a class="yt-timestamp" data-t="00:05:52">[05:52]</a>, <a class="yt-timestamp" data-t="00:06:09">[06:09]</a>. For example, the derivative of 2<sup>t</sup> is approximately 0.6931 * 2<sup>t</sup> <a class="yt-timestamp" data-t="00:06:09">[06:09]</a>, and for 3<sup>t</sup>, it's approximately 1.0986 * 3<sup>t</sup> <a class="yt-timestamp" data-t="00:06:41">[06:41]</a>.

When an [[exponential_growth | exponential]] function is written in the form *e*<sup>kt</sup>, the constant 'k' in the exponent takes on a very natural and interpretable meaning <a class="yt-timestamp" data-t="00:11:45">[11:45]</a>, <a class="yt-timestamp" data-t="00:12:56">[12:56]</a>. This 'k' value is precisely the proportionality constant between the changing variable's size and its rate of change <a class="yt-timestamp" data-t="00:13:04">[13:04]</a>.

For instance, any exponential function like 2<sup>t</sup> can be rewritten using *e* via the [[natural_logarithms_and_exponential_growth | natural logarithm]]: 2<sup>t</sup> = *e*<sup>(ln 2)t</sup> <a class="yt-timestamp" data-t="00:10:10">[10:10]</a>. Here, ln 2 (approximately 0.6931) serves as the constant 'k' <a class="yt-timestamp" data-t="00:10:34">[10:34]</a>. This demonstrates that the "mystery constants" observed with other bases are simply the [[natural_logarithms_and_exponential_growth | natural logarithm]] of the base <a class="yt-timestamp" data-t="00:10:46">[10:46]</a>.

This convention simplifies the application of calculus, especially the [[derivatives_of_exponential_functions | chain rule]], making the proportionality constant directly visible within the function's expression <a class="yt-timestamp" data-t="00:09:01">[09:01]</a>, <a class="yt-timestamp" data-t="00:09:38">[09:38]</a>.