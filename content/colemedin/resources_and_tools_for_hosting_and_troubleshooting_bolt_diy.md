---
title: Resources and tools for hosting and troubleshooting Bolt DIY
videoId: aZn8PhqUZVU
---

From: [[colemedin]] <br/> 

The Bolt DIY project provides various resources and tools to assist users in getting started, hosting the application, and troubleshooting common issues <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>. The team is dedicated to continuously improving these resources to lower the barrier to entry <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

## Community and General Information

*   **Community Platform**
    The official community for Bolt DIY is available at [[community_involvement_in_bolt_diy_project | thinktank.automator.ai]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This platform serves as a hub for discussions, updates, and collaborative efforts.
*   **Official URL**
    The project's URL is bolt.DIY <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   **Roadmap**
    A detailed roadmap for Bolt DIY is available and linked in the video description, the project's README, and other documentation <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This roadmap serves as a guiding pillar for the project's direction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. While there are no strict timelines, the roadmap is subject to change as the vision for Bolt DIY evolves collaboratively <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Getting Started and Self-Hosting

The maintainer team has worked diligently to build a comprehensive set of resources for getting started with Bolt DIY and hosting it yourself <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   **Dustin's Resources**
    Dustin, a core maintainer, has created a post on the Automator Think Tank with helpful resources for getting started with Bolt DIY <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>. These include videos on:
    *   How to use Bolt DIY once it's set up <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>.
    *   Instructions for running Bolt DIY on Ubuntu and Windows. The Windows video does not have audio, requiring users to follow along with the commands shown <a class="yt-timestamp" data-t="01:10:36">[01:10:36]</a>.
*   **Improved Documentation**
    The project's documentation, particularly in the README, has been simplified to provide clearer steps for running Bolt DIY on various operating systems <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>. Instructions cover both Docker and non-Docker setups <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Efforts are ongoing to make the documentation easier to understand and improve the Docker setup <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>.
*   **Cloudflare Pages Deployment Guide**
    Michael, another core maintainer, developed a comprehensive guide for deploying Bolt DIY using Cloudflare Pages <a class="yt-timestamp" data-t="01:11:17">[01:11:17]</a>. This method is recommended for self-hosting Bolt DIY without running it on your local computer <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>.
    *   The guide is extensive but features many images and detailed explanations, making it reliable for users to follow all necessary steps <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.
    *   It typically takes less than 20 steps to complete <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>.
    *   While hosting via Cloudflare Pages allows for a public URL, it will not connect to a locally running Ollama instance <a class="yt-timestamp" data-t="01:12:17">[01:12:17]</a>. However, other language model providers will work, and API keys can be set directly within the UI <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.

## Troubleshooting Tools

The project includes built-in features and resources to aid in troubleshooting issues.

*   **Debug Tab in Settings**
    Dustin implemented a debug tab within the new settings modal <a class="yt-timestamp" data-t="01:15:51">[01:15:51]</a>. This tab provides system information and can verify the connection to Ollama <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. Users can copy their debug information to paste into troubleshooting posts on the community forum, allowing the team to better assist them <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.
*   **Prompting with Screenshots**
    Ed, a maintainer, added the capability to screenshot a specific part of the preview and send it to the Large Language Model (LLM) <a class="yt-timestamp" data-t="01:18:31">[01:18:31]</a>. This feature is highly useful for pointing out errors or specific UI elements that need correction, such as when the LLM makes a mistake <a class="yt-timestamp" data-t="01:18:40">[01:18:40]</a>. This allows users to provide visual feedback instead of solely relying on text descriptions <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>. It can also be used to share snippets of errors within the web container <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Feature Discussion

Users are encouraged to suggest new features for Bolt DIY by posting their ideas in the "New Feature Discussions" subcategory within the [[community_involvement_in_bolt_diy_project | Automator Think Tank]] <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. Even better, users are encouraged to implement features themselves and submit a pull request to the repository <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.