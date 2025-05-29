---
title: Creating AI employees for startups
videoId: RHXb92PAIa0
---

From: [[gregisenberg]] <br/> 

The Lindy platform allows users to create thousands of AI employees (referred to as "Lindies") that can help [[building_a_startup_using_ai_tools | build a startup]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This approach makes businesses more efficient and enables faster growth <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Benefits of AI Employees (Lindies)

Utilizing AI employees offers several significant advantages:
*   **Efficiency and Growth** Lindies make a business more efficient and enable faster growth <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Scalability** They are easy to spin up, require no human management, and scale infinitely with demand, scaling down when not in use <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This "elastic" nature is similar to serverless cloud computing <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>.
*   **Continuous Improvement** AI employees continuously improve <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Intelligence over Automation** Unlike simple automations (like Zapier), Lindy agents possess intelligence and maintain context across tasks <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   **AI Prompts Anywhere** AI can be used at any point in Lindy workflows, allowing users to extract data or make decisions using natural language prompts without needing to manually inject data from previous steps <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This allows for complex actions like parsing email content by simply "speaking to the agent" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   **Long-Term Task Management** Lindy agents manage long-term tasks and time horizons, maintaining context throughout conversations (e.g., via email or Slack) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This enables follow-up questions and ongoing coaching within a thread <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

The future of business may involve setting up a team of 5,000 AI employees in a weekend <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Getting Started with Lindy

While there's a learning curve, resources like the Lindy Academy and available templates can help users get started <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. It's recommended to start with regular Lindy agents before graduating to Lindy-to-Lindy communication <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.

### Building a Lindy: Urgent Email Catcher Example

To create a Lindy that pings a user on Slack for urgent emails <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>:
1.  **Set a Trigger**: Use "Gmail" as the trigger for "when I receive an email" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
2.  **Add a Condition**: Create a natural language condition, such as "go down this path if this email is urgent and time sensitive" <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. The AI (e.g., Cloud 3.5 Sonnet) evaluates the email to determine its urgency <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
3.  **Define an Action**: Use Slack to "send me a direct message" <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
4.  **Prompt the Message**: Provide a prompt like "send me a message about this time sensitive email I just received with context about it" <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. The Lindy is aware of all previous steps and context <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
5.  **Enable Reply (AI Agent)**: To allow two-way communication, add an "after reply received" branch and incorporate an AI agent <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
    *   Unlike simple steps, an AI agent is given a prompt for guidance and "skills" (actions it can invoke) and figures out how to achieve its goal <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   For example, giving it the skills to "reply to the email" and "create a calendar event" allows it to respond and schedule based on follow-up instructions <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>, <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.

### Lindy-to-Lindy Communication (Advanced)

Lindies can communicate and work together, similar to object-oriented programming for agents <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>, <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

**Example: Proposal Generation**
1.  **Create a "Proposal Writer Lindy"**: This Lindy's trigger is "being summoned by another Lindy" (an agent message received) <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
2.  **Define Proposal Creation**: Its action is to create a Google Doc with a proposal <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. The prompt for content can be natural language, e.g., "write a proposal using the instructions that were given to you" <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
3.  **Callback to Summoning Agent**: The Proposal Writer Lindy is instructed to "tell the agent you're done and send it the link to the proposal you just created" <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
4.  **Delegate from "Time Sensitive Email Catcher"**: The "Time Sensitive Email Catcher" Lindy can then delegate the task of writing a proposal to the "Proposal Writer Lindy" based on an email request <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
    *   This delegation can be set as an exit condition, giving more control over parameters passed to the summoned agent <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.
    *   The primary Lindy will wait for the reply from the Proposal Writer and then act on it (e.g., sending the proposal via email) <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.

## Practical Use Cases for AI Employees

*   **Meeting Recorder & Coach**: A Lindy can join, record, and summarize meetings, creating Google Docs notes, sending them via Slack, and even providing coaching notes based on a custom prompt (e.g., "was I too confrontational?") <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Meeting Scheduler**: An AI agent can look at your calendar, suggest available times, and manage rescheduling by deleting old events and creating new ones based on conversation context <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.
*   **Data Extraction & Logging**: A Lindy can extract specific information from emails (e.g., reservation details, amounts) and append it to a Google Sheet <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Customer Support**: An e-commerce business uses Lindy as a customer support agent, handling thousands of tickets per day by scaling dynamically to meet demand, especially during peak times like Black Friday <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>.
*   **Recruiting & Lead Generation**:
    *   A Lindy can act as a "designer recruiter," taking various inputs (Twitter links, websites, names) and searching for associated email addresses, even understanding obfuscated email formats (e.g., "name at gmail") <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>. It can then send outreach emails and follow up with reminders <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
    *   A "lead generator Lindy" can find specific types of professionals (e.g., product designers at Zapier), add them to a Google Sheet, and even find personal email addresses if available <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. This can then be delegated to the "designer recruiter" Lindy to initiate outreach <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.

## [[ai_startups_and_entrepreneurship | Building a Business]] Around AI Employees

The ability to create an army of AI recruiters or other specialized agents means a company could scale infinitely with minimal human staff, essentially becoming an autonomous company <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This presents an [[opportunities_in_ai_design_for_startups | arbitrage opportunity]] because not everyone is currently leveraging these capabilities <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.

To start [[building_and_launching_an_ai_saas_business | building a business]] or automating tasks with Lindy, users can focus on identifying repetitive "jobs to be done" <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.

## Accessing Lindy

Users can sign up for Lindy at Lindy.ai <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>. A 7-day free trial is available, though payment information is required to sign up <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>.