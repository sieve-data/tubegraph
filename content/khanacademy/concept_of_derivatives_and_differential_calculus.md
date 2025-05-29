---
title: Concept of derivatives and differential calculus
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

[[differential_calculus_and_rates_of_change | Differential calculus]] is a branch of [[introduction_to_derivatives | calculus]] that focuses on understanding instantaneous rates of change <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Founding Fathers

The foundational work for [[differential_calculus_and_rates_of_change | calculus]] was primarily developed in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> by two key figures:
*   **Isaac Newton** A renowned British mathematician and physicist <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. His original term for [[differential_calculus_and_rates_of_change | differential calculus]] was "the method of fluxions" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Gottfried Leibniz** A famous German philosopher and mathematician, contemporary to Isaac Newton <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

These two gentlemen are considered the founding fathers of [[differential_calculus_and_rates_of_change | calculus]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Fundamental Question

Both Newton and Leibniz were intensely focused on the same fundamental question that [[differential_calculus_and_rates_of_change | differential calculus]] addresses: What is the instantaneous rate of change of something? <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This means understanding "what's happening in this instant" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Instantaneous vs. Average Rate of Change: Usain Bolt Example

To illustrate this, consider Usain Bolt, the Jamaican sprinter <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
His best work was in 2012, when he was considered the fastest human alive <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Average Speed Calculation
If we plot Usain Bolt's distance ($y$) as a function of time ($x$), starting from zero <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>:
*   At time 0, he hasn't moved <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   He can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

His average speed is calculated as the change in distance over the change in time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
This is equivalent to the change in $y$ over the change in $x$ ($\Delta y / \Delta x$) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. In terms of a graph, this is the slope between two points <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

For Usain Bolt's 100-meter dash:
*   Change in $y$ (distance) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Change in $x$ (time) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

Average speed = 100 meters / 9.58 seconds $\approx$ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This converts to approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This average speed represents the slope of the secant line connecting the start and end points of the race on a distance-time graph <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a> <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### The Challenge of Instantaneous Speed
Traditional algebra struggles to find an exact instantaneous rate of change <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. While the average speed is 23.5 mph, Usain Bolt doesn't maintain a constant speed throughout the race <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   He accelerates at the beginning, meaning his speed (and thus the slope of his distance-time graph) increases <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   He might slow down near the end <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   His actual instantaneous peak velocity is closer to 30 miles per hour <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The distance-time plot is a curve, and the slope is constantly changing <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The instantaneous rate of change at any point on this curve corresponds to the slope of the tangent line at that specific point <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## The Role of Limits and Derivatives
To find the exact instantaneous rate of change, or the slope of the tangent line, [[differential_calculus_and_rates_of_change | differential calculus]] uses the concept of [[introduction_to_limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

The instantaneous rate of change is found by taking the [[introduction_to_limits_in_calculus | limit]] of the average rate of change ($\Delta y / \Delta x$) as the change in $x$ ($\Delta x$) approaches zero <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a> <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. While $\Delta x$ cannot be exactly zero (as division by zero is undefined) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, the idea is to see what value the ratio approaches as $\Delta x$ becomes infinitesimally small <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### The Derivative
This [[concept_of_approaching_values_in_calculus | limit]], when it exists, is called the **derivative** <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. The [[definition_and_application_of_derivatives | derivative]] represents the instantaneous slope or instantaneous rate of change at a given point on a curve <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

The notation used for the derivative is $\text{dy}/\text{dx}$ <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. In this notation:
*   **dy** is a "differential" representing an infinitely small change in $y$ <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a> <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **dx** is a "differential" representing an infinitely small change in $x$ <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a> <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

By taking these infinitely small changes, one can determine the instantaneous speed (or rate of change) of Usain Bolt at any specific moment <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.