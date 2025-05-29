---
title: Building a SaaS app using Replit
videoId: vGSYuwNcdcc
---

From: [[gregisenberg]] <br/> 

An idea for an app capable of generating $2,000 to $3,000 a day, called Invoice Nudger, was brought to life using [[Replit as a tool for entrepreneurs and creatives | Replit AI agent]] and [[Introduction to Replit and Resendcom | Resend.com]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This project aimed to create a live coding tutorial on [[Using AI to build a SaaS startup | building a SaaS startup]] while also incorporating strategies for growth <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Team: "Vibe Coders Next Door"

The app was developed by Billy Howell and Nicholas Conley, described as "vibe coders next door" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Nicholas Conley, a sales professional, was learning to code on the side, while Billy Howell was noted for becoming "famous as a vibe coder" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Billy has a history of building numerous apps <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> and has seen success stories of non-engineers using [[Replit as a tool for entrepreneurs and creatives | Replit]] to sell apps, including one closing a $30,000 deal <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## The Problem: Unpaid Invoices

The inspiration for Invoice Nudger came from the common pain point of freelancers and agencies struggling to get paid for invoices, often due to clients forgetting <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Existing solutions like Stripe or QuickBooks often rely on automated, impersonal follow-ups that are less effective than a personal note <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The key differentiator for Invoice Nudger is its ability to send increasingly assertive, but professional, messages that appear to come from a personal source (e.g., "Susan in finance" or the CEO) <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This personal touch is expected to convert unpaid invoices into paid ones much quicker <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Designing the Solution: Invoice Nudger Features

The goal was to create a single-feature app that could be brought to life using AI coding principles <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### V1 (Minimum Viable Product)
The initial version aimed to:
*   Set up a custom email address <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   Use AI to write emails or make templates <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   Connect to billing platforms like Stripe or PayPal, though the immediate focus for V1 was on email sending without direct billing integration to simplify the demo <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Users could manually paste in their invoice links <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   Integrate an API from OpenAI or Claude to generate human-like emails <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   A suggested feature for V1 was a BCC email that auto-logs invoices into the system when sent, streamlining the process for users <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Future Ideas (V2)
*   **Lawyer's Letter Feature:** For an extra fee, the app could send a reminder email from a lawyer, leveraging the psychological impact of legal counsel <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>. This represents an upsell opportunity <a class="yt-timestamp" data-t="00:48:35">[00:48:35]</a>.

## Choosing the Right Tools

### [[Replit as a tool for entrepreneurs and creatives | Replit AI Agent]]
[[Replit as a tool for entrepreneurs and creatives | Replit]] was selected for its capability to rapidly build apps using AI <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. A new feature allows the agent to take screenshots or pull text context from pasted links, storing it in a context folder <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### [[Introduction to Replit and Resendcom | Resend.com]]
For email sending, [[Introduction to Replit and Resendcom | Resend.com]] was chosen over traditional options like Mailgun or SendGrid due to its ease of use, beautiful interface, and specific design for React and Node.js projects, making it ideal for [[Replit as a tool for entrepreneurs and creatives | Replit]]-based development <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. It simplifies transactional email setup, which is often a pain point for [[Building a vertical SaaS business | SaaS]] apps <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

### Other Tools
*   **ChatGPT/Claude:** Used to refine ideas, generate product requirements documents (PRDs), and even create marketing video scripts <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. It helps structure prompts for AI coding agents <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Porkbun:** Recommended for purchasing domain names due to its no-frills approach and pre-configured DNS settings for various platforms like Shopify <a class="yt-timestamp" data-t="00:53:17">[00:53:17]</a>.
*   **JotForm, Card, Tally.so, Typeform:** Suggested tools for collecting emails for a waitlist when launching an app <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>.

## The Development Process

### Initial Prompting
The process began by asking [[Replit as a tool for entrepreneurs and creatives | Replit AI agent]] to create a web app for drafting and setting automated invoice follow-up sequences using the Resend library, with styling from shadcn <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

### Using AI for PRD Generation
A more robust approach involved using ChatGPT to generate a detailed Product Requirements Document (PRD) based on a simple tweet about Invoice Nudger <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. The PRD included:
*   Core features (Invoice upload/creation, automated nudging, nudge history) <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   User roles and access control <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   Expected screens (dashboard, auth screens) <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

Crucially, it was advised to remove complex features like authentication and payment platform integrations from the initial prompt to avoid overwhelming the AI agent <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

### Building with [[Replit as a tool for entrepreneurs and creatives | Replit]]
With the refined PRD, the prompt "Build this web app based on the PRD I gave you" was fed to [[Replit as a tool for entrepreneurs and creatives | Replit AI agent]] <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. The agent then proposed a plan:
*   Use basic username/password authentication <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
*   Utilize a PostgreSQL database <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   Use shadcn for UI <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

The agent quickly scaffolded a visual preview of the app, demonstrating the idea in minutes <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. A manual database creation was recommended as a good practice to ensure the agent doesn't forget this step <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

The final app prototype allowed users to create invoices, enable automatic nudging, and manually send reminders <a class="yt-timestamp" data-t="00:47:16">[00:47:16]</a>. It also included a tab for email templates (first, second, third reminders) <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. Within an hour, a functioning app was built, highlighting the power of [[Replit as a tool for entrepreneurs and creatives | Replit]] and [[Introduction to Replit and Resendcom | Resend.com]] <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.

### Setting Up [[Introduction to Replit and Resendcom | Resend.com]] and Domain
To send emails, a domain name like "tonysopranoinvoices.com" was purchased <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>. Mail records (e.g., MX, CNAME, TXT) were set up in the DNS host (Porkbun) to verify ownership and allow sending from the custom domain through [[Introduction to Replit and Resendcom | Resend.com]] <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>. The AI agent was prompted to configure the app to send emails from "enforcer@tonysopranoinvoices.com" <a class="yt-timestamp" data-t="00:56:22">[00:56:22]</a>.

## Marketing Strategies for [[starting_a_saas_business_using_ai_tools | SaaS Apps]]

Effective marketing is crucial for growing a [[Starting a SaaS business using AI tools | SaaS startup]].

### 1. Video Marketing & Storytelling
*   Inspired by Farza TV's viral video for "Freewrite" (a Mac app), creating a beautifully done video can generate millions of views and downloads <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>.
*   The video should tell a story, perhaps "behind the scenes" of how Invoice Nudger saved a business, using a compelling brand identity (e.g., "sending the mob after people" for humor) <a class="yt-timestamp" data-t="00:28:31">[00:28:31]</a>.
*   AI tools like ChatGPT can be used to generate video scripts based on examples <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

### 2. Cold Email Campaigns
*   **Lead Generation:** Scrape emails of target audiences (e.g., agency owners) using tools like Apollo or Outscraper, or purchase lists from platforms like Upwork or Fiverr <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>. Find email and Instantly/Smart Leads can also be used <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
*   **Email Warming:** Crucial step where new email addresses send and receive emails from a "warming pool" to appear as real human interaction and avoid being flagged as spam <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>.
*   **Copywriting:** Craft killer copy with catchy subject lines (e.g., "Invoice Paid") <a class="yt-timestamp" data-t="00:33:56">[00:33:56]</a>.
*   **Call to Action (CTA):** Offer immediate value like "Go try it out. Get your first two invoices done for free," rather than asking for a meeting or video watch <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.
*   **A/B Testing:** Test different subject lines and CTAs to optimize conversion <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
*   Cold email can be layered on top of other strategies as a passive, background effort <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>.

### 3. Instagram and TikTok Playbook
*   Applicable to B2B despite being primarily B2C <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>.
*   Create multiple accounts and warm them up by engaging like real humans (following, bookmarking, liking) for 3-4 days <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.
*   Identify popular formats and hooks within the target niche (e.g., freelancer niche). Slideshows are currently effective <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.
*   Example content: "Here's the top five tools that saved my agency" including Invoice Nudger <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.

### 4. LinkedIn Short-Form Video
*   LinkedIn strongly prioritizes video content, making it a powerful channel <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.
*   Post short-form videos daily or every two days for consistent impressions (e.g., 2 million impressions in 14 days) <a class="yt-timestamp" data-t="00:40:16">[00:40:16]</a>.
*   Videos should tell stories of how Invoice Nudger helps clients, using engaging hooks like "This AI agent is the employee I always wanted" <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>.
*   Unlike X (formerly Twitter), LinkedIn allows direct links in posts to drive sign-ups <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. A tactic is to post content, wait for engagement, then edit the post to add the link at the bottom <a class="yt-timestamp" data-t="00:42:35">[00:42:35]</a>.
*   Despite some perceiving LinkedIn as "cringe," its large user base (hundreds of millions of active users) makes it a valuable tool for gaining attention and building trust <a class="yt-timestamp" data-t="00:46:15">[00:46:15]</a>.

### 5. Hand-to-Hand Combat (Direct Outreach)
*   Create a list of 50-100 target individuals <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>.
*   Engage with them on platforms like X by commenting on their posts to enter their "orbit" <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.
*   This is a longer-term strategy (e.g., a month-long play) <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>.
*   Avoid immediate pitching; instead, build rapport and subtly introduce the tool, offering it for testing <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

## Conclusion and Advice

The ability to quickly spin up an MVP app in an hour and then leverage free marketing channels is a significant advantage in the current landscape <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>. Key advice for aspiring builders:
*   **Iterate Constantly:** Build many apps (e.g., 50 apps) and try different approaches for the same idea to become proficient with various tools <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.
*   **Focus on Value:** Build what's most important to the user and clearly demonstrate how the app helps them make progress on that key performance indicator (KPI), making it shareable for marketing <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>.
*   **Don't Get Stuck:** Avoid getting overly attached to a single idea <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.
*   **Embrace Tools:** Utilize all available tools to increase the probability of success in the challenging startup environment <a class="yt-timestamp" data-t="00:45:49">[00:45:49]</a>.