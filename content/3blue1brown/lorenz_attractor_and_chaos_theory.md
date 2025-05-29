---
title: Lorenz Attractor and chaos theory
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

The Lorenz Attractor is a "bizarre shape" that emerged in the early history of [[Chaos: Making a New Science | chaos theory]] <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. It is derived from a set of deterministic differential equations in three dimensions <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. These equations describe how a point in 3D space should change at any given moment in time <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>, <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. The system includes tunable parameters that, when adjusted, can yield interesting diagrams <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>, <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

The Lorenz Attractor is considered "nice fodder for animation" <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Its characteristics are often illustrated by plotting the paths of multiple points starting from very slightly different initial conditions <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

## Characteristics of the Lorenz Attractor

The system's behavior is inherently chaotic <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. While points starting extremely close to each other will initially evolve similarly, they soon diverge, eventually appearing to follow "completely different things" <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>, <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>, <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. This sensitive dependence on initial conditions is a hallmark of chaos.

Despite this unpredictability, the Lorenz Attractor possesses a surprising property: regardless of where a point starts, its trajectory will eventually be "attracted to a certain shape" <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>, <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>, <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. Unlike other differential equations that might attract to a single point, blow up to infinity, or settle into a cycle, the Lorenz Attractor is a "strange attractor" <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>, <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. This shape is not simple and exhibits a [[Fractal Dimension and Its Application in Nature | fractal nature]] <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>, <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.

The paradoxical nature of the Lorenz Attractor lies in its combination of unpredictability and predictability: one knows that the trajectory will be confined to a specific subset of 3D space, but the exact location within that subset remains unknown <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>, <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>.

## Animation with Manim

The Lorenz Attractor is animated using a custom Python library called Manim <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The animation workflow involves:

1.  **Setting up the 3D environment**: While Manim defaults to 2D for pedagogical reasons, the Lorenz Attractor requires 3D axes <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>, <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. Objects are placed on an XY plane by default unless specified <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
2.  **Solving the differential equations**: A Python function describes the Lorenz system's differential equations, which define the derivative of the state (XYZ coordinates) at a given time <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>, <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. SciPy's numerical ODE solver (`solve_initial_value_problem`) is used to find solutions based on initial conditions <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>, <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>, <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
3.  **Generating curves and points**: The solutions from the ODE solver provide a set of points in 3D space <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>, <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. These points are interpreted by Manim as a curve using `set_points_as_corners` <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. The `coords_to_points` function converts mathematical coordinates to Manim's rendering system <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>, <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.
4.  **Animating the evolution**:
    *   The `ShowCreation` animation type is used to draw the curve over time, representing the system's evolution <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>, <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
    *   Crucially, for physically accurate representation, the `rate_function` for `ShowCreation` is set to `linear` instead of the default `smooth` (which applies a cubic Bezier easing) <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>, <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>, <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>, <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
    *   Multiple curves can be animated simultaneously by iterating through a list of initial conditions and colors <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>, <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>, <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. The `zip` function in Python is used to pair initial states with corresponding colors <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
    *   "Glow dots" are used to mark the endpoints of each curve, updating their position with an `updater` function at every frame <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>, <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>, <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>, <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
    *   A "Tracing Tail" effect can be applied to the dots, creating a fading trail behind them that smoothly transitions from full opacity to zero opacity and stroke width <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>, <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>, <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
5.  **Camera movement**: The camera frame can be animated using `frame.animate.reorient` to slowly pan and rotate, providing a better 3D perspective <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>, <a class="yt-timestamp" data-t="00:34:26">[00:34:26]</a>.
6.  **Displaying equations**: LaTeX objects can be rendered on screen using `self.add(MathTex(...))` <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. These can be "fixed in frame" to stay in view regardless of camera movement <a class="yt-timestamp" data-t="00:45:16">[00:45:16]</a>. Manim also allows selective styling and manipulation of individual characters or variables within a LaTeX expression <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>, <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>. Tools like MathPix can generate LaTeX code from images <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.

## Related Concepts

*   **Differential Equations**: The Lorenz Attractor is derived from a system of differential equations <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Initial Conditions**: The chaotic nature of the Lorenz Attractor is demonstrated by how slightly varied initial conditions lead to widely divergent paths <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
*   [[Attracting and Repelling Cycles in Functions | Attractors]]: While some systems are attracted to points or cycles, the Lorenz system is attracted to a "strange attractor" <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>, <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>.
*   [[Fractal Dimension and Its Application in Nature | Fractal Geometry]]: The strange attractor of the Lorenz system possesses a fractal nature <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.

### Further Reading

*   **Book**: *Chaos: Making a New Science* by James Gleick <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
*   **Video**: Veritasium video on the Lorenz Attractor <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>