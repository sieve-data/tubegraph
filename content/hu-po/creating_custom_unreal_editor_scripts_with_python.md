---
title: Creating custom Unreal Editor scripts with Python
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[using_python_in_unreal_engine_5 | Python in Unreal Engine 5]] is primarily used for automating tasks within the editor, managing assets, and building production pipelines. It is not used for running scripts within a compiled game executable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Key Uses
*   Constructing large-scale [[integrating_python_in_asset_management_and_production_pipelines | Asset Management Systems]] or workflows that link the Unreal Editor to other [[python_scripting_for_3d_applications_and_workflows | 3D applications]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   [[Automating work in Unreal Editor with Python | Automating time-consuming asset management tasks]], such as generating Levels of Detail (LODs) or static meshes, though Nanite in Unreal Engine 5 handles LODs automatically <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Procedurally laying out content <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Controlling the Unreal Editor from custom user interfaces (GUIs) created with Python, using modules like PySide and Qt for Python <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Enabling asset production pipelines that utilize deep learning <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Setup
Unreal Engine 5.1 was used for this demonstration <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
To enable Python scripting, the [[unreal_engine_plugin_management | Python Editor Script Plugin]] must be enabled in the Unreal Editor's plugin manager <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation is not required <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Running Python Scripts

Python scripts can be run in several ways within the Unreal Editor:

### Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Access the console input bar by pressing the tilde (`) key <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Enter single lines of Python code for immediate execution, similar to an interactive Python command line <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   Run multiple lines using `Shift + Enter` to separate lines or by pasting a multi-line block <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   Execute Python script files by typing their filename into the console <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Use the `py` command in the normal console to run the rest of the line as Python code <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    *   Example command: `py C:/Users/Public/Documents/Unreal Projects/PythonTest/Content/Python/arg_parse_test.py --num 10000` <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

### File Menu
The "File" menu in the main Unreal Editor window offers options to run Python script files:
*   `Execute Python Script`: Browse for and run a new script <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.
*   `Recent Python Scripts`: Rerun a previously executed script <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.

### Command Line
Python scripts can be specified in the command line arguments when starting the Unreal Editor <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. Additional command-line arguments required by the Python script can be included after the script name <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.
*   The editor shuts down immediately after script execution <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.
*   **Full Editor Launch**: Launches the full Unreal Editor, opens the specified project and default startup level, and then runs the script once everything is loaded. Useful for scripts that interact with project content or levels <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   **Headless Mode (Commandlet)**: A faster execution approach. It's trickier to load levels and other assets but is suitable for scripts that don't require the full editor UI <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. Arguments like `-run=PythonScript` and `script=<PathToScript>` are used <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

### Automatic Startup Scripts
*   **`init_unreal.py`**: If the editor detects a script named `init_unreal.py` in any configured Python paths, it automatically runs that script on startup. This is useful for project or plugin-specific initialization code <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>.
*   **Project Settings Startup Scripts**: In project settings, under `Plugins > Python`, specific Python scripts can be added to run every time the project is opened <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

### Editor-Only Blueprints
The [[unreal_engine_plugin_management | Python Editor Script Plugin]] exposes nodes to [[unreal_engine_plugin_management | Blueprint Visual Scripting]] for running Python code snippets <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>. These Python execution nodes are only available in editor-only Blueprint classes, such as [[unreal_engine_plugin_management | Editor Utility Widgets]] and [[unreal_engine_plugin_management | Editor Utility Blueprints]] <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>.
*   To execute a Python file from a Blueprint, the `Execute Python Script` node should be used, providing the full path to the `.py` file <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>.
*   Example: An [[unreal_engine_plugin_management | Editor Utility Blueprint]] (`python_script_runner`) can be set up to run a Python script on "Event Begin Play" by providing the script's path to an `Execute Python Script` node <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>.

## Python Environment Configuration
The Unreal Editor automatically adds several paths to Python's `sys.path` variable, including the `Content/Python` subfolder within the project directory <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>.
*   **Additional Paths**: Custom directories can be added to the Python path via `Edit > Project Settings > Python > Additional Paths` <a class="yt-timestamp" data-t="01:12:03">[01:12:03]</a>. This allows [[importing_python_libraries | importing custom Python modules]] located in those directories <a class="yt-timestamp" data-t="01:14:43">[01:14:43]</a>.
*   By default, Unreal's embedded Python interpreter runs in isolated mode <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.

## Unreal Python API (`unreal` module)
The `unreal` module exposes a wide range of classes and functions for interacting with the Unreal Editor, project assets, and level content <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.
*   It mirrors nearly everything exposed from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. New functionalities exposed by enabled plugins also become available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.
*   **Data Type Conversion**: Python lists, sets, and dictionaries are automatically converted to Unreal arrays, sets, or maps when passed to Unreal APIs <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.
*   **Naming Conventions**: Classes and objects maintain Blueprint names. Properties are exposed as lowercase snake_case, and enums are capitalized <a class="yt-timestamp" data-t="01:26:49">[01:26:49]</a>.

### Best Practices with the Python API
*   **Working with Assets**: Always use functions from the `unreal` module (e.g., `unreal.EditorAssetLibrary`) for asset operations (like moving files) instead of Python's built-in file management modules. This ensures proper handling of Unreal's internal asset management <a class="yt-timestamp" data-t="01:36:55">[01:36:55]</a>.
*   **Changing Editor Properties**: Access objects in the project and set their configuration properties programmatically. For example, a Python script can modify properties of `StaticMeshActors` in a level <a class="yt-timestamp" data-t="01:37:26">[01:37:26]</a>. It's recommended to use the `set_editor_property` function <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>.
*   **Logging and Feedback**: Use `unreal.log()`, `unreal.log_warning()`, and `unreal.log_error()` for outputting messages to the log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   [[Automating work in Unreal Editor with Python | Scoped Editor Transactions]] for Undo/Redo: Wrap operations that modify the editor state within `with unreal.ScopedEditorTransaction("Transaction Description")` blocks to ensure they are undoable <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
    *   Example: Creating and moving a `FloatingText` actor within a transaction <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.
*   [[Automating work in Unreal Editor with Python | Progress Dialogues]] for Slow Operations: For scripts that work on many assets or actors and take time to complete, use `with unreal.ScopedSlowTask(...)` to display a loading bar or progress dialogue, providing feedback to the user <a class="yt-timestamp" data-t="01:44:25">[01:44:25]</a>.

The ability to script the Unreal Editor, add objects, and change properties using Python is powerful, especially for integrating with [[integrating_python_in_asset_management_and_production_pipelines | production pipelines]] that leverage generative AI <a class="yt-timestamp" data-t="01:46:44">[01:46:44]</a>. Future explorations could include running PyTorch code or editing elements within the editor using neural networks <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.