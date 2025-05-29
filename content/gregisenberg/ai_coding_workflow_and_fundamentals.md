---
title: AI coding workflow and fundamentals
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Successfully leveraging AI for coding requires a structured approach that addresses the inherent unpredictability of large language models (LLMs) <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. While tutorials might suggest that AI can build an entire application from a simple prompt <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>, reality often presents unpredictable results and numerous errors <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. The problem to solve is how to streamline the [[challenges_in_coding_with_ai | AI coding flow]] to achieve more predictable outcomes <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

## Core Workflow Principles

An effective [[ai_workflow_integration_strategies | AI workflow integration strategy]] focuses on consistency and reducing ambiguity <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. The recommended workflow involves three key steps:

### 1. Write Clear and Detailed Specs Up Front

Spending significant time upfront to write very clear and detailed specifications is crucial <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. This step is about communicating effectively with AI, much like a product team works with engineers <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

*   **Simulate Product Team Process**: The aim is to simulate how a product team normally works, with a Product Manager (PM) writing core functionality specs and an engineering manager detailing individual tickets or architecture <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This leaves less ambiguity <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Uncover Uncertainty**: This process helps uncover many uncertainties upfront, leading to more consistent results <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   **Structure**: A common spec structure includes a project overview, core functionality breakdown, documentation for key features, current file structure, and additional requirements <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
    *   **Project Overview**: Simple statement of the project's purpose, e.g., "building a Reddit analytics platform" <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.
    *   **Core Functionality**: Must-have features, e.g., listing subreddits, adding new ones, displaying top posts and analysis in tabs <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
    *   **Key Feature Documentation**: Include proof-of-concept code snippets for critical functionalities, such as fetching data (e.g., Reddit posts with Snow-Wrap) and categorizing data using structured output (e.g., OpenAI) <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. This allows for early debugging and alignment <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
    *   **File Structure**: Communicate the project's file structure to AI tools like [[comparison_of_ai_coding_tools | Cursor]] to prevent incorrect file creation or dependency issues <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. Tools like `tree` can help generate this <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>.
    *   **Additional Requirements**: Specific instructions for web apps (e.g., `use client`, environment variables, error handling) or iOS apps (e.g., file creation, API calls) <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>. These can be saved as templates <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
*   **Leverage Stronger Models for Detail**: Use more powerful models (e.g., GPT-4o) to expand the initial draft into a detailed Product Requirement Document (PRD) <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. This acts like an "engineer manager" filling in architectural details and dependencies <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>.

### 2. Be Clear About the Role of Different Platforms

Understanding when to use which tool for specific tasks is essential <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

*   **Functionality First (e.g., [[comparison_of_ai_coding_tools | Cursor]])**: Focus [[comparison_of_ai_coding_tools | Cursor]] on building core functionality without initially considering the User Interface (UI) <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This is contrary to common practice but yields more success <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Building functionality first ensures the core project works as intended, making UI improvements more predictable later <a class="yt-timestamp" data-t="46:08:00">[46:08:00]</a>.
*   **UI Touch-ups Later (e.g., Vercel v0)**: Use tools like Vercel v0 to refine and enhance the UI interface bit by bit, once the underlying functionality is robust <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. Providing examples of desired styles, like "similar to Vercel," helps guide the AI <a class="yt-timestamp" data-t="46:48:00">[46:48:00]</a>.

### 3. Reusable Modular Prompts

Developing and sharing reusable, modular prompts for standard features can significantly speed up the development process <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

*   **Standard Features**: Features like user sign-in (authentication) or payment systems are often similar across different projects <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. Instead of rebuilding them every time, a collection of pre-tested prompts can generate the entire functionality <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   **Community Sharing**: The community could benefit from an aggregator of such modular prompts to facilitate sharing and reuse <a class="yt-timestamp" data-t="55:14:00">[55:14:00]</a>.

## Practical Application: Building a Reddit Analytics Platform

The described workflow is demonstrated through building a Reddit analytics platform <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Initial Setup and Spec Creation

1.  **Repository Setup**: Start with GitHub for version control <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.
2.  **Draft Spec**: Begin with a draft spec inside the [[comparison_of_ai_coding_tools | Cursor]] composer, outlining the project overview, core functionalities, and additional requirements <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
3.  **Proof of Concept (POC)**: Before full implementation, build small POCs for critical functionalities.
    *   **Reddit Data Fetching**: Use ChatGPT to identify a suitable package (e.g., Snow-Wrap) for fetching Reddit data in a Next.js project <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. Then, use [[comparison_of_ai_coding_tools | Cursor]] to generate a simple TypeScript script to fetch posts, including details like title, link, and score <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>. Ensure environment variables (`.env`) are used for credentials <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.
    *   **OpenAI Structured Output**: Create a script using OpenAI's structured output to categorize subreddit posts based on predefined categories (e.g., "tools and solutions," "pain and anger," "advice request," "money talk") <a class="yt-timestamp" data-t="20:34:00">[20:34:00]</a>. It's important to refine the prompt to make it generic and avoid hardcoding JSON structures <a class="yt-timestamp" data-t="25:49:00">[25:49:00]</a>.
    *   **Debugging POCs**: [[debugging_and_problemsolving_strategies_with_ai_coding | Debugging and problem-solving strategies with AI coding]] are crucial here. If errors occur, prompt the AI with "help me debug" or "help me fix it" <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. For more complex issues, using "let's think step by step" leverages a "chain of thought" prompting technique, breaking down problems into smaller steps for better results <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.
4.  **Project Setup**: Initialize the project (e.g., with Shadcn UI components like button, input, dialogue, tabs) <a class="yt-timestamp" data-t="32:30:00">[32:30:00]</a>. Create an `instructions` folder and copy the draft spec and `.env.local` file <a class="yt-timestamp" data-t="33:42:00">[33:42:00]</a>.
5.  **Generate Detailed File Structure**: Use a tree command to capture the project's file structure (excluding `node_modules` and `.git`) <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>. Paste this into the spec to inform [[comparison_of_ai_coding_tools | Cursor]] where to create files <a class="yt-timestamp" data-t="35:10:00">[35:10:00]</a>.
6.  **Engineer Manager Role (GPT-4o)**: Use a stronger model like GPT-4o to elaborate on the spec, generating a comprehensive project file structure and identifying dependencies based on the initial documentation <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>. This detailed PRD makes the development process much smoother for the AI, similar to how engineers prefer detailed specs <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a>.

### Iterative Building with AI

Once the detailed spec is ready, build the application functionality step by step using [[comparison_of_ai_coding_tools | Cursor]].

1.  **Break Down Tasks**: Instead of one-shotting the entire application, break it down into smaller, manageable tasks defined by the spec <a class="yt-timestamp" data-t="39:41:00">[39:41:00]</a>. This reduces the likelihood of errors and makes debugging easier <a class="yt-timestamp" data-t="40:47:00">[40:47:00]</a>.
2.  **Iterative Implementation**: Implement each part sequentially, prompting [[comparison_of_ai_coding_tools | Cursor]] to refer to the documentation and make sure it builds according to the plan <a class="yt-timestamp" data-t="40:39:00">[40:39:00]</a>.
3.  **Debugging**: If errors occur, add debug information to the code <a class="yt-timestamp" data-t="42:35:00">[42:35:00]</a>. This provides [[comparison_of_ai_coding_tools | Cursor]] with specific error messages to fix, improving the effectiveness of [[debugging_and_problemsolving_strategies_with_ai_coding | debugging and problem-solving strategies with AI coding]] <a class="yt-timestamp" data-t="42:52:00">[42:52:00]</a>.
4.  **UI Refinement**: Once the core functionality is stable, transition to Vercel v0 to refine the UI. Since the code is already functional, UI adjustments become more predictable <a class="yt-timestamp" data-t="46:02:00">[46:02:00]</a>.

### Reusable Prompts in Action

A crucial aspect of [[ai_workflow_integration_strategies | AI workflow integration strategies]] is the use of reusable prompts. For instance, a pre-written prompt for user authentication can be adapted and applied to different projects <a class="yt-timestamp" data-t="52:01:00">[52:01:00]</a>. By following the documented steps within the prompt (e.g., setting up OAuth, installing libraries, building sign-in/sign-up pages), [[comparison_of_ai_coding_tools | Cursor]] can quickly implement standard features <a class="yt-timestamp" data-t="53:33:00">[53:33:00]</a>. This approach can be extended to other common functionalities like payment systems <a class="yt-timestamp" data-t="55:06:00">[55:06:00]</a>.

## Conclusion

This structured workflow, emphasizing detailed upfront planning, specific tool roles, and reusable prompts, transforms [[challenges_in_coding_with_ai | AI coding challenges]] into a more predictable and efficient process <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>. It changes the role of the product manager, enabling them to also act as engineers by writing specs and building the product <a class="yt-timestamp" data-t="38:10:00">[38:10:00]</a>. While not a one-shot solution, it significantly speeds up development compared to traditional methods, providing an "electric-assisted bicycle" boost to the coding process <a class="yt-timestamp" data-t="57:37:00">[57:37:00]</a>.