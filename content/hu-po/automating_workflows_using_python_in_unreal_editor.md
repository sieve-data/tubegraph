---
title: Automating workflows using Python in Unreal Editor
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[python_scripting_in_unreal_engine_5 | Python scripting in Unreal Engine 5]] and 5.1 is primarily used within the Unreal Editor to automate tasks and build robust content pipelines, rather than for in-game execution within a built executable [00:30:07].

## Why Use Python for Automation?

Python has become a de facto language for production pipelines, a trend expected to grow with the rise of deep learning and generative AI models [01:00:00]. It is considered one of the easiest programming languages [01:36:00].

Key advantages for automation include:
*   **Ease of Use** Python is easy to learn and use for scripting [01:36:00].
*   **Workflow Automation** It's a great choice for automating workflows [01:31:00].
*   **Large-Scale Asset Management** Python makes it easier to create and maintain large-scale [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | asset management systems]] [01:26:00].
*   **Full-Featured UIs** It supports full-featured user interfaces through modules like PySide and Qt for Python [01:42:00].

## Key Use Cases in Unreal Editor

Python in the Unreal Editor can be used to:
*   Construct larger-scale [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | asset management pipelines]] or workflows that link the Unreal Editor to other 3D applications [02:31:00].
*   Automate time-consuming [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | asset management]] tasks like generating level of details (LODs) or static meshes, though some of this is now handled by Nanite in [[game_development_using_unreal_engine_5 | Unreal Engine 5]] [02:39:00].
*   [[using_python_for_asset_management_and_procedural_content_generation_in_unreal_engine | Procedurally lay out content]] and control the Unreal Editor from custom user interfaces created in Python [03:00:00].

## Enabling Python Support

To use Python in Unreal Editor, the "Python Editor Script Plugin" must be enabled [03:43:00]. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation is not required on the computer [03:36:00].

## Running Python Scripts

Python scripts can be executed in several ways within the Unreal Editor:

### Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands by pressing the tilde (~) key [08:14:00].
*   Individual lines of Python code can be executed immediately, similar to an interactive Python command line [08:40:00].
*   Multiple lines can be entered by using Shift+Enter to separate lines or by pasting a multi-line block [08:56:00].
*   Python script files can be executed by typing their file name into the console, optionally including command-line arguments [09:08:00]. The `pi` command can also be used in the normal console to run the rest of the line as Python code [09:27:00].

### From the Command Line
Python scripts can be specified in the command line arguments when launching the Unreal Editor. The editor will shut down immediately after running the script [03:05:00].
*   **Full Editor Launch**: The full Unreal Editor launches, loads the project and default level, and then runs the script. This is suitable for scripts interacting with project content or levels [03:13:00].
*   **Headless Mode (Commandlet)**: This approach is faster and suitable for scripts that can run without a full UI. It can be trickier to load levels or assets [03:47:00].

### Startup Scripts
The Unreal Editor can be configured to automatically run Python scripts on startup.
*   **`init_unreal.py`**: If a script named `init_unreal.py` is detected in any configured Python paths (e.g., in the `Content/Python` subfolder of a project or plugin), it runs automatically upon editor launch [04:51:00, 01:10:07]. This is useful for project- or plugin-specific initialization code [04:07:00].
*   **Project Settings**: Any number of Python scripts can be specified in the project settings to run every time that specific project is opened [04:48:00]. These scripts run after the default startup level is fully loaded [04:52:00].

### From Editor-Only Blueprints
The [[python_support_and_plugins_in_unreal_engine | Python Editor Script Plugin]] exposes new nodes in the [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]] system to run Python code snippets [04:39:00]. These Python execution nodes are only available in editor-only Blueprint classes, such as Editor Utility Widgets and Editor Utility Blueprints [04:47:00, 04:50:00].

## Python Environment
Unreal Engine's embedded Python interpreter runs in isolated mode by default [01:43:00].
*   **`sys.path`**: The Unreal Editor automatically adds several paths to Python's `sys.path` variable, including the `Content/Python` subfolder within the project [01:08:02].
*   **Additional Paths**: Users can add custom paths to the Python environment via project settings, allowing the import of external Python modules [01:12:00].

## Unreal Python API (`unreal` Module)

The `unreal` module, exposed by the Python Editor Script Plugin, provides a wide range of classes and functions to interact with the Unreal Editor, project assets, and level content [01:17:01].
*   It exposes nearly everything available from C++ to Blueprints within the editor environment [01:43:00].
*   As new plugins are enabled, anything they expose to Blueprints also becomes available in Python [01:55:00].
*   **Data Type Conversion**: Python lists, sets, and dictionaries are automatically converted to Unreal's equivalent `UArray`, `USet`, or `UMap` types [02:24:00, 02:37:00].
*   **Inheritance Hierarchy**: Python classes maintain the same inheritance hierarchy as their C++ and Blueprint counterparts [02:40:00].
*   **Naming Conventions**: The API balances C++ and Python naming conventions. Classes and objects have the same names as in Blueprints. Properties are automatically exposed as lowercase snake_case, and enums as capital snake_case [02:49:00].

## Best Practices

*   **Working with Assets**: Always use functions from the `unreal` module for asset operations (e.g., moving files, [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | asset management]]) instead of Python's built-in file management modules. This ensures Unreal's internal asset management is correctly updated [01:36:58].
*   **Changing Editor Properties**: Use Python to access objects and programmatically set their configuration properties, such as static mesh actor properties (e.g., damageable, hidden in game) [01:37:25]. It's recommended to use functions like `set_editor_property` instead of direct assignment [01:38:26].
*   **Logging and Feedback**: Use `unreal.log`, `unreal.log_warning`, and `unreal.log_error` for outputting messages to the log [01:38:58].
*   **Supporting Undo and Redo**: Operations that modify the editor state can be wrapped in `unreal.ScopedEditorTransaction` to ensure they are part of the undo/redo history [01:39:52].
*   **Process Dialogues for Slow Operations**: For scripts that process many assets or actors and might take time, use `unreal.ScopedSlowTask` to display progress bars, preventing the editor from appearing frozen [01:44:43].

## Conclusion

Python provides a powerful and flexible way to automate tasks within the Unreal Editor. It enables complex workflows, especially for [[integrating_python_scripts_with_unreal_engine_content_pipelines | content pipelines]] involving generative AI models or movie creation, where the final product is images or sequences rather than a game executable [01:46:17]. Future possibilities include integrating Python-based deep learning frameworks like PyTorch to modify or generate content directly within the editor [01:47:20].