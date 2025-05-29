---
title: Building AI Agents with CrewAI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Joe MOA, co-founder and CEO of CrewAI, discusses [[creating_and_customizing_ai_agents_for_specific_use_cases | building and customizing AI agents]] using the CrewAI platform. The session aims to provide tangible skills for users to understand, orchestrate, and deploy AI agents for various applications <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## Learning Objectives
By the end of the session, participants should be able to fully understand AI agents, how to orchestrate them using CrewAI, and even deploy them into a production environment using CrewAI's free tier <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The goal is to empower individuals, including solo entrepreneurs and small businesses, to [[building_businesses_around_ai_agents | build AI agents]] that work for them like an "army of agents" <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## Key Concepts of CrewAI

### What are AI Agents?
AI agents are autonomous entities that can perform tasks, research, analyze, and even draft communications, often working in teams to achieve a goal <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

### CrewAI Platform
CrewAI is an AI agent platform designed to orchestrate multiple AI agents to work together on complex tasks <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. It allows for defining agents, assigning tasks, and managing their interactions.

## Practical Applications of AI Agents

### Lead Enrichment and Outreach
One practical use case involves automating lead enrichment:
*   Given a lead, agents can find information about the person and company <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   The system can automatically write and send personalized emails <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   It can assess if a lead matches an Ideal Customer Profile (ICP) and if the company is a good match <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   Agents can generate ideas on how a product can be used by the lead based on their learned profile <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

### Custom Report Generation
AI agents can generate custom PDF reports that are more sophisticated and tailored than simple emails <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. This can automate tasks typically handled by junior marketing or design personnel <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. These reports can include company logos and be designed to serve as "champion materials" for leads to share internally <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

### Long-Form Content Creation (Educational Content)
Flows in CrewAI can be used for generating long-form documents, such as crash course PDFs with multiple chapters <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. This involves:
*   Gathering user inputs (topic, learning style, interests) <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.
*   A crew generating a comprehensive plan with chapters <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
*   Another crew writing each chapter in a loop, based on the plan <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
*   Saving the content as Markdown files <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

### AWS Monitoring Reports
CrewAI can be used to monitor AWS environments and produce detailed markdown reports, including executive summaries, tables of contents, and linked resources. This level of detail and accuracy requires careful configuration and guard rails to prevent hallucinations <a class="yt-timestamp" data-t="01:38:50">[01:38:50]</a>.

## Building with CrewAI

### Crew Studio (No-Code/UI)
Crew Studio, available on CrewAI Enterprise (with a free tier), allows users to [[building_powerful_no_code_ai_workflows | create AI agents by chatting]] and define their automation process <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. It provides a visual interface for tasks and agents <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>.

### Command Line Interface (CLI)
For more custom and local development, CrewAI offers a CLI:
*   `creai create [name_of_your_crew]`: Initiates a new crew, asking questions about providers (e.g., OpenAI) and models <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
*   `creai test`: Allows testing agents with different models locally to evaluate quality and hallucination scores <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.

### Agent Configuration
*   **Roles and Seniority:** Defining roles like "Senior Email Content Specialist" can influence agent behavior and output <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **Task Assignment:** In CrewAI, it's not a one-to-one relationship between agents and tasks; multiple tasks can be assigned to one agent, or multiple agents can contribute to a complex workflow <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Choosing Models:** GPT-4o Mini is often a good starting point for general agent behavior <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. Larger models might offer better quality but take longer to execute <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>.
*   **Tools:** Agents can be equipped with tools like Serper (for internet search) and Scrape Website (for web scraping) to gather information <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

### Deployment
Crews built using the UI or CLI can be deployed. The Enterprise version makes the crew available as an API <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>. GitHub integration allows for direct deployment from repositories <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>.

## Integrations

### Zapier
CrewAI integrates with Zapier, allowing it to connect with various apps. For instance, a Webflow form submission can trigger a CrewAI process via a webhook, and the resulting output can be used to send an email via Resend <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>.

### Resend (Email Service)
Resend is used for sending transactional emails, enabling automated outreach based on AI agent outputs <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.

### PDF.co (HTML to PDF Conversion)
For generating custom PDF reports, services like PDF.co can convert HTML output from CrewAI agents into PDF format <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.

## Advanced Concepts

### Structured Output (Pydantic/JSON)
For tasks requiring precise and programmatic data, agents can be configured to output structured data, such as Pydantic objects or JSON, ensuring consistency and usability <a class="yt-timestamp" data-t="36:55:00">[36:55:00]</a>.

### Hooks
CrewAI supports "hooks" which are functions that run at specific points in the execution flow. An "after kickoff" hook can process the crew's output, such as interpolating data into an HTML template for a PDF <a class="yt-timestamp" data-t="47:20:00">[47:20:00]</a>.

### Flows
Flows represent a more complex and event-based automation system within CrewAI <a class="yt-timestamp" data-t="50:24:00">[50:24:00]</a>.
*   **Event-Based Automation:** Flows allow chaining multiple crews and custom Python functions based on emitted events <a class="yt-timestamp" data-t="51:49:00">[51:49:00]</a>.
*   **Structure:** A flow has a `start` function and other functions that "listen" for previous functions to complete, enabling sequential or parallel execution of tasks and crews <a class="yt-timestamp" data-t="51:59:00">[51:59:00]</a>.
*   **Visualizing Flows:** The `creai flow plot` command generates a visual representation of the flow, aiding in understanding and documenting complex processes <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.
*   **Use Cases:** Flows are ideal for scenarios like generating long-form documents where different parts of the content are created by different agents or crews <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

## Tips for Building
*   **Start Simple, Iterate:** Begin with a basic version of the AI agent and continuously refine it based on testing and desired outcomes <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   **Prompt Optimization:** Significant effort should be invested in crafting and optimizing prompts to ensure agents produce the desired behavior and output <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
*   **Leverage Tools:** Integrating tools like search and scraping capabilities allows agents to access up-to-date external information beyond their internal knowledge <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Learning Resources
For those looking to dive deeper into [[building_and_deploying_ai_agents_for_business_tasks | building and deploying AI agents]], CrewAI recommends courses on DeepLearning.AI with Andrew Ng <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. These courses cover foundational concepts of AI agents and practical applications seen in companies, including how PwC uses CrewAI in production <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.