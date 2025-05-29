---
title: Using modular and reusable prompts
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

[[Developing and customizing AIdriven projects | AI coding]] has become a powerful tool for building applications, but achieving consistent and predictable results can be challenging due to the large language model's tendency to "hallucinate" or provide unpredictable outputs <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To address this, an effective workflow includes leveraging modular and reusable prompts <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## What Are Modular and Reusable Prompts?

Modular and reusable prompts are pre-defined sets of instructions or code examples that encapsulate common functionalities or features that are often needed across different projects <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Instead of re-prompting for basic features every time, these prompts allow developers to quickly integrate standard functionalities.

For example, core functionalities like user sign-in authentication and payment systems are largely the same across various applications <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. A modular prompt for user authentication, once crafted and refined, can be reused in any new project, saving significant time and effort <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.

## Benefits of Reusable Prompts

*   **Consistency**: They help achieve a more consistent output from AI models, reducing the likelihood of errors <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Efficiency**: They speed up the development process significantly by automating the creation of standard features <a class="yt-timestamp" data-t="00:56:22">[00:56:22]</a>.
*   **Reduced Ambiguity**: By providing clear, pre-tested instructions for common tasks, they reduce ambiguity for the AI, similar to how detailed specifications reduce ambiguity for human engineers <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>.
*   **Scalability**: They make it easier to add new features or categories by making the prompts more generic and less tied to specific instances <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

## Using Modular Prompts in Practice

The process involves having a collection of these prompts ready for common features. While some platforms like Cursor offer directories for rules, these are often not as useful as well-crafted, reusable prompts for specific functionalities <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

An example workflow for integrating a reusable prompt for user authentication:
1.  Prepare a detailed specification document (e.g., `setup_auth.md`) for authentication, including steps and expected outcomes <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
2.  Use this document as a `data-t="00:53:38"` target for the AI (e.g., Cursor) <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
3.  Instruct the AI to build the authentication features "strictly based on this setup_auth.md" <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
4.  Break down the implementation into smaller, sequential steps (e.g., "build step three and step four", then "step five", then "step six") to ensure better results and reduce errors <a class="yt-timestamp" data-t="00:53:54">[00:53:54]</a>. This [[sequential_prompting_with_ai_tools | sequential prompting]] approach minimizes the chances of the AI skipping steps or producing incorrect code <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.

The result is a functional login feature that integrates seamlessly into the application, which can be reused for other platforms that require similar standard features like payments <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.

## The Future of Modular Prompts

The speaker envisions a community where a collection of these standard feature prompts can be shared <a class="yt-timestamp" data-t="00:55:14">[00:55:14]</a>. This would allow developers to easily take a prompt and integrate it into their applications, acting as a shortcut for common development tasks <a class="yt-timestamp" data-t="00:55:23">[00:55:23]</a>. There is a desire for developer tools to build new ways for people to use such prompts, potentially through an aggregator <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>.

By adopting a structured workflow that prioritizes writing detailed specifications and utilizing reusable modular prompts, developers can significantly improve the success rate of [[developing_and_customizing_aidriven_projects | AI coding]] projects <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. This shifts the focus from simply asking AI to "build the whole thing" to a more disciplined, step-by-step approach that yields more reliable results <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>.