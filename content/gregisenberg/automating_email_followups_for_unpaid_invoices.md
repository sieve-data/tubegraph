---
title: Automating email followups for unpaid invoices
videoId: vGSYuwNcdcc
---

From: [[gregisenberg]] <br/> 

## The Invoice Nudger Idea

The concept of "Invoice Nudger" emerged from the common challenge freelancers and agencies face in collecting payments for outstanding invoices <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. Even without malicious intent, clients often forget to pay, necessitating a tool to automate follow-ups <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. The goal was to create a product that automatically follows up on unpaid invoices with increasingly assertive, yet professional, messages until payment is received, removing awkwardness for the freelancer <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

## The Problem with Existing Solutions

Existing platforms like Stripe and QuickBooks offer automated follow-ups <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. However, a key differentiator for Invoice Nudger is its ability to send personalized notes that appear to come from a real person (e.g., "Susan in finance" or even the CEO), potentially copying the sales representative <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This personal touch is expected to convert and get invoices paid much quicker than generic automated messages <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Key Differentiators and Features

*   **Personalized Messaging:** The system aims to send emails that look human-written, avoiding the standard "invoice due" notification <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
*   **"Aggression Meter":** A potential future feature involves an adjustable "aggression meter" for follow-up messages, ranging from a "Post Malone-esque" nice tone to a "Conor McGregor" or "mob"-like assertiveness <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
*   **Custom Domain Sending:** The ability to send emails from a custom domain (e.g., from "accounting" or a specific person's name at the client's site domain) was identified as crucial for effectiveness <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
*   **BCC Integration (Future):** A proposed feature would allow users to BCC a specific Invoice Nudger email when sending an initial invoice, automatically logging it into the system for follow-up <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.
*   **Lawyer's Letter Upsell (Future):** For an extra fee, the service could offer to send a formal reminder letter from a lawyer <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.

## Building the Invoice Nudger with AI Tools

The project aimed to take a single-feature app idea and bring it to life <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

### Initial Concept & Versioning

For a Minimum Viable Product (MVP), the initial focus was solely on email sending, deliberately avoiding direct Stripe or billing platform integrations due to their complexity for a demo <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>. Users could manually paste their invoice links <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>. Future versions (V2) would explore connections to billing platforms like Stripe or PayPal <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

### Leveraging AI for Development: Replet & ChatGPT

*   **Replet AI Agent:** Replet AI agent was used as the primary coding tool <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. A key feature of Replet's agent is its ability to "get context" from linked documentation, allowing it to understand external libraries <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>.
*   **ChatGPT for Product Requirements Document (PRD):** Before coding, ChatGPT or Claude can be used to outline the idea, identify missing elements, and structure a detailed PRD with requirements, screens, and database schema <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a>. This PRD was then provided to the Replet AI agent <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>. The PRD included core features like invoice upload, automated nudging, nudge history, and user roles <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>. For a V1, features like authentication and invoice upload/creation were initially removed from the prompt to avoid overwhelming the AI agent <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>.
*   **Scaffolding and UI:** Replet can quickly scaffold a UI using libraries like ShadCN, providing a visual preview of the app <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>.

### Setting up Email Sending with Resend.com

*   **Resend.com:** This platform was chosen for email sending due to its ease of use, particularly for React-based projects like those built in Replet <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. It simplifies transactional email setup, which is often an "annoying step" with traditional services <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
*   **Domain Verification:** To send emails from a custom domain (e.g., `enforcer@tonysopranoinvoices.com`), the domain must be verified in Resend.com by setting up specific mail records (MX, TXT, CNAME) in the DNS host (like Porkbun) <a class="yt-timestamp" data-t="54:51:00">[54:51:00]</a>.
*   **Functionality:** Within an hour, a functioning app was created, capable of sending reminders, showcasing the power of [[utilizing_ai_agents_to_automate_business_tasks | AI agents]] and tools like Resend <a class="yt-timestamp" data-t="59:31:00">[59:31:00]</a>.

## Marketing Strategies for a New App

After building an app, the next crucial step is growth <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

### The Power of Video and Storytelling

*   **Video-First Launches:** Modern product launches increasingly rely on video, especially on platforms like X (formerly Twitter) which prioritize video content <a class="yt-timestamp" data-t="29:39:00">[29:39:00]</a>.
*   **Farsza TV's Freewrite Example:** The launch of "Freewrite," a Mac writing app, gained 1.5 million views and hundreds of downloads per hour through a beautifully made video <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>. This demonstrates that even in saturated markets, effective video storytelling can drive significant interest <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.
*   **Branding and Storytelling:** For Invoice Nudger, marketing could involve humorous "mob" or "goon" themes in videos, showing the app "chasing down" clients to get invoices paid <a class="yt-timestamp" data-t="28:40:00">[28:40:00]</a>.
*   **Sharable Metrics:** Displaying a clear Key Performance Indicator (KPI) on the app's dashboard (e.g., "money collected this month") that users can screenshot and share acts as a powerful marketing tool <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.

### Cold Email Campaigns

*   **Targeting:** Identify target audiences (e.g., agencies) and scrape their contact information using tools like Apollo, Outscraper, Scrapebox, or Find Email <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>. It's also possible to directly purchase email lists from freelancers on platforms like Upwork or Fiverr <a class="yt-timestamp" data-t="35:17:00">[35:17:00]</a>.
*   **Tools:** Use platforms like Instantly or Smart Leads for sending and warming up email addresses to avoid spam flags <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.
*   **Copy & Call to Action:** Craft compelling subject lines and calls to action. A strong approach is to offer immediate value without requiring a meeting, such as "try it out, get your first two invoices done for free" <a class="yt-timestamp" data-t="34:25:00">[34:25:00]</a>. This is a passive marketing approach that can run in the background <a class="yt-timestamp" data-t="43:46:00">[43:46:00]</a>, ideal for [[creating_effective_cold_emails_with_ai | creating effective cold emails with AI]].

### Social Media Playbooks (Instagram, TikTok, LinkedIn)

*   **B2B on Social Media:** The Instagram and TikTok playbook, commonly used for B2C, has potential for B2B applications <a class="yt-timestamp" data-t="38:48:00">[38:48:00]</a>. This involves creating multiple accounts, warming them up by acting like real humans, and engaging with the target niche (e.g., freelancers) <a class="yt-timestamp" data-t="39:20:00">[39:20:00]</a>.
*   **LinkedIn Short-Form Video:** Posting short-form videos daily on LinkedIn can generate massive impressions (e.g., 2 million in 14 days) <a class="yt-timestamp" data-t="40:07:00">[40:07:00]</a>. LinkedIn heavily prioritizes video content, acting as a "fishing with dynamite" opportunity <a class="yt-timestamp" data-t="42:04:00">[42:04:00]</a>. The platform also allows direct links for sign-ups <a class="yt-timestamp" data-t="42:24:00">[42:24:00]</a>. It's a valuable [[ai_workflow_automation | AI workflow automation]] for B2B.
*   **Addressing "Cringe" Factor:** While some find LinkedIn "cringe," ignoring its hundreds of millions of active users for potential engagement and leads is a "foolish" decision for anyone building a startup <a class="yt-timestamp" data-t="46:45:00">[46:45:00]</a>.

### Direct Outreach ("Hand-to-Hand Combat")

*   **Personalized DMing:** Identify 50-100 key individuals or businesses and engage with them on platforms like X. This is a longer-term strategy that involves commenting on their posts and entering their "orbit" before a direct pitch. The goal is to build rapport and offer the tool as a solution after establishing a connection <a class="yt-timestamp" data-t="40:52:00">[40:52:00]</a>.

## The Impact of AI on App Development and Entrepreneurship

The ability to rapidly develop a functional app like Invoice Nudger within an hour using [[utilizing_ai_agents_to_automate_business_tasks | AI agents]] and specialized tools (Replet, Resend) highlights the transformative impact of AI on entrepreneurship <a class="yt-timestamp" data-t="59:31:00">[59:31:00]</a>. Developers can quickly build MVPs without extensive traditional coding knowledge <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. There have been reported instances of individuals selling apps built with Replet for significant amounts, including a $30,000 app, by addressing specific "red-hot pain points" in various niches <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. This demonstrates the potential for [[automating_business_processes_with_ai | automating business processes with AI]] and [[automating_professional_services_with_ai | automating professional services with AI]].

## Conclusion: Iteration and Exploration

The advice for aspiring entrepreneurs and developers is to "make like 50 apps" and keep iterating <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. Don't get stuck on one idea; instead, try to build it in different ways and then move to the next <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>. This approach fosters proficiency with [[ai_tools_for_streamlining_ecommerce_newsletters | AI tools]] and rapid prototyping. The current landscape allows for not only quick app development but also the testing of various free marketing channels to build an audience or waitlist even before significant development <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>. This highlights [[the_importance_of_automations_and_lead_magnets_in_email_marketing | the importance of automations and lead magnets in email marketing]].