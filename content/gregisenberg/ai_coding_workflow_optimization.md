---
title: AI coding workflow optimization
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Optimizing the [[AI tools and productivity enhancement | workflow for AI coding]] is crucial to achieve more predictable and consistent results, especially since large language model (LLM) based coding can be highly unpredictable and prone to errors or "hallucinations" in its initial outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Many online tutorials often present a smooth, one-shot process that doesn't reflect the reality of using AI for coding <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Core Principles of an Optimized AI Coding Workflow

The aim is to introduce a workflow that makes [[AI app development strategies | AI app development]] more consistent and reliable <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### 1. Write Clear and Detailed Specifications (Specs) Upfront
Spending significant time on writing very clear and detailed specifications is the first and most important step <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This process aims to simulate how a product team normally functions, where a product manager outlines core functionalities, and an engineering manager specs out individual tickets or architectural structures to minimize ambiguity <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This upfront planning helps uncover many uncertainties early on <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### 2. Be Clear About the Role of Different Platforms
It's essential to understand when to use specific [[comparison_of_ai_coding_tools | AI coding tools]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. A recommended approach is to:
*   **Cursor First**: Use Cursor to focus purely on core functionality, completely ignoring the user interface (UI) initially <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Vercel's v0 Second**: Once the core functionality is robust, then use v0 to refine and touch up the UI <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This sequential approach leads to much greater success than attempting to build everything at once <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Trying to keep the development open-ended from the start often results in outputs that aren't what's desired, and changing fundamental structures later becomes very difficult <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### 3. Leverage Reusable Modular Prompts
The concept of reusable modular prompts is particularly powerful <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. While platforms like Cursor offer "rules" or directories, these often don't provide significant value <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. What's truly beneficial are standard features and functionalities that are consistently needed across different projects, such as user authentication or payment systems <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. A community-driven collection of such prompts could allow users to quickly integrate full functionalities into their projects <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Practical Application: Building a Reddit Analytics Platform

To illustrate this workflow, the process of building a Reddit analytics platform, similar to "GummySearch," is demonstrated <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This platform would analyze Reddit posts to extract structured insights from unstructured data <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### 1. Initial Project Setup
*   Start with GitHub for version control <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   Open the project in Cursor <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### 2. Drafting the Initial Spec
Instead of immediately prompting Cursor to build the platform, begin by drafting a detailed spec using a template <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Project Overview**: A simple description of the application, e.g., "building a Reddit analytics platform where users can get analytics of different subreddits" <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Core Functionality**: Break down essential features, such as listing subreddits, adding new ones, displaying top posts and insights with categorization tabs, and fetching Reddit data <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. The spec should be clear enough to convey the project's goal and core functionalities without excessive detail at this stage <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

### 3. Including Key Feature Documentation/Proof-of-Concept
Integrate documentation and proof-of-concept (POC) code for critical functionalities <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This builds confidence in core features and minimizes future issues <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Reddit Data Fetching**: Research packages (e.g., `snoowrap` via ChatGPT or Google) <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. Create a simple TypeScript script to fetch subreddit posts (e.g., from `r/Docs`) including title, link, content, score, and comments, using `.env` for credentials <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Debugging these POCs early helps catch errors that would otherwise appear later <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **OpenAI Structured Output for Categorization**: Build a script using OpenAI's structured output to categorize subreddit posts into predefined categories (e.g., "tools and solutions," "pain and anger," "advice request," "money talk") <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. This often requires iterative prompting to ensure the correct model (`GPT-4o`) and structured output format are used, as initial AI responses might use outdated information or incorrect structures <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>. Explicitly providing code examples and detailing desired output formats helps <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. Using prompts like "let's think step by step" can help the AI break down complex problems and achieve better results <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
*   **Current File Structure**: Include the current file structure (e.g., generated by `tree -L 2`) in the spec. This guides Cursor on where to create files and manage dependencies, preventing incorrect file placement and broken dependencies <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Additional Requirements**: Add common requirements specific to the project type (e.g., for web apps: `use client` directives, environment variables, error handling) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### 4. Refining the Spec with a Stronger Model (e.g., GPT-4o)
Leverage a more powerful model like GPT-4o to act as an "engineer manager" to fill in details and architectural considerations <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.
*   Paste the entire draft spec into the model.
*   Prompt it to generate a detailed project file structure, common rules (e.g., component folders, page routing), and identify dependencies <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
*   Then, instruct it to add all the details from the original Product Requirements Document (PRD), including variables and additional requirements, without generating actual code <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. This results in a comprehensive PRD that leaves less ambiguity for the AI to interpret <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

### 5. Building the App Incrementally with Cursor
With the detailed spec, begin building the application piece by piece using Cursor Composer <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.
*   Commit the project setup <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>.
*   Prompt Cursor to build specific sections or "steps" from the detailed spec one at a time <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>. This significantly reduces the likelihood of errors and ensures the AI doesn't skip steps <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.
*   Debug errors by asking Cursor to add debug information or providing specific error messages <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

### 6. UI Refinement with Vercel's v0
Once the core functionality is built and working, turn to [[ai_tools_for_nocode_integration | UI tools]] like v0 <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.
*   Paste the existing functional code into v0.
*   Prompt v0 to "make the UI a ton better," optionally specifying desired styles (e.g., "black and white, dark mode, similar to Vercel") <a class="yt-timestamp" data-t="00:46:31">[00:46:31]</a>. Providing specific design language (e.g., from design books) can significantly improve results <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.
*   The process becomes more predictable and easier because the underlying functionality is already stable <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.

### 7. Demonstrating Reusable Modular Prompts
A key aspect of this workflow is the use of pre-prepared, reusable prompts for common functionalities, like user authentication <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.
*   Store these prompts as Markdown files (e.g., `setup_auth.md`) <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
*   When a new project requires authentication, simply paste the prompt with the necessary credentials and instruct Cursor to build specific steps of the authentication flow <a class="yt-timestamp" data-t="00:52:43">[00:52:43]</a>.
*   This significantly speeds up development for standard features, reducing redundant coding <a class="yt-timestamp" data-t="00:54:59">[00:54:59]</a>. The idea is to foster a community collection of such prompts <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>.

## Benefits and Conclusion
This structured approach to [[designing_and_optimizing_ai_tasks_and_agents | AI coding]] significantly improves the success rate and leads to more usable applications <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. By front-loading the planning, breaking down tasks, and separating functionality from UI, the development process becomes much more predictable <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. While it's less glamorous than "one-shot" app creation tutorials, it's the practical way to transition from casual AI use to becoming a proficient AI coder <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. It turns AI coding into an "electric-assisted bicycle"—you still pedal, but the AI provides a powerful boost <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.