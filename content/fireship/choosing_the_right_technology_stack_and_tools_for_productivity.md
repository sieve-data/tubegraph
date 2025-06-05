---
title: Choosing the right technology stack and tools for productivity
videoId: A4_TFHzqAAg
---

From: [[fireship]] <br/> 

When building a side hustle or software application, selecting the appropriate technology stack and tools is crucial for [[developer_productivity_tools | productivity]] and success. The ultimate goal is to create a "money printing machine" that can operate on autopilot, offering freedom without constant deadlines or bosses <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Mindset of a Solopreneur

Building a successful business requires hard work and some luck <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Success often comes from developing skills, identifying problems, and seizing opportune moments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For instance, Danny Postma's HeadshotPro succeeded by combining development skills with the emerging [[impact_of_ai_tools_on_coding_and_developers | AI hype train]] to solve the problem of expensive corporate photos <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

> [!TIP] Fail Early, Fail Often, Fail Forward
The only true validator of your project is the customer <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. It's essential to get real users providing feedback as soon as possible, rather than spending years building something nobody wants <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Before dedicating significant time to an idea, it's wise to validate it <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Ideas are Cheap, Execution is Everything

The technology itself is secondary to the business model and marketing plan <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. An excellent application won't succeed without a solid marketing strategy to reach users <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For those without large budgets, organic marketing through social media platforms like Twitter, YouTube, or TikTok is often necessary <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The principle is to first locate potential users, then offer an appealing service that they will be willing to pay for <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

> [!CAUTION] Don't write any code until you have a marketing plan <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Choosing the Optimal Tech Stack

When it comes to [[understanding_and_choosing_a_tech_stack | choosing a tech stack]], the primary concern is that it works <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Trends or specific frameworks like WordPress, React, or Angular are less important than the ability to deliver a functional product <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Indie makers like Peter Levels, who earns millions annually from side hustles, often stick to "boring old PHP" and avoid trendy [[software_engineering_and_development_tools | developer products]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

> [!IMPORTANT] Optimize for Productivity
It is critical to find technologies that optimize your [[developer_productivity_tools | productivity]] and stick to them unless there's a compelling reason to change <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Recommended Stack and Tools

For personal projects, the following stack is often used:
*   **Frontend Framework:** [[choosing_the_right_javascript_framework_for_your_project | SvelteKit]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
*   **Backend/Database:** Firebase <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
*   **UI Library/Framework:** Carbon Design System (IBM) or Tailwind CSS <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>

The "it stack" refers to SvelteKit and Firebase <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

#### Frontend: Svelte vs. React

While many developers opt for React, Svelte is preferred due to personal enjoyment in writing its code <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Working with tools you dislike can be demoralizing, making personal preference an important factor in [[programming_tools_and_software_preferences | programming tools and software preferences]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A custom library, `sveltefire`, integrates Svelte stores with Firebase data, simplifying backend data reading by using a dollar sign prefix <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

#### Backend and Database: Firebase

Firebase, despite potential negative trade-offs like vendor lock-in with Google Cloud and costs in specific situations, significantly simplifies development <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Key benefits of Firebase for [[simplifying_and_optimizing_your_tech_stack | simplifying and optimizing your tech stack]]:
*   **Automated Backend Processes:** Saving a document in Firestore can trigger a background function that securely handles tasks like calling external APIs (e.g., Eleven Labs for voice cloning), storing files in cloud storage, and generating secure download URLs <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This avoids exposing HTTP endpoints to the frontend <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Real-time Synchronization:** The Firebase SDK keeps the frontend database in sync in real-time. This allows for simple UI updates based on data status changes (e.g., "processing" to "complete") directly in the Svelte code <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Security Rules:** A single line of code in Firebase security rules can ensure authenticated users only access their own data <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

#### Database Choice: Firestore vs. Relational

Firestore is a fast and user-friendly document database <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, well-suited for simple data relationships, such as users generating many audio clips <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. For highly complex data relationships, it may not be suitable <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Relational databases like MySQL and PostgreSQL are generally the safest choice for most applications, though they also have their own limitations <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Thorough research is crucial when [[understanding_and_choosing_a_tech_stack | choosing a database]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Monetization Tools

*   **Payments API:** Stripe is a common choice for handling payments, though many other providers exist <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   **Free Trials:** Offering a free trial (e.g., 100 free tokens for a voice cloning service) allows users to experience the app before committing to a purchase <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   **Checkout Flow:** An authenticated Firebase Cloud function can generate a Stripe checkout session, redirecting users to a hosted checkout page, eliminating the need to manually code the UI <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Webhooks for Payment Confirmation:** Stripe sends a webhook to a server (another Firebase Cloud function) upon payment. This webhook contains payment data, allowing the application to update user information (e.g., adding purchased tokens to Firestore) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Email Service:** SendGrid can be integrated into the payment webhook function to send transactional emails, such as order confirmations, to customers <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

Pricing strategy can leverage techniques like the "Vercel strategy," which involves marking up the cost of third-party services (e.g., charging 69 cents per 1,000 characters when the underlying service costs 18 cents) to generate profit <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.