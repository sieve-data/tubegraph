---
title: Using Cursor for native iOS app development
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Chris Baroque, a developer building a large portfolio of mobile apps, leverages AI and [[building_ai_apps_with_cursor | Cursor]] to create native iOS applications and publish them to the App Store <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. His process involves detailed techniques for integrating AI agents, using Open Router, and employing ChatGPT for image generation <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Chris's Approach to AI-Powered App Development

Chris has built a portfolio of clean and interesting mobile apps, including "Ellie," a daily planning app with thousands of monthly active users and around 2,000 paid users <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. He emphasizes that he's able to build these robust apps due to AI supercharging his workflow <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Unlike typical weekend projects, his work demonstrates that AI can be used to build serious, complex applications over a long period <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

Chris aims to provide a behind-the-scenes look at an advanced Cursor workflow, specifically focusing on native iOS development, which he notes not many people do with Cursor <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a> <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. He hopes his methods demystify AI use for developers and encourage its adoption <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Tools and Models Used

*   **Cursor**: The primary tool for coding, used for about two years since early GitHub Copilot days <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a> <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Chris notes that people are surprised he uses it for native iOS development <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **ChatGPT for Asset Generation**: Used for creating and modifying assets, especially with the improved capabilities of GPT-4o <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   **Claude 3.7**: Chris's preferred model for code generation, particularly for native iOS development, despite its tendency to "go off the rails" sometimes <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a> <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. He finds it the best for iOS development <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Open Router**: A service that allows switching between over 300 different LLMs with a single line of code, enabling easy testing of models and price points during development <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a> <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

## Cursor Workflow for Native iOS Development

Chris describes his workflow for iOS development as "the jankst setup" but highly effective <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

*   **Opening Xcode Projects in Cursor**: He opens the Xcode project in Cursor to make edits and uses Cursor's chat feature for file modifications <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a> <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Switching Between Cursor and Xcode**: He then switches back to Xcode to build and run the app, repeating this process iteratively <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This method is substantially faster than his previous approach of pasting code into Claude and then back into Xcode <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

> [!CAUTION]
> Do not attempt to use Cursor to set up the Xcode project initially <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Many settings and framework embeddings in Xcode must be done manually, as Cursor is not capable of handling these configurations via the terminal for iOS projects <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a> <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. For example, enabling outgoing network requests needs to be done manually in Xcode <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

## Building an AI Feature in an iOS App: A Case Study

Chris demonstrates adding an AI chat feature to his existing budgeting app, "Luna" <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. The goal is to allow users to chat and ask questions about their spending, mimicking how many people use ChatGPT with exported CSVs of their finances <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Step 1: Creating the UI for the AI Chat

Chris's first prompt to Cursor was: "Create a new tab for an AI chat. Can you make the UI for this? Try to follow the similar UI as other parts of the app. You can just hardcode the chat. Just use dummy data." <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

*   **UI-First Approach**: Chris's technique is to focus solely on the UI first, using dummy data, before connecting it to backend or real data <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This increases the chances of success by allowing the AI to focus on one task <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   **Context and Consistency**: He tagged the entire codebase to provide the AI with context, and explicitly instructed it to follow the existing UI style <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a> <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Results**: Cursor generated the chat UI, hardcoding dummy data, and surprisingly included an animation where new messages scroll down <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a> <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. It successfully matched the app's purple color scheme <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Chris only manually added a chat icon <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Troubleshooting**: Minor issues included the message area being hidden behind the tab bar, requiring additional prompts to fix <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. Chris often feeds screenshots of errors or UI issues to Cursor for fixes <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Step 2: Connecting the UI to an LLM (Open Router)

The next step was to make the chat functional by hooking it up to an actual LLM <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

*   **Prompt**: "Make this functional and not hardcoded. Can you use open router so I can swap out the chat model quickly? Put a setting at the top right so we can toggle between the models. When you ask questions, can you use the last 3 months of transactions as context?" <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
*   **[[enhancing_cursor_ai_prompts_with_context_and_tagging | Feeding Documentation]]**: A crucial technique is feeding official API documentation (e.g., Open Router docs) directly into Cursor. This indexes the documentation, giving Cursor the necessary context for API calls without manual copying and pasting <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This also significantly reduces hallucinations, especially for platform-specific development like iOS or Mac <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.
*   **Results**: Cursor successfully integrated Open Router, making the chat functional with a model toggle <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a> <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. It generated two new files: `AI Chat View` for the UI and `Open Router Services` for the API calls <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Cursor demonstrated context of the app's file structure by making the `Open Router Services` file similar to existing services <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.
*   **Security Concern**: API keys were hardcoded in the frontend for demo purposes <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Chris notes this is a security risk and should ideally be handled in the backend <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

### Step 3: Improving the Prompt

The initial prompt provided by Cursor for the LLM was basic, leading to poor answers <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.

*   **Using Claude for Prompt Generation**: Chris uses Claude to generate better prompts, finding it particularly good at this task <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
*   **XML Format for Prompts**: He instructs Claude to provide the prompt in XML format (title and description tags), which he has observed leads to higher-quality LLM results <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a> <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.
*   **Prompting Claude**: An example prompt to Claude was: "I have a budgeting app. I want to add an AI chat to you. Can you give me a very good prompt in XML format so it can follow the instructions. And make it so the answers are very concise like a friend answering it for you. Don't show your work unless asked and just answer the question." <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>.
*   **Injecting into Cursor**: Chris then provided this improved prompt as context to Cursor, asking it to incorporate it into the application <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a> <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>.
*   **Results**: The improved prompt led to much more concise and natural-sounding responses, like a friend answering a question <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

### Step 4: Implementing Tool/Function Calling (Agents)

A key challenge was the cost and latency of feeding three months of transaction history for every question <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

*   **The Problem**: Sending large contexts (e.g., a year's worth of transactions) for simple questions (e.g., "Where did I eat last week?") is inefficient and expensive <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>.
*   **Solution: Function Calling (Agents)**: Open Router and GPT support tool/function calling, allowing the LLM to access defined tools and functions within the application <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>. This allows the LLM to dynamically fetch only the necessary context <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>.
    *   The LLM first assesses if it has enough context. If not, it checks if it has tools to get the missing information <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. It then calls the relevant tool and re-evaluates, looping until it has enough context or reaches a defined loop limit (e.g., 4 times) <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a> <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.
*   **Prompt**: "Create a new tool function that the LLM is able to call. I want to use function calling from Open Router. Create a few tools: a tool to get transactions for a specific date range, and a tool to get the current budget. Ensure all tools are local, not calling external APIs." <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Results**: Cursor generated tool definitions and the corresponding local Swift functions <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. These functions now interact with the local database to filter transactions by date range or retrieve budget information <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.
    *   Asking "Where did I eat last year?" now triggers the `get transactions for date range` tool, dynamically fetching only the relevant year's data <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>.
    *   Asking "Am I overbudget anywhere?" triggers the `get user's current budget` tool, providing specific budget vs. spending comparisons <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>.
*   **Power of Agents**: This functionality transforms the chat into an agent with access to specific tools, enabling complex queries and potentially actions like modifying budgets or generating reports <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. This was achieved with roughly 3-4 major prompts (and about 20 prompts including error fixes) <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a> <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.

### Step 5: Displaying Costs and Model Information

As an additional feature, Chris wanted to display the cost and tokens used for each LLM call <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

*   **Prompt**: "Alter the chat: right below the messages, I want to see the total tokens that were used and the cost. Make a call to Open Router's generation endpoint to pull this data." <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. He also tried to prompt it to pull all Open Router models dynamically <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>.
*   **Results**: Cursor successfully added the display of tokens consumed (prompt and completion) and the estimated cost for each response <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>. While the dynamic model pulling didn't work perfectly (due to some models not supporting function calling), it did show how various models differ in context window size and cost <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a> <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>.

## AI for Asset Generation

Chris emphasizes the use of GPT-4o for generating high-quality assets to enhance app aesthetics and user experience <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a> <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.

*   **Generating and Modifying Assets**: Users can feed existing assets (like a mascot) into GPT-4o and then prompt it to generate variations or secondary assets for loading screens, empty states, or illustrations <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. Examples include adding glasses, changing backgrounds, or incorporating specific objects like a coffee cup <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.
*   **Realistic Elements**: Chris demonstrated feeding an image of his dog to GPT-4o and asking it to modify an illustration to resemble his dog <a class="yt-timestamp" data-t="00:50:17">[00:50:17]</a>.
*   **Brainstorming**: AI can also be used to brainstorm initial logo ideas or mascots for apps <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

> [!TIP]
> Use realistic, localized dummy data generated by AI for demos and testing <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. This makes the app more relatable and helps potential users or investors envision themselves using it <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a> <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

## General Advice on [[AI integration in mobile apps | AI Integration in Mobile Apps]]

*   **For Developers**: Embrace AI tooling. Developers who learn to use these tools will thrive in the coming decade, as the technology is inevitable <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a> <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>.
*   **For Non-Developers**: [[using_cursor_ai_for_beginners_and_nondevelopers | Give AI tools a shot]], but primarily as a learning tool <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
    *   Start with tools like Replit or Lovable, which have more guardrails and are less "dangerous" than Cursor, as Cursor can easily allow users to commit risky code (e.g., hardcoding API keys in the frontend) <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a> <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a> <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>.
    *   Learn programming basics and use AI as a teacher to get better at fundamentals before diving into more advanced tools <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.