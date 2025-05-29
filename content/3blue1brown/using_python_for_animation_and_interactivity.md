---
title: Using Python for animation and interactivity
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

The primary tool used for creating animations in 3Blue1Brown videos is a custom Python library called [[introduction_to_manim_for_animations | Manim]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This library is programmatic and highly bespoke <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The initial motivation for developing Manim was to illustrate mathematical functions as transformations more effectively <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The tool has continuously improved alongside video production, allowing for increasingly complex and visually appealing animations <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Versions of Manim

There are two main versions of Manim <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>:

1.  **Original Version**: This version's history is deeply intertwined with the channel's development <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The code for all videos, and the underlying Manim tool, are open-source and visible on GitHub <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  **Manim Community Version**: A community of developers forked the original repository to create a more robust tool for others <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This version features better testing, documentation, and is more attentive to issues and pull requests <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. It is generally recommended for new users <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The original version has seen continuous development by its creator, adding more interactive and performant features over the years <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## [[workflow_and_tools_for_3d_animations | Workflow and Interactivity]]

The animation process in Manim involves writing Python code in a text editor (like Sublime Text) and interacting with a Python terminal <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Setting Up a Scene
All scenes in Manim are defined as Python classes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The rendering code resides within a specific method of that class, typically named `construct` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Objects, referred to as "mobjects," can be added to a scene. Most objects default to being in the center of the screen <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Interactive Development
A significant aspect of the [[workflow_and_tools_for_3d_animations | workflow]] is the interactive shell, allowing developers to highlight and run specific sections of code to immediately see the visual output <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>. This dramatically speeds up the iteration cycle compared to rendering the entire video file each time <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>.

To facilitate this, a "checkpoint paste" feature allows the scene to revert to a cached state before running a specific code section, mimicking the behavior of a Jupyter notebook within a single text file <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Animations and Transformations
Manim allows for various animations and transformations:
*   **`play` method**: Used to animate actions on objects, such as writing text or transforming shapes <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **`rate_function`**: Controls the easing or speed profile of an animation. The default is a smooth, cubic Bezier curve, but it can be set to `linear` for consistent speed <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Transformations**: Almost anything can be transformed into anything else <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. For example, a character from text can be transformed into a circle <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Manim also includes features like [[animating_mathematical_functions | anagram animators]] that automatically match and move letters between strings <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.

### [[visualizing_transformations_in_three_dimensions | 3D Visualizations]]
While most scenes are typically in 2D to simulate a blackboard <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>, Manim supports 3D rendering. Objects exist in 3D space by default, even if viewed on a 2D plane <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

For [[applications_of_3d_transformations_in_computer_graphics_and_robotics | 3D scenes]], features include:
*   **3D Axes**: Used to establish a [[graphical_analysis_using_a_graphing_calculator | coordinate system]] <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **`coords_to_points`**: A function to convert coordinates from the axis system to Manim's internal coordinate system <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Interactive Camera**: Allows real-time manipulation of the camera angle, which can be saved to code for animated panning <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. This is crucial for maintaining the illusion of depth on a 2D screen <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.

#### Example: Lorenz Attractor
The Lorenz Attractor is a classic example from chaos theory that requires 3D visualization <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. It's derived from a set of differential equations in three dimensions, defining how a point changes over time <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

To animate it:
1.  **Solve ODEs**: Python libraries like SciPy's `integrate` can solve the differential equations to get a sequence of points <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. Chat GPT was used to find boilerplate code for this <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
2.  **Create Curves**: These points are then used to draw curves within Manim's 3D coordinate system <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
3.  **[[visualizing_mathematical_concepts | Visualizing]] Chaos**: By using multiple initial conditions that are very close to each other, Manim can illustrate how the paths diverge over time, demonstrating the chaotic nature of the system <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
4.  **Tracing Tails**: A "Tracing Tail" function can be applied to individual dots to create a fading trail effect, visualizing the recent path of each point <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.

### Rendering to MP4
Once a scene is complete, it can be rendered to an MP4 file <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>. The process involves calling Manim from the command line, specifying the Python file and scene to render <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>. Parameters can be added for pre-running (to estimate time and catch errors) or writing to a file <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>.

## Advanced Features and Tips

*   **`glow_dot`**: A built-in function to create points that move and have a pleasant glow effect <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   **Updater Functions**: These functions can be added to objects to automatically update their properties (e.g., position) on every frame of the animation, allowing them to track other objects <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
*   **LaTeX Integration**: Manim can render LaTeX expressions directly into the scene <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. Tools like MathPix can convert equations from images into LaTeX code <a class="yt-timestamp" data-t="00:44:53">[00:44:53]</a>. Specific parts of LaTeX expressions can be indexed and controlled (e.g., colored differently) <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>.
*   **`global().update(locals())` (Cursed Line)**: A hack sometimes used in interactive sessions to make local variables accessible globally within a function, bypassing a bug in IPython embeds used by Manim <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>. A cleaner alternative is to pass variables explicitly as function arguments with default values <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>.
*   **`*` (Asterisk) Operator**: In Python, the asterisk operator (`*`) unpacks an iterable (like a list or tuple) into separate arguments when calling a function <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **`zip` function**: Stacks two or more lists in parallel, allowing for simultaneous iteration through their elements <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
*   **Color Gradients**: Can be used to create smooth transitions between colors <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.

## Resources
*   **Manim GitHub Repository**: All code for past and present 3Blue1Brown videos is openly visible on GitHub <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. The specific workflow and Sublime scripts will be documented there <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.
*   **Manim Community Documentation**: Provides better documentation for new users <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>.
*   **Example Scenes**: Manim includes example scenes that demonstrate available operations and functionality <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>.