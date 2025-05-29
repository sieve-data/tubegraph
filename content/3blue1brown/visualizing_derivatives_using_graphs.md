---
title: Visualizing derivatives using graphs
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding a derivative is to explain what it is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While often described as an "instantaneous rate of change," this phrase is an oxymoron because change occurs between distinct points in time, not at a single instant <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The cleverness of calculus lies in capturing this idea with a sensible piece of mathematics: the derivative <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Graphing Motion: Distance vs. Time

To understand [[understanding_what_a_derivative_is|what a derivative is]], consider the motion of a car starting at point A, speeding up, and then slowing to a stop at point B 100 meters away over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This motion can be graphed with the vertical axis representing the distance traveled and the horizontal axis representing time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. At any given time *t*, the height of the graph (commonly named *s*(*t*)) indicates the total distance the car has traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

The shape of this distance-time graph directly relates to the car's speed:
*   **Shallow Curve** The curve is initially shallow because the car starts slowly, meaning the distance traveled in the first second doesn't change much <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Steeper Slope** As the car speeds up, the distance covered in a given second increases, corresponding to a steeper slope in the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Shallowing Out** Towards the end, as the car slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

If the car's velocity (in meters per second) were plotted as a function of time, it might appear as a bump-shaped curve <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. These two curves (distance vs. time and velocity vs. time) are inherently related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Intuitively, the car's velocity should be higher when the distance function's graph is steeper, indicating more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### The Paradox of "Instantaneous Velocity"

While we intuitively understand "velocity at a given moment" (like a speedometer reading), mathematically, velocity requires two separate points in time to compare the change in distance across a change in time <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. A single snapshot of a car cannot tell you its speed <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This apparent paradox was a central conflict for the creators of calculus <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Approaching the Derivative: ds/dt

In the real world, a car's speedometer measures speed by calculating how far the car travels over a very small, but finite, amount of time (e.g., between 3 seconds and 3.01 seconds) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This small change in time is denoted as *dt*, and the resulting small change in distance is *ds* <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The velocity at a point in time is then approximately *ds* divided by *dt* <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

Graphically, *ds*/*dt* can be visualized by zooming in on a point on the distance-time graph <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>:
*   ***dt*** A small step to the right along the horizontal (time) axis <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   ***ds*** The resulting change in the height of the graph along the vertical (distance) axis <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

Thus, *ds*/*dt* represents the "rise over run" slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio, considered as a function of *t*, gives the velocity at any time *t* <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For example, to plot the velocity function, one could calculate *s*(*t* + *dt*) - *s*(*t*), then divide this by *dt* for many values of *t* <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## The True Derivative: Slope of a Tangent Line

The pure mathematical derivative isn't *ds*/*dt* for a *specific* small choice of *dt*. Instead, it's what that ratio *approaches* as *dt* approaches 0 <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Geometric Interpretation

As *dt* approaches 0, the two separate points used to calculate the slope also approach each other. This causes the slope of the line passing through these two points to approach the slope of a line that is *tangent* to the graph at the single point *t* <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Therefore, the [[geometric_interpretation_of_derivatives|true derivative]] is equal to the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

This approach provides a "sneaky backdoor" to talk about the rate of change at a single point in time without relying on the nonsensical idea of change in an instant <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. It allows for a reasonable discussion of "rate of change at a single point in time" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Derivative as Best Constant Approximation

It's healthiest to think of this slope not as an instantaneous rate of change, but as the best constant approximation for a rate of change around a point <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. The notation *ds*/*dt* conventionally implies the intention to see what happens as *dt* approaches 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Example: The Derivative of t³

Consider a distance function *s*(*t*) = *t*³ <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To find the velocity (derivative) at *t* = 2, one would initially calculate the ratio of the change in distance over a finite *dt*:
( *s*(2 + *dt*) - *s*(2) ) / *dt* = ( (2 + *dt*)³ - 2³ ) / *dt* <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

After algebraic expansion and simplification, much of the complexity (terms with *dt*) cancels out as *dt* approaches 0 <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. What remains is a simple expression: 3 * 2² = 12 <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. This means the slope of the line tangent to the graph at *t* = 2 is 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. More generally, the derivative of *t*³ is 3*t*² <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

This process simplifies the problem by allowing the disregard of terms that vanish as *dt* approaches zero <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>, which is at the heart of why [[calculating_derivatives_and_their_applications|calculus becomes useful]] <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## Addressing the Paradox

If the distance function is *s*(*t*) = *t*³, the derivative (velocity) is 3*t*² <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. At *t* = 0, the derivative is 3(0)² = 0 <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. Visually, the tangent line to the graph at *t* = 0 is perfectly flat <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This suggests the car is not moving at *t* = 0. However, if it's not moving at *t* = 0, when does it start moving? This highlights the issue with the question itself <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

The derivative being 0 means that the best constant approximation for the car's velocity *around* that point is 0 m/s <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For example, between 0 and 0.1 seconds, the car *does* move (0.001 m), resulting in a small average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative of 0 simply means that for increasingly smaller time nudges, the ratio of meters per second approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. It does not mean the car is static, as approximating its movement with a constant velocity of 0 is just an approximation <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

When people refer to the derivative as an "instantaneous rate of change," it should be understood as a conceptual shorthand for the *best constant approximation for rate of change* <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.