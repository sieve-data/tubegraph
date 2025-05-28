---
title: Integrating Python scripts with Unreal Engine content pipelines
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[Python scripting in Unreal Engine 5 | Python scripting]] is supported in [[Game development using Unreal Engine 5 | Unreal Engine 5]], specifically version 5.1 [00:00:34]. It has become a de facto language for production pipelines, with its importance expected to grow further due to deep learning and generative AI models like Stable Diffusion [00:01:00]. [[Python support and plugins in Unreal Engine | Python]] is considered an easy programming language and is a strong choice for automating workflows [00:01:36].

## Capabilities of Python in Unreal Editor

[[Automating workflows using Python in Unreal Editor | Python]] can be used within the Unreal Editor to:
*   Construct large-scale [[Using Python for asset management and procedural content generation in Unreal Engine | asset management]] pipelines [00:02:31].
*   Tie the Unreal Editor to other 3D applications used in an organization [00:02:34].
*   Automate time-consuming asset management tasks, such as generating levels of detail (LODs) or static meshes, although Nanite (a built-in Unreal Engine 5 system) now handles real-time LOD management [00:02:39].
*   [[Using Python for asset management and procedural content generation in Unreal Engine | Procedurally lay out content]] and control the Unreal Editor from custom user interfaces (GUIs) created using Python modules like PySide (e.g., PySide6 with Qt for Python projects) [00:01:42, 00:02:06, 00:03:01].

It is important to note that [[Python scripting in Unreal Engine 5 | Python]] is primarily used *within the Unreal Editor* for automation and scripting, not within the final packaged game executable. Python libraries and scripts are not included in the built game [00:03:10, 00:03:33].

## Enabling Python Support in Unreal Engine

To use [[Python support and plugins in Unreal Engine | Python]] in the Unreal Editor, the "Python Editor Script Plugin" must be enabled [00:03:43, 00:04:27]. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation on the computer is not required [00:05:36, 00:05:47].

## Running Python Scripts in Unreal Editor

There are several ways to execute [[Python scripting in Unreal Engine 5 | Python scripts]] within the Unreal Editor, each suited for different needs [00:07:18]:

### Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands [00:08:15]. This can be accessed via the tilde key (`~`) [00:08:30].
*   **Interactive execution**: Lines of Python code can be entered and executed immediately, similar to an interactive Python command line [00:08:40].
*   **Multi-line input**: Multiple lines can be entered using Shift+Enter or by pasting a multi-line block [00:08:56].
*   **`pi` command**: In the normal console mode, the `pi` command can be used to run the rest of the line as Python code [00:09:28].
*   **Script execution**: Python script files can be executed by typing their full path (or relative path if configured) and name into the console, optionally including command-line arguments [00:09:08, 00:23:30, 00:25:02].

### Command Line Execution
Python scripts can be specified in the command line arguments when starting the Unreal Editor [00:32:51].
*   **Full Editor Launch**: The full Unreal Editor launches, opens the specified project, loads the default startup level, and then runs the Python script once everything is loaded. This is suitable for scripts interacting with project content or levels [00:33:13].
*   **Headless Mode (Commandlet)**: A faster execution approach where scripts run in a headless mode using the `run_python_script` commandlet. This can be trickier for loading levels and other assets [00:33:47].

### `init_unreal.py` Script
If the editor detects a script named `init_unreal.py` in any of its configured Python paths (e.g., `Content/Python` in the project folder), it automatically runs that script immediately upon startup [00:34:27, 00:42:51]. This is useful for project or plugin-specific initialization code [00:43:12].

### Project Settings Startup Scripts
In the project settings, specific Python scripts can be listed to run every time the project is opened [00:43:48]. These scripts run once the default level is fully loaded [00:44:52].

### From Editor-Only Blueprints
The [[Python support and plugins in Unreal Engine | Python Editor Script Plugin]] exposes new nodes in [[Using Blueprint Visual Scripting in Unreal Engine | Blueprint Visual Scripting]] specifically for editor-only Blueprint classes like Editor Utility Widgets and Editor Utility Blueprints [00:45:36, 00:49:33].
*   The `Execute Python Script` node allows running Python code snippets [00:51:52].
*   The `Execute File` execution mode can run `.py` files [00:59:08].
*   The `Execute Python Command` node can also be used [00:58:45].

## Python Environment and Paths in Unreal

Unreal's embedded Python interpreter runs in isolated mode by default [01:16:41]. When running Python scripts with a relative path or importing modules, Unreal Editor automatically adds several paths to Python's `sys.path` variable, including the `Content/Python` subfolder within the project folder [01:08:02].

Users can add [[Python support and plugins in Unreal Engine | additional paths]] for Python modules and scripts in the project settings under "Python" -> "Additional Paths" [01:11:57, 01:12:32]. This allows for importing custom modules from specified locations [01:14:43].

## Unreal Python Editor API (`unreal` module)

The [[Python support and plugins in Unreal Engine | Python Editor Script Plugin]] exposes a wide range of classes and functions through the `unreal` module, enabling interaction with the Unreal Editor, project assets, and level content [01:17:01]. This API mirrors much of what is exposed from C++ to [[Using Blueprint Visual Scripting in Unreal Engine | Blueprints]] [01:19:39].

### API Features and Conventions
*   **Automatic Type Conversion**: Python lists, sets, and dictionaries are automatically converted to Unreal's `UArray`, `USet`, or `UMap` types when passed [01:20:24].
*   **Inheritance Hierarchy**: Python classes maintain the same inheritance hierarchy as their C++ counterparts [01:20:39].
*   **Naming Conventions**: Classes and objects have the same names as in Blueprints. Properties are automatically exposed in lowercase snake_case, and enums are capitalized [01:26:40, 01:27:09].

### Best Practices for Using the Python API
*   **Asset Management**: Always use functions from the `unreal.EditorAssetLibrary` module for working with [[Creating and managing 3D assets and materials in Unreal Engine | assets]] (e.g., moving files) rather than Python's built-in file management modules. This ensures proper backend processes are triggered [01:36:55].
*   **Changing Editor Properties**: Use Python to access objects and set their configuration properties programmatically. For example, modifying static mesh actor properties like damage or visibility [01:37:25]. The `set_editor_property` function is recommended for this [01:38:28].
*   **Logging and Feedback**: Use `unreal.log()`, `unreal.log_warning()`, and `unreal.log_error()` for outputting messages to the log [01:38:58].
*   **Undo and Redo Support**: Operations that modify the editor state should be wrapped in an `unreal.ScopedEditorTransaction` context. This ensures that changes are recorded in the undo history, allowing users to revert them [01:39:07, 01:39:52].
*   **Slow Operations**: For scripts that perform many operations or work on numerous assets, `unreal.ScopedSlowTask` can be used to display a progress bar, providing feedback to the user during lengthy processes [01:44:25]. For example, `unreal.EditorLevelLibrary.spawn_actor_from_class` can be used to create actors like `FloatingTextActor` [01:40:20].

## Future Possibilities and Use Cases

The integration of Python in Unreal Engine opens up significant possibilities, particularly in content creation pipelines beyond traditional [[Game development using Unreal Engine 5 | game development]]. This includes workflows for movies and commercials, where Unreal Engine serves as a rendering pipeline [01:40:01, 01:46:25].

Potential advanced use cases include:
*   Integrating external Python libraries for deep learning models (e.g., PyTorch) directly into asset pipelines, enabling [[Using Python for asset management and procedural content generation in Unreal Engine | generative AI]] applications for content creation and manipulation [01:46:44, 01:47:16].
*   Implementing render farm solutions by having Unreal instances make REST requests to a server to determine work and send back results, allowing for complex, distributed content processing [01:42:00, 01:42:10].