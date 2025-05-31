---
title: Monads unique blockchain technology and its impact on crypto
videoId: aW3KlttN814
---

From: [[when-shift-happens]] <br/> 

Monad Labs, the company behind Monad, has recently secured $225 million in funding, with Monad being described as a parallel EVM Layer 1 blockchain aimed at significantly increasing throughput for decentralized applications (dApps) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Heon Han, co-founder and CEO of Monad Labs, views Monad as a "super performing blockchain" designed to offer the best of both worlds between performance and compatibility <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Its core goal is to enable developers to benefit from much cheaper transactions, ultimately allowing their applications to achieve world-scale adoption <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## The Need for Monad's Innovation

The current state of on-chain crypto is described as "pretty inefficient" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. This inefficiency stems from technology that isn't performant and high individual transaction costs for market maker orders <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### Understanding Market Efficiency: Lessons from High-Frequency Trading

[[Impact of crypto on physical infrastructure and technology | High-frequency trading]] (HFT) is crucial in financial markets because it uses computers to automate market-making functionality that was once done by humans <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This automation leads to more efficient markets, tighter spreads, and better liquidity, making the cost of trading and investing cheaper for end-users <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

In traditional centralized markets (like NASDAQ or CME), efficiency is highest. Centralized exchanges trading crypto assets represent a medium level of efficiency, while [[Cryptocurrency and blockchain ecosystem challenges | decentralized exchanges]] trading crypto assets are currently the least efficient, resulting in higher costs for users <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. The inability of market makers to update quotes frequently due to high transaction costs contributes significantly to this inefficiency <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### The Scalability Challenge

The current [[Blockchain scalability and polkadot | scalability]] of existing EVM Layer 1 blockchains is a major bottleneck <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. For an app to reach world scale, similar to being the number one app on the iOS app store with millions of daily active users, it would require massive transaction throughput <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. For instance, an app with one million daily active users performing 50 transactions per user per day would generate 50 million transactions daily, equivalent to 500 transactions per second (TPS) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This volume would "more than saturate" any existing EVM blockchain <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

## Monad's Unique Blockchain Technology

Monad addresses these [[Cryptocurrency and blockchain ecosystem challenges | challenges]] by being unique in its effort to introduce [[the_concept_and_importance_of_parallelization_in_blockchain_technology | parallelism]] to the EVM, along with other performance re-architectures necessary for dApps to scale to mass adoption <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### The Concept of Parallelism

Modern computers intuitively use parallel processing (e.g., browsing with multiple tabs, playing music while editing a document) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. However, Ethereum and most other Ethereum-compatible blockchains are "single-threaded," meaning transactions are processed one after another, which is very inefficient <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

Ethereum's architecture was not initially built for high transaction volumes, as significant usage only began around "DeFi Summer" in 2020 <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. Making performance improvements requires years of development <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Beyond Layer 2 Rollups

While many projects in 2022 focused on Layer 2 rollups for scaling, Monad pursued an "orthogonal direction": optimizing the execution stack <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. This approach involves intensive low-level systems engineering, which was less emphasized by existing crypto teams focused on rollups <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

### Addressing Performance Bottlenecks

Monad's design is driven by observations of real performance bottlenecks <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. The single biggest bottleneck identified is "state access." Every transaction involves changing some state (e.g., account balances, smart contract data) <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. Accessing this state, which lives on a solid-state drive (SSD), is expensive. Monad has undertaken significant efforts to make state access more performant <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. Monad aims to achieve 10,000 TPS, or a billion transactions per day, through parallel execution and other improvements <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

### Learning from Solana and EVM Compatibility

Monad has benefited from hindsight, observing other projects that didn't anticipate or fully address all problems <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. [[Sui Network and Blockchain Innovation | Solana]], for example, rebuilt everything from scratch, focusing on performance and optimization at an early stage <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. Many other Layer 1s from 2017-2018 were Ethereum forks that primarily changed the consensus mechanism while reusing the same virtual machine and storage <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.

While Solana's approach yielded performance gains, Monad recognized the importance of EVM compatibility. Abandoning the EVM bytecode standard and Solidity would mean losing access to a vast ecosystem of developers, libraries, tooling, and applied cryptography research <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>. Monad chose to preserve the EVM status quo where it makes sense, meeting developers where they are while pushing the boundaries of performance <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.

## Funding and Financial Discipline

Monad's recent $225 million raise is seen as a way to put the project and its ecosystem in the best position to succeed, acting partly as a hedge for an uncertain future <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>. Despite the substantial funding, the team aims to remain disciplined about spending and focus on activities with a positive return on investment <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>.

> "I'd like to think that our team will continue to be disciplined about spend and disciplined about doing things that are positive Roi." <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>

## Building a Strong Community

Monad's rapid rise and significant funding are attributed to two main factors: unique and differentiated technology that meets a market need, and an incredibly strong community <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>.

### The Power of Community in Crypto Marketing

In [[Blockchain and Crypto Innovation | crypto]], effective marketing is synonymous with [[Vision and innovation in blockchain technology | community building]] <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a>. It's never too early to start building a community; Monad started in November 2022, just before the FTX collapse, finding that a bear market can paradoxically help by attracting dedicated, like-minded individuals <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>.

> "The crypto community in general is kind of amazing and that there's tons of people who care about things before they're perfect before they live." <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>

The "engineer mindset" of building the product first before marketing is contrasted with the "entrepreneur mindset" of building momentum and selling the vision early <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>. For Monad, the mantra has been "the community is the product" from day one <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. This means making the community experience "addictive" and enjoyable, not just outsourcing it to agencies <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>.

Monad's community is characterized by creativity, fun, art, memes, and social engagement <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>. Examples include community-hosted karaoke nights with hundreds of participants and oversubscribed poker games with community DJs <a class="yt-timestamp" data-t="00:45:41">[00:45:41]</a>. The team is in touch with the spirit of Crypto Twitter, not taking themselves too seriously and embracing community-driven lore like purple Pepes and the "mandac" hedgehog <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

Even though [[blockchain_and_crypto_innovation | crypto]] is often seen as an "extremely opportunistic industry" with financial motivations, Monad has built a strong community far ahead of any token launch <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>. Many community members are genuinely interested in the project, forming friendships and shared experiences beyond just farming for airdrops <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>.

## Future Outlook: Beyond the Playbook

For the Monad mainnet launch, the goal is to exceed high expectations <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>. This means going beyond "table stakes" like a great DEX, lending protocol, NFTs, oracles, and liquidity incentives <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. Monad aims for "completely new," "unique experiences" for users that drive immediate engagement, similar to how Friend.tech drove success for Base <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>.

Monad seeks to work with ambitious builders who have out-of-the-box ideas, even if their success is initially uncertain <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

### Boring Consistency and Humility

A key differentiator for Monad's approach is "boring consistency" <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>. This means thinking critically and logically, doing the same day in and day out, and not merely following a playbook <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

Humility is paramount, especially in the crypto space where overconfidence and "hubris" often lead to downfall <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>. Given that crypto users are very smart and judgmental, making big claims requires being able to back them up <a class="yt-timestamp" data-t="00:57:56">[00:57:56]</a>.

Consistency also means acknowledging the privilege of building in this space and taking advantage of the opportunity every day <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>. Even when community building wasn't an "instant massive success," persistence and belief in the right direction were crucial <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.

### Long-Term Vision

A significant prediction for the next 12 months is that more projects will prioritize [[vision_and_innovation_in_blockchain_technology | community]] building, moving beyond merely acknowledging its importance to actively dedicating resources and founder time to it <a class="yt-timestamp" data-t="01:06:12">[01:06:12]</a>.

There is a current tendency for projects to prioritize the short term, driven by perceptions of bull markets <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>. However, Monad advocates for "longer term thinking and longer term planning," emphasizing that projects should be built to last "multiple cycles" <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>. Founders should resist pressure from short-term profit-driven investors and instead focus on what's right for the project's long-term health <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. The core belief is that if the original idea is sound, it will attract the necessary funding and ultimately prevail <a class="yt-timestamp" data-t="01:10:24">[01:10:24]</a>.