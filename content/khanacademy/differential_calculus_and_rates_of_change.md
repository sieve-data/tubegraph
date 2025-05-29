---
title: Differential calculus and rates of change
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

[[concept_of_derivatives_and_differential_calculus | Differential calculus]] is a branch of mathematics focused on understanding the instantaneous rate of change of something <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Founding Fathers of Calculus

The foundation of calculus was primarily laid by two gentlemen:
*   **Isaac Newton** <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>: A super famous British mathematician and physicist who did most of his major work in the late 1600s <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. His original term for [[concept_of_derivatives_and_differential_calculus | differential calculus]] was "the method of fluxions" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Gottfried Leibniz** <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>: A famous German philosopher and mathematician who was a contemporary of Isaac Newton <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. He also did most of his major work in the late 1600s <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

Both Newton and Leibniz were obsessed with the same fundamental question: "What is the instantaneous rate of change of something?" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Instantaneous Rate of Change: The Core Question

The central problem that [[concept_of_derivatives_and_differential_calculus | differential calculus]] addresses is determining the instantaneous rate of change <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This means understanding how fast something is changing *right now*, not just its average change over a period <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Example: Usain Bolt's Speed

Consider Usain Bolt, the Jamaican sprinter, who, as of early 2012, was the fastest human alive <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The question in his case is: "How fast is he going right now?" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This is different from his average speed over a second or ten seconds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Average Speed vs. Instantaneous Speed

To illustrate the difference, consider a graph where the y-axis represents distance (y) and the x-axis represents time (x) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Usain Bolt can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

*   **Average Speed**: The average speed is calculated as the change in distance over the change in time (Δy / Δx) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This represents the slope of a line connecting two points on the distance-time graph <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
    *   Change in distance (Δy) = 100 meters <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
    *   Change in time (Δx) = 9.58 seconds <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
    *   Average Speed = 100 meters / 9.58 seconds ≈ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   This is approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

*   **Instantaneous Speed**: Usain Bolt does not maintain a constant speed. He accelerates at the start and may slow down towards the end <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Therefore, his distance-time graph would be a curve, not a straight line <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   The slope of this curve, representing the rate of change of distance, varies at different moments <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   His peak instantaneous velocity has been recorded closer to 30 miles per hour <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
    *   Finding this instantaneous speed is not a simple algebraic problem because the slope is constantly changing <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Calculating Instantaneous Rate of Change using Limits

To find the instantaneous rate of change (or instantaneous slope) at a specific point on a curve, calculus uses the concept of limits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

The instantaneous rate of change is defined as the limit of the average rate of change (Δy / Δx) as the change in x (Δx) approaches zero <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>:

$$
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

This is crucial because simply setting Δx to zero would result in an undefined division by zero <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. By taking the limit, one approaches the exact instantaneous rate of change <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Derivatives and Differentials

*   **Derivative**: In calculus terminology, the instantaneous slope at a point on a curve is called the [[concept_of_derivatives_and_differential_calculus | derivative]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. It is commonly denoted as dy/dx <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Differentials**: The terms 'dy' and 'dx' in the derivative notation are called differentials <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. They represent an infinitely small change in y (dy) over an infinitely small change in x (dx) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. By working with these infinitely small changes, one can determine the instantaneous slope, like Usain Bolt's instantaneous speed at a precise moment <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.