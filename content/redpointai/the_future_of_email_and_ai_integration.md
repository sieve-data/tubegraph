---
title: The Future of Email and AI Integration
videoId: cIJ8hMLCboE
---

From: [[redpointai]] <br/> 

Email remains an indispensable communication tool, despite perennial predictions of its demise <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Rahul Vohra, CEO of Superhuman, highlights that the persistence of email is less about the email format itself and more about the email address serving as a foundational digital identity <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Email addresses are company-owned identifiers, unlike personal phone numbers, making them crucial for corporate systems like SSO solutions (e.g., Okta, Rippling) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Key Future Themes for Email

The evolution of email will primarily revolve around two major themes:
1.  **Artificial Intelligence (AI)**: Specifically, an [[the_role_of_ai_agents_in_email_management|agentic AI future]] where AI agents operate around users' inboxes <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Collaboration**: Enhanced team features such as shared read statuses, reply indicators, snippets, and the ability to share and comment on email threads <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## Superhuman's AI Feature Development Strategy

Superhuman, an email tool that integrates [[applications_of_ai_in_email_management_and_debugging|AI features]], has adopted a phased approach to AI development <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This strategy began its generative AI journey in February 2023 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

### Three Flagship AI Features
1.  **Write with AI**: This feature allows users to jot down a few words, which are then transformed into a fully written email, matching the user's voice and tone from previously sent emails <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Users can then shorten, lengthen, improve, or translate the text <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  **Auto Summarize**: Launched in Fall 2023, this feature provides a one-line summary above an email conversation that updates instantly as new emails arrive <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. It changes the way people work, often eliminating the need to read the full email <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  **Instant Reply**: Released recently, this feature drafts replies for every incoming email, allowing users to simply edit and send, often without any changes <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Users of Instant Reply write emails twice as fast, demonstrating [[role_of_ai_in_future_business_operations|real business impact]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Phased Roadmap Strategy
*   **Phase One: On-demand AI Features**: These features (like Write with AI) require the user to actively remember to use them. They are generally easier and cheaper to build and run, serving as a way to test the technology and user adoption <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Phase Two: Always-on Features**: These are more ambitious, difficult, and expensive to run, as they are constantly working for the user (like Auto Summarize and Instant Reply) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Superhuman has processed 4 billion emails since launching these features <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Phase Three: Agentic AI Future**: This is the ultimate goal, where multiple autonomous AI agents handle goals (not just tasks) by planning, breaking down tasks, resolving ambiguity, and interacting with other systems and agents <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This future aims to free users to be more creative, strategic, and impactful <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Developing AI Features

### Team Structure and "Theta Mode"
Superhuman adopted a "Theta mode" operating model for AI development, distinct from their default "Alpha mode" <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. In Theta mode, an executive (in this case, the CEO) is embedded directly into the team, performing individual contributor work <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This signals the existential importance of the project, allowing it to move very quickly <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

### Design Decisions and User Interface
Key design decisions are crucial for AI feature usability. For Instant Reply, it was initially debated whether the reply options should be visible before a user starts typing <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. It was realized that showing options instantly provides "inspiration to reply," lowering activation energy <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

Another critical design choice was the length of replies; Instant Reply generates very short, snappy responses (one to two sentences) <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This matches the "impedance" of a fast-moving user, preventing the need for lengthy proofreading <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. The interaction design, such as using "Tab and Enter" instead of arrow keys for selection, significantly improved speed and usability by a factor of ten <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

### Prompt Engineering and Evaluation
Superhuman aims to avoid fine-tuning LLMs as much as possible due to time, cost, and transferability issues when models update <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>. Instead, they push prompt engineering to its limits, leveraging "multi-shot learning" (using other emails written by the user) to match individual writing styles <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

To ensure prompt quality and prevent breakage with new model versions, Superhuman uses a robust regression testing and evaluation framework (e.g., Brain Trust) <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>. This framework includes LLMs assessing their own responses for accuracy in addressing topics and recipients, and appropriate length <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.

## Model Selection and Cost

Superhuman primarily builds on OpenAI models, believing them to be 6 to 9 months ahead in model quality <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>. While OpenAI has a lead in model quality, speed is tremendously important for Superhuman's use cases <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. They also appreciate OpenAI's commitment to aggressively lowering costs <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>.

For features like Instant Reply and Auto Summarize, peak throughput and low latency are critical due to bursty usage patterns (e.g., everyone sending emails at 8:55 AM on Monday) <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. GPT-3.5 Turbo is currently more feasible than GPT-4 Turbo for these applications due to higher tokens-per-minute limits and better latency <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>. The long-term vision anticipates Edge LLMs running on devices within two to three years, further reducing costs <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

Superhuman charges $30/month, allowing them to fund these AI features <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>. The budget previously allocated to concierge onboarding has been redirected to AI development, aligning with their mission to provide the fastest, most powerful AI email experience <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

## Taking on Incumbents

While incumbents (like Outlook and Gmail) have advantages in AI due to existing data and user bases, they are also "encumbered" <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. Rahul Vohra advises new companies to target specific underserved yet economically powerful segments of the market <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.

Incumbents struggle with:
*   **One-size-fits-all solutions**: Products like Microsoft 365 and Gmail cater to billions of users, necessitating a broad approach that leaves niche segments underserved <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.
*   **Product Speed**: Superhuman's foundational advantage was its "lightning fast" speed, including instantaneous responses and sub-100-millisecond user interactions <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>. This is hard for older, client-server applications to replicate <a class="yt-timestamp" data-t="00:49:56">[00:49:56]</a>.
*   **Organizational Design (Conway's Law)**: Large companies often organize product features based on internal team structures rather than optimal user experience. This leads to disjointed interfaces (e.g., calendar being separate from mail and chat in Google Workspace) <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.

## The [[the_role_of_ai_agents_in_email_management|Agentic AI Future]]

The future envisions users having multiple AI agents, with an email agent serving as a primary interface <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. These agents will be mostly autonomous, able to interact with other systems (like CRM or internal APIs) and even other agents via cryptographic handshakes <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. For example, an executive AI agent could query an HR agent about open enrollment details and health insurance plans for family planning, providing an instantaneous, comprehensive recommendation <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.

Superhuman aims to be the "pane of glass" through which users interact with this ecosystem of agents <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>. As a "three-hour a day product" (where users spend 3+ hours daily), email applications like Superhuman are uniquely positioned to orchestrate these interactions <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. The strategy is for each company to build an agent relevant to its domain (e.g., an email agent for triage, drafting, scheduling, and sending emails) <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>. These interactions might even transition to [[the_future_of_voice_interfaces_in_ai|voice interfaces]] in the future <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>.

## Overhyped vs. Underhyped in AI

Rahul Vohra believes the idea of "AI coming for our jobs" is both overhyped and underhyped <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a>.
*   **Underhyped**: The speed at which AI will impact specific entry-level roles (e.g., customer support, sales) is not widely understood by the general public <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>. AI doesn't need to be perfect, only 80% as good at 10% of the cost to be widely adopted <a class="yt-timestamp" data-t="00:56:10">[00:56:10]</a>.
*   **Overhyped**: The impact extends beyond these specific roles; AI will eventually affect most jobs, including highly skilled ones like CEO <a class="yt-timestamp" data-t="00:56:43">[00:56:43]</a>. This shift will likely lead to a future where "work" resembles "leisure" by current standards, similar to how modern jobs would appear to a hunter-gatherer from 1,500 years ago <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>. Humans are hardwired to work and engage in status games, so they will find new ways to be productive and stressed <a class="yt-timestamp" data-t="00:58:01">[00:58:01]</a>.

## Improving Chat/Messaging Platforms

Vohra suggests that applications like Slack and Microsoft Teams could be significantly improved by adopting successful elements of email:
*   **Conversation Ordering**: Email conversations are ordered by the last reply, making it easier to see active discussions, unlike chat platforms where new messages push older ones down <a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>.
*   **Subject Lines**: Email provides clear subject lines for an "at-a-glance" view of a conversation's topic, which is often missing or manual in chat <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.
*   **Task Management**: Email allows users to mark things as "done," snooze, or assign threads <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>.
*   **Inbox Zero**: The ability to achieve inbox zero in email helps manage overwhelming information, a capability often lacking in chat platforms that accumulate unread channels <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>.

The vision is to combine the best of both worlds: a future workplace experience designed for thoughtful asynchronous discussion, with clear subject lines, archiving, snoozing, assigning, and the option of real-time chat, allowing users to choose their modality and maintain control <a class="yt-timestamp" data-t="01:01:18">[01:01:18]</a>. This would allow companies to be legitimately run, leveraging email's strengths that chat platforms have yet to capture <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>.

## Investment Insights

Rahul Vohra, also an active investor, is generally bearish on most de novo AI companies that simply add AI to existing app concepts, as this essentially requires building two companies at once <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>. He is bullish on companies with a clear distribution advantage (e.g., contacts, viral loops, track record) <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>. AI in such cases is often "incidental" to the core ability of the founder to create distribution and retain users <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a>.

When considering market size, Vohra points to the vast number of professionals (1 billion) who spend significant time (3+ hours daily) on email, representing trillions of hours annually <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. Achieving 300,000 subscribers at $30/month translates to a $100 million annual run rate, which is a small fraction of the total addressable market <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>. He also notes the rise of [[the_future_of_ai_in_robotics_and_its_impact|new robotics companies]] and applications of foundation models in fields like biology, where creating large, novel datasets is a significant challenge <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>.

Ultimately, Superhuman's mission transcends email, aiming to help professionals feel happier, more productive, and closer to achieving their potential <a class="yt-timestamp" data-t="01:03:43">[01:03:43]</a>.