---
title: Using Blueprint Visual Scripting in Unreal Engine
videoId: D4nnVwEoN98
---

From: [[hu-po]] <br/> 

[[game_development_using_unreal_engine_5 | Unreal Engine]] 5 features a visual scripting system known as Blueprints, allowing users to create interactive experiences without writing code <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. This system defines object-oriented classes and is implemented through a node-based interface, similar to those found in Blender <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

## Benefits of Blueprints

Blueprint visual scripting offers several advantages, especially for rapid prototyping and collaboration:
*   **No Code Required**: Entire games or complex logic can be created without writing a single line of code <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Rapid Development**: Blueprints enable quicker development compared to C++ <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.
*   **User-Friendly**: It provides an intuitive node-based interface that makes it easy to create new types of actors and script level agents <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.
*   **Collaboration**: Working with non-programmers is easier, as Blueprints are simple to modify <a class="yt-timestamp" data-t="01:08:48">[01:08:48]</a>.
*   **Performance Pathway**: While initial development is often faster with Blueprints, objects created using this system can later be converted to C++ for improved performance if needed <a class="yt-timestamp" data-t="01:08:54">[01:08:54]</a>.

### Comparison to C++
While [[game_development_using_unreal_engine_5 | Unreal Engine]] typically uses C++, which requires a stronger programming background and takes longer to write, Blueprints offer an alternative for those seeking a less code-intensive approach <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This contrasts with [[comparison_between_unity_and_unreal_engine | Unity]], which primarily uses C# for scripting <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>.

## Blueprint Editor Overview
The Blueprint Editor is used to define custom behaviors and combine mesh components into a single game object <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>. When opened, it displays a streamlined view with various panels:

### Components Panel
The **Components** panel lists all current components that make up the object (e.g., the body, windows, periscope, propeller of a vessel) <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>, <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>. The "Default Scene Root" is the topmost member and is visible only in the editor <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a>.

### Event Graph
The **Event Graph** is where the logic and nodes for the Blueprint are placed <a class="yt-timestamp" data-t="00:52:38">[00:52:38]</a>. It supports an event-based system where actions are triggered by specific events <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. Common event nodes include:
*   **Event Begin Play**: Triggers when play begins for the actor <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>.
*   **Event Actor Overlap**: Triggers when this actor overlaps with another actor (e.g., a player walking into a trigger) <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>.
*   **Event Tick**: Triggers every frame or at specified time intervals, useful for continuous actions like rotation <a class="yt-timestamp" data-t="00:53:24">[00:53:24]</a>, <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.

Nodes connect via input and output pins. An input pin must have a connection for the node to execute <a class="yt-timestamp" data-t="01:10:22">[01:10:22]</a>.

### My Blueprint Panel
This section is used to manage graphs, functions, and variables within the Blueprint <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.

### Viewport Panel
The **Viewport** tab provides a visual representation of the level, allowing users to look around by holding the right-click button and moving the mouse, and navigate using WASD keys <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

### Details Panel
The **Details** panel displays the properties of a selected object, such as location, static light properties, and event handling for collisions or damage <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.

## Working with Blueprints
1.  **Creating a Blueprint Class**: Users can create a Blueprint class by right-clicking in the Content Drawer and selecting "Blueprint Class" <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. Options include `Actor` (a general object that can be placed), `Pawn` (an actor that can be possessed by a controller), or `Character` (a type of Pawn that includes walking abilities) <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>.
2.  **Adding Components**: Objects can be dragged into the Blueprint's viewport to add them as components <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>.
3.  **Adding Logic**: Right-click in the Event Graph to bring up a menu of available nodes and search for desired functionalities, such as `Add Local Rotation` to make an object rotate <a class="yt-timestamp" data-t="01:11:33">[01:11:33]</a>. Connecting an event node (like `Event Tick`) to a logic node will make the action execute repeatedly <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.
4.  **Compiling and Saving**: After updating a Blueprint, it's crucial to `Compile` and `Save` it for changes to take effect in the game <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>.

### Integration with Python
It's noted that [[python_scripting_in_unreal_engine_5 | Python scripting in Unreal Engine 5]] can be used to control elements within the [[game_development_using_unreal_engine_5 | Unreal Engine]] <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. The [[python_support_and_plugins_in_unreal_engine | Unreal Editor Python API]] is thought to essentially mirror the capabilities of the Blueprint API, allowing for similar underlying functionality whether using nodes or [[python_scripting_in_unreal_engine_5 | Python scripts]] <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.

## Future Applications
Blueprints will be further explored for [[configuring_unreal_engine_5_plugins_for_vr_development | VR applications]] and mixed reality projects <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>.