---
title: Using Python for asset management and procedural content generation in Unreal Engine
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

Python has emerged as a crucial language for production pipelines, a trend expected to grow further with the rise of deep learning and generative AI models <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Its ease of use makes it an excellent choice for automating workflows and creating and maintaining large-scale asset management systems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Why Python in Unreal Engine?

[[python_scripting_in_unreal_engine_5 | Python scripting in Unreal Engine 5]] (specifically Unreal Engine 5.1) allows users to:
*   Construct large-scale [[integrating_python_scripts_with_unreal_engine_content_pipelines | asset management pipelines]] or workflows that connect the Unreal Editor to other 3D applications <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   [[automating_workflows_using_python_in_unreal_editor | Automate time-consuming asset management tasks]], such as generating Levels of Detail (though Nanite, a built-in system in Unreal Engine 5, now manages this automatically) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Procedurally lay out content and control the Unreal Editor through custom User Interfaces (UIs) created in Python <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

It is important to note that Python in Unreal Engine is primarily used within the editor itself for automation and scripting, not for running scripts as part of a built game executable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Python libraries and scripts are generally not included in the final packaged game <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Python Support and Environment

[[python_support_and_plugins_in_unreal_engine | Python support in the Unreal Editor]] is provided by the Python Editor Script plugin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation on the computer is not required <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Running Python Scripts

There are several ways to execute Python scripts in the Unreal Editor:

### Python Console and Output Log
The Unreal Editor's console input bar can accept Python code. This can be accessed by pressing the tilde key (~) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Users can type and execute Python code line by line, similar to an interactive Python shell <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Multiple lines can be entered using Shift+Enter or by pasting a multi-line block <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

Python script files can also be run by typing `pi` followed by the file path and any command-line arguments into the console <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### File Menu Options
In the main window of the Unreal Editor, the "File" menu offers "Execute Python Script" to browse for new scripts and "Recent Python Scripts" to rerun previously executed scripts <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

### Command Line Execution
Unreal Editor can be launched from the command line to specify and run a Python script <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. There are two primary modes:
1.  **Full Editor Launch**: The full Unreal Editor launches, opens a specified project, loads the default startup level, and then runs the Python script once everything is loaded <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>. This is useful for scripts interacting with project content or levels <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>.
2.  **Headless Mode (Commandlet)**: A faster approach where scripts can be run in a headless mode using the `runpythonscript` argument <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.

### Startup Scripts
*   **`init_unreal.py`**: If the editor detects a script named `init_unreal.py` in any configured Python paths, it automatically runs that script immediately upon startup <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>. This is suitable for project-wide initialization code <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
*   **Project Settings**: Users can specify any number of Python scripts to run every time a project is opened via the Project Settings <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>. These can be added under `Project Settings > Plugins > Python > Startup Scripts` <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.

### [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]]
The Python script plugin exposes nodes to Blueprint Visual Scripting that can be used to run Python code snippets <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. These Python execution nodes are exclusively available in editor-only Blueprint classes, such as Editor Utility Widgets and Editor Utility Blueprints <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>.

## Python Path and External Modules

When running Python scripts or importing modules using a relative path, the Unreal Editor automatically adds several paths to the `sys.path` variable of the Python environment <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>. This includes the `Content/Python` subfolder within the project folder <a class="yt-timestamp" data-t="01:08:21">[01:08:21]</a>.

Additional paths can be configured manually in the Project Settings under `Project Settings > Python > Additional Paths` <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. This allows for the integration of custom Python modules and libraries <a class="yt-timestamp" data-t="01:14:42">[01:14:42]</a>.

## Unreal Python API (`unreal` module)

The [[integrating_python_scripts_with_unreal_engine_content_pipelines | Python Editor Script plugin]] exposes a wide range of classes and functions through the `unreal` module, enabling interaction with the Unreal Editor, project assets, and level content <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.

The `unreal` module mirrors nearly everything exposed from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>. As new plugins are enabled, anything they expose to Blueprints also becomes available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.

### Data Type Conversion and Naming Conventions
The API automatically converts Python lists, sets, and dictionaries to Unreal's `UArray`, `USet`, or `UMap` equivalents <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>. Python classes maintain the same inheritance hierarchy as their C++ counterparts <a class="yt-timestamp" data-t="01:20:39">[01:20:39]</a>.

Naming conventions balance C++ and Python standards:
*   Classes and objects in the Python API share the same names as in Blueprints <a class="yt-timestamp" data-t="01:26:49">[01:26:49]</a>.
*   Blueprint properties are automatically exposed as `lowercase_snake_case` <a class="yt-timestamp" data-t="01:26:55">[01:26:55]</a>.
*   Enums are typically capitalized <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.

### Best Practices and Functionality
*   **Working with Assets**: Always use functions from the `unreal` module (e.g., `unreal.EditorAssetLibrary`) for [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | asset management]] rather than Python's built-in file management modules. This ensures proper backend processes are handled <a class="yt-timestamp" data-t="01:36:55">[01:36:55]</a>.
*   **Changing Editor Properties**: Python scripts can access and set configuration properties of objects in the project programmatically, such as modifying static mesh actors in a level <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.
*   **Undo/Redo Support**: The `unreal.ScopedEditorTransaction` context manager can be used to group operations, allowing them to be undone or redone as a single action <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Process Dialogues/Progress Bars**: For long-running operations that affect many assets or actors, `unreal.ScopedSlowTask` can be used to display a progress bar, providing user feedback and preventing the editor from appearing frozen <a class="yt-timestamp" data-t="01:44:40">[01:44:40]</a>.

For example, creating a new actor and setting its location can be done using `unreal.EditorLevelLibrary.spawn_actor_from_class` and `set_actor_location` <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

## Conclusion

The integration of Python within Unreal Engine provides a powerful toolset for [[integrating_python_scripts_with_unreal_engine_content_pipelines | automating content creation]] and managing complex asset pipelines, especially for workflows extending beyond traditional [[game_development_using_unreal_engine_5 | game development]] into areas like movie creation, commercials, and other forms of digital content <a class="yt-timestamp" data-t="01:46:25">[01:46:25]</a>. Its capabilities are particularly relevant for leveraging generative AI models in asset and content creation <a class="yt-timestamp" data-t="01:46:44">[01:46:44]</a>. Future explorations could involve running PyTorch code or editing assets within the editor using neural networks <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.