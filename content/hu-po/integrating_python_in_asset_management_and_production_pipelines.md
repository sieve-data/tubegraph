---
title: Integrating Python in asset management and production pipelines
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

This article explores the capabilities of [[using_python_in_unreal_engine_5 | Python in Unreal Engine 5]], specifically focusing on its application in asset management and production pipelines within Unreal Engine 5.1 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Python's Role in Production Pipelines

Python has emerged as the de facto language for production pipelines <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This trend is expected to accelerate with the rise of deep learning and generative AI models like Stable Diffusion, which are increasingly based on Python <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="01:46:44">[01:46:44]</a>. Its ease of use makes it a suitable choice for [[python_scripting_for_3d_applications_and_workflows | automating workflows]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> and creating and maintaining large-scale asset management systems <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Python can also facilitate full-featured user interfaces through modules like PySide <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Key Applications in Unreal Editor

[[automating_work_in_unreal_editor_with_python | Python in the Unreal Editor]] is primarily used to:
*   Construct large-scale asset management pipelines or workflows that integrate Unreal Editor with other 3D applications used in an organization <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Automate time-consuming asset management tasks, such as generating levels of detail (LODs) or static meshes, although Nanite now handles LOD management automatically in Unreal Engine 5 <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   Procedurally lay out content and control the Unreal Editor from custom UIs created in Python <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

It is important to note that Python scripts are executed *within the editor* and are not intended to run as part of a built game executable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Its main utility is in scripting and automation for asset production pipelines, particularly those that leverage deep learning <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

## Enabling and Running Python Scripts

To use Python in Unreal Editor, the "Python Editor Script Plugin" must be enabled <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Unreal Engine 5.1 includes an embedded version of Python 3.9.7, eliminating the need for a separate Python installation on the system <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Methods of Execution

There are several ways to [[creating_custom_unreal_editor_scripts_with_python | run Python scripts]] within Unreal Editor:

*   **Python Console and Output Log**: The editor's console input bar can be switched to accept Python code by pressing the tilde (~) key. This allows for line-by-line execution, or multi-line code via `Shift+Enter` or pasting <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Python script files can also be run by typing their names into the console using the `pi` command <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **File Menu**: The main window's File menu offers "Execute Python Script" to browse and run scripts, and "Recent Python Scripts" to re-run previously executed ones <a class="yt-timestamp" data-t="01:31:44">[01:31:44]</a>.
*   **Command Line on Editor Startup**: Unreal Editor can launch and execute Python scripts directly from the command line. This can be done in full editor mode (good for scripts interacting with project content) or in a faster, headless commandlet mode (trickier for loading levels) <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>, <a class="yt-timestamp" data-t="01:33:47">[01:33:47]</a>.
*   **Automatic Startup Scripts**:
    *   **`init_unreal.py`**: If a script named `init_unreal.py` is found in a configured Python path (e.g., `Content/Python` subfolder), it automatically runs when the editor starts. This is useful for project-specific initialization <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>, <a class="yt-timestamp" data-t="01:43:07">[01:43:07]</a>.
    *   **Project Settings**: Python scripts can be added to the project settings to run every time that specific project is opened <a class="yt-timestamp" data-t="01:43:48">[01:43:48]</a>.
*   **Editor-Only Blueprints**: The Python Script plugin exposes nodes in Blueprint visual scripting, allowing Python code snippets or files to be run from editor-only Blueprint classes like Editor Utility Widgets and Editor Utility Blueprints <a class="yt-timestamp" data-t="01:45:36">[01:45:36]</a>, <a class="yt-timestamp" data-t="01:49:33">[01:49:33]</a>.

## Python Environment and Module Management

The Unreal Editor automatically adds certain paths to Python's `sys.path` variable, including the `Content/Python` subfolder within a project <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>. Users can also specify [[importing_python_libraries | additional paths]] in the Project Settings under Python, allowing for custom modules to be imported and used <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>, <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Unreal Editor Python API (`unreal` module)

The Python Editor Script plugin exposes a comprehensive API contained within the `unreal` module <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>. This API mirrors most of what is exposed from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. Enabling new plugins also makes their Blueprint-exposed functionalities available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.

### API Features and Best Practices

*   **Data Type Conversion**: Python lists, sets, and dictionaries are automatically converted to their corresponding Unreal (U) array, set, or map types when passed to the API <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>, <a class="yt-timestamp" data-t="01:20:37">[01:20:37]</a>. The API ensures consistency with base Python types <a class="yt-timestamp" data-t="01:25:30">[01:25:30]</a>.
*   **Inheritance Hierarchy**: Python classes maintain the same inheritance hierarchy as their native Unreal counterparts <a class="yt-timestamp" data-t="01:20:41">[01:20:41]</a>.
*   **Naming Conventions**: The API blends C++ and Python naming conventions; classes and objects retain their Blueprint names, while properties are exposed as lowercase snake case <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>.
*   **Asset Management**: Always use functions from the `unreal` module (e.g., `unreal.editor_asset_library`) for working with assets in the project, rather than Python's built-in file management modules <a class="yt-timestamp" data-t="01:36:55">[01:36:55]</a>, <a class="yt-timestamp" data-t="01:37:16">[01:37:16]</a>.
*   **Property Modification**: Use the `set_editor_property` function to programmatically set configuration properties of objects <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>, <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>.
*   **Logging**: The `unreal` module provides functions for logging messages, warnings, and errors to the output log (e.g., `unreal.log`, `unreal.log_warning`, `unreal.log_error`) <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Undo/Redo Support**: For operations that modify the editor state, `unreal.ScopedEditorTransaction` can be used to group changes into a single undo/redo transaction <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Progress Dialogues**: For long-running operations on many assets or actors, `unreal.ScopedSlowTask` can display a progress bar to the user, providing feedback <a class="yt-timestamp" data-t="01:44:43">[01:44:43]</a>.

## Future Potential

The ability to script and [[using_ai_integration_in_coding_environments | automate work in Unreal Editor with Python]], including adding objects, changing properties, and interacting with core functionalities, is powerful <a class="yt-timestamp" data-t="01:46:57">[01:46:57]</a>. This capability opens doors for integrating external Python libraries, such as PyTorch for neural networks, allowing for advanced [[challenges_and_solutions_in_modern_computer_vision_pipelines | AI integration]] into content creation workflows and asset processing within Unreal Engine <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>. The flexibility of Unreal's Python integration allows for complex tasks like sending rendered images to cloud-based models and receiving processed data back <a class="yt-timestamp" data-t="01:42:14">[01:42:14]</a>.