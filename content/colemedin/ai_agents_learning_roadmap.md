---
title: AI agents learning roadmap
videoId: k-Cj6H6Zwos
---

From: [[colemedin]] <br/> 

The speaker has been [[ai_agents_and_their_development | building AI agents]] since 2022, which is considered an early start in the field, preceding features like function calling or competing LLMs like Claude or Gemini <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This experience has led to a confident approach in [[building_ai_agents | building AI agents]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The following outlines a clear and simple [[step_by_step_process_for_building_ai_agents | process]] to learn how to [[building_ai_agents | build AI agents]] from scratch, aiming to accelerate learning and avoid common pitfalls <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The roadmap consists of 10 phases, designed to be specific and manageable <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Even someone completely new to [[understanding_ai_agents | AI agents]] could get through this entire process in just a couple of months <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Phases of the AI Agent Learning Roadmap

### Phase 1: Building Our Foundation
This phase focuses on the absolute basics of [[ai_agents_and_large_language_models | AI agents and large language models]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

*   **Understanding Large Language Models (LLMs)**
    *   Learn what a large language model is <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   Explore current leading LLMs like Claude, Gemini, and GPT <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   Understand local AI models such as Mistral or Llama, which can run on a personal computer <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **[[understanding_ai_agents | AI Agents]] vs. Traditional Automations**
    *   Recognize the paradigm shift that [[understanding_ai_agents | AI agents]] introduce by adding reasoning to automations <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Understand the increased power and unpredictability that comes with this <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Effective Prompting**
    *   Learn how to effectively communicate with LLMs and agents, focusing on "effective prompting" rather than the "overused and overhyped" term "prompt engineering" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Leveraging Out-of-the-Box Tools**
    *   Before [[building_ai_agents | building an AI agent]], conduct due diligence to ensure a problem hasn't already been solved by an existing, affordable solution <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Examples of useful tools include:
        *   ChatGPT or Claude Desktop for chat applications, supporting MCP servers and other tool integrations <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
        *   Aqua Voice for converting speech to text across the computer <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
        *   MEM for organizing notes and scripts, with an API for easy integration <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
        *   Perplexity for deep research on new AI tech, LLMs, or frameworks <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

> [!tip] Capabilities Over Tools
> Always prioritize learning the high-level skills and capabilities that are widely applicable, rather than getting bogged down in mastering specific tools that might quickly become irrelevant <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Phase 2: Building AI Agents with No Code Tools
Regardless of coding experience, starting with no-code tools is highly recommended for first-time [[building_ai_agents | AI agent]] builders <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

*   **Recommended Platforms:** N8N, Flowise, Voice Flow, and Relevance AI are useful for quickly prototyping and getting agents up and running <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Tool Integration:** Learn how to integrate tools with agents to perform actions in services like Gmail, Slack, and Outlook <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Retrieval Augmented Generation (RAG):** Understand this crucial process for providing external knowledge to [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]], making them domain experts <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Basic Agent Memory:** Learn how agents remember conversations and how that data is stored <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Learn by Doing:** Build at least one (and ideally many) agents using no-code tools like N8N to gain practical experience and comfort <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Phase 3: Learning AI Coding Assistants
Leveraging AI to assist in coding is essential to stay competitive <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

*   **Impact of AI in Coding:** Companies like Anthropic report 70% of their code is now written by AI <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **AI IDEs:** Explore tools like Windsurf, Cursor, and Rue that operate within your development environment <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Front-end Specific Builders:** Tools like Lovable and Bolt.diy/Bolt.new run in the browser for front-end development <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Prompting AI Coding Assistants:** Learn specific techniques for prompting these assistants effectively <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Leveraging MCP Servers:** Use these to provide additional tools to AI coding assistants for tasks like database management or web searches <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Learn by Doing:** Build simple automations and agents with code using AI IDEs to become comfortable with these tools <a class="yt="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Phase 4: Using Code to Create AI Agents
Transitioning from no-code to code-based agent building offers greater flexibility, control, speed, and performance <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

*   **Benefits of Code:** While no-code tools are great for prototyping, code is preferred for maximum flexibility and performance <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Python Proficiency:** Python is the primary language for [[building_ai_agents | AI agents]] and frameworks <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Learn Python basics to understand what AI coding assistants create <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **Picking an [[understanding_ai_agent_frameworks | AI Agent Framework]]:** Explore options like Pydantic AI, LangGraph, OpenAI agents SDK, Agno, and Crew AI <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Choose based on simplicity, performance, and specific criteria, but avoid overthinking due to the "capabilities over tools" principle <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Learn by Doing:** Convert an agent prototyped with a no-code tool (like N8N) into a coded version using a framework like Pydantic AI <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

### Phase 5: [[advanced_architecture_for_ai_agents | Advanced Architecture]]
Elevate [[ai_agents_and_their_development | AI agents]] by exploring advanced architectural patterns <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

*   **Multi-Agent Workflows:** Distribute responsibility among multiple agents for complex systems <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Memory Systems:** Implement long-term memory solutions for agents <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Guardrails:** Crucial for reliability, implement input guardrails (preventing garbage input) and output guardrails (ensuring acceptable output to the end-user) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Fallback Mechanisms:** Design systems for graceful degradation in case of unexpected behavior <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Learn by Doing:** Enhance a previously coded agent by adding long-term memory, input guardrails, or by combining it with another agent to build a multi-agent workflow <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Phase 6: Deploying Our AI Agents
The next step is to prepare [[ai_agents_and_their_development | AI agents]] for production <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

*   **Docker Containerization:** Use Docker to containerize agents into isolated environments for easy deployment to the cloud <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Cloud Platforms:** Research and choose a suitable cloud platform:
    *   Easy-to-use options: Digital Ocean, Hostinger <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
    *   Enterprise-level: Amazon Web Services (AWS), Google Cloud Platform (GCP) <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
    *   GPU instances for larger local LLMs: Vast AI, RunPod <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Learn by Doing:** Deploy a built agent to the cloud using one of these platforms to gain comfort with the deployment and scaling process <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Phase 7: Monitoring Our Agents
Once an agent is in production, monitoring (observability) is critical <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

*   **Agent Observability:** Gain insight into agent behavior in production, including user requests, tool-calling decisions, and output to end-users <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **Error Detection and Improvement:** Essential for detecting errors and identifying opportunities to enhance the agent <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Tools:** Options for agent observability include Langfuse, Helicone, Langsmith, Logfire, and Pydantic AI <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. It is 100% necessary for production <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

### Phase 8: Agent Evaluation
Evaluation is distinct from traditional testing and crucial for continuous improvement <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

*   **Time Investment:** Building the code or automation for [[ai_agents_and_their_development | AI agents]] is only 25% of the effort; the remaining 75% is evaluating and adjusting the agent <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Behavioral Correctness:** Unlike testing for code correctness, evaluation focuses on "agent behavior correctness," ensuring the agent provides acceptable answers even if no error occurs <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Evaluation Methods:**
    *   **LLM as a Judge:** Using another large language model to evaluate the output of the agent <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
    *   **Task Completion Testing:** Assessing if the agent invoked necessary tools for tasks (e.g., updating a task in Asana, drafting an email) <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
    *   **Human Evaluation:** Gathering feedback from end-users through surveys or direct interaction <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Importance:** Evaluation ensures that the agents provide the desired results for the system being built or automated <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

### Phase 9: Mastering AI with Others
Learning with a community is vital for accelerating the mastery of [[ai_agent_development_challenges | AI agent development]] <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

*   **Community Benefits:** Mastering [[ai_agents_and_their_development | AI agents]] is challenging due to the power and unpredictability of LLMs. Finding a community for learning and collaboration significantly speeds up the process <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Dynamis AI Mastery Community:** A dedicated community offering:
    *   Collaboration with other early AI adopters <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
    *   Daily events like office hours and workshops <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
    *   AI agent templates and resources <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
    *   Daily support and idea sharing <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
    *   The "AI Agent Mastery course" which details the full process from planning to prototyping, building in Python, creating a front-end, and deployment <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

### Phase 10: Leveraging Your New Skill Set
Mastering [[ai_agents_and_their_development | AI agents]] opens up a versatile array of opportunities <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

*   **Personal and Business Automation:** Automate tasks in personal life or business operations <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   **Product Creation:** Create and sell [[ai_agents_and_their_development | AI agent]] templates or frameworks <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
*   **Service-Based Businesses:** Start an AI automation agency offering bespoke solutions <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
*   **Software as a Service (SaaS):** Build SaaS products powered by [[ai_agents_and_their_development | AI agents]] <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   **Consulting and Advisory:** Become an AI consultant or advisor for companies <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.
*   **Employment:** Join or start an AI-focused company, as this experience is valuable at the enterprise level <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Content Creation and Open Source:** Teach others through content creation or contribute to open-source [[ai_agents_and_their_development | AI agent]] projects <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.

The speaker emphasizes that [[ai_agents_and_their_development | AI agents]] are the future, and gaining this expertise provides immense versatility across all industries <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.