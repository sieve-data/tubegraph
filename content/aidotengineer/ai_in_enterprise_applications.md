---
title: AI in enterprise applications
videoId: z4zXicOAF28
---

From: [[aidotengineer]] <br/> 

The current wave of [[AI in Workplaces]] represents a significant revolution in technology, comparable to only a few others seen in decades [01:27:27]. Unlike previous technological hypes like blockchain or NFTs, the impact of AI is demonstrably real, evidenced by widespread user adoption and substantial revenue generation [01:47:48].

## Early Adoption & Real-World Impact

[[Introduction and application of AI in business platforms | AI's application in business platforms]] is already showing significant traction:
*   **ChatGPT** achieved 100 million users faster than any consumer product in tech history, with millions using it daily for various tasks, from writing essays to legal citations, and for legitimate business purposes hundreds of millions of times a day [01:08:02].
*   **GitHub Copilot** boasts millions of subscribers and is integrated into Microsoft 365, reaching 84 million everyday consumers [01:08:35]. This signifies a shift from mere "pair programming" to "peer programming," where Copilot acts as a teammate that can live in a codebase, operate in branches, and run tests until tasks are complete [01:39:26].
*   **Azure AI** is adopted by enterprises, generating an estimated $13 billion in annual revenue [01:48:46].
*   **AWS** is investing significantly, with $87 billion allocated for [[AI in IT infrastructure management | AI infrastructure]] in the current year [01:07:07].

This widespread adoption by major tech companies and consumers indicates a fundamental shift, moving AI from demos into full production [01:13:13].

## Key Drivers and Trends in Enterprise AI

### The Rise of AI Agents
AI agents are increasingly central to enterprise applications. Microsoft envisions an "agentic web" where agents interact with tools, models, and other agents across different clouds, companies, and devices [01:38:04]. This paradigm shifts the focus from software factories to "agent factories," where the output is behaviors, not just binaries [01:38:33].

Examples of agentic capabilities include:
*   **Codebase improvement**: Agents can continuously improve codebases, addressing maintenance which previously competed with new features [01:39:57]. Microsoft's FSY tool uses a "graph RAG" approach for codebases to reason, explain, and fix areas [01:40:04].
*   **Personalized development**: GitHub Copilot, through open-sourced extensions, now understands specific patterns, domains, and teams, allowing for more tailored assistance [01:40:26].
*   **Automated tasks**: GitHub Copilot can be assigned tasks like writing a README file and execute them live [01:42:42].
*   **Multi-agent systems**: Microsoft demonstrated a multi-agent event planner ("Build Events") powered by a voice-controlled agentic orchestrator that dynamically delegates tasks to sub-agents for research, email drafting, image generation, and social media posting [01:52:24]. These agents can operate simultaneously, with the research agent accessing speaker lists, attendees, and web search, and image and content agents working concurrently [01:54:47].

The concept of an "agent" can be defined as software that plans steps, includes AI, takes ownership of a task, holds a goal in memory, and can try different hypotheses and backtrack [01:07:13]. The number of agent startups has increased by 50% in the last year, with many showing real-world utility [01:08:02].

### Multimodality and its Business Impact
Beyond text-based AI, other modalities like voice, video, and image generation are progressing rapidly, with companies like HeyGen, ElevenLabs, and Midjourney achieving significant annual recurring revenue (ARR) [01:08:11]. This extends beyond niche verticals, with applications in various economic sectors. For example, voice is expected to impact business workflows first due to its natural communication mode, from medical consults to lead generation [01:09:55]. As these modalities become more controllable and less costly, their adoption will increase [01:10:15].

### Competitive Model Landscape
The market for AI model capabilities is becoming increasingly competitive. OpenAI's CEO, Sam Altman, stated that "last year's model is a commodity," reflecting the rapid decrease in model costs [01:10:48]. For instance, GPT-4's cost per million tokens dropped from $30 to $2 in about 18 months, with distilled versions at 10 cents [01:10:59]. This competition among major AI labs (Google, Anthropic, OpenAI) and new players like DeepSeek ensures continuous capability improvement and lower costs for builders [01:11:10].

## Building Successful AI Applications for Enterprises ("Cursor for X" Playbook)

The success of tools like Cursor (a code editor for AI) offers a playbook for [[building_and_scaling_ai_use_cases_for_enterprises | building and scaling AI use cases for enterprises]] across industries [01:14:01].

### Leveraging Domain Expertise
Instead of building generic text boxes, successful AI products leverage deep domain and workflow knowledge. They show up informed, automatically collect and package context (not just natural language), use the right models at the right time (orchestration), and present outputs thoughtfully [01:15:47]. This requires understanding the workflow intimately [01:13:58].

### The "AI Leapfrog" Effect
Surprisingly, some of the most conservative, low-tech industries are adopting AI fastest. Examples include:
*   **Sierra**: Resolves 70% of customer service queries for clients like SiriusXM or ADT [01:17:20].
*   **Harvey**: Has over $70 million ARR, making AI essential for competitiveness in the legal industry [01:17:31].
*   **Open Evidence**: Helps doctors stay updated with medical research, reaching a third of US doctors weekly with daily average usage [01:17:41].

These companies succeed by deeply understanding their customers and solving real problems, demonstrating significant value beyond generic chatbot applications [01:18:05].

### Augmentation Over Full Automation
While there is excitement about full automation and "agents," co-pilots (AI systems that augment human capabilities) are currently underrated for driving revenue [01:19:01]. The analogy of Iron Man's suit is apt: it augments Tony Stark, allowing him to do amazing things, but can also perform basic tasks independently [01:19:08]. Human tolerance for AI failure or hallucinations drastically reduces as latency increases, making augmentation the path of least frustration for many domains [01:19:21].

### Execution as the Moat
In the AI landscape, execution is often the most significant moat. Companies that ship great experiences faster and capture user trust, even if they didn't invent the underlying technology or product surface area, tend to succeed [01:22:01]. This contrasts with earlier AI products that relied solely on prompts and good SEO but struggled to maintain relevance as models evolved rapidly [01:22:29]. The constant evolution of AI capabilities means the "game board" is always being shaken up, creating continuous opportunities for those who can reimagine experiences and execute quickly [01:23:43].

## The Role of Model Context Protocol (MCP) in Enterprise Integration

The Model Context Protocol (MCP) is emerging as a foundational shift for integrating AI into enterprise systems.

### Solving "Copy and Paste Hell"
Before MCP, users often engaged in "copy and paste hell," manually transferring context between different AI tools, PDFs, and productivity suites [02:29:56]. MCP was designed to allow LLMs to "climb out of their box," reach into the real world, and bring context and actions directly to the model [02:33:48]. Its open-source and standardized nature is crucial for enabling this at scale [02:34:21].

### MCP for Internal Operations
Anthropic's internal adoption of MCP for automating workflows, including PR review bots and Slack management tools, highlights its utility within large organizations [02:35:41]. This standardization helps avoid "integration chaos" by providing a single approach for engineers, allowing them to focus on unique problems rather than repetitive plumbing tasks [02:51:39]. Features like sampling primitives within MCP can simplify complex internal needs like tracking usage and billing across different products [02:55:54].

Microsoft's Azure AI Foundry uses MCP as a core component of its agent factory, enabling multi-agent applications and facilitating the transition from shipping binaries to shipping agents that can retrain, redeploy, and change post-deployment [01:46:46].

### Building MCP Servers for Enterprises
Building MCP servers for enterprise use requires careful consideration:
*   **Beyond API Wrapping**: An MCP server is not simply an OpenAPI wrapper [02:45:41]. It requires designing around how models reason and react to context, often by providing information in human-readable formats like Markdown [03:25:57].
*   **Three Users**: Builders must consider three types of users: the end-user, the client developer, and the AI model itself. The model, as a user, needs tools exposed in a way that enables it to respond correctly to prompts [02:45:58].
*   **Authentication**: Implementing OAuth 2.1 support for remote MCP servers is essential for B2B SaaS companies, though it can be complex [03:25:08]. Centralized authentication models, like Anthropic's MCP gateway, simplify credential management for consumers and ensure portability of credentials [03:01:06].
*   **Client Support**: The ecosystem is still maturing, with only a handful of clients (like VS Code Insiders and Cloud Desktop) offering full and stable OAuth support for remote MCP servers [03:28:54].
*   **Cost Management**: Since the cost of token usage can be passed on, being mindful of the data returned by an MCP server is crucial to avoid excessive expenses [03:31:52].
*   **Dynamic Capabilities**: MCP supports dynamic discovery, allowing a server to offer tools relevant to the current context (e.g., a "battle" tool appearing only when a monster is present in a game) [03:09:16]. Features like "sampling" allow servers to request LLM completions from the client for tasks like summarizing resources or formatting data [03:11:41].
*   **Debugging**: Tools like VS Code's dev mode simplify debugging MCP servers by allowing direct debugger attachment [03:13:30].

### Challenges and Considerations
**Security** is a paramount concern for [[implementing_ai_in_enterprises | implementing AI in enterprises]], especially when applications have access to private data and can interact with the outside world [02:48:25]. The "lethal trifecta" arises when an AI system with access to private data is exposed to malicious instructions and has a mechanism to exfiltrate information [01:42:36]. Prompt injection remains a risk, and organizations must ensure that only trusted MCP tools are allowed to prevent severe consequences [03:28:34]. Auditing and observability are critical, with Microsoft integrating OpenTelemetry for continuous monitoring regardless of the agent's build platform [01:48:11].

## Future Outlook and Opportunities

The current era is likened to the "dial-up era of AI," rapidly moving towards "broadband" capabilities [01:23:19]. This presents immense opportunities for those who can build revolutionary products [01:24:28].

Opportunities include:
*   **Machines interrogating humans**: Collecting data on demand from people who were previously inaccessible [01:20:16].
*   **Proactive problem-solving**: Root causing every alert proactively rather than just firefighting [01:20:28].
*   **Scalable knowledge workers**: Building applications as if an organization had an army of compliant, infinitely patient knowledge workers [01:20:35].
*   **Hard sciences**: Applying AI to problems not found in common crawl data, such as robotics, biology, material science, physics, and simulation. These require clever data collection and interaction with atoms rather than just bits [01:20:48].

The transformative potential of [[AI Enhanced vs AI Native Businesses | AI in enterprise applications]] is still early, and engineers are uniquely positioned to translate these new capabilities for the rest of the world [01:24:21].