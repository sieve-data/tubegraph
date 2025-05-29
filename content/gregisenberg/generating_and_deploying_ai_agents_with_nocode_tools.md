---
title: Generating and deploying AI agents with nocode tools
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Joe Moa, co-founder and CEO of [[ai_agent_platforms | CrewAI]], demonstrates how to [[building_ai_agents_from_scratch_using_crewai | build AI agents]] and [[deploying_ai_applications_using_vercel | deploy them into a production environment]] using CrewAI, starting with no-code tools and progressing to more complex flows for business automation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

The session aims to provide tangible skills, enabling users to:
*   Fully understand what AI agents are <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Orchestrate AI agents using CrewAI <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   [[deploying_ai_applications_using_vercel | Deploy AI agents into a production environment]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Start [[building_ai_agents_for_business_automation | building AI agents for business automation]] and process automation <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Initial Use Case: Lead Enrichment and Email Generation

A practical [[examples_and_use_cases_of_ai_agents | use case]] for AI agents is lead enrichment and automated email drafting for sales and marketing <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This process helps determine if a lead fits an Ideal Customer Profile (ICP) and if the company is a good match <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

The proposed AI agent workflow includes:
1.  **Data Enrichment**: Researching a person and company based on name, email, and domain <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This includes learning about their role, seniority, company size, industry, and culture <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
2.  **Idea Generation**: Developing three specific ideas on how the lead can use the product (AI agents) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Email Drafting**: Generating a friendly, non-AI-sounding email that proposes how they could use AI agents in their business and suggests a call <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Building AI Agents with No-Code (Crew Studio)

Crew Studio, accessible via CrewAI Enterprise's free tier, allows users to create AI agents by chatting <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The process involves:
*   **Defining the Crew**: Specifying the goal (e.g., "research both a person and a company," "produce an email") <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Inputs and Outputs**: Identifying necessary inputs (name, email, domain) and desired outputs (fully crafted email) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Tools**: Suggesting tools like Serper (for search) and website scraping <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Agents and Tasks**: Crew Studio suggests agents (e.g., Researching, Analysis, Email Drafting) and tasks (e.g., researching person, researching company, generating ideas, drafting email) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Agents can be assigned to multiple tasks <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Customization**: Users can modify agent names (e.g., adding "Senior" to a role can influence output behavior) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> and model choices (e.g., GPT-4o, GPT-4o mini) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Deployment**: The studio generates code that can be downloaded or deployed directly as an API <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Model Selection for AI Agents
When selecting models for AI agents, it's recommended to start with models like GPT-4o mini, as smaller models (e.g., 7B, 14B) may take longer and explore more "blind alleys" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

CrewAI offers a "CrewAI Test" feature to evaluate different models locally <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This tool provides:
*   Task scores <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   Overall crew score <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   Execution time <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   Quality and hallucination scores <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

## Integration and Deployment Walkthrough

The deployed CrewAI agent functions as an API, allowing integration with other applications <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

### Zapier Integration
A Zapier webhook can trigger the CrewAI agent <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
1.  **Webhook Trigger**: Set up a Zapier webhook to receive data (name, email, domain) <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
2.  **CrewAI Action**: Configure CrewAI to kick off the deployed crew, mapping the webhook inputs to the agent's required inputs <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.
3.  **Email Sending (Resend)**: Use a service like Resend to send the drafted email, using the CrewAI agent's output as the email body <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>. Resend is highlighted as a transactional email service with a good analytics platform <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.

### Webflow Integration
A Webflow form can capture lead information and send it to the Zapier webhook <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. The form fields (name, email, company domain) are set up to match the data expected by Zapier and CrewAI <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

## Advanced Use Case: Custom PDF Report Generation

Beyond simple emails, AI agents can [[generating_content_with_ai_tools | generate custom PDF reports]] <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. This automates tasks typically performed by junior marketing personnel, providing a personalized, high-quality output <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.

The process for generating custom PDF reports involves:
1.  **HTML Template**: Generate a base HTML template (e.g., using ChatGPT) <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.
2.  **Dynamic Content**: Update the HTML template to include dynamic variables that will be interpolated with data from the AI agents <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
3.  **Structured Output (Pydantic)**: Modify the AI agent's tasks to output structured data (Pydantic object or JSON) instead of plain text, ensuring programmatic usability <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>.
4.  **After-Crew Hook**: Implement an "after-crew hook" function that runs after the agent completes its tasks <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>. This function takes the agent's structured output, interpolates it into the HTML template, and converts the HTML to PDF (e.g., using PDF.co) <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.

## Complex Automation with Flows

For more intricate [[building_ai_agents_for_business_automation | business automation]], CrewAI introduces "flows" <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. Flows are event-based automations that can contain multiple crews and custom Python logic <a class="yt-timestamp" data-t="00:51:28">[00:51:28]</a>.

Key features of flows:
*   **Event-Based System**: Functions listen to previous functions' completion, allowing for sequential or parallel execution of tasks and crews <a class="yt-timestamp" data-t="00:51:49">[00:51:49]</a>.
*   **Multiple Crews**: A flow can orchestrate multiple crews (collections of agents and tasks) to achieve complex goals <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>.
*   **Use Case Example: Educational Content Generation**: A flow can be used to [[generating_content_with_ai_tools | generate long-form documents]] like a crash course PDF <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>.
    *   **Gather User Input**: A function gathers inputs like topic, learning style, and interests <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>.
    *   **Content Plan Crew**: A crew generates a comprehensive content plan with chapters <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.
    *   **Chapter Writing Crew (Loop)**: Another crew, potentially in a loop, writes each chapter based on the content plan <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.
*   **Visual Representation**: The `crewAI flow plot` command generates a visual diagram of the flow, showing crews, inputs, functions, and events <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. This is useful for understanding complex workflows and documentation <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>.
*   **Adding Tools**: Agents within flows can utilize tools like Serper for internet search and web scraping to gather relevant, up-to-date information <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.

### Best Practices for Building AI Agents
*   **Start Simple**: Begin with basic functionality and iterate <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>. Don't aim for the fanciest output on day one <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.
*   **Optimize Behavior**: Focus on refining agent and task definitions (often in YAML files) to get the desired behavior <a class="yt-timestamp" data-t="01:38:01">[01:38:01]</a>.
*   **Ensure Precision**: For high precision and consistency, use Python files to add checks, create structured Pydantic objects, implement guard rails, and build complex flows <a class="yt-timestamp" data-t="01:38:14">[01:38:14]</a>.

For those looking to dive deeper, recommended resources include DeepLearning.AI courses by Andrew Ng, which cover fundamental concepts and practical [[comparison_of_ai_coding_tools | applications of AI agents]] in companies <a class="yt-timestamp" data-t="01:41:07">[01:41:07]</a>.