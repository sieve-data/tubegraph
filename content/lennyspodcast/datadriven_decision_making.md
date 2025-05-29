---
title: Datadriven decision making
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Jessica Lax, Vice President of Analytics and Data Science at DoorDash, has built one of the largest and most impactful data teams in tech over more than 10 years at the company, starting as the first GM responsible for launching new markets [00:00:51]. Her career began in investment banking at Lehman Brothers and she previously founded a social gifting startup called GS Simple [00:01:06].

## The Role and Structure of Analytics Teams

Lax emphasizes that analytics should be a business impact-driving function, not merely a service function [00:00:05]. Her team focuses on finding opportunities and having a point of view on decisions, answering "what do we do now that we know this?" rather than just "why?" [00:01:11].

### Centralized vs. Embedded Data Teams
Lax holds a "contrarian perspective" that a central model (Center of Excellence) for data teams is superior to embedding analysts directly into business units [00:06:00].

A centralized model means analytics teams report through a dedicated analytics organization (like hers), rather than directly into marketing or other functions [00:07:01]. While the reporting lines are centralized, her team is divided into "pods" that align perfectly with product, engineering, operations, and marketing structures, ensuring they are embedded with partner teams day-to-day [00:08:22]. This allows the analytics team to share the same goals as their partner teams, aligning incentives [00:06:50].

#### Benefits of a Centralized Data Org
*   **Consistent and High Talent Bar** A centralized structure allows for consistent evaluation of technical and soft skills using a common rubric, leading to higher quality hires [00:11:06].
*   **Growth Opportunities** It provides clearer growth paths for data professionals who might otherwise be siloed in a specific business unit [00:11:41]. This helps retain talent by allowing movement between different areas of the company, such as from marketing to merchant analytics, or into people management roles [00:12:05].
*   **Consistency of Methodologies and Metrics** A central team ensures that key metrics, like "sales," are defined and used consistently across the entire company, preventing discrepancies and enabling better collaboration [00:12:48]. It also allows for the improvement of methodologies with broader input, avoiding redundant work across multiple teams [00:13:05].
*   **Scalability** Recognizing common problems across different teams helps identify issues that need automation or improvement as the business scales, allowing the team to anticipate future challenges [00:13:24].
*   **Strong Team Culture and Brand** A central team fosters a unique culture of learning and sharing, where members can support each other, conduct peer reviews, and connect with like-minded "data nerds" [00:13:46].

### Balancing Proactive Insights and Reactive Requests
It's crucial to carve out time for exploratory work and deep dives, as there are always more questions than time [00:15:50]. To ensure this proactive work happens, goals should be set around finding insights through self-directed efforts [00:16:06].

Hackathons are a successful mechanism for this, allowing teams to dedicate days to exploring interesting problems and finding opportunities [00:16:49]. Many great insights that drive future roadmaps have originated from these deep dives [00:17:03].

> [!EXAMPLE] Referral Fraud Deep Dive
> During a hackathon, DoorDash's data team investigated their consumer acquisition referral channel, which showed below-average engagement and payback [00:17:35]. Instead of simply reducing spend, they dug deeper by trying to refer each other and even attempting referral fraud [00:18:12]. This uncovered widespread fraudulent behavior, including people posting codes online to get free discounts [00:19:15]. They found a bimodal distribution: one group of high-quality consumers referring other great consumers, and another group engaged in fraud [00:18:49]. This led to recommendations for better fraud checks and caps on referrals, significantly improving the channel's efficiency [00:19:57]. This example highlights how the average can be misleading and the value of examining distributions [00:20:05].

To manage inbound requests while also pursuing proactive work, [[strategies_for_effective_decisionmaking | data leaders]] and individual contributors (ICs) should:
*   **Establish Clear Operating Models:** Leadership should define rules for working, so junior team members aren't always forced to say no [00:21:14].
*   **Align Goals:** By sharing the same goals as business partners, it's easier to prioritize work based on shared objectives [00:21:32].
*   **Communicate Tradeoffs:** When new requests come in, present the tradeoff by asking if the new task is more important than other planned work [00:22:04]. This makes stakeholders aware of the prioritization decisions [00:22:09].
*   **Ruthless Prioritization:** Continuously re-evaluate priorities with business partners to ensure the team is working on the most impactful things [00:22:50]. Occasionally, quickly fulfilling small requests can build goodwill [00:23:46].
*   **Prove Value:** Demonstrate the value of longer-term, exploratory work by showcasing insights and opportunities found [00:24:06].

## Hiring for Data Teams

Beyond technical skills, which are considered "table stakes," Lax looks for specific unique characteristics in top talent [00:24:32]:
*   **Curiosity:** The ability to be self-motivated, pull on threads, and dig deeper when something seems "off" without being told [00:24:51]. This can be tested in interviews by presenting cases with subtle inconsistencies to see if candidates notice or how they react when inconsistencies are pointed out [00:25:42].
*   **Problem-Solving:** The capacity to break down complex problems and talk through solutions on the fly, as demonstrated through real-world business cases [00:27:16].
*   **Adaptability and Decision-Making:** Observing how candidates react to being told they are wrong, how they pivot with new information, and their ability to make a decision or have a point of view without full information [00:27:56]. This reflects real-life business scenarios where perfect information is rare [00:28:32].

Lax herself has a non-traditional background, initially in art and finance, becoming a data scientist out of necessity [00:29:02]. This has allowed her to hire technically skilled people (PhDs in statistics, ML data scientists) while maintaining a focus on driving [[business_strategy_and_decisionmaking_through_instinct_and_gut | business impact]] [00:30:51]. She encourages hiring individuals from diverse backgrounds (e.g., engineering, operations, marketing, finance) who acquire technical skills on the job or have some formal training, creating a unique environment with complementary skills and expertise [01:06:03]. This diversity also includes hiring people with experience at different company stages, bringing both hustle and grit from startups and knowledge of scale from larger organizations [01:08:04].

## Defining Effective Metrics

Lax highlights key lessons learned about metrics, often from "bad metrics" [00:44:45]:

1.  **Short-Term Metrics for Long-Term Outputs:** The goal is to find a short-term, measurable metric that drives a long-term output [00:44:51]. For example, retention is a "terrible thing to goal on" because it's hard to move meaningfully in the short term [00:45:02]. Instead, identify and test the inputs that drive retention through [[experimentation_and_decisionmaking_in_business_growth | experimentation]] [00:45:17]. These are often referred to as "proxy metrics" [00:55:59].
2.  **Keep it Simple:** Avoid complex composite metrics with coefficients that nobody truly understands [00:45:38]. Even if a simpler metric isn't "perfect," it's better if people understand it, have an intuition for it, and can discuss it across the company, as this drives real outcomes more effectively [00:46:07].
3.  **Common Currency:** It's essential to quantify how different metrics across the company relate to one another using a common currency [00:46:40]. For DoorDash, this means translating various levers (e.g., price changes, delivery time improvements, signing a new restaurant) into expected Gross Order Value (GOV) and volume [00:47:09]. This allows for data-driven tradeoffs between different teams (e.g., marketing vs. logistics) and quicker, better [[startup_strategies_for_pivoting_and_decisionmaking | decision-making]] by understanding the inventory of options and their predicted impact [00:47:37].
4.  **Focus on Edge Cases and Fail States:** While averages are important, it's crucial to examine "disaster deliveries" and other rare, negative experiences (e.g., "never delivered" orders) [00:55:31]. These rare events, though infrequent, can be extremely costly due to churn and refunds, and their impact is often missed when only focusing on averages [00:58:31]. Setting specific goals around eliminating these fail states can be very powerful [00:57:04].

> [!NOTE] Data Gaps
> Jessica Lax emphasizes the importance of considering "what data don't we have" [00:59:46]. For example, login errors might not appear in typical engagement data because affected users cannot even access the product to generate data [00:59:26]. Identifying these data gaps can reveal significant problems and opportunities that would otherwise be missed [00:59:51].

## Culture of Extreme Ownership

DoorDash cultivates a culture of extreme ownership, stemming from its founder and CEO, Tony Xu [00:34:16]. This means expecting every team member, including data scientists, to focus on solving problems and driving outcomes, regardless of their specific job description [00:41:20].

> [!EXAMPLE] Data Scientists Making Customer Calls
> When an affordability initiative didn't work as expected, data scientists on Jessica's team didn't just analyze the data; they picked up the phone and called customers to understand their motivations and experiences [00:42:16]. This qualitative research informed future decisions, demonstrating that any team member should do "what's needed to unblock us" [00:43:05].

This culture encourages going beyond traditional role boundaries, with data scientists engaging in product management or engineering work [00:43:37]. This fosters interest, growth, and contributes to team members moving into other organizations within the company, like product, operations, or finance [00:43:57].

## Global Data Organization
Managing a global data organization introduces complexities such as different currencies, languages, and regulations (e.g., EU vs. non-EU countries) [01:00:51]. However, Lax is often surprised by the similarities in data problems and user behavior across different regions [01:00:42]. This allows for applying learned solutions from one region to another, though testing is still crucial for cultural or other differences [01:01:33].

## [[AI in product management | AI in Data]] and [[Using AI tools for product management and development | Product Development]]

Lax is enthusiastic about [[creating_aipowered_product_teams | using AI to enhance team productivity]]. DoorDash has "office hours" where the analytics team provides support and training to non-technical users [01:03:12]. AI tools, like a chatbot, can empower these users to edit queries or adjust analyses independently, freeing up the analytics team's bandwidth [01:04:02]. DoorDash's internal AI chatbot is named "Ask Data AI," derived from their internal Slack channel, reflecting a preference for clear, direct naming conventions [01:04:52]. This represents an [[integration_of_ai_in_business_and_product_development | integration of AI]] to improve efficiency and self-service capabilities.