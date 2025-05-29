---
title: Building a prototype with Boltnew
videoId: lDMhK8DamuE
---

From: [[gregisenberg]] <br/> 

[[introduction_to_boltnew | Boltnew]] is an emerging tool that some claim is [[comparison_between_boltnew_and_cursor_ai | replacing Cursor AI]] due to its perceived ease of use <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It is suggested that [[benefits_of_using_boltnew_for_nontechnical_users | non-technical individuals]] can use Boltnew to create a [[reallife_examples_of_products_built_using_bolt | prototype]] in 20 minutes or less <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Described as a "Cursor killer" and a "v0 killer" <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, [[introduction_to_bolt_and_its_market_potential | Boltnew]] appears to be a consolidation of various development tools into a single platform <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Despite its recent launch and some initial bugs, its potential is undeniable <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## [[stepbystep_guidance_on_using_bolt_to_build_web_applications | Step-by-Step Guidance on Using Boltnew]]

The following sections detail the process of building a text-to-image AI application using Boltnew, highlighting its capabilities and challenges.

### Project Initialization

To begin, a simple [[reallife_examples_of_products_built_using_bolt | SaaS]] project was initiated using Next.js 14 <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Unlike v0, which defaults to Next.js due to its ownership by Vercel, Boltnew requires explicit specification of Next.js as the framework <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

A prompt was used to request a simple landing page with Next.js 14 best practices <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Boltnew not only generates code for individual files but also constructs layouts, landing pages, and installs necessary external packages <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The generated landing page serves as a solid starting point <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Integrating the Text-to-Image API

The goal was to build a text-to-image application using foul.ai, an aggregator of AI models that provides simple APIs <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Foul.ai wraps various AI models with its API, allowing access through a single snippet of code <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

A prompt was given to Boltnew: "I want to build a text to image AI application. I'm going to use foul.ai. What should I do?" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Boltnew responded by outlining the steps needed to implement the text generation functionality, including setting up a foul.ai client, creating a user input form, and handling image generation <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

A critical step was to replace a placeholder in the `.env.local` file with the actual API key obtained from foul.ai <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. After providing a text prompt like "two dudes on a podcast virtually talking about AI" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, the application successfully generated an image <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Troubleshooting and Iteration

During the development process, several errors were encountered. A common strategy for fixing these was to copy the error message from the terminal and paste it into Boltnew with a request to "fix this" <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This iterative approach, despite occasional slowness from Boltnew <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, proved effective <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. It was noted that Boltnew's initial version was buggy, similar to v0 when it first launched, but is expected to improve rapidly <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

It was also suggested that providing context or documentation (like from foul.ai's docs) when errors occur can help the AI model understand and fix issues more effectively, as the AI cannot always be assumed to know everything <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

### [[deployment_challenges_with_boltnew | Deployment Challenges]]

[[deployment_challenges_with_boltnew | Boltnew offers one-click deployment]] through a partnership with Netlify, a reliable and widely used platform <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. However, the deployment process encountered multiple errors, often related to missing modules or incorrect file dependencies <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. The speaker attempted to fix these by repeatedly copying error messages and asking Boltnew to resolve them <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

A particular challenge with [[deployment_challenges_with_boltnew | Boltnew's deployment]] is its finicky nature when dealing with external packages <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. It sometimes installs unnecessary files and dependencies, leading to build failures <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. Despite these issues, the ability to achieve a working prototype in less than 20 minutes was highlighted as a significant advantage <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

### [[comparison_between_bolt_and_other_development_tools_like_cursor | Comparison with Other Tools]]

When asked about preference between [[comparison_between_bolt_and_other_development_tools_like_cursor | Cursor]] and Boltnew, the speaker stated a personal preference for [[comparison_between_bolt_and_other_development_tools_like_cursor | Cursor]] due to the enjoyment of programming and coding <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. Boltnew, while excellent for [[reallife_examples_of_products_built_using_bolt | quick prototyping]] and visualizing how an app would work, tends to "take the wheel" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. In contrast, [[comparison_between_bolt_and_other_development_tools_like_cursor | Cursor]] allows the user to remain "in charge" while providing assistance, acting like a "junior engineer" <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

Boltnew and Replit are seen on one side of the spectrum, favoring quick prototyping and "instant prototype" for [[benefits_of_using_boltnew_for_nontechnical_users | non-technical users]] or those building simple Proof-of-Concepts (POCs) <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. Cursor and v0 are on the other side, better suited for those who want to understand the "nitty-gritty" of development or build full-fledged applications for users <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

For [[benefits_of_using_boltnew_for_nontechnical_users | non-technical individuals]], Boltnew and Replit are considered clear winners because they handle the end-to-end process, including deployment <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. This contrasts with tools like Cursor, where deployment remains a separate, complex task <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

## Conclusion and Recommendations

Despite the [[deployment_challenges_with_boltnew | deployment issues]] encountered, Boltnew's ability to quickly build a working prototype was highlighted <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. The speaker recommends that users keep experimenting with these new AI tools, as continuous learning and iteration are key <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. The ability to build functional applications with a few prompts, without writing any code, demonstrates the power of tools like Boltnew <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.