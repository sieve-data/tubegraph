---
title: Deployment challenges with Boltnew
videoId: lDMhK8DamuE
---

From: [[gregisenberg]] <br/> 

[[Introduction to Boltnew | Boltnew]], a recently launched tool, has been positioned as a potential replacement for [[Comparison between Boltnew and Cursor AI | Cursor AI]], offering an easier way for non-technical users to [[Building a prototype with Boltnew | create prototypes]] in 20 minutes or less <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite its promise, being an early-stage product, it has encountered several challenges, particularly concerning deployment and overall performance <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## General Observations

Upon its launch, [[Introduction to Boltnew | Boltnew]] has exhibited some general issues and bugs <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. A primary observation is its slowness, attributed to everything being online, which necessitates more user patience <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This slowness is potentially exacerbated by a high volume of users trying out the tool <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Specific Errors Encountered During Development and Deployment

During the process of [[Building a prototype with Boltnew | building a web application with Boltnew]], several errors arose:

*   **Broken Previews and Runtime Errors**
    The application preview occasionally broke, failing to display anything <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Runtime errors also occurred during image generation attempts <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Build Failures During Deployment**
    Deploying the application via Netlify, [[Introduction to Boltnew | Boltnew]]'s integrated platform, frequently resulted in build failures <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a> <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. Specific errors included:
    *   "Cannot find module" errors, indicating missing dependencies <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.
    *   Type issues <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
    *   Issues related to unused modules or files, such as `drawer` or `rad xui`, which the system attempted to use or find, leading to build errors <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a> <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. The core problem was that [[Introduction to Boltnew | Boltnew]] installed numerous unnecessary files and dependencies, causing deployment issues <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.

## Troubleshooting Workflow

Despite the bugs, a consistent workflow was applied to address errors:
1.  **Copying Errors**: Copy the specific error message provided by [[Introduction to Boltnew | Boltnew]]'s interface or terminal <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
2.  **Prompting for Fixes**: Paste the error back into the prompt area and instruct the AI to "fix this" <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a> <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
3.  **Iterative Problem Solving**: This iterative process, requiring "grit" and persistence, often led to the AI fixing the issue, even if it took multiple attempts <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a> <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
4.  **Providing Context/Documentation**: When the AI struggled, feeding it external documentation (e.g., API snippets from `file.aero`) helped guide its corrections, acknowledging that AI doesn't always know everything <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
5.  **Manual Intervention (as a Developer)**: For persistent issues, a developer might manually install missing packages or specifically instruct the AI to remove unused files causing conflicts <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a> <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

## Comparison to Other Tools

When comparing [[Introduction to Boltnew | Boltnew]] with other development tools:

*   **[[Comparison between Boltnew and Cursor AI | Boltnew]] vs. [[Comparison between Boltnew and Cursor AI | Cursor AI]]**: While [[Comparison between Boltnew and Cursor AI | Boltnew]] is simpler for rapid prototyping for non-technical users, [[Comparison between Boltnew and Cursor AI | Cursor AI]] is preferred by developers who enjoy coding but want an AI assistant <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. [[Comparison between Boltnew and Cursor AI | Boltnew]] and Replit tend to "take the wheel," whereas [[Comparison between Boltnew and Cursor AI | Cursor AI]] allows the user to remain "in charge" <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
*   **Deployment Ease**: For non-technical individuals, [[Introduction to Boltnew | Boltnew]] and Replit are considered superior to [[Comparison between Boltnew and Cursor AI | Cursor AI]] because they handle the "end-to-end" deployment process, which can be a complex "animal" in itself <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a> <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Early Stage Comparison**: Like V0 when it first launched, [[Introduction to Boltnew | Boltnew]] is currently buggy <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. [[Comparison between Boltnew and Cursor AI | Cursor AI]] was also slow initially until it received significant funding <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## Future Outlook

Despite the current deployment challenges and finicky nature when dealing with external packages <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>, the potential of [[Introduction to Boltnew | Boltnew]] is undeniable <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. It's expected that as the team receives funding and scales their servers, the slowness and bug issues will be resolved <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a> <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. It's anticipated that within a week of its launch, many of these deployment issues should be addressed <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

The ability to create a working prototype in less than 20 minutes, even with some troubleshooting, demonstrates [[Introduction to Boltnew | Boltnew]]'s value, especially for rapid iteration and testing ideas <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a> <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.