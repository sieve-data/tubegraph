---
title: Plotting distance versus time and slope interpretation
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

Differential calculus, pioneered by [[Isaac Newton | Isaac Newton]] and [[Gottfried Leibnitz | Gottfried Leibnitz]] in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, addresses the fundamental question of instantaneous rate of change <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This concept is crucial for understanding how fast something is moving at a precise moment, rather than its average speed over a period <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Newton himself referred to differential calculus as the "method of fluxions" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Graphing Distance Versus Time

To visualize the concept of rate of change, a common method is to [[graphing_equations | plot]] distance against time <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   The vertical axis (y-axis) represents distance <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   The horizontal axis (x-axis) represents time <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

Consider Usain Bolt, who can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. On such a graph, he starts at 0 distance at time 0 <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, and reaches 100 meters at 9.58 seconds <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Interpreting Slope as Rate of Change

### Average Rate of Change (Average Speed)

The average speed over a given interval can be calculated as the change in distance divided by the change in time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. On a distance-time graph, this corresponds to the [[understanding_slope_of_a_straight_line | slope of the line]] connecting the two points representing the start and end of the interval <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

This concept is similar to "rise over run" in algebra <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, where:
*   Change in distance (change in y) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Change in time (change in x) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

For Usain Bolt's 100-meter dash, his average speed (or average rate of change) is:
$$
\text{Average Speed} = \frac{\text{Change in distance}}{\text{Change in time}} = \frac{100 \text{ meters}}{9.58 \text{ seconds}} \approx 10.4 \text{ meters/second}
$$
<a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>

This average speed is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The [[slope_of_a_line_in_algebra | slope]] itself represents the rate of change <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, and its units (meters/second) are those of speed <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Instantaneous Rate of Change (Instantaneous Speed)

In reality, Usain Bolt's speed is not constant throughout the race; he accelerates and then may tire <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This means his distance-time [[graph interpretation for slope calculation | graph]] is a curve, not a straight line <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The [[determining_slope | slope]] of this curve is constantly changing <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, reflecting his varying instantaneous speed. His peak instantaneous velocity was closer to 30 miles per hour <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, which is higher than his average speed.

To find the instantaneous rate of change at a specific point on a curve, traditional algebra's method of [[Finding the slope of a line using two points | finding the slope between two points]] is insufficient because the curve's slope is continuously changing <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

Calculus addresses this by using the concept of a limit:
*   One can approximate the instantaneous slope by considering very small changes in x ($\Delta x$) and the corresponding changes in y ($\Delta y$) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   The more $\Delta x$ shrinks, the better the approximation of the slope at that point <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   The [[introduction_to_slope_of_a_curve | instantaneous rate of change]] is precisely defined as the limit of $\frac{\Delta y}{\Delta x}$ as $\Delta x$ approaches zero <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>, <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

This limit represents:
*   The instantaneous rate of change <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   The instantaneous slope at that point on the curve <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   The slope of the tangent line to the curve at that point <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   In calculus terminology, this is called the **derivative** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>, <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

The notation for the derivative is $\frac{dy}{dx}$ <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Here, $dy$ and $dx$ are considered "differentials," representing infinitely small changes in y and x, respectively <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This method allows for the calculation of an object's instantaneous speed at any given moment <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. It's important to note that you cannot simply substitute zero for $\Delta x$ because division by zero is undefined; instead, the limit as $\Delta x$ approaches zero is taken <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.