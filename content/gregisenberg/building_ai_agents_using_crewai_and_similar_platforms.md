---
title: Building AI agents using CrewAI and similar platforms
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

This article explores how to [[building_apps_with_ai | build AI agents]] and automation solutions, focusing on CrewAI as a leading [[introduction_to_ai_agent_platforms | AI agent platform]]. Joe Moja, co-founder and CEO of CrewAI, demonstrates practical applications and discusses key concepts for [[importance_of_building_ai_agents_and_automation | building AI agents and automation]]. <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

## Tangible Skills and Objectives

By the end of this exploration, users should be able to:
*   Understand what [[importance_of_building_ai_agents_and_automation | AI agents]] are <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   Orchestrate them using CrewAI <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   [[deploying_ai_agents_for_business_automation | Deploy them]] into a production environment <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   [[building_and_using_aipowered_tools_for_business_processes | Build AI agents]] to automate processes for themselves, especially beneficial for solo entrepreneurs or small businesses looking to scale operations <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

The ability to use [[importance_of_building_ai_agents_and_automation | AI agents]] to scale an AI agent company provides an "Inception-like experience" in [[building_businesses_around_ai_agents | building businesses around AI agents]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Building AI Agents: A Step-by-Step Approach

### Simple Use Case: Lead Enrichment and Email Drafting

A common challenge for startups and companies is excelling in marketing and sales to generate revenue and gather market insights <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. [[building_and_using_aipowered_tools_for_business_processes | AI agents]] can automate lead enrichment, determining if a lead matches an Ideal Customer Profile (ICP) and the company's suitability <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The process involves:
1.  **Research:** Agents learn about the person and company (role, seniority, company size, industry, culture) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Idea Generation:** Agents generate ideas on how the lead could use the product <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
3.  **Email Drafting:** An agent drafts a personalized, friendly email to the lead <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

#### No-Code Building with Crew Studio

CrewAI Enterprise offers a free tier with Crew Studio, a platform where users can create [[importance_of_building_ai_agents_and_automation | AI agents]] by chatting <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a> <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

To set up the lead enrichment crew:
*   Define the crew's purpose: Research a person and company, learn about their business, generate product usage ideas, and draft an email <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   Specify outputs (fully crafted email) and inputs (name, email, company domain) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Suggest tools: Serper (for search), Scrape Website, and GPT-3 (though GPT-3 was removed for this demo) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   Define agents: A research agent, an analysis agent, and an email drafting agent <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   Assign tasks: One agent can handle multiple tasks (e.g., the research agent researches both person and company) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

#### Code-Based Building with CrewAI CLI

For more customization, users can download the generated code from Crew Studio or start locally using the CrewAI Command Line Interface (CLI). <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>

*   `crei create <crew_name>` command initiates a new crew, asking for provider (e.g., OpenAI) and default model (e.g., GPT-4o mini) <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   Agents and tasks can be defined in Python files, allowing granular control over models and tools per agent <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

#### Model Selection and Evaluation
When choosing an AI model for a task:
*   Smaller models (e.g., 7B, 14B) generally take longer and can get stuck in "blind alleys" <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   GPT-4o mini is often a good default choice for general tasks <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   CrewAI offers a `crew AI test` feature to evaluate different models locally, providing quality scores, hallucination scores, and execution times for tasks <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This allows for comparative analysis to select the most efficient and accurate model for specific needs <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

#### Role-Playing Agents
Assigning specific roles (e.g., "senior email content specialist") to agents can significantly affect their output behavior, similar to how prompt engineering works in tools like ChatGPT <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Deployment and Integration

### Deploying the Crew
Crews can be deployed directly from the Crew Studio UI or by pushing code to a GitHub repository integrated with CrewAI <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Once deployed, the crew becomes an API endpoint <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

### Integration with External Services
CrewAI supports integrations with popular services like Zapier, HubSpot, and Slack <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

#### Webflow and Zapier Integration
A Webflow form can trigger a Zapier webhook, which then initiates the CrewAI agent <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. The agent's output can then be sent to another service, like Resend for email delivery <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.

#### Debugging Common Issues
Live debugging during the demonstration revealed common issues, such as missing agent descriptions or incorrect attribute references in the code, highlighting the iterative nature of [[nonengineers_building_software_with_ai | building software with AI]] <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a> <a class="yt-timestamp" data-t="01:26:21">[01:26:21]</a>.

## Advanced Use Cases

### Custom PDF Report Generation
Beyond simple emails, [[importance_of_building_ai_agents_and_automation | AI agents]] can generate custom, branded PDF reports that can be used as lead nurturing materials <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This can automate tasks typically handled by junior marketing personnel <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>.

To achieve this:
1.  **HTML Template:** Use an HTML template for the report (e.g., generated by ChatGPT) <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.
2.  **Structured Output:** Configure agents to output structured data (e.g., Pydantic objects or JSON) rather than plain text, allowing for precise interpolation into the HTML template <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a> <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.
3.  **Hooks:** Use CrewAI's "after kickoff" hooks to run Python code that loads the HTML template, interpolates the agent's structured output, and converts it to a PDF (e.g., using a service like PDF.co) <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a> <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.

This allows for highly personalized reports with dynamic content, company logos, and specific insights <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

### Flows for Complex Automation

CrewAI Flows enable event-based automation for more intricate scenarios, allowing multiple crews to interact based on sequential or parallel events <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a> <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>.

#### Example: Educational Content Generation
A flow can be used to generate long-form documents like crash course PDFs:
1.  **Gather Input:** A function gathers user inputs (topic, learning style, interests) <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>.
2.  **Content Plan Generation Crew:** A crew generates a detailed content plan with chapters, descriptions, and learning activities <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This crew can utilize tools like Serper and Scrape Website to research and incorporate up-to-date information <a class="yt-timestamp" data-t="01:14:12">[01:14:12]</a>.
3.  **Content Creation Crew (Loop):** After the plan is generated, another crew can loop through each chapter, researching and writing content for each one, then saving them as separate markdown files <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a> <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.
4.  **Flow Plot Visualization:** The `crei flow plot` command generates a visual representation of the flow, illustrating the sequence of functions, crews, and events, aiding in understanding complex processes <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. This is particularly useful for visual learners and team collaboration <a class="yt-timestamp" data-t="01:03:27">[01:03:27]</a>.

This demonstrates the potential for [[creating_ai_employees_for_startups | creating AI employees for startups]] capable of complex, multi-stage tasks. For example, a generated SEO course plan specifically tailored to "gaming" interests and "visual" learning styles showed creative applications like analyzing SEO in popular games like Fortnite and Zelda <a class="yt-timestamp" data-t="01:31:52">[01:31:52]</a>. While some fine-tuning may be needed, it highlights the ability to generate niche and relevant content <a class="yt-timestamp" data-t="01:36:07">[01:36:07]</a>.

## Best Practices and Further Optimization

*   **Start Simple:** Begin with basic functionality and iterate. It's more effective to get a working version out quickly than to aim for perfection from day one <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a> <a class="yt-timestamp" data-t="00:45:51">[00:45:51]</a>.
*   **Optimize Prompts:** Spend time refining agent and task prompts (YAML files) to achieve desired behaviors <a class="yt-timestamp" data-t="01:38:01">[01:38:01]</a>.
*   **Precision in Python:** For higher precision and consistency, use Python files to add checks, create Pydantic objects, and build guard rails or complex flows <a class="yt-timestamp" data-t="01:38:14">[01:38:14]</a>.

AI in coding is still an interactive process. While AI tools and agents accelerate development from "zero to one," refining and optimizing solutions from "one to ten" still requires significant human involvement <a class="yt-timestamp" data-t="01:28:25">[01:28:25]</a>.

## Learning Resources
To dive deeper into [[importance_of_building_ai_agents_and_automation | building AI agents]]:
*   DeepLearning.AI courses by Andrew Ng feature CrewAI, offering introductory and practical insights into building and [[deploying_ai_agents_for_business_automation | deploying AI agents]] in companies <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a> <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>. These courses cover foundational concepts like agents, tools, and LLMs, and practical applications, including interviews with industry leaders on how they use CrewAI in production (e.g., PWC) <a class="yt-timestamp" data-t="01:41:32">[01:41:32]</a> <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>.