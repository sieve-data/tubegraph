---
title: Usain Bolt and Calculus
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

## The Fundamental Question of Motion

Isaac Newton and Gottfried Leibnitz, considered the founding fathers of [[history_of_calculus | calculus]], performed their major work in the late 1600s <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Centuries later, Jamaican sprinter Usain Bolt, recognized as the fastest human alive as of early 2012, was still setting records <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. Despite the vast difference in their eras and fields, these individuals were all focused on the same fundamental question: what is the instantaneous rate of change of something? <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a> <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. This question is precisely what [[Differential Calculus and Its Applications | differential calculus]] addresses <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

For Usain Bolt, the question translates to "How fast is he going right now?" <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a> This differs significantly from his average speed over a period <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. [[Differential Calculus and Its Applications | Differential calculus]] is specifically focused on these instantaneous rates of change <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. Newton's original term for [[Differential Calculus and Its Applications | differential calculus]] was the "method of fluxions" <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>, emphasizing what happens "in this instant" <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Average Speed vs. Instantaneous Speed

To understand the challenge of instantaneous rate of change, consider Usain Bolt's distance plotted against time <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

### Calculating Average Speed

Usain Bolt can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. His average speed is calculated as the change in distance (y) over the change in time (x) <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a> <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This is equivalent to finding the slope of a line connecting the start point (0 meters at 0 seconds) and the end point (100 meters at 9.58 seconds) on a distance-time graph <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

The change in distance is 100 meters, and the change in time is 9.58 seconds <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
His average speed is:
$$ \frac{100 \text{ meters}}{9.58 \text{ seconds}} \approx 10.4 \text{ meters/second} $$ <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a> <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>

This average speed can be converted to miles per hour:
$$ 10.4 \text{ m/s} \times \frac{3600 \text{ s}}{1 \text{ hour}} \times \frac{1 \text{ mile}}{1600 \text{ meters}} \approx 23.5 \text{ mph} $$ <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a> <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a> <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>

This average speed represents the rate of change over the entire duration <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

### The Concept of Instantaneous Speed

Usain Bolt does not maintain a constant speed throughout his race; he accelerates <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. His distance-time graph would be a curve <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>:
- Initially, he starts slower, so the slope (speed) is lower <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
- He then accelerates, causing the slope to get steeper <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.
- Towards the end, he might tire, and his speed (slope) might decrease slightly <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

The average speed is the slope of the line connecting the start and end points of this curve <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. However, the instantaneous speed at any given moment is the slope of the *tangent line* to the curve at that specific point <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a> <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. Usain Bolt's peak instantaneous velocity during his 100m sprint was actually closer to 30 miles per hour, significantly higher than his average speed <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a> <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.

## The Role of Differential Calculus

Traditional algebra struggles to address instantaneous rate of change because the slope of a curve is constantly changing <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a> <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. Approximating the slope by taking a small change in x (`delta x`) and finding the corresponding change in y (`delta y`) provides an approximation <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

To find the true instantaneous rate of change, [[Differential Calculus and Its Applications | differential calculus]] uses the concept of a limit:
$$ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $$ <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a> <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>

This limit, where the change in x approaches zero, allows for the calculation of the instantaneous slope at a single point on the curve <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. This instantaneous slope is known as the **derivative** <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a> <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

The notation for the derivative is `dy/dx` <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. Here, `dy` and `dx` are considered "differentials," representing infinitely small changes in y and x, respectively <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. By evaluating the ratio of these infinitely small changes, one can determine the instantaneous speed, such as Usain Bolt's speed at any specific moment <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a> <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. It's crucial that `delta x` *approaches* zero rather than being zero, as division by zero is undefined <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a> <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.