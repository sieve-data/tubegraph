---
title: Building a productoriented engineering culture
videoId: F0_IKKY3HCk
---

From: [[lennyspodcast]] <br/> 

Stripe's approach to product development is deeply rooted in [[philosophical_approach_to_product_development | a philosophical approach]] that emphasizes co-creation with early users and a highly product-minded engineering team <a class="yt-timestamp" data-t="00:00:00"></a>. This philosophy has enabled Stripe to grow its internet economy infrastructure by making it easier for businesses to get started and operate <a class="yt-timestamp" data-t="00:06:03"></a>.

## The Genesis of a Product-Minded Culture

Stripe's core thesis is that the internet economy will continue to expand significantly <a class="yt-timestamp" data-t="00:05:52"></a>. The company was founded out of a direct need: the co-founders, John and Patrick, experienced firsthand the extreme difficulty of accepting credit card payments online for a previous business, realizing it was harder than setting up hardware in a data center <a class="yt-timestamp" data-t="00:06:15"></a>. This profound problem for businesses becoming an "upstart" provided the initial inspiration for Stripe, which adopted a very developer-centric approach from the outset <a class="yt-timestamp" data-t="00:07:14"></a>.

## Engineers as Product Managers

In its early years, Stripe operated without dedicated product managers for an extended period, leading to the development of a unique [[building_a_successful_product_management_team | product-oriented engineering team]] <a class="yt-timestamp" data-t="00:17:19"></a>. The original team was primarily composed of engineers who were "extremely product minded" and essentially acted as Product Managers (PMs) <a class="yt-timestamp" data-t="00:17:22"></a>.

This was especially effective because their initial product was developer-focused, and the best PMs for such products are often technical, many being former or current engineers themselves <a class="yt-timestamp" data-t="00:17:50"></a>. Every early team member had to deeply understand users and integrate personal insights into the product development loop <a class="yt-timestamp" data-t="00:18:12"></a>.

## Co-creation with Users

A cornerstone of Stripe's product development is finding and co-creating with the right set of early users <a class="yt-timestamp" data-t="00:18:27"></a>.

### Example: Stripe Billing
When developing Stripe Billing, their solution for subscriptions and invoicing, Stripe identified existing users like Figma and Slack who had subscription business models and were pushing the boundaries of what was possible <a class="yt-timestamp" data-t="00:18:40"></a>. The Stripe team working on Billing got to know these companies and the individuals operating their systems personally, understanding their challenges, hopes, and dreams <a class="yt-timestamp" data-t="00:19:12"></a>.

This led to a shared product development loop:
*   Shared Slack channels for direct communication <a class="yt-timestamp" data-t="00:00:34"></a>.
*   Regular product demonstrations to gather feedback <a class="yt-timestamp" data-t="00:00:35"></a>.
*   The product was only considered ready for a broader audience once this "alpha group" was "super super happy" with it <a class="yt-timestamp" data-t="00:00:42"></a>.

This co-creation process means that every engineer building product at Stripe exercises many attributes typically found in PMs at other companies <a class="yt-timestamp" data-t="00:00:51"></a>.

## Operationalizing "Be Meticulous in Your Craft"

Stripe's operating principles, distilled from the behaviors of its most effective employees, heavily influence its product-oriented culture <a class="yt-timestamp" data-t="00:23:02"></a>. "Users first" is a primary principle, ensuring users are at the center of all decisions <a class="yt-timestamp" data-t="00:23:28"></a>. Another key principle is "be meticulous in your craft" <a class="yt-timestamp" data-t="00:24:13"></a>.

To [[understanding_company_cultures_impact_on_product_development | operationalize this principle]] while maintaining speed, Stripe employs several practices:

### Friction Logging
This widely used process involves meticulously documenting the user experience, paying particular attention to points of friction.
1.  **User Persona:** Put oneself in the shoes of a specific user (e.g., an engineer at Atlassian integrating the Stripe Billing API) <a class="yt-timestamp" data-t="00:26:01"></a>.
2.  **Walkthrough:** Go through the entire product flow (dashboard, docs, writing code) <a class="yt-timestamp" data-t="00:26:37"></a>.
3.  **Stream of Consciousness Notes:** Record the experience, highlighting friction points the modeled user would find difficult <a class="yt-timestamp" data-t="00:26:47"></a>.
4.  **Prioritization:** These friction points are then prioritized for investment <a class="yt-timestamp" data-t="00:27:04"></a>.

An example of meticulousness: Stripe's API error messages link directly to the relevant documentation, saving developers significant time <a class="yt-timestamp" data-t="00:25:04"></a>. More code exists for handling edge cases and error messages than for the main flow <a class="yt-timestamp" data-t="00:27:21"></a>.

Friction logging is a regular practice for almost every product team, often led by the PM or engineering manager <a class="yt-timestamp" data-t="00:33:10"></a>. Senior leaders and executives also engage in this to maintain a cohesive product experience across many parallel-operating teams <a class="yt-timestamp" data-t="00:33:55"></a>.

### UX Reviews and "Walk the Store"
UX reviews are often conducted asynchronously through friction logging, but also in group walkthroughs. Teams bring together cross-functional partners, including support groups and executives, to experience the product as a user, discussing issues openly <a class="yt-timestamp" data-t="00:37:41"></a>.

"Walk the Store" is an occasional practice where the entire company (or a majority of it) reviews critical product flows in a weekly meeting, helping to establish a shared language and consistent understanding of the user experience and product quality <a class="yt-timestamp" data-t="00:39:15"></a>.

### Engineer Occasion
David Singleton personally practices "Engineer Occasions," where he clears his calendar for three or four days to join an engineering team, pick up a small task or feature, and take it all the way to production <a class="yt-timestamp" data-t="00:46:39"></a>. This involves using the team's developer tools, understanding the build infrastructure, code review processes, and deployment times <a class="yt-timestamp" data-t="00:47:07"></a>. A friction log is kept during this period, which then informs future prioritization and trade-offs <a class="yt-timestamp" data-t="00:47:28"></a>. Engineers are encouraged to provide unvarnished feedback during this process <a class="yt-timestamp" data-t="00:50:04"></a>.

This practice helps managers gain deep context about their teams' experiences and challenges, especially in areas like automation <a class="yt-timestamp" data-t="00:48:40"></a>. Engineering managers are advised to do this within their first quarter to six months at Stripe <a class="yt-timestamp" data-t="00:48:33"></a>.

### Prioritizing Polish and Reliability
Stripe's culture allows for setting aside bandwidth for "polish" and addressing issues that arise from friction logging <a class="yt-timestamp" data-t="00:36:17"></a>. This is ingrained in planning by prioritizing "incident remediations" (fixes for things that go wrong) ahead of other roadmap work <a class="yt-timestamp" data-t="00:36:04"></a>.

## Tools and Processes for Continuous Quality

Stripe emphasizes rapid iteration while maintaining high reliability and availability <a class="yt-timestamp" data-t="00:53:50"></a>. They deploy changes to their core API 16.4 times a day on average, with an uptime of 99.999% <a class="yt-timestamp" data-t="00:52:12"></a>.

Key enablers include:
*   **Comprehensive Automated Test Suites:** Every change goes through a battery of automated tests before deployment <a class="yt-timestamp" data-t="00:54:24"></a>. There are no manual testers <a class="yt-timestamp" data-t="00:54:27"></a>.
*   **Progressive Rollouts:** Changes are deployed to production starting with a very small percentage of traffic, gradually ramping up to detect problems early <a class="yt-timestamp" data-t="00:54:51"></a>.
*   **Automated Deployment:** Once an engineer's change passes tests and is reviewed, it automatically ends up in production within approximately 45 minutes <a class="yt-timestamp" data-t="00:55:20"></a>. This tight feedback loop allows for user feedback in the morning and a solution in their hands by the end of the day <a class="yt-timestamp" data-t="00:58:13"></a>.
*   **Continuous Learning from Incidents:** Stripe obsesses over reviewing incidents, identifying not only what went wrong but how to prevent entire classes of issues in the future. These fixes are prioritized over other roadmap items <a class="yt-timestamp" data-t="00:56:47"></a>.
*   **Chaos Testing:** Injecting errors to ensure systems respond without impacting users <a class="yt-timestamp" data-t="00:57:22"></a>.
*   **"Crying Octopus" Button:** A simple emoji button in developer tools allows engineers to quickly report "paper cut" problems, which are then used by the developer productivity team to prioritize their roadmap <a class="yt-timestamp" data-t="01:27:32"></a>.
*   **AI Integration:** Stripe leverages AI to enhance productivity. Copilot is available to engineers to accelerate tasks like test case generation and boilerplate code, allowing them to focus on larger architectural problems <a class="yt-timestamp" data-t="01:13:58"></a>.

## The Role of Product Managers Today
While engineers remain product-minded, PMs play an "absolute linchpin role" at Stripe <a class="yt-timestamp" data-t="00:21:04"></a>. Product building is a highly cross-functional team sport, involving not only engineers, managers, and designers but also financial partnerships, legal, risk, and compliance teams <a class="yt-timestamp" data-t="00:20:00"></a>. PMs provide the "locomotion" to bring these partnerships together, synthesize user learnings, and drive product strategy, ensuring long-term paths are aligned <a class="yt-timestamp" data-t="00:21:09"></a>.

## Key Takeaways for [[building_an_entrepreneurial_culture | Building a Product-Oriented Engineering Culture]]
*   **Deep User Engagement:** Build mechanisms to listen to users, get products into their hands quickly, and gather rapid feedback <a class="yt-timestamp" data-t="00:43:09"></a>.
*   **Meticulousness where it Matters:** Intentionally identify areas to "sweat the details" based on user impact <a class="yt-timestamp" data-t="00:27:47"></a>.
*   **Culture of Continuous Learning:** Prioritize fixing issues and learning from mistakes to prevent future problems <a class="yt-timestamp" data-t="00:55:57"></a>.
*   **Empowerment:** Enable engineers with good tools and processes to deliver changes continuously <a class="yt-timestamp" data-t="00:51:06"></a>.
*   **Shared Language and Metrics:** Ensure everyone understands the product experience and aligns on metrics to drive progress <a class="yt-timestamp" data-t="00:39:53"></a>.
*   **Leadership by Example:** Managers should actively engage with the product and development process to model the desired culture <a class="yt-timestamp" data-t="00:46:04"></a>.
*   **Strategic Planning:** Focus on user needs and iterate planning processes based on company growth and evolving needs <a class="yt-timestamp" data-t="01:17:02"></a>.
*   **Cross-Functional Collaboration:** Recognize product development as a team sport, involving all necessary functions from the early stages <a class="yt-timestamp" data-t="00:20:00"></a>.