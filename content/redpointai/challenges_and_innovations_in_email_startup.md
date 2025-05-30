---
title: Challenges and innovations in email startup
videoId: cIJ8hMLCboE
---

From: [[redpointai]] <br/> 

Superhuman, an email tool, has significantly impacted the tech world, particularly with its integration of artificial intelligence (AI) features <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The company's CEO, Rahul Vohra, discussed the future of email, the [[role_and_impact_of_ai_in_email_management | role of AI]], and strategies for [[building_ai_startups_and_the_challenges_of_scaling | building AI startups]] while [[competing_against_tech_incumbents_like_gmail_and_outlook | competing against tech incumbents like Gmail and Outlook]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Enduring Nature of Email

Despite perennial claims by journalists, email continues to be a fundamental communication tool <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This persistence stems from the email address's role as a unique, company-owned identifier essential for joining organizations and logging into various systems like SSO solutions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Superhuman's AI Innovations

Superhuman embarked on its generative AI journey in February 2023, building upon prior AI efforts like auto-correct, released in January 2022 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Rahul Vohra recognized the transformative potential of large language models (LLMs) after attending a conference in early 2023, leading to a strategic shift to prioritize AI development <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

### Phased Approach to AI Development

Superhuman adopted a strategic roadmap for AI integration, progressing through distinct phases <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>:
1.  **On-Demand AI Features:** These require users to actively remember to use them. They are generally easier and cheaper to build and run, serving as a way to test technology understanding and user adoption <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
2.  **Always-On AI Features:** More ambitious, difficult, and expensive to run due to their continuous operation and massive scale <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. For example, Superhuman has processed 4 billion emails since launching auto-summarize and instant reply, vastly exceeding typical LLM training corpuses <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
3.  **Agentic AI Future:** The ultimate vision, involving mostly autonomous AI agents that can handle goals (not just tasks), plan, resolve ambiguities, and interact with other agents to free up human time for creative, strategic, and impactful work <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

### Key AI Features

Superhuman has launched three flagship AI features:
*   **Write with AI:** Users jot down a few words, and the AI generates a full email matching their voice and tone. It also offers options to shorten, lengthen, improve writing, fix mistakes, and change language <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Auto-Summarize:** Provides a one-line summary of an entire email conversation, updating instantly with new emails. Users can also access a bullet-point summary <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This feature often eliminates the need to read the full email, saving time <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Instant Reply:** Generates draft replies for incoming emails, allowing users to simply edit and send, sometimes without any edits <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Impact and Metrics

The impact of these AI features has been significant:
*   Users of Instant Reply write emails twice as fast, reducing time spent by half <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   The feature provides inspiration, helping users reply to emails they might otherwise have left unanswered <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   AI features have made Superhuman "top of mind for everybody again," contributing to significant growth in new monetized retained seats <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

## Team Structure and Rapid Shipping

To rapidly ship AI features, Superhuman adopted a unique operating model alongside their standard "Alpha mode" (autonomous teams accountable to goals) <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>:

### Theta Mode Operating Model
In "Theta mode," an embedded executive (like the CEO) carries the project goal and performs individual contributor work daily <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. This mode is reserved for existential projects that "can't fail" and are designed to move "really really fast" <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. The AI team, initially staffed with one designer, one marketer, and two or three engineers, operated in this mode to develop the generative AI features <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

## Product Design Philosophy for AI

Designing AI features required novel approaches, as there was no existing playbook for user interfaces <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

### Instant Reply Design Journey
Key design decisions for Instant Reply included:
*   **Visibility:** Initially, there was debate whether reply suggestions should be visible before a user starts typing. It was realized that showing them constantly provides "goddamn inspiration" and lowers the activation energy to reply, even if the user just needs to see options <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Minimality:** Superhuman's principle is "when you want it and out of the way when you don't" <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. The visual design ensures the suggestions are tucked away but always present.
*   **Reply Length:** Unlike "Write with AI" (which generates medium-length replies), Instant Reply was designed to produce very short, snappy responses (one to two sentences) <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This matches the user's desire to move quickly, allowing for a quick edit and send <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Interaction Design:** Shifting from arrow keys to `Tab` and `Enter` for selecting replies dramatically improved usability and speed <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

### Importance of UI/UX over Prompt Engineering
While prompt engineering is crucial, the *interface itself* was key to Instant Reply's effectiveness <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. The ability to `Tab` and `Enter` quickly is fundamental <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

Superhuman avoids extensive fine-tuning of models, opting to push prompt engineering as far as possible <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. They rely on multi-shot learning (showing other emails the user has written) to match voice and tone <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>. To manage prompt iterations and model updates, they use Brain Trust, an evals framework, for robust regression testing <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

## Strategic Technology Decisions

### Choosing OpenAI Models
Superhuman chose OpenAI models due to their perceived 6-9 month lead in model quality and demonstrated commitment to aggressively lowering costs <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. The company also benefits from a deep collaborative relationship with OpenAI <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.

### Cost and Throughput Considerations
While costs are important, throughput and latency are often more critical <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. Superhuman uses GPT-3.5 Turbo for Instant Reply and Auto-Summarize because its higher tokens-per-minute limit can handle the "bursty" nature of email traffic, especially during peak times like Monday mornings <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>. The expectation is that edge LLMs running on devices will eventually make these costs less significant <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

### Pricing Strategy
Superhuman's retail price has remained $30 a month for eight years, despite being a much more advanced product <a class="yt-timestamp" data-t="00:38:10">[00:38:10]</a>. Initially, extra revenue went into concierge onboarding and training <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>. Now, with 85% self-service onboarding, those funds have been reallocated to AI development <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. The company is exploring future pricing models for its "Superhuman for Sales," Enterprise solutions, and a potential "platinum edition" <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>.

## [[challenges_in_ai_adoption_for_startups | Overcoming User Adoption Challenges]]

For AI startups, the "core trick" for user adoption is to start with "always-on" features (like Auto-summarize and Instant Reply) and then connect them to "on-demand" features (like Write with AI) <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>.

> [!info] The Power of "100% Reach Features"
> Rahul emphasizes building features that will be used by everyone. "100% reach features are so vanishingly rare that when you have the opportunity to build you should build them" <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>. The main reason startups fail to make progress is building features that people don't use <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. By connecting always-on features to on-demand ones, users are implicitly taught how to use the latter <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.

## [[competing_against_tech_incumbents_like_gmail_and_outlook | Competing with Incumbents]]

While incumbents may have an advantage in AI due to existing user bases and data, they are still "encumbered" and move slowly <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. Rahul actively seeks out founders who target incumbents because it can be a "really great strategy" <a class="yt-timestamp" data-t="00:48:04">[00:48:04]</a>.

### Incumbent Disadvantages
*   **One-Size-Fits-All Solutions:** Large incumbents like Microsoft Outlook (400M+ paid seats) and Gmail (1B+ users) must cater to a vast, diverse user base, leading to generic solutions <a class="yt-timestamp" data-t="00:48:14">[00:48:14]</a>. Startups can build a better product for an "underserved yet economically powerful sub-segment" <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
*   **Product Speed:** Incumbents struggle with speed. Superhuman was built on the platform of speed, offering instantaneous response and search (sub-100 milliseconds) <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. Their architecture, being the first email client entirely written in JavaScript, is difficult for older, client-server incumbents to replicate <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.
*   **Design and Conway's Law:** Product design in large organizations often reflects the internal organizational structure rather than user logic <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. This can lead to fragmented, non-intuitive user experiences, unlike startups that can design holistically around the user <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>.

## The [[future_of_email_and_ai_integration | Future of Email and AI]]

The [[future of email and AI integration | future of email]] involves agentic AI and enhanced collaboration features <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Superhuman is already building team features like team read statuses, reply indicators, and snippets, with plans to allow sharing and commenting on threads <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Agentic AI Vision
The future will involve multiple AI agents, potentially including an email agent, that are mostly autonomous <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. These agents will:
*   Be given "goals, not tasks" <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Plan and break down goals into subtasks <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   Handle ambiguity by asking questions or interrogating other systems (e.g., internal APIs, CRM) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Interact with other agents <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This agentic future will free humans to be more creative, strategic, and impactful <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Superhuman's position as a "three-hour-a-day product" (like chat and messaging) gives it a strategic advantage to be the primary "pane of glass" where users interact with these agents <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>.

### Vision for Workplace Communication (Critique of Slack)
Email excels in ways that team chat applications like Slack do not <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>:
*   **Ordered Conversations:** Email conversations are ordered by last reply, unlike Slack where they are ordered by when they started <a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>.
*   **Subject Lines:** Email provides at-a-glance subject lines, which are often missing or manual in Slack <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.
*   **Task Management:** Email allows marking items as done, snoozing, assigning threads, sharing, and commenting <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>.
*   **Inbox Zero:** The concept of an inbox that can be cleared <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

Rahul envisions combining the best of both worlds to build a "workplace experience of the future" designed for thoughtful asynchronous discussion, with options for chat modalities, while maintaining the organizational benefits of email <a class="yt-timestamp" data-t="01:01:18">[01:01:18]</a>.

## Investment Perspective on AI Startups

Rahul and Todd (his co-host) are generally "bearish on most de novo AI companies" because they often try to build a new app *with* AI, essentially building two companies at once <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>.

> [!tip] Investment Focus
> "Where I was bullish and continued to be bullish is if you have some kind of distribution advantage... AI is kind of incidental. AI might be a hook, but it's it's sort of incidental" <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>. This includes founders with strong contacts, viral loop insights, or a proven track record in launching products <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.

The email market is enormous, with a billion professionals spending an average of 3 hours daily on email, totaling trillions of hours annually <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>. This large addressable market allows for substantial businesses to be built even by targeting a small segment, demonstrating that a company can be "a several billion dollar company" with 300,000 subscribers <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.

## Societal Impact of AI (Jobs)

The idea that [[role_and_impact_of_ai_in_email_management | AI is coming for our jobs]] is both underhyped and overhyped <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a>.

*   **Underhyped:** Many people outside of tech don't yet grasp how quickly AI will impact specific entry-level roles like customer support or sales <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>. AI doesn't need to be perfect; if it's 80% as good at 10% of the cost, companies will adopt it <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>.
*   **Overhyped:** The focus on customer service and sales roles overlooks that AI's impact will extend to almost all jobs, including those of CEOs <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>.

Drawing a historical parallel, people a thousand years ago would view modern jobs as "just playing" <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>. Similarly, in 50 years, current jobs may seem like leisure. Bertrand Russell's view is that even when AI does most work, humans are "hardwired to work and to get stressed about stuff and to play Silly games of status," so it won't feel like leisure to them <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>.

Rahul believes that a healthy attitude toward work is paramount, allowing for consistent progress without constant anxiety, a vision central to Superhuman's mission to help professionals feel happier, more productive, and closer to achieving their potential <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>.