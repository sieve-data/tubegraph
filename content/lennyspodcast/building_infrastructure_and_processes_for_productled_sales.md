---
title: Building infrastructure and processes for productled sales
videoId: bxghtN-OlJQ
---

From: [[lennyspodcast]] <br/> 

[[understanding_productled_sales_and_its_differences_from_traditional_sales | Product-led sales]] (PLS) represents a significant shift in the go-to-market strategy for businesses, particularly within B2B SaaS. It emphasizes deep [[collaborative_dynamics_between_product_and_sales_teams | collaboration between product and sales teams]] and leverages product usage data to drive sales opportunities.

## What is Product-Led Sales?

[[understanding_productled_sales_and_its_differences_from_traditional_sales | Product-led sales]] converts product usage generated via self-serve into a sales opportunity, attaching a salesperson to close much larger contracts (e.g., $15,000 to $100,000+) <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. While [[understanding_productled_sales_and_its_differences_from_traditional_sales | product-led growth]] (PLG) focuses on the product's ability to self-serve activate, engage, and monetize usage <a class="yt-timestamp" data-t="08:00:02">[08:00:02]</a>, PLG often has a cap of around $10,000 for self-serve monetization due to credit card limits and consumer willingness to spend <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>. PLS addresses this by bridging the gap to enterprise-level solutions <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.

### Collaboration is Key
The most important aspect of [[understanding_productled_sales_and_its_differences_from_traditional_sales | product-led sales]] is the internal configuration of collaboration that needs to occur <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. In traditional sales, marketing creates pipeline for sales, sales sells the product, and product engages with the paid user to drive retention <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. In PLS, product acquires and activates customers, and product creates pipeline for sales <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. This means the [[the_role_of_product_teams_in_the_sales_process | product team]] must take accountability for pipeline <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. Trying to implement PLG or PLS purely through marketing is a "recipe for disaster" <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## When to Invest in Product-Led Sales

Implementing PLS means going up-market, targeting contract values likely over a typical sales floor of around $15,000 <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a>. This implies pursuing contracts of $100,000-$200,000 or more, typically with mid-market (200+ employees) or enterprise (1000+ employees) segments <a class="yt-timestamp" data-t="21:20:00">[21:20:00]</a>.

If you are a [[understanding_productled_sales_and_its_differences_from_traditional_sales | product-led growth]] company, you are [[transitioning_to_productled_sales | transitioning to product-led sales]] to move up-market <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>. If you're a traditional sales-led growth (SLG) organization, you might adopt PLS because your existing top-down motion isn't working (customers want to see value before signing) or to go down-market more efficiently by automating the selling process <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.

## Building PLS Infrastructure

### 1. Data Requirements
Start with intuition <a class="yt-timestamp" data-t="37:41:00">[37:41:00]</a>, identifying signals that sales finds exciting from product usage <a class="yt-timestamp" data-t="37:52:00">[37:52:00]</a>. Avoid immediately sending every user to sales, as this can devalue the product channel <a class="yt-timestamp" data-t="38:22:00">[38:22:00]</a>.

Next, look at the reality of "hand-raisers" (users who organically reach out to sales) <a class="yt-timestamp" data-t="38:43:00">[38:43:00]</a>. Analyze what differentiates them from other users to create a simple Product Qualified Account (PQA) model <a class="yt-timestamp" data-t="39:03:00">[39:03:00]</a>. This can involve linear regression or histogram analysis <a class="yt-timestamp" data-t="39:05:00">[39:05:00]</a>.

The PQA definition should not be static; it continuously evolves <a class="yt-timestamp" data-t="39:51:00">[39:51:00]</a>. Regular feedback cycles with sales are crucial <a class="yt-timestamp" data-t="39:41:00">[39:41:00]</a>.

Common PQA indicators:
*   **Number of users in the company:** The magic number is often around seven or more users from the same company <a class="yt-timestamp" data-t="43:29:00">[43:29:00]</a>.
*   **Volume threshold:** E.g., number of events sent (Amplitude), number of boards (Miro), number of revisions (Figma) <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.
*   **Velocity:** A significant change in the rate of user adds, events sent, or storage utilized <a class="yt-timestamp" data-t="44:28:00">[44:28:00]</a>.
*   **Behavioral signals:** Admin switches in an account <a class="yt-timestamp" data-t="45:33:00">[45:33:00]</a>, or users landing on "terms of use" or "privacy policy" pages, which indicate an evaluation process <a class="yt-timestamp" data-t="45:57:00">[45:57:00]</a>.

#### PQA vs. PQL vs. MQL
*   **Product Qualified Account (PQA):** An aggregation of multiple users from the same company or workspace using the product <a class="yt-timestamp" data-t="29:04:00">[29:04:00]</a>. It's based on product metrics like usage volume, velocity, or feature breadth <a class="yt-timestamp" data-t="29:29:00">[29:29:00]</a>.
*   **Product Qualified Lead (PQL):** A specific person within a PQA who is a potential buyer <a class="yt-timestamp" data-t="30:03:00">[30:03:00]</a>.
*   **Marketing Qualified Lead (MQL):** A lead qualified by marketing <a class="yt-timestamp" data-t="31:21:00">[31:21:00]</a>. In PLS, an MQL might be a buyer found externally by marketing, who is then connected to an existing PQA <a class="yt-timestamp" data-t="31:35:00">[31:35:00]</a>. There can also be traditional top-down leads with no prior product usage <a class="yt-timestamp" data-t="32:08:00">[32:08:00]</a>.

### 2. Tooling & Systems
Approach tooling as an evolution, not a revolution <a class="yt-timestamp" data-t="49:23:00">[49:23:00]</a>. Embed data into existing sales systems (e.g., Salesforce) rather than forcing sales to switch tools <a class="yt-timestamp" data-t="49:30:00">[49:30:00]</a>. Prove out the viability of PLS motion before making big automation commitments <a class="yt-timestamp" data-t="49:51:00">[49:51:00]</a>.

Initial tools can include:
*   Google Sheets <a class="yt-timestamp" data-t="50:17:00">[50:17:00]</a>
*   BI tools (Looker, Tableau) <a class="yt-timestamp" data-t="50:19:00">[50:19:00]</a>
*   Product analytics platforms (Amplitude, Mixpanel) <a class="yt-timestamp" data-t="50:21:00">[50:21:00]</a>
*   CRM widgets (Salesforce) or ETLs into marketing automation (HubSpot, Marketo) <a class="yt-timestamp" data-t="50:24:00">[50:24:00]</a>

The goal is to achieve "data-sales fit" before scaling with dedicated PLS platforms <a class="yt-timestamp" data-t="41:26:00">[41:26:00]</a>.

### 3. People & Resources
The core team for PLS includes:
*   [[the_role_of_product_teams_in_the_sales_process | Product managers]] to get accounts to the PQA stage <a class="yt-timestamp" data-t="51:11:00">[51:11:00]</a>.
*   Salespeople who understand which usage triggers PQAs and how to leverage that information to find and enable a buyer <a class="yt-timestamp" data-t="51:23:00">[51:23:00]</a>.
*   Marketing to educate end-users and enterprise buyers on the value proposition <a class="yt-timestamp" data-t="51:36:00">[51:36:00]</a>.
*   Data analysts to continuously find correlative signals in the data <a class="yt-timestamp" data-t="51:46:00">[51:46:00]</a>.
*   Engineering (bundled with product) <a class="yt-timestamp" data-t="52:01:00">[52:01:00]</a>.

Start with a pilot:
*   **For SLG companies:** Partner with an Account Executive (AE) or Sales Development Representative (SDR) to run a pilot, keeping it separate from the main sales engine initially <a class="yt-timestamp" data-t="52:11:00">[52:11:00]</a>.
*   **For PLG companies:** Consider [[founderled_sales_strategies | founder-led sales]] or have support/finance teams handle early deals to understand the [[sales_cycle_steps_and_processes | sales process]] <a class="yt-timestamp" data-t="52:46:00">[52:46:00]</a>. Start with a blend of SDR/AE roles rather than immediate specialization <a class="yt-timestamp" data-t="53:18:00">[53:18:00]</a>.

## Key Performance Indicators and Benchmarks

### Product Team Goals
*   **Self-Serve Revenue:** Product leadership should be accountable for self-serve revenue targets, while individual product managers are responsible for KPIs like:
    *   Free-to-paid conversion rates (typically around 5% for freemium, 10-15% for trials) <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>
    *   Trial-to-paid conversion rates <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>
    *   Package mix <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>
    *   Average revenue per user (ARPU) <a class="yt-timestamp" data-t="01:00:28">[01:00:28]</a>
    *   Retention rates <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>
*   **Product-Led Sales (PLS) Pipeline:** [[the_role_of_product_teams_in_the_sales_process | Product teams]] should own PQA targets <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>. This is typically measured as a conversion rate: "how many teams in my Ideal Customer Profile (ICP) segment are active, and how many of those are reaching PQA target this month?" <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.

### Monetization Awareness
A critical but often overlooked metric is monetization awareness <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>. Up to 75% of freemium users may not be aware of what paid plans offer <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>. Track this qualitatively (surveys) <a class="yt-timestamp" data-t="01:04:48">[01:04:48]</a> and quantitatively (pricing page views per activated account) <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>. Ensure paid functionality is visible and understood in the free product state <a class="yt-timestamp" data-t="01:05:48">[01:05:48]</a>.

### Time to Contract
It takes time for individual usage to escalate to an enterprise contract. Benchmarks show it can be 12 months or more of usage before a sustainable sales contract can be created <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>.

## [[common_pitfalls_and_best_practices_in_implementing_productled_sales_strategies | Common Pitfalls]]

1.  **Treating PLS like traditional top-down sales:** Not every user is a sales opportunity. Understand specific triggers and usage patterns for automation and timing <a class="yt-timestamp" data-t="01:06:45">[01:06:45]</a>. Sales interactions must add value, not disrupt <a class="yt-timestamp" data-t="01:07:13">[01:07:13]</a>.
2.  **Not holding product accountable:** PLS cannot be solely executed by marketing and sales. [[the_role_of_product_teams_in_the_sales_process | Product must have a seat at the table]] and be accountable for pipeline <a class="yt-timestamp" data-t="01:07:45">[01:07:45]</a>. Foster new rituals and communication channels between product and sales <a class="yt-timestamp" data-t="01:08:09">[01:08:09]</a>.
3.  **Leaving marketing out:** Most usage won't have an immediate buyer. Enterprise marketing and Account-Based Marketing (ABM) are crucial to find and connect buyers with product usage <a class="yt-timestamp" data-t="01:08:17">[01:08:17]</a>.
4.  **Delaying data efficacy:** Don't wait too long to scale data infrastructure. PLS relies on leveraging usage for pipeline, requiring robust measurement, tracking, and evolution of data <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.
5.  **Not profiling users:** Skipping onboarding questions leads to a lack of understanding of users (buyers vs. non-buyers, ICP fit) <a class="yt-timestamp" data-t="01:10:38">[01:10:38]</a>. Profile users for company size, department, seniority, and use case <a class="yt-timestamp" data-t="01:12:38">[01:12:38]</a>.

## The Future of Growth: AI Sales?

With the rise of AI, it's possible that AI could automate complex sales conversations, offering deep, personalized answers faster than humans <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>. This could lead to an "AI Sales" model, where the product isn't strictly selling itself, but AI is facilitating the sales process <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.