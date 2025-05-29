---
title: Differential Calculus and Its Applications
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

[[introduction_to_derivatives_in_calculus | Differential calculus]] is a branch of mathematics focused on understanding the instantaneous rate of change of something <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Founding Fathers of Calculus
The foundation of calculus was primarily laid by two prominent figures in the late 1600s <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>:
*   **Isaac Newton:** A super famous British mathematician and physicist <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. His original term for [[introduction_to_derivatives_in_calculus | differential calculus]] was "the method of fluxions" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Gottfried Leibnitz:** A famous German philosopher and mathematician, contemporary to Isaac Newton <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

Together, these two gentlemen are considered the founding fathers of calculus <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Core Question: Instantaneous Rate of Change
The fundamental question addressed by [[introduction_to_derivatives_in_calculus | differential calculus]] is "what is the instantaneous rate of change of something?" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This contrasts with average rates of change, aiming to understand what is happening in a specific instant <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Application: Usain Bolt's Speed
To illustrate the concept, consider Usain Bolt, a Jamaican sprinter <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, who was the fastest human alive as of early 2012 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The question in his case is: "How fast is he going right now?" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

#### Average Speed Calculation
Using basic [[comparing_algebraic_and_differential_equations | algebra]], one can calculate average speed <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. If Usain Bolt runs 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:
*   **Average Speed** = Change in Distance / Change in Time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   This is equivalent to the slope (rise over run) between two points on a distance-time graph <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Using `y` for distance and `x` for time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, the average speed is `change in y` over `change in x` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   For Usain Bolt, his average speed over 100 meters is:
    100 meters / 9.58 seconds ≈ 10.4 meters per second <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    This translates to approximately 23.5 miles per hour <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

#### The Challenge of Instantaneous Speed
Average speed doesn't account for variations in speed during a run <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. A runner accelerates at the start and might slow down towards the end <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. On a distance-time graph, this creates a curve, where the slope is constantly changing <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   The slope at any given moment represents the instantaneous speed <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Usain Bolt's peak instantaneous velocity is closer to 30 miles per hour, higher than his average speed <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

#### Finding Instantaneous Rate of Change using Calculus
To find the instantaneous rate of change (or instantaneous slope) at a specific point on a curve, [[introduction_to_derivatives_in_calculus | differential calculus]] employs the concept of a limit <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
1.  **Approximation:** One can approximate the slope by taking a very small change in `x` (`delta x`) and the corresponding change in `y` (`delta y`) around the point of interest <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. However, this is still an approximation because the curve's slope is continuously changing <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
2.  **The Limit:** To get a more precise value, we take the limit as `delta x` approaches zero <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>:
    $$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$
    This process approaches the instantaneous rate of change <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
3.  **The Derivative:** This instantaneous slope is called the **derivative** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
    *   The notation for the derivative is `dy/dx` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
    *   `dy` and `dx` are referred to as "differentials," representing an infinitely small change in `y` and `x` respectively <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   By considering these infinitesimally small changes, [[introduction_to_derivatives_in_calculus | differential calculus]] allows for the calculation of instantaneous values, like Usain Bolt's speed at a particular moment <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

> [!CAUTION]
> It is crucial to note that `delta x` cannot simply be zero, as division by zero is undefined <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. The limit process addresses this by examining what happens as `delta x` gets arbitrarily close to zero <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.