---
title: Generating Custom Reports and PDFs Using AI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Joe Moa, co-founder and CEO of CrewAI, demonstrated how to build AI agents to generate custom reports and PDFs, showcasing the platform's capabilities for [[utilizing_ai_for_scaling_and_automation | scaling and automation]] in businesses <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## What are AI Agents?
AI agents are autonomous programs that can perform tasks, make decisions, and interact with environments to achieve specific goals <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. CrewAI is described as a leading platform for orchestrating and deploying these agents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The goal is to enable individuals and businesses, including solo entrepreneurs, to build an "army of agents" to perform work automatically <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Core Capabilities and Tangible Skills
By the end of the demonstration, users should be able to:
*   Fully understand what AI agents are <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Orchestrate them using CrewAI <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Deploy them into a production environment <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Build AI agents for themselves and automate processes <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Automating Sales & Marketing with AI Agents

A primary use case for AI agents is [[creating_automated_marketing_and_sales_processes_with_ai | automating marketing and sales processes]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Specifically, agents can perform lead enrichment, learning more about a person and company from a new lead <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Lead Enrichment and Email Drafting
The process involves agents:
1.  **Researching**: Gathering information about a person (role, seniority) and company (size, industry, culture) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Idea Generation**: Brainstorming three actionable ideas on how the lead could use the product <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **Email Drafting**: Creating a personalized, friendly email incorporating the learned information and product ideas <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

This process aims to determine if a lead fits the Ideal Customer Profile (ICP) and is worth pursuing <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Building the Agent Crew
Agents can be built using CrewAI's:
*   **Crew Studio (No-Code)**: A UI that allows users to create AI agents by chatting their way into an automation <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. It suggests tools, agents, and tasks based on the prompt <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **CLI (Code-based)**: For more custom and complex implementations, allowing local creation and testing of crews <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

A "crew" is a collection of agents working together, where one agent can perform multiple tasks <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For the lead enrichment example, agents might include a "profile researcher," an "idea generation specialist," and an "email content specialist" <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### Model Selection and Testing
Choosing the right AI model is crucial <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Generally:
*   **GPT-4o Mini** is a good go-to for many tasks <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   Smaller models (e.g., 7B, 14B) can be slower and less effective <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   Larger models might offer better quality but take longer <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

CrewAI includes a `crewAI test` feature to evaluate different models locally, providing quality and hallucination scores for each task <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>, <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Defining agent roles (e.g., "senior email content specialist") can also influence the output behavior <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Integration with External Tools
CrewAI Enterprise offers integrations with platforms like:
*   **Zapier**: To connect crews to webhooks from other applications (e.g., Webflow forms) <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>, <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **HubSpot / Slack**: For CRM integration and communication <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>, <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Resend**: For sending transactional emails with analytics <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.
*   **PDF.co**: A service to convert HTML to PDF dynamically <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.

## Generating Custom PDF Reports
Beyond just emails, AI agents can [[creating_and_optimizing_marketing_content_using_ai | create and optimize marketing content]] like custom PDF reports <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This automates tasks typically performed by junior marketing or design personnel <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>, potentially saving significant costs <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>.

### Process for PDF Generation
1.  **Structured Output**: Agents need to output structured data (e.g., Pydantic objects or JSON) containing all necessary information for the report (title, sections, ideas) <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>, <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.
2.  **HTML Template**: An HTML template, potentially generated by a large language model like ChatGPT <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>, serves as the base for the report. This allows for dynamic content interpolation <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
3.  **Dynamic Content**: The structured data from the agents is then interpolated into the HTML template <a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a>.
4.  **PDF Conversion**: The fully populated HTML is converted into a PDF, which can then be attached to an email <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>, <a class="yt-timestamp" data-t="01:22:03">[01:22:03]</a>.

This method allows for high-quality, custom reports that can include company logos and specific details, making the material highly valuable for the recipient <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>, <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. It's a prime example of [[creating_art_and_branding_with_ai | creating art and branding with AI]].

## Advanced AI Agent Orchestration: Flows
For more complex, event-driven automation, CrewAI offers "flows" <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. Flows allow for sequences of operations, where functions can listen for other functions to finish, and multiple crews can be chained together <a class="yt-timestamp" data-t="00:51:49">[00:51:49]</a>, <a class="yt-timestamp" data-t="00:52:02">[00:52:02]</a>.

### Use Cases for Flows
*   **Long-form Document Generation**: A flow can gather user inputs (topic, learning style, interests), then generate a content plan using one crew, and subsequently use another crew to write each chapter in a loop, resulting in a multi-page PDF or crash course <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>, <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>. This is a practical application of [[building_ai_tools_for_infographic_and_content_generation | building AI tools for infographic and content generation]].
*   **AWS Monitoring Reports**: A crew can monitor AWS services and generate a detailed markdown report, including an executive summary, table of contents, and linked analysis, with guard rails to prevent hallucinations in links <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>, <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>. This demonstrates [[using_ai_for_professional_services_automation | professional services automation with AI]].

### Visualizing Flows
CrewAI provides `crewAI flow plot`, which generates a visual representation of the flow, showing the sequence of functions, events, and crews involved. This enhances understanding and documentation of complex automation <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>, <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>.

## Iterative Development and Learning
The process of building AI agents is iterative <a class="yt-timestamp" data-t="01:45:55">[01:45:55]</a>. It's recommended to:
*   Start simple to get a basic working model <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
*   Progressively tweak and optimize the prompts, agents, and tasks for better precision and specific behaviors <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>, <a class="yt-timestamp" data-t="01:37:56">[01:37:56]</a>.
*   Add more complex features like structured outputs and flows as needed <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.

AI tools make the "zero to one" stage of development very fast, while optimization from "one to ten" still requires traditional refinement <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>.

For those looking to dive deeper into AI agents, Joe Moa recommends checking out courses by Andrew Ng on DeepLearning.AI, which cover everything from introductions to practical applications in companies <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>.