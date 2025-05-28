---
title: Installing Unreal Engine 5 on Ubuntu 2004
videoId: D4nnVwEoN98
---

From: [[hu-po]] <br/> 

[[game_development_using_unreal_engine_5 | Unreal Engine]] is a powerful [[game_development_using_unreal_engine_5 | game engine]] designed for simulation creation, primarily used for video games and movies, but increasingly finding use in robotics, deep learning, and computer vision simulations <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This article focuses on the installation and initial exploration of [[game_development_using_unreal_engine_5 | Unreal Engine 5]], the latest version, on an Ubuntu 20.04 system <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## System Requirements and Preparation
While the official guide used for installation is for Ubuntu 22.04, it is noted that [[game_development_using_unreal_engine_5 | Unreal Engine 5]] can work with Ubuntu 20.04 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Key system specifications verified for this installation included:
*   An 8-gigabyte graphics card <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   More than 60 gigabytes of free disk space <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   An AMD Ryzen 12-core processor <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   An Nvidia driver version 510, despite a warning recommending 515 or 525 <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>, <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

## Installation Process
The installation involves manually unzipping the Unreal Engine files:
1.  **Create a directory:** A new directory, "UnrealEngineFive" (without spaces), was created to house the engine files <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Unzip the installer:** The `unzip` command was used to extract the Unreal Engine 5.1 Linux installer into the newly created directory <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
3.  **Navigate to binaries:** After extraction, the user navigated to `engine/binaries/Linux` within the Unreal Engine directory <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
4.  **Run the Unreal Editor:** The `UnrealEditor` executable was run <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. A warning regarding outdated graphics drivers (Nvidia 510) was displayed, but the installation proceeded <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

## Initial Setup and Editor Overview

### Project Creation
Upon launching, the [[game_development_using_unreal_engine_5 | Unreal Engine]] Project Browser appears <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. For initial setup:
*   A "Blank" template was selected under the "Games" category <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>, <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   Settings were configured for "Blueprint" <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>, "Desktop" target platform <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>, and "Maximum" quality preset <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
*   "Starter Content" and "Ray Tracing" were unchecked to create a clean project <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   The project was named "Submarine" <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a> and saved, creating an `Untitled` level which should be saved as `BaseLevel` <a class="yt-timestamp" data-t="00:41:13">[00:41:13]</a>, <a class="yt-timestamp" data-t="00:47:18">[00:47:18]</a>.

### Editor Interface
The [[game_development_using_unreal_engine_5 | Unreal Engine 5]] editor features a streamlined interface compared to previous versions <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>:
*   **Viewport (1):** Displays the 3D level, navigable by holding right-click and using WASD keys <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>, <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. Pressing 'F' focuses on the selected object <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.
*   **Modes Panel (2):** Allows selection between tools like Landscape, Foliage, Modeling, and Animation modes <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>, <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
*   **World Outliner (3):** Lists all objects in the current level, allowing organization and filtering <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.
*   **Details Panel (4):** Shows properties of the currently selected object <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.
*   **Toolbar (5):** Contains common functions, including the "Play" button to run the simulation <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>, <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.
*   **Content Drawer (6):** Manages project files, including 3D models, textures, and Blueprints <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>, <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
    *   Files are organized into folders (e.g., `Models`, `Materials`, `Blueprints`) <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.
    *   Unsaved changes in the Content Drawer are indicated by a star; `Ctrl+Shift+S` saves all <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

## Core Concepts

### Game Engine Paradigms: Unreal vs. Unity
[[comparison_between_unity_and_unreal_engine | Unreal Engine]] is often compared to [[comparison_between_unity_and_unreal_engine | Unity]] <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. While [[comparison_between_unity_and_unreal_engine | Unity]] is generally more lightweight, [[comparison_between_unity_and_unreal_engine | Unreal Engine]] offers more powerful built-in tools and functionalities <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Key differences include:
*   **Programming Languages:** [[comparison_between_unity_and_unreal_engine | Unity]] uses C# (easier to learn), whereas [[game_development_using_unreal_engine_5 | Unreal Engine]] primarily uses C++ (requiring a stronger programming background) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Built-in Systems:** [[game_development_using_unreal_engine_5 | Unreal Engine]] boasts advanced technologies like **Nanite** (virtualized micro-polygon geometry for level of detail) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, and **Lumen** (real-time global illumination) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, as well as **Metahuman** for realistic avatars <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Blueprints Visual Scripting
Blueprints are a node-based visual scripting system in [[game_development_using_unreal_engine_5 | Unreal Engine 5]] that allows users to create entire games or define object behaviors without writing code <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>, <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.
*   **Functionality:** Blueprints define object-oriented classes and game logic using a node-based interface similar to Blender <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Event Graph:** Blueprints use an event-based system where nodes trigger actions based on events like `Event Begin Play` (when actor starts) <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>, `Event Actor Overlap` (collision) <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>, or `Event Tick` (every frame) <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>.
*   **Nodes and Pins:** Logic is built by connecting nodes via "pins" (inputs and outputs) <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>.
*   **Compilation:** Blueprints must be compiled and saved after updates for changes to take effect <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.

### [[python_scripting_in_unreal_engine_5 | Python Scripting in Unreal Engine]]
[[python_scripting_in_unreal_engine_5 | Unreal Engine]] also offers [[python_scripting_in_unreal_engine_5 | Python scripting]] capabilities <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. The [[python_scripting_in_unreal_engine_5 | Python API]] allows direct scripting of [[game_development_using_unreal_engine_5 | Unreal Editor]] functionalities, effectively offering a code-based alternative to Blueprints for operations like [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | asset management]] <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>, <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>, and [[integrating_python_scripts_with_unreal_engine_content_pipelines | integrating into content pipelines]] <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

### Assets and Materials
3D objects in [[game_development_using_unreal_engine_5 | Unreal Engine]] consist of:
*   **Meshes:** Collections of 3D positions (vertices), lines, and faces that define the object's shape <a class="yt-timestamp" data-t="00:58:47">[00:58:47]</a>.
*   **Materials:** Define the visual appearance of a mesh, including properties like base color, metallic, roughness, and specular <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | Materials can be created]] and applied to objects <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>, <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.
    *   **Material Editor:** A node-based interface allows users to define material properties and connect textures <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>, <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>. Textures (e.g., PNG files) can be dragged directly into the graph and linked to material properties like base color <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>, <a class="yt-timestamp" data-t="01:05:44">[01:05:44]</a>.
    *   **Lighting:** The process of calculating how light interacts with objects in a scene. "Baking" lights pre-calculates interactions, improving performance <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

## Practical Demonstration: USB Component Rotation

A practical demonstration involved importing a 3D model of a Raspberry Pi USB component, creating a custom material, and applying a rotation logic via Blueprints.

### Steps:
1.  **Import 3D Model:** A Raspberry Pi USB component model (GLTF file) was imported into the project's "Models" folder <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>, <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>.
2.  **Create and Apply Material:**
    *   A new material, "USB Material," was created in the "Materials" folder <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>, <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.
    *   A PCB texture was dragged into the Material Editor and connected to the `Base Color` input of the main material node <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>, <a class="yt-timestamp" data-t="01:05:44">[01:05:44]</a>.
    *   A "Constant" node was connected to the `Metallic` input, allowing adjustment of the material's shininess <a class="yt-timestamp" data-t="01:06:18">[01:06:18]</a>.
    *   The material was applied to the imported USB models within their Blueprint <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.
3.  **Create Actor Blueprint:** A new "Actor" Blueprint class named "USB" was created in the "Blueprints" folder <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>, <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. The imported USB meshes were added as components to this Blueprint <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>.
4.  **Add Rotation Logic:**
    *   Inside the USB Blueprint's Event Graph, an `Add Local Rotation` node was created and targeted at one of the USB components <a class="yt-timestamp" data-t="01:11:33">[01:11:33]</a>.
    *   The Y value of the `Delta Rotation` was set to `2.0` <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.
    *   The `Add Local Rotation` node was connected to the `Event Tick` node, causing the component to rotate every frame <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
    *   The Blueprint was compiled and saved <a class="yt-timestamp" data-t="01:13:42">[01:13:42]</a>.
5.  **Place in Scene:** The "USB" Blueprint actor was dragged from the Content Drawer into the main viewport <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>. Objects can be moved (W), rotated (E), and scaled (R) <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>.
6.  **Add Post-Process Effect:**
    *   The default "Volumetric Cloud" object was deleted from the scene <a class="yt-timestamp" data-t="01:15:29">[01:15:29]</a>, <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.
    *   A "Post Process Volume" was added via the "Quick Add" menu <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>.
    *   Its transform was set to `0,0,0` for location and a scale of `0.1, 0.1, 0.1` to cover the scene <a class="yt-timestamp" data-t="01:17:39">[01:17:39]</a>, <a class="yt-timestamp" data-t="01:18:25">[01:18:25]</a>.
    *   Inside the Post Process Volume's details, the "Global Contrast" and "Gamma" under "Color Grading" were set to a bluish value to simulate an underwater effect <a class="yt-timestamp" data-t="01:19:13">[01:19:13]</a>.
7.  **Run Simulation:** Hitting "Play" in the toolbar showed the USB component rotating within the bluish, underwater-like environment <a class="yt-timestamp" data-t="01:20:02">[01:20:02]</a>.

## Future Applications
The exploration of [[game_development_using_unreal_engine_5 | Unreal Engine 5]] is a foundational step towards using it for [[configuring_unreal_engine_5_plugins_for_vr_development | VR applications]] and specifically mixed reality projects <a class="yt-timestamp" data-t="01:21:03">[01:21:03]</a>, <a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>. While not explicitly covered in this installation, [[installing_oculus_quest_integration_in_unreal_engine_5 | Unreal Engine]] has built-in support for devices like [[configuring_unreal_engine_5_plugins_for_vr_development | Oculus Quest]] and HoloLens <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.