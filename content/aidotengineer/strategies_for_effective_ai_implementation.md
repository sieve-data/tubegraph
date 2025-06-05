---
title: Strategies for effective AI implementation
videoId: DjUIecgpYAo
---

From: [[aidotengineer]] <br/> 

Many teams approach their AI strategy like ordering takeout, choosing something that looks good online and paying a premium, only to find it doesn't meet expectations due to overly high expectations <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. While social media often showcases "bleeding edge models" suitable for millions of customers, this can be overkill and expensive for internal company needs, akin to "paying for truffles to garnish your instant noodles" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. A different, more practical recipe, which delivered millions of dollars in revenue, focuses on strategic in-house development and user-centricity <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Build vs. Buy: The Core Dilemma

In Q1 2024, a team faced the classic "build or buy" dilemma for an AI solution <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. They opted to build in-house with two developers and roughly 10+ sprint weeks of effort, resulting in several million dollars of Annual Recurring Revenue (ARR) and a group-level award <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Approaches featuring "giant evals, multi-agent systems, RF models" — often seen as cutting-edge — are costly and delay launch, making them ideal for flashy demos but overkill for internal needs <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

Software as a Service (SaaS) is comparable to a hotel buffet: generic but safe <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. However, internal users often desire a customized solution, or "grandma's secret sauce," over generic options <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

**When to Buy SaaS:**
*   SaaS solutions excel when you require vendor integrations or access to cross-industry [[best_practices_for_implementing_ai_in_teams | best practices]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

**When to Build In-House:**
*   Building in-house is advantageous when your organization already owns the data <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Your colleagues possess specific knowledge about workflows and can be involved in double-checking outputs <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   Proximity to users allows for rapid tweaks that can ship the same day <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   User interfaces can be tailored to speak their language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Leveraging existing infrastructure reduces costs significantly, sometimes to pennies <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The rule of thumb is to buy SaaS when exploring the unknown but build in-house once the workflow is established and owned internally <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Five Lessons for Effective AI Implementation

Effective AI implementation is built upon five interconnected lessons <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>:

### 1. Focus on One Painful Job
In-house development shines by allowing deep dives into a single, painful "job to be done" without chasing a broad "total addressable market" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Identify Value Event:** Select a task where the dollar-based outcome, or "value event," is easily pinpointed <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **User-Centricity:** Start with a simple use case, like sales alerts, and expand from there <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Engage users to understand their needs thoroughly and keep the solution simple, avoiding complex multi-agent systems <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### 2. Revenue Impact Trumps Evaluation Metrics
While offline evaluations are important as "smoke alarms," board meetings prioritize revenue impact over F1 scores or NDCG <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Track Money:** Instrument everything to directly link AI tasks to specific dollar values <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Build Revenue Funnels:** Create a complete revenue funnel from beginning to end, leading back to the identified value event <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **User as Guardrails:** Users serve as guardrails, enabling ambitious experiments without overthinking evaluations <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Streamlined Decisions:** Linking the system to financial outcomes simplifies decision-making and prioritization <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Automate Reporting:** Automate team performance reports and create leaderboards to foster healthy competition, gain [[leadership_and_organizational_strategies_for_ai_integration | leadership investment]], identify champions, and support struggling team members <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### 3. Push Insights Proactively
Once revenue is being tracked, become a "chef who anticipates the next dish" rather than waiting for users to come with requests <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Anticipate Needs:** The best UI is one users never need to use; leverage business understanding to proactively implement solutions <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **Daily Digests:** For example, building a system to send daily digests of critical information can serve user needs before they even ask <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. A shared UI can then serve as a fallback for unexpected tasks <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 4. Guide Action, Not Just Deliver Information
Proactive systems should guide action, not merely deliver information <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Convert Time Saved to Time Well Spent:** Saving time is worthless if it's filled with unproductive tasks <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The true power lies in converting saved time into high-value activities by understanding the highest value actions for users and diverting their attention there <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Improved Engagement:** A proactive system that surfaces unforeseen opportunities can significantly boost Net Promoter Score (NPS) and engagement compared to chat-based applications <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### 5. Invest in the Basics: Good Data Beats Great Models
When deciding where to invest limited development resources, "good data consistently beats great models" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Cost vs. Impact:** Larger models like GPT-3 can be significantly more expensive and slower than smaller alternatives like GPT-4 mini, with the biggest impact in production often being on cost <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Focus on Triggers and Depth:** Better results often come from simply adding more triggers to alert users and going deeper into their specific needs, even if it seems "boring" <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Model changes may only affect costs and evaluations, not user value <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **User Value Over Benchmarks:** Build for what users need, not what you want to experiment with <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. Focusing on true user value instead of chasing model benchmarks initiates a "powerful flywheel" <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## The Revenue Flywheel
Focusing on user value creates tight feedback loops, making users feel heard and prompting them to provide improvement ideas <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This feedback enables rapid experiments, driving more adoption, generating more data for prioritization, and leading to more ideas <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This accelerates the "revenue flywheel," leading to continuous improvement and growth <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Key Takeaways for [[Strategies for AI evaluation and troubleshooting | Effective AI Implementation]]
To effectively implement AI solutions, start small and follow these principles:
*   **Focus on one painful job:** Prioritize a specific problem with clear dollar value, avoiding comprehensive "boil the ocean" solutions <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Revenue impact over evaluation metrics:** Track everything to the final dollar-based outcome and base decisions on this financial impact <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Push insights proactively:** Deliver information and guidance before users have to ask for it <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Guide action effectively:** Ensure time savings are channeled into the highest value activities <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Invest in the basics:** Prioritize good data and user needs over chasing the latest, most expensive models <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

In summary, start small, follow the money, and let your users guide your AI strategy <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.