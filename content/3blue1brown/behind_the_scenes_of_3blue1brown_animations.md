---
title: Behind the scenes of 3Blue1Brown animations
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

The animations for 3Blue1Brown videos are created using a custom, bespoke [[python_for_animation | Python]] library called [[manim_animation_library | Manim]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This library allows for programmatic creation of visuals, offering a unique workflow for [[creating_mathematical_animations | mathematical animations]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The [[manim_animation_library | Manim]] Animation Library

[[manim_animation_library | Manim]] originated as a personal coding project during the creator's undergraduate studies, aimed at better illustrating mathematical functions as transformations <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The tool evolved incrementally with each new video produced <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Modern versions allow for complex visuals, which would have been significantly harder to create just a few years prior due to workflow improvements <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Versions of [[manim_animation_library | Manim]]
There are currently two main versions of [[manim_animation_library | Manim]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>:
*   **Original Version**: Developed by the channel's creator, this version is continuously updated for performance and interactivity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. All code for past videos is openly visible on GitHub <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Manim Community Version**: This version was forked by a community of users who desired a more robust, well-documented, and tested tool <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. It is generally recommended for new users due to its better documentation and testing <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Animation Workflow

The animation process primarily uses [[python_for_animation | Python]] within a text editor like Sublime Text <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, interacting with a live Python terminal <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Scene Creation
All scenes are structured as Python classes, with rendering code residing within a `construct` method <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Objects like circles and squares can be added and manipulated within the scene <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Interactive Development
A key aspect of the workflow is the ability to run code snippets immediately and see the visual output <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. A keyboard shortcut copies selected code to the terminal for instant execution, allowing for rapid iteration <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Managing Long Scenes
Scenes can be very long, often consisting of a "big pile of [[python_for_animation | Python]]" code <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. To facilitate development within these long scenes, a "checkpoint paste" feature is used <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows developers to run a specific section of code, with the scene reverting to its state at the beginning of that section, similar to a Jupyter notebook but within a single text file <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Animation Primitives
[[manim_animation_library | Manim]] includes built-in functions for common animations:
*   **Adding Objects**: `add` makes an object appear on screen <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **`play` Method**: Used for animations that unfold over time <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **`Write`**: Simulates text or objects being written onto the screen <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **`Transform`**: Allows any object to smoothly morph into another <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Rate Functions**: Control the easing or speed profile of animations, defaulting to a smooth cubic Bezier ("smooth") or allowing for linear transitions <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. Attention to these details enhances the visual quality of animations <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### Working with 3D and Coordinates
By default, objects exist on the X-Y plane <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. For [[visualization_of_3d_vector_transformations | 3D visualizations]], `3D axes` can be added <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Manim's coordinate system can be aligned with arbitrary axes using functions like `coords_to_points` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. The camera can be slowly panned and reoriented throughout an animation to enhance the perception of depth in 3D scenes <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.

### Example: Animating the Lorenz Attractor
The Lorenz Attractor, important in chaos theory, is a dynamic system defined by [[threedimensional_linear_transformations | differential equations in three dimensions]] <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. To animate it in [[manim_animation_library | Manim]]:
1.  **Mathematical Setup**: A Python function describes the differential equation <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. SciPy's numerical ODE solver is used to generate a series of points representing the solution over time from an initial condition <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
2.  **Rendering the Curve**: The generated points are used to create a `VMobject` (vectorized mathematical object) curve, drawing lines between them <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
3.  **Illustrating Chaos**: To show chaotic divergence, multiple curves are generated from slightly different initial conditions <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. These are often colored differently for distinction <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
4.  **Tracking Points**: "Glow dots" are added to track the end points of the curves, using an "updater" function that repositions the dots on each frame <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
5.  **Visual Effects**:
    *   Curves can be made to fade out over time, leaving only the dots <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.
    *   A "Tracing Tail" effect can be applied to the dots, creating a fading trail that follows their movement <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. This helps visualize the path even as the main curve disappears.
    *   Adjusting the initial conditions to be extremely close together demonstrates how long it takes for the chaotic divergence to become apparent <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

### Rendering to Output File
Once a scene is finalized, it is rendered into an MP4 video file, often at 4K resolution <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. This is typically done via a command-line call to [[manim_animation_library | Manim]], which can pre-run the animation to estimate time and catch errors <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>. The iterative workflow of highlighting code and seeing immediate results is a significant improvement over constantly rendering full MP4s <a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>.

### LaTeX Integration
[[manim_animation_library | Manim]] can render LaTeX expressions directly into the scene as objects <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. Tools like MathPix can convert equations from bitmaps to scalable vector graphics (SVGs) and provide their LaTeX code <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>. Variables within LaTeX expressions can be indexed and colored <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>. Special `transform` methods attempt to match underlying strings to create smooth animations when equations are rearranged <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.

## Code Access and Community
All code used for 3Blue1Brown videos is available on GitHub (github.com/3b1b/videos) <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>. This allows users to examine existing functionality <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. While the [[manim_animation_library | Manim]] community version has extensive documentation <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>, users of the original [[manim_animation_library | Manim]] can explore the `animation` folder within the library to see available functions <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. Text editor features like language servers (e.g., Pi LSP in Sublime) provide auto-completion to assist in discovering functions <a class="yt-timestamp" data-t="00:51:24">[00:51:24]</a>.

> [!NOTE]
> The workflow shown features a "cursed" line of code (`globals().update(locals())`) <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. This was a hack to work around a bug in the IPython embed used, ensuring that locally defined variables were accessible within functions, similar to how Jupyter Notebooks handle scope <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>. A better, more explicit approach would be to pass such variables as arguments to functions <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>. This specific bug, however, appears to have been resolved in later versions of the [[manim_animation_library | Manim]] environment <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

The creator plans to document the specific Sublime scripts and workflow on the GitHub repository for those interested in replicating it in other text editors <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.