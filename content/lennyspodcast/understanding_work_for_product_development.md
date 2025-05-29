---
title: Understanding work for product development
videoId: Ub9UkWByFIQ
---

From: [[lennyspodcast]] <br/> 

"Understand work" is a critical phase in product development, emphasizing deep learning before execution. It is a concept championed by Bengali as a foundational element of a product team's workflow <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. This approach aims to prevent the "anti-pattern" of product development, where teams identify a feature, justify its existence with data, and then execute without truly understanding user needs or market dynamics <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.

## The Anti-Pattern: Identify, Justify, Execute

The common pitfall, referred to as the "identify, justify, execute" anti-pattern, occurs when a team decides to build something based on an initial idea, then seeks data to validate that idea, and finally spends significant time building it, only to find that the product doesn't achieve the desired impact or metrics remain flat <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>, <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>. This happens because the team failed to grasp key components such as real user pain points, the value of alternatives, or the ideal user experience <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

Instead, the preferred framework is "understand, identify, execute," where comprehensive understanding precedes any decision to build <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## What is Understand Work?

Understand work is defined as an intentional allowance in the product development process to de-risk a project and gain crucial insights <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>, <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. It involves planned, dedicated time for the team to thoroughly investigate and comprehend the problem space <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. This intentional allocation prevents the assumption that understanding will happen passively in the background while execution sprints forward <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.

## Operationalizing Understand Work

To effectively implement understand work, it needs to be integrated into the team's regular workflow:

*   **Intentional Affordance:** Explicitly list understand work items on roadmaps or in sprint plans. For example, a product manager might allocate time to write a strategy, or a designer to create a prototype <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
*   **Cross-Functional Involvement:** Every function within a team can and should contribute to understand work.
    *   **Data Science** can pull funnels and analyze different user connection types to identify issues <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>, or work on [[developing_and_deploying_a_product_strategy | activation metrics]] and proxy metrics <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.
    *   **Engineering** can instrument logging to ensure data visibility or analyze code for refactoring needs and scalability <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>, <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.
    *   **Product Management** might focus on partnership strategy ahead of launch <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.
*   **Balancing Execution and Understanding:** Initially, a team might spend more time on understand work (e.g., 40%), especially when entering a new, complex problem space <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. As knowledge grows, the balance shifts towards more execution (e.g., 80-85%), with understand work becoming more focused on identifying low-to-medium effort, high-impact opportunities, or running "cheap tests" to learn quickly <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>, <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>, <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>.
*   **Bottoms-Up Approach:** Teams should be encouraged to ask "what else do we need to understand?" during planning sessions, involving cross-functional partners like go-to-market and marketing, not just product, design, data science, and engineering <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>.

## Benefits of Understand Work

*   **De-risking Projects:** It clarifies root causes, "jobs to be done," and the right use cases, significantly de-risking projects before extensive development <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>.
*   **Empowering Teams:** It enables teams to confidently push back on ideas that lack sufficient understanding, fostering a culture of informed decision-making <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>.
*   **Velocity Multiplier:** By running "parallel paths of work" (executing on high-conviction items while simultaneously doing understand work), teams gain continuous learnings and insights. This leads to a higher win rate on shipped features and overall increased velocity over time <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>, <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>.
*   **Clarity and Purpose:** It helps teams understand what to work on and, crucially, what *not* to work on, providing clarity and purpose to their efforts <a class="yt-timestamp" data-t="00:58:19">[00:58:19]</a>.

> "If you actually think about it what is a better outcome is a better outcome to just ship more faster now but most of the things are unimpactful right or is it a better outcome to ship fewer things but really work on making sure that you're shipping them in the best way and de risking a lot of other things so that a year later your win rate's higher and your velocity is higher" <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>

The emphasis on understand work highlights that slowing down to gain deeper insight can paradoxically lead to faster, more impactful execution in the long run <a class="yt-timestamp" data-t="00:34:26">[00:34:26]</a>.

## Examples of Understand Work in Practice

*   **Instagram Onboarding:** Upon joining Instagram in 2016, a critical "understand work" project was to instrument logging for the entire signup flow. Previously, only the start and end of the flow were logged, obscuring drop-off points within the eight-step process. This initial understanding phase was crucial before attempting to fix issues <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>.
*   **YouTube Live Virtual Goods:** For a team working on paid virtual goods in YouTube's live experience, initial "understand work" focused on mapping out the entire live ecosystem funnel – how many people watch live, click through, see the product, and buy. This was necessary to identify opportunities before iterating on existing products <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
*   **Instagram Account Access:** A significant problem at Instagram was account churn due to users being unable to log back in (hundreds of thousands daily, leading to millions of lost monthly active users annually) <a class="yt-timestamp" data-t="01:20:16">[01:20:16]</a>. Understanding work revealed that users needed to log out (e.g., sharing phones in regions with prepaid plans) <a class="yt-timestamp" data-t="01:21:27">[01:21:27]</a>. The solution involved simplifying login with an "Omni box" (email, phone, handle in one field) and offering to save credentials upon logout. This led to unexpected insights about increased content creation from second and third accounts, leading to the creation of a "multiple accounts" team <a class="yt-timestamp" data-t="01:23:07">[01:23:07]</a>. This exemplifies how understand work can lead to solving problems and uncovering new, impactful opportunities.
*   **Facebook Friend Recommendations in India:** When Facebook's people graph appeared "broken" in India (fewer common friends, high friending/unfriending rates), extensive on-the-ground understand work revealed cultural context was missing. Western-centric profile fields (school, job title) were irrelevant for many Indian users, who instead looked at photos for identifying friends. This led to the realization of common names (e.g., 250,000 "Amit Kumar" profiles monthly) and the need for creative solutions to connect users <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This demonstrates the power of understand work to reveal [[understanding_company_cultures_impact_on_product_development | cultural context]] and drive significant product adaptations.
*   **Instacart Reordering:** Understanding the "job to be done" for grocery shopping (meal preparation, not just acquiring ingredients) led to realizing that Instacart made reordering difficult, despite 90% of repeat orders being similar. This insight highlighted a missed growth opportunity and the need to simplify the reordering experience <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>, <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

## Adjacent User Theory

A key aspect of understand work, particularly for driving growth, is focusing on the "adjacent user" <a class="yt-timestamp" data-t="00:56:28">[00:56:28]</a>. The adjacent user is the next group of people who *could* be using the product but currently aren't, or aren't getting value from it. Existing power users often have a deep, informed knowledge of the product, making their experience vastly different from a new or less tech-savvy user <a class="yt-timestamp" data-t="00:56:42">[00:56:42]</a>.

Understanding the adjacent user involves:

*   **Identifying the next user persona:** Understanding who they are, what motivates them, and why the current product doesn't work for them <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>.
*   **Dogfooding as the adjacent user:** Actively using the product from their perspective to identify pain points and broken experiences <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a>.
*   **Qualitative Research:** Talking to and visiting these users to observe their real-time interactions with the product <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>.

This approach is mandatory for hypergrowth companies, where user personas change rapidly, but is also highly beneficial for slower-growing companies looking to expand their audience or capture more share of wallet <a class="yt-timestamp" data-t="01:07:21">[01:07:21]</a>. It's about looking just "outside the circle" of current users to understand what is needed for the next wave of adoption <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>. This emphasizes [[integrating_ux_research_into_product_development_cycles | user research]] and deep empathy for potential users.