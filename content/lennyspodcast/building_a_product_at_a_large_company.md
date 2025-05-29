---
title: Building a product at a large company
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Jeff Weinstein, a product leader with over six years of experience at Stripe, including scaling [[building_and_evolving_a_software_product | Stripe's payment infrastructure]] and taking on [[developing_and_launching_new_products_in_a_company | Stripe Atlas]], offers profound insights into [[product_management_in_tech_companies | product management]] and [[building_a_productoriented_engineering_team | product development]] within a large organization [01:00:00]. His approach emphasizes relentless customer obsession, strategic metric selection, and fostering a culture of empathy and action.

## Core Philosophy: Go-Go-Go + Long-Term Compounding

Weinstein describes his philosophy as "go-go-go plus optimism, long-term compounding approach" [02:01:03]. This involves injecting energy to achieve immediate results while simultaneously building foundational elements that [[building_and_evolving_a_software_product | compound over time]] [00:10:47].

For instance, at Stripe, initially, adding new countries and payment methods was slow, despite significant effort [00:13:52]. The "go-go-go" attitude alone wasn't working [00:14:13]. The team had to step back and envision the future, building internal platforms and sending people globally to establish payment methods, a slower but ultimately more scalable approach that led to supporting over 100 payment methods [00:14:31]. This required [[balancing_startup_and_large_company_operations | balancing the immediate desire for results with a long-term strategic mindset]] [00:12:00].

## Customer Obsession and User Research

Weinstein believes that product managers are responsible for achieving product-market fit, which is evident through metrics showing growth and positive customer feedback [00:46:00]. His past failures stemmed from building products people didn't desperately need, leading to a profound focus on identifying "burning problems" [00:18:09].

### Listening to Customers

He emphasizes the direct engagement with customers, breaking the traditional wall between product teams and users [00:24:26]:
*   **Direct Engagement**: He actively shares his email and is text-message friendly with a small number of key customers to get "direct signal" [00:27:01].
*   **Speed**: Responding quickly to customer feedback, even a brief acknowledgment, is crucial because their decision to reach out is an "unbelievable gift" [00:30:25].
*   **Silence Technique**: During customer conversations, he refrains from pitching the product and instead asks open-ended questions like "What would you be working on if you weren't talking to me right now?" or "What grinded your gears last week?" [00:22:31]. This "sitting in silence" allows customers to reveal their most pressing problems, which can directly inform the product roadmap [00:22:04].
*   **Filtering Feedback**: To avoid being overwhelmed, he prioritizes feedback from paying customers over friends or casual users [00:38:56]. He created a rule to "discount all of that feedback from our friends to zero" [00:38:59].
*   **The "Paying" Forcing Function**: He encourages customers to practice paying for solutions, even a small amount, to gauge their true need and willingness to exchange value [00:44:20]. This helps reveal the core value proposition [00:40:06].

### Craft and Quality

While prioritizing a burning problem, Weinstein acknowledges the importance of product craft and quality. However, he sees craft as "a dessert that you get after the meal of does your thing solve a real problem in the world" [00:19:03]. No amount of beauty or delight can compensate for a product that doesn't address a fundamental need [00:19:50].

## Metrics for Success

Choosing the right metrics is vital for guiding product development and ensuring alignment within a large company [00:48:50].

*   **Customer-Centric Metrics**: Metrics should be a numerical representation of the value provided to the customer, measured from their perspective, not internal operations [00:46:50].
*   **"Companies with Zero Support Tickets" (Stripe Atlas)**: For [[developing_and_launching_new_products_in_a_company | Stripe Atlas]], the key metric became the percentage of companies that completed the incorporation process with *zero* support tickets [00:50:56]. This directly reflected customer satisfaction and correlated with market share growth, increasing from 15% to 85% over 18 months [00:51:21]. This metric was chosen because it spoke directly to what the customer wanted [00:52:07].
*   **"Users Having a Bad Day"**: A highly exportable metric is to track "users having a bad day" [01:01:05]. This involves emitting a log line anytime a user encounters a problem (e.g., 404 error, delayed payout). A bar chart of "bad day reasons" helps identify and prioritize issues [01:01:38].
*   **Metric Hygiene and Discoverability**: Giving metrics clear, customer-focused titles (e.g., "companies with zero support tickets") makes them more motivating and understandable [01:05:51]. Consistent formatting and accessible dashboards (`go/metrics` at Stripe) encourage daily team engagement and trust in the data [01:07:07].

## Study Groups

To systematically embed user empathy and focus on craft across Stripe, Weinstein initiated "study groups" [01:08:08].

*   **Structure**: Small, random groups (4-8 people) from different parts of the company (not necessarily product or engineering) choose a scenario where they "pretend to be some company with some outcome problem" [01:17:10].
*   **Rules**:
    1.  **"You do no longer work at Stripe"**: Participants must fully embody the customer, without using any internal Stripe knowledge or lingo [01:17:46].
    2.  **"We're not here to solve any problems"**: The focus is purely on experiencing the product from the customer's perspective and practicing empathy, not on critiquing or filing bugs in the moment [01:19:36].
*   **Impact**: These groups have been "deeply eye-opening" [01:20:12], fostering a deeper understanding of user struggles and creating a "cultural piece of information that is very high signal" [01:33:41]. Seeing teammates struggle motivates action more than external customer complaints [01:32:51]. This helps [[building_a_strong_company_culture_in_a_fastgrowing_company | build a strong company culture]] around customer focus.

## Getting Things Done in a Large Company

Weinstein emphasizes that [[innovating_within_large_organizations | succeeding in a large company]] requires a clear vision and practical execution, cutting through bureaucracy [02:03:44].

*   **Customer-Driven Ideas**: Frame initiatives around "deep customer stories" so they aren't just "your idea" [02:04:10].
*   **Visual Storyboarding**: Sketch "unconstrained perfect solutions" using simple tools like a Sharpie, not complex design software [02:05:01]. This quickly communicates the vision.
*   **Proof of Existence**: Demonstrate "tangible forward progress" by getting "one thing working one time" [02:06:17]. This "proof by existence" is more powerful than theory or debate [02:06:32].
*   **Momentum and Trust**: Small wins and continuous momentum build trust, allowing teams to take on bigger bets with less need for "permission" [02:07:05].
*   **Economic Viability**: Clearly articulate the economic case for a product (e.g., customer acquisition, margin generation) alongside product quality [02:09:24].
*   **Team Diversity**: Building a team with diverse perspectives (e.g., majority women on the Atlas team) is crucial for effective product development and decision-making [01:56:07]. This is an "up funnel problem," requiring intentionality in hiring pools from the start [01:57:17].

## Stripe Atlas: A Case Study in Unlocking Entrepreneurship

[[developing_and_launching_new_products_in_a_company | Stripe Atlas]] is a product that embodies many of these principles, aiming to dramatically lower the barriers to starting a company [01:39:50].

### Origin and Mission
Stripe Atlas was born from the observation that entrepreneurs globally had to fly to the US to establish a US company to access the financial system [01:38:00]. This "burning problem" led to Atlas's mission: to simplify the process of starting a company in a few clicks, driven by the belief that "there should be more startups" [01:39:23].

### Key Features and Automation
Atlas has progressively automated complex administrative tasks. A significant recent achievement is the automation of the 83b election, a Byzantine IRS rule requiring snail mail submission within 30 days, which Atlas now handles with "a single click" [01:42:01]. This automation extends to incorporation documents, EIN acquisition, and share purchases, tasks that previously took weeks or months [01:25:00]. The [[building_and_evolving_a_software_product | Atlas team]] (only 10 people) focuses solely on work that can be automated, leveraging third-party vendors for tasks like physical mail and phone calls, while building robust software to monitor their external operations [01:50:54].

### Impact and Future
Atlas has significantly impacted entrepreneurship:
*   As of the podcast launch, one in six new Delaware Corporations are started on Stripe Atlas [01:32:00].
*   Companies started through Atlas are generating $5 billion a year in revenue [01:50:11].
*   The "earliest cohort charts of new startups" are growing faster, with 2024 cohorts reaching $50 million in revenue twice as quickly as 2023 cohorts [01:49:33].
*   More solo founders are using Atlas, indicating that the ease of use enables a broader range of entrepreneurs [01:48:25].
*   The product's success has reset expectations for other tools, driving demand for simplified banking and compliance solutions [01:50:16].

### Collaboration Over Competition
Stripe Atlas's journey also highlights the value of collaboration. When AngelList launched a competing incorporation service, Stripe chose to maintain an "open relationship," sharing insights and even collaborating on legal constructs [02:12:47]. Ultimately, AngelList decided to exit the space and directed its users to Atlas, illustrating that "they're not competitors, it's alternatives" when the focus is on serving the customer and the broader mission [02:14:15]. This approach has led to seamless integrations with partners like Mercury and Carta [02:13:58].

Ultimately, Jeff Weinstein’s approach emphasizes that [[creative_approaches_to_building_beloved_b2b_products | building beloved products]], even in a large organization, stems from a deep, continuous, and empathetic understanding of the customer's burning problems, coupled with strategic execution and a focus on long-term impact [02:00:56].