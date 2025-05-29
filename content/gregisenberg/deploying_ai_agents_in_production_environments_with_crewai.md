---
title: Deploying AI agents in production environments with CrewAI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

CrewAI is described as one of the leading [[AI agents and their applications | AI agent platforms]] currently available <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores how to build, orchestrate, and deploy [[AI agents and their applications | AI agents]] using CrewAI into a production environment <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The goal is to enable individuals and businesses, including solo entrepreneurs and startups, to leverage an "army of agents" to automate processes and scale operations <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Core Concepts and Tangible Skills

By the end of learning about CrewAI, users should be able to:
*   Understand what [[AI agents and their applications | AI agents]] are <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Orchestrate them using CrewAI <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Deploy them into a production environment <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   [[Building AI agent platforms with CrewAI | Build AI agents]] for themselves and automate processes <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The co-founder and CEO of CrewAI noted that even their own startup has benefited from using [[AI agents and their applications | AI agents]] to scale an [[building_ai_agent_platforms_with_crewai | AI agent company]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The idea of having [[AI agents and their applications | agents]] automating certain processes can be quite amazing for [[creating_ai_employees_for_startups | building businesses]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Building and Deploying AI Agents

CrewAI offers both no-code and code-based methods for [[building_ai_agent_platforms_with_crewai | building AI agents]].

### Using Crew Studio (No-Code)

Crew Studio is a way to create [[AI agents and their applications | AI agents]] by chatting, allowing users to chat their way into an automation <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. It's available on CrewAI Enterprise's free tier <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

An example use case is a lead enrichment system that can research a person and company based on their name, email, and company domain <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This system aims to learn about their business, role, seniority, company size, industry, and culture <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. It also generates three ideas on how they can use [[AI agents and their applications | AI agents]] and drafts a friendly, non-AI-sounding email <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

The process in Crew Studio involves:
1.  **Defining the Crew**: Inputting the desired outcome, inputs (name, email, domain), suggesting tools (Serper, Scrape Website), and proposing agents (researching, analysis, email drafting) and tasks <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Generating the Crew**: The studio generates the code, which can be downloaded or deployed directly <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
3.  **Configuring Agents and Tasks**: Users can change tasks, agents, and assign tools (e.g., Serper, Scrape Website) to specific tasks <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Using the CLI for Local Development

Users can also create crews locally using the open-source version by running `crei create <crew_name>` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This command prompts for provider (e.g., OpenAI) and default model (e.g., GPT-4o Mini), with the option to specify individual models per agent later <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

#### Model Selection

Choosing the right model is crucial. Smaller models (like 7B, 14B) generally don't work as well as [[building_ai_agent_platforms_with_crewai | agents]] and can take longer due to exploring "blind alleys" <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. GPT-4o Mini is a common go-to choice for good performance <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

#### Testing and Evaluation

CrewAI offers a `crewAI test` feature to evaluate different models locally <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This command runs agents with various models (e.g., GPT-4, GPT-4o Mini) and provides task scores, overall crew scores, and execution times, helping users compare performance and hallucination scores <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

#### Agent Roles and Their Impact

Giving [[AI agents and their applications | agents]] specific roles (e.g., "senior email content specialist") can influence their behavior and output <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is similar to how prompting ChatGPT to "behave as an SEC stock analyst" yields different results than a general assessment <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Deployment Options

Crews built using the Enterprise platform automatically become an API, opening opportunities for [[collaboration_and_deployment_in_ai_coding_tools | integration]] with various applications <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Direct API Calls**: Users can interact with the deployed crew via API, providing inputs like `name`, `email`, and `company_name` <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **Webhooks**: Technical users can use webhooks for progress bars and other functionalities <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Built-in UI**: The platform provides a simple UI where users can input data and trigger agents <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Export React Component**: For embedding, a React component can be exported <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **GitHub Integration**: Crews developed locally with code can be deployed directly via GitHub integration <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

## Practical Use Cases

### 1. Lead Enrichment and Automated Email Generation

This use case demonstrates how [[AI agents and their applications | AI agents]] can perform lead enrichment, learning about a person and company, and then draft a personalized outreach email <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
The workflow involves:
*   **Research Agent**: Researches the person and company <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Analysis Agent**: Generates ideas for product usage <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Email Drafting Agent**: Crafts the email using insights from the research and analysis <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

This system can be integrated with external services like Webflow (for collecting leads) and Zapier (to trigger the CrewAI process) <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. Resend can be used for sending transactional emails <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>. The output email can be immediately usable, and further optimization can be done by tweaking the prompt <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.

### 2. Generating Custom PDF Reports

Taking the lead enrichment further, [[AI agents and their applications | agents]] can generate a custom, fancy PDF report that looks professional and tailored to the lead's company <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This automates a task that would typically require a junior marketing person or designer, potentially saving significant costs <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.

The process involves:
1.  **HTML Template**: Generate an HTML template (e.g., using ChatGPT) <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.
2.  **Dynamic Content**: Update the HTML template to include variables that can be interpolated with data from the [[AI agents and their applications | agents]] <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
3.  **Structured Output**: Configure the [[AI agents and their applications | agents]] to output structured data (e.g., Pydantic object or JSON) for programmatic use, instead of just text <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.
4.  **After Kickoff Hook**: Use an `after_kickoff` hook in CrewAI to run a function that interpolates the collected data into the HTML template <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>.
5.  **HTML to PDF Conversion**: Utilize a service like PDF.co (or similar) to dynamically convert the generated HTML into a PDF <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.
6.  **Email Attachment**: Attach the generated PDF report to the email <a class="yt-timestamp" data-t="01:22:27">[01:22:27]</a>.

This allows for highly personalized marketing materials that a lead could even show in a meeting <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.

### 3. Long-Form Document Generation with Flows

For more complex, event-based automations, CrewAI introduces "Flows" <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. Flows can integrate with various sources like Salesforce and execute Python code before, after, or during crew runs <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

An example is generating a crash course PDF, which involves creating a long-form document with many chapters <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>. The flow can:
1.  **Gather User Input**: A function gathers inputs like topic, learning style, and interests <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>.
2.  **Generate Content Plan (Crew 1)**: A dedicated crew generates a plan, outlining chapters and their structure <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This crew can use tools like Serper and scraping to find relevant and up-to-date information <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.
3.  **Generate Chapter Content (Crew 2)**: Another crew takes the content plan and iteratively writes each chapter <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>. This crew can also use tools for research <a class="yt-timestamp" data-t="01:33:11">[01:33:11]</a>.
4.  **Save Content**: Functions save the generated content (e.g., as Markdown files) <a class="yt-timestamp" data-t="01:01:59">[01:01:59]</a>.

Flows allow for complex conditional logic and parallel execution <a class="yt-timestamp" data-t="00:58:58">[00:58:58]</a>. CrewAI provides `crei flow plot` to visualize the flow, showing crews, inputs, and events, aiding in documentation and understanding <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.

### 4. Monitoring AWS

A practical, high-level example is building a crew to monitor AWS (Amazon Web Services), producing a detailed Markdown report with an executive summary, table of contents, analysis, and even linked resources <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>. This level of detail includes guardrails to ensure links are valid and not hallucinations <a class="yt-timestamp" data-t="01:39:24">[01:39:24]</a>.

## Development Philosophy

The general approach to [[utilizing_ai_for_automation_and_scalability | building apps with AI tools]] is to:
*   **Start Simple**: Get a basic version working first <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.
*   **Iterate and Optimize**: Continuously tweak and refine the outputs, especially by optimizing prompts for agents and tasks <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>.
*   **Add Precision**: As use cases become more complex, add precision using Python files, checks, and structured data objects <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. This includes using "before and after hooks" and "guardrails" <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.
*   **Embrace Debugging**: Expect and work through errors, as [[collaboration_and_deployment_in_ai_coding_tools | AI coding tools]] are still an interactive process <a class="yt-timestamp" data-t="01:28:06">[01:28:06]</a>.

> [!NOTE] Early Days
> It's still very early days for [[AI agents and their applications | AI agents]], and no one knows how things will play out or which tools will become dominant <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>. The best approach is to learn these tools and use them, as this knowledge will be valuable regardless of future outcomes <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>.

## Learning Resources

For those looking to dive deeper, there are courses available on deeplearning.ai (taught by Andrew Yang) that cover:
*   **Introduction to AI Agents**: For beginners, explaining what [[AI agents and their applications | agents]], tools, and LLMs are <a class="yt-timestamp" data-t="01:41:20">[01:41:20]</a>.
*   **Practical Applications**: Focuses on what companies are doing with CrewAI, including an interview with the CTO of Gen on PWC, discussing how PWC is using CrewAI in production <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.