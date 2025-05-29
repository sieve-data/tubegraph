---
title: Building MVPs with AI tools
videoId: vGSYuwNcdcc
---

From: [[gregisenberg]] <br/> 

This article details the process of [[using_ai_for_rapid_mvp_development | rapidly building a Minimum Viable Product (MVP)]], specifically an invoice follow-up application named "Invoice Nudger", using AI tools like Replet AI and Resend. The discussion covers the initial idea, the [[building_apps_using_ai_tools | AI-driven development process]], and [[product_management_with_ai_tools | strategies for growing the application]].

## The Invoice Nudger Concept

The core idea behind Invoice Nudger is to create a product for freelancers that automatically follows up on unpaid invoices with increasingly assertive, but professional, messages until payment is received, without awkwardness <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The concept emerged from the common issue agencies face in getting paid, often due to clients simply forgetting <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Differentiating from Existing Solutions
While platforms like Stripe and QuickBooks offer automated reminders, Invoice Nudger aims to differentiate itself by sending personalized notes, which are more effective in getting invoices paid quickly than generic automated follow-ups <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. These personalized emails could appear to come from individuals within the client's organization, such as "Susan in finance" or even the CEO, with relevant parties CC'd, making them more impactful and positioning the tool as a revenue generator rather than just another utility <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Key AI Tools for Development

The project primarily leveraged two AI tools:
*   **Replet AI Agent**: Used for the primary [[building_apps_using_ai_tools | application development]] and scaffolding the web app <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. A new feature allows the agent to take screenshots or get text context from pasted links, storing this information in a context folder for development <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Resend.com**: An email powerhouse used for sending automated emails <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It's noted for its ease of use, especially for those not super technical, being built for React and designed for simple integration with just a few lines of code <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. It simplifies the often arduous process of setting up transactional emails for SaaS applications <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

## MVP Development Process

The process involved several key steps, demonstrating [[combining_different_ai_tools_for_effective_development | how different AI tools can be combined]] for effective development.

### Defining Features for V1
Initially, V1 was considered to integrate with billing platforms like Stripe or PayPal and use AI (OpenAI or Claude API) to write human-like emails <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. However, for a true MVP, a simpler approach was chosen: focus solely on email sending without Stripe or billing integration to avoid setup complexities <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Users could manually paste their invoice link <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. A potential future feature discussed was a BCC email address for logging invoices directly into the system upon initial sending <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Prompt Engineering with ChatGPT
Before interacting with Replet, the developers used ChatGPT to create a Product Requirements Document (PRD) based on the initial idea <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. This involved:
1.  Explaining the app idea to ChatGPT.
2.  Asking it to define requirements, screens, and database schema.
3.  Instructing it to avoid being opinionated about the tech stack, as Replet is adept at choosing its own <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
4.  Editing the generated PRD to remove complex features like invoice upload/creation and full authentication for the initial MVP <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

This refined PRD was then fed to Replet AI Agent with the prompt: "Build this web app based on the PRD I gave you" <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

### Building the App with Replet AI
Replet immediately began scaffolding a UI using Shadcn for styling <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. It proposed using a Postgress database and basic username/password authentication, which was accepted <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
A good practice when [[building_apps_using_ai_tools | using AI coders]] like Replet is to manually create the database first, as the agent might sometimes forget <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. After scaffolding, Replet builds out routes and backend plumbing, including setting up database schemas and importing UI components <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.

### Setting up Email Sending with Resend
To enable email sending, a custom domain was required to verify ownership with Resend. In this case, "tonysopranoinvoices.com" was purchased <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>. DNS mail records (MX, TXT, CNAME) were configured via Porkbun, the domain registrar, to verify the domain with Resend <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>. API keys for Resend were added to Replet's secrets tool for security <a class="yt-timestamp" data-t="00:49:43">[00:49:43]</a>.

After implementation, the app was able to manually send reminders from the configured domain <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>. This rapid development from idea to a functioning MVP capable of sending emails within an hour highlighted the power of [[using_ai_for_rapid_mvp_development | AI for rapid MVP development]] <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.

## Marketing Strategies for Growing the App

Beyond building, a significant focus was placed on how to market and grow the app. This section offers various [[product_management_with_ai_tools | marketing strategies]] applicable to new products.

### 1. Video Content & Storytelling on X
*   **Leverage Viral Content**: Inspired by Farza TV's "Freewrite" launch video, which garnered 1.5 million views <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>. This demonstrated that even in saturated markets, a well-produced video on X (formerly Twitter) can lead to significant traction <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
*   **Create a Brand Narrative**: For Invoice Nudger, a playful "mob" or "goons" theme was suggested, creating videos or content around "sending the mob after people" to collect invoices <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
*   **AI-Generated Videos**: Utilize AI to create short, engaging videos, possibly featuring AI-generated characters like "Conor McGregor with a bat" or the "mob showing up at businesses" to collect payments <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.
*   **Prompt AI for Scripts**: ChatGPT can be prompted with examples (like Farza's video stills) to write marketing video scripts, even imagining a CMO like Farza for the product <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.
*   **Sharable Dashboards**: Design the app's dashboard with visually appealing charts (e.g., "cash collected this month") that users would be incentivized to screenshot and share, acting as organic marketing tools <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.

### 2. Cold Email Campaigns
*   **Strategy**: Target agencies and freelancers. Acquire lead lists (e.g., from Apollo, Outscraper, or directly from freelancers on Upwork/Fiverr) <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.
*   **Tools**: Use platforms like Instantly or Smart Leads for warming up email addresses and sending campaigns <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.
*   **Copy**: Focus on a call to action that offers immediate value without requiring a meeting, such as "Go try it out. You get your first two invoices done for free" <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>. A/B test subject lines and calls to action <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a>.

### 3. Instagram and TikTok Playbook (B2B Niche)
*   **Strategy**: Adapt B2C strategies for B2B. Create multiple accounts on each platform and warm them up by engaging authentically with content in the target niche (e.g., freelancer community) <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.
*   **Content**: Focus on formats that work, such as slideshows (e.g., "Here's the top five tools that saved my agency") <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>.

### 4. LinkedIn Short-Form Video
*   **Effectiveness**: LinkedIn heavily prioritizes video content, making it a "fishing with dynamite" opportunity <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>. Consistent posting can lead to viral content <a class="yt-timestamp" data-t="00:45:14">[00:45:14]</a>.
*   **Content**: Post daily short-form videos sharing stories of how Invoice Nudger helps clients, using engaging hooks like "This AI agent is like the employee I always wanted" or "This AI agent collects my money without breaking kneecaps" <a class="yt-timestamp" data-t="00:40:37">[00:40:37]</a>.
*   **Links**: While X suppresses links, LinkedIn allows links within posts, but it's often more effective to post content, let it gain traction, then edit the post to add a link at the bottom <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.
*   **Overcoming "Cringe"**: For those who find LinkedIn "cringe," the advice is to prioritize success over perception, as LinkedIn offers a massive active user base for potential engagement <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>.

### 5. Hand-to-Hand Combat (Direct Outreach)
*   **Strategy**: Identify 50-100 target users, engage with their content on platforms like X, and enter their "orbit" <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>.
*   **Approach**: Avoid immediate pitch-slapping. Build rapport over a month before subtly introducing the tool and asking if they'd be willing to test it <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>.

## Conclusion and Advice for Builders

The demonstration highlighted the incredible speed and ease of [[building_a_5_million_startup_using_ai_tools | building a functional MVP]] in about an hour using Replet and Resend <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.

> "The fact that not only can you spin up an app like we just did in an hour or at least an MVP, but you can also then go out to all these marketing channels that are completely free and you could test all of these marketing channels and get a weight list before you even touched Replet." <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>

Key advice for aspiring builders:
*   **Iterate Rapidly**: Don't get stuck on one idea; try to make 50 apps, iterating and building the same idea in three different ways to become proficient with the tools <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.
*   **Leverage Free Channels**: Utilize readily available and free marketing channels to test ideas and build interest (e.g., a waitlist) even before extensive development <a class="yt-timestamp" data-t="01:03:27">[01:03:27]</a>.

For collecting emails for a waitlist or early interest, tools like Jot Form, Card, Framer, Tally.so, or Typeform were suggested <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>.