---
title: New features in oTToDev
videoId: 5I9VgwauuzU
---

From: [[colemedin]] <br/> 

[[oTToDev open source AI coding assistant | oTToDev]], a fork of Boltnew, is undergoing significant development to become a leading open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The project recently launched its community in the Automator Think Tank, which has led to increased engagement and contributions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Recent Feature Highlights

Several new features and improvements have been integrated into [[oTToDev open source AI coding assistant | oTToDev]], enhancing its functionality and user experience:

### Model and Provider Enhancements
*   **Respecting Provider Choice**
    *   A Pull Request (PR) by Tommy ensures that the provider selected in the UI is consistently used in the backend <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Expanded Model Support**
    *   Muu Tin added support for Groq and the latest Sonnet and Haiku models <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Ollama Context Length Configuration**
    *   Patrick implemented a configuration within [[oTToDev open source AI coding assistant | oTToDev]] to manage Ollama's default 2,000-token context length, eliminating the need for users to create separate model files for variations <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Now, any Ollama model should work directly <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Standardized Model Provider Code**
    *   Edward introduced standardized model provider code, allowing [[oTToDev open source AI coding assistant | oTToDev]] to automatically fetch all available models from providers like OpenRouter, rather than relying on hardcoded lists <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This feature also includes a button in the UI that links users directly to obtain API keys for providers or download pages for local models like Ollama <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. For OpenRouter, it now displays a comprehensive, alphabetically sorted list of models with pricing information <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### UI and Workflow Improvements
*   **Code Streaming**
    *   A significant addition by "the codus" enables users to see the Large Language Model (LLM) type out code in each file as it's being generated, rather than simply presenting the completed file at once <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Bolt Terminal Integration**
    *   Also from "the codus," a Bolt Terminal is now attached to the workbench. This allows users to view the real-time output of commands executed by the LLM. Previously, only the commands chosen by the LLM were visible, making it difficult to debug if a command failed <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This provides crucial visibility into the LLM's actions and potential issues <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **General Bug Fixes and Cleanup**
    *   Janen and Ally contributed various bug fixes <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Aaron also performed cleanup work related to containerization <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Chris played a key role in coordinating merges, adding tags, and supporting the overall development process behind the scenes <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## [[Roadmap and development progress of Autod Dev | Future Roadmap and Development Goals]]

An initial [[Roadmap and development progress of Autod Dev | roadmap]] for [[oTToDev open source AI coding assistant | oTToDev]] has been shared, outlining upcoming features and the project's strategic direction <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This [[Roadmap and development progress of Autod Dev | roadmap]] is a living document, planned to be updated as the community collaboratively shapes the project's future <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

Key upcoming priorities include:
*   **Crowdfunding and Bounties**: Establishing crowdfunding to allow for bounties on features, encouraging faster development by paying developers <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **High Priority Features**:
    *   Preventing Bolt from constantly rewriting many files <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   Improved prompting for smaller LLMs to enhance performance, as current prompting is optimized for Sonnet <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   [[Introduction of local project load feature in Autod Dev | Loading local projects]] <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   Attaching images to prompts for models that support it <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Running agents in the backend for more advanced code generation, such as a Chain of Thought system with a mixture of agents <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **One-Click Deployment**: Implementing a one-click deployment option to Netlify, similar to the commercial Boltnew <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Extension Marketplace**: A major long-term goal is to introduce an extension marketplace, allowing developers to create plugins for [[oTToDev open source AI coding assistant | oTToDev]] without needing to update the main repository. Users will be able to toggle these extensions on and off in the UI, preventing feature bloat while enabling continuous expansion of functionality <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Crowdfunding Efforts
The team is actively exploring crowdfunding options, with Kickstarter being a primary consideration <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>. There are also potential [[Upcoming strategic partnership for Autod Dev | strategic partnerships]] being discussed, with more updates expected soon <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## [[Troubleshooting and debugging oTToDev | Troubleshooting oTToDev]]

For users encountering issues, it's crucial to understand how to [[troubleshooting_and_debugging_ottodev | troubleshoot]] [[oTToDev open source AI coding assistant | oTToDev]]. A common unhelpful error message in the UI is "there was an error processing your request" <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. More useful error messages can be found:
*   **Terminal Output**: For backend issues (e.g., 500 internal server errors), detailed error messages will appear in the terminal where [[oTToDev open source AI coding assistant | oTToDev]] was started <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Developer Console**: For frontend issues (e.g., 400 errors), error messages are visible in the browser's developer tools console <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Bolt Terminal Output**: The integrated Bolt Terminal also displays output from LLM-executed commands, which can reveal if the LLM hallucinated a bad command or file structure, leading to issues like a blank preview <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **LLM Hallucinations**: Often, a blank preview or bad results are not a bug in [[oTToDev open source AI coding assistant | oTToDev]] but rather an issue with the LLM hallucinating incorrect code or commands, especially with smaller models <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Using larger, more capable models is recommended for better results <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Restarting**: Simple issues like a missing API key header (x-api-key header missing) can often be resolved by restarting the [[oTToDev open source AI coding assistant | oTToDev]] container or site <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

A pinned comment in the [[oTToDev open source AI coding assistant | oTToDev]] community's issues and [[troubleshooting_and_debugging_ottodev | troubleshooting]] category provides further guidance <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.