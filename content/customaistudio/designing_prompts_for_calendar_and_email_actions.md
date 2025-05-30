---
title: Designing Prompts for Calendar and Email Actions
videoId: d_R77Pe-VEo
---

From: [[customaistudio]] <br/> 

[[introduction_to_prompt_engineering | Prompt engineering]], though often an overused term, involves the structured process of instructing an AI model or "agent" on what to do, who it is, and how to perform its tasks <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. It is akin to software engineering, but instead of writing code in a programming language, one uses natural language (English) to tell the computer or system what to do <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Proficiency in reading and writing English, especially in asking precise questions, generally leads to better results when extracting information or commanding an AI <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

This approach is crucial for [[building_efficient_ai_agents_with_prompts | building efficient AI agents]], particularly for [[integrating_ai_with_communication_tools_like_email_and_calendar | integrating AI with communication tools like email and calendar]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Calendar Management with AI Agents

A practical application of prompt engineering is seen in AI agents designed to manage calendars <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. For instance, a personal agent can be instructed to perform actions like creating meetings <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Workflow Example: Creating a Meeting

Consider the prompt: "create a meeting for Thursday at 5:00 p.m. and add Andrew Lewis to it" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The AI agent's workflow involves several steps:
1.  **AI Node Processing**: The initial prompt is sent to the AI node <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **[[data_management_and_prompt_engineering_for_ai_agents | Data Retrieval]]**: The agent consults a [[data_management_and_prompt_engineering_for_ai_agents | vector store]] (database) to retrieve necessary information, such as "Andrew Lewis's email address" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. It also needs to calculate the specific date and time for "Thursday at 5:00 p.m.," as models like GPT-4 are trained up to a certain date and don't inherently know current day/time <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **Action Identification**: A "switch function" node identifies the specific action required from the user's request (e.g., create an event, delete an event, get an event, update an event) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. In this case, "create an event" is chosen <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  **Event Creation**: The event is created, and the agent receives the output <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
5.  **Output Formatting**: A "set node" captures key information from the created event (e.g., success status, title, description, start/end times, and a link to the event) and formats it as a "response" for the agent <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This response is typically in a JSON package <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

The result is a successfully created meeting in the calendar, with the correct attendees and time <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Handling Complex Requests

AI agents can manage more complex, multi-step requests. For example: "send Andrew an email asking if he has finished the project proposal for our call with John on Friday and schedule a meeting with him 30 minutes before the call with John and call it like team sync" <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

In such a scenario, the agent would:
*   Receive the entire user message <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   Extract relevant information for each tool it needs to call (e.g., email action tool, calendar action tool) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Prioritize actions if needed, e.g., focusing on creating the calendar event first <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## The Prompt Design Formula

Effective prompt engineering for AI agents follows a structured formula to ensure consistent and reliable output <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>:

1.  **Objective**:
    *   Define a clear and specific overall objective for the agent <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   It should concisely describe the main task or goal <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   *Example for Calendar Agent*: "Your objective is to parse user input to identify and extract event related information specific to calendar operations. You must generate a JSON package with the correct parameters for each action such as creating, updating, retrieving and deleting calendar events. Your focus should be solely on event management tasks ignoring unrelated instructions" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This ensures the agent only focuses on calendar-related actions <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

2.  **Context**:
    *   Provides comprehensive background information to the agent <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Includes details about the user's situation, relevant databases, and other information that gives the agent a better understanding of its role <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   Context can be used to emphasize the importance of certain outputs (e.g., using all caps in the prompt if a specific output format is critical, or stating high stakes if the AI fails to comply) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

3.  **Instructions**:
    *   Step-by-step guidance on exactly what the agent should be doing <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   *Example for Calendar Agent*:
        1.  **Identify calendar action**: Understand the user prompt and determine the required action (e.g., create, delete) <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
        2.  **Extract event information**: Gather necessary details from the user's request <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
        3.  **Retrieve information from the database**: Look up additional data like email addresses from a database <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
        4.  **Generate a JSON output**: Format the extracted and retrieved information into a JSON package, which is necessary for subsequent nodes that execute the actual action (e.g., a Gmail node for sending an email) <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

4.  **Output Requirements**:
    *   Specifies the format and content the agent should output once the work is completed <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
    *   This is typically a JSON package, a report, or any other format required by the next step in the [[agentic_workflows_and_team_productivity | workflow]] <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. The AI identifies what needs to happen and then outputs the data in the specific format the next step needs to finish the action <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

5.  **Examples**:
    *   Provide as many real-world examples as possible, including edge cases <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
    *   Examples are key to achieving consistent output, especially when agents have significant responsibilities within a business <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   *Example Scenario*:
        *   **User Input**: "schedule a meeting with the team tomorrow at 10: a.m. the meeting should last one hour include John and Sarah in the meeting" <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
        *   **Agent Steps**:
            1.  Identify calendar action: `create an event` <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
            2.  Extract event information: `meeting with team`, `tomorrow at 10 a.m.`, `one hour duration`, `John and Sarah` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
            3.  Retrieve information from database: Verify John and Sarah's emails <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
            4.  Generate JSON output <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

## Leveraging Custom GPTs for Prompt Generation

A custom GPT can be used as a "prompt generator" to streamline the process of creating prompts <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Users can provide a high-level request, such as "give me a prompt for an AI node that will execute email actions," and the custom GPT will generate a structured prompt using the described formula (objective, context, instructions, output requirements, examples) <a class="yt-timestamp" data-t="00:14:41">[00:15:01]</a>. While the generated prompt provides a strong outline, specific details unique to the user's needs (like detailed JSON output formats) still need to be refined <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This tool simplifies the initial setup for [[agentic_prompting_and_decisionmaking_frameworks | agentic prompting]] <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.