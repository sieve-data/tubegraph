---
title: Debugging and problemsolving strategies with AI coding
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

AI-powered coding, while powerful, presents significant challenges, particularly its unpredictable results and propensity for "hallucinations" leading to errors [00:00:51 | 00:00:58]. Unlike polished tutorials, real-world [[challenges_in_coding_with_ai | AI coding]] often involves encountering many errors [00:01:01 | 00:01:06]. A key goal is to develop a workflow that yields more consistent results [00:01:16].

## Core Problemsolving Strategies

To achieve more consistent and predictable outcomes in [[ai_coding_workflow_and_fundamentals | AI coding]], several strategies can be employed:

### 1. Upfront Planning and Detailed Specifications
Spending significant time upfront writing clear and detailed specifications is crucial for reducing uncertainty [00:01:30 | 00:02:26]. This process simulates how a product team works, with a product manager defining core functionality and an engineering manager detailing tickets or architecture [00:01:56 | 00:02:11]. This structured approach reduces ambiguity and leads to a more consistent output [00:02:11 | 00:02:32].

> "You start really getting uncover a lot of uncertainty upfront and taking out the planning work a f cursor um a lot to get a more consistent result" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

A detailed specification (Product Requirements Document - PRD) should include:
*   **Project Overview**: A simple description of the goal [00:11:19 | 00:11:39].
*   **Core Functionality**: Main features required [00:11:43 | 00:12:45].
*   **Documentation for Key Features (Proof-of-Concept)**:
    *   Building proof-of-concept for core functionalities, such as figuring out which package to use or how to implement specific features [00:12:51 | 00:13:09].
    *   This helps identify and address errors early on, rather than having them appear later in the process [00:17:19 | 00:17:26].
    *   Use external tools like ChatGPT to research packages [00:13:28 | 00:13:51].
    *   Test isolated scripts to ensure they work before integrating them into the main application [00:17:01 | 00:17:19].
*   **Current File Structure**: Communicating the existing file structure to the AI (e.g., using the `tree` command) helps it know where to create and modify files, preventing wrong placements or dependencies [00:10:02 | 00:10:18 | 00:34:06 | 00:35:15].
*   **Additional Requirements**: Specific instructions for the AI based on the project type (e.g., web app, iOS app) to ensure common pitfalls are avoided (e.g., `use client`, environment variables, error handling) [00:10:20 | 00:11:15].

Using a stronger AI model like `01` can help fill in gaps in the spec, acting as an "engineer manager" to add details, architectural plans, and identify dependencies [00:35:38 | 00:37:23].

### 2. Iterative Development and Step-by-Step Implementation
Instead of attempting to build the entire application at once (one-shotting), break down the development into smaller, manageable tasks [00:39:43 | 00:41:01]. This reduces the likelihood of errors and allows for more focused debugging [00:40:47 | 00:40:57]. Implement and test one part of the functionality before moving to the next [00:40:42 | 00:40:48].

### 3. Debugging AI-Generated Code

When errors occur:
*   **"Help me debug" / "Help me fix it"**: Start with general prompts like `help me debug` or `help me fix it` [00:17:33 | 00:17:36].
*   **"Let's think step by step" (Chain of Thought Prompting)**: For more complex issues, prompting the AI to "think step by step" can be highly effective [00:18:11 | 00:29:36]. This technique, also known as [[ais_role_in_problemsolving | Chain of Thought prompting]], encourages the model to break down the problem into smaller, sequential steps, leading to more accurate solutions [00:29:47 | 00:30:28].
*   **Add Debug Info**: When errors are not clearly communicated by the AI, explicitly ask it to add debug information to the code. This provides a clearer way to communicate specific errors back to the AI for more accurate fixes [00:42:35 | 00:42:56].
*   **Reference Documentation and Examples**: If the AI makes a mistake (e.g., ignoring documentation or using an old model), explicitly reference the correct code examples or documentation within your prompt [00:24:40 | 00:25:13 | 00:41:41 | 00:42:02].
*   **Review Changes**: Utilize features like "checkout" in tools like Cursor to review AI-generated changes more carefully, allowing for better identification of incorrect modifications [00:28:13 | 00:28:20].
*   **Anticipate Common Errors**: Be aware of common mistakes AI models make, such as using outdated documentation or selecting the wrong model for specific tasks (e.g., GPT-4 lacking support for structured output initially) [00:20:08 | 00:24:32 | 00:45:05 | 00:45:21].

### 4. Role Specialization of AI Tools
Be clear about the role of different platforms and tools in your workflow [00:02:37]. For example:
*   **Cursor**: Focus on core functionality and code generation first, postponing UI considerations [00:02:49 | 00:02:54].
*   **V0**: Used for refining the user interface (UI) *after* the core functionality is built [00:02:55 | 00:03:00]. This is often counter-intuitive to how people usually approach [[improving_ai_designs_and_interfaces | UI interface]] design with AI [00:04:25 | 00:04:32]. Building functionality first makes UI refinement more predictable because the underlying logic is stable [00:46:08 | 00:46:15].

### 5. Reusable Modular Prompts
Develop and utilize reusable modular prompts for standard features like user authentication or payment systems [00:03:08 | 00:03:52]. These prompts can be shared within a community, significantly accelerating development as they generate entire functionalities consistently [00:03:47 | 00:04:06 | 00:52:01 | 00:52:30]. This addresses the challenge of maintaining code when everything is embedded directly in prompts, making updates difficult [00:26:22 | 00:26:29]. This approach is an example of [[testing_and_optimizing_ai_models_for_agent_tasks | Testing and Optimizing AI Models for Agent Tasks]] by standardizing inputs for common patterns.

> "If we have a collection of this type of standard feature prompt... this going to be extremely useful" <a class="yt-timestamp" data-t="00:55:14">[00:55:14]</a>

## Conclusion
While AI coding may appear simple in tutorials, becoming an [[ai_coding_workflow_and_fundamentals | AI coder]] requires a structured, deliberate approach [00:05:00 | 00:05:19]. By embracing detailed planning, iterative development, and strategic debugging, developers can significantly improve the success rate and consistency of AI-generated code [00:17:17 | 00:17:22 | 00:55:57 | 00:56:22]. This process is akin to an electric-assisted bicycle: it provides a significant boost, but still requires the user to pedal and guide the direction [00:57:37 | 00:57:49].