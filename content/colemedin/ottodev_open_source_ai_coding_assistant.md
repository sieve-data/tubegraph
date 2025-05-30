---
title: oTToDev open source AI coding assistant
videoId: 5I9VgwauuzU
---

From: [[colemedin]] <br/> 

oTToDev is an [[Opensource AI coding assistant development | open-source AI coding assistant]] currently under active development, aiming to be the best in its category <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The project recently launched its [[Opensource AI coding assistants and community building | community]] within the Automator Think Tank, which has led to a significant increase in engagement and contributions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Recent Updates and New Features

Many exciting [[updates_and_future_goals_for_ottodev_ai_coding_assistant | updates]] have been implemented in oTToDev, with several new features designed to enhance [[Using AI coding assistance | AI coding assistance]] and user experience <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Key Contributions and Pull Requests (PRs)

The development team and community have made significant strides, including:

*   **Provider Choice Respect** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>: Tommy implemented a feature ensuring that the provider choice made in the UI is consistently used in the backend <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Expanded Model Support** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>: Muu Tin added support for Groq and the latest Sonnet and Haiku models <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Ollama Configuration** <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>: Patrick added configuration to oTToDev to address the default 2,000 token context length issue with Ollama's base models, making all Ollama models work out-of-the-box <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Code Streaming** <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>: The Codus implemented code streaming, allowing users to see the large language model (LLM) type out code in real-time as it's generated, rather than just dumping it all at once <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Built-in Terminal** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>: A "bolt terminal" is now attached to the workbench, displaying the output of commands run by the LLM <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Previously, users could only see the commands chosen, not their output, making debugging failed commands difficult <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Containerization Cleanup** <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>: Aaron contributed to cleaning up the repository for containerization efforts <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Bug Fixes** <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>: Janen and Ally provided important bug fixes <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Standardized Model Provider Code** <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>: Edward added functionality to automatically fetch available models from providers like Open Router, eliminating the need for hardcoding models <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. He also added buttons to link directly to API key acquisition pages or download pages (for Ollama) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Coordination and Merging** <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>: Chris has been instrumental behind the scenes, coordinating merges and organizing PRs and bugs <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### UI Demonstrations

The updated UI showcases these [[Improvements to AI Coding Assistants | improvements]]:
*   **Automatic Model Fetching** <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>: When selecting a provider like Open Router, a comprehensive, alphabetically sorted list of available models, including their pricing, is automatically fetched <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **API Key Access** <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>: A convenient button directs users to their provider's account page to obtain their API key <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Real-time Code Generation** <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>: When generating code, the LLM's typing process is visible in real-time on the right-hand side, as opposed to the previous method of instantly dumping the completed file <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Command Output Visibility** <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>: The new bolt terminal in the bottom right corner displays the output of commands run by the LLM, providing crucial debugging information that was previously unavailable <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Roadmap and Vision

The oTToDev team is using Road map.sh to collaboratively plan the project's future <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This [[updates_and_future_goals_for_ottodev_ai_coding_assistant | roadmap]], though a rough draft, emphasizes a clear vision to prevent feature bloat and ensure sustainable [[AI coding assistant development | AI coding assistant development]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Short-Term Goals
*   **Crowdfunding for Bounties** <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>: A key next step is establishing crowdfunding to offer bounties for feature implementation, accelerating development <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **High-Priority Features** <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>:
    *   Preventing Bolt from constantly rewriting files <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   Improving prompting for smaller LLMs, as current prompts are optimized for models like Sonnet <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Enabling the loading of local projects <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Allowing attachment of images to prompts for models that support it <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   Running agents in the backend, potentially using a Chain of Thought system with a mixture of agents to generate better code <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This represents a step towards [[Open Source AI agent development | Open Source AI agent development]].
    *   Implementing one-click deployment to Netlify <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   Developing different prompts tailored for various LLMs, especially local ones, to improve performance beyond Sonnet's current optimization <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Long-Term Vision
*   **Extension Marketplace** <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>: A significant future goal is an extension marketplace where developers can create plugins for oTToDev without directly updating the core repository <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This will allow users to toggle specific features on and off, preventing [[Open Source AI Code Generators | Open Source AI Code Generators]] from becoming cluttered with excessive features <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## Crowdfunding Update

The community has expressed strong interest in donating to support the project <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Options like Kickstarter are being considered as prime crowdfunding platforms <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. Additionally, partnerships are being explored, with more updates expected soon <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Crowdfunding will contribute to the overall [[Benefits of opensourcing AI coding assistants | Benefits of opensourcing AI coding assistants]].

## Troubleshooting oTToDev

Debugging common issues with oTToDev can help users either fix problems themselves or provide more useful error messages for community support <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

> [!WARNING] Unhelpful UI Error Message
> The UI often displays a generic "there was an error processing your request" <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, which is not specific enough for debugging <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. More helpful messages can be found elsewhere.

### Identifying Error Sources

*   **Backend Errors (Terminal Output)** <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>: For internal server errors (500 errors), helpful output will appear in the terminal where oTToDev was started <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This output is crucial for diagnosis <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Frontend Errors (Developer Tools Console)** <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>: For frontend issues (e.g., 400 errors), error messages can be found in the browser's developer console (right-click, then "Inspect" > "Console" tab) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

> [!NOTE] Observing LLM Commands
> While oTToDev is running, the terminal output will show the commands the LLM is choosing to run <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Any issues from the bolt terminal (the built-in terminal for LLM commands) will also appear here, indicating backend errors (500) or frontend errors (400) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Common Troubleshooting Scenarios

*   **Blank Preview (404 Error)** <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>: A blank preview often indicates that the LLM has "hallucinated" something with the code, file structure, or commands, rather than an issue with oTToDev itself <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Using a larger, more capable model can resolve this <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **"X API Key Header Missing"** <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>: This error is frequently resolved by simply restarting the container or site <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   **Poor Results/LLM Mess-ups** <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>: If everything seems to be working but the generated results are poor, it typically means a smaller, less powerful LLM is being used <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. While local and smaller models have their use cases (e.g., quick tests, limited hardware), larger models like Claude or GPT often yield significantly better results for complex tasks <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

A pinned comment in the "issues and troubleshooting" category of the oTToDev [[Opensource AI coding assistants and community building | community]] provides a comprehensive guide to these debugging tips <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.