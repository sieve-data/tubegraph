---
title: Average speed versus instantaneous speed
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

The fundamental question addressed by [[Differential calculus and instantaneous rate of change | differential calculus]] is: "What is the instantaneous rate of change of something?" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> This concept differentiates between an object's overall rate of motion over a period and its speed at a specific moment in time.

## Founding Fathers of Calculus

[[Differential calculus and instantaneous rate of change | Calculus]] was primarily founded by Isaac Newton, a British mathematician and physicist, and Gottfried Leibnitz, a German philosopher and mathematician <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. They conducted most of their major work in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Newton's original term for [[Differential calculus and instantaneous rate of change | differential calculus]] was "the method of fluxions," which emphasizes what is happening in a particular instant <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Average Speed

To understand the difference, consider Usain Bolt, who in early 2012 was the fastest human alive <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. He is capable of traveling 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

On a graph where the y-axis represents distance and the x-axis represents time <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, if we plot his distance as a function of time, his journey starts at (0,0) and ends at (9.58 seconds, 100 meters) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

His average speed is calculated as the change in distance over the change in time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This is equivalent to the change in y (distance) over the change in x (time) between two points <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. In algebra, this calculation represents the [[understanding_slope_as_rate_of_change | slope]] of the line connecting these two points on a [[plotting_distance_versus_time_and_slope_interpretation | distance-time graph]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

For Usain Bolt's 100-meter dash:
*   Change in distance (Δy) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Change in time (Δx) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

His average speed is:
$$
\text{Average Speed} = \frac{100 \text{ meters}}{9.58 \text{ seconds}} \approx 10.4 \text{ meters per second}
$$
<a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>

This average speed is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This value represents the average rate of change between the start and end points <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
It's important to note that this is speed, not velocity, because direction is not specified in this calculation, though speed and velocity are closely related, with velocity specifying direction. This highlights a key aspect of [[examples_of_vectors_and_scalars_in_motion | vectors and scalars in motion]] and the [[difference_between_speed_and_velocity | difference between speed and velocity]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Instantaneous Speed

Average speed does not reflect how fast Usain Bolt was going at any specific moment <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. He doesn't immediately reach his top speed; he accelerates <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
A more realistic [[plotting_distance_versus_time_and_slope_interpretation | distance-time graph]] for Usain Bolt would be a curve:
*   He starts slower, so the [[understanding_slope_as_rate_of_change | slope]] is lower <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   He accelerates, making the [[understanding_slope_as_rate_of_change | slope]] steeper <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   He might tire near the end, causing the [[understanding_slope_as_rate_of_change | slope]] to flatten slightly <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The average speed is simply the slope of the line connecting the start and end points of this curve <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. However, at any given moment, the actual speed (or instantaneous rate of change of distance) is different <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

To find the instantaneous speed, one must consider the [[calculating_the_derivative_as_the_slope_of_tangent_line | slope of the tangent line]] at that specific point on the curve <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Traditional algebra struggles with this because the slope of the curve is constantly changing <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### The Role of Limits and the Derivative

[[Differential calculus and instantaneous rate of change | Differential calculus]] addresses this by taking the limit of the average rate of change as the change in time (Δx) approaches zero <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

$$
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$
<a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>

This limit approaches the instantaneous rate of change <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This instantaneous slope is known as the [[calculating_the_derivative_as_the_slope_of_tangent_line | derivative]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. The notation for the derivative is dy/dx <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Here, 'dy' and 'dx' are considered "differentials," representing infinitely small changes in y and x, respectively <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. By examining these infinitely small changes, calculus can determine the exact instantaneous slope or speed at a given moment <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

For example, while Usain Bolt's average speed was 23.5 miles per hour, his peak instantaneous velocity was closer to 30 miles per hour <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This higher speed occurred at his fastest point during the race, represented by the steepest part of his [[plotting_distance_versus_time_and_slope_interpretation | distance-time graph]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.