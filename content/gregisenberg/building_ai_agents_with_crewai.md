---
title: Building AI agents with CrewAI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

CrewAI is described as a leading platform for [[replacing_traditional_workflows_with_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The platform allows users to fully understand what [[replacing_traditional_workflows_with_ai_agents | AI agents]] are, how to orchestrate them, and even [[deploying_ai_agents_in_production_environments | deploy them into a production environment]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The goal is to empower individuals and businesses, including solo entrepreneurs and those with employees, to leverage an "army of agents" to automate tasks <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Core Concepts & Capabilities
At its core, CrewAI enables the orchestration of multiple AI agents to collaboratively complete tasks <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This approach is beneficial for scaling operations, even for an [[building_an_ai_startup_workflow | AI agent company]] itself <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The platform supports structured and programmatic outputs, allowing for high precision and consistency in use cases <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>.

### Choosing AI Models
When selecting AI models for tasks, smaller models (e.g., 7B, 14B) generally do not perform as well as agents and can take longer due to exploring "blind alleys" <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. A recommended starting point is GPT-4o mini, which typically performs well <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. CrewAI offers a `crew AI test` feature that allows users to evaluate how different models (e.g., GPT-4, GPT-4o mini) perform on specific tasks, providing quality and hallucination scores, as well as execution time <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

### Defining Agent Roles
Assigning specific roles to agents can significantly influence their behavior and outputs <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. For example, asking an AI to "behave as an FCC-proven stock analyst" will yield a completely different answer than a general assessment, even with the same prompt <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This steering mechanism helps in achieving desired outcomes <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

## Practical Application: Lead Enrichment Workflow

A straightforward use case for [[utilizing_ai_agents_to_automate_business_tasks | AI agents]] is lead enrichment, particularly for sales and marketing <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Workflow Goal
The objective is to automatically:
1.  **Research** a person and company (role, seniority, company size, industry, culture) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
2.  **Determine** if they fit the ideal customer profile (ICP) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
3.  **Generate ideas** on how they can use a product <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
4.  **Draft a personalized email** for outreach <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Building with Crew Studio (No-Code)
Crew Studio, accessible via CrewAI Enterprise's free tier, allows [[building_and_deploying_apps_with_ai_integration | creating AI agents by chatting]] <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
The process involves:
*   **Defining inputs**: Name, email, company domain <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Suggesting tools**: Serper (for search), Scrape Website, and GPT-3 (though GPT-3 was later removed in the example) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Defining agents**: Research agent, Analysis agent, Email Drafting agent <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Defining tasks**: Researching person, researching company (both by research agent), generating ideas (by analysis agent), drafting email (by email agent) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The Studio can generate the underlying code for download or allow direct deployment <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. Users can also create crews locally using the open-source `crei create` command <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Deployment and Integrations
Deployed crews become APIs, enabling integration with other applications like Zapier, HubSpot, and Slack <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

#### Webflow and Zapier Integration Example
A demonstration showed integrating the lead enrichment crew with a Webflow form using Zapier <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>:
1.  A Webflow form captures name, email, and company domain <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
2.  Zapier is set up with a webhook to receive form submissions <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.
3.  A "Kick off a Crew" action in Zapier triggers the CrewAI agent with the collected data <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
4.  Resend (an email service) is used to send the drafted email, with the CrewAI output as the email body <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

#### Custom PDF Reports
Instead of just sending an email, agents can generate custom PDF reports that are more specific and tailored to a company <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>. This can replace the manual work of a junior marketing person <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
*   **Template Creation**: HTML templates (e.g., generated by ChatGPT) can be used <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>.
*   **Dynamic Content**: The HTML content is made dynamic by interpolating variables from the agent's output <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   **Structured Output**: Agents are configured to output structured data (e.g., Pydantic objects or JSON) instead of plain text, which is crucial for programmatic use <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.
*   **Post-processing**: An `after kickoff` hook can be implemented to take the structured output, interpolate it into the HTML template, and then convert it to a PDF using a service like PDF.co <a class="yt-timestamp" data-t="01:21:51">[01:21:51]</a>.

## Advanced Workflows: CrewAI Flows
For more complex scenarios, CrewAI introduces "Flows," an event-based automation system that can contain multiple crews <a class="yt-timestamp" data-t="00:51:28">[00:51:28]</a>. This allows for conditional execution, validation of outputs, and integration with various data sources like SAP and Salesforce <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.

### Building an Educational Content Flow
An example of a complex flow is generating long-form educational documents, such as a crash course PDF <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.
1.  **Gather User Input**: A function gathers inputs like topic, learning style, and interests <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.
2.  **Generate Content Plan**: A "Content Plan Crew" generates a structured plan with chapters, descriptions, and learning activities <a class="yt-timestamp" data-t="00:53:41">[00:53:41]</a>. This crew can utilize tools like Serper and Scraping for research <a class="yt-timestamp" data-t="01:14:59">[01:14:59]</a>.
3.  **Save Content Plan**: The plan can be saved as a JSON file <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.
4.  **Generate Content**: A "Content Creator Crew" iterates through each chapter from the plan to write the actual content in markdown format <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>. This process runs in a loop, generating individual markdown files for each chapter <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>.

### Visualizing Flows
CrewAI provides a `crei flow plot` command to generate a visual representation of the flow, showing the crews, functions, and event dependencies. This helps in understanding and documenting complex workflows <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>.

> [01:03:30] "I'm like this this this is what I need you know I needed this. I'm going to say it does helps with like this more complex flows because like, uh again you even if you crack it and you get the hangout of in you're still working on the team sometimes there's beaing this so the more visual that you can get for people to just like wrap their heads around what's happening, the better and the easier it is for you to kind of like build the more complex flows like this one."

## Optimization and Learning
While [[replacing_traditional_workflows_with_ai_agents | AI agents]] can accelerate development from zero to one, optimizing performance (one to ten) still requires traditional coding practices and iteration <a class="yt-timestamp" data-t="01:28:32">[01:28:32]</a>.
*   **Iterative Development**: It's recommended to start with a basic functional output and then spend time tweaking and learning to make it more advanced <a class="yt-timestamp" data-t="00:44:55">[00:44:55]</a>.
*   **Prompt Optimization**: Significant optimization occurs by carefully defining agent prompts and tasks in YAML files to ensure desired behavior <a class="yt-timestamp" data-t="01:38:11">[01:38:11]</a>.
*   **Precision with Python**: For higher precision, developers can add checks, create Pydantic objects, and implement guard rails within Python files <a class="yt-timestamp" data-t="01:38:22">[01:38:22]</a>.

> For example, an AWS monitoring crew was built to produce detailed markdown reports with executive summaries, detailed analyses, and even valid, non-hallucinated links by adding guard rails <a class="yt-timestamp" data-t="01:39:13">[01:39:13]</a>.

### Recommended Learning Resources
For those looking to get started, Joe Moa recommends checking out a couple of courses with Andrew Yang on Deep Learning AI <a class="yt-timestamp" data-t="01:41:12">[01:41:12]</a>. The first course provides a beginner-friendly introduction to agents, tools, and LLMs, while the second focuses on practical company applications and includes an interview on how PWC is [[deploying_ai_agents_in_production_environments | using CrewAI in production]] <a class="yt-timestamp" data-t="01:41:43">[01:41:43]</a>. Over 100,000 people have enrolled in these courses <a class="yt-timestamp" data-t="01:42:02">[01:42:02]</a>.