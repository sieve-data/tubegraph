---
title: Using components and auto layout in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

When designing in Figma, leveraging components and [[plugins_and_tools_for_enhancing_figma_design_workflow | Auto Layout]] can significantly speed up your workflow and ensure consistency [00:02:46]. These features allow designers to iterate quickly and manage changes efficiently [00:01:04].

## Starting with Components

A "component" in Figma acts as a container, similar to a CSS `div` [00:02:09]. To create a component:
1.  Hit `F` to create a frame, which serves as your container [00:02:07].
2.  Turn this frame into a component as an initial step, even before adding content [00:02:42].
    *   This approach is a "total hack" for moving quickly, as it allows you to define a single source of truth for your design elements [00:02:36].
    *   The goal is to avoid repeating the same actions [00:03:00].
3.  Once the component is created, you can duplicate it multiple times within a container [00:03:17]. Any changes made to the main component will automatically apply to all its instances [00:04:06].

### Managing Iterations with Components

When iterating on designs, you might create multiple versions of a component. To "freeze" a specific iteration and prevent it from updating with the main component:
*   Duplicate the entire frame containing the component instances [00:10:00].
*   Use the "Destroyer" plugin to remove all component instances within that duplicated frame, effectively freezing them in time [00:10:11]. This allows you to preserve different stages of your design exploration [00:10:26].

### Multi-Editing Component Variants

Figma's multi-edit variants feature allows you to make changes across all states or variants of a component simultaneously:
*   Select your component [00:27:00].
*   Click the "multi-edit variants" icon or press `Q` [00:27:04].
*   Any changes made will populate across all variants, saving time and ensuring consistency [00:27:10].

## Implementing Auto Layout

[[plugins_and_tools_for_enhancing_figma_design_workflow | Auto Layout]] is a powerful feature that organizes frames and their contents automatically, similar to CSS Flexbox [00:03:32].
1.  To apply Auto Layout to a frame, select it and press `Shift + A` [00:03:36].
2.  Once in Auto Layout, you can control properties like spacing between items [00:03:50] and padding [00:16:04].
3.  Auto Layout ensures that elements dynamically adjust their width and position [00:27:56]. This is crucial for creating responsive and scalable designs [00:15:05].
    *   Designing with [[plugins_and_tools_for_enhancing_figma_design_workflow | Auto Layout]] makes it much easier for developers to translate designs into code, as it directly maps to Flexbox properties in CSS [00:16:16].
    *   Avoid randomly positioning elements in a frame without Auto Layout, as this is akin to using absolute positioning in CSS, which can be problematic for development [00:15:16].

## Prototyping with Components and Auto Layout

[[prototyping_and_adding_interactivity_in_figma | Prototyping]] allows you to add interactivity, such as hover states, to your designs [00:01:27].
1.  To add a hover state, create a component with a default state [00:23:29].
2.  Add a "variant" to the component, naming it "hover" [00:23:33].
3.  In the hover variant, make the desired visual changes (e.g., increased blur, background, or border) [00:23:58].
4.  Switch to "Prototype" mode [00:24:22].
5.  Drag a connection from the default component state to the hover variant [00:24:29].
6.  Set the interaction trigger to "While Hovering" [00:24:41].
7.  For a smooth transition, choose "Smart Animate" and adjust the easing (e.g., "gentle" with a duration of 400ms) [00:24:53].

## Enhancing Visuals with Plugins

While Figma offers many built-in capabilities, a few plugins can enhance visual effects:
*   **Phosphor**: For adding icons, ensuring they look consistent [00:13:26].
*   **Smooth Shadow**: For creating realistic and beautiful drop shadows [00:25:59].
*   **Noise and Texture**: To add graininess and visual interest to designs [00:20:13].
*   **Destroyer**: As mentioned, useful for breaking component instances [00:10:22].
*   **Content Reel**: For quickly populating designs with placeholder content like avatars or text [00:31:00].

It's recommended to not stress about building a vast repertoire of plugins, as Figma's native features, especially [[plugins_and_tools_for_enhancing_figma_design_workflow | Auto Layout]] and bulk editing, have significantly reduced the need for many external tools [00:32:43].

## Design Philosophy

The design process often involves constant exploration and iteration [00:12:47]. It's recommended to have a separate monitor or laptop displaying the design at 1x in prototype mode, while zooming in and making changes on the primary screen. This allows for real-time feedback on how the design feels at its actual size [00:11:20].

Designers are often "collectors of design" rather than just creators [00:37:34]. Continuously noticing and asking "why" you like certain design elements helps build an internal database of ideas [00:07:42].

Figma is excellent for generative design and exploring a wide array of ideas, providing a "piece of paper" for sketching and diverging [00:35:53]. However, once core ideas are solidified, tools like Framer (for web design) or [[using_vz_platform_for_app_component_generation | VZ]] (for app components) may be used for final refinement and building in a code-based medium, as the line between high-fidelity design and high-fidelity code continues to blur [00:36:26].