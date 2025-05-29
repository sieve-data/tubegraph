---
title: Implementing reusable modular prompts in AI projects
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing with large language models (LLMs) often presents unpredictable results, leading to errors and frustrations for AI coders <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. A key strategy to achieve more consistent outcomes and streamline the AI coding workflow is the implementation of reusable modular prompts <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This approach stands in contrast to the common misconception that one can simply prompt an AI to build an entire application at once <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Why Reusable Modular Prompts?

The nature of LLMs can lead to "hallucinations" and a "bunch of errors" if not guided precisely <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. While tutorials might suggest a smooth, one-shot process, reality often involves debugging and unpredictable outcomes <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. Reusable modular prompts aim to make [[challenges_in_coding_with_ai | AI coding]] more consistent <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

Instead of writing a single, massive prompt for an entire application, the idea is to break down the development into smaller, manageable tasks using predefined, optimized prompts <a class="yt-timestamp" data-t="03:10:55">[03:10:55]</a>. This allows for a more predictable result <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

## Benefits of Modular Prompts

*   **Consistency**: Helps achieve more consistent outputs from AI coding <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   **Reduced Ambiguity**: Similar to how a product team hands off detailed specs to engineers, modular prompts provide clear instructions, reducing uncertainty <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Reusability**: Standard features like user authentication or payment systems are often the same across different projects <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. Modular prompts for these features save significant time and effort, preventing the need to "rebuild" them repeatedly <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Speed**: Aggregating a collection of reusable prompts can significantly speed up the development process <a class="yt-timestamp" data-t="56:19">[56:19]</a>.
*   **Lower Error Rates**: By breaking down tasks into smaller steps, there's less room for errors compared to trying to generate everything at once <a class="yt-timestamp" data-t="40:48">[40:48]</a>.

## Implementing Reusable Modular Prompts

### 1. Detailed Specifications and Planning

Before writing any code or prompts, dedicate significant time upfront to write very clear and detailed specifications (specs) <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. This involves:
*   **Project Overview**: A simple overview of the project's goal <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Core Functionality Breakdown**: Define the "must-have" features, similar to how a product manager would <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. For example, for a Reddit analytics platform, core functionalities might include displaying available subreddits, adding new ones, building a subreddit page with tabs for "top posts" and "analysis," and fetching/analyzing Reddit post data <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
*   **Including Documentation**: Include relevant technical documentation for key features. While AI tools might allow direct insertion of documentation, it's often more effective to include "proof of concept" code snippets that have been tested and verified to work <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. For example, demonstrating how to fetch Reddit data using a specific package (like SnowWrap) <a class="yt-timestamp" data-t="13:01:00">[01:13:01]</a>.
*   **Current File Structure**: Communicate the existing file structure to the AI. This helps prevent the AI from creating files in the wrong place or with incorrect dependencies, reducing uncertainty <a class="yt-timestamp" data-t="10:02:00">[01:10:02]</a>, <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
*   **Additional Requirements**: Add specific requirements based on the project type (e.g., for web apps, use `use client`, ensure correct file placement, use environment variables) <a class="yt-timestamp" data-t="10:20:00">[01:10:20]</a>.

### 2. Proof of Concept and Iteration

Before full implementation, build small "proof of concept" scripts for core functionalities. For instance, creating a TypeScript script to fetch subreddit posts or using OpenAI's structured output for categorization <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

When encountering errors, use [[effective_prompting_techniques | prompting techniques]] like "help me debug" or "let's think step by step" to guide the AI <a class="yt-timestamp" data-t="17:33:00">[01:17:33]</a>, <a class="yt-timestamp" data-t="29:25:00">[01:29:25]</a>. This [[sequential_prompting_with_ai_tools | sequential prompting]] helps the AI break down complex problems into smaller, more manageable steps, leading to better results <a class="yt-timestamp" data-t="29:56:00">[01:29:56]</a>.

### 3. Engineer Manager Role for AI

Leverage more powerful AI models (like 01) to act as an "engineer manager," filling in the details of the initial product document (PRD) <a class="yt-timestamp" data-t="35:38:00">[01:35:38]</a>. Provide the draft spec and ask it to structure the project files, identify dependencies, and elaborate on common rules for components and pages <a class="yt-timestamp" data-t="36:12:00">[01:36:12]</a>. This creates a detailed documentation that engineers—or the AI itself—can follow <a class="yt-timestamp" data-t="37:44:00">[01:37:44]</a>.

### 4. Functionality First, UI Later

A common mistake is trying to develop the UI and functionality simultaneously <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Instead, focus on building the core functionality first using tools like Cursor <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. Once the application's functionality is robust, then use tools like Vercel's v0 to refine the UI <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. This makes the UI design process more predictable and less prone to errors, as the underlying code is already stable <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

### 5. Leveraging Reusable Prompt Templates

Create and utilize modular prompt templates for standard features. For example, a prompt for user authentication that covers setup, library installation, sign-in, and sign-up pages <a class="yt-timestamp" data-t="52:12:00">[00:52:12]</a>.

These prompts can then be integrated into new applications by simply providing the template and instructing the AI (e.g., Cursor) to implement specific steps <a class="yt-timestamp" data-t="53:40:00">[00:53:40]</a>. This approach minimizes redundant coding and speeds up development for common functionalities like payment systems <a class="yt-timestamp" data-t="55:06:00">[00:55:06]</a>.

## Future Outlook

There is a potential for a community-driven collection or aggregator of these modular prompts to be shared, further enhancing the efficiency of AI coding <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>, <a class="yt-timestamp" data-t="55:49:00">[00:55:49]</a>. This shift moves AI coding from a trial-and-error process to a more structured and predictable workflow, similar to how traditional development operates <a class="yt-timestamp" data-t="57:10:00">[00:57:10]</a>.