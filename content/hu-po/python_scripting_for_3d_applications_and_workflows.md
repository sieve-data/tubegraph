---
title: Python scripting for 3D applications and workflows
videoId: pes7-J6rWy8
---

From: [[hu-po]] <br/> 

[[using_python_in_unreal_engine_5 | Python scripting in Unreal Engine 5]] is a powerful tool for [[integrating_python_in_asset_management_and_production_pipelines | production pipelines and asset management systems]], especially with the rise of deep learning and generative AI models like Stable Diffusion <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Python is widely adopted due to its ease of use and ability to create and maintain large-scale systems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Key Uses of Python in Unreal Engine

Python is primarily used within the Unreal Editor to [[automating_work_in_unreal_editor_with_Python | automate workflows]] and tie the editor to other [[3d_representations_and_their_applications | 3D applications]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Key applications include:
*   Constructing large-scale asset management pipelines <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Automating time-consuming asset management tasks, such as generating levels of detail (LODs) or static meshes, although Unreal Engine 5's Nanite system now handles this automatically <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Procedurally laying out content <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Controlling the Unreal Editor from custom user interfaces (UIs) created with Python modules like PySide and Qt <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Integrating deep learning models into asset production pipelines, which are often Python-based <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

It is important to note that Python scripts run within the Unreal Editor and are not part of the final packaged game executable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Python Integration in Unreal Engine 5.1

Unreal Engine 5.1 includes built-in Python support through the Python Editor Script Plugin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This plugin contains an embedded version of Python 3.9.7, meaning a separate Python installation is not required on the user's computer <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Running Python Scripts

There are several ways to [[creating_custom_unreal_editor_scripts_with_Python | run Python scripts]] within the Unreal Editor:

*   **Python Console and Output Log:**
    *   The Unreal Editor's console input bar can be switched to accept Python code by pressing the tilde (~) key <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    *   Users can enter and execute single lines of Python code or paste multi-line blocks <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   Python script files can be executed by typing their name into the console, optionally including command-line arguments <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
    *   The `py` command can be used in the normal console to execute a line of Python code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **File Menu:**
    *   The Unreal Editor's file menu offers "Execute Python Script" to browse for and run new scripts <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.
    *   "Recent Python Scripts" allows re-running previously executed scripts <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.
*   **Command Line:**
    *   Python scripts can be specified as command-line arguments when launching the Unreal Editor, either with a full editor launch or in headless mode <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
    *   This is useful for automation scenarios where the editor needs to shut down immediately after script execution <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>.
*   **Startup Scripts:**
    *   The Unreal Editor automatically runs a script named `init_unreal.py` if found in configured Python paths <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>. This is ideal for project-specific initialization code <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
    *   Additional Python scripts can be specified in project settings to run every time a project opens <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>. These scripts execute after the project's default startup level has fully loaded <a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>.
*   **Editor-Only Blueprints:**
    *   The Python Script Plugin exposes nodes to Blueprint visual scripting, allowing Python code snippets to be run from editor-only Blueprint classes like Editor Utility Widgets and Editor Utility Blueprints <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. This enables designers to trigger Python scripts directly from custom UI tools within the editor <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

### Python Environment and Paths

The Unreal Editor automatically adds several paths to the `sys.path` variable of its Python environment, including the `Content/Python` subfolder within the project folder <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>. Users can also add [[importing_python_libraries | additional Python paths]] in the project settings (`Edit > Project Settings > Python > Additional Paths`) to import custom modules or external libraries <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. By default, Unreal's embedded Python interpreter runs in isolated mode <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>.

## Unreal Python API (`unreal` module)

The Python Editor Script Plugin provides the `unreal` module, which exposes a wide range of classes and functions for interacting with the Unreal Editor, project assets, and level content <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>. This API mirrors much of what is exposed from C++ to Blueprints in the editor environment <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>. New plugins that expose Blueprint functionality also make that functionality available in Python <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.

Key features of the `unreal` module:
*   **Automatic Type Conversion:** Python lists, sets, and dictionaries are automatically converted to Unreal arrays, sets, or maps when passed into Unreal API functions <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.
*   **Inheritance Hierarchy:** Python classes maintain the same inheritance hierarchy as their C++ counterparts <a class="yt-timestamp" data-t="01:20:41">[01:20:41]</a>.
*   **Naming Conventions:** The API balances C++ and Python naming conventions; classes and objects have the same names as in Blueprints, while properties are automatically exposed in `snake_case` <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>.

### Best Practices

*   **Asset Management:** Always use functions from the `unreal` module for asset management operations (e.g., moving files) instead of Python's built-in file management modules <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>.
*   **Property Modification:** Use `set_editor_property()` to change object configuration properties programmatically <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.
*   **Logging:** Use `unreal.log()`, `unreal.log_warning()`, and `unreal.log_error()` for logging messages to the Output Log <a class="yt-timestamp" data-t="01:38:58">[01:38:58]</a>.
*   **Undo/Redo:** Use `with unreal.ScopedEditorTransaction("Transaction Name"):` to wrap operations that should be part of the undo/redo history <a class="yt-timestamp" data-t="01:39:52">[01:39:52]</a>.
*   **Progress Dialogues:** For long-running operations, display progress to the user using `with unreal.ScopedSlowTask("Task Description", is_100_frames=True) as slow_task:`, then `slow_task.enter_progress_frame(frame_number)` <a class="yt-timestamp" data-t="01:44:25">[01:44:25]</a>.

For example, to [[creating_custom_unreal_editor_scripts_with_Python | create a new actor]] and set its location:
```python
import unreal

with unreal.ScopedEditorTransaction("Create and Move Actor"):
    # Spawn a FloatingText actor
    floating_text_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.FloatingText, unreal.Vector(0, 0, 0))
    
    # Set its text (example property, actual FloatingText might vary)
    # floating_text_actor.set_editor_property("text_content", "Hello World!") 
    
    # Set its location
    floating_text_actor.set_actor_location(unreal.Vector(0, 0, 100), False, False)
```
This script would create a "FloatingText" actor at coordinates (0, 0, 100) within the Unreal Editor <a class="yt-timestamp" data-t="01:40:47">[01:40:47]</a>.

## Future Potential

The strong integration of Python in Unreal Engine opens up significant possibilities for future workflows, especially as [[potential_applications_and_future_directions_in_3d_scene_representations | generative AI continues to evolve]] <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>. This could include using neural networks to edit content within the editor or integrating advanced models for [[applications_of_text_to_3d_model_generation_in_various_industries | text-to-3D model generation]] directly into production pipelines <a class="yt-timestamp" data-t="01:47:31">[01:47:31]</a>. Unreal Engine's increasing use in film, television, and commercials, where the final product is images rather than executables, makes Python scripting for rendering pipelines particularly valuable <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>. External Python libraries can be used to apply styles or modify images as part of the rendering process, potentially connecting to cloud-served models via REST requests <a class="yt-timestamp" data-t="01:41:17">[01:41:17]</a>.