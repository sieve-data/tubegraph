---
title: Amazon Web Services AWS history and origin stories
videoId: APvj15_YCqk
---

From: [[acquiredfm]] <br/> 

Amazon Web Services (AWS) is described as "one of the biggest and most important businesses, technologies, [and] products" in the modern world, perhaps even more so than [[amazons_early_history_and_founding | Amazon's retail business]] <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. While AWS revenue is approximately 15% of [[amazons_early_history_and_founding | Amazon's retail business]], its operating income has been equal to or greater than the e-commerce store every year since 2015, when AWS financials began to be broken out <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This article explores the various origin stories of AWS.

## The "Excess Capacity" Myth

One widely believed but untrue origin story for AWS is the "excess capacity narrative" <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This myth suggests that the retail business, being highly seasonal with huge demand spikes in Q4, built out technical infrastructure for peak demand, leaving excess capacity during other quarters that Amazon decided to rent out to other developers <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. The idea was to turn a large expense into a revenue stream <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

However, this story is disproven by practicalities of pre-cloud technology and logical business needs:
*   **Technical incompatibility:** Pre-cloud technology companies had highly customized servers tightly coupled to their applications, making it impossible to easily rent out capacity to others due to security and network hardware limitations <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Early Amazon servers were monolithic DEC Alpha servers, making 80% gross margins for the manufacturer <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. The shift to [[the_role_of_linux_in_amazons_infrastructure_evolution | Linux]] and open-source systems, like HP servers, did save Amazon money but did not create virtualized cloud servers <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Customer service during peak times:** AWS could not serve customers like Netflix by simply taking back their infrastructure during Amazon's peak Q4 needs <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Official denial:** Werner Vogels, the CTO of AWS and later of all Amazon, stated in a 2011 Quora post that "the excess capacity story is a myth. It was never a matter of selling excess capacity. Actually, within two months after launch AWS would have already burned through the excess amazon.com capacity" <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>. He affirmed that [[awss_business_model_and_financial_impact | AWS was always considered a business by itself]], with the expectation that it could grow as big as the Amazon.com retail operation <a class="yt-timestamp" data-t="01:19:32">[01:19:32]</a>.

This myth underestimates Amazon's intentionality and strategy, as technology was always viewed as an investment rather than a cost center <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>.

## The Web 2.0 and API Vision

The true origins of AWS are deeply tied to the evolution of web technology and internal challenges at Amazon.

### Inspiration from Tim O'Reilly and Web 2.0
In early 2002, Tim O'Reilly, a prominent figure in programming and technology, met with [[bezos_and_the_foundation_of_amazon | Jeff Bezos]] in Seattle <a class="yt-timestamp" data-t="02:05:04">[02:05:04]</a>. O'Reilly championed the concept of Web 2.0, emphasizing "participatory culture" and "interoperability" through Application Programming Interfaces (APIs) <a class="yt-timestamp" data-t="02:22:06">[02:22:06]</a>. This vision proposed that businesses could interact programmatically via APIs without complex business development agreements, enabling transactions with thousands of companies instead of just a few cherry-picked ones <a class="yt-timestamp" data-t="02:39:05">[02:39:05]</a>.

Bezos immediately grasped this idea, particularly for Amazon's giant affiliate program, Amazon Associates <a class="yt-timestamp" data-t="02:33:37">[02:33:37]</a>. An API would allow affiliates to access Amazon's product catalog and display information, sharing revenue seamlessly <a class="yt-timestamp" data-t="02:48:49">[02:48:49]</a>.

Following this meeting, Bezos:
1.  **Embraced Web 2.0:** He invited O'Reilly to speak at Amazon's all-hands meetings to evangelize Web 2.0 and API concepts <a class="yt-timestamp" data-t="02:47:11">[02:47:11]</a>.
2.  **Formed a New Team:** He created a team to build APIs for Amazon.com's product catalog, with the goal to "let them surprise us with what they build" <a class="yt-timestamp" data-t="02:47:24">[02:47:24]</a>.
3.  **Launched "Amazon Web Services":** In 2002, Amazon held a conference for developers to announce this new division called Amazon Web Services <a class="yt-timestamp" data-t="02:56:05">[02:56:05]</a>. Only eight people attended <a class="yt-timestamp" data-t="02:58:01">[02:58:01]</a>. At this stage, AWS was focused on exposing Amazon.com's assets to affiliates and lived within the Amazon Associates program, led by Colin Bryar <a class="yt-timestamp" data-t="02:59:02">[02:59:02]</a>.

This initial iteration of AWS was not cloud-based IT infrastructure but rather about democratizing access to Amazon.com's data via APIs <a class="yt-timestamp" data-t="02:28:30">[02:28:30]</a>. The term "cloud" in IT infrastructure actually originated at General Magic, an Apple spin-out that developed a "distributed always accessible back-end IT infrastructure" for mobile devices <a class="yt-timestamp" data-t="03:03:07">[03:03:07]</a>.

## The Internal Monolith Problem and Bezos's Mandate

Around 2001-2002, Amazon faced a critical internal problem: its monolithic software codebase, designed in 1995 by Shell Kaphan, was hindering growth and innovation <a class="yt-timestamp" data-t="03:08:58">[03:08:58]</a>.
*   **Slow Development:** Adding new features or teams to the monolith could break everything, leading to code freezes and a literal grinding halt in development <a class="yt-timestamp" data-t="03:31:50">[03:31:50]</a>.
*   **Complexity:** The codebase was a "rat's nest of complexities," making communication and coordination between teams difficult and fearing unintended breakage <a class="yt-timestamp" data-t="03:25:25">[03:25:25]</a>.
*   **Growth Impediment:** This technical bottleneck prevented Amazon from expanding into new businesses and categories, which was crucial for its [[amazons_early_history_and_founding | cashflow-driven growth model]] <a class="yt-timestamp" data-t="03:41:40">[03:41:40]</a>.

Instead of increasing communication and coordination (as Microsoft did with program managers <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>), Bezos and his technical assistant, [[awss_business_model_and_financial_impact | Andy Jassy]] (who would later become Amazon's CEO <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>), made a radical decision: *less communication, no communication* <a class="yt-timestamp" data-t="04:49:09">[04:49:09]</a>. This was a direct application of the Web 2.0 API concept internally.

### The Bezos API Mandate
A legendary internal memo, later described by former Google engineer Steve Yegge, outlined Bezos's mandate:
> 1. All teams will henceforth expose their data and functionality through service interfaces <a class="yt-timestamp" data-t="04:50:06">[04:50:06]</a>.
> 2. Teams must communicate with each other through these interfaces <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
> 3. There will be no other form of inter-process communication allowed: no direct linking, no direct reads of another team's data store, no shared memory model, no backdoors whatsoever. The only communication allowed is via service interface calls over the network <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.
> 4. It doesn't matter what technology they use... Bezos doesn't care <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.
> 5. All service interfaces, without exception, must be designed from the ground up to be externalizable – that is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
> 6. Anyone who doesn't do this will be fired <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
> 7. Thank you; have a nice day <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

This mandate forced a "service-oriented architecture" (SOA) where every small team and individual feature became its own separate application interacting via strictly documented APIs <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. The goal was to remove communication overhead and allow engineers to focus on "making their beer taste better" – i.e., building new features and improving customer experience, rather than managing complex infrastructure <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

## The Birth of Cloud IT Infrastructure

The internal shift to SOA inevitably led to the externalization of IT infrastructure. With decentralized teams operating independently, central planning for IT capacity became impossible <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. Amazon realized they needed to transform IT itself into an API-accessible pool of computing resources <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

### Jassy's Vision Document and the Launch of Core Services
In mid-2003, [[awss_business_model_and_financial_impact | Andy Jassy]], as Jeff Bezos's TA, proposed taking this API-based IT infrastructure and offering it to third parties <a class="yt-timestamp" data-t="05:58:19">[05:58:19]</a>. He famously wrote a six-page document (adjusting margins to fit everything, even omitting financial projections) outlining this vision and asking for 57 new hires <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. The proposal was approved, and Jassy took over the nascent AWS division from Colin Bryar <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>.

The vision was to launch a complete "operating system of the internet" with core IT primitives: storage, compute, databases, and a content distribution network (CDN), all necessary to "recreate any internet service of scale" <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>. However, this full suite wasn't launched simultaneously.

The first service to launch was **S3 (Simple Storage Service)** in March 2006 <a class="yt-timestamp" data-t="01:05:52">[01:05:52]</a>. S3 offered magical, insanely cheap object storage accessible via URL <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>. This allowed developers to "dump images there" without worrying about buying, configuring, or maintaining servers, paying only as they go <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.

**EC2 (Elastic Compute Cloud)** launched in beta a few months later, in August 2006 <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>. EC2 provided compute resources – a "processor in the cloud" – that developers could spin up and treat like their own server, but without persistent storage <a class="yt-timestamp" data-t="01:07:22">[01:07:22]</a>.

Later services included:
*   **CloudFront** (CDN) in 2008 <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.
*   **RDS (Relational Database Service)** in 2009, which ran existing database systems like Postgres in the cloud <a class="yt-timestamp" data-t="01:07:42">[01:07:42]</a>.

### The "Dissenting Narrative" for EC2
Concurrently and somewhat separately from Jassy's overarching business plan, the idea for virtualized compute servers was also developed by network engineer Benjamin Black and his boss, Chris Pinkham (who reported to Amazon CIO Rick Dalzell) <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. They wrote a six-page document on restructuring IT architecture and appended the idea of selling virtual compute servers to third-party developers <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.

Pinkham, wanting to move to South Africa, was convinced by Dalzell to stay and lead a new Amazon subsidiary in Cape Town <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>. This subsidiary, led by Chris Pinkham and engineer Chris Brown, independently built EC2 <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>. Brad Stone, in *The Everything Store*, notes that "EC2 was born in isolation, with Pinkham talking to his colleagues in Seattle only sporadically at least for the first year" <a class="yt-timestamp" data-t="01:12:43">[01:12:43]</a>. Pinkham reportedly sought distance from Bezos's "intrusive" attention <a class="yt-timestamp" data-t="01:12:50">[01:12:50]</a>.

While Jassy's account suggests his vision document in September 2003 predated Pinkham's move to South Africa and outlined EC2 <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>, there is clear tension between the official narrative and the decentralized innovation that Amazon prides itself on <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. This highlights that success often has "many fathers" <a class="yt-timestamp" data-t="01:08:48">[01:08:48]</a>, and it's less about a single idea and more about the "thousands of micro decisions" made during execution <a class="yt-timestamp" data-t="01:15:48">[01:15:48]</a>.

## Market Disruption and Early Adoption

AWS's launch revolutionized the IT landscape with its radical business model:
*   **Credit Card Provisioning:** As James Hamilton, then an engineer at Microsoft and later an AWS SVP, noted, S3 allowed provisioning storage with just a credit card, eliminating proposals, RFPs, vendor selection, and data center space <a class="yt-timestamp" data-t="01:18:44">[01:18:44]</a>. The cost for development and testing could be mere dollars <a class="yt-timestamp" data-t="01:19:24">[01:19:24]</a>.
*   **Pay-As-You-Go:** This model was disruptive because traditional IT companies (Oracle, Microsoft, IBM, HP) operated on high-margin, six-to-eight-figure contracts, not small, pay-as-you-go services <a class="yt-timestamp" data-t="01:20:20">[01:20:20]</a>.
*   **Birth of Startups:** AWS enabled a new wave of startups like Dropbox, Instagram, Airbnb, Uber, and Zynga <a class="yt-timestamp" data-t="01:20:40">[01:20:40]</a>. It drastically reduced the time and capital needed to launch a new service, allowing ideas to go from concept to internet-ready in days <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Startup Ecosystem Engagement:** Amazon actively embraced the startup community, offering free credits and developer evangelism, making AWS the "obvious default" for building new ventures <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>. They even launched the AWS Startup Challenge in 2007, where Justin.tv (which later pivoted to Twitch, acquired by Amazon) was an early contestant <a class="yt-timestamp" data-t="01:21:37">[01:21:37]</a>.

AWS initially targeted startups, recognizing that large enterprises would be hesitant to move all their mission-critical applications to the cloud <a class="yt-timestamp" data-t="01:23:50">[01:23:50]</a>. However, as the platform matured, it gained enterprise trust:
*   **Netflix Adoption:** In 2009, Netflix, despite competing with Amazon.com, decided to move its entire streaming infrastructure to AWS, demonstrating that AWS was a legitimate, independent infrastructure decision <a class="yt-timestamp" data-t="01:31:35">[01:31:35]</a>.
*   **Government Contracts:** The CIA also became an AWS customer, signaling sufficient security for highly sensitive operations <a class="yt-timestamp" data-t="01:32:46">[01:32:46]</a>. NASA famously used AWS starting in 2009 for data streaming and video distribution of the Mars landing <a class="yt-timestamp" data-t="01:45:10">[01:45:10]</a>.

## Competitors' Misses

Traditional IT and other tech giants largely "whiffed" on the cloud opportunity due to various factors:
*   **Oracle and IBM:** These companies, accustomed to 80% gross margins on proprietary hardware and software, saw AWS's 20-40% target margins as unattractive <a class="yt-timestamp" data-t="01:34:52">[01:34:52]</a>. Their business models relied on large upfront licenses and expensive upgrades, which cloud infrastructure disrupted by offering continuous updates <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. They also lacked the ability to "meter usage" and charge dynamically <a class="yt-timestamp" data-t="01:34:20">[01:34:20]</a>.
*   **Microsoft:** Microsoft faced internal power struggles, particularly from the Windows Server group, which feared cannibalization of its lucrative license business <a class="yt-timestamp" data-t="01:37:46">[01:37:46]</a>. When they did launch Azure, they initially took a "platform as a service" (PaaS) approach (Azure Cloud Services), trying to build a new development paradigm instead of offering basic "infrastructure as a service" (IaaS) primitives like AWS <a class="yt-timestamp" data-t="01:39:01">[01:39:01]</a>. This meant they missed both startups (who wanted primitives) and enterprises (who needed lift-and-shift capabilities) <a class="yt-timestamp" data-t="01:30:45">[01:30:45]</a>. Microsoft eventually corrected course under Satya Nadella, but lost valuable years <a class="yt-timestamp" data-t="01:38:45">[01:38:45]</a>.
*   **Google:** Google, having accidentally stumbled into an "unbelievably cash generative" advertising business with high gross margins, viewed a 30% gross margin cloud business as less attractive <a class="yt-timestamp" data-t="01:41:01">[01:41:01]</a>. They also lacked enterprise sales competency and the "iron gut" for a "grind it out" business like AWS <a class="yt-timestamp" data-t="01:43:01">[01:43:01]</a>. Despite having advanced underlying technology from their search operations, their initial cloud offering, Google App Engine, was also a PaaS approach, which was too far ahead of the market and failed to gain traction <a class="yt-timestamp" data-t="01:43:25">[01:43:25]</a>.

## AWS's Continued Growth and Strategy

[[growth_and_impact_of_aws_on_amazons_business | AWS's business model and financial impact]] has been extraordinary. Since 2015, AWS has consistently contributed the majority of Amazon's operating profits <a class="yt-timestamp" data-t="01:56:54">[01:56:54]</a>.

*   **Financial Performance:** AWS currently operates at an $80 billion annual revenue run rate <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>. Its deferred revenue backlog (committed contractual revenue) is over $100 billion <a class="yt-timestamp" data-t="01:52:56">[01:52:56]</a>. In 2014, Jeff Bezos declared AWS's market size "unconstrained" <a class="yt-timestamp" data-t="01:54:44">[01:54:44]</a>. This is based on the idea that anything a computer could touch, AWS could take a tax on <a class="yt-timestamp" data-t="01:55:12">[01:55:12]</a>.
*   **Market Share:** AWS holds approximately 39% of the cloud market share, with Azure at 21% and Google at 7% <a class="yt-timestamp" data-t="01:58:03">[01:58:03]</a>.
*   **Database Dominance:** Beyond compute and storage, AWS is a massive database business, with its database services (like Redshift and Aurora) ranking among its most used, taking significant market share from Oracle <a class="yt-timestamp" data-t="01:46:24">[01:46:24]</a>. The name "Redshift" itself is a nod to "shift away from Big Red" (Oracle) <a class="yt-timestamp" data-t="01:47:22">[01:47:22]</a>. The global database software market is $100 billion and growing at 10% per year <a class="yt-timestamp" data-t="01:47:39">[01:47:39]</a>, with databases being some of the stickiest software due to the sheer volume of data and migration challenges <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Even Amazon.com itself took 13 years (until 2019) to fully migrate off Oracle databases onto AWS products <a class="yt-timestamp" data-t="01:51:15">[01:51:15]</a>.
*   **Hardware Innovation:** Since 2015, Amazon has invested in custom chip design by acquiring Annapurna Labs, developing specialized chips for machine learning training (Trainium) and inference (Inferentia) <a class="yt-timestamp" data-t="01:58:34">[01:58:34]</a>.
*   **Evolving Cloud Definition:** The meaning of "cloud" has evolved. Initially, it meant using primitive building blocks in Amazon's data centers on a pay-as-you-go basis <a class="yt-timestamp" data-t="02:29:44">[02:29:44]</a>. Now, it refers to using higher-level, often proprietary, cloud services that can run in multiple public clouds or even in the customer's own data center (hybrid cloud), with AWS employees installing and maintaining servers on-prem <a class="yt-timestamp" data-t="02:28:08">[02:28:08]</a>. This reflects [[awss_approach_to_cloud_computing_and_technology_strategy | AWS's approach to cloud computing and technology strategy]] and its increasing shift towards a platform-as-a-service model, offering more "cloud-native" services like Lambda (serverless computing) <a class="yt-timestamp" data-t="02:28:51">[02:28:51]</a>.
*   **Customer Obsession:** AWS's consistent success stems from its intense focus on customer needs, always prioritizing what developers and IT managers want to build or migrate to <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. They famously resist building products without a clear customer use case, even for hyped technologies like blockchain <a class="yt-timestamp" data-t="02:30:10">[02:30:10]</a>.

## The Data Warehousing "Miss"

Despite its successes, AWS has one notable "black mark": missing the data warehousing market, exemplified by Snowflake's rise to a $50 billion company storing data on AWS and other public clouds <a class="yt-timestamp" data-t="02:11:12">[02:11:12]</a>. While Amazon has Redshift, a fast-growing service, it requires significant customization and does not offer the same out-of-the-box developer experience as Snowflake <a class="yt-timestamp" data-t="02:13:24">[02:13:24]</a>. This oversight may be attributed to Amazon's size and commitment to existing Service Level Agreements (SLAs), which can hamper agility, and a focus on competing with traditional players like Oracle rather than identifying new customer segments <a class="yt-timestamp" data-t="02:02:56">[02:02:56]</a>.

## Conclusion

AWS is considered one of the greatest case studies in business power. It embodies several "seven powers":
*   **Counter-positioning:** AWS offered a business model that incumbents could not pursue without cannibalizing their existing, high-margin revenue <a class="yt-timestamp" data-t="02:14:43">[02:14:43]</a>.
*   **Scale Economies:** AWS benefits from immense scale, allowing it to amortize massive fixed costs (data centers, infrastructure) across a huge customer base. This enables lower prices and higher profit margins than competitors <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. This also allows them to proactively reduce prices, fostering growth and confidence in future infrastructure investments <a class="yt-timestamp" data-t="02:24:28">[02:24:28]</a>.
*   **Switching Costs:** Once customers move their data and applications to AWS, the practical and financial costs of migrating away are substantial <a class="yt-timestamp" data-t="02:15:10">[02:15:10]</a>.
*   **Branding:** AWS's market leadership and consistent innovation have built strong brand trust, making it the default choice for many new projects and expansions <a class="yt-timestamp" data-t="02:15:28">[02:15:28]</a>.

AWS is often likened to an "unregulated public utility for the internet" <a class="yt-timestamp" data-t="02:22:57">[02:22:57]</a>. This business mirrors [[amazons_early_history_and_founding | Amazon's retail business]] in its heavy, amortized investments (data centers instead of fulfillment centers), but with significantly higher profit margins <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

[[bezos_and_the_foundation_of_amazon | Jeff Bezos's early career at a startup]] instilled in him a focus on "asymmetric upside," where the potential for enormous returns outweighs the risk of frequent small failures <a class="yt-timestamp" data-t="03:11:13">[03:11:13]</a>. This philosophy, coupled with his genius as a "high beta capital allocator," led to the massive investment in AWS, which effectively became the most successful venture bet in history for Amazon <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.