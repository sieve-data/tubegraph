---
title: Animating mathematical functions
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

Manim is a custom Python library specifically designed for animating mathematical concepts and functions programmatically. It allows for highly bespoke and detailed visual explanations, forming the backbone of educational videos by 3Blue1Brown <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Manim Versions and History

There are two primary versions of Manim:
*   **Original Manim** The development of Manim is deeply intertwined with the history of the 3Blue1Brown channel <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It began as a personal coding project to better illustrate [[complex_functions_and_transformations | mathematical functions as transformations]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The tool continuously improved alongside the creation of more videos <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The underlying code for videos and the Manim tool itself are open source and available on GitHub <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Manim Community Version** A community of users forked the original Manim repository to create a more robust version with better documentation, testing, and active management of issues and pull requests <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This version is generally recommended for new users <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The original developer's version has evolved to be more interactive and performant <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Workflow and Tools

Manim operates entirely within a Python environment <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Text Editor** Users typically write Manim code in a text editor like Sublime Text <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Scenes and Objects** All animations are structured around "scenes," which are Python classes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. The core rendering logic resides within a `construct` method inside these classes <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Objects are called "mobjects" (mathematical objects), many of which are vectorized (e.g., `Circle`, `Square`, `Text`, `VGroup`) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Interactive Development** A key part of the workflow is an interactive Python terminal that communicates directly with the scene <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This allows for immediate testing of code snippets, such as moving a `square.shift(RIGHT)` <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, without rendering a full video <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This interactive mode, which allows running sections of code and seeing immediate visual feedback, is a significant workflow improvement <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>.
*   **Animations**
    *   **Adding Objects:** Objects can be added to the scene using `self.add()` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   **Playing Animations:** The `self.play()` method is used to animate changes to objects <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Common animations include `Write` (making text appear as if being written) <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a> and `Transform` (morphing one object into another) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   **Rate Functions:** Animations have a `rate_function` attribute, defaulting to `smooth` (a cubic Bezier function) <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This controls the easing of the animation, making it look natural <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. For mathematical phenomena, a `linear` rate function might be necessary to accurately represent the underlying behavior <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Rendering:** Once a scene is complete, it can be rendered into an MP4 video file (e.g., at 4K resolution) <a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a>. This is typically done via a command-line interface <a class="yt-timestamp" data-t="00:42:14">[00:42:14]</a>.

## Illustrating the Lorenz Attractor

The Lorenz Attractor, a key concept in chaos theory, provides an excellent example of Manim's capabilities <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. It's derived from a set of three-dimensional differential equations <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Steps to Animate:
1.  **3D Environment:** Manim scenes default to 2D, but can be set up with 3D axes <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Objects are placed using `coordinates to points` (or `c2p`) to map mathematical coordinates to Manim's internal display system <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
2.  **Solving Differential Equations:** Python libraries like SciPy's `solve_ivp` (initial value problem solver) can be used to generate the trajectory points for the Lorenz equations <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. The equations have tunable parameters (e.g., sigma, rho, beta) that influence the shape of the attractor <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
3.  **Plotting Curves:** The generated points are used to create `VMobject` curves (vectorized mathematical objects) that represent the trajectory <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
4.  **Animating Evolution:** The `ShowCreation` animation type makes the curve appear as it evolves over time <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. It's crucial to set the `rate_function` to `linear` for accurate representation of the system's dynamics <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
5.  **Visualizing Chaos:** To illustrate the chaotic nature of the Lorenz Attractor, multiple curves are plotted with slightly different initial conditions <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Initially, they stay close, but rapidly diverge, showcasing the system's sensitivity to initial conditions <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.
6.  **Tracking Points:** `GlowDot` objects can be attached to the endpoints of the curves and updated frame-by-frame to follow the evolving trajectory <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>. This uses an `updater` function that moves the dot to the curve's current endpoint <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.
7.  **Tracing Tails:** A `TracingTail` function can be applied to the dots, creating a fading tail effect that visually represents the path traced by the points, emphasizing the divergence <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.
8.  **Camera Movement:** For 3D visualizations, the camera can be animated to pan and rotate throughout the scene, providing depth and perspective <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>. Camera positions can be captured and pasted into the code <a class="yt-timestamp" data-t="00:34:13">[00:34:13]</a>.

## Displaying Equations and Text

Manim can render LaTeX expressions, which are essential for presenting mathematical equations <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **LaTeX Objects:** Equations are created as `LaTeX` mobjects <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Positioning:** For 3D scenes, equations can be "fixed in frame" to appear glued to the camera view, often in a corner <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>.
*   **Styling:** Specific parts of a LaTeX equation (e.g., variables like X, Y, Z) can be isolated and colored, allowing for visual emphasis and control over individual elements <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>.
*   **Advanced Text Operations:** Manim includes functions like `TransformMatchingStrings` which can automatically animate the rearrangement of terms in equations or even perform anagrams, simplifying complex text animations <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>. Other features like `flash_around` and `indicate` can highlight specific characters or sections of text <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>.

## Resources for Learning

*   **GitHub Repositories:** All code for 3Blue1Brown videos is openly available on GitHub at `github.com/3b1b/videos` <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>. This serves as a vast resource for understanding available functionality <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Example Scenes:** The Manim library includes example scenes that demonstrate various operations and animations <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>.
*   **Documentation:** The Manim Community version has robust documentation <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>.
*   **Community:** For further learning and support, communities around Manim are active <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.