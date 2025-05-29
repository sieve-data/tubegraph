---
title: Creating and using reusable modular AI prompts
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Achieving predictable results in [[introduction_to_ai_prompting_and_reasoning_models | AI prompting]] for coding can be challenging due to the tendency of large language models (LLMs) to "hallucinate" or produce unexpected errors [00:00:34]. A structured workflow, focusing on reusable modular prompts, can significantly improve consistency and reduce development time [00:01:12].

## The Workflow for Consistent AI Coding

The core idea is to simulate a product team's development process, where detailed specifications and modular components lead to predictable outcomes [00:01:56]. This involves three main pillars:

1.  **Writing Clear and Detailed Specifications (Specs)**: Spend significant time upfront on comprehensive planning [00:01:30].
2.  **Defining Clear Roles for Different Platforms**: Use tools strategically based on their strengths [00:02:35].
3.  **Developing Reusable Modular Prompts**: Standardize common functionalities for quick integration [00:03:08].

### 1. Writing Clear and Detailed Specs

This is crucial for effective AI coding, moving beyond simple one-shot prompts that often lead to unpredictable errors [00:00:44]. The process should mirror a product team's workflow:

*   **Project Overview and Core Functionality**: Start by defining the project's goal and its essential features, similar to a product manager's role [00:02:00]. This provides a clear high-level understanding [00:11:19].
*   **Proof-of-Concept (POC) and Documentation**:
    *   Research and identify necessary packages or APIs [00:13:21].
    *   Build small POC scripts for core functionalities to ensure they work. For example, fetching data from an external API or using [[function_and_tool_calling_in_ai_apps | structured output]] from an LLM [00:12:57]. This early testing helps uncover errors that would otherwise appear much later [00:17:19].
    *   Include the working code examples and their expected responses directly in the spec document [00:19:32].
*   **Current File Structure and Additional Requirements**:
    *   Provide the AI with the existing file structure of the project [00:10:02]. This helps prevent the AI from creating files in the wrong place or with incorrect dependencies [00:10:07].
    *   Add "additional requirements" specific to the project type (e.g., web app, mobile app) that the AI might commonly miss, such as `use client` directives, environment variables, or error handling [00:10:20].
*   **Refining Specs with Stronger Models**: Use advanced LLMs (like GPT-4) to act as an "engineer manager" to elaborate on the initial product requirements document (PRD) [00:35:38]. This helps fill in details, define file structures, and propose components, leaving less ambiguity for the AI to interpret [00:37:26].

### 2. Defining Clear Roles for Different Platforms

Choosing the right tool for the right task is vital:

*   **Cursor for Functionality**: Focus on using Cursor (or similar coding AI) to build the core logic and functionality of the application [00:02:49].
*   **Vercel's V0 for User Interface (UI)**: Once the functionality is established and robust, use V0 to refine and improve the UI [00:02:57]. Attempting to do both simultaneously can lead to less predictable results [00:03:00]. When prompting V0, provide specific style references (e.g., "similar to Vercel") rather than vague instructions like "make it look better" [00:46:41].

### 3. Developing Reusable Modular Prompts

Instead of constantly reinventing the wheel, identify common features that are standard across many projects and create reusable prompts for them [00:03:37].

*   **Standard Features**: Functionalities like user authentication (e.g., user sign-in/sign-up, OAuth) or payment systems are largely the same across different applications [00:03:44].
*   **Community Aggregation**: A community-driven collection of these modular prompts could be extremely useful, allowing developers to quickly integrate standard features by simply providing the pre-defined prompt to their coding AI [00:03:47].
*   **Step-by-Step Implementation**: Even with modular prompts, it's beneficial to break down the implementation into smaller, sequential steps, avoiding "one-shot" attempts that can lead to more errors [00:40:47]. This aligns with the concept of [[sequential_prompting_in_ai_workflows | chain-of-thought prompting]], where the AI breaks down a complex problem into smaller, manageable steps, leading to better results [00:29:47].

## Building an Application with the Workflow (Example: Reddit Analytics Platform)

An example application like a Reddit analytics platform can illustrate this workflow [00:06:14].

1.  **Project Setup**: Initialize with a version control system like GitHub and open the project in Cursor [00:08:45].
2.  **Initial Spec Draft**: Create an `instructions.md` file with a project overview and core functionalities (e.g., listing subreddits, adding new subreddits, displaying top posts, categorizing posts) [00:09:07].
3.  **Proof-of-Concept Code**:
    *   For Reddit data fetching, research packages (e.g., SnowWrap) and create a simple TypeScript script to test credentials and data retrieval [00:13:01]. Debugging is an iterative process, where errors are fixed step-by-step [00:17:19].
    *   For [[function_and_tool_calling_in_ai_apps | AI-powered categorization]], build a script using OpenAI's [[function_and_tool_calling_in_ai_apps | structured output]] feature. Address common issues like using outdated documentation or models [00:20:02].
    *   Once working, include these POC code examples and expected responses in the `instructions.md` [00:19:19].
4.  **Detailed Spec Generation**:
    *   Generate the project's file structure (e.g., using `tree -L 2`) and include it in the spec [00:34:16].
    *   Feed the initial `instructions.md` to a powerful LLM (like GPT-4) and prompt it to act as an "engineer manager," filling in detailed architectural plans and dependencies for the project [00:35:40]. This detailed PRD makes the subsequent coding process much smoother for the AI [00:37:44].
5.  **Iterative AI-Assisted Coding**:
    *   Commit the project setup [00:39:05].
    *   Provide the comprehensive `instructions.md` to Cursor and ask it to implement the core functionalities *one by one*, rather than attempting a single, large prompt [00:39:21]. This structured approach significantly reduces errors [00:40:47].
    *   Run the application after each step (`npm run dev`) and debug errors by providing the error messages back to Cursor, sometimes asking it to "think step by step" to encourage [[sequential_prompting_in_ai_workflows | chain-of-thought reasoning]] [00:42:27].
6.  **UI Refinement with V0**: After core functionality is complete, use V0 to improve the user interface component by component, providing specific design instructions [00:46:02].

## The Future of Reusable Prompts

The ability to share and aggregate these modular, reusable prompts across a community could revolutionize [[building_applications_using_ai_with_replit | AI-assisted development]] [00:51:14]. This would allow for rapid assembly of complex applications by leveraging pre-tested, standard feature prompts [00:55:12]. While tools like Cursor already offer some "rules" or directories, these modular prompts go deeper into providing working code examples and refined instructions [00:03:16]. This approach turns AI coding into an "electric-assisted bicycle" – it still requires effort, but provides a significant boost [00:57:41].

This structured methodology represents a significant shift from simply "using AI coding" to becoming an "AI coder" [00:05:10]. It's a more disciplined, but ultimately more effective, way to leverage AI for software development.