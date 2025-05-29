---
title: Building products at Stripe
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Jeff Weinstein, a prominent product leader, spent over six years at Stripe, where he scaled Stripe Payments to hundreds of billions of dollars in annual volume and led various [[Building 0 to 1 products within a company | 0 to 1 bets]], including [[building_new_products_within_larger_companies | Stripe Atlas]] <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a> <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a> <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>. His approach to product development emphasizes optimism, rapid action, and long-term compounding, underpinned by a profound customer obsession <a class="yt-timestamp" data-t="02:01:02">[02:01:02]</a>.

## Core Product Philosophy: Go-Go-Go and Long-Term Compounding

Weinstein's product philosophy is characterized by a "go-go-go plus optimism, long-term compounding approach" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. He believes in injecting energy to act quickly and optimistically, often pushing for immediate results <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This drive is balanced with a strategic, long-term mindset that recognizes some problems require foundational layers of infrastructure, services, applications, UI, and partnerships <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The goal is to invest in capabilities that will "never regret spending time in," such as improving API latency or reliability <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The challenge lies in mixing this rapid execution with long-term strategic investments <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

An example of this philosophy in action is Stripe's global expansion, which initially saw flat growth in country and payment method additions despite significant effort <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The team had to step back and ask what the world would look like in 10 years, which meant slowing down to build internal platforms and sending people globally to establish new payment methods <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This strategic shift, after an initial "Flatline," led to a non-linear acceleration, increasing supported payment methods from 10 to over 100 <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## Customer Obsession: Listening and Engaging

Weinstein emphasizes that true product success comes from solving a real, burning problem for customers, one that they desperately need to be solved <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. He stresses the importance of engaging directly with customers rather than relying solely on user research departments <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Direct Engagement Tactics

*   **Breaking the Wall**: Actively sharing contact information (email, Twitter) to encourage direct customer feedback <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Rapid Response**: Prioritizing customer messages as "P0 alert level intensity" and responding immediately, even if just to acknowledge receipt <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This builds trust and turns detractors into promoters <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Silence**: In customer conversations, avoid pitching the product. Instead, sit in silence and prompt customers with open-ended questions like, "What would you be working on if you weren't talking to me right now?" or "What grinds your gears?" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This allows customers to reveal their most pressing problems, which can directly inform the product roadmap <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Text Messaging**: Being "text message friendly" with a small group of ambitious, technical, and fast-growing customers provides highly direct and infectious signals <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Bounded Programs**: Creating temporary programs, like "bugfinder," to gather structured feedback (e.g., videos) from specific customer segments within a defined timeframe <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Prioritizing Feedback

Weinstein has a strict rule: **only pay attention to feedback from paying customers** <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. He discounts feedback from friends or non-target users to zero, as they don't represent the true target customer who is willing to exchange money for a solution to their problem <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

He encourages founders to "practice paying" or "practice charging" to solidify their understanding of the transaction's value <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. For large companies, he advises a similar approach, suggesting, "If we're super serious about this, send us a million dollars" to gauge true commitment, as "ready to pay" is significantly different from "paying" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## Metrics and Quality

Metrics, for Weinstein, are the numerical representation of the value a product provides to the customer <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. They serve to measure product-market fit, force tradeoffs, and align teams <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Key Metrics and Their Implementation

*   **Companies with Zero Support Tickets**: For [[building_new_products_within_larger_companies | Stripe Atlas]], the core metric was the percentage of companies that completed the entire incorporation process (from application to two weeks post-launch) without submitting a single support ticket <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This metric directly correlated with market share, increasing from 15% to 85% in 18 months <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This approach allowed engineers to directly address customer pain points found in support tickets <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Users Having a Bad Day**: A universal metric that tracks any instance where a user encounters a problem (e.g., 404 error, delayed payout, multiple payment declines) <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. By categorizing and counting these "bad day" events, teams can prioritize and "burn down" the most frequent issues, providing a "background noise counting system" for problems <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Cohort Metrics**: Focusing on specific cohorts (e.g., customers who started last month) and tracking metrics like time-to-resolution (e.g., risk review time) <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. These metrics often aim for "up and to the left" charts, indicating faster completion or higher success rates <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Metric Hygiene and Culture

*   **Meaningful Titles**: Naming metrics clearly and concisely (e.g., "companies with zero support tickets") helps build a shared understanding and creates internal currency <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Dashboard Discoverability**: Centralizing metrics in an easily accessible system (like Stripe's `go/metrics`) ensures everyone looks at the same, trusted information <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This consistent access drives adoption and trust within teams <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Trust and Focus**: By investing attention in a small number of critical metrics, teams are forced to focus on what truly matters to the customer and the business <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## [[Stripes approach to product development and cocreation | Stripe's Approach to Product Development and Co-creation]]: Study Groups

To foster an obsession with craft, user experience, and quality, Weinstein initiated "study groups" at Stripe <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. These are random groups of 4-8 employees from any department (e.g., support, sales, engineering) who sign up voluntarily <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Study Group Rules and Impact

1.  **"You Do Not Work at Stripe"**: Participants pretend to be a fictional company with a specific problem to solve using Stripe's products (e.g., "dolphin aquarium Industries" wanting to sell in-person tickets) <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Strict adherence to this rule means no internal Stripe knowledge is used, forcing participants to experience the product from an external customer's perspective <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
2.  **"We're Not Here to Solve Any Problems"**: The primary goal is empathy and understanding the customer's journey, not immediate critique or bug filing <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Observations are recorded for later action <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

These sessions, typically 1-1.5 hours long, encourage team members to "embody the customer" and provide deeply eye-opening experiences <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Over 250 people have participated, leading to widespread internal adoption and even a "franchised" model where different teams run their own study groups <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The findings from study groups are funneled into existing formal bug processes, though the direct experience often motivates teams to act on issues without needing a mandate <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## Building [[building_new_products_within_larger_companies | Stripe Atlas]]: A Case Study in Automation and Impact

Stripe Atlas is a service that allows entrepreneurs to start a company with "a few clicks" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Its mission is to dramatically lower the barrier for great people worldwide to solve problems, especially those who previously needed to fly to the U.S. to form a company and access the U.S. financial system <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Radical Simplification and Automation

Atlas focuses on automating administrative complexities that typically hinder new businesses <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. A significant recent development is the "single-click" incorporation, which handles legal documents, EIN (tax ID) acquisition, share purchases, and 83b elections automatically <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The 83b election, a complex IRS process requiring snail mail and a strict 30-day deadline, was a major pain point that Atlas now fully automates, eliminating a significant source of founder anxiety <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

This automation is achieved by deeply integrating with governments and banking partners, allowing Atlas to provide access to the financial system even before official government approvals <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The Atlas team (10 people) focuses exclusively on work that can be automated, aiming to be the "only" solution rather than just the "best" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. They strategically work with third-party vendors for tasks like printing and mailing, forcing them to build robust software interfaces and monitoring for external processes <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Impact and Vision

*   **Market Share**: As of the podcast's launch, one in six new Delaware Corporations are started on [[building_new_products_within_larger_companies | Stripe Atlas]] <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Customer Satisfaction**: Atlas boasts an NPS (Net Promoter Score) above 80, with nearly 50% response rates, surpassing even products like Apple AirPods <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Acceleration of Business**: Companies using the automated Atlas process start charging customers sooner, cutting weeks off their time to first revenue <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. The cohort of 2024 startups on Atlas reached $50 million in revenue twice as quickly as the 2023 cohort <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Growth in Solo Founders**: The automation work has led to an increase in solo founders using Atlas, reflecting the broader trend of individuals leveraging no-code tools and the internet to build businesses <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Global Impact**: Over 55,000 companies have started through Atlas to date, generating $5 billion in annual revenue <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Roughly 20% of users state they would not have started their business without Atlas <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. A surprising statistic is that over 20% of multi-founder teams on Atlas have at least one founder from a different country ("cross-border founders") <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

The vision for Atlas is to continue automating more and more of the administrative overhead of running a company, treating it like cloud services (e.g., AWS EC2 or S3) that eliminate the need for in-house IT infrastructure <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Competition and Collaboration

Stripe's approach to competition, exemplified by Atlas's relationship with AngelList, prioritizes the customer and the mission over strict competitive rivalry <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. Despite initial concerns when AngelList launched a similar incorporation service, Stripe continued to focus on its long-term compounding strategy and building the most efficient solution <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This focus, combined with an open working relationship (sharing legal constructs, discussing issues like Delaware delays), led AngelList to eventually redirect its users to Atlas <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This collaboration now allows seamless information transfer between the platforms, benefiting the founders <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## [[building_new_products_within_larger_companies | Building New Products Within Larger Companies]]

Jeff Weinstein's experience in [[building_new_products_within_larger_companies | building new products within larger companies]] like Stripe offers several key lessons:

*   **"Not Your Idea"**: Frame initiatives as solutions to deep customer problems, supported by direct customer stories and quantitative data. This makes it less about a single person's idea and more about addressing a clear need <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Storyboard the Ideal Solution**: Visually articulate the "unconstrained perfect solution" to a burning problem using simple tools like a Sharpie and stick figures <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Show Tangible Forward Progress**: Focus on achieving small, quick wins ("proof of existence") to build momentum and trust. For Atlas, this was as simple as a single piece of paper being sent in the mail <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Economic Viability**: Clearly communicate the business case for new products, whether it's customer acquisition, margin generation, or ecosystem growth, and ensure metrics reflect this value <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Trust and Metrics**: When teams can easily track success through transparent metrics, it reduces the need for constant internal updates and builds confidence in the product's impact <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Customer Co-Design**: Actively involve customers in the design process, inviting them to directly draw or map out what they envision for new features or dashboards <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This gives customers "write access" to the company and provides highly relevant insights <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **Diversity in Teams**: Intentionally build diverse teams, as varied perspectives significantly enhance problem-solving and product development <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This is an "up funnel problem," requiring focus on the candidate pool from the start <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

### Lessons from Stripe Founders

*   **Patrick Collison**: Entrusted new hires with significant responsibility early on, even tasks like writing quarterly business reviews, to force deep understanding and encourage personal perspective <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.
*   **John Collison**: Provided "gut punch" feedback that focused on prioritization: "You are one of the best people I've ever worked with at solving problems three through 100, but I need you stuck on problems one and two" <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>. This forced Weinstein to prioritize the hardest, most impactful problems.