---
title: AI coding workflow and challenges
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

While online tutorials often suggest that [[aipowered_workflow_and_task_management | AI coding]] can simply involve prompting an AI to build an entire application, the reality is that the results are often unpredictable due to the [[the_role_of_ai_in_designing_and_generating_productionready_code | AI's tendency to hallucinate]] and produce errors [00:00:40]. To achieve more consistent and predictable outcomes in [[aipowered_workflow_and_task_management | AI-based coding]], a structured workflow is recommended [00:01:16].

## Recommended Workflow for Consistent AI Coding

The following principles can significantly improve the success rate of [[aipowered_workflow_and_task_management | AI coding]]:

### 1. Write Clear and Detailed Specifications (Specs) Upfront
Spending considerable time writing very clear and detailed specifications is the first and most important step [00:01:30]. This process should simulate how a product team normally functions, with a Product Manager (PM) defining core functionalities and an Engineering Manager (EM) detailing individual tasks and architecture [00:01:56]. This approach uncovers uncertainties early in the planning phase, leading to more consistent results [00:02:23].

Key elements for detailed specs include:
*   **Project Overview** A simple summary of the project's goal [00:11:19].
*   **Core Functionalities** A breakdown of essential features, allowing for some initial openness without excessive detail [00:11:43].
*   **Key Feature Implementations Documentation** Include documentation or "proof of concept" code for critical features to ensure core functionality is clearly outlined [00:09:37].
*   **Current File Structure** Provide the AI with the existing file structure to prevent it from creating files in incorrect locations or with wrong dependencies [00:10:00].
*   **Additional Requirements** Specific instructions for the type of project (e.g., using `use client` for web apps, environment variables, error handling) that AI tools might commonly miss [00:10:20].

### 2. Clearly Define the Role of Different Platforms
It's crucial to understand when to use specific [[pros_and_cons_of_different_ai_coding_tools | AI coding tools]] [00:02:37]. A recommended strategy is to:
*   **Use Cursor First for Functionality**: Focus on building the core functionality without considering the User Interface (UI) initially [00:02:49].
*   **Use V0 Second for UI/UX Refinement**: Once the functionality is established, use V0 to refine and enhance the UI interface [00:02:57]. This approach leads to more success than trying to build everything at once [00:03:00].

### 3. Leverage Reusable Modular Prompts
Standard features like user authentication or payment systems are often similar across different projects [00:03:37]. Creating and sharing a collection of reusable, modular prompts for these standard functionalities can significantly speed up the development process [00:03:50]. This is more effective than relying on general "cursor rules," which are often not as useful [00:03:27].

## Case Study: Building a Reddit Analytics Platform

A demonstration of this workflow involves building a Reddit analytics platform, inspired by Gumy Search [00:07:32]. The platform aims to structure insights from unstructured Reddit data at scale, categorized into themes like "tools and solutions," "pain and anger," "advice requests," and "money talk" [00:07:59].

### Initial Setup and Spec Drafting
1.  **Repository Setup**: Start with a GitHub repository for version control, then open it in Cursor [00:08:45].
2.  **Drafting the Spec**: Begin with a draft specification following the recommended structure:
    *   **Project Overview**: "You are building a Reddit analytics platform where users can get analytics of different subreddits, where they can see top content and see the category approval" [00:11:26].
    *   **Core Functionality**:
        *   See a list of available subreddits and add new ones [00:11:57].
        *   Build a subreddit page with two tabs: "Top Posts" and "Analysis" [00:12:02].
        *   Fetch Reddit post data and perform analysis, categorizing them into different themes [00:12:15].

### Proof of Concept (POC) for Core Functionalities
Before full development, build POCs for key functionalities to ensure they work as expected.
1.  **Fetching Reddit Data**:
    *   **Research**: Use tools like ChatGPT to identify suitable packages (e.g., SnowWrap) for fetching Reddit data in a Next.js project [00:13:21].
    *   **Code Example**: Go to NPM, review examples for the chosen package, and draft a simple TypeScript script using Cursor [00:14:05]. The prompt would include details like fetching posts from the past 24 hours, specifying data points (title, link, content, score, comments), and using `.env` for credentials [00:14:46].
    *   **Credential Setup**: Create a Reddit app (via Reddit's preferences/apps page) to obtain client ID and secret, saving them in a `.env` file [00:15:41].
    *   **Testing and Debugging**: Run the script using `npx TS node` [00:17:07]. If errors occur, use prompts like "help me debug" or "let's think step by step" to guide Cursor [00:17:33].
    *   **Documenting the POC**: Once validated, paste the working code example into the specification document under "Documentation for how to fetch Reddit posts using SnowWrap" [00:19:19].

2.  **Categorizing Posts with OpenAI Structured Output**:
    *   **Prompting**: Ask Cursor to build a TypeScript script using OpenAI's structured output to categorize subreddit posts based on predefined categories (e.g., "tools and solutions," "pain and anger," "advice requests," "money talk") [00:20:21]. Specify the desired JSON output format [00:21:40].
    *   **Refinement**: If the initial output uses outdated models or doesn't follow the structured output as intended, provide more specific instructions, including code examples from OpenAI's documentation. Direct it to use `users.package` for data structure, GPT-4o model, move category descriptions to the model description, and make the prompt generic to avoid tying it to specific categories [00:24:40]. This demonstrates thinking about future maintainability [00:26:07].
    *   **Testing and Debugging**: Similar to Reddit data fetching, test and debug the script. If errors persist, try adding debug information or using the "let's think step by step" prompt [00:27:17].
    *   **Documenting the POC**: Add the working code and expected response to the specification document [00:31:32].

### Project Structuring and PRD Generation with GPT-4o
1.  **Initial Project Setup**: Use a framework like Shadcn UI for component libraries [00:32:30]. This provides clean, good coverage for UI components [00:32:43].
2.  **File Structure Communication**: Use a package like `tree` to generate a file structure that Cursor can reference, helping it place files correctly [00:34:06].
3.  **Detailed PRD Generation**: Use a more powerful model like GPT-4o to act as an "engineer manager" to fill in missing details and structure the project further [00:35:40]. Provide the draft spec and ask it to propose a final file structure and identify dependencies [00:36:19]. Then, prompt it to add all the details from the original PRD, ensuring it defines functionalities, variables, file structures, and additional requirements in granular detail [00:37:29]. This significantly reduces ambiguity for the engineering process [00:38:31].

### Step-by-Step Development with Cursor
Once the detailed PRD is complete, use Cursor to build the application piece by piece.
1.  **Commit Project Setup**: Commit the initial project setup [00:39:05].
2.  **Phased Implementation**: Instruct Cursor to implement one section of the PRD at a time, for example, "Let's build number one first" [00:39:37]. This breaks down tasks into smaller, manageable chunks, reducing the likelihood of errors and making debugging easier [00:40:43].
3.  **Iterative Building**: Continue this process for each defined core functionality (e.g., "Now let's do the second part," "Now let's do the third step, make sure you refer to the documentation at the bottom") [00:40:39].

### UI/UX Refinement with V0
Once the core functionality is built, use V0 to refine the UI.
1.  **Transfer Code**: Paste the relevant code (e.g., from the homepage component) into V0 [00:46:17].
2.  **Prompt for UI Improvements**: Instruct V0 to "keep the functionality exactly like above but make the UI a ton better," optionally adding preferred styles like "black and white" or "dark mode" or referencing existing designs (e.g., "similar to Vercel") [00:46:31].
3.  **Iterative Design**: Continue this component by component, using V0 to update UI elements based on the existing code structure [00:49:08]. This makes UI design more predictable and less error-prone because the underlying functionality is stable [00:46:10].

### Reusable Prompts for Standard Features
For common features across projects, such as user authentication, reusable prompts can be invaluable [00:52:01].
1.  **Prepare a Modular Prompt**: Create a detailed markdown document (e.g., `setup_auth.md`) outlining the steps for implementing authentication [00:52:35].
2.  **Integrate**: Paste the credential and then use Cursor to build the authentication functionality, instructing it to strictly follow the modular prompt [00:53:05]. Break down the implementation into steps (e.g., "build step three and step four") to ensure a structured approach [00:53:51].
3.  **Community Sharing**: The speaker expresses hope for a community aggregator of such modular prompts for features like payment systems, which could be integrated into developer tools [00:55:14].

## Challenges and Best Practices

*   **Unpredictable Results**: Large Language Models (LLMs) can "hallucinate" and produce errors, especially when trying to build an entire application from a single prompt [00:00:51].
*   **Debugging**: Errors are common, and getting the AI to debug effectively requires specific prompts like "help me debug" or "let's think step by step" to encourage a "chain of thought" process [00:17:33]. Directly communicating complex errors to Cursor can be challenging without additional debug info [00:42:20].
*   **Old Documentation**: AI models sometimes rely on outdated documentation, requiring explicit guidance and current code examples [00:20:07].
*   **Maintaining Consistency**: Without proper planning and detailed specs, the AI might produce code that is hard to maintain or modify later [00:26:22].
*   **Over-reliance on One-Shotting**: Attempting to build a complete app with a single prompt often leads to numerous errors and a longer debugging process [00:41:01].

In conclusion, while [[aipowered_workflow_and_task_management | AI coding]] can seem challenging, adopting a structured approach, akin to an [[ai_transformation_agencies | AI transformation agency]], involving detailed planning, phased development, and strategic use of [[pros_and_cons_of_different_ai_coding_tools | AI coding tools]], can significantly enhance productivity and produce more robust applications [00:56:01]. This systematic workflow transforms the process from simply "using AI coding" to becoming an "AI coder" [00:51:19]. The process is like an electric-assisted bicycle; it still requires effort but provides a significant boost [00:57:37].