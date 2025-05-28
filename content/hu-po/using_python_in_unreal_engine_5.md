---
title: Using Python in Unreal Engine 5
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

Unreal Engine 5 (UE5) integrates Python, making it a de facto language for production pipelines, especially with the rise of deep learning and generative AI models like Stable Diffusion <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Python's ease of use makes it an excellent choice for [[automating_work_in_unreal_editor_with_python | automating workflows]] and [[integrating_python_in_asset_management_and_production_pipelines | creating and maintaining large-scale asset management systems]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Key Capabilities of Python in Unreal Editor

[[python_scripting_for_3d_applications_and_workflows | Python scripting]] in Unreal Editor allows users to:
*   Construct large-scale asset management pipelines <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Tie the Unreal Editor to other 3D applications used in an organization <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Automate time-consuming asset management tasks, though some, like generating Levels of Detail (LODs) for static meshes, are now handled by Nanite in UE5 <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Procedurally lay out content and control the Unreal Editor from custom Python UIs built with modules like PySide <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

It's crucial to note that Python scripts primarily function *within the editor* for automation and asset pipeline tasks <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. They are **not** executed as part of a built game executable and are not included in the final packaged game <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Enabling Python Support

To use Python, the `Python Editor Script Plugin` must be enabled <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin includes an embedded version of Python 3.9.7, meaning a separate Python installation is not required on your system <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Running Python Scripts

Several methods exist for running Python scripts in the Unreal Editor:

### Python Console and Output Log
The Unreal Editor's console input bar can be switched to accept Python code instead of Unreal console commands <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This is accessed by pressing the tilde key (`~`) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **Line by Line Execution:** Type individual lines of Python code, and the editor executes each immediately, similar to an interactive Python shell <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Multi-line Code:** Use `Shift+Enter` to separate lines or paste a multi-line block <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Running Script Files:** Execute a Python script file by typing its filename into the console. Command line arguments can be included after the script name <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. The `pi` command can also be used in the normal console to run the rest of the line as Python code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### File Menu Options
The `File` menu in the main Unreal Editor window offers `Execute Python Script` to browse for a new script, and `Recent Python Scripts` to rerun previously executed scripts <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

### Command Line Startup
Python scripts can be specified in the command line arguments when starting the Unreal Editor <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Full Editor Launch:** The full editor launches, loads the project and default startup level, then runs the script once everything is loaded. This is useful for scripts interacting with project content or levels <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   **Headless Mode (Commandlet):** A faster approach for scripts that don't require the full UI, though loading levels and assets might be trickier <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.

### Startup Scripts
The editor automatically runs a script named `init_unreal.py` if found in configured Python paths, such as the `Content/Python` subfolder of your project or plugin <a class="yt-timestamp" data-t="00:43:07">[00:43:07]</a>. This is useful for project-specific initialization code <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.

Additionally, specific Python scripts can be listed in the project settings (`Project Preferences > Python > Startup Scripts`) to run every time that project is opened <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

### Python Scripting with Blueprints
The Python Editor Script Plugin exposes nodes to Blueprint visual scripting, allowing Python code snippets to be executed within editor-only Blueprint classes <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. These include `Editor Utility Widgets` and `Editor Utility Blueprints` <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>. The `Execute Python Script` node can be used to run a specified Python file <a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>.

## Managing Python Paths and Importing Libraries

The Unreal Editor automatically adds several paths to Python's `sys.path` variable, including the `Content/Python` subfolder within your project <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>. Additional paths can be explicitly added via the project settings (`Project Settings > Python > Additional Paths`) <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. This allows for [[importing_python_libraries | importing custom Python modules]] and libraries into the Unreal Engine environment <a class="yt-timestamp" data-t="01:14:40">[01:14:40]</a>.

## Unreal Editor Python API (`unreal` module)

The Python Editor Script Plugin provides a comprehensive API through the `unreal` module, which exposes nearly everything accessible from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>. As new [[unreal_engine_plugin_management | plugins]] are enabled, their Blueprint-exposed functionalities also become available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.

The API prioritizes Python-friendly naming conventions while maintaining consistency with Unreal's native APIs <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>:
*   Classes and objects have the same names as their Blueprint counterparts <a class="yt-timestamp" data-t="01:26:49">[01:26:49]</a>.
*   Blueprint properties are automatically exposed as `snake_case` <a class="yt-timestamp" data-t="01:26:55">[01:26:55]</a>.
*   Enums are typically `CAPITAL_SNAKE_CASE` <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.
*   Data types like Python lists, sets, and dicts are automatically converted to Unreal arrays, sets, or maps when passed to Unreal functions <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.

### Interacting with Editor Objects
The `unreal` module allows for programmatic interaction with objects in the project, such as creating actors and setting their configuration properties <a class="yt-timestamp" data-t="01:27:26">[01:27:26]</a>. For example, `unreal.EditorAssetLibrary` functions should be used for asset management (e.g., moving files) instead of standard Python file management modules <a class="yt-timestamp" data-t="01:36:55">[01:36:55]</a>. Properties should be set using `set_editor_property` functions <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>.

### Best Practices and Features
*   **Logging:** Use `unreal.log`, `unreal.log_warning`, and `unreal.log_error` for outputting messages to the log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Undo/Redo Support:** Use `with unreal.ScopedEditorTransaction(...)` to wrap operations, allowing them to be recorded in the editor's undo history <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Progress Dialogues:** For long-running operations, `with unreal.ScopedSlowTask(...)` can be used to display a progress bar to the user <a class="yt-timestamp" data-t="01:44:43">[01:44:43]</a>.

## Conclusion

The integration of Python in Unreal Engine 5 provides a powerful toolset for content creation workflows, particularly for [[integrating_python_in_asset_management and production pipelines | complex asset management]] and automation within the editor <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>. This capability is expected to become even more vital with the increasing adoption of generative AI <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>. Future possibilities include [[using_ai_integration_in_coding_environments | integrating AI models like PyTorch]] to directly manipulate editor content <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.