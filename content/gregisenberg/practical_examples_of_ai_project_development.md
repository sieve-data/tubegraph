---
title: Practical examples of AI project development
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

This article outlines a structured workflow for [[building_apps_with_ai_tools | AI coding]], aiming for more consistent and predictable results than often portrayed in online [[tutorial_on_ai_tools_and_startup_ideas | tutorials on AI tools and startup ideas]]. The goal is to transition from merely using AI coding to becoming an "AI coder" [00:05:15].

> [!abstract] The Challenge with AI-based Coding
> Large Language Model (LLM)-based coding is currently one of the hardest topics to master, with many tutorials suggesting that users can simply prompt an AI to build an entire application [00:00:36]. In reality, the results are often unpredictable, leading to errors due to the LLM's tendency to "hallucinate" [00:00:53].

## Workflow for Consistent AI Coding

The presented workflow focuses on a consistent readout for [[building_apps_with_ai_tools | AI coding]] [00:01:16].

### 1. Writing Clear and Detailed Specifications
Spending significant upfront time to write clear and detailed specifications (specs) is crucial [00:01:30]. This approach simulates how a product team normally functions, with a Product Manager (PM) writing core functionality specs and an Engineering Manager (EM) detailing individual tickets or architecture [00:01:56]. This process helps uncover uncertainties early on [00:02:23].

### 2. Defining Roles for Different Platforms
It is important to be clear about when to use different AI tools [00:02:37]:
*   **Cursor:** Focus on building core functionality without initially considering the User Interface (UI) [00:02:49].
*   **V0:** Use V0 to refine and touch up the UI interface after the functionality is built [00:02:57]. This approach leads to more success than trying to achieve everything at once [00:03:00]. This order is contrary to what many people typically do, who might start with V0 for wireframes [00:04:29].

### 3. Reusable Modular Prompts
The concept of reusable modular prompts is key for efficiency [00:03:10]. While Cursor's directory for sharing rules hasn't proven very useful [00:03:19], standard features like user sign-in/authentication or payment systems are often similar across different [[building a startup using AI tools | startup ideas]] [00:03:41]. A community-driven collection of such modular prompts could allow users to generate entire functionalities by simply providing them to Cursor [00:03:50].

## Case Study: Building a Reddit Analytics Platform

To illustrate the workflow, an example of building a Reddit analytics platform (similar to "Gumy Search") is used [00:07:31]. This application utilizes LLMs to structure insights from unstructured data at scale [00:07:51].

### Initial Project Setup
1.  **Initialize with GitHub:** Start with GitHub for better version control [00:08:45].
2.  **Open in Cursor:** Open the project in Cursor [00:08:51].

### Drafting the Spec (Draft.md)
Instead of immediately prompting Cursor to build the platform, begin with a draft spec [00:09:02]. A common structure includes:
*   **Project Overview:** A simple overview of the project's goal [00:11:19]. For the Reddit analytics platform, the goal is to build a platform where users can get analytics of different subreddits, seeing top content and category breakdowns [00:11:26].
*   **Core Functionality:** Define must-have features [00:11:43]. For this project, these include:
    *   Displaying a list of available subreddits and adding new ones [00:11:57].
    *   Building a subreddit page with two tabs: "Top Posts" and "Analysis" [00:12:02].
    *   Fetching Reddit post data and categorizing it into themes [00:12:15].
*   **Proof-of-Concept Documentation:** Include specific documentation for implementing key features [00:13:54]. This helps to ensure core functionality is clearly defined early on [00:09:55].
    *   **Reddit Data Fetching:** Research packages (e.g., `snoowrap` for Reddit data) and generate a simple TypeScript script to fetch subreddit posts from the past 24 hours, including title, link, content, score, and comments [00:13:01]. This step involves handling credentials via `.env` files and debugging initial errors [00:15:25].
    *   **OpenAI Structured Output:** Generate a script using OpenAI's structured output to categorize subreddit posts based on predefined categories (e.g., "tools and solutions," "pain and anger," "advice request," "money talk") [00:20:02]. It's crucial to ensure the prompt is generic and not tied to specific JSON output structures for future maintainability [00:25:52].
*   **Current File Structure:** Include the current file structure using a tool like `tree` to help Cursor understand where to create files, preventing errors [00:10:02].
*   **Additional Requirements:** Add common prompts for specific project types (e.g., web apps, iOS apps) to address frequent omissions or errors by Cursor (e.g., `use client`, environment variables, error handling) [00:10:20].

### Refining the Spec with a Stronger Model (01 Model)
Use a stronger model like 01 (or another advanced LLM) to act as an "engineer manager," filling in the details of the draft spec [00:35:38]. This involves:
1.  **Generating File Structure:** Prompting the 01 model with the existing draft to propose a final project structure and identify dependencies [00:36:12]. This helps to align on the project architecture early [00:37:12].
2.  **Detailed PRD Generation:** Ask the 01 model to add all original PRD (Product Requirements Document) details, including file structure and documentation, without generating actual code [00:37:29]. This results in a highly detailed PRD that engineers (or Cursor) can follow with less ambiguity [00:38:05].

### Step-by-Step Building with Cursor
With the detailed PRD, use Cursor Composer to build the application step-by-step [00:39:03].
1.  **Commit Project Setup:** Commit the initial project setup [00:39:05].
2.  **Implement Functionality Incrementally:** Address one core functionality at a time, strictly based on the detailed instructions [00:39:37]. For example, first implement the display of available subreddits, then the subreddit page structure, and finally the data fetching and categorization [00:39:52]. This reduces errors and prevents the AI from skipping steps [00:40:47].
3.  **Debug Iteratively:** When errors occur, use commands like "help me debug" or "help me fix it" [00:42:35]. For more complex issues, prompting with "let's think step by step" can help the AI break down the problem (a "chain of thought" technique) [00:29:47].

### UI Refinement with V0
Once the core functionality is built, use V0 to improve the UI [00:46:02].
1.  **Copy Code to V0:** Paste the relevant code (e.g., homepage component) into V0 [00:46:17].
2.  **Prompt for UI Improvement:** Ask V0 to "make the UI a ton better," providing specific style preferences (e.g., "black and white," "dark mode," "similar to Vercel") [00:46:34]. This approach is more predictable because the functionality is already in place [00:46:13].
3.  **Iterate on Components:** Continue refining component by component within V0 [00:49:10].

## Reusable Modular Prompts in Practice
The concept of reusable modular prompts significantly speeds up development [00:52:01]. For instance, a standardized prompt for user authentication (sign-in/sign-up) can be applied to different projects because the functionality is largely the same [00:52:27]. By having a collection of such prompts for standard features like authentication or payment systems, developers can integrate complex functionalities more quickly [00:54:59].

## Conclusion

This structured workflow significantly improves the success rate of [[building_a_startup_using_ai_tools | building a startup using AI tools]] [00:07:17] and [[building_successful_ai_apps | building successful AI apps]] [00:03:05]. It focuses on:
*   Spending extensive upfront time on detailed specs to minimize uncertainty [00:56:05].
*   Prioritizing functionality development with Cursor before UI refinement with V0 [00:56:14].
*   [[using_ai_for_creating_steps_in_startup_projects | Using AI for creating steps in startup projects]] in a structured, iterative manner.
*   Aggregating and sharing reusable modular prompts to accelerate the development process [00:56:17].

This approach transforms [[leveraging_ai_in_startup_development | leveraging AI in startup development]] into a more structured, predictable process, akin to using an electric-assisted bicycle that provides a boost while still requiring effort [00:57:37].

For more on [[building_apps_with_ai_tools | building apps with AI tools]], explore AI Jason's YouTube channel for interesting AI experiments and tutorials [00:58:11].