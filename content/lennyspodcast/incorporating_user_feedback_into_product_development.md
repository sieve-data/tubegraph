---
title: Incorporating user feedback into product development
videoId: F0_IKKY3HCk
---

From: [[lennyspodcast]] <br/> 

Stripe's approach to [[integrating_customer_feedback_loops_in_product_development | product development]] is fundamentally centered around its users. The company emphasizes deeply understanding user needs and [[customer_engagement_and_product_development | co-creating]] solutions with them to ensure that products are not only effective but also meticulously crafted <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Co-creation with Early Users

Stripe's core philosophy involves finding the correct set of early users to [[customer_engagement_and_product_development | co-create]] the product alongside them <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

> [!example] Stripe Billing
> The Stripe Billing product development began by identifying existing users, such as Figma and Slack, who already utilized Stripe for payments and operated subscription business models <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Recognizing these companies were pushing the boundaries of what was possible, Stripe decided to [[customer_engagement_and_product_development | co-create]] the billing product with them <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
>
> This process involved:
> *   Forming shared Slack channels <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
> *   Regularly demonstrating the product to users <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
> *   Actively gathering [[effective_customer_interaction_and_feedback_gathering | feedback]] <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
>
> The product was only considered ready for a broader audience once this initial "alpha group" was extremely satisfied <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. This approach ensures that every engineer at Stripe possesses and exercises attributes typically found in product managers in other companies <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

## Operating Principles Driven by Users

Stripe's [[methods_for_stakeholder_engagement_in_product_planning | operating principles]] serve as behavioral guidelines distilled from the most effective "Stripes" (employees) <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

> [!quote] "Users First"
> The very first operating principle is "users first," meaning users are at the core of determining what the company should be building <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>. This principle guides the formation of deep personal relationships with users to inform every decision <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. This mindset attracts individuals who desire agency, deep understanding of problems, and the ability to generate their own solutions <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

## Systematic Methods for [[improving_user_experience_through_customer_feedback | Improving User Experience]]

### Friction Logging
Stripe employs a widely used process called "friction logging" across its product teams, and even internally for tools used by employees <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>. This method involves:
1.  **Modeling a specific user**: Clearly defining whose shoes the team member is stepping into (e.g., an engineer integrating the Stripe Billing API at a large SaaS platform like Atlassian) <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.
2.  **Using the product**: Going through the entire user flow, from the dashboard to writing code, as that specific user <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
3.  **Meticulous note-taking**: Documenting a stream of consciousness, with particular attention to points of friction the modeled user would encounter <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>. Positive aspects of the experience are also noted <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.
4.  **Investing in solutions**: These identified friction points become areas for significant investment to make the experience seamless <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

> [!example] Error Messages in API
> An early example of this meticulousness is how Stripe designed its API error messages to link directly to the relevant documentation sections for solving the problem <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. This detail, though uncommon, is highly valued by developers during critical problem-solving moments <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. In fact, there's more code in the Stripe API to handle these error edge cases than in the main flow <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. This attention to detail has significantly improved user adoption and continued use of Stripe products <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.

Friction logging is a regular, repeating activity, often undertaken by product managers or engineering managers, and senior leaders also engage in it to ensure cohesion across parallel work streams <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

### UX Reviews
Stripe conducts UX reviews, often asynchronously, where individuals dedicate time to thoroughly go through the product and make detailed notes <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. These reviews are also conducted collaboratively, bringing together the product team, cross-functional partners (like support groups), and executives <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.

The process for a collaborative UX review includes:
1.  **Adopting a user persona**: Imagining being a specific user and experiencing the product from their perspective <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>.
2.  **Live issue logging**: Using a shared log where anyone can type in issues as the product manager walks through the flow <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.
3.  **Discussion and prioritization**: Discussing each issue at the end to determine its importance and need for address <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

> [!quote] "Walk the Store"
> Occasionally, Stripe conducts "walk the store" sessions, where the entire company reviews critical product flows together during a weekly meeting <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>. This practice helps to build a shared language and common understanding of the product experience and its connection to the company's priorities <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>.

### Engineer Occasions
A unique practice called "engineer occasions" involves engineers, including the CTO, clearing their schedules for several days to join a team and pick up a small feature or task <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>. This allows them to experience the team's development process firsthand, from using developer tools to understanding the build infrastructure and documentation, and ultimately seeing their work live in production to initiate the [[integrating_customer_feedback_loops_in_product_development | feedback loop]] <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>. A friction log is maintained during this process, and a report is written and shared to provide context for future prioritization decisions <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.

## Prioritizing User-Identified Issues

Stripe's planning processes are structured to reserve time for making the user experience exceptional <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>. This includes addressing "instant remediations" – issues identified through friction logs or incidents – which are often prioritized ahead of other roadmap work <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>. Teams are encouraged to allocate appropriate bandwidth for polishing and operational tasks <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

## Cultivating a Continuous [[integrating_customer_feedback_loops_in_product_development | Feedback Loop]]

The most impactful advice for [[building_customercentric_products_through_design | building better products]] is to establish and accelerate a [[integrating_customer_feedback_loops_in_product_development | feedback mechanism]] with users <a class="yt-timestamp" data-t="00:43:09">[00:43:09]</a>. This means:
*   **Listening to users**: Continuously engaging with user feedback.
*   **Rapid iteration**: Getting a product or feature into users' hands quickly.
*   **Collecting feedback**: Actively soliciting their thoughts and observations.
*   **Closing the loop**: Feeding that feedback back into the development process <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.

Stripe's developer tooling and infrastructure are designed to enable continuous delivery of changes to production, allowing for rapid deployment and quick [[leveraging_user_insights_for_product_development | user feedback]] acquisition <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>. This fast iteration allows feedback received in the morning to potentially result in a change back in users' hands by the end of the day <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.

> [!tip] Crying Octopus Button
> In a relatively minor but impactful change, Stripe added a "crying octopus" emoji button to every developer tool <a class="yt-timestamp" data-t="01:27:32">[01:27:32]</a>. Clicking it allows engineers to quickly type in what went wrong ("paper cuts"), which the developer productivity team then uses to prioritize their roadmap <a class="yt-timestamp" data-t="01:27:40">[01:27:40]</a>. This "frictionless problem recording" has proven highly valuable <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>.

## Impact of a User-Centric and Meticulous Approach

Stripe's commitment to user-first principles and meticulousness results in significant business impact. For example, by continuously tuning checkout flows and obsessing over details like removing latency or clicks, Stripe measured that users migrating to their Payment Element or Stripe Checkout increased their average revenue by 10.5% <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>. This demonstrates how a series of small, compounding improvements, driven by user focus, can lead to dramatic results <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>.