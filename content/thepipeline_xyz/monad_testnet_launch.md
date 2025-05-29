---
title: Monad Testnet launch
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The [[monad_public_test_net_launch | public test net]] for Monad is officially going live, serving as a showcase for the [[Monad Blockchain Technology | technology]] that has been developed from the ground up [00:00:02](<a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, [00:01:23](<a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>), [00:33:38](<a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>). While many see the launch of a testnet or mainnet as a finish line, for Monad, it is viewed as "crossing the starting line" [00:00:20](<a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, [00:00:25](<a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>), [00:48:18](<a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>), signifying the beginning of further innovation and growth [00:49:09](<a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>), [00:50:04](<a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>).

## Building from Scratch

Monad's unique approach involved building its protocol entirely from scratch [00:01:44](<a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>), rather than forking existing open-source projects [00:02:11](<a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>). This decision was made to ensure greater technical control and flexibility [00:02:06](<a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>).

James Hunsaker, CEO/CTO at Category Labs, explained that if they had forked an existing project, they would have had to modify too many things, preventing them from leveraging ongoing new features or maintenance [00:02:19](<a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>). Building from scratch allows Monad to be "very particular about the way certain things are implemented" [00:02:41](<a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>), such as memory allocation or disk interaction, to achieve optimal performance [00:02:57](<a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>), [00:03:07](<a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>).

### Why Others Haven't Taken This Approach

For over 10 years, the EVM has existed, yet few projects have attempted a similar ground-up rebuild focused on high performance [00:03:27](<a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>), [00:03:39](<a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>). James points out that existing Ethereum clients are "arbitrarily rate limited to this... low throughput" [00:04:07](<a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>) to maintain low node requirements [00:04:13](<a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>). Monad, however, was envisioned from the start as a [[Monad Blockchain Technology | high-performance EVM chain]] with the primary restriction being 100% EVM and Ethereum compatibility [00:04:21](<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>), [00:04:31](<a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>).

Furthermore, building such a system is inherently difficult, requiring specialized low-level systems engineers who are rare in the developer community [00:05:12](<a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>), [00:05:21](<a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>).

## Monad's Technical Innovations

The main challenge in building Monad was achieving concurrent execution to leverage multiple CPU cores, as most existing clients are single-core [00:06:17](<a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>). The "main innovations" in Monad revolve around how transactions are executed to "always keep the machine busy" [00:07:53](<a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>).

James explains the importance of not waiting for disk access, which can take tens of microseconds and add up quickly across many transactions [00:07:10](<a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>), [00:07:37](<a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>). To address this, Monad built its own database [00:08:10](<a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>).

The community often refers to this pipelined execution as the "washing machine" analogy:
> "you have a washing machine, you have a dryer and then you have to fold and you have to put them away right if you can use washer dryer and be folding different sets at different times that allows you to do way more loads in a much shorter time than if you had to do one load all the way through" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>

Monad's architecture is "highly pipeline[d]" [00:09:00](<a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>), constantly striving to keep the CPU active [00:09:02](<a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>). Keon Han, GM at Monad Foundation, uses an airplane analogy: Ethereum was the "zero to one" innovation, enabling smart contracts and permissionless global finance [00:11:11](<a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>), [00:11:51](<a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>). Monad represents the "next step" – the performance engineering layer that optimizes many smaller details to achieve "much more performance and much cheaper transactions" [00:12:04](<a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>).

## Comparison to Devnet and Benchmarking

Earlier in 2024, there was excitement around the [[devnet_launch_and_implications_for_monad | Devnet launch]] [00:16:10](<a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>). James explains the [[comparison_between_devnet_and_testnet_and_their_importance | difference between Devnet and Testnet]]:
*   **Devnet:** Served as a "feedback loop from early testers or infrastructure providers" [00:17:22](<a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>) to identify what was missing or needed fixing [00:17:28](<a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>). It was used for internal testing and running replays to monitor performance metrics like TPS and gas per second [00:16:44](<a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>). One team simulated 3 trillion gas usage, equivalent to about 30 days of Ethereum throughput, in just a few hours [00:17:53](<a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>), [00:18:17](<a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>).
*   **Testnet:** Represents a "whole another sort of phase" [00:17:47](<a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>), allowing individual users to test applications [00:18:59](<a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>). Its goal is to "exercise the technology and get more feedback on the client" [00:32:51](<a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>) in a real-world usage scenario [00:33:01](<a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>). It allows builders to get public user feedback and see what breaks in the wild [00:35:05](<a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>).

### Meaningful Benchmarking

Monad emphasizes using Ethereum history to replay transactions for benchmarking [00:19:31](<a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>), rather than simple token transfers which can be easily inflated [00:20:26](<a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>). James explains that benchmarks of "10K TPS" solely for token transfers are "not interesting because it's easily achievable" [00:20:27](<a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>), with even unoptimized clients capable of 50K TPS on such artificial scenarios [00:20:36](<a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>).

Real Ethereum usage involves more complex transactions like AMMs, lending protocols, and especially expensive ZK-proofs [00:21:26](<a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>). Monad's goal is to handle this "real usage" effectively [00:22:34](<a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>), continuously pushing for higher TPS and gas per second [00:22:14](<a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>).

> "When somebody publishes like oh we're doing 10K TPS and you look and it's like token transfer it's like that's actually not I mean maybe some people are wild by that but I'm not wild by that because I've seen it like even under even not so optimize clients or not parallel execution clients do 50k TPS on the sort of artificial benchmarks" <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>

Monad rejects practices that artificially inflate metrics, such as having all nodes geographically collocated or requiring extremely high hardware/bandwidth [00:24:13](<a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>), [00:24:17](<a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>), [00:26:10](<a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>). Monad intentionally tests worst-case scenarios, like highly stake-weighted nodes in distant locations (e.g., Singapore and New York), to optimize for robust performance under diverse conditions [00:25:40](<a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>), [00:26:03](<a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>).

## What Monad Testnet Unlocks for Developers and Users

Monad aims to provide a "performant version of that shared global state that offers built-in payment rails [and] built-in programmability" [00:13:06](<a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>). This high performance enables applications to scale to "millions or tens or hundreds of millions of users" [00:13:20](<a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>) who already have on-chain assets and digital identities [00:13:25](<a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>).

Specific verticals anticipated to benefit include:
*   **High-fidelity DeFi:** Allowing personal finance to scale to hundreds of millions of users with "really cheap transaction fees" [00:13:45](<a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>). This also leads to low slippage due to efficient liquidity provision and competitive spreads on fully on-chain exchanges [00:14:02](<a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>).
*   **Consumer Space:** Applications targeted at consumers requiring massive scale, potentially reaching "a billion transactions per day" [00:14:22](<a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>), [00:14:33](<a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>).
*   **DePIN (Decentralized Physical Infrastructure Networks) Space:** Where large amounts of usage are price-sensitive [00:38:18](<a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>). Cheaper transaction fees (e.g., a fraction of a cent to push data to chain) [[Monad Blockchain Updates | unlock new business models]] such as marketplaces for health data or device data [00:38:28](<a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>).

A key benefit for users is the ability for applications to "sponsor gas" and simplify the user experience, abstracting away gas fees [00:37:06](<a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>). This is more feasible when gas costs are "really cheap" [00:37:30](<a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>).

Kevin, Director of Growth at Monad Foundation, highlights the "unpredictable" side of new applications that will emerge [00:43:00](<a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>). Just as no one predicted YouTube or Instagram from early internet bandwidth, [[Monad Blockchain Updates | Monad's speed and cost-efficiency]] could enable entirely new crypto use cases, including "AI agents" [00:30:40](<a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>), that are currently hard to foresee [00:43:02](<a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>), [00:43:15](<a class="yt-timestamp" data-t="00:43:15">[00:43:15]</a>).

## Goals for Public Testnet

The public testnet is intended to:
*   **Exercise the technology:** Get more feedback on the client and identify its strengths and weaknesses [00:32:51](<a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>), [00:33:08](<a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>).
*   **Showcase Monad's power:** Demonstrate the capabilities of the [[Monad Blockchain Technology | underlying technology]] and the applications built on it [00:33:38](<a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>), [00:33:45](<a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>).
*   **Generate excitement:** Provide an opportunity for the community to "play around" with the performance capabilities [00:34:01](<a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>).
*   **Attract builders:** Show the real-world performance of Monad to attract new developers looking to push the limits of what's possible in crypto [00:35:31](<a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>), [00:35:48](<a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>).
*   **Gather unexpected data:** Observe how the system handles unforeseen "use patterns" like mass NFT mints or 100,000 concurrent users sending transactions, and how it degrades gracefully when limits are approached [00:27:50](<a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>), [00:28:03](<a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>), [00:29:05](<a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>).

## Misconceptions

A common misconception is that the launch of a testnet or mainnet is the "finish line" for development [00:48:18](<a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>). However, for Monad, it's merely the "starting line" [00:49:06](<a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>). The team has a "massive... queue of ideas" for future optimizations, rewrites, research, new features (e.g., usability, privacy), and increasing decentralization (supporting thousands of nodes) [00:48:59](<a class="yt-timestamp" data-t="00:48:59">[00:48:59]</a>), [00:49:30](<a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>).

Another misconception in crypto, particularly with many EVM-compatible chains, is that "technology doesn't matter" or that "go to market is more important than technology" [00:49:57](<a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>), [00:51:44](<a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>). Monad believes that bringing "real innovative technology" [00:52:41](<a class="yt-timestamp" data-t="00:52:41">[00:52:41]</a>) to market, combined with full EVM and RPC backward compatibility, is the start of a much broader effort to impact crypto adoption [00:51:06](<a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>), [00:52:47](<a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>).

> [Danny Pipelines]: "go try out the test net... you can think of it like a new city is opening and there's a ton of opportunity in this city... everybody has the opportunity to to play a role in that" <a class="yt-timestamp" data-t="00:58:44">[00:58:44]</a>