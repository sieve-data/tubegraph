---
title: Game development using Unreal Engine 5
videoId: D4nnVwEoN98
---

From: [[hu-po]] <br/> 

Unreal Engine 5 (UE5) is a powerful game engine, which can be thought of as a "simulation creation machine" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It is the latest version of Epic Games' Unreal Engine <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. While traditionally used for video games and even movies, UE5 is increasingly being adopted for simulations in fields such as robotics, deep learning, and computer vision <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Comparison with [[Comparison between Unity and Unreal Engine | Unity]]
Other game engines exist, such as [[Comparison between Unity and Unreal Engine | Unity]] and Godot <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. [[Comparison between Unity and Unreal Engine | Unity]] is more lightweight but less powerful than Unreal Engine, lacking some of its built-in systems and speed <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. A significant difference lies in their primary scripting languages: [[Comparison between Unity and Unreal Engine | Unity]] uses C#, which is generally considered easier to write in, while Unreal Engine uses C++, requiring a stronger programming background <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Core Features of Unreal Engine 5

### Nanite
Nanite is a level of detail system within UE5 <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. It automatically renders 3D assets at different levels of detail based on their distance from the camera, optimizing performance by rendering objects further away at a lower detail <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Lumen
Lumen is another key technology in UE5, associated with real-time global illumination and reflections <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### MetaHuman
UE5 includes MetaHuman, which allows for the creation of realistic avatars <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### [[Using Blueprint Visual Scripting in Unreal Engine | Blueprint Visual Scripting]]
[[Using Blueprint Visual Scripting in Unreal Engine | Blueprints]] is a node-based visual scripting system that enables users to create entire games without writing a single line of code <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. It functions as a node-based interface, similar to those found in Blender, used to define object-oriented classes and script level events <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a> <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

Key aspects of [[Using Blueprint Visual Scripting in Unreal Engine | Blueprints]]:
*   **Event-based system:** [[Using Blueprint Visual Scripting in Unreal Engine | Blueprints]] utilize an event-based system, where actions are triggered by specific events like `Event Begin Play` (when the actor is created or scene initialized), `Event Actor Overlap` (when an actor touches another), or `Event Tick` (called every frame or at specified intervals) <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a> <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>.
*   **Nodes and Pins:** [[Using Blueprint Visual Scripting in Unreal Engine | Blueprints]] consist of nodes, which represent functionalities, connected by pins (inputs and outputs) <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. Execution flow depends on connections between input pins <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>.
*   **Actors, Pawns, and Characters:**
    *   **Actor:** Any object that can be placed in the game world <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>.
    *   **Pawn:** An Actor that can be "possessed" and receive input from a controller <a class="yt-timestamp" data-t="00:50:23">[00:50:23]</a>.
    *   **Character:** A type of Pawn that includes built-in abilities for walking and movement <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.
*   **Components:** [[Using Blueprint Visual Scripting in Unreal Engine | Blueprint]] components are constituent parts of an object (e.g., body, windows, periscope for a submarine model) <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.

### [[Python support and plugins in Unreal Engine | Python Scripting]]
Unreal Engine supports [[Python scripting in Unreal Engine 5 | Python scripting]] via an API <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. This allows users to script actions within the Unreal Editor using [[Using Python for asset management and procedural content generation in Unreal Engine | Python]] <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. The [[Python support and plugins in Unreal Engine | Python API]] effectively mirrors the functionality available through the [[Using Blueprint Visual Scripting in Unreal Engine | Blueprint]] visual scripting system <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

### Virtual Reality (VR) Capabilities
Unreal Engine 5 includes built-in support for VR devices such as [[Installing Oculus Quest integration in Unreal Engine 5 | Oculus Quest]] and [[Configuring Unreal Engine 5 plugins for VR development | HoloLens]] <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. Project templates for handheld AR and virtual reality are available <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

## Workflow and User Interface

### [[Installing Unreal Engine 5 on Ubuntu 2004 | Installation]]
Unreal Engine 5 can be installed on Linux distributions like Ubuntu. While official guides might target newer versions (e.g., Ubuntu 22.04), it is possible to install and run UE5 on older versions like Ubuntu 20.04 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
Minimum system requirements include an 8GB graphics card and more than 60GB of free disk space <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Installation involves unzipping the downloaded files and running the Unreal Editor executable <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Users might encounter warnings about outdated NVIDIA drivers, but the engine can often still run <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Project Management and UI
*   **Project Types:** Users can choose from various project templates, including first-person, third-person, top-down, vehicle, blank, handheld AR, virtual reality, film and video, and architecture visualization <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Editor View:** The UE5 editor features a streamlined control and sidebar interface <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
*   **Viewport:** The main window for viewing and navigating the level <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. Navigation involves holding the right-click and moving the mouse to look around, and using WASD keys to move <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. Objects can be moved (W), rotated (E), and scaled (R) <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>. Pressing 'F' focuses the camera on a selected object <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.
*   **Modes Panel:** Allows selection between various tools such as landscape, foliage, mesh paint, modeling, and animation <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
*   **World Outliner:** Displays all objects in the current level, allowing for organization into folders and filtering <a class="yt-timestamp" data-t="00:29:13">[00:29:13]</a>.
*   **Details Panel:** Shows properties of a selected object, component, or node <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a> <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
*   **Content Drawer:** Manages all project files, including meshes, textures, and blueprints <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>.
*   **Toolbar:** Contains frequently used functions, most notably the "Play" button to run the simulation <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
*   **Saving:** Projects must be explicitly saved, typically using `Ctrl+S` for the current level and `Ctrl+Shift+S` to save all modified assets <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a> <a class="yt-timestamp" data-t="00:44:25">[00:44:25]</a>.

### [[Creating and managing 3D assets and materials in Unreal Engine | Assets and Materials]]
*   **Meshes:** 3D objects are composed of meshes, which are collections of vertices (3D positions) and faces that connect them (e.g., triangles) <a class="yt-timestamp" data-t="00:58:47">[00:58:47]</a>.
*   **Materials:** Materials define the appearance of 3D objects <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. They have properties such as:
    *   **Base Color:** The primary color of the object <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>.
    *   **Metallic:** Determines how metallic an object appears and reflects light <a class="yt-timestamp" data-t="00:59:41">[00:59:41]</a>.
    *   **Specular:** Controls the shininess <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>.
    *   **Roughness:** Determines how matte or reflective an object is; high roughness means less reflection <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a>.
*   **Material Editor:** Materials are created and modified using a node-graph based system within the Material Editor, allowing complex textures and visual effects <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>. Textures (e.g., PNG images) can be dragged directly into the graph and connected to material properties <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.
*   **Importing Assets:** 3D models and textures can be imported into the Content Drawer, organized into folders (e.g., "models," "materials"), and then applied to objects within the scene <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a> <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

### Lighting and Post-Processing
*   **Baked Lighting:** Calculating how light interacts with objects can be computationally expensive <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. "Baked" lighting means these calculations are done beforehand and are fixed, speeding up game-time rendering <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>.
*   **Post-Process Volume:** A post-process volume is a bounding box within the scene that applies visual effects to the camera view if the camera is inside its extent <a class="yt-timestamp" data-t="01:16:55">[01:16:55]</a>. Properties like global contrast and gamma can be adjusted to create specific atmospheric effects, such as an underwater look <a class="yt-timestamp" data-t="01:19:13">[01:19:13]</a>.