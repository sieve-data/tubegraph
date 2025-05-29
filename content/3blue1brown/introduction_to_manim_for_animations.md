---
title: Introduction to Manim for animations
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

Manim is a custom Python library used for creating programmatic and bespoke animations, primarily for [[visualizing_mathematical_concepts | illustrating mathematical functions as transformations]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It is widely known for animating the videos of 3Blue1Brown <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## History and Evolution <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>
The project began when its creator was finishing undergrad, as a coding project to better illustrate mathematical functions <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The tool evolved significantly with the creation of more videos, leading to a continuous cycle of improvement and new content <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Workflow improvements over the years have made complex animations, like those seen in recent hologram videos, much easier to produce <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The code for Manim videos is openly visible on GitHub <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, and the underlying Manim tool itself was also made open source <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Manim Versions <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
There are two main versions of Manim:
*   **Original Version:** The creator's personal version, which has made changes over the years to be more interactive and performant <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Manim Community Version:** Developed by a community of users who forked the original repository <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This version is more robust, attentive to issues and pull requests, and features better testing and documentation <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. It is generally recommended for new users <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

> [!NOTE] [[differences_between_manim_versions | Differences between Manim versions]]
> While the creator often uses his own version for demonstrations, the community version is recommended for those seeking a more documented and tested experience <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Workflow and Tools <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
The Manim workflow involves [[using_python_for_animation_and_interactivity | writing Python code]] to generate animations.

### Development Environment <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
*   **Text Editor:** Typically a text editor like Sublime Text is used to write Python code for the scene <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Interactive Python Terminal:** Manim integrates with an interactive Python terminal that communicates directly with the scene <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This allows for immediate testing of code lines and interactions with objects on the screen <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Keyboard Shortcuts:** Custom shortcuts, like Command R, can be set up to copy and run selected code directly into the interactive terminal, providing immediate visual feedback <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. This significantly speeds up the iteration cycle compared to repeatedly rendering from the command line <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>.
*   **Checkpoint Paste:** For longer scenes, a feature called "checkpoint paste" allows the user to run a specific section of code by reverting the scene to a cached state from an earlier point <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This makes iterative development on specific parts of a long animation more efficient <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Debugging:** While similar to Jupyter notebooks in interactivity, the creator prefers a single text file for the scene combined with interactive scripting <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. A "cursed" `globals().update(locals())` line was historically used as a hack to resolve scope issues in the embedded IPython environment during interactive scene development <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. A more explicit and robust way is to pass variables as arguments to functions, especially with `lambda` functions <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>.

### Final Output <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>
Once satisfied with the scene, it is rendered into an MP4 video file, often in 4K resolution <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. The rendering process can be initiated from the command line, with options to pre-run for error checking and time estimation <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>.

> [!TIP] [[workflow_and_tools_for_3d_animations | Workflow and tools for 3D animations]]
> The interactive shell and custom shortcuts significantly enhance the workflow for scene development, allowing for rapid iteration and real-time adjustments to animations <a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>. The creator plans to document his specific Sublime scripts for others to replicate the workflow in their preferred text editors <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.

## Core Concepts in Manim

### Scenes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>
All animations are structured as Python classes called "scenes". The code that renders the animation is placed within a method called `construct` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Mobjects (Mathematical Objects) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>
Manim refers to all visual elements as "mobjects" (mathematical objects) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. Many mobjects are "vectorized," meaning they are described by points and can have properties like stroke thickness and fill <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

#### Adding Objects to a Scene <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   To make an object appear, it needs to be added to the scene, e.g., `self.add(square)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   By default, most objects appear in the center of the screen <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### Animations <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
The `play` method is used to execute animations <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

*   **`Write`:** Animates an object, such as text, as if it is being written onto the screen <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **`Transform`:** Allows one object to smoothly morph into another <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. Manim attempts to match underlying strings or geometric data for smooth transitions <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.
*   **Rate Functions:** Control the easing or speed of an animation.
    *   `smooth`: The default, providing a visually smooth start and stop <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   `linear`: Provides a constant speed, useful when the mathematical behavior being represented requires it <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Camera Control:** The camera can be animated to pan or reorient during a scene, which is especially useful for maintaining the illusion of depth in 3D animations <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.
*   **`TracingTail`:** A specialized animation that creates a fading trail behind a moving object <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>.

### Working with LaTeX <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>
Manim supports rendering LaTeX expressions into objects on the screen <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.
*   **`LaTeX` object:** Takes a LaTeX string and renders it <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Positioning:** Objects can be fixed to the camera frame (e.g., in a corner) even in a 3D scene using `fix_in_frame()` <a class="yt-timestamp" data-t="00:39:52">[00:39:52]</a>.
*   **Highlighting parts:** Manim allows for individual elements within a LaTeX expression (like variables or symbols) to be isolated, colored, or animated independently <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>. This is useful for [[animating_mathematical_functions | highlighting specific mathematical concepts]] <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.
*   **MathPix:** A useful tool for converting snapshots of equations into LaTeX code or SVGs <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>.

## Example: The Lorenz Attractor <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
Manim is well-suited for [[animating_mathematical_functions | animating mathematical functions]] like the Lorenz Attractor <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

The Lorenz Attractor is a bizarre shape from the early history of chaos theory, generated from a set of three-dimensional differential equations <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. It demonstrates how infinitesimally small differences in initial conditions can lead to vastly different outcomes over time <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Despite the chaotic divergence, all points are attracted to a specific "strange attractor" shape <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>.

To animate the Lorenz Attractor in Manim:
1.  **3D Axes:** Set up 3D axes as the base for the animation <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
2.  **Differential Equation Solver:** Use a numerical ODE solver (e.g., from SciPy) to get points for the Lorenz system's evolution <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. Chat GPT can assist in generating boilerplate code for this <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
3.  **Create Curves:** Convert the calculated points into Manim `VMobject` curves <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
4.  **Coordinate Transformation:** Use `axes.coords_to_point` to map mathematical coordinates to Manim's rendering space <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
5.  **Animate Creation:** Use `ShowCreation` to animate the drawing of the curves <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
6.  **Real-time Endpoints:** Use an `updater` function to attach and move "glow dots" to the end of each evolving curve, tracking its path <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
7.  **Illustrate Chaos:** Create multiple curves with slightly different initial conditions and assign distinct colors to visualize their divergence over time <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. The `color_gradient` function can generate a range of colors for multiple paths <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
8.  **Visual Effects:** Curves can be made to fade out over time using `FadeOut` or `set_opacity(0)` combined with `TracingTail` to leave a decaying visual trail <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>.

## Learning Resources <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>
*   **Example Scenes:** Manim includes example scenes demonstrating various functionalities <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>.
*   **GitHub Repository:** All code for 3Blue1Brown videos is available on GitHub (github.com/3b1b/videos) <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. This provides practical examples of how different functionalities are used <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Documentation:** The Manim Community Version offers much better documentation compared to the original <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>.
*   **Text Editor Features:** Features like auto-completion (via Language Server Protocols) in text editors can help discover available functions and methods <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>.