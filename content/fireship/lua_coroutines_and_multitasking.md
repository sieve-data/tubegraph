---
title: Lua coroutines and multitasking
videoId: jUuqBZwwkQw
---

From: [[fireship]] <br/> 

Lua supports [[benefits_and_applications_of_lua | collaborative multitasking]] through the use of co-routines <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Although the language is single-threaded <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, co-routines enable the pausing and resuming of a function's execution <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## How Coroutines Work

To utilize coroutines:
*   **Creation and Suspension**: A co-routine is created, and its execution can be suspended using the `yield` keyword <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Resumption**: Execution of a suspended co-routine can be continued from elsewhere in the code by using `co-routine resume` <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This continues until the co-routine reaches a `return` statement <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

This mechanism allows for managing concurrent tasks in a single-threaded environment <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.