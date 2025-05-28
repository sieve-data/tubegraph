---
title: Automating work in Unreal Editor with Python
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[using_python_in_unreal_engine_5 | Python in Unreal Engine 5]] is a powerful tool primarily used for automating tasks and building robust production pipelines within the Unreal Editor <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It is particularly relevant for [[integrating_python_in_asset_management_and_production_pipelines | asset management]] and workflows, especially with the rise of [[using_ai_integration_in_coding_environments | deep learning]] and [[ai_agents_and_automation | generative AI]] models like Stable Diffusion, which are often Python-based <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Key Capabilities and Role of Python

Python's integration allows users to:
*   Construct larger-scale [[integrating_python_in_asset_management_and_production_pipelines | asset management systems]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Automate time-consuming asset management tasks, such as generating levels of detail (though Nanite in Unreal Engine 5 now handles this automatically) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Tie the Unreal Editor to other [[python_scripting_for_3d_applications_and_workflows | 3D applications]] used in an organization <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Procedurally lay out content <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Control the Unreal Editor from custom user interfaces designed with Python modules like PySideQT <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, allowing for GUI creation <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

It's crucial to note that Python scripts in Unreal Engine 5 are primarily for **editor automation** <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> and **asset production pipelines** <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. They are **not** used for running within the game itself or as part of a built executable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The final packaged game will not contain Python libraries or scripts <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Python Editor Script Plugin

Python support in the Unreal Editor is provided by the [[unreal_engine_plugin_management | Python Editor Script Plugin]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation is not required on the user's computer <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. To enable Python scripting, this plugin must be activated in the Unreal Editor <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Running Python Scripts

There are several ways to execute Python scripts within Unreal Engine:

### Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This console can be accessed by pressing the tilde key (`~`) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **Line-by-line execution**: Users can enter single lines of Python code for immediate execution <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Multi-line input**: Shift+Enter can be used to separate lines, or multi-line blocks can be pasted <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Running script files**: Python script files can be executed by typing `pi` followed by the file path and any arguments into the console <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Running Scripts on Editor Startup
Unreal Editor provides mechanisms to run Python scripts automatically upon loading a project:
*   **`init_unreal` script**: If a script named `init_unreal.py` is detected in any configured Python paths (e.g., `Content/Python` folder within a project or plugin), it automatically runs immediately when the editor starts <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a> <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a> <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. This is useful for project-specific or plugin-specific initialization code <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
*   **Project Settings**: In the project settings, under the Python section, users can specify any number of Python scripts to run every time the project is opened <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

### Running Scripts from the Command Line
Python scripts can also be executed when launching the Unreal Editor from the command line:
*   **Full editor launch**: This approach launches the full Unreal Editor, opens the specified project and default level, and then runs the Python script once everything is loaded. This is suitable for scripts that interact with project content or levels <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   **Headless mode (Commandlet)**: This is a faster execution method where the script can run in headless mode using a commandlet, though loading levels and assets might be trickier <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.

### [[creating_custom_unreal_editor_scripts_with_python | Blueprint Integration]]
The Python Script plugin exposes nodes to Blueprint visual scripting, allowing users to run Python code snippets <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.
*   **Editor-only Blueprints**: Python execution nodes are only available in editor-only Blueprint classes, such as Editor Utility Widgets and Editor Utility Blueprints <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>. This means a standard Blueprint, like a Scene Component, cannot directly run Python scripts <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a>.
*   **`Execute Python Script` node**: Within an Editor Utility Blueprint, the `Execute Python Script` node can be used to run a specified Python file <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>.

## Python Environment and API

### Python Paths
When running Python scripts with relative paths or importing modules, Unreal Editor automatically adds several directories to the `sys.path` variable of the Python environment <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>. This includes the `Content/Python` subfolder within the project directory <a class="yt-timestamp" data-t="01:08:21">[01:08:21]</a>. Additional paths can also be explicitly added in the Project Settings under the Python section <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. By default, Unreal's embedded Python interpreter runs in isolated mode <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.

### Unreal Python API
The [[integrating_python_in_asset_management_and_production_pipelines | Unreal Python API]] is contained within the `unreal` module <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>. This API exposes a wide range of classes and functions that allow interaction with the Unreal Editor, project assets, and level content <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>. It exposes nearly everything available from C++ to Blueprints, and as new plugins are enabled, their Blueprint-exposed features also become available in Python <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>.

#### Data Type Conversion and Naming Conventions
The API converts Python data types (like lists, sets, and dicts) to Unreal equivalents (UArrays, USets, UMaps) automatically <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>. Python classes maintain the same inheritance hierarchy as their Unreal counterparts <a class="yt-timestamp" data-t="01:20:40">[01:20:40]</a>. Naming conventions strive for a balance between C++ and Python standards:
*   Classes and objects use the same names as in Blueprints <a class="yt-timestamp" data-t="01:26:49">[01:26:49]</a>.
*   Blueprint properties are exposed as `lowercase_snake_case` <a class="yt-timestamp" data-t="01:26:55">[01:26:55]</a>.
*   Enums are typically capitalized <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.

### Best Practices for Using the Python API
*   **Asset Management**: Always use functions from the `unreal` module (e.g., `editor_asset_library`) for working with assets in the project. Avoid using Python's built-in file management modules directly with asset files <a class="yt-timestamp" data-t="01:36:55">[01:36:55]</a>.
*   **Changing Editor Properties**: Access objects and set configuration properties programmatically using functions like `set_editor_property` <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.
*   **Logging and Feedback**: Use `unreal.log`, `unreal.log_warning`, and `unreal.log_error` for outputting information to the log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Supporting Undo and Redo**: Operations that modify the editor state should be wrapped in `with unreal.ScopedEditorTransaction("Transaction Name")` to ensure they are part of the undo/redo history <a class="yt-timestamp" data-t="01:39:07">[01:39:07]</a> <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Process Dialogues for Slow Operations**: For long-running scripts (e.g., those processing many assets), `with unreal.ScopedSlowTask("Task Description", is_
`cancelable=True)` can be used to display a loading bar and allow users to cancel the operation <a class="yt-timestamp" data-t="01:44:25">[01:44:25]</a>.

## Practical Applications

Python in Unreal Engine is increasingly valuable for:
*   **Movie Creation**: Automating rendering queues and manipulating scene elements between renders, allowing for dynamic changes to lighting or objects <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
*   **Integration with AI**: Sending rendered images to external models (e.g., served on the cloud via REST requests) for style transfer or other [[using_ai_integration_in_coding_environments | AI-driven modifications]], then receiving results back into the pipeline <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>.
*   **Render Farms**: Implementing advanced plugins that connect to render farms via sockets or REST requests to distribute work <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

The ability to script the Unreal Editor, add objects, change properties, and integrate external Python libraries makes it a very powerful tool for content creation workflows beyond traditional game development <a class="yt-timestamp" data-t="01:46:25">[01:46:25]</a>.