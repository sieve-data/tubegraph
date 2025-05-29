---
title: Python for animation
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

The 3Blue1Brown YouTube channel's animations are created using a custom Python library called [[manim_animation_library | Manim]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This tool is entirely programmatic and bespoke <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The workflow involves extensive use of Python for defining scenes, objects, and animations <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## The Manim Library

[[manim_animation_library | Manim]] began as a coding project to better illustrate mathematical functions as transformations <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>. The tool improved as more videos were made, and vice versa <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>. All code used for the videos is openly visible on GitHub, and the [[manim_animation_library | Manim]] tool itself was also made open source <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

There are two versions of [[manim_animation_library | Manim]] <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>:
*   **Original Version:** This version is developed and used by 3Blue1Brown, and it has seen workflow improvements, making it more interactive and performant over the years <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Manim Community Version:** A community-driven fork of the original repository, which is more robust, attentive to issues and pull requests, and has better testing and documentation <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. It is generally recommended for new users <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

## Workflow and Interactivity

Animation in [[manim_animation_library | Manim]] is highly interactive, allowing for rapid iteration during scene development <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

### Scene Creation
All scenes in [[manim_animation_library | Manim]] are created as Python classes <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. The primary animation code resides within a method called `construct` <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

### Objects and Manipulation
Mathematical objects (`mobjects`) like circles, squares, and text can be added to a scene <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. These objects can be manipulated using various methods, such as `shift` to move them <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Immediate Feedback
A key aspect of the workflow is the ability to run Python code snippets directly from a text editor (like Sublime Text) and see immediate visual output in the [[manim_animation_library | Manim]] scene <a class="yt-timestamp" data-t="04:20:00">[04:20:22]</a>. This is achieved through a Python terminal that communicates with the active scene <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. For longer scenes, a "checkpoint paste" functionality allows running specific sections of code by reverting the scene to a cached state at the start of that section, similar to a Jupyter notebook <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.

### Animations
The `play` method is used to execute animations on objects <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. Common animations include:
*   **`write`**: Makes text appear as if being written <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
*   **`transform`**: Transforms one object into another <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. This can include precise transformations, such as changing an 'H' character into a circle by mapping their geometrical points <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.
*   **`show creation`**: Gradually draws a curve or object <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>.
*   **`fade out`**: Gradually changes an object to have zero opacity <a class="yt-timestamp" data-t="38:14:00">[38:14:00]</a>.
*   **`tracing tail`**: Creates a fading trail behind a moving object <a class="yt-timestamp" data-t="39:17:00">[39:17:00]</a>.

Animations often use "rate functions" (e.g., `smooth`, `linear`) to control the pacing and easing of transformations, which significantly impacts the aesthetic quality <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.

### 3D Capabilities
While most scenes are in 2D to simulate a blackboard <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>, [[manim_animation_library | Manim]] supports 3D animations using 3D axes <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>. Coordinates can be converted between the mathematical and [[manim_animation_library | Manim]]'s internal coordinate systems using functions like `coords to points` <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>. Camera movements, such as panning and rotation, can be animated to enhance the perception of depth <a class="yt-timestamp" data-t="33:55:00">[33:55:00]</a>. Objects can be "fixed in frame" to appear glued to the camera, regardless of camera movement <a class="yt-timestamp" data-t="39:00:00">[39:00:00]</a>.

### Mathematical Rendering
[[manim_animation_library | Manim]] can render LaTeX expressions, converting them into scalable vector graphics (SVGs) for display <a class="yt-timestamp" data-t="44:41:00">[44:41:00]</a>. Specific parts of LaTeX expressions, such as variables, can be programmatically colored or animated individually for highlighting <a class="yt-timestamp" data-t="45:56:00">[45:56:00]</a>. Functions like `transform` can match and animate transitions between strings, even creating anagram-like animations <a class="yt-timestamp" data-t="49:06:00">[49:06:00]</a>.

## Example: Lorenz Attractor

The Lorenz Attractor is a classic example of chaos theory, originating from a set of differential equations in three dimensions <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>. Animating it in [[manim_animation_library | Manim]] demonstrates several key features:

1.  **Mathematical Calculation**: Python's SciPy library can be used to solve the Lorenz equations numerically for given initial conditions <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>. Chat GPT can assist in generating boilerplate code for this <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.
2.  **Curve Generation**: The solutions (sets of points) are used to create `vectorized mobjects` (curves) <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.
3.  **Multiple Initial Conditions**: Multiple curves can be generated from slightly different initial conditions, each with distinct colors <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. The `color_gradient` function helps generate a range of colors <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.
4.  **Dynamic Elements**: "Glow dots" can be added to track the endpoints of each curve, updating their position with an `updater function` on every frame <a class="yt-timestamp" data-t="24:06:00">[24:06:00]</a>.
5.  **Illustrating Chaos**: By animating multiple curves and their tracking dots, the "chaotic" behavior of the Lorenz system—where initially close points diverge significantly over time—is clearly visualized <a class="yt-timestamp" data-t="20:22:00">[20:22:00]</a>.

## Rendering and Output

Once a scene is developed and refined, it can be rendered into an MP4 file <a class="yt-timestamp" data-t="42:52:00">[42:52:00]</a>. This is typically done via the command line using `manim <file.py> <SceneName> -w` (for writing to file), with options for pre-running to estimate time and catch errors <a class="yt-timestamp" data-t="42:09:00">[42:09:00]</a>. Rendering at 4K resolution can take longer <a class="yt-timestamp" data-t="42:59:00">[42:59:00]</a>. The interactive shell version significantly speeds up the iteration cycle compared to repeatedly rendering from the command line <a class="yt-timestamp" data-t="43:31:00">[43:31:00]</a>.

## Accessing Code and Documentation

All 3Blue1Brown video animation code is available on GitHub at `github.com/3b1b/videos` <a class="yt-timestamp" data-t="50:38:00">[50:38:00]</a>. This repository serves as a valuable resource for understanding available functionality <a class="yt-timestamp" data-t="51:02:00">[51:02:00]</a>. The [[manim_animation_library | Manim]] community version offers comprehensive documentation <a class="yt-timestamp" data-t="50:22:00">[50:22:00]</a>. Text editor tools, such as language server protocols, can provide auto-completion for functions within the library <a class="yt-timestamp" data-t="51:25:00">[51:25:00]</a>.