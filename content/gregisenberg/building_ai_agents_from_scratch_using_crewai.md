---
title: Building AI agents from scratch using CrewAI
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

Joe Moa, co-founder and CEO of CrewAI, introduces the platform as a leading tool for [[building_ai_agents_for_business_automation | building AI agents]] and automating business processes. By the end of this session, users should be able to build and deploy AI agents using CrewAI, understanding how to orchestrate them for various tasks <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. This approach is particularly beneficial for solo entrepreneurs and businesses looking to create an "army of Agents" to increase productivity <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## Core Concepts of AI Agents

AI agents in CrewAI are designed to impersonate roles, with their behavior influenced by the specific role assigned to them <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. For example, asking ChatGPT for a stock assessment yields a different answer if it's asked to "behave as an FCC-proven stock analyst" <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This allows for steering the model's behavior in a desired way <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

Agents can also be assigned specific tools, such as Serper (for searching) and web scraping tools, to gather relevant, up-to-date information online <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## Use Case: Automated Lead Enrichment and Email Drafting

A primary demonstration involves using AI agents for lead enrichment, sales, and marketing tasks <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. The goal is to automatically gather information about a lead and their company, assess if they fit the ideal customer profile (ICP), and then draft a personalized email <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

The process involves agents:
1.  **Researching**: Learning about the person's role, seniority, and the company's size, industry, and culture <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
2.  **Generating Ideas**: Coming up with three specific ideas on how the lead can use the product based on the gathered information <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
3.  **Drafting Email**: Creating a friendly, non-AI-sounding email that offers to explain how agents can be used in their business <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

Inputs for this crew include the person's name, email, and company domain <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

## [[generating_and_deploying_ai_agents_with_nocode_tools | Building AI Agents with Crew Studio (No-Code)]]

CrewAI Enterprise offers Crew Studio, a free-tier platform that allows users to create AI agents by chatting, effectively automating workflows without code <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

To build a crew in Crew Studio:
1.  **Define the Goal**: For lead enrichment, the goal is to research a person and company, learn about their business, and produce a ready-to-send email with product usage ideas <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
2.  **Studio Prompts**: The platform suggests agents (e.g., research agent, analysis agent, email drafting agent), tasks, and tools (e.g., Serper, scrape website) based on the user's prompt <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
3.  **Agent-Task Mapping**: CrewAI allows one agent to perform multiple tasks, providing flexibility <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
4.  **Deployment**: Once the crew plan is generated, it can be deployed directly from the studio <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. The deployed crew exposes an API with defined inputs <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

## [[building_ai_agents_from_scratch_using_crewai_cli | Building AI Agents with CLI (Code)]]

For users who prefer coding or require more customization, CrewAI provides a Command Line Interface (CLI):
*   **`crei create`**: Initializes a new crew, asking questions about providers (e.g., OpenAI), models (e.g., GPT-4o, GPT-4o mini, Sonnet), and other configurations <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **Model Selection**: GPT-4o mini is recommended as a general go-to model, as smaller models can be slower and explore "blind alleys" <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **[[crew_ai_test | CrewAI Test]]**: This feature allows local evaluation of different models, providing quality and hallucination scores, as well as execution time for each task and the overall crew <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. This helps compare model performance, e.g., Sonnet might be better for quality but slower <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Code Inspection**: Crews created in Crew Studio can be downloaded as code, allowing users to inspect and further customize agents, tasks, and configurations <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Deployment from Git**: Crews can be deployed via GitHub integration by pushing the code to a repository <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

## Integration and Deployment with Zapier

Deployed CrewAI agents can be integrated with other applications via API calls. CrewAI Enterprise offers direct integrations with tools like Zapier and HubSpot <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

The demonstration shows integrating a Webflow form with CrewAI via Zapier:
1.  **Webflow Form**: A simple website form collects name, email, and company domain <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
2.  **Zapier Webhook**: Zapier receives the form submission via a webhook <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
3.  **CrewAI Kickoff**: Zapier triggers the CrewAI agent using its API, passing the collected lead data <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
4.  **Resend Email**: After the CrewAI agent generates the email content, Zapier uses Resend (an email API) to send the personalized email to the lead <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Resend is highlighted for its transactional email capabilities and analytics <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

Initial implementations might have minor issues like missing inputs or formatting, but these can be debugged and refined through testing and tweaking prompts <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

## Advanced Use Case: Custom PDF Report Generation

Beyond email drafting, AI agents can generate more sophisticated outputs like custom PDF reports. This replaces manual work typically done by a junior marketing person <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

Steps to implement this:
1.  **Structured Output**: Agents need to output structured data (e.g., Pydantic objects or JSON) rather than just text <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. This allows for programmatic use of the data <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
2.  **HTML Template**: An HTML template (which can be generated by ChatGPT) is used as the base for the PDF <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Variables within the HTML are set up for interpolation <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
3.  **After Kickoff Hook**: CrewAI's `after_kickoff` hook allows custom Python functions to run after the crew completes its tasks. This function takes the crew's structured output, interpolates it into the HTML template, and then converts the HTML to a PDF using a service like PDF.co <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
4.  **Email Attachment**: The generated PDF URL is then attached to the email sent via Resend <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

This allows for highly personalized and visually appealing reports tailored to each customer, potentially including company logos and specific insights <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

## Flows for Complex, Event-Based Automation

For even more complex use cases, CrewAI introduces "Flows." Flows enable event-based automation, allowing multiple crews to interact sequentially or in parallel based on defined events <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

*   **`crei create flow`**: Initializes a new flow <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   **Structure**: A flow contains a `crews` folder, allowing for modular organization of different AI agent crews <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **Event-Driven**: Functions within a flow listen for completion events from previous functions (e.g., `generate_poem` listens for `meeting_event`) <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Advanced Logic**: Flows can include conditional logic, validation of outputs, and loops, enabling complex decision-making and iterative content generation <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.
*   **Use Case: Educational Content Generation**: An example flow for generating a multi-chapter crash course PDF:
    1.  **Gather User Input**: Collects topic, learning style, and interests <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
    2.  **Generate Content Plan (Crew 1)**: A crew plans the chapters, outlines, and activities based on user input <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. The output is a structured Pydantic object representing the content plan <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
    3.  **Generate Chapter Content (Crew 2)**: This crew loops through the chapters from the content plan, researching and writing each chapter as a Markdown file <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
    4.  **Save Content**: Saves the generated content.
*   **`crei flow plot`**: Generates a visual representation of the flow, showing the sequence of crews and events, which is helpful for documentation and team collaboration <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.

## Key Takeaways for [[building_automated_businesses_with_ai | Building AI-Powered Workflows]]

*   **Start Simple, Iterate Often**: Begin with a basic functional agent and then refine and optimize it <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. The easiest way to get started is by iterating and making incremental improvements <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Precision vs. Fuzzy Output**: Initial AI agent outputs might be "fuzzy" (text-based), but as use cases become more complex, structured outputs (Pydantic, JSON) become necessary for repeatability and consistency <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
*   **Optimize Prompts**: Spend time crafting detailed prompts and defining agent roles to guide behavior <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.
*   **Leverage Tools**: Provide agents with access to external tools like search engines and web scrapers to enhance their research capabilities <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **Beyond Basic Automation**: AI agents can be integrated with CRM, calendar systems, and other platforms to create fully automated workflows, such as scheduling calls directly after sending an email <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
*   **Embrace the Learning Process**: The field of AI is still early; learning these tools is crucial for future success, regardless of how the market evolves <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Even with AI assistance, coding still involves an interactive debugging process <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

## Getting Started Resources

Joe Moa recommends checking out the DeepLearning.AI courses with Andrew Yang, which provide an introduction to AI agents, tools, and LLMs, as well as practical examples and interviews with companies like PWC on their real-world usage of CrewAI <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.