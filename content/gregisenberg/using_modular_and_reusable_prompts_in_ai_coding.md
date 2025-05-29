---
title: Using modular and reusable prompts in AI coding
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Achieving predictable and consistent results in large language model-based coding is a significant challenge, often touted as the hardest topic in AI development <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. While tutorials might suggest that one can simply prompt an AI to build an entire application, the reality is often unpredictable, leading to numerous errors due to the AI's tendency to "hallucinate" <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. To counter this, a structured workflow focusing on meticulous planning and [[sequential_prompting_for_ai_workflows | sequential prompting]] can lead to more consistent outcomes <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Core Principles for Consistent AI Coding

The workflow for AI coding emphasizes three main aspects to ensure more reliable results:

### 1. Clear and Detailed Specifications
Spending significant upfront time to write very clear and detailed specifications is crucial <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. This process simulates how a product team normally works, with product managers writing core functionality specs and engineering managers detailing individual tickets and architecture <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This approach uncovers uncertainties early and leads to a more consistent output <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

Key elements of a detailed spec include:
*   **Project Overview** Defines the goal and scope of the project <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.
*   **Core Functionality Breakdown** Lists essential features, similar to a product manager's outline <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
*   **Proof-of-Concept Documentation** Includes "docs" on how to implement key features, addressing common AI failures when integrating documentation directly <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This involves building small, testable scripts for core functionalities upfront <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   **Current File Structure** Provides the AI with context about the project's organization to prevent files from being created in incorrect locations or with wrong dependencies <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.
*   **Additional Requirements** Specifies common pitfalls for certain project types (e.g., web apps needing `use client` directives, environment variables, error handling) <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.

### 2. Delineating Roles of Different Platforms
It's important to be clear about when to use different AI coding tools <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. A recommended approach is to:
*   **Cursor First for Functionality** Focus on building the core functionality without considering the UI initially <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
*   **Vercel v0 Second for UI** Once functionality is stable, use Vercel v0 to refine and touch up the user interface <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. This prevents trying to build everything at once, which often leads to less success <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### 3. Modular and Reusable Prompts
A key strategy involves creating [[prompting_techniques_for_effective_use_of_ai_models | reusable modular prompts]] for common features <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. While "Cursor rules" exist, they often don't deliver significant benefits <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. The true value lies in identifying standard functionalities, like user authentication or payment systems, and creating prompts that can be given to the AI to generate the entire feature <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. This reduces the need to rebuild these common parts for every new project <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

There is a desire for a community-shared collection or aggregator of such modular prompts to further accelerate development <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

## Case Study: Building a Reddit Analytics Platform

To demonstrate this workflow, a Reddit Analytics Platform is built, which involves gathering structured insights from unstructured data at scale <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

### Initial Setup and Detailed Spec
1.  **Repository Setup:** Start by creating a new GitHub repository for better version control, then open it in Cursor <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.
2.  **Drafting the Spec:** Create a draft `spec.md` file with a project overview, core functionalities (e.g., listing subreddits, adding new ones, displaying top posts and analyses, fetching data), and initial thoughts <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.

### Building Proof of Concepts (POCs)
Before full implementation, build small POCs for core functionalities.
1.  **Reddit Data Fetching:**
    *   Research a suitable package (e.g., `snoowrap` via ChatGPT) <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>.
    *   Obtain necessary API credentials (e.g., from Reddit `perf/apps`) <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>.
    *   Use Cursor's composer to write a TypeScript script to fetch subreddit posts, specifying required data points and credential handling (e.g., `.env` file) <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.
    *   Debug early and iteratively using prompts like "help me debug" or "let's think step by step" to ensure the script works as intended <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>.
    *   Once validated, include the working code example in the main documentation <a class="yt-timestamp" data-t="19:17:00">[19:19:00]</a>.

2.  **OpenAI Structured Output for Categorization:**
    *   Use OpenAI's structured output functionality to categorize Reddit posts <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>.
    *   Prompt Cursor to build a script, defining specific categories and the desired JSON output format <a class="yt-timestamp" data-t="20:34:00">[20:34:00]</a>.
    *   Address issues where Cursor might use old models or ignore documentation; actively prompt it to follow best practices, update models (e.g., GPT-4), and use specific packages (e.g., `zod`) <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
    *   Emphasize making the prompt more generic (not tied to specific categories) to allow for easier future expansion <a class="yt-timestamp" data-t="25:52:00">[25:52:00]</a>.
    *   Iterate with debugging prompts until the script correctly categorizes text with structured output <a class="yt-timestamp" data-t="28:10:00">[28:10:00]</a>.
    *   Add the validated code and expected response to the main documentation <a class="yt-timestamp" data-t="31:32:00">[31:32:00]</a>.

### Project Setup and Detailed PRD Generation
1.  **Initialize Project:** Use `shadcn` to set up the Next.js project, deleting the initial `package.json` to ensure a clean start <a class="yt-timestamp" data-t="32:30:00">[32:30:00]</a>.
2.  **Organize Instructions:** Create an `instructions` folder and copy the draft spec into it. Also, create a `.env.local` file for credentials <a class="yt-timestamp" data-t="33:40:00">[33:40:00]</a>.
3.  **Generate File Structure:** Use a tool like `tree -L 2` (ignoring `node_modules` and `.git`) to capture the current file structure and paste it into the instructions <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>.
4.  **Refine PRD with Stronger Model:** Leverage a more powerful model (e.g., 01 model) as an "engineering manager" to fill in granular details of the PRD <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. This involves pasting the entire current document into the model and asking it to structure the project file <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>. This proposed structure, including dependencies, helps align expectations and reduces ambiguity for the subsequent AI coding steps <a class="yt-timestamp" data-t="37:12:00">[37:12:00]</a>.

### Step-by-Step AI Implementation
With the detailed PRD, the application is built incrementally using Cursor:
1.  **Implement Core Functionality:** Prompt Cursor to build the application strictly based on the detailed instructions, tackling one numbered section at a time <a class="yt-timestamp" data-t="39:37:00">[39:37:00]</a>. This [[sequential_prompting_for_ai_workflows | sequential prompting]] significantly reduces errors and ensures the AI doesn't skip steps, unlike trying to "one-shot" the entire application <a class="yt-timestamp" data-t="40:47:00">[40:47:00]</a>.
2.  **Debugging During Development:** If errors occur, use commands like "help me debug" or "please help me add debug info to the code" to gain more information for the AI to fix issues <a class="yt-timestamp" data-t="42:35:00">[42:35:00]</a>.

### UI Refinement with Vercel v0
Once the functionality is built, refine the UI using Vercel v0:
1.  **Component-by-Component Refinement:** Copy specific UI code (e.g., homepage, subreddit card) into Vercel v0 <a class="yt-timestamp" data-t="46:17:00">[46:17:00]</a>.
2.  **Specific Styling Prompts:** Ask v0 to "make the UI a ton better," providing specific style preferences like "black and white, maybe dark mode as well, similar to Vercel" to guide the AI's design choices <a class="yt-timestamp" data-t="46:31:00">[46:31:00]</a>. Providing examples or referencing design principles from books can enhance the quality of the output <a class="yt-timestamp" data-t="47:21:00">[47:21:00]</a>.
3.  **Functionality Preservation:** Crucially, instruct v0 to "keep the functionality exactly like above but make the UI a ton better" to ensure the AI only modifies the visual aspects <a class="yt-timestamp" data-t="46:33:00">[46:33:00]</a>. This makes the UI changes more predictable and reduces the room for errors <a class="yt-timestamp" data-t="49:18:00">[49:18:00]</a>.

### [[sequential_prompting_for_ai_workflows | Reusable Modular Prompts]] in Action
A key demonstration of modular prompts is implementing user authentication:
1.  **Standardized Functionality:** User authentication (sign-in, sign-up) is a common, standardized feature across many applications <a class="yt-timestamp" data-t="52:27:00">[52:27:00]</a>.
2.  **Pre-defined Prompt/Doc:** A pre-existing documentation (`setup_auth.md`) containing a detailed prompt for authentication setup can be reused <a class="yt-timestamp" data-t="53:38:00">[53:38:00]</a>.
3.  **Step-by-Step Implementation:** Instruct Cursor to build the authentication features strictly based on this reusable document, breaking it down into distinct steps (e.g., "build step three and step four," then "step five," then "step six") <a class="yt-timestamp" data-t="53:33:00">[53:33:00]</a>. This demonstrates how a complex, yet standard, feature can be rapidly integrated by leveraging pre-defined, modular prompts <a class="yt-timestamp" data-t="54:08:00">[54:08:00]</a>.
4.  **Community Sharing:** The vision includes a community-driven aggregator for such modular prompts, enabling developers to easily share and integrate standard features like payment systems into their applications <a class="yt-timestamp" data-t="55:14:00">[55:14:00]</a>.

## Conclusion
This structured approach to AI coding, combining detailed specifications, clear platform roles, and the strategic use of [[sequential_prompting_for_ai_workflows | sequential]] and reusable modular prompts, significantly improves the predictability and success rate of AI-assisted development <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>. While it requires more upfront planning than simply "one-shotting" a prompt, it mirrors professional development processes and yields a much more robust and usable end product <a class="yt-timestamp" data-t="56:32:00">[56:32:00]</a>. This method transforms AI coding from an unpredictable gamble into a powerful, structured, and accelerated development tool, akin to an electric-assisted bicycle that still requires pedaling but provides a significant boost <a class="yt-timestamp" data-t="57:37:00">[57:37:00]</a>.