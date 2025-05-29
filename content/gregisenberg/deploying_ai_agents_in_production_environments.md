---
title: Deploying AI agents in production environments
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

[[Building AI agents with CrewAI | CrewAI]] is a leading platform for [[building_ai_agents_with_crewai | building AI agents]] and orchestrating them, enabling users to [[deploying_ai_agents_in_production_environments | deploy them into a production environment]] <a class="yt-timestamp" data-t="01:20:20">[01:20:20]</a>. This allows individuals and businesses to [[utilizing_ai_agents_to_automate_business_tasks | automate tasks]] and processes, effectively creating an "army of agents" to perform more work <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Even an AI agent company can [[implementing_ai_in_app_development_processes | use AI agents to scale]] its operations <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

## Core Capabilities of Deployed AI Agents

Once deployed, [[building_ai_agents_with_crewai | CrewAI]] agents can:
*   Perform data enrichment for leads <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
*   Automatically write and send emails <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   Produce real-time reports and generate PDFs <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.
*   Identify an ideal customer profile (ICP) and determine if a company is a good match <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   Propose actionable ideas for how a product can be used by a specific person or company <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   Draft tailored emails for outreach <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   Generate custom PDF reports tailored to a specific company <a class="yt-timestamp" data-t="27:00:00">[27:00:00]</a>.
*   Integrate with CRM systems and Google Calendar for advanced workflows like scheduling calls <a class="yt-timestamp" data-t="44:06:00">[44:06:00]</a>.
*   Generate long-form documents with multiple chapters, such as crash course PDFs <a class="yt-timestamp" data-t="52:49:00">[52:49:00]</a>.
*   Monitor cloud services like AWS and produce detailed markdown reports with validated links <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>.

## Methods for Deployment

### No-Code Deployment with Crew Studio
The CrewAI Enterprise free tier includes Crew Studio, a UI that allows users to [[building_ai_agents_with_crewai | create AI agents]] by chatting <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Users can define their crew's purpose, desired outputs, inputs, suggested tools, and agents, then generate and deploy the crew directly <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. This method is suitable for those less tech-savvy <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

### Code-Based Deployment
For more custom and complex implementations, users can download the generated code from Crew Studio <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
*   **Local Development**: Create crews locally using the `crewai create` command, which prompts for provider and model preferences <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
*   **GitHub Integration**: Deploy crews directly via GitHub integration, connecting a repository to the CrewAI platform <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>. Updates can be pushed via `git` commands, triggering re-deployment <a class="yt-timestamp" data-t="49:40:00">[49:40:00]</a>.

## Integration with External Services
Deployed [[building_ai_agents_with_crewai | CrewAI]] agents can act as an API, opening opportunities for interaction with various applications <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.
*   **Zapier**: Integrate with Zapier to connect workflows, such as triggering a crew based on a web form submission <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>. This allows for dynamic data mapping between external services and the AI agent's inputs <a class="yt-timestamp" data-t="24:27:00">[24:27:00]</a>.
*   **HubSpot and Slack**: Other integrations are available for business workflows <a class="yt-timestamp" data-t="22:59:00">[22:59:00]</a>.
*   **Resend**: Use services like Resend to send transactional emails, attaching AI-generated reports or content <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.
*   **PDF.co**: Utilize services like PDF.co to dynamically convert HTML outputs from agents into PDF format <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.

## Key Considerations for Deployment

### Model Selection
*   **Smaller Models**: Models like 7B or 14B may take longer to behave as agents due to getting stuck in "blind alleys" <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.
*   **Recommended Models**: GPT-4o mini is often a good starting point and generally works well <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
*   **Testing**: Use `crewai test` to evaluate different models locally, comparing task scores, overall crew scores, and execution times to optimize performance <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.

### Agent Design
*   **Role Impersonation**: Giving agents specific roles (e.g., "senior email content specialist") can influence their behavior and output quality <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
*   **Structured Outputs**: For complex tasks, agents can be configured to output structured data like Pydantic objects or JSON, allowing for programmatic use of the output <a class="yt-timestamp" data-t="36:52:00">[36:52:00]</a>.
*   **Tools**: Provide agents with tools like `serper.dev` for searching and web scraping to access up-to-date information and enhance their capabilities <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>.

### Workflow Orchestration
*   **Before/After Hooks**: Use hooks to define actions that run before or after a crew's execution, such as rendering an HTML template with dynamic data <a class="yt-timestamp" data-t="47:20:00">[47:20:00]</a>.
*   **[[setting_up_ai_agent_swarms_for_efficiency | Flows]]**: For more complex and event-based automations, [[setting_up_ai_agent_swarms_for_efficiency | flows]] allow for chained execution of multiple crews and custom Python functions based on specific events or conditions <a class="yt-timestamp" data-t="50:24:00">[50:24:00]</a>. Flows can include validation steps and conditional routing to different crews <a class="yt-timestamp" data-t="52:30:00">[52:30:00]</a>.
*   **Visualization**: [[setting_up_ai_agent_swarms_for_efficiency | Flows]] can be visualized using `crewai flow plot`, providing a clear diagram of the entire workflow, including agents, tasks, and event triggers <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. This enhances understanding and documentation of complex systems <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.

### Iteration and Optimization
*   **Start Simple**: It's recommended to start with a basic functional output and then iteratively tweak and refine it rather than aiming for a perfect output from day one <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   **Prompt Optimization**: Significant optimization often lies in refining the prompts for agents and tasks within the YAML files, especially in the initial planning stages of a multi-agent system <a class="yt-timestamp" data-t="01:37:56">[01:37:56]</a>.
*   **Precision through Code**: For greater precision and consistency, users should focus on adding checks, creating Pydantic objects, and implementing guardrails within the Python files <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>, <a class="yt-timestamp" data-t="01:38:14">[01:38:14]</a>.

For those looking to get started, CrewAI offers courses on DeepLearning.AI that cover fundamental concepts of [[ai_agent_startup_framework | AI agents]] and practical applications in companies <a class="yt-timestamp" data-t="01:41:06">[01:41:06]</a>.