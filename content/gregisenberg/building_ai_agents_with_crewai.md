---
title: Building AI agents with CrewAI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

CrewAI is a leading platform for [[ai_agents_and_automation | building and orchestrating AI agents]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It allows users to understand what AI agents are, how to orchestrate them, and even [[deploying_ai_agents_in_production | deploy them into a production environment]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The platform empowers individuals and businesses, including solo entrepreneurs and small businesses, to [[creating_ai_employees | build agents]] that can perform work, effectively creating an "army of Agents" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. CrewAI itself has leveraged AI agents to scale its own operations, providing an "Inception-like experience" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Core Concepts & Capabilities

### What are AI Agents?
AI agents are autonomous entities that can perform tasks, research, analyze information, and interact with tools to achieve specific goals <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. In CrewAI, agents can impersonate roles, with different roles influencing their behavior and outputs <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Use Cases for AI Agents
AI agents are particularly effective for automating processes and scaling operations <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Examples include:
*   **Data Enrichment and Sales/Marketing Automation** <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>:
    *   Automating lead enrichment by finding information about a person and company <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Identifying if a lead matches an Ideal Customer Profile (ICP) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Generating product usage ideas based on lead information <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    *   Drafting personalized outreach emails <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Reporting and Document Generation**:
    *   Producing real-time reports and generating PDFs <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Creating custom PDF reports that are "more fancy" and drafted specifically for a company, including company logos and tailored content <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This can automate tasks typically handled by junior marketing personnel <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.
    *   Generating long-form documents like crash course PDFs with multiple chapters <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>.
*   **Operational Monitoring**:
    *   Monitoring AWS (Amazon Web Services) for security and compliance, producing detailed markdown reports with executive summaries and risk assessments <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>.

## Building AI Agents with CrewAI

CrewAI offers both no-code/low-code and code-based methods for [[building_apps_using_ai_tools | building apps using AI tools]].

### Crew Studio (No-Code/Low-Code)
Crew Studio, available on CrewAI Enterprise's free tier, allows users to [[building_automated_businesses_with_ai | create AI agents by chatting]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Users can define the crew's objective, inputs (e.g., name, email, company domain), desired outputs (e.g., fully crafted email), and suggest tools (e.g., Serper, Scrape Website) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Crew Studio suggests agents (e.g., Researching, Analysis, Email Drafting) and tasks <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   It generates the underlying code, which can be downloaded or deployed directly <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### CLI (Code-Based)
For more custom development, users can use the CrewAI CLI:
*   `creai create <crew_name>` generates a local crew, prompting for details like the AI provider (e.g., OpenAI) and the default model (e.g., GPT-4o mini) <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>. Individual models can be specified per agent later <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>.
*   The generated code allows for inspection and further customization <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>.

### Model Selection
Choosing the right model is crucial for [[designing_and_optimizing_ai_tasks_and_agents | optimizing AI tasks and agents]] <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.
*   Smaller models (e.g., 7B, 14B) may work as agents but often take longer and can explore "blind alleys" <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>.
*   GPT-4o mini is a recommended starting point <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>.
*   The chosen model can influence agent behavior; for example, defining an agent as a "senior email content specialist" can lead to different outputs compared to a generic role <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.

### Testing and Optimization
CrewAI provides tools for testing and optimizing agent performance:
*   **`crewai test`**: This feature allows users to test agents with various models (e.g., GPT-4, GPT-4o mini, Sonnet) and get metrics like quality score, hallucination score, and execution time for each task and the overall crew <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>.
*   On the Enterprise side, there's a visual comparison tool for models <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>.
*   Optimizing agents involves iterating on prompts, agents, and tasks <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>. It's recommended to get a basic version working first, then refine it <a class="yt-timestamp" data-t="01:44:50">[01:44:50]</a>.
*   For precision, particularly in complex use cases, users can leverage Python files to add checks, create Pydantic objects for structured data, and implement guard rails <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>.

### Deployment and Integration
Once built, crews can be deployed and integrated with other services:
*   Deployed crews function as APIs <a class="yt-timestamp" data-t="01:44:43">[01:44:43]</a>.
*   Integrations are available for platforms like Zapier, HubSpot, and Slack <a class="yt-timestamp" data-t="01:52:48">[01:52:48]</a>. This allows for triggering crews from web forms or other events <a class="yt-timestamp" data-t="01:54:09">[01:54:09]</a>.
*   Users can export a React component for a UI <a class="yt-timestamp" data-t="01:57:48">[01:57:48]</a>.
*   Deployment can be managed via GitHub integration <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

## Advanced Concepts: Flows

Flows in CrewAI enable more complex, event-based automation by orchestrating multiple crews <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>.
*   Flows are created using `creai create flow <flow_name>` <a class="yt-timestamp" data-t="01:51:03">[01:51:03]</a>.
*   A flow can contain multiple crews within a `crews` folder <a class="yt-timestamp" data-t="01:54:40">[01:54:40]</a>.
*   They operate on an event-based system with a `start` function and other functions listening for specific events <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.
*   Flows allow for sophisticated logic, such as performing validation on output or conditionally calling other crews based on results <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>.
*   A visual representation of the flow's structure can be generated using `crewai flow plot` <a class="yt-timestamp" data-t="02:02:22">[02:02:22]</a>.

### Example: Educational Content Flow
A complex use case for flows is [[use_of_ai_agents_and_workflows_in_marketing | generating educational content]] <a class="yt-timestamp" data-t="02:52:49">[02:52:49]</a>, such as a crash course PDF <a class="yt-timestamp" data-t="02:53:30">[02:53:30]</a>:
1.  **Gather User Input**: A function gathers inputs like the topic, learning style, and interests <a class="yt-timestamp" data-t="02:56:55">[02:56:55]</a>.
2.  **Generate Content Plan**: A crew takes the user input and generates a plan with chapters and their structure <a class="yt-timestamp" data-t="02:58:19">[02:58:19]</a>. This output is a structured Pydantic object <a class="yt-timestamp" data-t="03:00:03">[03:00:03]</a>.
3.  **Generate Content**: Another crew then loops through each chapter from the plan to write the content <a class="yt-timestamp" data-t="03:01:08">[03:01:08]</a>. This crew can utilize tools like Serper and scraping for research <a class="yt-timestamp" data-t="03:13:12">[03:13:12]</a>.
    *   Agents involved may include a content researcher, technical writer, and educational content writer <a class="yt-timestamp" data-t="03:18:18">[03:18:18]</a>.
    *   The output for each chapter can be a markdown file <a class="yt-timestamp" data-t="03:11:59">[03:11:59]</a>.
4.  **Save Content**: Functions can save the generated content, for example, as JSON or markdown files <a class="yt-timestamp" data-t="03:01:56">[03:01:56]</a>.

## Getting Started
To dive deeper, users are recommended to check out courses available on DeepLearning.AI, which cover topics from an introduction to AI agents and tools to practical applications in companies <a class="yt-timestamp" data-t="03:06:07">[03:06:07]</a>.