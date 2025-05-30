---
title: Data security and compliance with AI
videoId: vuKCZxhD4lU
---

From: [[customaistudio]] <br/> 

## Addressing Data Security Concerns with AI Solutions

When developing AI solutions, particularly for sensitive industries like insurance, handling Personally Identifiable Information (PII) and ensuring data security and compliance are paramount concerns <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Clients often inquire about the approach to guardrails and aligning with their requirements <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

### Technical Safeguards

Key technical measures for securing data in AI-driven systems include:
*   **Encryption at Rest**: Ensuring all data stored is encrypted <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
*   **Strict Row-Level Security**: Implementing granular security at the database level to control data access <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
*   **Platform Choice**: Utilizing robust platforms like Superbase, which offers features such as authentication, edge functions, and real-time updates while ensuring data security <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>, <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>, <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>, <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.
*   **Multi-tenant vs. Single-tenant**: Considering a multi-tenant architecture when building the system, provided it is securely locked down <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

### Process and Traceability

Compliance ultimately comes down to the tools used and the processes followed <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.
*   **Audit Trail**: Maintaining an audit trail of all transactions and communications, both between AI agents and with humans, to ensure traceability of data touchpoints <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>, <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.
*   **Tool Compliance**: Leveraging platforms like Naden, Superbase, or Lovable (for front-end) which are designed to be compliant <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   **Data Handling Guidelines**: Following established guidelines for how the team handles data internally <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.

While some information in industries like insurance might be public, it is crucial to be very careful to prevent users from seeing other people's information <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

## Human in the Loop for Compliance and Quality

Sanctifi's core belief is that humans remain special, particularly for compliance-related tasks <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>, <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. The vision is for AI to complete tasks up to a certain point, requiring human approval, especially if a specific certification is needed <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>, <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

### Marketplace for Certified Human Input
A marketplace is being explored where AI agents act as buyers, seeking humans with specific certifications (e.g., lawyers for legal compliance, doctors for medical sign-offs) to perform tasks <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>, <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>. This system would involve:
*   **Smart Contracts and Ledgers**: To track budgets, job offers, contracts, and fulfillment <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>, <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.
*   **Performance Tracking**: Recording metrics like success rates and acceptance rates for human workers to help AI agents find the most suitable expert <a class="yt-timestamp" data-t="00:52:18">[00:52:18]</a>.
*   **MCP Server Integration**: The MCP (Multi-party Computation Protocol) server facilitates this by allowing any client (e.g., [[integrating_ai_tools_into_operational_processes | Naden]], Claude, LangChain) to point to an endpoint and discover a directory of workers and task types <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>, <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.

This approach leans into "gig work," where humans with specific expertise provide final discretion or "human magic" that AI outputs might lack, ensuring quality and alignment with human intent and social context <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>, <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>. It addresses the potential for AI-generated content to become an "echo chamber" lacking new, fresh human perspectives <a class="yt-timestamp" data-t="00:43:17">[00:43:17]</a>.

## Future Considerations: AI as Consumers

The idea of AI agents making purchases presents significant downstream effects <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>. If AI becomes the capital allocator and consumer, the language of marketing and transactions could shift from human-focused to AI-focused <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>. This raises questions about manipulation and transparency in AI decision-making <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>, <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>. It also opens up possibilities for AI to use a "hidden language" (similar to SEO) to navigate and find products or services <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.