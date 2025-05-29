---
title: Improving user experience through customer feedback
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Improving user experience is paramount for building successful and beloved products, a philosophy deeply ingrained in product leadership, as exemplified by Jeff Weinstein's approach at Stripe. This focus extends beyond mere aesthetics to deeply understanding and addressing customer needs <a class="yt-timestamp" data-t="01:55:01">[01:55:01]</a>.

## The Value of Customer Feedback

The feedback loop with customers is considered an "unbelievable gift" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. When a customer feels compelled enough to voice a problem, it signals a significant unmet need <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Breaking Down the Wall

Traditional barriers between product managers and customers are actively broken down. Jeff Weinstein openly shares his email and is frequently on calls with customers, bypassing intermediaries like user research teams <a class="yt-timestamp" data-t="02:43:03">[02:43:03]</a>. This direct [[effective_customer_interaction_and_feedback_gathering | customer interaction]] provides raw, unfiltered insights <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Listening Effectively

A key technique for [[effective_customer_interaction_and_feedback_gathering | gathering feedback]] is to "sit in silence" <a class="yt-timestamp" data-t="02:17:20">[02:17:20]</a>. Rather than pitching a product or solution, the goal is to prompt customers to share their burning problems, allowing their true pain points to emerge organically <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>. This approach helps in [[leveraging_user_insights_for_product_development | leveraging user insights]] to uncover critical issues that might otherwise be missed <a class="yt-timestamp" data-t="02:48:09">[02:48:09]</a>.

Examples of prompts that encourage open sharing include:
*   "Do you mind just opening up your email, like what's in there?" <a class="yt-timestamp" data-t="02:32:32">[02:32:32]</a>
*   "If you weren't talking to me right now, what would you be working on?" <a class="yt-timestamp" data-t="02:35:37">[02:35:37]</a>
*   "Last week, what grinded your gears?" <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>
*   "Magic wand, what do you wish you could just have off your plate immediately?" <a class="yt-timestamp" data-t="02:43:45">[02:43:45]</a>
*   Asking about their regular life, which often leads to them "spilling" their biggest problems <a class="yt-timestamp" data-t="02:45:15">[02:45:15]</a>.

### Responding with Speed

Speed is critical when a customer provides feedback. A prompt response, even if brief, validates their effort and builds trust <a class="yt-timestamp" data-t="03:08:48">[03:08:48]</a>. This rapid engagement helps turn potential detractors into promoters, as demonstrated when a serious bug in Stripe Atlas was quickly addressed, transforming a critical user into a valuable long-term partner <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

### Prioritizing Feedback

While large volumes of feedback are a "problem to have," it's crucial to select where to go deep <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Key prioritization strategies include:
*   **Focusing on paying customers:** Feedback from paying customers is given priority because they are willing to exchange value for a solution to their problem <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. Friends or beta testers' feedback is discounted to zero if they aren't the target paying customer <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   **Willingness to pay vs. paying:** The act of *actually paying* is significantly different from being "ready to pay" <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. Encouraging customers to practice paying, even a small amount, reveals their true commitment to a solution <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
*   **Self-selection:** Asking for screenshots, videos, or detailed bullet points (e.g., "three to five bullet points") helps self-select those truly invested in providing detailed, actionable feedback <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Bounded programs:** Creating temporary, named programs (e.g., "bugfinder program") can encourage a burst of focused feedback within a set timeframe <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

## Measuring User Experience

Metrics are seen as a numerical representation of the value a product provides to the customer <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. They serve as "deep deep siblings and equals" to qualitative feedback (like tweets) <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

### Metrics Reflecting Customer Value

The most effective metrics measure success from the customer's perspective, rather than internal operational metrics <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. They should force trade-offs and decision-making for teams <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

A prime example is the metric used for Stripe Atlas: **"Companies with zero support tickets"** <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   This metric directly correlates with customer satisfaction and willingness to recommend the service <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   It tracks the percentage of users who complete the entire incorporation process (from application start to two weeks post-IRS/government communication) without contacting support <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
*   By focusing on this metric, the team dramatically improved the user experience, increasing the percentage from 15% to 85% over 18 months, which directly correlated with market share growth <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.
*   It motivated engineers to address common support issues by baking solutions directly into the product, essentially turning engineers into "PMs" for specific problem areas <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

### "Users Having a Bad Day" Metric

For any business, a powerful metric to implement is "users having a bad day" <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.
*   This involves emitting a log line whenever a user encounters a known problem (e.g., 404 error, delayed payout, multiple payment declines) <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>.
*   These "bad day reasons" can be visualized in a stacked bar chart, revealing their frequencies <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.
*   The goal is to eradicate these bad day reasons, not just minimize them <a class="yt-timestamp" data-t="01:02:35">[01:02:35]</a>.
*   It's a way to scale understanding of user issues across teams, encouraging anyone to add new "bad day" events to the chart <a class="yt-timestamp" data-t="01:02:19">[01:02:19]</a>.

## Cultivating Empathy and Understanding

Beyond metrics, fostering empathy for the customer is crucial for [[understanding_and_improving_developer_experience | understanding and improving developer experience]] and overall user experience <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

### Study Groups

Jeff Weinstein initiated "study groups" at Stripe to increase the frequency and fun of internal product review <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Format:** Typically four to eight people from different parts of the company (e.g., support, sales, engineering) meet <a class="yt-timestamp" data-t="01:17:13">[01:17:13]</a>.
*   **Rule 1: "You do not work at Stripe."** Participants pretend to be a company with a specific problem (e.g., Dolphin Aquarium Industries trying to sell in-person tickets). They must not use any internal Stripe knowledge to navigate the product <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>. This forces participants to embody the customer's perspective painstakingly slowly <a class="yt-timestamp" data-t="01:22:23">[01:22:23]</a>.
*   **Rule 2: "We're not here to solve any problems."** The primary goal is to practice empathy, not to critique or file bugs during the session. Outputs are recorded and can be funneled into existing formal bug processes later <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>.
*   **Impact:** Over 250 people participated in 25+ study groups in early 2024, leading to "deeply eye-opening" experiences and increased motivation for teams to act on observed issues <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

### Product Experience Beyond Software

The concept of "product" extends beyond software interfaces to encompass the entire customer journey <a class="yt-timestamp" data-t="01:29:18">[01:29:18]</a>. This includes human interactions, administrative processes, sales, and support <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   For example, Fidelity's process for 401k rollovers, involving a phone call with a knowledgeable person who knew the customer's details and sent a pre-filled envelope with clear instructions, is considered a "product experience" even without being a purely digital solution <a class="yt-timestamp" data-t="01:28:41">[01:28:41]</a>.
*   When customers reach out to support or sales for help, their inquiries themselves define what the product needs to be. For a self-service product with high support volume, the support contacts *are* the product, indicating areas for improvement or even a need for human intervention as part of the intended flow <a class="yt-timestamp" data-t="01:27:20">[01:27:20]</a>.
*   Allowing customers to *design* parts of the product, such as a dashboard in a collaborative tool like Whimsical, can yield direct and valuable insights, short-circuiting traditional design processes <a class="yt-timestamp" data-t="02:17:15">[02:17:15]</a>. This represents giving customers "write access" rather than just "read access" to the company's development process <a class="yt-timestamp" data-t="02:18:11">[02:18:11]</a>.

Ultimately, consistently prioritizing customer feedback and integrating it into every aspect of product development leads to [[building_customercentric_products_through_design | building customer-centric products]] that resonate deeply and drive sustained growth <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.