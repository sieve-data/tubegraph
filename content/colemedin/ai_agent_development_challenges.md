---
title: AI agent development challenges
videoId: DpPVEw4dd0w
---

From: [[colemedin]] <br/> 

When [[Building AI Agents | building AI agents]], a significant challenge is that much of the process involves "guesswork" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Many individuals are not focused on [[Building AI Agents | building AI agents]] that are genuinely useful in real-world scenarios <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. To create production-ready [[AI agents and their development | AI agents]], it's crucial to address several key challenges, especially regarding observability.

## The Problem of Observability
[[AI agents and their development | AI agent development]] without proper observability is like "flying completely blind" when the agent is running in a live environment <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This lack of visibility presents several critical issues:

*   **Debugging Failures** When an agent fails, developers often have "no idea why" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Cost Management** It becomes impossible to accurately track "how much you're spending" on agent operations <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Iteration and Improvement** Without clear insights, it's difficult to "iterate on your agent to improve specific responses or address any bottlenecks" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This makes it challenging to refine the agent's behavior or fix underlying issues like a tool that "misbehaves" or an agent that "always gives bad parameters to a tool" <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. An agent might even make a "mistake" without an explicit error <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

The speaker emphasizes that it is "way too dangerous to not invest time" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> in learning platforms that provide this observability.

## Complexity of Self-Hosting
While open-source solutions like Langfuse offer flexibility, self-hosting them can be complex. Setting up Langfuse independently "is not super trivial" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> because it relies on multiple services for data storage, including Redis, PostgreSQL, ClickHouse, and blob storage <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Integration Limitations
Even with robust tools, specific integrations might be lacking. For example, there is currently "not a native integration for Langfuse in N8N" <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, despite demand from both communities <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. While custom setups exist, they often come with downsides, such as having to "hardcode your Langfuse authentication keys in the code node in N8N" <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>, which is "not an ideal solution" <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>.

## Conclusion
To overcome these [[AI agent development | AI agent development]] challenges, especially when deploying [[AI agents and their development | AI agents]] into production, it is crucial to utilize platforms like Langfuse. Such tools provide essential visibility into agent executions, allowing for monitoring of costs, response times, user conversations, tool calls, and error tracking <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This robust logging and tracing capability is vital for troubleshooting and continuous improvement of [[AI agents and their development | AI agents]] <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.