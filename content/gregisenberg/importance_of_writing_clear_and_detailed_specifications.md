---
title: Importance of writing clear and detailed specifications
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

Developing with large language models (LLMs) for coding is currently one of the most challenging topics, as results can often be unpredictable due to the LLM's tendency to "hallucinate" [00:00:36]. Tutorials may show seamless code generation, but in reality, users frequently encounter errors [00:01:01]. To achieve more consistent and predictable results, a structured workflow focusing on clear and detailed specifications is crucial [00:01:16].

## The Problem with Unpredictable AI Coding Results
AI coding based on large language models often yields unpredictable results [00:00:53]. Many online tutorials give the impression that one can simply prompt an AI to build an entire application, but in practice, this leads to numerous errors and a lack of smooth progression [00:00:44]. The inherent "hallucination" nature of LLMs means that initial attempts often result in a "bunch of errors" [00:00:58].

## The Core Solution: Upfront Planning and Detailed Specs
The first and most important step in achieving consistent AI coding results is to dedicate significant upfront time to writing very clear and detailed specifications [00:01:30]. This approach aims to simulate the workflow of a product team, where product managers (PMs) outline core functionalities, and engineering managers (EMs) further detail individual tickets or project architecture [00:01:56]. This process uncovers uncertainties early on, leading to more consistent outcomes [00:02:23].

> "I would spend a lot of time up front to actually write very clear and detailed specs" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

### Simulating Product Team Workflow
The ideal process for AI coding involves simulating how a product team operates [00:01:56]. A Product Manager (PM) would typically define the core functionalities of a product, which would then be handed over to an Engineering Manager (EM) to specify individual tasks or the project's architecture [00:02:00]. This structured approach reduces ambiguity later in the development cycle [00:02:11]. This structured approach reduces ambiguity, preventing the AI from delivering outcomes that are not precisely what the user intended [00:38:47].

### Benefits of Detailed Specifications
*   **Reduced Uncertainty**: Detailed specifications help uncover a lot of uncertainty upfront, streamlining the planning work [00:02:23].
*   **Consistent Results**: By removing ambiguity, detailed specs lead to more predictable and consistent AI-generated code [00:02:30].
*   **Clear Communication**: Specs serve as a clear communication tool for the AI, similar to how they communicate with human engineers [00:01:52].
*   **Improved Success Rate**: From experience, this approach significantly improves the success rate of AI coding projects [00:07:17].
*   **Scalability**: A well-structured plan, with generic prompts, allows for easier maintenance and addition of new features later [00:26:03].

## Workflow for Creating Detailed Specifications

The workflow involves several key stages to ensure the AI has a clear understanding of the project.

### 1. Draft Spec Creation
Start by drafting a specification document using a template structure [00:09:10]. This includes:
*   **Project Overview**: A simple overview stating the goal, such as "building a Reddit analytics platform where users can get analytics of different subreddits" [00:21:21].
*   **Core Functionality**: Break down the "must-have" features, similar to what a product manager would define [00:11:43]. For the Reddit analytics platform example, this included:
    *   Seeing a list of available subreddits and adding new ones [00:11:57].
    *   A subreddit page with "top post" and "analysis" tabs [00:12:02].
    *   Fetching Reddit post data and analyzing it into different themes [00:12:15].
This initial draft doesn't need every detail, but it should clearly communicate the project's goal and core functions [00:12:36].

### 2. Including Proof-of-Concept Code and Documentation
Before full implementation, it's crucial to build small proof-of-concept pieces for core functionalities and include their documentation within the spec [00:12:57]. This helps align the AI on implementation details and prevents later errors [00:09:53].

*   **Research Libraries**: Use tools like ChatGPT to identify appropriate packages (e.g., `snoowrap` for Reddit data in a Next.js project) [00:13:34].
*   **Examine Examples**: Check package documentation (e.g., npm) for code examples to understand authentication and usage [00:14:05].
*   **Build Proof-of-Concept Scripts**: Create simple TypeScript scripts to test core functionalities (e.g., fetching subreddit posts) [00:14:30].
*   **Debug Early**: Testing these proof-of-concept scripts early on allows for debugging common errors, which would otherwise appear later in the main project [00:17:19]. Using prompts like "help me debug" or "let's think step by step" can guide the AI to resolve issues systematically [00:17:33].
*   **Document Proven Code**: Once a proof-of-concept script works, include the functional code and expected responses directly in the spec as documentation [00:19:19]. This serves as a clear reference for the AI later [00:31:54].

### 3. Communicating File Structure
A common reason for AI coding failures is the AI's lack of understanding of the project's file structure [00:10:04].
*   **Generate File Structure**: Use tools like `tree` (e.g., `tree -L 2 --ignore node_modules`) to generate a snapshot of the desired file structure [00:34:16].
*   **Include in Spec**: Paste this file structure into the specification document, ensuring the AI knows where to create and modify files [00:35:10].

### 4. Refining Specs with Advanced Models (e.g., 01/GPT-4)
While initial specs are helpful, they might still have gaps from an engineering perspective [00:35:30].
*   **Use Stronger Models**: Feed the initial draft spec into a more powerful LLM (like 01 or GPT-4) [00:36:00].
*   **Act as Engineer Manager**: Prompt the model to act as an "engineer manager" and fill in the details, proposing a final project structure and identifying dependencies [00:36:12]. This helps to align the product manager's high-level vision with the detailed engineering plan [00:38:05].
*   **Generate Detailed PRD**: Ask the model to generate a comprehensive Product Requirements Document (PRD) that includes defined functionalities, variables, file structures, and additional requirements [00:37:29]. This detailed PRD makes engineers "light up" as it provides clear guidance and leaves "a lot less ambiguity" [00:38:07].

## Building the Application Step-by-Step

Once the detailed specifications are ready, begin building the application incrementally using an AI coding tool like Cursor.

1.  **Commit Project Setup**: After setting up the project and adding UI components (like `shadcn/ui`), commit the initial setup to version control [00:39:05].
2.  **Strictly Follow Instructions**: Prompt the AI tool to build the application "strictly based on this instruction" and tackle features one by one, like "number one first" [00:39:33]. This reduces the likelihood of errors and prevents the AI from skipping steps [00:40:48].
3.  **Iterative Development**: Continuously prompt the AI to implement the next step (e.g., "now let's do the second part") [00:40:39]. This "crawl, walk, run" strategy is more effective than attempting a "one-shot" generation [00:41:17].
4.  **Debugging**: If errors occur, use debug info to provide specific feedback to the AI [00:42:47]. The prior research on specific libraries also helps in understanding and fixing recurring errors [00:45:00].

## UI Design and Reusable Prompts

### Functionality First, UI Later
A key strategy is to focus on building the core functionality first and address the UI later [00:02:51]. Tools like Cursor can handle functionality, while VZ (Vercel's generative UI tool) can be used for UI refinement [00:02:55]. This approach makes UI changes more predictable and easier to manage once the underlying code is stable [00:46:10]. When prompting VZ, specifying a desired style (e.g., "black and white, dark mode, similar to Vercel") helps the AI interpret "look better" in a consistent way [00:46:43]. [[aesthetics_in_software_design | Aesthetics in software design]] can be significantly improved by leveraging design principles from books and translating them into clear prompts for VZ [00:47:21].

### Reusable Modular Prompts
Reusable modular prompts are highly valuable for common, standardized functionalities across different projects [00:03:12].
*   **Standard Features**: Features like user authentication (user "auth") or payment systems are often standard across many applications [00:03:44].
*   **Community Sharing**: There's a potential for a community-driven collection of such prompts that developers can share and reuse [00:03:49].
*   **Example: User Authentication**: A pre-prepared document can be used as a modular prompt to guide the AI through setting up user authentication step-by-step, including library installation and sign-up/sign-in page creation [00:53:33]. This significantly speeds up the development process for common features [00:55:19].

## Conclusion
Adopting a structured, planned approach to AI coding, similar to traditional product development, is essential for achieving consistent and predictable results [00:56:05]. This involves:
1.  **Extensive Upfront Planning**: Dedicating significant time to writing detailed specifications to minimize uncertainty [00:56:05].
2.  **Functionality First**: Prioritizing the core functionality before diving into UI design [00:56:14].
3.  **Reusable Prompts**: Developing and sharing modular prompts for standard features to accelerate development [00:56:16].

While AI coding may not be a "one-shot" solution where everything works instantly, it significantly simplifies the development process compared to traditional methods [00:57:21]. It's akin to an "electric-assisted bicycle"—it provides a substantial boost, but still requires the user to "pedal the wheels" by providing clear guidance and structured steps [00:57:41].