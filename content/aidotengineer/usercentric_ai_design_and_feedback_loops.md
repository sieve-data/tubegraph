---
title: Usercentric AI design and feedback loops
videoId: DjUIecgpYAo
---

From: [[aidotengineer]] <br/> 

Many teams initially approach AI strategy by seeking "bleeding edge models" and complex solutions, often leading to disappointment and high costs for in-house needs <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. While such advanced systems might be suitable for large-scale external applications, they are often "overkill" for internal company requirements <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A more effective approach, particularly for internal tools, involves prioritizing user needs, focusing on specific problems, and establishing robust feedback loops.

## Build vs. Buy: The User-Centric Decision

The decision to build an AI solution in-house versus buying a Software-as-a-Service (SaaS) product should be guided by user-centric considerations <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

*   **When to Buy**: SaaS is beneficial for exploring unknown territories or when requiring vendor integrations and cross-industry best practices <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **When to Build In-House**: Building an internal solution is advantageous when:
    *   The organization owns the data <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   Colleagues possess precise knowledge of workflows needed to achieve goals <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   Users can be directly involved in [[human_reviews_of_ai_outputs | double-checking the outputs]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   Proximity to users allows for rapid adjustments and same-day tweaks <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   The user interface (UI) can be tailored to speak the users' specific language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   The solution can run on existing infrastructure, significantly reducing costs <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The general rule of thumb is to "buy to explore the unknown but build in-house once the workflow is yours" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Five Lessons for User-Centric AI Development

To successfully implement user-centric AI solutions that drive revenue, consider these five lessons:

### 1. Focus on One Painful Job to Be Done

Instead of pursuing a broad, comprehensive solution, concentrate on a single, "painful job to be done" that has a clear, quantifiable "dollar-based outcome" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This deep dive into a specific use case makes the development process simpler and more manageable <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

*   **User Input is Key**: Engage directly with users to understand their needs and challenges fully. "Talk to them to really nail it" <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Keep it Simple**: Staying focused on a narrow use case allows for simplicity and helps avoid complex, [[best_practices_for_building_ai_agents | agentic systems]] that may be unnecessary for internal tools <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### 2. Revenue Impact Trumps Evaluation Metrics

While offline [[evaluations_and_finetuning_in_ai_development | evaluations]] serve as "smoke alarms," the ultimate measure of success is the actual impact on revenue <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Track Everything**: Instrument every part of the system to clearly link AI tasks to specific dollar outcomes, building a "revenue funnel" from start to the final value event <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Users as Guardrails**: Users can act as "guard rails," allowing for ambitious experiments without overthinking [[evaluations_and_finetuning_in_ai_development | evaluations]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Align with Business Goals**: Tying the system to financial impact simplifies decision-making and prioritization, shifting conversations to potential sales and performance <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Automate Reporting**: Automate team performance reports and create leaderboards to foster healthy competition, gain leadership investment, identify champions, and support struggling users <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### 3. Push Insights Proactively

Don't wait for users to ask for information or insights; anticipate their needs and deliver them proactively <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The "best UI is the one you never need to use" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

*   **Anticipate Needs**: As the business owner, you know the next logical steps for users. Proactively provide them, such as daily digests with essential information <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UI as Fallback**: While proactive pushes are primary, a traditional UI can serve as a fallback for unexpected or unplanned tasks <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 4. Guide Action, Don't Just Deliver Information

Simply saving time for users is not enough; the AI system must guide them toward high-value activities <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. If saved time is filled with unproductive tasks, the AI's value diminishes <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

*   **Convert Time Saved into Time Well Spent**: Understand the highest value activities and divert users' newly freed time and attention towards them <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Proactive Systems Drive Engagement**: A proactive system that surfaces activities users wouldn't have considered can lead to significantly higher user satisfaction (NPS) and engagement compared to traditional chat applications <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### 5. Invest in the Basics (Good Data Beats Great Models)

When allocating development resources, prioritize good data and foundational improvements over chasing the latest, most expensive models <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

*   **Data Quality is Paramount**: "Good data consistently beats great models" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. More advanced models often come with significantly higher costs and slower performance without a proportional increase in value for internal use cases <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Focus on User Needs, Not Benchmarks**: The greatest impact often comes from simple improvements like adding more triggers to alert users or deepening the understanding of their specific needs <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Changes in models might only affect costs and [[evaluations_and_finetuning_in_ai_development | evaluations]], not user value <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Build for what users need, not what you want to try <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

## The Revenue Flywheel: A Powerful Feedback Loop

When development focuses on true user value rather than just model benchmarks, a powerful "flywheel" effect begins <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

*   **Tight Feedback Loops**: Users feel heard, leading them to provide more ideas for improvements <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Iterative Improvement**: This feedback enables rapid experiments, driving more adoption <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Data Generation**: Increased adoption generates more data for prioritization and further ideas <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Accelerated Growth**: This continuous cycle causes the "revenue flywheel" to spin faster, leading to sustained improvement and financial impact <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

In summary, start small with a clear dollar value, track revenue impact over traditional metrics, proactively guide users, ensure time savings translate to high-value activities, and invest in fundamental data improvements rather than just complex models <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. Let your users be the guide for effective AI development <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.