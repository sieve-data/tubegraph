---
title: Coding and debugging in AI workshops
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

This article details the hands-on, dynamic approach to coding and debugging adopted in a specific AI workshop, emphasizing real-time implementation and problem-solving.

## Workshop Structure and Philosophy
The workshop aimed to be highly dynamic and interactive, encouraging participants to interrupt with questions at any point via Slack or by unmuting themselves <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The core of the session involved significant live coding from scratch, with a recognition that debugging would likely be a part of the process <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

A key philosophy highlighted was to approach concepts from "first principles" and reduce perceived complexity, suggesting that many advanced AI concepts are fundamentally about [[function_calling_in_AI | function calling]] <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>.

### Live Coding Environment
The presenter frequently used the Cursor IDE, noting its utility for auto-completion and code generation <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>, <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. The `swarm` framework was also utilized for its convenient looping tools and agent implementations, although the presenter noted that core agent logic can be implemented in a small amount of code (around 70 lines) <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>, <a class="yt-timestamp" data-t="01:06:40">[01:06:40]</a>.

## Core Coding Demonstrations

### Crash Course on [[function_calling_in_AI | Function Calling]]
The workshop provided a rapid overview of [[function_calling_in_AI | function calling]], noting its two main purposes: fetching data (e.g., reading APIs, retrieval) and taking action (e.g., writing APIs, managing application state, workflow actions) <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>, <a class="yt-timestamp" data-t="01:20:19">[01:20:19]</a>. A key distinction was made that the model *tells* you its intent to use a function but does not *execute* it; the developer is responsible for parsing, executing, and providing the result back to the model <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>, <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.

Best practices for writing functions for AI models include:
*   Writing clear function descriptions and parameter purposes <a class="yt-timestamp" data-t="01:17:50">[01:17:50]</a>.
*   Applying software engineering best practices, ensuring functions are intuitive and follow the principle of least privilege <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a>.
*   Using enums and object structures to prevent models from making invalid calls <a class="yt-timestamp" data-t="01:20:02">[01:20:02]</a>.

### Implementing Memory
A very basic form of memory was implemented using a simple Python list to store factual information about the user. This memory was persisted by writing it to and reading it from a local JSON file <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>, <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. The demonstration showed that an agent could retrieve this stored memory in subsequent interactions <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

For enforcing consistency in stored memories, one suggestion was to perform retrieval of semantically similar memories before storing new ones, then use a model to explicitly check for updates or contradictions. Storing timestamps and creating explicit "chains of updates" (like a linked list of changes) was also proposed to manage evolving information <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>.

### Agent Delegation and Asynchronous Operations
The workshop explored different forms of [[strategies_for_ai_evaluation_and_troubleshooting | agent]] delegation:
*   **Handoffs:** Fully swapping a conversation to a different [[strategies_for_ai_evaluation_and_troubleshooting | agent]] by replacing its system prompt and [[using_tools_and_function_calls_with_ai_sdk | tools]] <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>. This is seen as a primary use case for [[strategies_for_ai_evaluation_and_troubleshooting | agents]] and handoffs, functioning as a "glorified triage" among multiple functions <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.
*   **Nested calls:** The simplest form of delegation, often overlooked <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>.
*   **Manager tasks:** More complex, involving asynchronous operations <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.

A simple delegation to a "smarter model" was demonstrated by having one model call another directly via API <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. The challenge of waiting for synchronous responses led to the implementation of asynchronous calls. Using `asyncio.sleep` to emulate non-blocking network calls, it was shown that multiple function calls could run in parallel, significantly reducing perceived latency <a class="yt-timestamp" data-t="00:52:02">[00:52:02]</a>, <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>.

To address the issue of waiting for parallel tasks to complete before interacting with the model again, a "task" system was introduced. This allowed the main interaction loop to continue while tasks ran in the background. A `create_task` function would initiate a background process and return a task ID, and a `check_tasks` function would be called later to retrieve the results <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>, <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>. This enabled the user to continue chatting with the model while background tasks were processed <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>.

### Self-Tool Writing [[strategies_for_ai_evaluation_and_troubleshooting | Agents]]
Perhaps the most "fun" and "cool" part of the live coding was demonstrating an [[strategies_for_ai_evaluation_and_troubleshooting | agent]]'s ability to write its own [[using_tools_and_function_calls_with_ai_sdk | tools]]/functions dynamically <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>, <a class="yt-timestamp" data-t="01:25:55">[01:25:55]</a>. This was achieved by having the model generate Python code for a function, using `exec` to interpret and load it into the current environment, and then adding it to the [[strategies_for_ai_evaluation_and_troubleshooting | agent]]'s available [[using_tools_and_function_calls_with_ai_sdk | tools]] <a class="yt-timestamp" data-t="01:21:31">[01:21:31]</a>, <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>. While noted as "super dangerous code," it successfully demonstrated an [[strategies_for_ai_evaluation_and_troubleshooting | agent]] creating and utilizing its own custom calculator function <a class="yt-timestamp" data-t="01:26:03">[01:26:03]</a>.

## Debugging in Practice
The workshop explicitly included debugging, which was an expected part of the live coding process <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Instances of debugging included:
*   Resolving audio issues with the Zoom setup <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Troubleshooting code where functions were not correctly provided to the model or were hallucinated <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>, <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
*   Identifying and fixing issues with printing function call results in the console <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>.
*   Correcting the use of `eval` to `exec` for dynamic code execution <a class="yt-timestamp" data-t="01:21:34">[01:21:34]</a>.
*   Attempting to debug real-time API demos which proved challenging in a live setting <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>, <a class="yt-timestamp" data-t="01:39:08">[01:39:08]</a>.

## Advanced Considerations for Functions
### Scaling Functions
When dealing with dozens or hundreds of functions, several techniques were suggested:
*   **Multiple [[strategies_for_ai_evaluation_and_troubleshooting | agents]]**: Splitting responsibilities and function groupings among different [[strategies_for_ai_evaluation_and_troubleshooting | agents]], invoking the correct one as needed <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
*   **[[evaluations_and_finetuning_in_ai_development | Fine-tuning]]**: It's possible to [[evaluations_and_finetuning_in_ai_development | fine-tune]] smaller models with many functions (e.g., 120 functions with GPT-3.5 in a latency-sensitive project) <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>.
*   **Dynamic Function Loading**: Based on user input or conversation context, only the most relevant functions are loaded into memory <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>. This can be done with embeddings or a two-step [[function_calling_in_AI | function call]], where one function loads more functions (similar to a handoff) <a class="yt-timestamp" data-t="01:09:06">[01:09:06]</a>.
*   **Router Patterns**: Using multiple [[strategies_for_ai_evaluation_and_troubleshooting | agents]] and handing off to one based on the query is an effective routing strategy <a class="yt-timestamp" data-t="01:10:26">[01:10:26]</a>.

A general rule of thumb suggested for models without extensive prompting or [[evaluations_and_finetuning_in_ai_development | fine-tuning]] is to keep the number of [[using_tools_and_function_calls_with_ai_sdk | tools]]/functions around 10 to 20 <a class="yt-timestamp" data-t="01:16:20">[01:16:20]</a>.

### [[Function calling in AI | Function Calling]] in Vision Models
Regarding vision models, it was noted that while it is technically possible with post-training, the current API for GPT-4 does not expose or allow functions to be called within the model's "thought" process or internal chain of thought. [[function_calling_in_AI | Function calls]] currently happen at the very end of the model's generation <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>.