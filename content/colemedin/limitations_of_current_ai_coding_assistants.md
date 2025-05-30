---
title: Limitations of current AI coding assistants
videoId: ZoyPqXvnnZ8
---

From: [[colemedin]] <br/> 

Despite being able to build almost anything, the [[issues_with_current_ai_coding_assistants | biggest limitation]] of [[using_ai_coding_assistance | AI coding assistants]] is their inability to consistently work well with specific tools or frameworks like MCP, Superbase, or Pyantic AI <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. To address this, there's a need to integrate RAG (Retrieval Augmented Generation) capabilities for tool and framework documentation into these assistants <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Context 7, an MCP server, was introduced to provide an instant RAG knowledge base for thousands of frameworks and tools <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. However, Context 7 itself has notable issues <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Issues with Context 7 and AI Coding Assistants

### Overwhelming Public Knowledge Base
Context 7 provides documentation for over 8,000 libraries, but users typically only care about a small fraction of these <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This extensive, collective knowledge base can lead to [[external_knowledge_issues_in_ai_coding_tools | AI coding assistants]] leveraging the wrong documentation or hallucinating due to the irrelevant majority of information <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Developers often prefer a more private and limited knowledge base tailored to their specific tech stack <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Lack of Private Knowledge Base Support
Users cannot integrate private GitHub repositories or other private data into Context 7's knowledge base, as it forces reliance on its open, collective knowledge <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Lack of True Open-Source Nature
While Context 7's MCP server itself is open-source (a GitHub repository is available), its core logic and the entire product are not <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The MCP server's code is minimal (only 68 lines) because it primarily hits a private endpoint that handles the main functionality, such as searching for libraries, scraping, and RAG <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This suggests that the service may eventually be monetized, forcing users to pay for what appears to be a free and open-source solution <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Limitations in Other Platforms
Platforms like Cursor and Windsurf offer native documentation search and, in Cursor's case, custom document addition <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. However, their performance for documentation retrieval is not as effective as specialized tools like Context 7 <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This highlights a general challenge in providing robust and efficient knowledge access within [[effective_use_of_ai_coding_assistants | AI coding environments]].