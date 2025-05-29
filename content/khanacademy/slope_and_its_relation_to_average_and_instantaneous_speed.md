---
title: Slope and its relation to average and instantaneous speed
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

Differential calculus, pioneered by Isaac Newton <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> and Gottfried Leibnitz <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, primarily addresses the fundamental question: "What is the [[tangent_line_and_instantaneous_slope | instantaneous rate of change]] of something?" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> This concept applies to various scenarios, such as determining how fast an athlete like Usain Bolt is going at a specific moment in time <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Newton's original term for differential calculus was the "method of fluxions" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, emphasizing the focus on what is happening "in this instant" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Graphing Distance Versus Time

To understand the difference between average and instantaneous speed, a graph with distance (y-axis) and time (x-axis) is useful <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. For Usain Bolt, at time zero, he hasn't moved <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. He is known to cover 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Average Speed and Slope

[[calculating_speed_and_velocity | Average speed]] is calculated as the [[definition_of_slope_as_change_in_y_over_change_in_x | change in distance over the change in time]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. On a distance-time graph, this corresponds to the [[slope_of_a_line_in_algebra | slope of a straight line]] connecting two points <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

For Usain Bolt's 100-meter dash:
*   Change in distance (Δy) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Change in time (Δx) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

His average speed is 100 meters / 9.58 seconds ≈ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The [[slope_of_a_straight_line | slope]] here represents the average rate of change between these two points <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Instantaneous Speed and the Slope of a Curve

Unlike average speed, [[tangent_line_and_instantaneous_slope | instantaneous speed]] considers the speed at a precise moment <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. An athlete does not maintain a constant speed; they accelerate and decelerate <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. On a distance-time graph, Usain Bolt's actual performance would be represented by a [[slope_of_a_curve | curve]], not a straight line, as he starts slower, accelerates, and then might tire <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

At any given moment on this curve, the [[slope_of_a_curve | slope is different]] <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The [[tangent_line_and_instantaneous_slope | instantaneous rate of change]] (or instantaneous speed) at a specific point on the curve is the [[slope_of_a_curve | slope of the tangent line]] at that point <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Usain Bolt's peak instantaneous velocity, for example, is closer to 30 miles per hour, significantly higher than his average speed <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Approaching Instantaneous Rate of Change

Calculating instantaneous speed is not straightforward with traditional algebra because the [[slope_of_a_curve | slope of a curve]] is constantly changing <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. To find the instantaneous rate of change, one must consider what happens as the "change in x" (Δx) gets infinitesimally smaller <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This concept is formalized by taking the limit of the [[definition_of_slope_as_change_in_y_over_change_in_x | change in y over change in x]] (Δy/Δx) as Δx approaches zero:

$$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$ <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>

This limit represents the [[tangent_line_and_instantaneous_slope | instantaneous slope]] <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>, also known as the [[tangent_line_and_instantaneous_slope | slope of the tangent line]] at that specific point on the curve <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## The Derivative: Instantaneous Slope

In calculus terminology, this [[tangent_line_and_instantaneous_slope | instantaneous slope]] is called the **derivative** <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The notation for the derivative is `dy/dx` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Here, `dy` and `dx` are considered "differentials," representing infinitely small changes in y and x, respectively <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. By considering these infinitesimally small changes, the instantaneous slope (or speed in this example) can be precisely determined <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It's crucial to note that one cannot simply substitute zero for Δx, as this would lead to an undefined division by zero <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>; hence, the use of a limit <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.