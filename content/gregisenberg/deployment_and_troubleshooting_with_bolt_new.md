---
title: Deployment and troubleshooting with Bolt new
videoId: lDMhK8DamuE
---

From: [[gregisenberg]] <br/> 

[[bolt_new_tool_overview | Bolt New]] is a recently launched tool that aims to simplify the process of creating prototypes and applications, even for non-technical individuals. It is considered by some to be easier than Cursor AI, potentially allowing users to create a prototype in 20 minutes or less <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The tool is seen as a culmination of various development tools integrated into one platform <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Building an Application with [[bolt_new_tool_overview | Bolt New]]

The process of [[building_a_directory_with_bolt | building a directory with Bolt]] or other applications often starts with a simple prompt. For instance, to build a text-to-image AI application, a user might instruct [[bolt_new_tool_overview | Bolt New]] to create a simple SaaS project using Next.js 14 best practices, starting with a landing page <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Unlike V0, which defaults to Next.js due to its ownership by Vercel, [[bolt_new_tool_overview | Bolt New]] requires the user to specify the use of Next.js <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

[[bolt_new_tool_overview | Bolt New]] is designed to build out the entire project structure, including layouts and landing pages, and automatically install necessary external packages for functionality <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Integrating External APIs
When integrating external services, like the Foul.ai image generation API, [[bolt_new_tool_overview | Bolt New]] guides the user on necessary steps <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This includes:
*   Installing required packages/clients <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   Setting up API keys in environment files (e.g., `.env.local`) <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   Providing code snippets for interaction with the API <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## [[design_and_deployment_with_bolt | Deployment with Bolt New]]

[[bolt_new_tool_overview | Bolt New]] offers a one-click deployment feature, partnering with Netlify for reliable hosting <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. The deployment process involves:
1.  Building the application <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.
2.  Checking for errors or issues before deployment <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
3.  Compiling the code and preparing the application for production <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
4.  Deploying to Netlify and providing a sharable URL <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

Netlify is highlighted as a robust and reliable deployment platform used by large companies <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Troubleshooting with [[bolt_new_tool_overview | Bolt New]]

While powerful, [[bolt_new_tool_overview | Bolt New]] is an early-stage tool and users may encounter bugs and issues <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

> [!NOTE] Patience is Key
> Because [[bolt_new_tool_overview | Bolt New]] operates entirely online, it can be slower, requiring more patience from users <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This slowness is attributed to its recent launch and high user traffic, with expectations that performance will improve with funding and server scaling <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Common Troubleshooting Workflow
A common workflow for troubleshooting in [[bolt_new_tool_overview | Bolt New]] involves:
1.  **Copying the error:** When an error occurs, copy the "janky text" from the terminal or error output <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
2.  **Pasting into the prompt:** Paste the error message directly into [[bolt_new_tool_overview | Bolt New]]'s prompt and instruct it to "fix this" <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This often works, though it might require multiple attempts <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
3.  **Providing additional context:** If the AI struggles, it helps to provide relevant documentation or context from external services (e.g., Foul.ai's API documentation) to guide the AI's fixes <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. Pre-researching how external services work can help avoid mistakes <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
4.  **Addressing deployment issues:** Deployment can be "finicky" especially with external packages <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. Common deployment errors include:
    *   Module not found errors <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.
    *   Type issues <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
    *   Unnecessary files or dependencies causing conflicts <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
    *   The AI may generate and install files that are not actually needed, leading to errors during deployment <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.

> [!TIP] Non-Technical User Advantage
> For non-technical users, dealing with minor bugs and re-prompting [[bolt_new_tool_overview | Bolt New]] to fix issues is often preferable to manually figuring out complex deployment processes, which can be a "whole different animal" with other tools <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. [[bolt_new_tool_overview | Bolt New]] aims to handle the "end to end" process <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

### Comparison to Other Tools
*   **[[prototype_creation_with_bolt_new | Bolt New]] vs. Cursor AI:** While Cursor AI is favored by developers who enjoy coding, [[bolt_new_tool_overview | Bolt New]] and Replit are seen as tools that "take the wheel," handling more of the process automatically <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Cursor allows the user to remain "in charge" but deployment is a separate challenge <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
*   **Target Audience:** [[bolt_new_tool_overview | Bolt New]] and Replit are ideal for non-technical founders or business people who want to instantly prototype or build simple proof-of-concepts (POCs) <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. For those aiming to understand the "nitty-gritty" or build full-fledged applications for users, deeper engagement with code (perhaps with tools like Cursor) is suggested <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

## Outlook for [[bolt_new_tool_overview | Bolt New]]

Despite current bugs, the potential of [[bolt_new_tool_overview | Bolt New]] is clear <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Improvements in speed and bug fixes are anticipated, likely with future funding and server scaling <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The expectation is that within a week of launch, many of the observed deployment issues should be resolved <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

Users are encouraged to continue playing with and exploring new AI tools like [[bolt_new_tool_overview | Bolt New]], as consistent experimentation helps develop workflows and knowledge that will be invaluable as these tools improve <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The ability to build a working prototype in under 20 minutes with just a few prompts and no code is a significant advantage <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.