---
title: Balancing revenue goals and technological advancements
videoId: DjUIecgpYAo
---

From: [[aidotengineer]] <br/> 

Many teams often approach their [[AI strategies in financial technology companies | AI strategy]] like ordering takeout, choosing something appealing online and paying a premium, only to find it doesn't meet expectations due to overly high expectations [00:00:01]. While advanced, bleeding-edge models may suit external customers numbering in the millions, they can be an unnecessary luxury for internal company needs, akin to garnishing instant noodles with truffles [00:00:27]. A different approach, focusing on specific internal needs, has proven successful in delivering millions of dollars in revenue [00:00:42].

## The Build vs. Buy Dilemma

In Q1 2024, a classic "build or buy" dilemma arose. The choice was to build an internal system with two developers over approximately 10 sprint weeks [00:00:59]. This resulted in several million dollars of Annual Recurring Revenue (ARR) and a group-level award [00:01:10]. Complex external solutions, often touted on platforms like Twitter, involving giant evaluations, multi-agent systems, and RF models, while appearing "delicious," can cost a fortune and delay launch [00:01:27]. These are often perfect for flashy SaaS demos but are overkill for in-house requirements [00:01:43].

When considering this dilemma:
*   **Buy** (SaaS) is suitable for exploring the unknown, especially when vendor integrations or cross-industry best practices are required [00:02:04].
*   **Build** (in-house) wins when the company already owns the data, colleagues possess specific knowledge to close deals, and they can be involved in double-checking outputs [00:02:24]. Sitting next to users allows for same-day tweaks, UIs that speak their language, and leveraging existing infrastructure, significantly reducing [[cost_management_in_ai_projects | costs]] [00:02:42].
*   The general rule is to buy to explore the unknown but build in-house once the workflow is well-understood and owned [00:03:02].

## Prioritizing for Revenue Impact

A successful recipe for [[AI integration in financial systems at Ramp | AI integration]] focuses on foundational principles:

### 1. Focus on One Painful Job to Be Done
In-house development excels at going "absurdly deep" on a single, painful task without needing to chase a total addressable market [00:03:29]. The key is to pick something where the "value event"—the dollar-based outcome—can be easily pinpointed [00:03:42]. Starting with a simple sales alert use case and growing from there proved effective [00:03:54]. By focusing intensely on one use case, complexity is reduced, and general purpose [[AI applications and customer success stories | agentic solutions]] can be avoided [00:04:03]. Understanding users' needs through direct communication is crucial to nailing the solution [00:04:19].

### 2. Revenue Impact Trumps Evaluation Metrics
Offline evaluations (like F1 score or NDCG) are important "smoke alarms" but do not directly sign contracts or impress board members [00:04:36]. The ultimate question is whether the solution moved revenues [00:04:46]. It is essential to instrument everything to track the actual financial impact, linking each [[AI applications and customer success stories | AI task]] to a specific dollar value [00:04:59]. Building a complete revenue funnel, from start to the final "value event," is critical [00:05:11]. This linkage simplifies decision-making and prioritization, shifting conversations to potential revenue generation [00:05:31]. Automating team performance reports and creating leaderboards can also foster healthy competition and leadership investment [00:05:52].

### 3. Proactive Insights and Actionable Guidance
Instead of waiting for users to ask questions, the system should anticipate their needs and proactively push insights [00:06:11]. The goal is to be the "chef who anticipates what the next dish should be" [00:06:16]. For example, sending daily digests of critical information can turn the primary UI into a fallback for unexpected tasks [00:06:37].

Furthermore, an [[AI applications and customer success stories | AI system]] should guide action, not just deliver information [00:07:05]. Saving time is worthless if users fill it with unproductive activities [00:07:14]. The real power comes from converting time saved into time "well spent" on highest-value activities [00:07:24]. Proactive systems that surface opportunities users wouldn't have considered can lead to significantly higher Net Promoter Scores (NPS) and engagement compared to chat applications [00:07:43]. This approach ensures that time savings are channeled into the highest value activities, directly impacting revenue [00:10:23].

## Strategic Investment: Data Over Models

When considering investment of limited development resources, "good data consistently beats great models" [00:08:11]. While "shiny things" like complex models are appealing, they can be significantly more expensive and slower (e.g., GPT-3 being 60 times more expensive and an order of magnitude slower than GPT-4-mini) [00:08:22]. The biggest impact on production [[cost_management_in_ai_projects | costs]] often comes from model choice [00:08:30].

The best results have been observed from simply adding more triggers to alert users and going deeper into their needs [00:08:34]. Changes in models have primarily affected costs and evaluations, not necessarily user value [00:08:45]. Therefore, it is crucial to build for user needs rather than for desired technological experimentation [00:08:55]. This aligns with [[AI Engineering Trends | AI Engineering Trends]] that prioritize practical value over theoretical performance.

## The Revenue Flywheel: User-Guided Development

Focusing on what users truly value, instead of just chasing model benchmarks, initiates a "powerful flywheel" [00:09:03]. Tight feedback loops make users feel heard, encouraging them to provide ideas for improvements [00:09:17]. This user feedback enables rapid experiments, which drives even more adoption, generates more data for prioritization, and leads to further ideas [00:09:27]. This iterative process causes the "revenue flywheel" to spin faster and faster, continually driving business growth [00:09:38]. This is a key aspect of [[leveraging_ai_tools_for_efficiency_and_scalability | leveraging AI tools for efficiency and scalability]] and achieving [[outcome_based_pricing_models | outcome-based pricing models]] internally.

In summary, to balance revenue goals and technological advancements:
*   Focus on one specific, painful problem with a clear dollar value, avoiding comprehensive "boil the ocean" solutions [00:09:52].
*   Prioritize revenue impact over evaluation metrics, tracking everything to the final dollar-based outcome [00:10:01].
*   Push insights proactively and ensure time savings are channeled into the highest-value activities [00:10:11].
*   Invest in foundational data and triggers rather than chasing complex, expensive models [00:10:29].
*   Start small, follow the money, and let users guide development [00:10:37].