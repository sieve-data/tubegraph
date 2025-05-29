---
title: Combining different AI tools for effective development
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing applications with large language models (LLMs) can be challenging, as the results are often unpredictable due to the models' tendency to "hallucinate" [00:00:53]. Tutorials might suggest that prompts can build an entire application, but in reality, this often leads to errors [00:01:00]. This article outlines a streamlined [[comparison_of_ai_coding_tools | AI coding]] workflow designed to yield more consistent results [00:00:28].

## Core Workflow Principles

To achieve more consistent and predictable [[building_apps_using_ai_tools | app development]] with AI tools, the following principles are crucial:

### 1. Write Clear and Detailed Specifications
Spending significant upfront time on writing clear and detailed specifications is the most important step [00:01:30]. This concept, while often mentioned in [[planning_before_using_ai_tools | planning before using AI tools]], isn't always detailed [00:01:45]. The process should simulate how a product team works:
*   **Product Manager Role (Initial Spec)**: Define core functionalities [00:02:00].
*   **Engineer Manager Role (Detailed Spec)**: Break down into individual tickets, architect the project structure, and minimize ambiguity [00:02:06].

This approach helps uncover uncertainties early on [00:02:23] and leads to a more consistent output [00:02:30]. A detailed specification includes:
*   Project overview and goals [00:09:21].
*   Core functionalities [00:09:25].
*   Documentation on how to implement key features [00:09:37].
*   Current file structure to guide the AI [00:10:02].
*   Additional requirements specific to the project type (e.g., web app, iOS app), such as `use client` directives, environment variables, and error handling [00:10:20].

### 2. Clearly Define the Role of Each Platform
Different [[tools_and_platforms_for_ai_app_development | AI development platforms]] serve different purposes, and understanding when to use which is key [00:02:37].
*   **Cursor**: Focus solely on core functionality, ignoring UI initially [00:02:49].
*   **V0**: Used later to refine the UI [00:02:57]. This is contrary to common practice where `v0` is often used first for wireframes [00:04:29]. The rationale is that if the structure is open-ended, it's hard to change once `Cursor` generates code [00:06:01].

### 3. Leverage Reusable Modular Prompts
Standard features like user authentication or payment systems are often similar across projects [00:03:37]. Creating a collection of reusable, modular prompts for these standard functionalities can significantly speed up development [0003:49]. These prompts can be given to `Cursor` to generate entire functionalities [00:03:52].

> [!info] The "Chain of Thought" Prompting Technique
> When dealing with complex problems or persistent errors, a technique called "Chain of Thought" prompting can be effective. By prompting the AI to "think step by step," it breaks down the problem into smaller, manageable steps, leading to better results than asking it to solve everything at once [00:30:06]. This helps in debugging and refining the AI's output [00:30:28].

## Case Study: Building a Reddit Analytics Platform

This workflow can be demonstrated by attempting to rebuild a simplified version of "Gumy Search," a platform that extracts structured insights from unstructured data [00:07:48].

### Initial Setup and Spec Generation
1.  **Project Initialization**: Start with GitHub for version control and open the project in `Cursor` [00:08:48].
2.  **Drafting the Spec**: Begin with a draft spec including project overview, core functionalities (e.g., list subreddits, add new subreddits, show top content, categorize posts), and a placeholder for documentation and file structure [00:09:10].
3.  **Pre-requisite Research and Proof of Concept (PoC)**:
    *   **Reddit Data Fetching**: Research `Next.js` packages for Reddit data. `Snowrap` was identified [00:13:09]. A simple TypeScript script to fetch subreddit posts (title, link, content, score, comments) using `Snowrap` with environment variables for credentials was created and tested in `Cursor` [00:14:53]. This early PoC helps identify and fix errors that would otherwise appear later [00:17:19].
    *   **OpenAI Categorization**: Research using OpenAI's structured output for categorizing posts. A script was developed to categorize subreddit posts into predefined categories (e.g., "tools and solutions," "pain and anger," "advice request," "money talk") with a specific boolean output format [00:20:26]. This PoC revealed `Cursor` might initially ignore documents and use older models, requiring further prompting to enforce best practices and specify the `GPT-4o` model for structured output [00:24:32].
    *   **Documenting PoCs**: Once working, the PoC code examples and expected responses are added to the detailed specification [00:19:19], [00:31:32].

### Project Structuring and Detailed PRD Generation
1.  **Initial Project Setup**: Use a tool like `Shadcn` for setting up the project and adding necessary UI components (e.g., button, input, dialogue, tabs, table, sheet, card) [00:32:30].
2.  **File Structure Communication**: Use a package like `tree -L 2` to generate the current file structure and include it in the specification to help `Cursor` understand where to create files [00:34:16].
3.  **Engineer Manager Role (01 Model)**: Use a stronger model like `01 Model` to fill in the gaps and provide a more detailed architectural plan [00:35:38]. This includes generating a proposed final file structure and identifying dependencies, similar to an engineer manager's role in refining a product requirements document (PRD) [00:37:00]. This detailed PRD, including variables and file structures, reduces ambiguity for the AI and results in a more robust end product [00:38:07].

### Iterative Building with Cursor and UI Refinement with V0
1.  **Step-by-step Development**: Break down the building process into small, manageable tasks based on the detailed spec. For example, build the subreddit list first, then the subreddit page, and then integrate data fetching and categorization [00:40:39]. This reduces errors and prevents the AI from skipping steps [00:40:47].
2.  **Debugging**: When errors occur, prompt `Cursor` to add debug information to understand the issue better [00:42:35]. Persist in fixing issues, even if it's frustrating [00:27:21].
3.  **UI Touch-up with V0**: Once the core functionality is built, use `v0` to improve the UI [00:46:02]. Provide the existing code and instruct `v0` to maintain functionality while making UI improvements, specifying desired styles (e.g., "black and white," "dark mode," "similar to Vercel") [00:46:33]. Providing design language or referencing design books can also help `v0` generate better designs [00:47:21].

### Reusable Modular Prompts for Standard Features
For features like user authentication (user "o" function), which are standard across many projects, a pre-written modular prompt can be used [00:52:01]. This prompt, containing detailed setup instructions (e.g., Auth.js setup, library installation), can be integrated into the project by prompting `Cursor` to follow the setup steps [00:53:33]. This significantly accelerates the development of common functionalities [00:54:59].

## Conclusion
This structured approach to [[building_apps_using_ai_tools | building apps using AI tools]] by combining detailed [[planning_before_using_ai_tools | planning before using AI tools]], a clear division of labor between `Cursor` (functionality) and `v0` (UI), and leveraging reusable modular prompts, significantly improves the success rate of [[comparison_of_ai_coding_tools | AI coding]] [00:56:05]. While it may feel more structured than typical "one-shot" [[comparison_of_ai_coding_tools | AI coding]] tutorials, it aligns more with traditional software development expectations, leading to more robust and usable applications [00:57:06]. This workflow transforms developers from simply using AI tools to becoming effective "AI coders" [00:51:19], enabling them to tackle [[building_ai_startup_using_ai_tools | AI startup ideas]] with greater efficiency.