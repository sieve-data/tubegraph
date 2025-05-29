---
title: Instantaneous Rate of Change
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

The concept of instantaneous rate of change is a fundamental question addressed by [[Differential Calculus and Its Applications | differential calculus]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This concept was primarily developed by Isaac Newton, a super famous British mathematician and physicist, and Gottfried Leibniz, a famous German philosopher and mathematician, both contemporaries who performed much of their major work in the late 1600s <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. They were both concerned with the same core question: "what is the instantaneous rate of change of something?" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Distinguishing from Average Rate of Change

To understand instantaneous rate of change, it's helpful to first consider average rate of change.

### Example: Usain Bolt's Speed

Consider Usain Bolt, the Jamaican sprinter, who is the fastest human alive as of early 2012 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The question about him is: "How fast is he going right now?" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This differs from his average speed over a period of time, such as his average speed for the last second or over the next 10 seconds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

#### Average Speed Calculation

If we plot Usain Bolt's distance (y-axis) as a function of time (x-axis) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
*   At time zero, he hasn't moved <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   He can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

His average speed is calculated as the change in distance over the change in time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This is equivalent to the slope between two points on a distance-time graph <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

*   Change in distance (Δy) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Change in time (Δx) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

Average speed = 100 meters / 9.58 seconds ≈ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
This average speed is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The slope here represents the average rate of change between these two points <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

#### Instantaneous Speed

Usain Bolt does not maintain a constant speed; he accelerates and then might slow down slightly <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>, <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   Initially, he starts slower, meaning the slope of his distance-time graph is flatter <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   As he accelerates, the slope becomes steeper <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Towards the end, he might tire, and the slope might flatten again <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

His distance plotted against time would be a curve, not a straight line <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. What was calculated (10.4 m/s) is only the average slope across the entire time interval <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. At any given moment, his actual speed (instantaneous speed) is different <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. For instance, Usain Bolt's peak instantaneous [[speed_vs_velocity | velocity]] is closer to 30 miles per hour <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Calculating Instantaneous Rate of Change

Calculating the instantaneous rate of change is not straightforward with traditional algebra, as the slope of the curve is constantly changing <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. An approximation can be made by taking a very small change in time (Δx) and calculating the change in distance (Δy) around a specific point <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

To get a precise instantaneous rate of change, the concept of a [[Definition of the Derivative | limit]] is used:

```
lim (Δy / Δx) as Δx approaches 0
```
This process yields the instantaneous rate of change, which can be viewed as:
*   The instantaneous slope at that point on the curve <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   The slope of the tangent line at that point on the curve <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   The [[Understanding Derivatives | derivative]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Notation

The notation for the derivative is `dy/dx` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. In this notation, `dy` is a differential (an infinitely small change in y), and `dx` is a differential (an infinitely small change in x) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. By considering these infinitesimally small changes, the instantaneous slope or speed at a given moment can be determined <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. It's crucial to understand that Δx approaches zero, rather than being exactly zero, because division by zero is undefined <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Newton's original term for [[Differential Calculus and Its Applications | differential calculus]] was "the method of fluxions," emphasizing "what's happening in this instant" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.