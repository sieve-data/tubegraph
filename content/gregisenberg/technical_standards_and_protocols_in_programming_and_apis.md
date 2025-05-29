---
title: Technical standards and protocols in programming and APIs
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Technical standards and protocols are fundamental in programming and API development, allowing engineers to build systems that communicate effectively with one another <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. These formalities are crucial for making development easier and ensuring scalability <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Importance of Standards

Standards enable engineers to connect systems from different providers <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. For example, REST APIs are a popular standard followed by companies when constructing their APIs and services, allowing engineers to connect with them seamlessly <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Without standards, connecting different services feels like gluing disparate parts together, which can be frustrating and difficult at scale <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Limitations of Large Language Models (LLMs) Without Tools

By themselves, LLMs are largely incapable of performing meaningful actions beyond predicting the next word or answering questions <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, an LLM cannot send an email or perform specific tasks on a user's behalf without external capabilities <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. They are fundamentally "dumb" in their standalone state <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Evolution: LLMs + Tools

The next evolution in LLM capability involved developers combining LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This allows LLMs to perform actions like searching the internet (as seen with Perplexity) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a> or automating tasks through services like Zapier or Endate <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. While this makes LLMs more capable, it presents significant challenges <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Challenges with LLMs + Tools

*   **Complexity**: Building an assistant that performs multiple functions (e.g., searching, reading emails, summarizing) requires gluing many different tools to LLMs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Cumbersome Integration**: Stacking these tools and making them cohesive is a "nightmare" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Each service provider constructs their APIs differently, requiring varied information and setup, akin to speaking different languages <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Maintenance**: Updates to external APIs (e.g., Slack's API) can break complex automation sequences, leading to significant engineering effort to fix <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Hallucination**: Engineers must ensure the LLM doesn't hallucinate or act "stupidly" when using these tools <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## The Role of mCP (Machine Coded Protocols)

mCP is proposed as the next evolution, acting as a layer between an LLM and various services/tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Its primary function is to translate the disparate "languages" of different tools into a unified language that the LLM can easily understand and use <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This simplifies the LLM's connection and access to outside resources <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Key Aspects of mCP

*   **Standardization**: mCP is essentially a standard created by Anthropic, which aims to make LLMs more capable <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. It unifies the LLM and the service, creating an efficient communication layer <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Ecosystem**: The mCP ecosystem consists of:
    *   **mCP Client**: The LLM-facing side (e.g., Tempo, Windsurf, Cursor) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   **mCP Protocol**: The two-way connection between the client and server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
    *   **mCP Server**: Translates the external service's capabilities for the client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Service providers are responsible for constructing these servers <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
    *   **Service**: The external tool or API (e.g., a database, Slack, a text service) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Benefits**:
    *   **Seamless Integration**: Allows for much smoother and easier integration with external services <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
    *   **Reduced Manual Work**: Less step-by-step planning and fewer edge cases compared to direct tool integration <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   **Scalability**: Makes it easier to combine and stack capabilities like "Lego pieces" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

### Current Challenges with mCP

Despite its promise, mCP is in its early stages <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>. Setting up an mCP server can still be "annoying" due to manual downloading, file movement, and local setup <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. These "kinks" need to be figured out for the standard to be polished and widely adopted <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## Future Outlook

When standards like mCP are finalized, they open up significant opportunities for development, enabling LLMs to become even more powerful and capable <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. Businesses and developers should monitor the evolution of mCP and similar standards <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.

### Startup Opportunities

*   **mCP App Store**: An online platform where users can browse, deploy, and install mCP servers from various repositories, obtaining a URL to integrate directly with an mCP client <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **[[leveraging_ai_and_new_technologies_in_app_development | AI Tools for App Development]]**: For non-technical individuals, staying updated with platforms that are building out mCP capability is key to understanding future integration possibilities and identifying opportunities when the standard is finalized <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. While the current stage is early for immediate action, observing and learning will allow for timely strikes when the market matures <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.