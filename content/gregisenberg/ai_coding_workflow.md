---
title: AI coding workflow
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Building software with Artificial Intelligence (AI) can be challenging, particularly with large language models (LLMs) which often produce unpredictable results and errors, contrary to the smooth demonstrations seen in online tutorials <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To achieve more consistent outcomes, a structured [[ai_workflow_automation | AI workflow automation]] is essential <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This article outlines a proven approach to [[building_an_ai_startup_workflow | building an AI startup workflow]] for coding, emphasizing upfront planning, strategic tool usage, and the leverage of reusable components.

## The AI Coding Workflow

The proposed workflow focuses on three key principles to make AI coding more reliable and efficient:

### 1. Spend Upfront Time Writing Clear and Detailed Specs

One of the most crucial initial steps is to dedicate significant time to writing very clear and detailed specifications (specs) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. While planning is generally acknowledged as important, the specifics of *how* to write an effective spec for AI communication are often overlooked <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

#### Simulating a Product Team Workflow
The ideal process simulates a traditional product team workflow <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   A Product Manager (PM) writes the core functionality spec <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   An Engineering Manager (EM) specs out individual tickets or the project architecture, reducing ambiguity for later stages <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   This EM role can be effectively filled by a stronger LLM, like GPT-40, to expand initial high-level specs into detailed engineering requirements <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>.

#### Benefits of Detailed Specs
*   **Uncover Uncertainty:** Upfront planning helps identify and address uncertainties early in the process <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Consistent Results:** Leads to more predictable and consistent coding outcomes <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Reduced Ambiguity:** Minimizes misinterpretations by the AI, ensuring the delivered product aligns with expectations <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a>.

### 2. Be Clear About the Role of Different Platforms (Cursor First, V0 Second)

Various [[comparison_of_ai_coding_tools | AI coding tools]] exist, such as Cursor, V0, and Replit <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. A key insight is to define specific roles for each tool:
*   **Cursor for Functionality:** Focus on using Cursor to build the core functionality, completely ignoring the User Interface (UI) at the initial stage <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **V0 for UI Touch-ups:** Only after the functionality is robust should V0 be used to refine and improve the UI <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This approach often leads to greater success compared to trying to achieve everything at once, as AI can struggle with open-ended requests, making it difficult to correct structural issues later <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### 3. Reusable Modular Prompts

Developing and using reusable modular prompts is a powerful technique <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. While platforms like Cursor offer shared rules, they often prove less useful <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Instead, focus on standard features like user authentication or payment systems, which are largely the same across many projects <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

#### Standard Features Example (User Auth)
A modular prompt for user authentication (user auth) can be reused across different applications, quickly generating the necessary sign-in and sign-up pages <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.

#### Community Aggregation Idea
There's potential for a community-driven collection or aggregator of these modular prompts to be shared, significantly accelerating the development process for standard features <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.

## Case Study: Building a Reddit Analytics Platform

To illustrate this workflow, the speaker demonstrates building a Reddit analytics platform, inspired by Gumy Search <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Project Overview
The goal is to build a Reddit analytics platform where users can get analytics for different subreddits, view top content, and categorize posts <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### Core Functionality
Key features include <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>:
*   Listing and adding new subreddits <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   A subreddit page with "Top Posts" and "Analysis" tabs <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   Fetching Reddit post data and categorizing them into themes <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Adding Documentation and Proof of Concepts

Before starting the main build, two proof-of-concept scripts are developed:

1.  **Reddit Data Fetching (Snowrap):**
    *   Research packages (e.g., via ChatGPT) to find suitable libraries like `snowrap` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   Examine package documentation and examples (e.g., on npm) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
    *   Prompt Cursor Composer to create a TypeScript script to fetch subreddit posts, specifying required data fields and secure credential handling (e.g., `.env` files) <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
    *   **Debugging and Iteration:** This stage often involves debugging errors, using prompts like "help me debug" or "help me fix this" <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. The importance of preparing Reddit API credentials upfront is noted <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

2.  **OpenAI Structured Output for Categorization:**
    *   Prompt Cursor Composer to build a TypeScript script using OpenAI's structured output to categorize subreddit posts based on predefined categories (e.g., "tools and solutions," "pain and anger," "advice requests," "money talk") <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
    *   **Iterative Refinement:** Initial attempts by the AI might use outdated models or fail to follow instructions (e.g., ignoring structured output) <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>. Direct feedback ("you are not following the best practice") and specific instructions (e.g., use `users.package`, GPT-40 model, move descriptions to model, make prompt generic, avoid specifying JSON output structure) are crucial for refinement <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
    *   **"Let's think step by step":** This prompting technique, inspired by "Chain of Thought" reasoning, helps the LLM break down complex problems into smaller, manageable steps, leading to better results <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.

### Setting Up the Project (Shadcn, Github)
*   Initialize a new GitHub repository for version control <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   Use `shadcn/ui` for UI components, as it's clean, offers good coverage, and is compatible with V0 <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.
*   Generate the current file structure using a tool like `tree` to communicate the project layout to the AI, preventing file placement errors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

### Leveraging LLMs for Detailed PRD (01 Model as "Engineer Manager")
*   The initial high-level spec is fed into a stronger LLM (e.g., `01 Model`) to act as an "engineer manager." <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>
*   This model proposes a detailed project structure, identifies dependencies, and fills in architectural details, turning a product manager's spec into an engineer-ready document <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.

### Step-by-Step Implementation with Cursor
With a detailed spec and file structure, Cursor is then prompted to build the application step-by-step <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>.
*   Break down the build into smaller, manageable tasks, reducing the likelihood of errors <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.
*   Focus on implementing core functionalities first (e.g., displaying subreddit cards, then the subreddit page structure, then data fetching and categorization) <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
*   Regularly run the application (`npm run dev`) and test to identify and debug issues <a class="yt-timestamp" data-t="00:40:16">[00:40:16]</a>.

### Refining UI with V0
Once the functionality is built and working, V0 is used to enhance the UI <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.
*   Provide clear instructions, such as preferring a "black and white" style similar to Vercel, to guide the AI's design choices <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.
*   The key is to give the AI good design language, potentially by referencing design books, to get better visual outcomes <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>.

## Benefits and Outlook

*   **Improved Success Rate:** This structured approach significantly improves the success rate of [[ai_tools_for_building_software | AI tools for building software]], making the results more predictable <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Democratization of Product Management:** [[Explaining code and learning through AI assistance | AI coding]] enables a wider range of people, including those without traditional coding backgrounds, to become product managers and build products <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   **Future of AI Coding Tools:** Future tools like Bolt may automate the current manual step-by-step prompting, streamlining the workflow further <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>.
*   **Analogy: Electric-Assisted Bicycle:** AI coding is like an electric-assisted bicycle; you still need to pedal (plan and guide), but it provides a significant boost, making development much easier than traditional methods <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.

This structured workflow transforms the often frustrating experience of AI coding into a more efficient and productive process, moving users from merely "using AI coding" to becoming an "[[ai_tools_for_app_development | AI coder]]" <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>.

# Further Resources
For more [[ai_workflow_automation | AI workflow automation]] tutorials and experiments, check out AI Jason on YouTube <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.