---
title: Community Contributions to Software Development
videoId: p1YvKuRfEhg
---

From: [[colemedin]] <br/> 

The `bolt.new` platform is a popular AI code generator <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. A custom version, or "fork," was created to introduce several significant improvements, primarily allowing users to choose the Large Language Model (LLM) for code generation, including local LLMs via tools like Ollama for free code generation <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This contrasts with the main `bolt.new` version, which restricts users to a single model <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

The video detailing this [[forking_open_source_platforms_for_custom_modifications | `bolt.new` Fork]] gained significant traction, becoming the third most-watched video on the channel and generating "insane" and "unmatched" [[community_engagement_and_contributions | engagement]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This high level of [[community_engagement_in_open_source_projects | community engagement]] manifested in numerous suggestions, feedback, and direct contributions to the fork <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This feedback has been taken to heart, leading to the development of a [[community_engagement_in_open_source_projects | community]] around the project <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The project is seen as an opportunity for the [[community_engagement_in_open_source_projects | community]] to collaboratively improve it and potentially evolve beyond just a fork <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Current Functionality of the Bolt.new Fork

The `bolt.new` fork offers several enhancements not found in the official version <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>:

*   **LLM Selection**: Users can choose their LLM provider, such as OpenAI, and specific models <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Code Generation**: Users can input prompts or select predefined templates for AI code generation <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Interactive Development**: The fork opens a chat widget and a code widget, automatically creating project files and running `npm` commands to provide an app preview <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. For example, a to-do app can be generated and tested within an in-browser Node.js environment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Community-Driven Improvements

The `bolt.new` fork's GitHub repository shows continuous [[improvements_in_project_organization_and_contribution_management | development]] through [[community_engagement_and_contributions | community contributions]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. A dedicated section in the README lists requested additions from YouTube comments <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Implemented [[improvements_in_project_organization_and_contribution_management | features]] include:

*   **OpenRouter Integration**: This was a highly requested [[improvements_in_project_organization_and_contribution_management | feature]] that allows using OpenRouter's range of models <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Gemini Integration**: Support for Gemini 1.5 Flash and Pro models was added via [[community_engagement_and_contributions | pull requests]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Dynamic Ollama Model List**: Initially, a hardcoded list of Ollama models caused issues for users who didn't have all models downloaded <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. A contributor enabled dynamic model selection, displaying only models available locally through Ollama's API <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Provider Filtering**: A filter was added to sort models by provider, making the selection process cleaner <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Code Download as Zip**: A highly requested [[improvements_in_project_organization_and_contribution_management | feature]] allowing users to download the generated code as a zip file, eliminating the need to manually copy and paste files <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This was implemented using `jszip` and `FileSaver.js` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Demonstrating New Features

The improved UI now includes a dropdown for providers, allowing users to select options like OpenRouter or Google's Gemini models (Flash and Pro) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. After code generation, a "Download Code" button creates a zip file with the project's entire structure <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The Ollama integration dynamically shows only models downloaded on the user's machine <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

## Future Work and [[community_engagement_and_contributions | Collaboration]]

The project actively seeks further [[community_engagement_and_contributions | contributions]] for future [[improvements_in_project_organization_and_contribution_management | development]] <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. The list of desired [[improvements_in_project_organization_and_contribution_management | features]] includes:

*   **LM Studio Integration**: To support local models for users who prefer LM Studio over Ollama <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Deepseek API Integration**: To leverage powerful Deepseek Coder models, particularly the 36-billion parameter one <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Improved Prompting for Smaller Models**: To ensure smaller LLMs effectively open the web container and generate files rather than just a chat interface <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. A workaround currently exists by restarting the prompt after the initial generation <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Image Attachment to Prompts**: To replicate a [[feature]] from the paid `bolt.new` version that allows users to include images in their prompts <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Backend Agent Integration**: A significant [[improvements_in_project_organization_and_contribution_management | feature]] to run agents in the backend, allowing multiple LLMs to collaborate on code generation for more robust results, potentially using tools like LangChain, LangGraph, or OpenAI Swarm <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Direct GitHub Publishing**: To enable publishing projects directly to GitHub, similar to the paid version <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Loading Local Projects**: To allow users to import existing local projects (e.g., from VS Code) into the `bolt.new` app for continued development <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **General Prompt Improvements**: To refine the main `bolt.new` prompt for better overall results, especially concerning UI/UX and functionality with state management <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

This [[Open Source Development | open-source]] `bolt.new` fork is positioned as a [[community_involvement_in_bolt_diy_project | collaborative effort]], aiming to collectively improve the tool and provide a platform for learning about [[Opensource AI coding assistants and community building | leveraging AI]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The project is not intended for monetization, emphasizing its role as a [[Participating in AI hackathons and building communitydriven projects | community-driven initiative]] <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.