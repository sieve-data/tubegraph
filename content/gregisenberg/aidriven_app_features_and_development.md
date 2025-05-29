---
title: AIdriven app features and development
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroque is building a significant portfolio of mobile applications using AI, specifically [[AIdriven coding platforms | Cursor]], for their creation <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. His process involves leveraging AI for various aspects of app development, from UI generation to integrating advanced AI capabilities like tool calling and dynamic asset creation <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Development Workflow and Tools

Chris's workflow primarily uses [[AIdriven coding platforms | Cursor]] for coding <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. He has explored many [[AI tools for app development | AI tools for app development]] for coding over two years, including GitHub Copilot and Claude Code, but currently finds [[AIdriven coding platforms | Cursor]] to be the most effective <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

He uses:
*   **[[AIdriven coding platforms | Cursor]]**: The primary tool for native iOS development, even though many people use it for React and Expo development <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **ChatGPT 4o**: Used for [[AIdriven storytelling and content creation | asset generation]] and image creation <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Open Router**: A service that allows switching between over 300 large language models (LLMs) with a single line of code, making it ideal for testing and development <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Claude 3.7**: The preferred LLM for iOS development, chosen for its effectiveness despite occasional "going off the rails" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

The development process involves opening Xcode projects directly in [[AIdriven coding platforms | Cursor]] to make edits, then switching back to Xcode to build and run the app <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. While this requires switching between applications, it's significantly faster than previous methods like manually pasting code into Claude <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Key Techniques for [[Developing and customizing AIdriven projects | AIdriven Development]]
*   **Manual Project Setup**: It's crucial to set up Xcode projects manually, as [[AIdriven coding platforms | Cursor]] struggles with initial project configuration, including framework selection and enabling network requests <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **UI-First Approach**: Chris recommends building the user interface with dummy data first, as this makes it easier for the AI to follow instructions by focusing on one task <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Contextual UI Design**: When prompting the AI to create UI, explicitly tell it to "follow the similar UI as other parts of the app" to ensure consistency <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Feeding Documentation**: Continuously feeding official documentation (e.g., Open Router docs, Apple documentation) into [[AIdriven coding platforms | Cursor]] helps reduce AI hallucinations, especially in platform-specific development like iOS and macOS <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This is particularly useful as APIs are constantly changing <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
*   **Screenshot-Driven Debugging**: When encountering errors, Chris screenshots the error message and feeds it back to [[AIdriven coding platforms | Cursor]] to get fixes <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.

## Building AI Features: An Example with a Budgeting App

Chris demonstrates adding an AI chat feature to an existing budgeting app called Luna <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. The goal is to allow users to ask questions about their spending directly within the app <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

### Phase 1: Creating the UI
The first step was to prompt [[AIdriven coding platforms | Cursor]] to create a new tab for an AI chat with a UI similar to the rest of the app, using hardcoded dummy data <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. The AI successfully generated a functional chat UI, including message animations, in a single prompt, requiring only minor manual adjustments like adding a chat icon <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

### Phase 2: Integrating with LLMs via Open Router
Next, the goal was to make the chat functional by hooking it up to an actual LLM using Open Router <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. The prompt requested:
*   Making the chat functional, not hardcoded <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   Using Open Router for quick model swapping <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   Adding a setting to toggle between models <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
*   Using the last three months of transactions as context for questions <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

[[AIdriven coding platforms | Cursor]] generated the necessary code, creating a new `AI chat view` and an `Open Router services` file, following the app's existing service structure <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
*   **Security Note**: API keys should ideally reside in the backend, not hardcoded in the frontend as seen in the demo for simplicity <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

### Phase 3: Optimizing the Prompt
Recognizing that the initial LLM prompt was too basic, Chris used Claude to generate a more effective prompt <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
*   **XML Format**: Formatting the prompt in XML (with `title` and `description` tags) increases the chance of the LLM producing good results <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>.
*   **Conciseness and Persona**: The prompt instructed the AI to provide concise answers, like a friend, and not to show its work unless asked <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>. This empathetic approach to prompting enhances the user experience <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

### Phase 4: Implementing Agent/Tool Calling
To optimize costs and context management, Chris implemented tool calling, allowing the LLM to dynamically retrieve only the necessary data <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.
*   **Problem**: Initially, the app fed three months of transaction history for every question, which is costly and inefficient <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.
*   **Solution**: Tool/function calling allows the LLM to access defined "tools" (functions) to gather specific information before answering <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This creates an "agent" within the app <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>.
*   **Defining Tools**: Chris prompted [[AIdriven coding platforms | Cursor]] to create local tools, such as `getTransactionsForDateRange` and `getUserCurrentBudget` <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>. These tools interact with the app's local database <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.
*   **Dynamic Context**: Now, if a user asks, "Where did I eat last year?" the LLM first calls the `getTransactionsForDateRange` tool for the entire year, then uses that specific data to answer the question, avoiding sending irrelevant data <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>.
*   **Benefits**: This significantly reduces costs and improves efficiency. It also allows the AI to perform more complex actions, such as analyzing budgets or even potentially rebalancing them if given the right tools <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

### Phase 5: Displaying Costs and Models
For transparency and [[AIdriven business automation | business automation]], Chris integrated a feature to display the token count and cost of each AI interaction directly within the chat <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>. He also enabled the app to dynamically pull and display all available Open Router models, along with their context windows and costs <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. This provides valuable insights during development and for future production monitoring <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>.

## AI-Driven Asset Generation with ChatGPT 4o

Chris extensively uses GPT-4o for generating high-quality visual assets for his apps <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   **Infinite Secondary Assets**: By taking an existing primary asset (e.g., an app mascot), GPT-4o can generate an infinite number of secondary assets for different purposes, such as loading screens, empty states, or unique illustrations <a class="yt-timestamp" data-t="00:49:28">[00:49:28]</a>.
*   **Prompting for Specificity**: Prompts can be highly specific (e.g., "give it wired glasses and put it in front of a laptop" <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>) and allow for iterative refinement, including modifying specific elements or matching styles <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Realistic Mock Data**: AI can generate realistic mock data (e.g., restaurant names in Dallas) for testing and demos, making the app more relatable and engaging for potential users or investors <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. This helps in validating [[AIdriven startup ideas | startup ideas]] <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
*   **Brainstorming**: AI can also assist in brainstorming app mascots or logos based on app functionality <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## Advice for Developers and Non-Technical Individuals

*   **For Developers**: Embrace AI tooling. It significantly accelerates development, and developers who learn to use these tools will thrive in the coming decade <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.
*   **For Non-Developers**: Use AI as a learning tool to grasp programming fundamentals <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. While AI can generate code, tools like [[AIdriven coding platforms | Cursor]] can be dangerous if one lacks basic programming knowledge, as they might inadvertently expose sensitive information like API keys <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. Safer options with more "guardrails" include Replit or Lovable <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.

Chris emphasizes the importance of humanizing apps by adding "delight" through elements like unique loading screens, welcome emails, and custom illustrations <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>. AI can help create these touches, transforming bare-bones apps into more engaging products <a class="yt-timestamp" data-t="00:52:41">[00:52:41]</a>.