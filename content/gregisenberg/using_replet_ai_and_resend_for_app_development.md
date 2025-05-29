---
title: Using Replet AI and Resend for app development
videoId: vGSYuwNcdcc
---

From: [[gregisenberg]] <br/> 

This article explores how a team used [[replit_as_a_tool_for_coding_and_app_development | Replit AI Agent]] and Resend.com to build a functioning application, Invoice Nudger, from an idea to a working prototype capable of generating significant revenue [00:00:03]. The process covered not only development but also strategies for growing the app through marketing [00:00:26].

## The Idea: Invoice Nudger
Invoice Nudger is a product designed for freelancers to automatically follow up on unpaid invoices with increasingly assertive, yet professional, messages until payment is received, aiming to eliminate awkwardness and ensure freelancers get paid [00:01:57]. The idea stems from the common pain point of agencies and freelancers struggling to get paid, not due to malice, but forgetfulness on the client's part [00:02:20].

### Differentiation from Existing Solutions
Unlike automated reminders from platforms like Stripe or QuickBooks, Invoice Nudger aims to send personalized notes that appear to come from a real person, such as "Susan in finance" or even the CEO, potentially with the sales rep or account manager CC'd [00:02:59]. This personal touch is expected to convert outstanding invoices into payments much quicker than generic automated messages [00:02:47]. The app can also include a custom domain to send emails from the user's site domain, making messages more impactful [00:03:22].

### Potential and Branding
The app has the potential to generate $2,000 to $3,000 per day [00:00:06]. It is envisioned as a revenue generator rather than just another tool [00:03:14]. Marketing could involve campaigns suggesting it "sends the mob after people" with an "aggression meter" for messages, ranging from "Conor McGregor" to a "nice Post Malone-esque figure" [00:04:02]. Future upsells could include sending legal reminders or lawyer's letters for an extra fee [00:08:02, 00:48:09].

## Tools and Technologies for Development
The core of the development relied on [[replit_as_a_tool_for_coding_and_app_development | Replit AI agent]] and Resend.com [00:00:11, 00:00:15].

### Core Development Tools
*   **[[replit_as_a_tool_for_coding_and_app_development | Replit AI agent]]**: Used as the primary AI coding tool to build the web application [00:00:11, 00:59:59].
*   **Resend.com**: Selected for email sending due to its ease of use, React-based design, and simple setup for transactional emails [00:10:07, 00:12:02, 00:13:36]. It's described as a "godsend" for quickly building MVPs that send emails [00:13:38].
*   **Shad CN**: A component library chosen for UI styling because of its appearance and familiarity [00:14:21].
*   **Postgres**: The chosen database for the application [00:21:39].

### Other Tools Mentioned
*   **Lindy or Gum Loop**: Suggested for building a V1 prototype to test the market without fully developing the Replit app [00:07:52].
*   **OpenAI or Claude**: Recommended for integrating AI to write more human-like email templates [00:08:21].
*   **Domain Registrars**: Pork Bun and Namecheap were mentioned for purchasing and managing domain names, with Pork Bun noted for its ease of use and preconfigured DNS settings [00:53:17, 00:53:20, 00:53:25].

## Development Process with Replit AI
The development process began by defining features and considering a Minimum Viable Product (MVP) [00:07:32, 00:07:45].

### Prompting Strategy
An effective strategy involved first explaining the app idea to a large language model like ChatGPT or Claude [00:15:30]. This allowed the AI to act as an "engineer," outlining a Product Requirements Document (PRD) with core features, user roles, screen layouts, and a database schema, catching potential omissions [00:15:39, 00:18:23]. The PRD was then given to [[replit_as_a_tool_for_coding_and_app_development | Replit AI]] [00:20:50].

### Replit AI Capabilities
[[replit_as_a_tool_for_coding_and_app_development | Replit AI]] can:
*   **Ingest Context**: When pasting a link, it offers to take a screenshot or extract text context, storing it in a context folder for the agent to reference [00:14:37].
*   **Scaffold UI**: It quickly visualizes ideas by scaffolding the application's UI, including dashboards and modules, often within minutes [00:22:21, 00:23:31].
*   **Build Plumbing**: In the background, it sets up routes and the underlying structure of the app [00:24:23].
*   **Implement Features**: It can implement features like sending reminders and setting up cron jobs for automated nudging [00:48:46, 00:49:53].
*   **Manage Secrets**: API keys can be securely added to Replit's secrets tool [00:49:43].

### Development Challenges and Solutions
*   **Database Creation**: Sometimes the AI agent might forget to create a database, so manually creating one in Replit's database tab is a good practice [00:24:38].
*   **Email Sending Domain**: To send emails via Resend, a custom domain needs to be verified within Resend's dashboard, requiring DNS record configuration [00:51:57, 00:54:51].
*   **AI Overload**: Providing too many features in the initial prompt can overload the AI agent, making it beneficial to prioritize a "killer feature" for the MVP [00:19:12, 00:19:55].

### Outcome
Within an hour, a functioning app with multiple pages was created, capable of sending email reminders [00:59:31, 00:59:40]. The ease of use of both [[replit_as_a_tool_for_coding_and_app_development | Replit AI]] and Resend.com was highlighted, even for someone new to Resend [01:00:06].

## Marketing and Growth Strategies
A significant portion of the discussion focused on how to market and grow the application, moving beyond just building it [00:00:29, 00:05:13, 00:52:57].

### General Approach
*   **Storytelling with Video**: The current community for launching software lives primarily on X (formerly Twitter) and prioritizes video content [00:29:33, 00:29:39]. Creating a beautifully done video that tells a story, like the "Freewrite" example by Farsza TV, can generate millions of views and downloads [00:28:17, 00:30:47].
*   **Dashboards as Marketing Tools**: A visually appealing dashboard that highlights key performance indicators (KPIs) relevant to the user, like "cash collected this month," can serve as a marketing tool. If users can easily screenshot and share their success (e.g., "no kneecaps broken, all this money collected"), it acts as organic promotion [00:25:56, 00:26:30, 00:26:47].

### Specific Marketing Channels
1.  **Cold Email**:
    *   **Lead Generation**: Obtain lists of target audience (e.g., agency owners) from platforms like Apollo, or by hiring freelancers on Upwork/Fiverr who already have lists [00:35:06, 00:35:17]. Alternatively, use tools like Outscraper for local business leads or Find Email for LinkedIn leads [00:36:04, 00:37:01].
    *   **Campaign Setup**: Use tools like Instantly or Smart Leads to warm up email addresses (simulating human interaction to avoid spam filters) [00:37:13, 00:37:28].
    *   **Copywriting**: Craft killer copy with engaging subject lines (e.g., "invoice paid") and call to actions that offer immediate value (e.g., "try it out, get your first two invoices done for free") rather than asking for a meeting [00:33:56, 00:34:25].
    *   **A/B Testing**: Test different subject lines and call to actions across smaller lead buckets [00:38:01].
2.  **Instagram and TikTok Playbook**:
    *   **B2B Opportunity**: Despite being primarily B2C, there's a large untapped B2B opportunity [00:39:13, 00:39:55].
    *   **Account Warming**: Create multiple accounts and warm them up by acting like a real human (following, bookmarking, liking content) for 3-4 days to enter the target niche [00:39:20, 00:39:31].
    *   **Content**: Create content relevant to freelancers, such as slideshows (e.g., "top five tools that saved my agency") [00:39:43, 00:39:50].
3.  **LinkedIn Short Form Video**:
    *   **High Engagement**: LinkedIn prioritizes video content, making it highly effective for gaining impressions [00:42:07, 00:45:07]. Consistent posting (e.g., one video a day for 14 days) can lead to millions of impressions [00:40:17, 00:40:19].
    *   **Linking Strategy**: Unlike X, LinkedIn allows links within posts without suppression. A common tactic is to post content, let it gain traction, then edit the post to add a link at the bottom [00:42:24].
    *   **Content Hooks**: Use hooks like "check this tool out," "this AI agent is the employee I always wanted," or "this AI agent collects my money without breaking kneecaps" [00:40:37].
    *   **Utilizing AI**: AI like ChatGPT can help generate script ideas for marketing videos by analyzing successful examples [00:32:30].
4.  **Hand-to-Hand Combat**:
    *   **Direct Outreach**: Identify 50-100 target users and engage with them on platforms like X [00:40:56, 00:40:59].
    *   **Orbiting**: Comment on their posts and interact without immediately pitching the product. Build a relationship over a month before subtly introducing the tool [00:41:04, 00:41:15].
    *   **Personalized Approach**: When finally reaching out via DM, acknowledge their work before asking them to test the tool [00:41:31].

### Marketing Tools for AI Apps
*   **ChatGPT/Claude**: For generating Product Requirement Documents (PRDs) and marketing scripts [00:15:30, 00:32:30].
*   **Upwork/Fiverr**: For hiring freelancers to acquire lead lists [00:35:17].
*   **Apollo / Outscraper / Find Email**: For lead generation and email scraping [00:35:08, 00:36:04, 00:37:01].
*   **Instantly / Smart Leads**: For cold email campaigns and email warming [00:37:13].
*   **Jot Form / Card / Tally.so / Typeform / Framer**: For setting up landing pages and collecting emails for waitlists [01:02:22, 01:02:37].

## Advice for App Development and Startups
*   **Iterate Quickly**: Don't get stuck on one idea; try to build it in multiple ways and move on to the next, fostering skill development with various tools [01:03:03, 01:03:06, 01:03:11].
*   **Leverage Free Channels**: The current environment allows for spinning up an MVP quickly and testing marketing channels for free to build a waitlist even before significant development [01:03:24, 01:03:29].
*   **Embrace "Cringe"**: Don't let perceived social awkwardness stop you from using powerful platforms like LinkedIn for growth, as it offers a massive pool of potential users [00:45:27, 00:46:15].