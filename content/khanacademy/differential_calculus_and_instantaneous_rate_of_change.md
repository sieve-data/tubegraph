---
title: Differential calculus and instantaneous rate of change
videoId: EKvHQc3QEow
---

From: [[khanacademy]] <br/> 

[[Introduction to Differential Equations | Differential calculus]] is a foundational branch of mathematics focused on understanding the instantaneous rate of change of quantities <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. It addresses the fundamental question: "what is the instantaneous rate of change of something?" <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>

## Founders of Calculus

The development of calculus is largely attributed to two prominent figures:
*   **Isaac Newton** (British mathematician and physicist) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>
*   **Gottfried Leibniz** (German philosopher and mathematician) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

These two gentlemen are considered the "founding fathers of calculus" and did most of their major work in the late 1600s <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. Newton's original term for differential calculus was the "method of fluxions" <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

## Understanding Instantaneous Rate of Change

The core concept in differential calculus is the "instantaneous rate of change" <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This differs from average rate of change because it describes how fast something is changing *at a specific moment* <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

### Example: Usain Bolt's Speed

To illustrate, consider Usain Bolt, the Jamaican sprinter <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

1.  **Plotting Distance vs. Time**: If we plot his distance (y-axis) as a function of time (x-axis), we know he can travel 100 meters in 9.58 seconds <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
    *   At time 0, distance is 0 <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
    *   At 9.58 seconds, distance is 100 meters <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

2.  **Average Speed**:
    *   Average speed is calculated as the change in distance over the change in time (Δy/Δx) <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This is equivalent to the slope of a line connecting two points on the graph <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
    *   For Usain Bolt's 100-meter dash:
        *   Δy = 100 meters <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>
        *   Δx = 9.58 seconds <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>
        *   Average speed = 100 m / 9.58 s ≈ 10.4 meters per second <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a> <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>
        *   This equates to approximately 23.5 miles per hour <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

3.  **Instantaneous Speed vs. Average Speed**:
    *   Usain Bolt does not maintain a constant speed throughout the race; he accelerates and potentially decelerates <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
    *   His distance-time graph would be a curve, where the slope changes continuously <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
    *   The average speed is just the slope of the secant line connecting the start and end points <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
    *   His peak instantaneous velocity is closer to 30 miles per hour, significantly higher than his average <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.

### The Limit Concept

To find the instantaneous rate of change at a specific point on a curve, one must find the slope of the tangent line at that point <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a> <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. This is achieved using the concept of limits:

*   Instead of calculating the average slope over a large Δx, we consider what happens as Δx (change in x) gets "smaller and smaller and smaller" <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   We take the limit as Δx approaches 0 of Δy/Δx <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   This limit will approach the instantaneous rate of change <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   It's important to note that you cannot simply divide by 0 (Δx = 0); the limit concept handles this by observing the behavior as it *approaches* zero <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.

## Terminology

*   **Derivative**: In [[derivatives_and_calculus_terminology | calculus terminology]], the instantaneous slope or instantaneous rate of change is called the [[understanding_derivatives_in_differential_equations | derivative]] <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a> <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Notation (dy/dx)**: The notation used for the derivative is dy/dx <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.
*   **Differentials**: The terms `dy` and `dx` are called differentials <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. They represent an "infinitely small change in y" and an "infinitely small change in x," respectively <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>. By considering these super small changes, the instantaneous slope can be determined <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.