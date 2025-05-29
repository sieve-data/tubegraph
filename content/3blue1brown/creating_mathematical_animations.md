---
title: Creating mathematical animations
videoId: rbu7Zu5X1zI
---

From: [[3blue1brown]] <br/> 

[[Manim animation library | Manim]] is a custom [[Python for animation | Python]] library designed for animating videos, particularly for visualizing mathematical concepts. It is entirely programmatic and bespoke, developed by 3Blue1Brown to illustrate [[mathematical_functions_and_graphs | mathematical functions]] as transformations and create visually engaging explanations [00:00:05 | 00:01:04].

## The Manim Library

### History and Versions
[[Manim animation library | Manim]]'s history is closely tied to the 3Blue1Brown channel. It began as a personal coding project to better illustrate mathematical transformations. As videos were made, the tool improved, leading to a continuous cycle of enhancement and content creation [00:01:00 | 00:01:21].

There are two main versions of Manim:
*   **Original Version**: Developed by 3Blue1Brown, this version has evolved over the years to become more interactive and performant [00:01:54 | 00:02:22]. The code for videos and the tool itself are open source on GitHub [00:01:38 | 00:01:42].
*   **Manim Community Version**: A community of developers forked the original repository to create a more robust, better-tested, and well-documented version, which is generally recommended for new users [00:01:59 | 00:02:13]. The original creator often makes changes to his version that are not immediately integrated into the community version [00:02:15 | 00:02:19].

## Manim Workflow

The core workflow involves writing [[Python for animation | Python]] code in a text editor and running it in an interactive shell to instantly see visual outputs [00:02:40 | 00:02:49].

### Scene Structure
All animations are defined within Python classes that represent "scenes" [00:03:00 | 00:03:03]. The rendering logic resides within a specific method called `construct` [00:03:08 | 00:03:11].

### Interactive Development
A key feature of the workflow is the interactive [[Python for animation | Python]] terminal that communicates directly with the scene [00:03:54 | 00:03:58]. This allows for immediate testing of code snippets:
*   **Direct Command Execution**: Users can type [[Python for animation | Python]] commands directly into the terminal to manipulate objects, like `square.shift` to move a square [00:03:41 | 00:03:45].
*   **Shortcut for Code Execution**: A keyboard shortcut (e.g., Command+R in Sublime Text) copies and runs selected code from the text editor into the terminal, providing instant visual feedback [00:04:28 | 00:04:41].
*   **Checkpoint Paste**: For long scenes, a `checkpoint paste` feature allows running a specific section of code. This reverts the scene to its state at the beginning of that section, enabling rapid iteration and tweaking of small parts without re-rendering the entire scene from scratch [00:05:36 | 00:06:19]. This offers a hybridization between a raw text file and a Jupyter notebook, combining the benefits of both [00:06:38 | 00:06:46].

### Objects and Animations
Manim works with "mathematical objects" (mobjects), many of which are vectorized (e.g., curves) and have properties like stroke thickness or fill [00:15:55 | 00:16:08].

Common animation operations include:
*   `add`: Makes an object appear on the screen [00:07:00 | 00:07:02].
*   `play`: Orchestrates animations over time [00:07:17 | 00:07:22].
*   `write`: Animates text as if it's being written [00:07:26 | 00:07:28].
*   `transform`: Allows any object to smoothly transform into another [00:07:52 | 00:07:58]. This function is foundational for many Manim animations [00:08:44 | 00:08:48].
*   `show_creation`: Reveals an object (like a curve) gradually [00:19:03 | 00:19:09].
*   `fade_out`: Slowly changes an object's opacity to zero [00:38:14 | 00:38:21].
*   `TracingTail`: Creates a fading trail behind a moving object [00:39:07 | 00:39:17].

### Styling and Rate Functions
Animations can be styled with colors, gradients, and stroke widths [00:19:50 | 00:20:11]. Manim also utilizes "rate functions" to control the pacing and smoothness of animations. The default `smooth` function uses a cubic Bézier curve for fluid transitions, while `linear` creates jerky starts and stops, which might be desired for specific effects or when representing precise [[continuity and mathematical functions | mathematical behavior]] [00:09:52 | 00:10:29].

### Camera Control
For 3D scenes, camera reorientation (`frame.reorient`) allows for dynamic perspectives, crucial for maintaining the illusion of depth on a 2D screen [00:33:52 | 00:34:06]. Interactive camera movement during development is also possible [00:33:33 | 00:33:36].

### Handling LaTeX and Text
Manim can render LaTeX expressions, which can be dynamically styled (e.g., coloring specific variables) or positioned within the scene [00:44:41 | 00:46:00]. The `fix_in_frame` command glues objects (like equations) to the camera frame so they appear stationary relative to the view, rather than moving with the 3D scene [00:39:00 | 00:39:03 | 00:45:39 | 00:45:44].

### Final Rendering
Once a scene is complete, it can be rendered to an MP4 file, typically in 4K resolution [00:42:52 | 00:42:56]. This file can then be used in video editing software [00:42:58 | 00:43:03 | 00:43:29].

## Example: Animating the Lorenz Attractor

The Lorenz Attractor is a famous bizarre shape from chaos theory, generated by a set of differential equations in three dimensions [00:10:41 | 00:11:02]. It's excellent fodder for [[visualization_of_3d_vector_transformations | 3D visualization]] [00:11:08 | 00:11:09].

The animation process for the Lorenz Attractor involved:
1.  **Setting up 3D Axes**: While most Manim scenes are 2D, the Lorenz Attractor necessitates a 3D coordinate system [00:12:02 | 00:12:20].
2.  **Solving Differential Equations**: Python libraries like SciPy (specifically, its numerical ODE solver) are used to find solutions to the Lorenz equations for given initial conditions over time [00:12:35 | 00:13:00 | 00:13:18].
3.  **Plotting Points**: The calculated XYZ points are converted to Manim's coordinate system using `coords_to_points` and then used to define a curve [00:16:45 | 00:17:01].
4.  **Animating Evolution**: The `show_creation` animation with a linear rate function reveals the curve over time, accurately representing the system's evolution [00:19:16 | 00:19:43].
5.  **Illustrating Chaos**: Multiple curves, starting from slightly different initial conditions, are animated simultaneously with distinct colors to demonstrate the chaotic divergence [00:20:26 | 00:22:02].
6.  **Tracking Endpoints**: `GlowDot` objects track the endpoints of each curve, with an `updater` function continuously moving them to the curve's current end point [00:24:06 | 00:25:04].
7.  **Fading Trails**: The `TracingTail` function creates a fading trail behind the moving dots, visualizing the recent path of each point [00:39:07 | 00:40:51]. This visually emphasizes the "strange attractor" behavior, where despite initial proximity, the paths eventually diverge widely within the same bounded shape [00:36:40 | 00:37:08].

## Development Environment and Best Practices

*   **Open Source Code**: All video animation code is openly available on GitHub (github.com/3b1b/videos) for users to explore and learn from [00:35:57 | 00:38:09 | 00:41:40 | 00:41:47 | 00:50:35 | 00:50:42].
*   **Debugging**: While an interactive shell is powerful, some Python scoping issues (like a "name error" when a function tries to access a variable defined in an outer scope during interactive sessions) can arise. A "cursed" but effective hack (`globals().update(locals())`) is used to make all local variables globally accessible within the interactive environment for scene development [00:29:00 | 00:30:27]. The more proper way to handle this is to pass variables explicitly as arguments to functions, including default values [00:31:15 | 00:31:34].
*   **Helper Tools**: Tools like MathPix, which uses OCR to convert equations from images into LaTeX, are incredibly useful for integrating complex mathematical expressions [00:44:53 | 00:45:15].
*   **Learning Manim**: New users are encouraged to explore Manim's `animation` folder for existing animation types or consult example scenes provided in the library to understand available functionalities [00:48:47 | 00:49:20 | 00:50:27 | 00:52:30]. Text editor features like language server protocols or auto-completion can also help in discovering functions [00:51:24 | 00:51:38].