---
title: Understanding AI Agent Output and Examples
videoId: d_R77Pe-VEo
---

From: [[customaistudio]] <br/> 

[[Building Efficient AI Agents with Prompts | Prompt engineering]] is the process of telling an AI agent what to do, who it is, and how to do it, effectively giving it instructions and context to achieve a desired output <a class="yt-timestamp" data-t="08:10:13">[08:10:13]</a>. While the term is often overused, there is merit to understanding and applying its principles to achieve reliable AI agent performance <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

## How AI Agents Generate Output

AI agents process input and generate output based on the instructions provided in their prompts. This output often needs to be in a specific format, such as a JSON package, to be utilized by subsequent tools or nodes in an automation workflow <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. For instance, the system prompt tells the agent exactly what to do and ensures the output is specific, often in JSON format, containing necessary parameters like attendees and start dates <a class="yt-timestamp" data-t="05:37:16">[05:37:16]</a>.

The agent's output needs to be named "response" for the agent to receive it from a tool <a class="yt-timestamp" data-t="03:30:17">[03:30:17]</a>. After an event is created, key information is extracted and placed into a "set node" named "response," which the agent then receives, including details like success status, title, description, start/end times, and a link <a class="yt-timestamp" data-t="03:42:02">[03:42:02]</a>.

## Example: Calendar Management AI Agent

A practical example demonstrates an AI agent managing a calendar based on user input.

### User Input and Agent Processing

Consider the prompt: "create a meeting for Thursday at 500 p.m and add Andrew Lewis to it" <a class="yt-timestamp" data-t="02:32:41">[02:32:41]</a>.

To execute this, the AI agent needs to:
*   Identify Andrew Lewis's email address from a vector store (database) <a class="yt-timestamp" data-t="02:39:27">[02:39:27]</a>.
*   Calculate the correct date and time for "Thursday at 5:00 p.m.," as the underlying OpenAI GPT-4 model is trained up to 2023 and doesn't inherently know current day and time <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   Identify the required action, which is "create an event," from a switch function that handles different calendar actions (create, delete, get, update) <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>.

### Agent Output and Workflow

The agent's workflow involves several nodes:
1.  **AI Node:** Receives the chat input from the user <a class="yt-timestamp" data-t="03:00:54">[03:00:54]</a>.
2.  **Vector Store:** Checks the database to retrieve necessary information, such as Andrew Lewis's email <a class="yt-timestamp" data-t="03:02:43">[03:02:43]</a>.
3.  **Switch Function:** Identifies the precise action to take (e.g., "create an event") <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>.
4.  **Calendar Event Creation:** The event is created based on the extracted information <a class="yt-timestamp" data-t="03:17:59">[03:17:59]</a>.
5.  **Set Node:** Takes the key information outputted after the event creation and names it "response," which is then received by the agent <a class="yt-timestamp" data-t="03:19:35">[03:19:35]</a>.

The final output received by the agent includes: `success`, `title` (e.g., "Meeting" if no specific title was given), `description`, `start` and `end` times, and a `link` to the created event <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. This results in the meeting being correctly created in the calendar with the specified time and attendee <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

Another example of complex user input: "send Andrew an email asking if he has finished the project proposal for our call with John on Friday and schedule a meeting with him 30 minutes before the call with John and call it like team sync" <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. The agent needs to extract the relevant action (create a calendar event) and ignore the email-related part for the calendar tool <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Prompt Formula for Consistent Output

A robust prompt formula helps ensure consistent and reliable agent output:

*   **Objective:** Define a clear and specific overall objective for the agent. This should succinctly describe its main task or goal <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    *   *Example:* For a calendar agent, the objective is to parse user input, identify event-related information, and generate a JSON package with correct parameters for calendar operations, focusing solely on event management tasks <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.
*   **Context:** Provide comprehensive background information, including user situation, relevant databases, and other details that give the agent a better understanding of its role <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. Context can emphasize the importance of certain output formats or actions, influencing the AI's reasoning <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.
*   **Instructions:** Offer step-by-step instructions on exactly what the agent should do <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.
    *   *Example for Calendar Agent:* Identify calendar action, extract event information, retrieve information from the database (like email addresses), and generate a JSON output <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **Output Requirements:** Specify the exact format the agent should output once its work is completed, such as a JSON package, to ensure compatibility with subsequent steps in the workflow <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. The AI takes in information, identifies what needs to happen, and then outputs the data the next step requires <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.
*   **Examples:** Provide as many real-world examples as possible, including edge cases. Examples are crucial for achieving consistent output, especially when agents have significant responsibilities within a business <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.

A dedicated custom GPT can even generate prompts following this structure, providing an outline and important details for specific actions, like email actions <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. While the generated prompt provides a structure, crucial details, especially for output requirements (e.g., specific JSON structure), still need to be tailored to the specific automation needs <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.