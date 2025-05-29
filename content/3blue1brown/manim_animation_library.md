---
title: Manim animation library
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

Manim is a custom [[python_for_animation | Python library]] used to [[creating_mathematical_animations | animate videos]] for the 3Blue1Brown YouTube channel <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It is a programmatic and bespoke tool designed for illustrating mathematical concepts <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This article offers a [[behind_the_scenes_of_3blue1brown_animations | behind the scenes of 3Blue1Brown animations]] look at Manim, its workflow, and capabilities <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## History and Versions

Manim's history is deeply intertwined with the 3Blue1Brown channel <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The creator began the project while finishing his undergraduate degree, aiming to illustrate mathematical functions as transformations through a scrappy bit of Python code <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. As more videos were made, the tool continuously improved <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Modern visuals, such as those in a video on holograms, are dramatically easier to create now due to workflow improvements <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

The Manim code, including all video-specific code, is openly visible on GitHub <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The underlying tool itself was also made open source <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

There are currently two main versions of Manim <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>:
*   **Original/Creator's Version**: The version actively used and developed by the creator, continuously improved for interactivity and performance <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Manim Community Version**: A fork created by a community of users who wanted a more robust tool with better issue management, pull request attention, testing, and documentation <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This version is generally recommended for new users <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Workflow and Scene Creation

Manim operations are entirely in [[python_for_animation | Python]] <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. A typical workflow involves:

1.  **Defining a Scene**: All animations take the form of a Python class, with rendering code residing in a `construct` method <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Adding Objects**: Mathematical objects (mobjects) like circles, squares, or text can be added to the scene <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Most objects default to being in the center <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Interactive Development**: The creator uses Sublime Text as a text editor <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, with a Python terminal integrated to interact with the scene <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    *   Commands can be sent directly to the scene, such as `square.shift` to move an object <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   A custom keyboard shortcut (e.g., Command+R) copies and runs selected code, providing immediate visual feedback <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   For longer scenes, a "checkpoint paste" feature allows running a specific section of code by reverting the scene to its state at the beginning of that section, similar to a Jupyter notebook <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

> [!CAUTION] The "cursed line" `globals().update(locals())` <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a> was a hack to address a scope bug in the embedded IPython environment, allowing local variables to be recognized by functions and list constructors. While it appears the underlying bug might be resolved, explicit argument passing is the better practice <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>.

4.  **Animating Objects**: The `play` method initiates animations, often applying transformations to objects over time <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Manim aims to make aesthetically pleasing animations easy to create <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

    *   **Rate Functions**: Control the speed profile of animations. The default `smooth` function uses a cubic Bézier curve for fluid motion, while `linear` provides a constant speed <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
    *   **Transformations**: A core philosophy is that "anything can transform into anything" <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. Objects can morph between different shapes <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   **Custom Effects**: Includes baked-in functions like `Write` (for text appearing as if written <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>), `GlowDot` (for points with an ambient glow <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>), and `TracingTail` (for a fading trail behind moving objects <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>).

5.  **Rendering to MP4**: Once satisfied, the scene can be rendered to an MP4 file using a command-line utility. Parameters control quality (e.g., 4K), pre-running for error checking, and opening the file in the OS file system <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>.

## Capabilities and Examples

### Lorenz Attractor Animation

Manim is well-suited for [[visualization_of_3d_vector_transformations | visualizing 3D vector transformations]] and complex systems. The Lorenz Attractor, a famous chaotic system derived from differential equations, serves as a prime example <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

*   **3D Axes**: Manim scenes exist in 3D by default, though most pedagogical content uses 2D to simulate a blackboard <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. For the Lorenz Attractor, 3D axes are necessary <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Numerical Integration**: Python libraries like SciPy's `solve_ivp` (initial value problem solver) can be integrated to generate point data for the attractor's evolution <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   **Animating Evolution**: Curves representing the paths of points can be drawn, with optional `GlowDot` objects tracking their endpoints <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. The `rate_function` is set to `linear` to accurately represent the mathematical evolution <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Illustrating Chaos**: Multiple curves starting from slightly different initial conditions can be animated, demonstrating their eventual divergence due to chaotic behavior <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. Color gradients can differentiate paths <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
*   **Camera Control**: The camera can be animated to pan and rotate during 3D scenes, maintaining the illusion of depth <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.
*   **Fading Trails**: `TracingTail` objects provide a visual effect where the curves fade out, leaving only the moving dots, clearly showing the chaotic spread <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.

### LaTeX Integration

Manim supports LaTeX for rendering mathematical equations <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Equation Objects**: LaTeX expressions can be created as `LaTeX` objects and added to the scene <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.
*   **Camera Fixed Placement**: Equations can be "fixed in frame" to appear glued to the camera frame, useful for overlays in 3D scenes <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.
*   **Highlighting Parts**: Specific parts of a LaTeX equation can be indexed and colored (e.g., coloring all 'x's red) or individually animated using functions like `flash_around` or `indicate` <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>.
*   **Transforming Equations**: Manim can transform between different LaTeX expressions by matching strings, allowing for animations that smoothly rearrange equations <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.

### Other Features

*   **Text Manipulation**: Includes features like automatically animating anagrams by moving letters to corresponding positions <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.
*   **Sub-Object Control**: Manim can extract and manipulate individual components of complex objects, such as pulling out the geometrical points of a specific letter from a text object <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

## Resources

*   **GitHub Repository**: All code for 3Blue1Brown videos, including the Manim tool itself, is available on GitHub at `github.com/3b1b/videos` <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>.
*   **Example Scenes**: The repository includes example scenes that demonstrate various operations and functionalities <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>.
*   **Documentation**: The Manim Community version has robust documentation <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>. The animations themselves can be found in a folder within the library called `animation` <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>.
*   **Workflow Replication**: The creator plans to document his specific workflow, including Sublime Text scripts, to help others replicate it in their preferred text editors <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.