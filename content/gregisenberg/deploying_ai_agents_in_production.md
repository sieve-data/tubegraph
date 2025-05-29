---
title: Deploying AI agents in production
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Deploying [[ai_agents_and_automation | AI agents]] in a production environment allows businesses and solo entrepreneurs to automate complex processes and scale operations. Joe MOA, Co-founder and CEO of CrewAI, demonstrates how to build, orchestrate, and deploy [[ai_agents_and_automation | AI agents]] for practical business applications using the CrewAI platform <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core Concepts of AI Agent Deployment
At the heart of [[building_ai_agents_with_crewai | building AI agents with CrewAI]] is the idea of creating an "army of Agents" to do more work for a business <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This includes tasks ranging from data enrichment to generating custom reports.

By the end of a practical session, users should be able to:
*   Understand what [[ai_agents_and_automation | AI agents]] are <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   Orchestrate them using CrewAI <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   Deploy them into a production environment, even using a free tier <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

### Initial Use Case: Lead Enrichment
A common [[use_cases_and_applications_of_ai_agents | use case]] for [[implementing_ai_agents_for_efficiency | implementing AI agents for efficiency]] is lead enrichment, which boosts marketing and sales efforts <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. The goal is to automatically learn about a lead and their company, assess if they fit the ideal customer profile, and then generate actionable follow-up <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

The process involves:
1.  **Researching the lead and company**: Gathering information such as role, seniority, company size, industry, and culture <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
2.  **Generating product usage ideas**: Creating three ideas on how the lead can use the product based on the collected data <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
3.  **Drafting an email**: Composing a friendly email with the insights and product ideas, ready to be sent <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

Inputs for this crew include the lead's name, email, and company domain <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. Agents don't necessarily have a one-to-one task ratio; one agent can handle multiple tasks <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

## Building and Testing AI Agents
CrewAI offers `Crew Studio`, a no-code interface where [[creating_ai_employees | AI agents]] can be created by simply chatting <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Alternatively, users can generate and download the Python code for more customization <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.

### Model Selection and Performance
When choosing an LLM model for agents, "smaller models" (e.g., 7B, 14B) generally "don't work as well" and can take longer due to "blind alleys" <a class="yt-timestamp" data-t="11:07:00">[01:11:07]</a>. GPT-4o Mini is a common go-to choice for good performance <a class="yt-timestamp" data-t="11:23:00">[01:11:23]</a>.

CrewAI includes a `crewai test` feature that allows users to compare different models and receive actual quality and hallucination scores, along with execution times, helping to optimize model choices <a class="yt-timestamp" data-t="11:43:00">[01:11:43]</a>.

### Impact of Agent Roles
The role assigned to an agent can significantly impact its behavior and outputs. For example, explicitly naming an agent as a "senior email content specialist" can steer the model to behave in a specific, more professional way <a class="yt-timestamp" data-t="13:17:00">[01:13:17]</a>. This is akin to role-playing with a large language model <a class="yt-timestamp" data-t="13:31:00">[01:13:31]</a>.

## Advanced Integrations and Outputs
CrewAI Enterprise provides an API for seamless integration with other applications like Zapier, HubSpot, and Slack <a class="yt-timestamp" data-t="15:43:00">[01:15:43]</a>. This allows for automated workflows, such as triggering an AI agent when a new lead signs up on a Webflow website <a class="yt-timestamp" data-t="16:45:00">[01:16:45]</a>.

### From Emails to Custom PDF Reports
While simple emails are a good starting point, [[practical_use_cases_for_ai_agents_in_business | AI agents and their applications]] can go further by generating custom PDF reports. This automates a task that typically requires a junior marketing person, saving significant costs <a class="yt-timestamp" data-t="27:43:00">[01:27:43]</a>.

Key benefits of custom PDF reports:
*   **Highly customized**: Tailored specifically to the client's company with dynamic content and company logos <a class="yt-timestamp" data-t="28:26:00">[01:28:26]</a>.
*   **High quality**: Designed to be professional enough for leads to present internally in meetings <a class="yt-timestamp" data-t="28:54:00">[01:28:54]</a>.
*   **Programmatic output**: Agents can be configured to output structured data (e.g., Pydantic objects or JSON) that can be interpolated into HTML templates and converted to PDFs using services like PDF.co <a class="yt-timestamp" data-t="36:55:00">[01:36:55]</a>.

### Using Hooks for Post-Processing
CrewAI allows the use of `after_kickoff` hooks, which are functions that run automatically after a crew completes its tasks <a class="yt-timestamp" data-t="47:20:00">[01:47:20]</a>. This enables post-processing of the crew's output, such as interpolating data into an HTML template to create the final PDF report <a class="yt-timestamp" data-t="48:07:00">[01:48:07]</a>.

## Complex Workflows with Flows
For more intricate automations, CrewAI introduces "Flows." These are event-based systems that can orchestrate multiple crews and integrate with various external sources like SAP or Salesforce <a class="yt-timestamp" data-t="50:38:00">[01:50:38]</a>.

A good example of a flow is generating long-form educational content <a class="yt-timestamp" data-t="52:49:00">[01:52:49]</a>:
*   A `start` function gathers user inputs (topic, learning style, interests) <a class="yt-timestamp" data-t="53:07:00">[01:53:07]</a>.
*   One crew generates a comprehensive content plan with chapters and their outlines <a class="yt-timestamp" data-t="53:31:00">[01:53:31]</a>.
*   Another crew writes individual chapters based on the plan, potentially looping through each chapter <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.
*   The output can be saved as Markdown files for each chapter <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>.

Flows provide a visual representation of the workflow, making it easier to understand and debug complex multi-agent systems <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>.

### Optimizing Agent Behavior
Optimizing [[designing_and_optimizing_ai_tasks_and_agents | AI tasks and agents]] involves refining their YAML files and ensuring tasks are precisely defined. For higher precision and consistency, Python files can incorporate "checks" and "guard rails" <a class="yt-timestamp" data-t="01:38:01">[01:38:01]</a>. This allows for validation of agent outputs and conditional execution of subsequent crews within a flow <a class="yt-timestamp" data-t="01:38:22">[01:38:22]</a>.

## Conclusion
While the process of deploying [[ai_agents_and_automation | AI agents]] in production involves "zigs and zags" and debugging <a class="yt-timestamp" data-t="01:26:06">[01:26:06]</a>, the ability to rapidly go from "zero to one" in building these automations is accelerating <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>. Learning these tools now is crucial, regardless of future market changes, as the knowledge will be invaluable <a class="yt-timestamp" data-t="01:39:12">[01:39:12]</a>.

For those looking to dive deeper, CrewAI recommends courses on DeepLearning.AI, which cover foundational concepts of [[ai_agents_and_automation | AI agents]] and practical [[use_cases_and_applications_of_ai_agents | use cases]] in companies like PWC <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>.