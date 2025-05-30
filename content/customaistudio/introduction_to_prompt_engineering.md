---
title: Introduction to Prompt Engineering
videoId: d_R77Pe-VEo
---

From: [[customaistudio]] <br/> 

[[prompt_engineering_and_modularity_in_ai_systems | Prompt engineering]] is a widely used term in the AI space, though it is sometimes associated with "grifty marketers" pushing simple prompt lists for quick gains <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Despite this, there is genuine merit to the practice, akin to software engineering but utilizing natural language <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## What is Prompt Engineering?
[[the_challenges_and_strategies_of_llm_prompt_engineering | Prompt engineering]] is essentially the process of telling an AI agent what to do, who it is, and how to do it <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. It involves providing clear instructions, context, and sometimes examples to guide the AI's behavior and output <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### Prompt Engineering vs. Software Engineering
Similar to how software engineering involves writing precise instructions in a different language to tell a computer what to do, [[the_challenges_and_strategies_of_llm_prompt_engineering | prompt engineering]] involves writing prompts in natural language (like English) to instruct an AI system <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### The Role of Language
Effective [[the_role_of_language_in_ai_prompt_engineering | prompt engineering]] benefits from strong language skills, as being proficient in speaking and reading English can lead to better question asking and more effective information extraction <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, simply being able to speak a language does not automatically make one an "elite prompt engineer" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Designing Prompts for AI Agents
When [[building_efficient_ai_agents_with_prompts | building efficient AI agents]], [[the_challenges_and_strategies_of_llm_prompt_engineering | prompt engineering]] is crucial for ensuring reliable and consistent performance <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

### Core Prompt Formula
A successful prompt formula for [[building_efficient_ai_agents_with_prompts | AI agents]] includes:
1.  **Objective**: A clear role and specific overall goal for the agent <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
2.  **Context**: Comprehensive background information about the user's situation or relevant databases <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
3.  **Instructions**: Step-by-step guidance on how the agent should perform its job <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
4.  **Output Requirements**: Specifications for the exact format of the agent's output <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
5.  **Examples**: Real-world examples, including edge cases, to improve consistency <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Examples are key for consistent output and reliability when agents are integral to business operations <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

#### Detailed Explanation of Formula Components

##### Objective
The objective defines the agent's main task, describing what it needs to achieve <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Example for a Calendar Agent**: "Your objective is to parse user input to identify and extract event-related information specific to calendar operations. You must generate a JSON package with the correct parameters for each action such as creating, updating, retrieving, and deleting calendar events. Your focus should be solely on event management tasks ignoring unrelated instructions." <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>

##### Context
This section provides background information, helping the agent understand its role and specific scenarios <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Context can emphasize the importance of certain outputs or behaviors. For instance, stating that a specific output format is critical for the entire automation to function ensures the AI takes it seriously <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

##### Instructions
Instructions outline the step-by-step process the agent should follow <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Example for a Calendar Agent**:
    1.  **Identify the calendar action**: Understand the user prompt and determine the required action (e.g., create, delete, get event) <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
    2.  **Extract event information**: Gather necessary details from the user's message <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    3.  **Retrieve information from the database**: Access data like email addresses from a [[data_management_and_prompt_engineering_for_ai_agents | vector store database]] <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    4.  **Generate a JSON output**: Format the extracted and retrieved information into a JSON package, which serves as inputs for subsequent nodes <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

##### Output Requirements
This specifies the format and content of the agent's final output, ensuring it meets the needs of the next step in the workflow <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. For example, a JSON package is often required for automated actions <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

##### Examples
Providing numerous real-world examples, especially those covering edge cases, significantly improves the consistency and reliability of the agent's output <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. While it's not necessary to account for every single scenario, more examples lead to better results <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

## Practical Application: Calendar Tool Example
The principles of [[the_challenges_and_strategies_of_llm_prompt_engineering | prompt engineering]] are demonstrated through a calendar tool designed to manage events via natural language commands <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Workflow Example
A personal agent can be instructed to manage a calendar. For instance, a user might say: "Create a meeting for Thursday at 5:00 p.m. and add Andrew Lewis to it" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The [[agentic_prompting_and_decisionmaking_frameworks | AI agent]] then performs several steps:
1.  **Information Retrieval**: It accesses a [[data_management_and_prompt_engineering_for_ai_agents | vector store database]] to find Andrew Lewis's email address <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Date/Time Calculation**: Since models like GPT-4 are trained up to a certain date (e.g., 2023), the system calculates the correct date and time for "Thursday at 5:00 p.m." based on the current date and time <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **Action Identification**: A "switch function" identifies the specific action required, such as "create an event," "delete an event," or "update an event" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
4.  **Event Creation**: The event is created on the calendar <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
5.  **Response Formatting**: Key information from the created event (title, description, start/end times, link) is then formatted into a "response" field, which the agent receives <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This allows for complex commands, such as "send Andrew an email asking if he has finished the project proposal for our call with John on Friday and schedule a meeting with him 30 minutes before the call with John and call it team sync" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The agent, using the appropriate [[designing_prompts_for_calendar_and_email_actions | email actions]] and [[designing_prompts_for_calendar_and_email_actions | calendar actions]] tools, extracts only the relevant information (e.g., creating the calendar event 30 minutes before John's meeting) and ignores extraneous details <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Prompt Details in Action
The system prompt guides the [[agentic_prompting_and_decisionmaking_frameworks | agentic prompting]] by defining its objective, context, and required parameters <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Outputs are specifically requested in a JSON package, which includes details like attendees and start dates <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Separate prompts are used for calculating dates and times, ensuring accuracy <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### [[challenges_in_ai_prompt_engineering_and_development | Challenges in AI Prompt Engineering]]
While current methods work, continuous effort is put into making the process more streamlined, optimized, and cost-efficient <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The goal is for [[agentic_prompting_and_decisionmaking_frameworks | AI agents]] to generate correct outputs more independently, reducing the need for intermediate "nodes" handling entire tool functions <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Tools for Prompt Generation
Custom GPTs can be used to generate prompt templates based on user input, providing a structured outline for various AI actions like email management <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a> <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. While these generators provide a solid structure, users still need to add specific details and examples to tailor the prompt for their exact needs <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.