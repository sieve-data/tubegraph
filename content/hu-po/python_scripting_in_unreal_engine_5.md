---
title: Python scripting in Unreal Engine 5
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[python_support_and_plugins_in_unreal_engine | Python scripting]] is supported in [[game_development_using_unreal_engine_5 | Unreal Engine 5]], specifically Unreal Engine 5.1, which was recently released at the time of this documentation <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This feature is crucial as Python has become a de facto language for production pipelines, especially with the rise of deep learning and generative AI models <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Why Use Python in Unreal Engine?

[[python_support_and_plugins_in_unreal_engine | Python]] is an excellent choice for [[automating_workflows_using_python_in_unreal_editor | automating workflows]] due to its ease of use <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It enables developers to:
*   Create and maintain large-scale [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | asset management systems]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Construct larger-scale [[integrating_python_scripts_with_unreal_engine_content_pipelines | asset management pipelines]] or workflows that link the Unreal Editor to other 3D applications <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   [[automating_workflows_using_python_in_unreal_editor | Automate time-consuming asset management tasks]], such as generating level of details (LODs) or static meshes, although Nanite in Unreal Engine 5 now handles LOD management automatically <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | Procedurally lay out content]] and control the Unreal Editor from custom UIs created in Python <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

> [!NOTE] Python scripting in Unreal Engine is primarily used *within* the editor for [[automating_workflows_using_python_in_unreal_editor | automation]] and [[integrating_python_scripts_with_unreal_engine_content_pipelines | pipeline integration]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It is not intended for running Python scripts as part of a compiled game executable <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Python libraries are not included in the final packaged executable <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Python Editor Script Plugin

[[python_support_and_plugins_in_unreal_engine | Python support]] in the Unreal Editor is provided by the **Python Editor Script Plugin** <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin includes an embedded version of Python 3.9.7, meaning you do not need to install Python separately on your computer <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

To enable the plugin:
1.  Launch the Unreal Engine 5.1 Editor <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
2.  Create a new project (e.g., a blank film and video project) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  Go into the Plugins section and ensure the "Python Editor Script" plugin is enabled <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Running Python Scripts

There are several ways to run [[python_support_and_plugins_in_unreal_engine | Python scripts]] within the Unreal Editor, each suited for different needs <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Unlike [[using_blueprint_visual_scripting_in_unreal_engine | Blueprints]], the Python environment is only available in the Unreal Editor, not when running the Unreal Engine in any other mode (e.g., packaged game or even playing in the editor) <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### 1. Python Console and Output Log

The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   Open the console input bar by pressing the tilde (`) key <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Change the input mode to Python.
*   Enter lines of Python code, which the editor executes immediately, similar to an interactive Python command line <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   Use `Shift + Enter` to separate multiple lines of code, or paste a multi-line block <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   To run a Python script file, type its name into the console (e.g., `pi <script_name.py>`) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Additional command-line arguments can be included after the script name <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### 2. From the File Menu

The File menu in the main Unreal Editor window offers options to run Python scripts:
*   **Execute Python Script**: Browse for a new script to run <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.
*   **Recent Python Scripts**: Rerun any script that was run previously <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.

### 3. On Project Startup

You can configure Unreal Engine to run Python scripts automatically when a project opens:
*   **`init_unreal.py`**: If the editor detects a script named `init_unreal.py` in any of the configured Python paths (e.g., `Content/Python` within your project), it automatically runs that script on startup <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>. This is useful for consistent initialization code across a project or plugin <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
*   **Project Settings Startup Scripts**: In your Project Settings, you can specify additional Python scripts to run every time you open that project <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>. Navigate to `Settings > Project Preferences > Plugins > Python > Startup Scripts` and add the desired script paths <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.

### 4. From Command Line

Python scripts can be run when starting the Unreal Editor from the command line:
*   The editor will shut down immediately after running the Python script <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.
*   **Full Editor Launch**: This approach launches the full Unreal Editor, opens the specified project, loads the default startup level, and runs the script once everything is loaded. This is suitable if your script needs to interact with project content or levels <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   **Headless Mode (Commandlet)**: A faster execution approach for scripts that don't require the full editor UI. It's trickier to load levels and assets in this mode <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. Arguments like `-run=pythonscript -script=<script_name.py>` can be used <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

### 5. From Blueprints

The Python Editor Script plugin exposes new nodes to [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]] for running Python code snippets <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.
*   These nodes are only available in editor-only [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint]] classes, such as Editor Utility Widgets and Editor Utility Blueprints <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>.
*   To use, create an `Editor Utilities > Editor Utility Blueprint` <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>. Within its Event Graph, you can use the `Execute Python Script` or `Execute Python Command` nodes <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
*   `Execute Python Script` node allows running a Python file directly <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.

## Python Environment and Paths

Unreal's embedded Python interpreter runs in isolated mode by default <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.
*   When using a relative path to run or import a Python script, the script must be in a path listed in the `sys.path` variable of the Python environment <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>.
*   The Unreal Editor automatically adds several paths to `sys.path`, including the `Content/Python` subfolder in your project folder <a class="yt-timestamp" data-t="01:08:16">[01:08:16]</a>.
*   Additional paths can be added via `Edit > Project Settings > Python > Additional Paths` <a class="yt-timestamp" data-t="01:12:03">[01:12:03]</a>. This allows importing custom Python modules from specified directories <a class="yt-timestamp" data-t="01:14:43">[01:14:43]</a>.

## Unreal Python Editor API

The Python Editor Script Plugin exposes a wide range of classes and functions through the `unreal` module <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>. This API allows interaction with the Unreal Editor, project assets, and level content <a class="yt-timestamp" data-t="01:17:07">[01:17:07]</a>.

### `unreal` Module
The `unreal` module reflects nearly everything exposed from C++ to [[using_blueprint_visual_scripting_in_unreal_engine | Blueprints]] in the editor environment <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>. As new plugins are enabled, anything they expose to [[using_blueprint_visual_scripting_in_unreal_engine | Blueprints]] also becomes available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.

### Data Type Conversion
The Python API converts Python lists, sets, and dicts to Unreal's `UArray`, `USet`, or `UMap` respectively <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>. This automatic type conversion simplifies interaction between Python and Unreal's native types <a class="yt-timestamp" data-t="01:26:33">[01:26:33]</a>. Python classes also maintain the same inheritance hierarchy as their Unreal counterparts <a class="yt-timestamp" data-t="01:20:39">[01:20:39]</a>.

### Naming Conventions
The API balances C++ and Python naming conventions:
*   Classes and objects have the same names as in [[using_blueprint_visual_scripting_in_unreal_engine | Blueprints]] <a class="yt-timestamp" data-t="01:26:49">[01:26:49]</a>.
*   Properties are automatically exposed as lowercase snake_case <a class="yt-timestamp" data-t="01:26:56">[01:26:56]</a>.
*   Enums use capital letters <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.

### Best Practices

*   **Working with Assets**: Always use functions from the `unreal` module (e.g., `unreal.EditorAssetLibrary`) to interact with assets in your project <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>. Avoid using Python's built-in file management modules directly with asset files <a class="yt-timestamp" data-t="01:37:01">[01:37:01]</a>.
*   **Changing Editor Properties**: Python scripts can access objects and set their configuration properties programmatically. Use the `set_editor_property` function for this <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.
*   **Logging and Feedback**: Use `unreal.log`, `unreal.log_warning`, and `unreal.log_error` for outputting messages to the log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Supporting Undo and Redo**: For operations that modify the editor, use `with unreal.ScopedEditorTransaction(...)` to ensure changes are included in the undo history <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
    *   Example: Spawning an actor and setting its location within a transaction <a class="yt-timestamp" data-t="01:40:12">[01:40:12]</a>.
*   **Process Dialogues for Slow Operations**: For operations involving many assets or actors that may take time, use `with unreal.ScopedSlowTask(...)` to display a progress bar in the editor, providing feedback to the user <a class="yt-timestamp" data-t="01:44:25">[01:44:25]</a>.

## Conclusion

[[python_support_and_plugins_in_unreal_engine | Python scripting in Unreal Engine 5]] offers a powerful way to [[integrating_python_scripts_with_unreal_engine_content_pipelines | integrate]] and [[automating_workflows_using_python_in_unreal_editor | automate complex workflows]], especially relevant for movie creation, commercials, and other content creation workflows where [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | procedural generation]] and generative AI are increasingly used <a class="yt-timestamp" data-t="01:46:25">[01:46:25]</a>. The ability to script the Unreal Editor, add objects, and change properties entirely in Python provides significant flexibility <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Future explorations may include running PyTorch code or integrating neural networks within the editor using Python <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.