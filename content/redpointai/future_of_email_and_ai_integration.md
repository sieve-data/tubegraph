---
title: Future of email and AI integration
videoId: cIJ8hMLCboE
---

From: [[redpointai]] <br/> 

Email, despite perennial claims of its demise, continues to be a foundational communication tool, primarily because email addresses serve as critical, company-owned unique identifiers for individuals within organizations <a class="yt-timestamp" data-t="01:40:42">[01:40:42]</a>. This persistent role means that while the *form* of email will evolve, the underlying infrastructure of email addresses is here to stay <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

The future of email is marked by two significant trends: [[role_and_impact_of_ai_in_email_management | AI integration]] and enhanced collaboration features <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Superhuman's Approach to AI in Email

Superhuman, a "lightning-fast email tool," has strategically integrated [[role_and_impact_of_ai_in_email_management | AI]] features into its platform <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. Their AI development journey has progressed through distinct phases:

### Phase 1: On-Demand AI Features
This initial phase focused on features users had to actively remember to employ <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. These features were generally easier and cheaper to build and run, serving as a way to test the technology and user adoption <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

*   **Write with AI** <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>: Users jot down a few words, and the AI generates a full email, matching the user's existing voice and tone by analyzing previously sent emails <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. It also allows for shortening, lengthening, improving writing, fixing mistakes, and changing languages <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. This feature "went viral" upon its launch, demonstrating [[challenges_and_opportunities_in_ai_integration | AI]]'s potential to significantly boost product visibility <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>.

### Phase 2: Always-On AI Features
This phase involved more ambitious features that operate continuously in the background, working on the user's behalf <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. They are more challenging and costly to develop and run due to operating at massive scale <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. Superhuman has processed 4 billion emails for these features, vastly exceeding common LLM training corpuses <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

*   **Auto Summarize** <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>: Provides a one-line summary of an entire email conversation, updating instantly as new emails arrive <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. Users often find they don't need to read the full email, enabling faster processing <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
*   **Instant Reply** <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>: Generates draft replies for incoming emails, allowing users to simply edit and send, or sometimes send without any changes <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. This feature has demonstrably reduced email writing time by half <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>. Its value extends beyond speed, also providing inspiration and reducing the "activation energy" to respond to emails <a class="yt-timestamp" data-t="09:04:00">[09:04:04]</a>.

### Phase 3: [[future_of_ai_agents_in_productivity_tools | Agentic AI Future]]
The long-term vision is an "agentic AI future" where users have multiple autonomous AI agents, including an email agent, working on their behalf <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. These agents will be able to:
*   Receive goals, not just tasks <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   Plan and break down goals into subtasks <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   Handle ambiguity by asking questions and querying other systems like internal APIs or CRMs <a class="yt-timestamp" data-t="08:18:00">[08:18:18]</a>.
*   Interact with other agents <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
This future aims to free users to be more creative, strategic, and impactful <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.

## User Experience and Design Decisions for AI
Developing intuitive [[role_and_impact_of_ai_in_email_management | AI]] features required significant design innovation <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>. Key principles include:

*   **Visibility**: For Instant Reply, the suggestions are visible *before* a user starts typing, providing inspiration and reducing activation energy, even if the user doesn't reply to most emails <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.
*   **Minimalist Design**: Adhering to the principle of "when you want it and out of the way when you don't" <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.
*   **Reply Length**: Instant replies are intentionally short (one to two sentences) to match the user's desire for speed, enabling quick proofreading and sending <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a>.
*   **Interaction Speed**: Prioritizing keyboard shortcuts like "Tab and Enter" over arrow keys dramatically increased usability and speed (10 times faster) <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>.

## Prompt Engineering and Model Selection
Superhuman focuses heavily on prompt engineering rather than fine-tuning models <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>. This approach is preferred because fine-tuning is time-consuming, costly, and its benefits don't easily transfer across model updates <a class="yt-timestamp" data-t="25:06:00">[25:06:00]</a>.

*   They use multi-shot learning by incorporating previous emails a user has written to match their unique voice and tone <a class="yt-timestamp" data-t="25:39:00">[25:39:00]</a>.
*   Challenges include the fragility of prompts, where new model versions can unexpectedly break existing prompt functionality <a class="yt-timestamp" data-t="26:17:00">[26:17:00]</a>.
*   A robust regression testing and evaluation framework, utilizing tools like Brain Trust, is essential <a class="yt-timestamp" data-t="26:46:00">[26:46:00]</a>. This framework often uses [[role_and_impact_of_ai_in_email_management | LLMs]] to self-assess the quality of their own responses <a class="yt-timestamp" data-t="27:08:00">[27:08:00]</a>.
*   Superhuman chose OpenAI models due to their perceived 6-9 month lead in model quality, commitment to aggressively lowering costs, and deep collaborative relationship <a class="yt-timestamp" data-t="29:28:00">[29:28:00]</a>.
*   **Throughput and Latency**: For features like Instant Reply and Auto Summarize, peak throughput and low latency are more critical than raw model intelligence, especially given the bursty nature of email usage (e.g., all emails sent at 8:55 AM on Monday) <a class="yt-timestamp" data-t="31:44:00">[31:44:00]</a>. This means [[role_and_impact_of_ai_in_email_management | AI]] integration is constrained by model speed and hardware acceleration (like Groq) rather than just cost <a class="yt-timestamp" data-t="32:37:00">[32:37:00]</a>.

## Business Impact and Pricing
Superhuman, priced at $30/month, has shifted its revenue allocation from extensive onboarding (common in its early days) to funding [[role_and_impact_of_ai_in_email_management | AI]] features <a class="yt-timestamp" data-t="33:12:00">[33:12:00]</a>. The company aims to leverage its premium pricing to "build the fastest, most powerful AI email experience ever" <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>. Future pricing strategies are being explored for different business lines, including Superhuman for Sales and Enterprise <a class="yt-timestamp" data-t="38:27:00">[38:27:00]</a>.

## Competing with Incumbents in the Age of AI
While incumbents (like Gmail and Outlook) have advantages such as existing user bases and data, they are also "encumbered" by their size and legacy <a class="yt-timestamp" data-t="46:36:00">[46:36:00]</a>. Startups can compete by:

1.  **Targeting Underserved Segments**: Incumbents offer one-size-fits-all solutions. Startups can build superior products for specific, economically powerful sub-segments of the market <a class="yt-timestamp" data-t="48:17:00">[48:17:00]</a>.
2.  **Leveraging Product Speed**: Incumbents struggle to rebuild their platforms for speed, which was Superhuman's initial competitive advantage (instantaneous response, sub-100 millisecond user interactions) <a class="yt-timestamp" data-t="49:15:00">[49:15:00]</a>.
3.  **Superior Design**: Large organizations often have product structures dictated by internal teams rather than user logic (Conway's Law), leading to less intuitive designs <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>. Startups can prioritize user-centric design <a class="yt-timestamp" data-t="50:58:00">[50:58:00]</a>.

The email market is enormous, with billions of hours spent daily, providing ample opportunity for niche products to achieve significant scale <a class="yt-timestamp" data-t="54:21:00">[54:21:00]</a>.

## Overhyped vs. Underhyped in [[the_future_potential_and_development_of_ai_assistance_apis | AI]]

The idea that [[the_future_potential_and_development_of_ai_assistance_apis | AI]] is "coming for our jobs" is both underhyped and overhyped:

*   **Underhyped**: The speed at which [[the_future_potential_and_development_of_ai_assistance_apis | AI]] will impact *specific* entry-level roles (e.g., customer support, sales) is underestimated by the general public. [[the_future_potential_and_development_of_ai_assistance_apis | AI]] doesn't need to be perfect; if it's 80% as good but 10% of the cost, companies will adopt it widely <a class="yt-timestamp" data-t="56:04:00">[56:04:00]</a>.
*   **Overhyped**: The notion that only these specific roles are at risk is overhyped. [[the_future_potential_and_development_of_ai_assistance_apis | AI]] will eventually affect all jobs, including high-level ones like CEO, within decades <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>.

This shift will redefine "work" as it has throughout history, potentially leading to a future where what we perceive as leisure becomes the primary human activity <a class="yt-timestamp" data-t="57:10:00">[57:10:00]</a>.

## The Future of Workplace Communication
Email's enduring strengths lie in its structured conversations (subject lines, chronological replies, at-a-glance views), ability to mark things as done or snooze, and future capabilities like assigning and commenting on threads <a class="yt-timestamp" data-t="59:22:00">[59:22:00]</a>. Traditional chat platforms like Slack, while offering real-time interaction, lack this structure, leading to overwhelming unread channels and difficulty in tracking conversations <a class="yt-timestamp" data-t="00:59:58">[00:59:58]</a>.

The ideal [[the_future_of_human_communication | future of workplace communication]] would combine the best of both worlds: a platform designed for "thoughtful asynchronous discussion" with clear subject lines, archiving, snoozing, and assignment capabilities, alongside integrated chat options, allowing users to choose the modality <a class="yt-timestamp" data-t="01:01:18">[01:01:18]</a>. This convergence would allow companies to be run more effectively and reduce stress for professionals <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>.

This future heavily relies on the development of [[future_of_voice_ai_and_its_impact | AI agents]] that can understand user priorities, manage communication across platforms (email, chat, calendar), and organize work, allowing individuals to focus on consistent progress without anxiety <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>. This aligns with Superhuman's mission to help professionals feel happier, more productive, and closer to achieving their potential <a class="yt-timestamp" data-t="01:03:41">[01:03:41]</a>.