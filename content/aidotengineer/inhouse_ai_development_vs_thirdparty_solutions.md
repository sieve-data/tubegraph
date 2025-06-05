---
title: Inhouse AI development vs thirdparty solutions
videoId: DjUIecgpYAo
---

From: [[aidotengineer]] <br/> 

Many teams approach their [[AI in enterprise and startups | AI strategy]] by treating it like ordering takeout: picking something appealing online and paying a premium, only to find it doesn't meet expectations <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This often stems from overly high expectations influenced by social media showcases of "bleeding edge models" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. While such advanced models might be suitable for millions of customers, they can be an expensive overkill for internal company needs <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## A Different Recipe: Building In-House

A different approach, focusing on in-house development, has delivered millions of dollars in revenue <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. For example, in Q1 2024, a team faced the classic "build or buy" dilemma and chose to build <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. With just two developers and approximately 10 sprint weeks of effort, they created a system that generated several million dollars in Annual Recurring Revenue (ARR) and earned a group-level award <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This success demonstrated that focusing on complex features like "giant evals, multi-agent systems, or RF models" (often seen on social media) would have been detrimental, leading to high costs and delayed launches <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. These flashy solutions are often perfect for SaaS demos but overkill for internal needs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## The Build vs. Buy Decision

### When "Buy" (SaaS) Shines

Buying a Software as a Service (SaaS) solution can be compared to a "hotel buffet" – generic but safe <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. It is advantageous when:
*   You require vendor integrations <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   You need cross-industry best practices <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### When "Build" (In-House) Wins

Building in-house, like preparing a "home kitchen" meal, is superior when:
*   You already own the data <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Your colleagues possess precise knowledge of workflows (e.g., exact keystrokes to close deals) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   You can involve internal users in double-checking outputs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   Proximity to users allows for same-day tweaks and UI that speaks their language <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   The system can run on existing infrastructure, significantly lowering costs <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The general rule of thumb is to "buy SaaS to explore the unknown, but build in-house once the workflow is yours" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Five Lessons for Successful In-House AI Development

These lessons work best when applied as a set, starting with the foundation:

### 1. Focus on One Painful Job to Be Done (JTD)

In-house development excels at going "absurdly deep on one painful job to be done" without needing to chase a large total addressable market <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Identify a Value Event**: Pick something where you can easily pinpoint a clear, dollar-based outcome <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Start Simple**: For instance, begin with a simple sales alert use case and expand from there <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Engage Users**: Your users know best what's needed; talk to them to truly nail the solution <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Keep it Simple**: Staying focused allows you to avoid complex, "agentic" systems <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This also helps with [[challenges_in_building_ai_applications | challenges in building AI applications]].

### 2. Track Revenue Impact (Not Just Evaluation Metrics)

Offline evaluations (evals) are important as "smoke alarms," but they don't sign contracts <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Focus on Dollars**: Board meetings ask about revenue impact, not F1 scores or NDCG <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Instrument Everything**: Ensure you can trace an [[AI in enterprise and startups | AI]] task's contribution directly to revenue <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Build Revenue Funnels**: Map the entire process from beginning to end to the defined "value event" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Users as Guard Rails**: Your users can serve as guard rails for ambitious experiments, reducing the need to overthink evaluations <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Simplify Decisions**: Linking your system to dollar impact streamlines decision-making and prioritization <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Automate Reports and Leaderboards**: Automate team performance reports and create leaderboards to foster healthy competition, engage leadership, identify champions, and support struggling users <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### 3. Be Proactive, Anticipate User Needs

Don't wait for users to come to you; become the "chef who anticipates what the next dish should be" <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **The Best UI is Invisible**: The most effective user interface is one users never need to use <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Automate Tasks**: Since you understand the business, proactively take the next steps for users rather than waiting for requests <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Example**: Building a motion to send daily digests ("Here is what you need to know today") <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   A traditional UI can still exist as a fallback for unexpected tasks <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 4. Guide Action, Don't Just Deliver Information

Your [[AI in enterprise and startups | AI]] system should guide action, not merely provide information <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Convert Time Saved to Time Well Spent**: Saving 30 minutes is pointless if users fill it with unproductive tasks <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The true value comes from converting saved time into engagement with high-value activities <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Leverage Revenue Funnels**: As you build revenue funnels, you gain insights into where to direct freed-up time and user attention <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Proactive System Success**: Proactive systems that surface unthought-of actions can achieve significantly higher NPS (20 points higher) and engagement than chat-based applications <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This highlights a successful [[ai_enhanced_vs_ai_native_organizations | AI-enhanced organization]] approach.

### 5. Invest in Good Data, Not Just Great Models

This is a secret often not found on social media: good data consistently outperforms great models <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This is critical for [[challenges_in_ai_development | AI development]] and [[challenges_in_scaling_ai_products | scaling AI products]].
*   **Cost vs. Performance**: More advanced models (like O3) can be 60 times more expensive and an order of magnitude slower than simpler ones (like 41 mini), primarily impacting production costs <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Focus on User Needs**: The best results come from adding more triggers to alert users and delving deeper into their specific needs <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Changes in models often only affect costs and evaluations, not user value <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **The Revenue Flywheel**: Focusing on true user value rather than chasing model benchmarks initiates a powerful feedback loop <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>:
    *   Tight feedback loops make users feel heard <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
    *   Users provide ideas for improvements <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   This enables running experiments based on feedback <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   Which drives more adoption <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   Generating more data for prioritization and new ideas <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   Accelerating the "revenue flywheel" <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Key Takeaways

To successfully implement [[AI in enterprise and startups | AI]] in-house:
*   **Focus Small**: Concentrate on one painful job with a clear dollar value, avoiding comprehensive "boil the ocean" solutions <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Follow the Money**: Prioritize revenue impact over evaluation metrics, tracking everything to the final dollar-based outcome <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Be Proactive**: Push insights proactively instead of waiting for user questions <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Guide Action**: Ensure time savings are channeled into the highest-value activities <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Invest in Basics**: Prioritize good data and user needs over chasing complex models; it truly pays off <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

In essence: Start small, follow the money, and let your users guide you <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.