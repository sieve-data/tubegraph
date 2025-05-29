---
title: Stripes product development strategy
videoId: F0_IKKY3HCk
---

From: [[lennyspodcast]] <br/> 

Stripe's core thesis is that the internet economy will become significantly larger and more important in the future [0:05:50]. This belief drives the company to build economic infrastructure for the internet and beyond [0:07:58]. Stripe operates as a business full of [[developing_a_product_strategy | product-minded]] builders aiming to simplify the process for businesses to start and operate online [0:06:03].

## Core Product Development Philosophy

Stripe's approach to product development is deeply rooted in understanding and collaborating with its users [0:18:27]. This involves:
*   **Co-creation with Early Users** Identifying a select group of early users to co-create products [0:03:00, 0:18:31]. A prime example is Stripe Billing, where the team worked closely with existing users like [[figmas_product_development_philosophy | Figma]] and Slack, who already had subscription business models [0:18:49]. They shared Slack channels, showed product regularly, and gathered feedback [0:19:27]. The product was only considered ready for a broader audience once this initial "alpha group" was extremely satisfied [0:19:37].
*   **User-Centric Approach** Placing users at the center of determining what to build [0:23:28]. Stripe aims to develop deep personal relationships with users to guide all aspects of its product development [0:23:38].
*   **Product-Minded Engineers** Cultivating a culture where every engineer building product at Stripe possesses and exercises many attributes typically found in product managers at other companies [0:00:50, 0:19:43]. This enabled Stripe to operate for many years without a dedicated product manager, as its initial product was very developer-focused, and the best product managers for such products are often technical, even former engineers [0:17:50, 0:18:01].
*   **Cross-Functional Collaboration** Building products is a "team sport" across various functions [0:20:05]. This includes engineers, engineering managers, product managers, and designers [0:20:10], but also extends to financial partnerships, legal, risk, and compliance teams, whose creative thinking is crucial for building the right solutions [0:20:36, 0:20:49]. Product managers often synthesize user learnings and provide [[developing_a_product_strategy | product strategy]] [0:21:15, 0:21:31].

## [[operational_principles_at_stripe | Operating Principles]] and Practices

Stripe's [[operational_principles_at_stripe | operating principles]] are formalized behaviors distilled from the most effective "Stripes" [0:23:04]. They are consistently referenced internally for feedback, recognition, and guiding decision-making [0:23:14].

### Being Meticulous in Craft

The principle of "be meticulous in your craft" means sweating the details, especially in moments critical to the user experience [0:24:13, 0:25:31].
*   **Context-Sensitive Error Messages**: An early example of this meticulousness was linking API error messages directly to the relevant documentation, allowing developers to quickly resolve issues [0:25:02]. This detail, though uncommon, is highly valued by users [0:27:33].
*   **Iterative Design**: Stripe's hosted payment surfaces (e.g., Payment Element, Stripe Checkout) have undergone years of meticulous tuning to remove latency and unnecessary clicks [0:28:22, 0:28:39]. These continuous, small improvements have compounded to significantly increase user revenue by an average of 10.5% [0:28:47, 0:29:07].

### Friction Logging

A widely used process across product teams, and even internally, is "friction logging" [0:25:54].
*   **Process**: Teams, often led by a product manager or engineering manager, regularly immerse themselves in a specific user's shoes (e.g., an engineer integrating Stripe's API) [0:26:01, 0:33:12]. They go through the product's end-to-end flow, from dashboard to coding, and meticulously log every point of friction encountered [0:26:35, 0:26:47]. The template for a friction log encourages stating the goal, defining the user persona, and maintaining a stream-of-consciousness record of the experience, highlighting both friction points and positive aspects [0:34:24, 0:34:41].
*   **Purpose**: These logs pinpoint areas where a "tremendous amount" of investment in detail can solve problems and improve the user experience [0:27:04]. Senior leaders and executives also engage in friction logging to ensure cohesion across parallel teams and large product areas [0:34:00, 0:34:11].
*   **Prioritization**: Findings from friction logs, along with insights from incidents (e.g., reliability issues), are prioritized on roadmaps [0:36:04, 0:36:11]. Teams are encouraged to reserve bandwidth for addressing these polish and operational tasks [0:36:40].

### UX Reviews

Stripe conducts structured UX reviews, often using friction logging techniques [0:37:21, 0:37:28].
*   **Format**: Reviews can be asynchronous (individual deep dives) or collaborative walkthroughs involving the product team and cross-functional partners like support groups and executives [0:37:34, 0:37:51]. Issues are logged during the walkthrough and then discussed to determine if they need addressing [0:38:15, 0:38:25].
*   **"Walk the Store"**: Occasionally, "walk the store" sessions are held where the entire company reviews critical product flows together during weekly "Friday Fireside" meetings [0:39:13, 0:39:24]. This fosters a shared language and understanding of the user experience and product values across the organization [0:39:50, 0:39:55].
*   **Managerial Guidance**: When presenting in UX reviews, managers encourage teams to anchor their discussions and responses to user needs and the desired user experience [0:41:48, 0:42:42].

### Engineer Occasions

To ensure managers maintain a deep understanding of their teams' work, David Singleton (Stripe's CTO) personally engages in "engineer occasions" [0:45:47, 0:46:40].
*   **Process**: This involves blocking out several days (three or four) to join a team and work on a small feature from start to finish, including deployment to production [0:46:50, 0:47:05]. During this time, a friction log is maintained to capture the experience of using developer tools, build infrastructure, code review processes, and deployment times [0:47:07, 0:47:17]. Engineers are encouraged to treat the manager's code contributions like any other for review [0:49:56].
*   **Benefits**: The write-up of this experience serves as a "memoir" for future trade-off discussions and prioritization [0:47:33, 0:47:45]. It also demonstrates empathy and understanding to the team, fostering a culture of continuous improvement in developer productivity [0:47:50, 0:51:07]. New engineering managers are advised to do an engineer occasion within their first six months, and annually thereafter, to gain valuable context [0:48:33].

## Rapid Iteration and Reliability

Stripe balances rapid iteration with a commitment to extremely high reliability, crucial for its business-critical financial services [0:53:50, 0:54:02].
*   **Automated Testing**: Stripe uses comprehensive automated test suites, replacing manual testers [0:54:24]. Every code change runs through these tests before reaching production [0:54:41].
*   **Progressive Deployment**: Changes are deployed progressively, starting with a small percentage of traffic and gradually ramping up to full exposure, allowing for early problem detection [0:55:05].
*   **Continuous Delivery**: Code changes submitted by engineers automatically deploy to production within approximately 45 minutes [0:55:20, 0:57:41]. This rapid feedback loop allows user feedback received in the morning to result in a new product version in their hands by the end of the day [0:58:13, 0:58:21].
*   **Incident Response**: Stripe has robust incident response systems to minimize damage and rapidly resolve issues [0:56:13, 0:56:33]. Critically, there's a strong emphasis on continuous learning from incidents through careful reviews to identify root causes and prevent entire classes of future issues [0:56:50, 0:56:53]. These "instant remediations" are prioritized over other roadmap work [0:56:57].
*   **Chaos Testing**: Stripe also employs "chaos testing," injecting errors to ensure systems respond without impacting users [0:57:22].

## Impact of AI on Product Development

Stripe has been using machine learning (ML) and advanced ML techniques, including Transformer technology, for years, particularly in areas like fraud detection (Radar) and catching bad actors [1:01:13, 1:01:31].
*   **Powering AI Businesses**: Stripe provides the underlying financial infrastructure for many AI startups, helping them with monetization, subscriptions, and financial operations, which is crucial given the high compute costs associated with AI [1:02:20, 1:02:44].
*   **Internal Applications**:
    *   **Documentation Q&A**: Stripe uses GPT-4 to read its extensive documentation and answer developer questions in natural language [1:03:51, 1:04:09].
    *   **Natural Language to SQL**: A new feature for Stripe Sigma allows users to ask questions in natural language, and the system automatically generates SQL queries to interrogate their Stripe data [1:04:52, 1:05:07].
    *   **Internal Efficiency**: AI is also applied internally to answer user questions faster and improve collaboration [1:05:21, 1:05:26]. Stripe built an internal UI for GPT-4 with "presets" (pre-written prompts) that can be shared across the company, enabling various job families (e.g., marketing, user support) to leverage AI [1:05:56, 1:06:35].
*   **Engineer Productivity**: Stripe has made GitHub Copilot available to its engineers after a rigorous trial [1:07:13]. It has shown to be effective in improving productivity and allowing engineers to focus on higher-level problems rather than boilerplate code [1:07:35, 1:07:41]. Copilot is particularly valuable for generating test cases, which reduces manual effort while still requiring careful reasoning about test coverage [1:08:18, 1:08:42].

## Organizational Management and Planning

Stripe's approach to management and planning emphasizes trust, delegation, and continuous learning [1:10:24, 1:10:32].
*   **Hiring and Trust**: With thousands of daily decisions made across the organization, the focus is on hiring trustworthy individuals who can operate with a high degree of autonomy [1:10:04, 1:10:21]. Reference checks are taken very seriously during hiring to gain deep insights into candidates [1:10:47]. Managers are encouraged to be generous with trust initially but also hold people accountable [1:11:32, 1:11:38].
*   **Delegation**: Leaders strive to delegate, even beyond their comfort zone, to effectively operate at scale [1:12:03, 1:12:10].
*   **Personal Time Management**: Leaders consciously manage their time to prioritize high-impact activities rather than being driven by inbox demands [1:12:27, 1:12:44]. David Singleton, for example, makes a weekly list of key achievements for the week every Sunday night [1:13:00, 1:13:10].
*   **Culture Setting**: Managers and leaders must consistently embody the company's [[operational_principles_at_stripe | values]] and desired culture, modeling behavior for the entire organization [1:13:42, 1:14:06].
*   **Planning Process**: Stripe's planning process is a "reverse W" shape: teams propose initial ideas, leaders synthesize a draft company strategy, teams refine their plans based on the draft, and then the strategy is distributed [1:17:49, 1:18:18]. This process is revisited and adjusted annually, drawing from first principles and learning from other companies like Amazon [1:15:16, 1:15:34]. Key to planning is a clear focus on the specific user segments being served, from very small startups to multinational corporations [1:17:04, 1:17:41].
*   **"Crying Octopus" Button**: A minor but impactful change in developer tools is a "crying octopus" emoji button [1:27:32, 1:27:38]. Clicking it allows engineers to quickly report "paper cuts" or minor frustrations, which the developer productivity team uses to prioritize their roadmap, leading to frictionless problem reporting [1:27:47, 1:27:54].