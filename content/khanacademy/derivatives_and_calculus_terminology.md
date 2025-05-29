---
title: Derivatives and calculus terminology
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

[[differential_calculus_and_instantaneous_rate_of_change | Differential calculus]] was primarily founded by Isaac Newton, a British mathematician and physicist, and Gottfried Leibnitz, a German philosopher and mathematician <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. These two individuals performed most of their significant work in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Both were deeply interested in the same fundamental question: what is the instantaneous rate of change of something? <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> This question is the core focus of [[differential_calculus_and_instantaneous_rate_of_change | differential calculus]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Understanding Instantaneous Rate of Change

The core concept in [[differential_calculus_and_instantaneous_rate_of_change | differential calculus]] is the instantaneous rate of change, which seeks to answer how fast something is changing *right now* <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. For example, rather than knowing Usain Bolt's average speed over a period, [[differential_calculus_and_instantaneous_rate_of_change | differential calculus]] aims to determine his speed at a precise moment <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Isaac Newton's original term for [[differential_calculus_and_instantaneous_rate_of_change | differential calculus]] was the "method of fluxions," which also emphasized understanding what is happening in a specific instant <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Average vs. Instantaneous Speed

To illustrate the difference between average and instantaneous rates, consider a graph plotting distance (y-axis) against time (x-axis) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

Usain Bolt's performance in a 100-meter sprint serves as an example:
*   He travels 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Average speed** is calculated as the change in distance over the change in time (Δy / Δx) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a> <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   This calculation represents the [[calculating_the_derivative_as_the_slope_of_tangent_line | slope]] of a line connecting two points on the distance-time graph <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   For Bolt's 100-meter sprint, his average speed is 100 meters / 9.58 seconds ≈ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, which is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This average speed is the rate of change between the starting and ending points <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a> <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

However, a runner does not maintain a constant speed. They accelerate, reach a peak speed, and may slow down. If Bolt's distance versus time were plotted, it would be a curve, not a straight line <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   At the beginning, his speed (slope) would be lower <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a> <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   As he accelerates, the slope becomes steeper <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a> <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   Towards the end, he might tire, and the slope would flatten slightly <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a> <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

Bolt's peak instantaneous velocity, for instance, is closer to 30 miles per hour, significantly higher than his average speed <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. The instantaneous speed is the [[calculating_the_derivative_as_the_slope_of_tangent_line | slope of the tangent line]] at a specific point on the curve <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Calculating the Derivative

Approximating instantaneous speed by taking a small change in x (Δx) and finding the corresponding change in y (Δy) only provides an approximation because the curve's slope is constantly changing <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. To find the true instantaneous rate of change, one must take the [[the_concept_of_a_limit_in_finding_derivatives | limit]] as Δx approaches zero <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>:

$$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$ <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>

This concept leads to the [[definition_and_significance_of_the_derivative | definition of the derivative]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Terminology:

*   The instantaneous rate of change, or the instantaneous [[calculating_the_derivative_as_the_slope_of_tangent_line | slope]] at a point on a curve, is known as the [[definition_and_significance_of_the_derivative | derivative]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   The notation for the [[definition_and_significance_of_the_derivative | derivative]] is `dy/dx` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   `dy` and `dx` are referred to as "differentials," representing infinitely small changes in y and x, respectively <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a> <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a> <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This process of considering infinitesimally small changes allows for the determination of instantaneous rates of change <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   It is crucial to use the concept of a [[the_concept_of_a_limit_in_finding_derivatives | limit]] because simply dividing by zero (`Δx = 0`) would result in an undefined value <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a> <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Instead, one considers what the value approaches as `Δx` gets infinitesimally close to zero <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

This rigorous study of [[the_concept_of_a_limit_in_finding_derivatives | limits]] and instantaneous rates is central to understanding [[introduction_to_derivatives | derivatives]] in [[introduction_to_derivatives | calculus]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a> <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.