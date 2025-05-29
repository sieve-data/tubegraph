---
title: Understanding AWS and cloud computing fundamentals
videoId: APvj15_YCqk
---

From: [[acquiredfm]] <br/> 

Amazon Web Services (AWS) is recognized as a pioneer in cloud computing and one of the most significant businesses and technologies in the modern world <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. Although its revenue is approximately 15% of Amazon's massive retail business, AWS's operating income has been equal to or greater than the e-commerce store's since 2015 <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## The Origins of AWS

The origin story of AWS is complex, with several conflicting narratives <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

### The "Excess Capacity Myth"

The most commonly believed, yet untrue, origin story posits that AWS arose from Amazon.com's need to rent out excess technical infrastructure capacity during off-peak seasons (Q1-Q3), as they had to build for the huge spikes in Q4 holiday shopping <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. This narrative suggests Amazon decided to turn a large expense line into a revenue line by renting out idle servers <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.

This story is incorrect for two main reasons:
1.  **Technical Infeasibility**: Pre-cloud technology companies did not have infrastructure that could be easily rented out. Servers were highly customized, tightly coupled to applications, and lacked the necessary security and networking for multi-tenancy <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. The [[importance_of_linux_and_open_source_for_aws_development | move to Linux]] and open source allowed for more standardized hardware, but this was about cost savings for Amazon.com, not virtualization for external use <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
2.  **Service Reliability**: If AWS customers depended on "excess capacity," their services would be disrupted during Amazon.com's peak Q4, which is illogical for critical applications <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

Werner Vogels, Amazon's CTO, explicitly debunked this [[the_excess_capacity_myth_in_aws_origin_story | excess capacity story]] in 2011, stating that AWS would have "burned through" any excess Amazon.com capacity within two months of launch <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. He affirmed that AWS was always conceived as a business expected to grow as large as Amazon.com's retail operation <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This highlights [[amazon_and_aws_business_strategy_intentions | Amazon's intentionality and strategy]] rather than accidental discovery <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

### Web 2.0 and APIs

A more accurate origin stems from Tim O'Reilly's visit to Jeff Bezos in early 2002 <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. O'Reilly pitched the idea of Amazon embracing Web 2.0, emphasizing "participatory culture" and "interoperability" through APIs <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This meant allowing other developers to access data and content from Amazon.com programmatically, similar to how Google Maps or Flickr offered APIs for "mashups" <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

Bezos embraced this vision, inviting O'Reilly to evangelize Web 2.0 and APIs within Amazon <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. A new team was formed to build APIs for the Amazon.com product catalog, with the mission to "let them surprise us with what they build" <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This division, launched in 2002, was named **Amazon Web Services** <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Initially, this AWS was focused on exposing Amazon.com's assets to affiliates, not providing [[cloud_infrastructure_and_enterprise_enablement | cloud infrastructure]] <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

### The Internal Monolith Problem and Service-Oriented Architecture

Around 2001-2002, Amazon faced significant internal [[challenges_faced_by_amazon_preaws | challenges]] due to its monolithic software codebase, inherited from its 1995 origins <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Adding new features or teams to this single codebase could "break everything," leading to code freezes (especially in Q4) and halting innovation <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

Jeff Bezos, along with his technical assistant and future AWS CEO Andy Jassy, recognized this as a critical problem <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Instead of increasing internal communication (as many companies did), Bezos made an "incredible leap" <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. He mandated that:
*   All teams must expose their data and functionality through "hardened interfaces" (APIs) <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
*   Teams must communicate *only* through these interfaces, with no direct linking, shared memory, or backdoors <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   All service interfaces must be designed to be "externalizable" to outside developers, with "no exceptions" <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
*   Anyone failing to comply would be fired <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

This "no communication" rule forced Amazon to adopt a **service-oriented architecture (SOA)**, breaking the monolith into independent, API-driven services <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. This shift aimed to allow engineers to focus on "making the beer taste better" (customer-facing features) rather than "undifferentiated heavy IT lifting" <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. The same logic was then applied to IT infrastructure, transforming it into an API-accessible "pool of computing resources" <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

### The "Dissenting Narrative"

Concurrently, a network engineer named Benjamin Black and his boss Chris Pinkham (who reported to Amazon's CIO, Rick Dalzell) were independently working on restructuring Amazon's IT architecture <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. In a six-pager, they suggested that their proposed architecture could also be used to "sell virtual compute servers as a service to third-party developers" <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

Chris Pinkham eventually moved to Cape Town, South Africa, to lead a new Amazon subsidiary and built what would become EC2 (Elastic Compute Cloud) in isolation <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. While Andy Jassy claims the full vision, including EC2, was in his 2003 proposal, Pinkham's account suggests a more decentralized, independent development <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This decentralized innovation is, ironically, a core tenet of Amazon's culture <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## Core Cloud Computing Fundamentals

AWS launched its first services in March and August 2006 <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. The core services were designed as **primitives** – basic, unopinionated building blocks for developers <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

*   **Amazon S3 (Simple Storage Service)**: Launched March 2006 <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. S3 offers internet-accessible, "cloud" storage for any data (images, files), where users "don't have to buy a server... configure a server... rack a server" <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Users pay only for what they use, at incredibly low prices <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   **Amazon EC2 (Elastic Compute Cloud)**: Launched August 2006 (beta) <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. EC2 provides virtualized compute instances (processors in the cloud) that can be spun up or down as needed, without persistent storage <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   **Amazon CloudFront**: A content delivery network (CDN) launched in 2008 <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.
*   **Amazon RDS (Relational Database Service)**: The first major database offering, launched in 2009 <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. RDS allows users to run their existing databases (e.g., PostgreSQL) in the cloud, abstracting away the underlying server management <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

The definition of "cloud" has evolved: initially it meant using primitive building blocks in Amazon's data centers, paying as you go <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. Today, it refers to using cloud services (often proprietary and at higher levels of abstraction) that can run anywhere, including on-premises, accessed via APIs <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This was inspired by General Magic, which used the term "cloud infrastructure" for its distributed, always-accessible backend <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

## Business Model and Market Impact

AWS revolutionized the IT industry with its disruptive "pay-as-you-go" pricing model <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. James Hamilton, a distinguished engineer at Amazon, noted in 2006 that provisioning storage required only a credit card, with no lengthy financial approvals or vendor negotiations, costing mere cents <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This drastically reduced the barrier to entry for developers and startups <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

This model was a game-changer for [[awss_impact_on_startups_and_enterprise_adoption | startups]], enabling companies like Dropbox, Instagram, Airbnb, Uber, and Zynga to get started rapidly without needing significant upfront capital for infrastructure <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. The ability to launch an application in 48 hours instead of spending millions and months on data centers "birthed that movement" <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Amazon actively fostered this through initiatives like the AWS Startup Challenge, which even featured Justin.tv (later Twitch) as a contestant <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

For enterprises, AWS offered several advantages:
*   **Trading CapEx for OpEx**: Shifting capital expenditure (buying servers) to operational expenditure (paying for usage) <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Lower OpEx**: Benefiting from AWS's economies of scale <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Elasticity**: Scaling infrastructure capacity up or down as needed, eliminating the need for upfront forecasting <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
*   **Focus on Core Business**: Engineers could focus on writing code and building features, not on infrastructure management <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Global Reach**: Instant access to global infrastructure <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

Major enterprises like Netflix became AWS customers in 2009, even after building their own internal cloud <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Netflix's public endorsement helped build trust, addressing concerns from other retailers about doing business with a competitor <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. AWS also secured contracts with academic institutions and government agencies like NASA, helping them develop enterprise sales capabilities <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This cemented AWS's position as a [[aws_as_a_gamechanger_in_enterprise_sales | game-changer in enterprise sales]].

## Evolution and Competition

AWS is a continuous innovator, moving beyond basic infrastructure to higher-level services. **Lambda** is a key example of "building for the cloud," where users write code that automatically executes without managing servers ("serverless") <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. They also developed custom chips (like Trainium and Inferentia) for machine learning workloads <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

AWS's dominance forced [[comparative_analysis_of_aws_and_its_competitors | competitors]] like Microsoft and Google to adapt.
*   **Oracle/IBM**: These legacy companies, with their high-margin proprietary software and licensing models, were unwilling to cannibalize their existing annuity businesses by offering pay-as-you-go cloud services <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. AWS's database offerings (like Redshift, named to "shift away from big red" Oracle <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>) significantly took market share <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
*   **Microsoft**: Initially hampered by internal power struggles (Windows group protecting server licenses) and a mistaken focus on Platform-as-a-Service (PaaS) instead of Infrastructure-as-a-Service (IaaS) <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. Microsoft later made a strong comeback with Azure under Satya Nadella, realizing the need for a separate cloud strategy and embracing IaaS <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Google**: With its highly profitable advertising business, Google initially saw cloud as less attractive and lacked enterprise sales competency <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. They also focused on a PaaS approach (Google App Engine), which was "a decade early" <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Despite having superior technology and expertise in data centers and AI, they struggled to capitalize on the market early on <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

AWS's market share is around 39%, with Azure at 21% and Google at 7% <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## Key Learnings

*   **Scale Economies**: AWS is arguably the greatest scale economy business of all time <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Its enormous fixed costs (data centers, infrastructure) are amortized across a massive customer base, allowing it to offer lower prices while maintaining strong profit margins <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. This resembles a utility company, requiring huge capital expenditures but becoming a self-fulfilling prophecy of market leadership <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **Proactive Price Cuts**: AWS proactively reduced prices even without significant competition (23 price reductions by 2012, 51 by 2015 <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>). This strategy aimed to win market share, secure future contracts, and justify massive infrastructure investments, similar to TSMC's approach <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Customer Obsession ("Make Something People Want")**: Unlike competitors who built what they thought was clever technology, Amazon focused on what startups and IT managers actually wanted – reliable, scalable, and affordable infrastructure services <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. They prioritize customer use cases before investing in development <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Asymmetric Upside**: Jeff Bezos's philosophy emphasized making bets with a 10% chance of a "hundred times payoff," understanding that "big winners pay for so many experiments" <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. AWS was a "market size unconstrained" bet, a "venture bet in their portfolio that they own 100% of" <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   **Sticky Enterprise Services**: Once customers migrate their data to a cloud provider, there are significant switching costs. Amazon.com itself took 13 years to fully migrate off Oracle databases onto AWS products <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. This stickiness means AWS rarely deprecates services, even if they have internal cost issues, to maintain customer trust <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

AWS operates on an $80 billion annual revenue run rate <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a> and holds over $100 billion in contracted, unrecognized revenue backlog <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. This represents enormous future business, highlighting its entrenched position and the continued shift of IT to the cloud.