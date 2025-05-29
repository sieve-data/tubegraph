---
title: Building and scaling a data organization
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Building and scaling a data organization involves establishing a clear philosophy, structuring teams effectively, attracting top talent, and continuously optimizing processes and metrics. Jessica Lax, VP of Analytics and Data Science at DoorDash, shares insights from her experience in building one of Tech's largest and most respected data teams [00:00:00], [00:00:55], [00:01:59].

## The Role of Analytics

For Jessica, analytics is a business impact-driving function, not merely a service function [00:00:05], [00:05:15]. The goal is to not just answer "why," but to answer "what do we do now that we know this?" [00:00:11], [00:05:42]. This means finding opportunities, having a point of view on decisions, and proactively bringing insights, deep dives, and discussions about efficient growth and trade-offs to the table [00:05:37], [00:10:15]. Analytics teams earn their "seat at the table" by consistently bringing opportunities [00:10:41].

## Data Team Structure: Centralized vs. Embedded

Jessica advocates for a [[centralized_vs_embedded_data_team_structures | centralized data organization model]] (Center of Excellence) as superior to an embedded one, a "contrarian perspective" that DoorDash has experimented with [00:06:00], [00:06:07], [00:06:10], [00:06:17].

In a centralized model, data professionals' reporting lines go up through a central analytics organization rather than directly into specific business units like marketing [00:06:45], [00:07:01], [00:07:02], [00:07:09], [00:08:40]. However, they still share the same goals as their partner teams (e.g., marketing, product, engineering, operations), ensuring incentives are aligned [00:06:50], [00:09:01], [00:10:05].

DoorDash's approach involves a central analytics team divided into pods that map perfectly with the structure of product, engineering, operations, and marketing [00:08:22]. This allows team members to be de facto embedded with their partner teams while maintaining a central reporting structure [00:08:34], [00:08:40].

### Benefits of a Centralized Model
*   **Consistent and High Talent Bar** A centralized structure helps maintain a consistent bar for evaluating technical and soft skills during hiring, leading to higher quality talent [00:11:06], [00:11:16].
*   **Growth Opportunities** It provides more growth opportunities for individuals, as they can move between different areas of the company (e.g., from marketing to merchant analytics) if their current problems become less engaging or if they seek promotion into people management [00:11:41], [00:11:56], [00:12:05], [00:12:24]. This helps in [[startup_scaling_strategies | retaining talent]] [00:12:44].
*   **Consistency of Methodologies and Metrics** A central team ensures that definitions (e.g., "sales") and methodologies are consistent across the company, preventing duplicated effort and allowing for collective improvement of methods [00:12:48], [00:13:01], [00:13:11], [00:13:13].
*   **Scalability** Centralization helps in identifying common problems across teams, which can then be automated or improved, allowing the business and team to scale more effectively [00:13:24], [00:13:31].
*   **Strong Team Culture** It fosters a strong team culture and brand (DoorDash's analytics team is called "The A Team"), promoting learning, sharing, and peer review among like-minded "data nerds" [00:13:46], [00:13:50], [00:14:04], [00:14:51]. This is particularly important for smaller teams in early stages [00:14:21].

### Managing Proactivity and Reactive Requests
It's crucial to intentionally carve out time for exploratory work and deep dives, as reactive questions can quickly consume all available hours [00:15:50], [00:15:59]. Setting goals around finding insights through self-directed work helps maintain accountability [00:16:06]. Hackathons can be a successful mechanism for this, enabling teams to explore interesting problems and find opportunities that drive future roadmaps [00:16:49], [00:16:52], [00:17:06].

One example involved a hackathon focused on referral marketing [00:17:35]. The team's deep dive, which included trying to commit referral fraud, uncovered significant fraudulent behavior and a bimodal distribution of consumer engagement [00:18:12], [00:18:22], [00:18:49]. This led to recommendations for better fraud checks and caps on referrals, significantly improving the channel's efficiency [00:19:57], [00:20:01], [00:20:05].

To manage inbound requests, data professionals should:
*   **Establish a Culture and Operating Model** Leadership should establish clear rules of engagement to prevent junior team members from constantly having to say no [00:21:17].
*   **Align Goals** By having the same goals as business partners, it's easier to discuss limited time and prioritize the most important tasks [00:21:32], [00:21:44].
*   **Communicate Trade-offs** Always share the trade-offs involved when new requests come in. This makes stakeholders aware that doing a new task means deprioritizing something else [00:22:06], [00:22:19], [00:22:26].
*   **Ruthless Prioritization** Constantly re-evaluate priorities with business partners to ensure the team is working on the most impactful things [00:22:50], [00:22:55], [00:24:03].
*   **Build Goodwill** Occasionally, it's beneficial to quickly complete smaller, "five-minute" tasks to build goodwill [00:23:47].
*   **Prove Value of Long-Term Work** Demonstrate the value of proactive, longer-term initiatives by showcasing the opportunities found [00:24:08], [00:24:12].

## Hiring for Data Teams

Beyond technical skills, which are "table stakes," Jessica looks for unique characteristics in top talent [00:24:32], [00:24:36].

*   **Curiosity and Self-Motivation** The ability to "pull on threads" when something seems odd, to dig deeper proactively without being told, is invaluable [00:24:51], [00:25:03], [00:25:20], [00:25:34]. This can be tested by presenting cases with slight inconsistencies or by asking for examples of past self-directed investigations [00:25:44], [00:26:07].
*   **Problem-Solving and Ambiguity Tolerance** Using real-world business cases (often from DoorDash's history) helps assess how candidates break down problems and handle ambiguity [00:27:02], [00:27:16].
*   **Adaptability and Decisiveness** It's important to see how candidates react to being told they're wrong, how they incorporate new information, and their ability to make decisions with imperfect information [00:27:56], [00:28:03], [00:28:10], [00:28:30].
*   **Non-Traditional Backgrounds** Jessica herself has a non-traditional background (art, investment banking, GM) and is self-taught in SQL and Python [00:29:03], [00:29:26], [00:29:43]. This background helps her hire technical experts (e.g., PhDs in statistics, machine learning) and keep them focused on driving business impact [00:30:31], [00:30:51], [00:31:06]. A diverse mix of backgrounds, expertise, and experience from different company sizes (startups to large scale) creates a unique and effective team [01:06:03], [01:06:41], [01:07:09], [01:07:57], [01:08:04], [01:08:16].

## Picking and Aligning Metrics

Jessica highlights several key lessons about defining and utilizing metrics:
*   **Short-Term Metrics Driving Long-Term Outcomes** Find measurable short-term proxy metrics that drive desired long-term outputs [00:26:22], [00:44:51], [00:55:02], [00:55:08]. For example, retention is a difficult metric to goal on in the short term, so focus on inputs that can be quickly experimented with and proven to drive retention [00:45:02], [00:45:13], [00:45:17].
*   **Keep It Simple** Avoid complex composite metrics that nobody understands [00:45:33], [00:45:38], [00:45:50], [00:46:07]. A simpler, even if imperfect, metric that people understand and have intuition around will drive better outcomes [00:46:09], [00:46:13], [00:46:15], [00:46:20], [00:52:18], [00:52:27]. For instance, instead of a composite "Merchant Health Score," focus on direct, understandable inputs like "new merchants getting an order in seven days" or "merchant photo coverage" [00:50:56], [00:51:31], [00:51:48], [00:51:53], [00:52:02], [00:52:30].
*   **Common Currency** Quantify how different metrics and levers across the company equate to a common currency (e.g., Gross Order Value (GOV) or volume at DoorDash) [00:46:38], [00:46:40], [00:46:43], [00:46:49], [00:47:02], [00:47:14], [00:47:58], [00:48:20], [00:48:28]. This allows for better trade-off decisions between different teams (e.g., marketing vs. logistics) and quicker, better decision-making [00:47:07], [00:47:37], [00:49:48], [00:50:11].
*   **Focus on Edge Cases and Fail States** While averages are important, actively set goals and create metrics around edge cases and "disaster" scenarios, even if they are rare [00:55:29], [00:55:34], [00:55:36], [00:56:02], [00:56:09], [00:56:47]. These experiences, like "never delivered" orders, can lead to significant churn and high costs, disproportionate to their frequency [00:56:21], [00:56:27], [00:56:32], [00:56:38], [00:58:19], [00:58:31]. Such issues might also be missed in data if users cannot even access the product (e.g., login errors) [00:59:26], [00:59:41]. Quantifying the impact of these fail states on engagement and profitability can highlight their importance [00:59:11], [00:59:15].

## Culture and Extreme Ownership

A culture of extreme ownership, where team members feel personally responsible for outcomes, is critical [00:32:51], [00:36:25], [00:40:41], [00:41:20]. This starts from the top (e.g., Tony Xu, DoorDash's CEO) [00:34:16], [00:41:08]. Jessica expects her team to be problem-solvers who will do whatever is needed to achieve their goals, even if it means stepping outside traditional role boundaries [00:41:20], [00:41:27], [00:41:56], [00:43:13]. This could involve a data scientist picking up the phone to call customers for qualitative research [00:41:47], [00:42:53], [00:42:55], or even doing some product management or engineering work [00:43:37], [00:43:41]. This cross-functional experience is encouraged and allows team members to explore other career paths within the company [00:43:55], [00:44:07].

DoorDash also instills its "We Dash" program, where all employees (including analytics) go out and deliver or do customer support four times a year. This builds empathy with consumers, Dashers, and merchants, and helps identify bugs [00:38:31], [00:39:09], [00:39:31].

## Managing a Global Data Organization

While global operations introduce complexities like different currencies, languages, and regulations, Jessica is often surprised by how similar problems and people are across regions [01:01:01], [01:01:03], [01:01:06], [01:01:13], [01:01:19], [01:01:22], [01:01:31]. Having encountered similar problems in different markets, there's often an "instinct" for what the solution might be, though local differences still warrant testing [01:01:33], [01:01:51], [01:01:56]. The differences, when they arise, keep things interesting [01:02:23], [01:02:27].

## Using AI in Data Teams

AI presents opportunities to enhance productivity [01:03:01]. One exciting application is empowering non-technical users to perform data tasks themselves, reducing reliance on the analytics team [01:03:07], [01:03:12], [01:03:31]. For example, a chatbot (internally called "Ask Data AI") allows users to edit SQL queries or adjust them for different business segments, freeing up the analytics team's bandwidth [01:04:05], [01:04:40], [01:04:52].