---
title: Advanced workflow techniques for mobile app development
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroke has demonstrated how to build a substantial portfolio of robust, clean, and engaging [[consumer_mobile_app_development_strategies | mobile apps]] using [[ai_app_development_strategies | AI]]. His approach leverages AI to significantly enhance and accelerate the [[optimizing_workflow_with_ai_design_tools | workflow]] for app development, even for complex projects like native iOS applications <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Chris, who describes himself as a "regular guy" without a Stanford or Google background, highlights that deep technical expertise isn't a prerequisite when utilizing these advanced tools <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Core Tools and Technologies <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>

Chris's primary tools and models include:
*   **Cursor**: His main integrated development environment (IDE) for coding, even for native iOS development, which is less common <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. He has used AI for coding for about two years, trying various tools like GitHub Copilot, Windsurf, and Claude Code <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
*   **Chat GPT 4o**: Used specifically for asset generation <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **Claude 3.7**: Chris prefers this model for LLM responses, particularly for iOS development, noting its effectiveness despite occasional "off-the-rails" behavior that an experienced developer can manage <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Open Router**: A service that allows developers to easily switch between over 300 different LLM models with a single line of code, enabling efficient testing and comparison of models and their costs during development <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a><a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a><a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.

## Workflow for Native iOS Development with Cursor <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>

Chris uses what he calls a "janky setup" for native iOS development:
1.  He opens the Xcode project file directly in Cursor <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
2.  He uses Cursor's chat feature to make file edits <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
3.  He then switches back to Xcode to build and test the changes <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. This iterative process, though involving switching, is "substantially faster" than his previous method of copying and pasting code into Claude <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.

### Important Caveats for Xcode Integration <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>
*   **Manual Project Setup**: Do **not** use Cursor to set up the Xcode project initially. Many settings and frameworks (like enabling outgoing network requests) must be configured manually within Xcode <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. Cursor is more effective once the project is already set up <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

## Key Techniques and Tips <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>

### 1. UI First Approach <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>
*   Prioritize building the user interface (UI) with dummy data before hooking up the backend or live data <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>. This helps the AI focus on one task at a time, increasing the chances of success <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.
*   **Example**: For a budgeting app, Chris first prompted Cursor to create a chat UI with hardcoded data, making sure it visually matched the rest of the app <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.

### 2. Providing Full Codebase Context <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>
*   When making major changes, tag the entire codebase (e.g., the root folder of the project) so the AI has complete context, which helps it understand the existing structure and make appropriate modifications <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>.

### 3. Maintaining UI Consistency <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>
*   Explicitly instruct the AI to "follow the similar UI as other parts of the app" to ensure new features blend seamlessly <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. Otherwise, the AI might generate components that don't match the existing design <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.

### 4. Using Screenshots for UI Issues <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>
*   When the UI isn't rendering correctly, take screenshots and feed them into Cursor. This visual input helps the AI understand the problem and provide better fixes <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>.

### 5. Feeding Documentation to Reduce Hallucinations <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>
*   Copy and paste URLs of official documentation (e.g., Open Router API docs, Apple's iOS documentation) into Cursor using `@docs` <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>. Cursor will index these documents, providing the AI with up-to-date and accurate information, drastically reducing "hallucinations" (incorrect or non-existent functionalities) <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. This is especially crucial for rapidly changing APIs and platform-specific development like iOS and Mac apps <a class="yt-timestamp" data-t="21:20:00">[21:21:00]</a>.

### 6. Prompt Engineering for Better LLM Responses <a class="yt-timestamp" data-t="26:46:00">[26:46:00]</a>
*   **Use Claude for Prompt Generation**: Chris uses Claude to generate high-quality prompts, finding it particularly good at this task <a class="yt-timestamp" data-t="27:26:00">[27:26:00]</a>.
*   **XML Formatting**: Formatting prompts in XML (e.g., `<budgeting_assist_instructions>...</budgeting_assist_instructions>`) can lead to better results from the LLM <a class="yt-timestamp" data-t="27:53:00">[27:53:00]</a>.
*   **Concise and Empathetic Instructions**: Ask the AI to be concise and adopt a specific persona (e.g., "like a friend answering it for you," "don't show your work unless asked") to control the tone and verbosity of responses <a class="yt-timestamp" data-t="28:26:00">[28:26:00]</a><a class="yt-timestamp" data-t="30:08:00">[30:08:00]</a>. This focus on user experience (UX) dramatically improves the product's quality <a class="yt-timestamp" data-t="29:46:00">[29:46:00]</a>.

### 7. Generating Realistic Mock Data with AI <a class="yt-timestamp" data-t="31:19:00">[31:19:00]</a>
*   Instead of generic dummy data, use AI to generate mock data that is more realistic and relevant to your target audience (e.g., "restaurants and places that look way more realistic for a 28-year-old male in Dallas") <a class="yt-timestamp" data-t="31:41:00">[31:41:00]</a>. This makes demos and testing more impactful and helps potential users visualize themselves using the app <a class="yt-timestamp" data-t="32:38:00">[32:38:00]</a>.

### 8. [[Building_AIpowered_workflows_without_coding | Implementing AI-Powered Workflows Without Coding]]: Tool/Function Calling (Agents) <a class="yt-timestamp" data-t="36:46:00">[36:46:00]</a>
*   Instead of chaining multiple LLMs to parse requests and then answer, leverage tool or function calling, a feature available in Open Router and GPT models <a class="yt-timestamp" data-t="36:01:00">[36:01:00]</a>.
*   **How it works**: The LLM is given access to a set of predefined "tools" (functions) that it can decide to call based on the user's query <a class="yt-timestamp" data-t="36:48:00">[36:48:00]</a>.
    *   The LLM first assesses if it has enough context to answer <a class="yt-timestamp" data-t="38:23:00">[38:23:00]</a>.
    *   If not, it checks if it has a tool that can provide the necessary information <a class="yt-timestamp" data-t="38:29:00">[38:29:00]</a>.
    *   It then calls the tool, receives the output, and uses that new context to answer the question <a class="yt-timestamp" data-t="38:32:00">[38:32:00]</a>. This process can loop until sufficient information is gathered <a class="yt-timestamp" data-t="38:34:00">[38:34:00]</a>.
*   **Local Tools**: Tools can be functions within your application that interact with local data (e.g., `getTransactionsForDateRange`, `getCurrentBudget`) rather than external APIs, making them efficient and secure <a class="yt-timestamp" data-t="37:10:00">[37:10:00]</a><a class="yt-timestamp" data-t="39:20:00">[39:20:00]</a>.
*   **Benefits**: Reduces costs by only providing relevant context, enables the creation of powerful agents that can perform complex tasks (e.g., rebalancing budgets, generating reports) <a class="yt-timestamp" data-t="35:10:00">[35:10:00]</a><a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.
*   **Loop Limits**: Set a maximum number of loops for tool calling to prevent infinite loops <a class="yt-timestamp" data-t="41:50:00">[41:50:00]</a>.

### 9. Monitoring LLM Costs and Token Usage <a class="yt-timestamp" data-t="45:31:00">[45:31:00]</a>
*   Integrate API calls (e.g., Open Router's generation endpoint) to display token usage and estimated costs directly within the app's chat interface <a class="yt-timestamp" data-t="45:56:00">[45:56:00]</a>. This provides immediate feedback on the financial implications of different queries and models during development <a class="yt-timestamp" data-t="47:54:00">[47:54:00]</a>.

### 10. [[optimizing_workflow_with_ai_design_tools | Optimizing Workflow with AI Design Tools]]: AI for Asset Generation <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a>
*   **GPT-4o for High-Quality Assets**: Use models like GPT-4o to generate high-quality and consistent visual assets for apps <a class="yt-timestamp" data-t="49:00:00">[49:00:00]</a>.
*   **Infinite Variations**: By providing an initial mascot or character, AI can generate an "infinite number of secondary assets" for various app states (loading screens, empty states, illustrations) while maintaining a consistent style <a class="yt-timestamp" data-t="49:28:00">[49:28:00]</a>.
*   **Refinement**: Continuously prompt the AI to refine assets based on specific requirements (e.g., "remove the legs," "make the dog look more like my dog") <a class="yt-timestamp" data-t="50:14:00">[50:14:00]</a>.
*   **Brainstorming**: AI can also be used to brainstorm initial ideas for mascots or logos <a class="yt-timestamp" data-t="52:54:00">[52:54:00]</a>.
*   **Humanizing the App**: These AI-generated visuals add a crucial layer of polish and "delight" to the app, humanizing the user experience beyond bare-bones functionality <a class="yt-timestamp" data-t="51:38:00">[51:38:00]</a>.

## Security Considerations <a class="yt-timestamp" data-t="55:04:00">[55:04:00]</a>
*   Be cautious about hardcoding API keys or sensitive information directly into the frontend of the application, especially when using AI code generation <a class="yt-timestamp" data-t="23:57:00">[23:57:00]</a><a class="yt-timestamp" data-t="55:28:00">[55:28:00]</a>. Such keys can be easily exploited if accidentally exposed <a class="yt-timestamp" data-t="55:36:00">[55:36:00]</a>. Ideally, these should reside in a secure backend environment <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.

## Advice for Developers and Non-Developers <a class="yt-timestamp" data-t="53:39:00">[53:39:00]</a>

*   **For Developers**: Embrace AI tooling. While everyone will benefit, skilled developers who learn to leverage these tools will "thrive for the next decade" <a class="yt-timestamp" data-t="53:56:00">[53:56:00]</a>.
*   **For Non-Developers**: [[creating_apps_without_extensive_coding_knowledge | Give AI a shot]] as a learning tool. Start with platforms that have more "guardrails" like Replit or Lovable, as Cursor can be "dangerous" and may produce code that leads to unexpected or problematic behavior (e.g., exposing API keys) <a class="yt-timestamp" data-t="54:40:00">[54:40:00]</a>. It's advisable to learn some basic programming fundamentals and use AI as a teacher to improve at them before diving into more advanced AI coding tools <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>.