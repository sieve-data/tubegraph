---
title: Opensource AI coding assistant development
videoId: aZn8PhqUZVU
---

From: [[colemedin]] <br/> 

Bolt.DIY, the official [[open_source_ai_code_generators | open-source AI coding assistant]] version of Bolt.new, has seen significant growth and development following its partnership with StackBlitz <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The project aims to become the leading [[open_source_ai_code_generators | open-source AI coding assistant]] through community collaboration and continuous improvement <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The community can engage at thinktank.automator.ai and explore the project at bolt.diy <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Project Roadmap and Vision

The Bolt.DIY team is focused on long-term development, with a publicly accessible roadmap that outlines current progress and future features <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This roadmap is subject to change as the vision for the project evolves with community input <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Completed Milestones

*   **Genesis**: Started as "bolt.new," with initial capability to use various Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Foundation Building**: Established the core maintainer team, launched the community, improved documentation and FAQs (V1), and enhanced the repository with CI/CD and issue templates <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Official Partnership**: Became the official [[open_source_ai_code_generators | open-source]] Bolt.new through the StackBlitz partnership <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Financial Incentives**: The partnership provides financial support for the project, including plans to host events with cash prizes to encourage contributions <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **High-Priority Features**: Recently implemented features include loading local GitHub projects, attaching images to prompts, and various settings improvements for overall project maturity <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Future Implementations

The roadmap outlines several key features planned for Bolt.DIY:

*   **Prompt Library**: To optimize performance across different LLMs (e.g., Claude 3.5 Sonet, Llama 3.3, Gemini) by providing tailored prompts <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This system would also be highly adjustable and extendable <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **File Walking and Diffs**: Similar to the commercial Bolt.new, this feature aims to reduce the need for constant file rewrites by the AI <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Discussions with the StackBlitz team are underway to implement this <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **One-Click Deploy**: Integration for easy deployment to platforms like Netlify <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Kanban-style Board**: To better manage Pull Requests (PRs), especially high-priority ones, providing a clear overview of team progress and backlogs <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Plugin System/Extension Marketplace**: This will allow users to contribute features on top of Bolt.DIY without directly editing the main repository <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. It will prevent "feature bloat" in the core application while enabling a rich ecosystem of add-ons <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Components include a backend for the extension library, and frontends for posting and managing plugins <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   **Potential Plugins**: Examples include uploading documents for extra context before prompting <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, implementing a pre-planning step (e.g., a reasoning model) before code generation <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>, and Superbase integration <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Agentic Systems**: Potentially a plugin allowing a "mixture of experts" (multiple agents) to create code instead of a single LLM call <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This could enable better results, especially with smaller LLMs (7 billion parameters or less) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This aligns with [[open_source_ai_agent_development | open source AI agent development]].

## Resources for [[using_ai_coding_assistance | Using AI Coding Assistance]]

To lower the barrier to entry for Bolt.DIY, the maintainer team has developed several resources:

*   **Video Guides**: Dustin, a team member, has created videos demonstrating how to use Bolt.DIY once set up, and guides for running it on Ubuntu and Windows <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Improved Documentation**: The project's README now features simplified steps for running Bolt.DIY across various operating systems, with and without Docker <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Cloudflare Pages Deployment Guide**: Michael, another core maintainer, provided a comprehensive guide for deploying Bolt.DIY using Cloudflare Pages, which is the recommended method for self-hosting beyond a local machine <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. This guide explains how to use API keys for various providers (though not Olama, which requires a local connection) <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## Recent Features and Key Contributors

The project has seen an "insane" amount of work, with many pull requests merged recently, especially following the StackBlitz partnership <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

*   **Key Contributors**: Dustin and Onur Bolat (TheKodakKiss) have been particularly instrumental, contributing a significant number of pull requests <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Other maintainers like Edward, Jonathan, and Ed have also made substantial contributions <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

*   **Official Releases**: The repository now features official releases with automatically generated changelogs via CI/CD, thanks to Onur Bolat <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

*   **New Settings Model**: This feature, heavily worked on by Dustin and Onur Bolat, offers:
    *   **Provider Toggles**: Users can enable or disable AI providers to reduce UI bloat <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
    *   **GitHub Connections**: Settings for GitHub integration <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
    *   **Experimental Prompt**: Onur Bolat implemented an optimized, experimental prompt aiming for better results than the default system prompt <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   **Debug Tab**: Dustin added a debug tab to display system information and connection status (e.g., Olama), allowing users to copy debug info for troubleshooting assistance <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

*   **Token Usage Display**: Edward implemented the ability to see token usage for both prompts and LLM outputs, which is crucial for users paying for API access to estimate costs <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

*   **Full-Screen and Resizable Preview**: Jonathan added functionality to full-screen and resize the application preview, enhancing the user experience, especially on smaller devices <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.

*   **Screenshot to LLM**: Ed recently implemented a feature allowing users to screenshot a specific part of the preview and send it directly to the LLM <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This is highly useful for pointing out UI errors or providing visual context to the AI <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

## How to Contribute

The project actively encourages community contributions. Users can propose new features in the "New Feature Discussions" subcategory on the Automator Think Tank <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Even better, contributors are encouraged to implement ideas themselves and submit a pull request <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. The goal is to build the best [[open_source_ai_code_generators | open-source AI coding assistant]] as a community <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.