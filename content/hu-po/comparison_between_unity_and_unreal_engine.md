---
title: Comparison between Unity and Unreal Engine
videoId: D4nnVwEoN98
---

From: [[hu-po]] <br/> 

[[game_development_using_unreal_engine_5 | Unreal Engine]] and Unity are two prominent game engines, though their applications extend beyond traditional video game development <a class="yt-timestamp" data-t="01:02:07"></a>.

## Core Purpose and Application
While both are considered "game engines," they can also function as "simulation creation machines" <a class="yt-timestamp" data-t="01:11:00"></a>.
*   **[[game_development_using_unreal_engine_5 | Unreal Engine]]**: Historically used for video games and occasionally movies <a class="yt-timestamp" data-t="01:27:00"></a>. Increasingly, it's finding use as a simulation tool for fields like robotics, deep learning, and computer vision <a class="yt-timestamp" data-t="01:34:00"></a>.
*   **Unity**: Also a widely known game engine <a class="yt-timestamp" data-t="01:49:00"></a>.

## Performance and Features
[[game_development_using_unreal_engine_5 | Unreal Engine]] is generally considered more powerful than Unity <a class="yt-timestamp" data-t="02:07:00"></a>.
*   **[[game_development_using_unreal_engine_5 | Unreal Engine]]**:
    *   Less lightweight but more powerful <a class="yt-timestamp" data-t="02:07:00"></a>.
    *   Features built-in systems and is faster <a class="yt-timestamp" data-t="02:08:00"></a>.
    *   Includes powerful built-in tools and functionalities like Nanite (level of detail for 3D assets) and Lumen (lighting) <a class="yt-timestamp" data-t="08:03:00"></a> <a class="yt-timestamp" data-t="09:00:00"></a>.
    *   Features realistic avatars through MetaHuman <a class="yt-timestamp" data-t="09:13:00"></a>.
*   **Unity**:
    *   More lightweight <a class="yt-timestamp" data-t="02:01:00"></a>.
    *   Less powerful and has fewer built-in systems, meaning it's not as fast <a class="yt-timestamp" data-t="02:07:00"></a>.

## Scripting and Programming
A significant difference lies in their primary scripting languages:
*   **[[game_development_using_unreal_engine_5 | Unreal Engine]]**: Uses C++ for scripting <a class="yt-timestamp" data-t="10:00:00"></a>. C++ can be a "hurdle" as it takes longer to write and requires a stronger programming background <a class="yt-timestamp" data-t="10:13:00"></a>.
*   **Unity**: Uses C# for scripting <a class="yt-timestamp" data-t="10:03:00"></a>. C# is generally considered easier to write compared to C++ <a class="yt-timestamp" data-t="10:10:00"></a>.

## Scripting Alternatives
Both engines offer alternatives to direct code scripting:
*   **[[game_development_using_unreal_engine_5 | Unreal Engine]]**: Features [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint Visual Scripting]], which allows for creating entire games without writing a single line of code <a class="yt-timestamp" data-t="09:22:00"></a> <a class="yt-timestamp" data-t="50:01:00"></a>. This is a node-based interface, similar to those found in Blender <a class="yt-timestamp" data-t="09:41:00"></a>. [[python_support_and_plugins_in_unreal_engine | Python scripting in Unreal Engine 5]] is also supported, with a [[python_scripting_in_unreal_engine_5 | Python API]] that can be seen as an alternative interface to the Blueprint API <a class="yt-timestamp" data-t="21:45:00"></a> <a class="yt-timestamp" data-t="23:26:00"></a>.
*   **Unity**: Has a similar concept where a script is attached to an object <a class="yt-timestamp" data-t="40:49:00"></a>.

## Development Experience
The speaker notes a personal shift in development focus:
> "I've actually spent the majority of my development in game engines within unity and now I kind of want to try out [[game_development_using_unreal_engine_5 | Unreal Engine]] and see see what it's like to work with that" <a class="yt-timestamp" data-t="02:15:00"></a>.

A common approach when working with [[game_development_using_unreal_engine_5 | Unreal Engine]] is to initially create objects using [[using_blueprint_visual_scripting_in_unreal_engine | Blueprint]] and then convert them to C++ as performance demands require <a class="yt-timestamp" data-t="01:08:54"></a>. This allows for quicker development initially and easier collaboration with non-programmers <a class="yt-timestamp" data-t="01:08:42"></a>.