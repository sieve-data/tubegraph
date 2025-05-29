---
title: Using AI in lead enrichment and marketing
videoId: PM9zr7wgJX4
---

From: [[gregisenberg]] <br/> 

[[AI agents and automated marketing workflows | AI agents]] can be leveraged for tasks such as data enrichment and automated marketing workflows <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This approach allows businesses, including solo entrepreneurs and small businesses, to perform more work through automated agents <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Joe Moa, co-founder and CEO of CrewAI, demonstrates how to build and deploy these agents <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Core Concepts of [[AI agents and automated marketing workflows | AI Agents]] and CrewAI

By the end of the demonstration, users should be able to understand what [[AI agents and automated marketing workflows | AI agents]] are, how to orchestrate them using CrewAI, and how to deploy them into a production environment <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The core incentive is to empower individuals to build agents that work for them, especially for those looking to [[Using AI to scale and automate marketing tasks | scale and automate marketing tasks]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. [[Using AI and Technology in Marketing | Using AI and technology in marketing]] can help scale an AI agent company, proving the automation's utility <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Lead Enrichment and Automated Outreach Use Case

A primary use case for [[AI agents and automated marketing workflows | AI agents]] in marketing and sales is lead enrichment <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
The goal is to answer key questions about a lead:
*   Is this person within the Ideal Customer Profile (ICP)? <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
*   Is the company a good match? <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   Should time be spent pursuing them? <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>

### Process Flow
The demonstration outlines a process to enrich lead data and make it actionable <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>:
1.  **Research**: Agents research a person and company based on name, email, and domain. They gather information like role, seniority, company size, industry, and culture <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
2.  **Idea Generation**: Agents generate three ideas on how the lead can use AI agents in their business <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **Email Drafting**: Agents draft a friendly email, free of AI jargon, offering to explain how agents can be used <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
4.  **Custom PDF Report Generation**: Beyond a simple email, agents can generate a custom, fancy PDF report tailored to the company, incorporating logos and specific ideas for using the product <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. This report can be sent to leads to help them internally champion the product <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. This automates a task typically performed by a junior marketing person <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.

### Tools and Technologies Used
*   **CrewAI**: The platform for orchestrating [[AI agents and automated marketing workflows | AI agents]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
*   **Crew Studio**: A no-code interface for creating [[AI agents and automated marketing workflows | AI agents]] by chatting <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **CrewAI CLI**: For local development and deploying CrewAI projects <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **AI Models**: GPT-4o mini, GPT-4o, and Sonnet are evaluated for different tasks <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Generally, larger models like GPT-4o mini are preferred as smaller models can be slower and less effective <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **Tools (within CrewAI)**:
    *   **Serper**: For web searching <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   **Scrape Website**: For extracting content from websites <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Integration Platforms**:
    *   **Zapier**: To connect CrewAI agents with other applications, enabling automated workflows from web forms (e.g., Webflow) to email sending (e.g., Resend) <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>, <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
    *   **Resend**: For sending transactional emails <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.
    *   **PDF.co**: For dynamically converting HTML to PDF <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.
*   **Development Tools**: Cursor (AI-powered code editor) was used for live coding <a class="yt-timestamp" data-t="00:36:07">[00:36:07]</a>.

### Agent Orchestration and Tasks
CrewAI allows for flexible assignment of agents to tasks, not strictly one-to-one <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For example, a research agent can handle both person and company research tasks <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Defining specific roles for agents, like "Senior Email Content Specialist," can influence their behavior and output <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Outputs and Structured Data
Agents can be configured to produce structured outputs, such as Pydantic objects or JSON, which is crucial for programmatic use (e.g., interpolating data into a PDF template) <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. HTML templates can be used for custom reports, with variables for dynamic content <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

## Advanced Workflow: Flows
CrewAI "flows" enable event-based automations containing multiple crews <a class="yt-timestamp" data-t="00:51:28">[00:51:28]</a>. This allows for more complex use cases and integrations with systems like SAP, Salesforce, and custom Python scripts <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

### Example: Educational Content Generation
A flow can be used for generating long-form documents, such as a crash course PDF <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>.
*   **User Input**: Gather topic, learning style, and interests <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>.
*   **Content Plan Crew**: Generates a detailed plan with chapters and their structure <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.
*   **Content Creation Crew (in a loop)**: Writes each chapter, researching and incorporating user interests for examples <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.
*   **Saving Content**: Saves the generated content, for example, as markdown files <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

Visual representations of flows can be generated, making complex automations easier to understand and document <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.

## Key Takeaways
*   **Start Simple**: It's recommended to build a basic functional agent first and then iterate and optimize <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>, <a class="yt-timestamp" data-t="00:45:51">[00:45:51]</a>.
*   **Iterative Process**: Building with [[AI agents and automated marketing workflows | AI agents]] is an iterative process, involving testing, debugging, and continuous refinement of agents and tasks <a class="yt-timestamp" data-t="01:28:06">[01:28:06]</a>.
*   **Precision and Consistency**: For complex use cases, more precision is needed through structured outputs (Pydantic objects), hooks (before/after tasks), and guardrails <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.
*   **Learning is Key**: Given that the AI market is in its early stages, continuous learning about new tools and approaches is crucial, as it sets individuals up for future success regardless of market winners <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>.

## Learning Resources
For those looking to dive deeper into building with CrewAI and [[AI agents and automated marketing workflows | AI agents]], Joe Moa recommends checking out courses by Andrew Ng on DeepLearning.AI <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>. These courses cover foundational concepts of [[AI agents and automated marketing workflows | AI agents]] and practical applications seen in companies, including how PWC uses CrewAI in production <a class="yt-timestamp" data-t="01:41:32">[01:41:32]</a>.