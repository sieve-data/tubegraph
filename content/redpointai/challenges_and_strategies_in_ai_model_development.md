---
title: Challenges and strategies in AI model development
videoId: GlBY-zbwaXU
---

From: [[redpointai]] <br/> 

Developing AI models, particularly in specialized fields like law, presents unique [[challenges and advancements in AI model development | challenges and advancements]]. The rapid evolution of AI models and supporting frameworks necessitates strategic decisions regarding development focus, resource allocation, and long-term viability.

## Evolution of AI in Legal Applications

Initially, in 2020, AI models like early BERT models were found to be decent in English but "horrendously bad" in Swedish for legal applications [00:01:46]. The arrival of GPT 3.5 marked a "paradigm starter," shifting the industry from pure experimentation to implementing practical, end-to-end solutions [00:01:52]. For instance, due diligence processes that once required physical presence and manual review now involve uploading documents to platforms like Lorra, specifying requirements, and generating reports based on the findings [00:02:08]. This progression demonstrates a move from simple queries against data sets to defining processes for LLMs to follow, where agents are given tools to plan and execute tasks [00:02:29].

## Key Strategies in Model Development

### Leveraging Surrounding Frameworks
While AI models themselves are continuously improving, significant leverage is gained from surrounding frameworks such as function calling, tool calling, and multi-chain prompting (MCP) [00:02:53]. These frameworks enable integration of various functionalities that were previously fragmented into separate tools (e.g., translations, document comparisons, searching, reviewing) [00:03:09]. This integration allows for a more cohesive platform that can handle tasks ranging from simple data extraction to complex document drafting [00:03:21].

### Build vs. Integrate Decision-Making
A core strategy revolves around deciding what to build internally versus what to rely on external AI labs for [00:14:24]. The philosophy is that if AI labs (like OpenAI, Claude, Gemini) are likely to build a feature and make it available to developers, then it should not be built internally [00:14:27]. This approach allows applications to improve as the underlying models and platforms evolve, analogous to "all the functionality just gets better" when the tide rises [00:14:40].

An example of this is the "playbooks" feature in Lorra, which currently allows users to define negotiation rules for documents [00:14:46]. However, if future models become capable of processing such playbooks from simple documents and applying them, the need for building that specific feature in the same way might become unnecessary [00:15:22]. Similarly, complex multi-step workflows, traditionally built with node-based builders, can increasingly be handled by LLMs capable of planning and executing tasks on the fly, given access to the right tools [00:15:43].

This decision-making requires anticipating future model capabilities. For instance, Lorra built its own citation feature early on because it was critical for legal use cases, but with AI providers like Claude and Anthropic releasing citations as part of their API, such custom code may eventually be deprecated [00:17:02].

### Prioritization and Cohesive Platform Design
One of the hardest parts of [[challenges in building and deploying AI features | building AI features]] today is prioritizing among a hundred high-value opportunities and ensuring they form a cohesive platform [00:17:31]. Without careful planning, companies risk building a "Frankenstein monster" by chasing every "next hot thing" [00:17:49]. It is crucial to plan how the platform will look and be structured, considering aspects like data organization and shared projects [00:18:08]. This requires aligning with evolving client expectations for technology application in the legal field [00:18:36].

### Model Selection and Optimization
As models improve but also become more expensive, a strategy for [[challenges and optimizations in ai model training and inference | optimization]] involves selecting the right model for the task [00:20:07]. Lorra increasingly uses classification algorithms and "model pickers" to choose the most appropriate model, balancing capability with cost, asking whether a "bazooka" or a "handgun" is needed for a specific task [00:20:25].

## Overcoming Challenges in Adoption and Infrastructure

### User Onboarding and Expectation Management
Teaching lawyers to use AI tools has proven to be "way more work" than initially anticipated [00:12:44]. Unlike traditional software rollouts, where 5-10% adoption might be considered good, AI tools like Lorra are seeing adoption rates of 70-80% because lawyers are actively seeking access [00:13:00]. However, managing user expectations remains a challenge; while some attorneys are tech-savvy and set up workflows with templates and prompt libraries, others may expect the tool to "write me an SPA" from a simple query, leading to disappointment if it doesn't work as expected [00:37:48]. This necessitates extensive training and onboarding programs [00:38:13].

### Infrastructure Gaps and Tooling
In terms of [[challenges and opportunities in ai infrastructure development | infrastructure]], multi-chain prompting (MCP) or tool-calling is considered both underhyped and overhyped [00:37:10]. While it offers fundamental capabilities for universal applications by allowing AI to call outside tools (like redlining documents), its full production use still requires addressing challenges around authentication and other technical aspects [00:21:06]. A significant opportunity arises when clients can provide their own tools for the AI to access, such as client-specific CRMs, knowledge databases, or notification systems, greatly expanding the scope of possibilities [00:21:13].

### Reliability and System of Record Status
Ensuring reliability is paramount, especially when working with law firms [00:29:43]. If an attorney's query doesn't work, they tend not to return, making reactivation difficult [00:29:36]. Initial challenges included reliability, infrastructure, chunking, and ensuring the Retrieval-Augmented Generation (RAG) system met expectations [00:29:45]. As Lorra became a system of record for end-to-end legal deliverables, expectations for uptime and performance became "incredibly high," leading to immediate contact if issues arise [00:30:16]. This shift requires moving from rapid "ship it as soon as we have something" to working with design partners for proper, robust launches [00:30:50].

## Organizational and Cultural Dynamics

### Founder-Led Pace and Urgency
The pace of development in AI companies is exceptionally fast, requiring constant adaptation and high velocity [00:31:02]. Max Unistrom emphasizes a culture of urgency, with a co-founder coding 14 hours a day [00:32:25]. This drive trickles down throughout the organization, from engineering and product to go-to-market teams [00:31:27]. Recruitment explicitly sets the expectation that it's "not a 9 to 5 job" but a mission to build for the future [00:32:48].

### Strategic Market Entry
Starting in a smaller, fragmented market like the Nordics allowed Lorra to become a dominant player ("crocodile in a smaller pond") before expanding to larger markets like the US [00:08:58]. This approach provided an advantage as a "fast second mover," allowing observation of what worked and what didn't for others [00:09:43]. Instead of focusing on training their own LLMs with limited funding, Lorra prioritized building an application layer that users would be excited about [00:10:07]. This also meant being "enterprise ready" when entering new markets, leveraging referrals from well-connected law firms [00:11:52].

### Adapting to a New Growth Paradigm
The AI era has created a new expectation for how quickly software companies can grow [00:35:44]. Unlike the SaaS era where companies often started with SMBs before moving to enterprise, AI companies can target enterprise clients from day one, often creating entirely new product categories rather than replacing existing software [00:35:51]. This demands high velocity and focus on product and service quality to dominate the market [00:36:09]. Lorra, for example, started with large enterprise clients and invested heavily in certifications like SOC and ISO from the outset to meet their stringent requirements [00:36:18].

## Future Outlook

The legal profession, particularly in areas like depositions, can greatly benefit from multimodal AI applications [00:41:00]. Uploading audio files, transcribing them, and treating them as searchable documents allows for efficient interrogation of information that previously required manual notation [00:41:26]. The future of legal skills will shift from simply following instructions to embodying entrepreneurial and creative thinking, challenging existing methods [00:42:30]. Lawyers will increasingly need to be fluent in working with AI and act as managers of AI agents from day one [00:43:00].