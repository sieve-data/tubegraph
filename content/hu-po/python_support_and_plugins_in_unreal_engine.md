---
title: Python support and plugins in Unreal Engine
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[python_scripting_in_unreal_engine_5 | Python scripting in Unreal Engine 5]] (specifically Unreal Engine 5.1, as seen in the transcript) is supported through a dedicated plugin, providing powerful capabilities for [[automating_workflows_using_python_in_unreal_editor | automating workflows]] and managing content within the editor <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

## Why Use Python in Unreal Engine?

Python has become a de facto language for production pipelines, a trend expected to increase with the rise of deep learning and generative AI models <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Its ease of use makes it a strong choice for:
*   **Asset Management**: Creating and maintaining large-scale [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | asset management]] systems <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.
*   **Workflow Automation**: Automating time-consuming tasks like generating level of details (LODs) or static meshes (though Nanite in UE5 handles LODs automatically) <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.
*   **Procedural Content Generation**: [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | Procedurally laying out content]] and controlling the Unreal Editor from custom user interfaces (UIs) built with Python modules like PySide/PySideQT <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Pipeline Integration**: Tying the Unreal Editor to other 3D applications used in an organization <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Deep Learning Integration**: Facilitating asset production pipelines that leverage deep learning, as most deep learning frameworks are Python-based <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

## Python Environment and Scope

Python support in Unreal Engine is primarily for editor functionality and pipeline automation, not for runtime game logic <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Editor-Only**: The Python environment is only available within the Unreal Editor <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. It does not run as part of a built executable game, meaning no Python libraries or scripts are included in the final packaged product <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Embedded Python**: The Python Editor Script plugin contains an embedded version of Python 3.9.7, so a separate Python installation is not required on the user's computer <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Plugin**: The core functionality is provided by the "Python Editor Script" plugin, which needs to be enabled in the Unreal Editor <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>, <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

## Running Python Scripts

There are several ways to execute Python scripts within the Unreal Editor:

### 1. Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Interactive Mode**: Pressing the `~` (tilde) key brings up the console input bar, allowing users to enter and execute single lines of Python code immediately <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>, <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>. Multiple lines can be entered using `Shift + Enter` or by pasting multi-line blocks <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
*   **Running Script Files**: Python script files can be executed by typing their full path (e.g., `C:/path/to/script.py`) into the console <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>, <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>. Command-line arguments can be included after the script name <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
*   **`pi` Command**: In the normal console, the `pi` command can be used to run the rest of the line as Python code <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.

### 2. File Menu
The "File" menu in the Unreal Editor's main window offers options to "Execute Python Script" (to browse and run a new script) or "Recent Python Scripts" (to rerun previously executed scripts) <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

### 3. Command Line
Python scripts can be specified in the command-line arguments when starting the Unreal Editor. In both command-line approaches, the editor shuts down immediately after the script finishes <a class="yt-timestamp" data-t="32:51:00">[32:51:00]</a>.
*   **Full Editor Launch**: The full Unreal Editor launches, loads the specified project and default startup level, then runs the Python script once everything is loaded. This is suitable for scripts that interact with project content or levels <a class="yt-timestamp" data-t="33:13:00">[33:13:00]</a>.
*   **Headless Mode (Commandlet)**: A faster execution method where scripts run in headless mode. While quicker, it's trickier to load levels and assets <a class="yt-timestamp" data-t="33:47:00">[33:47:00]</a>.

### 4. Startup Scripts
Python scripts can be configured to run automatically when the Unreal Editor starts:
*   **`init_unreal.py`**: If a script named `init_unreal.py` is detected in one of the configured Python paths (e.g., `Content/Python` subfolder within a project or plugin), it will automatically run upon editor startup. This is useful for project- or plugin-specific initialization code <a class="yt-timestamp" data-t="42:51:00">[42:51:00]</a>, <a class="yt-timestamp" data-t="43:10:00">[43:10:00]</a>.
*   **Project Settings**: Users can specify any number of Python scripts in their project settings to run every time that specific project is opened <a class="yt-timestamp" data-t="43:48:00">[43:48:00]</a>. This is found under `Project Settings > Python > Startup Scripts` <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>.

### 5. [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]]
The Python Editor Script plugin exposes new nodes to [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]] that can execute Python code snippets <a class="yt-timestamp" data-t="45:36:00">[45:36:00]</a>.
*   **Editor-Only Blueprints**: These Python execution nodes are only available in editor-only Blueprint classes, such as Editor Utility Widgets and Editor Utility Blueprints (e.g., Editor Utility Action Objects) <a class="yt-timestamp" data-t="45:48:00">[45:48:00]</a>, <a class="yt-timestamp" data-t="50:22:00">[50:22:00]</a>.
*   **Execution Nodes**: Nodes like "Execute Python Script" allow calling Python files with arguments <a class="yt-timestamp" data-t="58:35:00">[58:35:00]</a>.

## Python Environment Configuration

*   **`sys.path`**: When running a Python script with a relative path or importing a module, Unreal's Python environment automatically adds several paths to the `sys.path` variable, including the `Content/Python` subfolder in the project directory <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **[[integrating_python_scripts_with_unreal_engine_content_pipelines | Additional Paths]]**: Custom Python module paths can be added in `Project Settings > Python > Additional Paths` <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This allows importing custom Python modules from specified directories <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Isolated Mode**: By default, Unreal's embedded Python interpreter runs in isolated mode <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Unreal Python Editor API

The Python Editor Script plugin exposes a wide range of classes and functions through the `unreal` module, allowing interaction with the Unreal Editor, project assets, and content within levels <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.
*   **API Coverage**: This API reflects nearly everything exposed from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>. As new plugins are enabled, anything they expose to Blueprints also becomes available in Python <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Data Type Conversion**: Python lists, sets, and dictionaries are automatically converted to their Unreal counterparts (UArray, USet, UMap) <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. Unreal classes maintain the same inheritance hierarchy in Python <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   **Naming Conventions**: The API balances C++ and Python naming conventions. Classes and objects have the same names as in Blueprints, while properties are automatically exposed as lowercase snake_case <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>. Enums typically follow a capital naming convention <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.
*   **Asset Interaction**: When working with assets, it's crucial to use functions from the `unreal` module (e.g., `unreal.EditorAssetLibrary`) instead of Python's built-in file management modules to ensure proper asset handling <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>.
*   **Editor Property Modification**: Python scripts can access objects and set their configuration properties programmatically (e.g., modifying static mesh actor properties in a level) <a class="yt-timestamp" data-t="01:37:26">[01:37:26]</a>.
*   **Logging**: The `unreal` module provides logging functions like `unreal.log`, `unreal.log_warning`, and `unreal.log_error` for outputting messages to the log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Undo/Redo Support**: Operations that modify the editor state can be wrapped in `unreal.ScopedEditorTransaction` to ensure they are recorded in the undo/redo history <a class="yt-timestamp" data-t="01:39:15">[01:39:15]</a>, <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Slow Operations**: For scripts that perform many operations and might take time, `unreal.ScopedSlowTask` can be used to display a progress bar in the editor <a class="yt-timestamp" data-t="01:44:43">[01:44:43]</a>.

The ability to script the Unreal Editor, add objects, and change properties using Python is a powerful feature that supports complex [[game_development_using_unreal_engine_5 | content creation workflows]], especially with the growing use of generative AI <a class="yt-timestamp" data-t="01:46:21">[01:46:21]</a>.