---
title: Advanced features and use cases of AI for startups
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Joe Moa, co-founder and CEO of CrewAI, discusses how AI agents can be utilized by [[young_entrepreneurs_in_ai_startups | startups]] and [[business_opportunities_using_ai_technologies | businesses]] to automate processes and scale operations <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The session aims to provide practical skills in building and orchestrating AI agents using CrewAI, enabling users to deploy them in production environments <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The core incentive is to empower individuals and small teams to build agents that work for them, effectively creating an "army of agents" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Core Concepts of AI Agents and CrewAI

AI agents, as discussed, are designed to "impersonate roles," influencing their behavior and output <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. For instance, instructing a model to "behave as an FCC-proven stock analyst" will yield a different response than a general assessment <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

CrewAI allows for orchestration of multiple agents and tasks, where a single agent can perform multiple tasks <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

### Choosing AI Models

When selecting AI models for specific tasks, a general guideline is that smaller models (e.g., 7B, 14B) may take longer and explore "blind alleys," whereas models like GPT-4o mini often perform well <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. CrewAI provides a testing feature, `crewai test`, which allows users to evaluate different models locally based on task scores, overall crew score, and execution time <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>, <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This helps in understanding how each model performs and identifying potential trade-offs between quality and speed <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>, <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

## Practical Applications for Startups

### Lead Enrichment and Email Drafting

A fundamental use case for [[business_opportunities_using_ai_technologies | AI in startups]] is automating marketing and sales processes <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. AI agents can perform lead enrichment, automatically finding information about a lead, identifying if they fit the Ideal Customer Profile (ICP), and assessing if their company is a good match <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Beyond just gathering data, agents can generate ideas on how the product can be used by the lead and then draft personalized outreach emails <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Custom PDF Report Generation

Taking automation a step further, AI agents can generate custom PDF reports for leads <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. This process, typically handled by a junior marketing person or designer, can be automated to produce highly customized reports specific to a company, including their logos and tailored information <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>, <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>, <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. The goal is to create "lead materials that they would like to show in a meeting," empowering the customer's champion <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>, <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>. This involves:
*   Generating HTML templates with dynamic content <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
*   Ensuring agents output structured data (e.g., Pydantic objects or JSON) for programmatic use <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>.
*   Using after-kickoff hooks to interpolate variables into the HTML and convert it to PDF <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>, <a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a>.

### Building and Deployment (No-Code, CLI, & Integrations)

Users can choose between a no-code UI (Crew Studio) or a command-line interface (CLI) to build their AI agent workflows <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Crew Studio:** Allows users to chat their way into an automation <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **CLI:** For more technical users, `crewai create` command prompts for provider and model preferences <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Deployment:** Workflows can be deployed as APIs, allowing integration with other applications like Zapier and HubSpot <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>, <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. An example integration with Webflow for lead capture and Resend for email delivery is demonstrated <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>, <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.

## Advanced Concepts: Flows and Multi-Crew Orchestration

Flows represent a more complex, event-based automation system that can contain multiple crews (groups of agents and tasks) <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>, <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>. They enable complex sequences where one function can trigger another, allowing for validation of outputs and conditional execution of different crews <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>.

### Use Cases for Flows: Long-Form Content Generation

A prominent use case for flows is [[creating_ai_employees_for_startups | generating long-form documents]] like crash course PDFs <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>. This involves:
1.  **Gathering User Input:** A function collects information such as topic, learning style, and interests <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>.
2.  **Content Plan Generation:** A crew generates a comprehensive plan with chapters and their structure <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.
3.  **Chapter Generation:** Another crew writes each chapter in a loop, utilizing the structured plan and potentially external tools for research <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>, <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>.
4.  **Content Saving:** The generated content (e.g., as Markdown files) is saved <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

Flows can also visually represent their structure using `crewai flow plot`, which aids in understanding complex automations and serves as documentation <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>, <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>.

### Real-World Example: AWS Monitoring

Another [[practical_applications_of_voice_ai_in_startups | advanced application]] is building a crew to monitor AWS (Amazon Web Services) environments <a class="yt-timestamp" data-t="01:38:55">[01:38:55]</a>. This agent can produce detailed markdown reports including an executive summary, table of contents, detailed analysis, and even embed valid, non-hallucinated links to resources <a class="yt-timestamp" data-t="01:39:07">[01:39:07]</a>, <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>.

## Getting Started

For individuals looking to dive into building AI agents, checking out courses on deeplearning.ai (such as those by Andrew Ng and Joe Moa) is highly recommended. These courses cover foundational concepts of AI agents, tools, and LLMs, and also showcase practical applications by companies like PWC <a class="yt-timestamp" data-t="01:41:06">[01:41:06]</a>, <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>. The prevailing advice is to simply start learning and using these tools, as proficiency in AI will be beneficial regardless of future market dynamics <a class="yt-timestamp" data-t="01:39:02">[01:39:02]</a>, <a class="yt-timestamp" data-t="01:39:12">[01:39:12]</a>. While the initial setup can be fast, optimizing for precision and consistency still requires a traditional, iterative coding approach <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>.