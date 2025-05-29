---
title: Creating and using custom nodes and interfaces in automation
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gumloop, a leading AI agent and AI automation company that recently raised $9 million <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, offers features like custom nodes and interfaces to empower users to build powerful, tailored [[creating_effective_workflows_with_ai_tools | AI workflows]] and [[automating_business_processes | automate more things in their business]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. These tools extend the platform's capabilities, allowing for deep customization and simplified user interaction.

## Custom Nodes: Expanding Integration Capabilities

Custom nodes address the need for integrating with internal company data or third-party services not natively supported by the platform <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This feature allows users to build their own integrations without extensive engineering knowledge.

### How to Create a Custom Node
The process of creating a custom node involves using an AI-powered builder:
*   Users can copy and paste API documentation into the custom node builder <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
*   The AI understands the context of a Gumloop integration and can generate the necessary code, including where to input API keys <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>.
*   Users can specify inputs and outputs, and add a logo for the node <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.
*   Once created, these custom nodes are accessible to everyone in the user's workspace, enabling collaboration on custom integrations <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>. Users can also modify the code if needed <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

### Use Cases for Custom Nodes
This functionality allows semi-technical individuals within companies to build complex tools, such as:
*   Twitter scrapers <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>.
*   Blue Sky scrapers for social media analysis <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.
*   Integrations with internal development teams without needing to be a developer <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

### Future Vision for Custom Nodes
The future aims to make custom node creation even more intuitive, allowing users to simply describe the desired integration, and the AI will handle naming, icon selection, code generation, and testing, making the process seamless <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.

## Interfaces: Simplifying User Interaction

Gumloop interfaces simplify complex workflows by creating a user-friendly layer on top of them <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. This means non-technical users can interact with powerful automations without seeing the intricate flowchart of connected nodes <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### How to Create an Interface
Interfaces are built using a simple drag-and-drop UI builder <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. The result is a straightforward, "impossible to mess up" version of the application <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.

### Example: Competitor Ad Analysis Workflow
One powerful example is a competitor ad analysis workflow that can be scheduled to run automatically <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   It scrapes a competitor's Facebook ads (including Instagram and WhatsApp ads) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   AI analyzes each video ad and image to understand the company's objectives <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
*   All analyses are fed into a large AI prompt to generate an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   This analysis is formatted in HTML and sent as an email to management on a scheduled basis (e.g., every Friday morning) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   The email includes links to the ads, information about new ads in the last seven days, and insights into content type and structure <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
*   This workflow essentially creates a "junior ad assistant" <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a> at a significantly lower cost than a human employee <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>. The cost depends on the number of ads and AI queries but is dramatically reduced if users provide their own API keys <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.

### Building SaaS Products with Gumloop Interfaces
Gumloop allows users to create their own SaaS products by building workflows and exposing them via webhooks <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. This means a user could build a website, charge customers, and have Gumloop perform the backend work <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. Workflows can be triggered via API calls, enabling dynamic fields to be passed in from external forms or internal dashboards <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>. Alerts can be set up to notify users if anything goes wrong <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.

## Chrome Extension: On-Demand Workflow Execution

The Gumloop Chrome extension makes workflows accessible directly from the browser <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. A workflow can be configured to start with a Chrome extension node, allowing it to scrape content from the current screen or perform other browser actions <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

### Example: LinkedIn Profile Researcher
A LinkedIn profile researcher workflow demonstrates the power of the Chrome extension:
*   When activated, it scrapes the entire content of a LinkedIn profile <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   It extracts key data like name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
*   It summarizes the person's background, highlighting notable details relevant to a candidate search (e.g., founding engineer, founder experience) <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
*   The workflow finds the person's Twitter and GitHub profiles by using AI to look at Google search results <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   All gathered data is dumped into a Google Sheet for tracking candidates <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
*   It pings the team on Slack to notify them of a new profile <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
*   It finds their email using Apollo and drafts a basic message in the user's inbox <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.

This allows any team member, even an intern, to identify interesting candidates and have a personalized email draft ready for a founder to send <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>. The combination of the Chrome extension and custom node builder enables the creation of "infinitely powerful no-code Chrome extensions" <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.

## The Advantage of Automation

Regardless of company size, from solo entrepreneurs to large enterprises, identifying and [[automating_manual_processes_with_ai | automating manual processes with AI]] offers a significant "unfair advantage" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. If a task can be described as a list of steps, it can likely be [[automating_job_responsibilities_with_ai | automated]] <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. By automating repetitive tasks, businesses can save time and focus on high-leverage activities that truly move the needle <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>. Gumloop itself [[using_ai_for_business_automation | automates business processes]] internally, contributing to its efficiency and continuous product improvement <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.