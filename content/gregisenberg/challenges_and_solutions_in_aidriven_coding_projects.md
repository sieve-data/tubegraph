---
title: Challenges and solutions in AIdriven coding projects
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing with AI-driven coding tools presents unique [[challenges_and_opportunities_for_ai_integration | challenges]], particularly in achieving predictable and consistent results [00:00:31]. While online tutorials often depict a seamless process where AI can build an entire application from a simple prompt [00:00:44], the reality is often less straightforward [00:00:48].

## Core Challenges in AI-Driven Coding

One of the primary difficulties in large language model-based [[ai_coding_workflow_optimization | AI coding]] is the unpredictable nature of the output [00:00:53]. Large language models can "hallucinate," leading to a series of errors rather than smooth execution [00:01:00]. This unpredictability makes it difficult to achieve the "smooth sailing" often seen in edited tutorials [00:01:06]. Debugging these errors can also be frustrating, especially when the AI provides limited information, making it hard to communicate the exact problem back to the model [00:42:20].

Another challenge is the general lack of detailed guidance on how to write effective specifications for AI [00:01:47]. While many acknowledge the importance of upfront planning, specific steps for creating a spec that communicates well with AI are often missing [00:01:49]. Furthermore, AI models, like Cursor, can struggle with understanding the existing file structure, leading to files being created in incorrect locations or with wrong dependencies, increasing uncertainty in the process [00:10:07].

## Workflow Optimization for AI-Driven Coding

To achieve more consistent and predictable results in [[ai_coding_workflow_optimization | AI coding]], a structured workflow is crucial [00:01:16]. This workflow simulates how product and engineering teams collaborate in traditional development, reducing ambiguity [00:01:56].

### 1. Write Clear and Detailed Specifications

The most critical step is to invest significant time upfront in writing very clear and detailed specifications (specs) [00:01:30]. This process uncovers uncertainties early on, making the planning work more focused and leading to a more consistent output [00:02:23].

*   **Structure the Spec**: A typical spec includes a project overview, breaking down core functionalities, and crucial implementation details [00:09:14].
*   **Include Proof-of-Concept Docs**: Integrate documentation that includes proof-of-concept code examples for key features [00:09:37]. This helps ensure the AI understands the core functionality before full implementation [00:09:55]. For instance, demonstrating how to fetch Reddit data using a specific package (e.g., Snowrap) and how to use OpenAI's structured output for categorization can serve as clear examples [00:12:51].
*   **Provide Current File Structure**: Communicating the current file structure to the AI is vital to prevent misplacement of files and incorrect dependencies [00:10:02]. Tools like `tree` can be used to generate this structure [00:34:16].
*   **Add Additional Requirements**: Include common pitfalls or specific requirements for the project type (e.g., using `use client` in web apps, environment variables, error handling) [00:10:20].
*   **Leverage Stronger Models for PRD Details**: Initially, a draft spec can be created. Then, a more powerful model like `01` can be used to act as an "engineer manager" to fill in the detailed Product Requirements Document (PRD), including project architecture, dependencies, and detailed variable definitions [00:35:38]. This detailed PRD significantly reduces ambiguity for the AI, similar to how it benefits human engineers [00:37:44].

### 2. Define Clear Roles for Different Platforms

Different [[comparison_of_ai_coding_tools | AI coding tools]] have strengths. The speaker recommends a specific order for their use [00:02:37]:

*   **Cursor First for Functionality**: Focus Cursor solely on building the core functionality of the application [00:02:49].
*   **Vercel v0 Second for UI**: Once the core logic is in place, use Vercel v0 to refine and enhance the User Interface (UI) [00:02:55]. This approach avoids trying to tackle everything at once, leading to greater success [00:03:00]. It's advised to keep the UI simple initially, focusing on the underlying code [00:40:19].

### 3. Utilize Reusable Modular Prompts

A key strategy is to develop and use reusable, modular prompts for standard functionalities [00:03:08]. Features like user authentication (user "auth") and payment systems are largely the same across many projects [00:03:41].

*   **Community Collection**: The vision is for a community-shared collection of these modular prompts that can be fed to AI tools like Cursor to generate entire functionalities [00:03:49].
*   **Standardized Setup**: These prompts can include predefined documentation for common setups, like authentication flows [00:52:35].
*   **Step-by-Step Implementation**: Even with modular prompts, it's beneficial to break down the implementation into smaller, sequential steps (e.g., "build step three, then step four") to ensure consistency and reduce errors [00:54:08].

## Practical Application: Building a Reddit Analytics Platform

The proposed workflow was demonstrated by building a Reddit analytics platform [00:06:17].

*   **Project Goal**: To create a platform where users can analyze different subreddits, view top content, and categorize posts [00:11:22].
*   **Proof-of-Concept for API and AI**:
    *   Identified `snowrap` for fetching Reddit data and tested a TypeScript script to gather post titles, links, content, and comments, ensuring it used `.env` for credentials [00:13:01]. Initial debugging was performed to resolve errors, often by asking the AI to "help me debug" or "help me fix this, let's think step by step" [00:17:19].
    *   Used OpenAI's structured output to categorize subreddit posts based on predefined categories (e.g., "tools and solutions," "pain and anger," "advice request," "money talk") [00:20:02]. This also required iterative prompting to correct the AI's initial use of old models and incorrect output structures [00:24:43].
*   **Project Setup**: Initiated a Next.js project using `shadcn/ui` for UI components, as it provides a clean and well-covered library often integrated by default with Vercel v0 [00:32:29].
*   **Iterative Development with Cursor**: Once the detailed spec and initial file structure were established, Cursor was used to build the application section by section, starting with listing available subreddits, then creating the subreddit page with tabs for top posts and analysis, and finally integrating the data fetching and categorization [00:39:19]. This step-by-step approach significantly reduces the chance of errors [00:40:47].
*   **UI Refinement with Vercel v0**: After the core functionality was working, Vercel v0 was used to improve the UI, with specific prompts to ensure desired aesthetics (e.g., "black and white," "dark mode," "similar to Vercel") [00:46:02].
*   **Modular Prompt for Authentication**: A pre-prepared modular prompt for user authentication was integrated, demonstrating how standard features can be quickly added to new projects [00:52:01].

## Conclusion

This structured approach transforms [[ai_coding_workflow_optimization | AI coding]] from an unpredictable, error-prone endeavor into a more reliable and efficient development process [00:56:01]. By prioritizing upfront planning, detailed specifications, strategic tool utilization, and the development of reusable components, developers can significantly improve the success rate of their AI-driven coding projects [00:56:05]. While it requires a more structured approach than simply "one-shotting" an app with a single prompt, it makes the transition from a casual AI user to an effective [[ai_coding_workflow_optimization | AI coder]] much more feasible [00:54:54]. The comparison to an electric-assisted bicycle highlights that AI provides a significant boost, but developers still need to "pedal the wheels" through careful planning and iteration [00:57:41].