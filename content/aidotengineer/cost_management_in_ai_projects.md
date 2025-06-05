---
title: Cost management in AI projects
videoId: DjUIecgpYAo
---

From: [[aidotengineer]] <br/> 

Many teams approach their AI strategy similarly to ordering takeout: selecting something that appears good online, paying a premium, and later discovering it falls short of expectations <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This often stems from overly high expectations driven by discussions on platforms like LinkedIn or Twitter, which showcase "bleeding edge models" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. While these might suit large-scale consumer applications, for internal company use, they can be likened to "paying for truffles to garnish your instant noodles" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, representing an unnecessary expense.

A different approach, which delivered millions of dollars in revenue, focuses on a more practical "recipe" for AI implementation <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Build vs. Buy Dilemma

In Q1 2024, a team faced the classic "build or buy" decision for their AI solution <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. They opted to build in-house, utilizing two developers and approximately 10 sprint weeks of effort <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This resulted in a system that generated several million dollars in Annual Recurring Revenue (ARR) <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Contrastingly, strategies often seen on social media, involving "giant evals, multi-agent systems, RF models," while appearing appealing, can "cost a fortune" and significantly delay launch <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. These advanced solutions are often "overkill for your in-house needs" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The rule of thumb for cost-effective AI implementation is: "buy SaaS to explore the unknown but build in-house once the workflow is yours" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Advantages of In-House Development for Cost Efficiency

Building AI solutions in-house offers significant [[cost_considerations_in_ai_agent_development | cost advantages]], particularly for internal applications:

*   **Data Ownership and Proximity**: When a company already owns the necessary data, developing in-house leverages this asset effectively <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **User Involvement**: Direct collaboration with internal users who understand the precise workflows allows for double-checking outputs and ensuring relevance <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Rapid Iteration**: Proximity to users enables same-day tweaks and adjustments, enhancing agility <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Leveraging Existing Infrastructure**: Running AI solutions on infrastructure already paid for significantly reduces additional expenses <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

These factors collectively "drop the cost to pennies" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Key Lessons for [[Cost and latency optimization in AI deployments | Cost-Effective AI Implementation]]

The speaker shares five key lessons for successful and [[strategies_for_effective_ai_implementation | cost-effective AI implementation]]:

### 1. Focus on a Single Painful Job with Clear Value

Instead of attempting a comprehensive solution that tries to "boil the ocean" <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, concentrate on one specific, painful task <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This allows for absurdly deep dives into a problem without chasing a total addressable market <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Identify a "value event"—a clear dollar-based outcome—that the AI solution will drive <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. By going deep on a single use case, such as a simple sales alert, the process becomes much simpler, avoiding overly "agentic" designs <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### 2. Prioritize Revenue Impact Over Evaluation Metrics

While offline evaluations are important as "smoke alarms," they should not be the primary metric for success <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Boards ask about revenue, not F1 scores or NDCG <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Therefore, instrument everything to track the actual financial impact, linking AI tasks directly to revenue generation <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Building a revenue funnel from beginning to end, culminating in the defined value event, is crucial <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. When a system is linked to dollars, decisions and prioritization become straightforward <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This also enables the automation of team performance reports and leaderboards, fostering healthy competition and identifying champions or those needing support <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### 3. Push Insights Proactively

Don't wait for users to ask for information; become the "chef who anticipates what the next dish should be" <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The most effective UI is often one that users "never need to use" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Proactive systems, like daily digests of key information, can be highly effective, with traditional UIs serving as fallback for unexpected tasks <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 4. Guide Action, Don't Just Deliver Information

Simply saving time is insufficient if users fill that time with unproductive activities <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The true power of AI comes from converting saved time into "time well spent" on the highest-value activities <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. As revenue funnels are built, it becomes clearer where to divert users' freed-up time and attention <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Proactive systems that surface actions users wouldn't have considered can lead to significantly higher engagement and Net Promoter Scores (NPS) compared to chat applications <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### 5. Invest in Good Data Over Great Models

This is a critical decision point for [[cost_considerations_in_ai_agent_development | resource allocation]]. "Good data consistently beats great models" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. While advanced models like GPT-3 might be 60 times more expensive and an order of magnitude slower than alternatives like GPT-4 mini, their biggest impact in production is often on [[cost_and_latency_optimization_in_ai_deployments | cost]] <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The best results often come from simply adding more triggers to alert users and understanding their needs more deeply <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Changes in models have primarily affected costs and evaluations, not necessarily user value <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Building for user needs rather than chasing model benchmarks leads to a powerful flywheel: tight feedback loops make users feel heard, leading to more ideas for improvements, which drives more adoption, generating more data for prioritization, and more ideas, accelerating the revenue flywheel <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

In summary, for effective [[cost_considerations_in_ai_agent_development | cost management in AI projects]], teams should start small, follow the money, and let their users guide development <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.