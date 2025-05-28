---
title: Creating and managing 3D assets and materials in Unreal Engine
videoId: D4nnVwEoN98
---

From: [[hu-po]] <br/> 

[[game_development_using_unreal_engine_5 | Unreal Engine 5]] (UE5) is a powerful game engine, also used as a simulation creation machine for various applications like robotics, deep learning, and computer vision <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Compared to other engines like Unity, [[comparison_between_unity_and_unreal_engine | Unreal Engine]] is generally considered more powerful, offering built-in systems and speed <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. This article covers the process of creating and managing 3D assets and their associated materials within [[game_development_using_unreal_engine_5 | Unreal Engine 5]].

## Understanding 3D Assets and Materials

In virtual worlds, 3D objects, also known as assets, are rendered based on two fundamental components:
*   **Mesh**: A collection of 3D positions in space (vertices) connected by lines and faces (triangles) that define the object's shape <a class="yt-timestamp" data-t="00:58:47">[00:58:47]</a>.
*   **Material**: Defines the visual appearance of an object, including properties like base color, metallic properties (shininess), and roughness (matte look) <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.

## Importing 3D Models

To bring external 3D models into [[game_development_using_unreal_engine_5 | Unreal Engine]], you can use the Content Drawer and the Import button <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.

When importing a 3D model (e.g., an `.fbx` or `.gltf` file), [[game_development_using_unreal_engine_5 | Unreal Engine]] provides various options, such as:
*   **Import Scale**: Adjust the size of the model <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.
*   **Import Textures**: Option to import textures along with the model or separately <a class="yt-timestamp" data-t="00:36:33">[00:36:33]</a>.
*   **Force all meshes type**: Allows specifying mesh type <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.
*   **Build skeletal meshes**: For models with animation skeletons <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.

After importing, models are placed in the Content Drawer, which serves as a file browser for your project <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.

## Creating and Using Materials

Materials are crucial for defining how your 3D models look in the engine.

### Creating a New Material
1.  Navigate to the desired folder in the Content Drawer (e.g., `Materials`).
2.  Right-click and select "Material" to create a new material asset <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.
3.  Give it a descriptive name <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>.
4.  Double-click the new material to open the **Material Editor** <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>.

### The Material Editor
The Material Editor uses a node-graph-based system <a class="yt-timestamp" data-t="01:00:43">[01:00:43]</a>, where nodes represent functions and can have inputs and outputs (pins) <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>.
*   **Viewport**: Displays a real-time preview of the material's appearance <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.
*   **Details Panel**: Shows properties of the selected node <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.
*   **Material Graph**: Where all the nodes and the final result node are connected <a class="yt-timestamp" data-t="01:01:32">[01:01:32]</a>.
*   **Palette**: Lists all available nodes <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.

### Connecting Textures and Adjusting Properties
To add color and detail to a material, you typically use textures.
1.  Drag image files (textures) from your Content Drawer directly into the Material Graph <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.
2.  Connect the **RGB output** of a Texture Sample node to the **Base Color input** of the main material node to apply the texture's color to the object <a class="yt-timestamp" data-t="01:05:44">[01:05:44]</a>.
3.  You can also add **Constant** nodes and connect them to properties like **Metallic** or **Roughness** to control the material's shininess or matte appearance <a class="yt-timestamp" data-t="01:06:18">[01:06:18]</a>. A higher metallic value makes it shinier, while a higher roughness value gives it a matte look <a class="yt-timestamp" data-t="01:06:28">[01:06:28]</a>.
4.  After making changes, click **Apply** and **Save** in the toolbar <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a>.

### Applying Materials to Meshes
Once a material is created, you can apply it to your 3D models:
1.  Open the blueprint or asset containing the mesh you wish to texture.
2.  Select the desired mesh components (e.g., `USB 3.0` and `USB 2.0`).
3.  In the Details panel, find the `Materials` section.
4.  Click the dropdown on the right of `Element 0` and select your newly created material <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>.
5.  **Compile and Save** the blueprint to see the changes <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.

## Organizing and Saving Assets

Good organization in the Content Drawer is key. You can create folders like `Models`, `Materials`, and `Blueprints` to keep your project tidy <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.

It is crucial to save your work frequently in [[game_development_using_unreal_engine_5 | Unreal Engine]], as changes are not permanent until explicitly saved <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>.
*   `Save Current Level`: Saves the current level.
*   `Save All`: Saves all modified assets in the project <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>. A common shortcut for "Save All" is `Ctrl + Shift + S` <a class="yt-timestamp" data-t="01:09:08">[01:09:08]</a>.

## Integrating Assets with Blueprints

Imported meshes and created materials are often integrated into [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint actors]]. A Blueprint acts as a "master object" that can combine mesh components into a single object used in the game <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>. This allows attaching scriptable behavior to 3D objects without writing code, though [[python_support_and_plugins_in_unreal_engine | Python support and plugins in Unreal Engine]] also allow for scripting via a Python API <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>, bridging the gap between [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]] and traditional coding approaches for asset management and procedural content generation <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

For instance, an `Actor` Blueprint can contain multiple static mesh components (e.g., two USB components) <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. Logic can then be added to the Blueprint's Event Graph using nodes (e.g., `Add Local Rotation` for continuous movement based on `Event Tick`) <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. The Blueprint becomes the entity dragged into the scene, encapsulating both the visual mesh and its interactive logic <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.

[[game_development_using_unreal_engine_5 | Unreal Engine]] also supports advanced features for rendering and simulation, including built-in VR capabilities for devices like [[installing_oculus_quest_integration_in_unreal_engine_5 | Oculus Quest]] and HoloLens <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.