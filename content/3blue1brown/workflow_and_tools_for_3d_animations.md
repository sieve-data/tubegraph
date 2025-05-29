---
title: Workflow and tools for 3D animations
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

The 3Blue1Brown animated videos are created using a custom [[using_python_for_animation_and_interactivity | Python library]] named Manim <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This library is programmatic and highly bespoke <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The development of Manim began during the creator's undergrad, aiming to better illustrate [[animating_mathematical_functions | mathematical functions]] as transformations <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Manim: The Core Animation Library

Manim is an open-source tool, with all video code openly visible on GitHub <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. There are two main versions:
*   **Original Version:** Developed by the creator, this version has evolved to be more interactive and performant over the years <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. It is the version typically used for 3Blue1Brown videos <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Manim Community Version:** Created by a community of developers who forked the original repository, this version is more robust, with better testing, documentation, and responsiveness to issues and pull requests <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>, <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>. It is generally recommended for new users <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Workflow for Animation Development

The animation workflow is highly interactive and relies on a specific setup:

### Text Editor and Terminal
*   **Text Editor:** Sublime Text is used for writing [[using_python_for_animation_and_interactivity | Python]] code <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Interactive Python Terminal:** A Python terminal, integrated via the Terminus extension in Sublime, communicates directly with the scene being created <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>. This allows for immediate testing of code lines <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Iteration and Live Previews
*   **Keyboard Shortcuts:** Custom keyboard shortcuts (e.g., Command R on Mac) are used to copy and run selected code directly in the terminal, providing immediate visual feedback <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Checkpoint Pasting:** For long scenes, a "checkpoint paste" feature allows running a section of code by reverting the scene to its state at the beginning of that section <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This hybridizes the text file workflow with a Jupyter notebook-like experience <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Scene Structure
*   All scenes are defined as Python classes, with the rendering code residing within a `construct` method <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   Scenes can become very long, with code organized as a single large pile of Python, sharing local variables <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Key Manim Features and Concepts

*   **Mobjects:** "Mathematical objects" are the base for visual elements <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. Many are "vectorized mobjects" (`VGroup`), optimizing rendering for curves and shapes with stroke thickness <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>, <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>, <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   **Adding Objects:** Objects are added to the scene using `self.add()` to make them appear <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Animations (`.play()`):** The `.play()` method is used to animate transformations and other actions on objects <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
    *   **`write` animation:** Simulates text being written on screen <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   **`transform` animation:** Allows any object to visually transform into another <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Rate Functions:** Control the easing and speed of animations. `smooth` is the default for a fluid look (cubic Bezier) <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>, <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. `linear` provides a constant speed, useful when the animation represents a specific mathematical behavior <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>, <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Updaters:** Functions that are called on objects at every frame, allowing for continuous movement or changes based on other elements in the scene <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>, <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>, <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
*   **[[visualizing_transformations_in_three_dimensions | 3D]] Capabilities:**
    *   Scenes can be rendered in [[vectors_in_two_and_three_dimensions | 3D]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Objects by default exist on the XY plane in [[vectors_in_two_and_three_dimensions | 2D]] <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>, <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
    *   `3D axes` can be added to establish a coordinate system <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>, <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.
    *   Camera control: The camera frame can be animated to pan or rotate the view of the scene <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>, <a class="yt-timestamp" data-t="00:34:26">[00:34:26]</a>, <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. Custom shortcuts exist to capture the current camera position <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>.
*   **LaTeX Integration:** LaTeX expressions can be rendered as objects within the scene, allowing for precise control over mathematical formulas <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>, <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>. Specific parts of LaTeX objects can be individually colored or manipulated <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>, <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>, <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>. `fix_in_frame` can be used to glue objects to the camera frame so they don't move with camera pans <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>, <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.
*   **Pre-built Animations and Utilities:** Manim includes various functions for common effects like `glow_dot` (a point that moves and glows) <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>, <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>, and `TracingTail` (a fading tail following an object) <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>, <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>.
*   **Object Manipulation:** Objects can be shifted, styled (e.g., `set_stroke`, `set_opacity`, `color_gradient`), and grouped (`VGroup`) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>, <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>, <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>.
*   **Python Specifics:** The `*` operator can be used to unpack iterables as arguments to functions <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. The `zip` function is used to iterate through multiple lists in parallel <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>, <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.

## Animating the Lorenz Attractor

The Lorenz Attractor, a key concept in chaos theory, is used as a demonstration <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   It is derived from a set of differential equations in [[vectors_in_two_and_three_dimensions | 3D]] <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   To obtain points for plotting, the `SciPy integrate` library's `solve_initial_value_problem` function is used to solve the numerical ordinary differential equations (ODE) <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>, <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>, <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Chat GPT can assist in generating boilerplate code for this <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Multiple curves are generated from slightly varied initial conditions to illustrate chaotic divergence <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>, <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
*   The evolution time of the simulation can be set independently from the animation runtime <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>, <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.

## Rendering and Post-Production

Once a scene is complete, it is rendered to an MP4 file <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>.
*   **Rendering Command:** Manim scenes are typically rendered from the command line using `manim <file.py> <SceneName>` <a class="yt-timestamp" data-t="00:42:14">[00:42:14]</a>, <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>. Parameters like `pre-run` (to estimate time and catch errors) and `write to file` (`-w`) are common <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>, <a class="yt-timestamp" data-t="00:42:46">[00:42:46]</a>.
*   **Resolution:** Rendering is often done at 4K resolution, which can increase rendering time <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>.
*   **Post-Production:** The rendered MP4 file is then imported into video editing software like Final Cut for final editing <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>, <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>.

**External Tools and Resources:**
*   **MathPix:** An OCR tool used to convert screenshots of equations into LaTeX expressions and SVGs <a class="yt-timestamp" data-t="00:44:53">[00:44:53]</a>, <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>.
*   **GitHub:** All code for 3Blue1Brown videos and the Manim tool itself are available on GitHub <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>, <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>, <a class="yt-timestamp" data-t="00:50:42">[00:50:42]</a>.
*   **SciPy:** A Python library used for numerical operations, including solving differential equations <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   **Documentation and Examples:** The Manim Community version offers better documentation <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>. Example scenes within the Manim library itself provide a good starting point for understanding available functionalities <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>, <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>, <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a>.
*   **AI Assistants:** GitHub Copilot is available for auto-completion but the creator prefers simpler tools due to his familiarity with Manim's codebase <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>, <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>, <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.