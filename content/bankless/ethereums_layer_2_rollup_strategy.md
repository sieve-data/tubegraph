---
title: Ethereums Layer 2 Rollup Strategy
videoId: WzSVcUeKRZ4
---

From: [[bankless]] <br/> 

Ethereum's approach to scaling involves a "rollup-centric roadmap," which is built around a strong Layer 1 (L1) [00:00:14]. This strategy is considered the correct long-term architecture, as it's believed that a blockchain cannot scale to billions of users with microtransactions without Layer 2s (L2s) [00:15:00]. L2s provide "execution compression," where actions are compressed and then verified on the L1 [00:15:14].

## Benefits of Layer 2s

L2s are essential for Ethereum's growth and scalability [00:41:43]. Two main roles for L2s are envisioned:
*   **Transparent Generic Spillover Space** L2s can act as a transparent and generic overflow space from the L1 [00:41:18]. While the L1 is being scaled, it won't immediately handle all demand, necessitating L2s indefinitely [00:41:39]. The goal is to achieve seamless interoperability between L1 and these L2s, with standards for assets that flow between them, ultimately making the user experience indistinguishable between L1 and L2 [00:41:52].
*   **Special Purpose Layer 2s** There is also room for more specialized, differentiated L2s designed for specific applications, such as gaming [00:42:20]. These L2s may not aim for full transparency with the L1, maintaining a distinct user experience [00:42:31]. The L1 would still provide data availability and settlement for them, with this relationship expected to remain stable over time [00:42:41].

## Challenges and Shifting Focus

Despite the long-term vision, Ethereum has faced [[challenges_ethereum_faces_in_the_crowded_layer_1_space | challenges Ethereum faces in the crowded Layer 1 space]] and a perceived lack of growth, especially on Layer 1 [00:13:09]. This led to a period where Layer 1 was "neglected" [00:00:12].

A key issue is that L2 growth, such as on Base, is not always perceived as Ethereum growth [00:16:06]. This is attributed to several factors:
*   **Lack of Unified Product** L2s have not been sufficiently integrated to feel like one cohesive product with the L1 [00:16:36].
*   **Interoperability Issues** Technical interoperability between L1 and L2s has not been as good as it should be [00:16:59].
*   **Branding and Economic Disconnect** L2s often have their own branding and, while they contribute to fees, they can feel like separate chains competing with Ethereum [00:17:15].

This has led to a realization that Ethereum needs to adopt a "product mindset" and actively listen to app builders and users [00:09:51]. The previous focus on long-term, high-brow research from an "ivory tower" perspective meant not building what users wanted [00:09:22].

## Reorienting the Strategy

There is now a strong consensus on the urgency of short to medium-term actions to restore Ethereum's growth [01:29:28]. [[ethereums_strategic_pivot_and_scaling_layer_1_efforts | Ethereum's strategic pivot and scaling Layer 1 efforts]] is a primary focus, reversing the past mistake of being complacent and rejecting growth on L1 [00:15:36].

Key changes and objectives include:
*   **Scaling L1** The immediate focus is on [[scaling_ethereum_layer_1_and_layer_2_solutions | scaling Ethereum layer 1 and layer 2 solutions]] [00:34:26]. There is broad acceptance for significantly increasing L1 capacity, aiming for a 10x increase from current levels within a few years, potentially reaching a 300 million gas limit [00:38:39]. This involves three stages:
    1.  **Utilizing Existing Headroom** Pushing the current technology without changes, as Ethereum was historically very conservative [01:03:38]. The gas limit increased from 30 million to 36 million, with projections to reach 72 million by fall and 100 million by the end of the year [01:04:13].
    2.  **Feature-Based Scaling** Implementing features like delayed execution and block-level access lists in upcoming hard forks (e.g., Glamsterdam) to further increase scalability without proportionally increasing network load [01:04:54].
    3.  **ZK-Based Scaling** In two to three years, leveraging ZK-based proving systems to allow the L1 to scale aggressively while maintaining lightweight verification for nodes [01:05:27]. This is considered a "rollup trick" for the L1 itself, where the L1 technically becomes a rollup [00:59:02].
*   **Improved Interoperability** Establishing standards for assets flowing between L1 and L2s to create a more seamless user experience [00:41:54].
*   **Making L1 Economically Important** Ensuring the L1 remains a vibrant economic center for DeFi, providing reasons for L2s to build on Ethereum rather than other data availability layers [00:44:49].
*   **Reducing Block Times and Improving Finality** While scaling L1 capacity is a priority, reducing block times and improving finality are also crucial for DeFi and user experience [01:09:12]. This includes:
    *   **Optimistic Pre-confirmations** Providing rapid, cryptoeconomically guaranteed confirmations for transactions, which could drastically improve user experience by eliminating "spinning wheel" waits [01:00:27].
    *   **Reduced Slot Times** Exploring the possibility of reducing slot times, potentially to 6 seconds in the medium term, and even aiming for below 4 seconds or 1 second in the very long term, while preserving Ethereum's core properties of verifiability and censorship resistance [01:12:27].
    *   **Faster Censorship Resistance** Ideas like "for fossil" could lead to much shorter censorship resistance times [01:14:14].

> [!NOTE] The goal is to offer a path that leads to a mutually beneficial outcome for L1 and L2s, where being a "tightly integrated L2" is attractive due to enhanced interop and continued access to the Ethereum brand [00:56:40]. This forms the basis of [[ethereums_scaling_strategy_with_native_rollups | Ethereum's scaling strategy with native rollups]].

## Native Rollups and Product Differentiation

The concept of "native rollups" and "based rollups" signifies a move towards L2s being more deeply integrated with Ethereum's L1 [00:52:02]. These models reduce the overhead for L2s by eliminating certain "pie slices" of their security models (e.g., L1 repurposing the sequencer) [00:52:13]. This allows these L2s to be "much closer to truly being Ethereum" [00:53:33].

This means the L1 would offer services to L2s, such as:
*   **Sequencing** As seen with based rollups, where the L1 sequencer is repurposed [00:52:15].
*   **Eliminating Overhead** Reducing the need for L2s to manage their own security councils or proof systems [00:40:11].
*   **R&D and Developer Resources** Ethereum actively invests in making L2s more compatible with the L1 [00:54:50].

This approach increases "stickiness" for L2s, providing significant value that makes it difficult for them to switch to other ecosystems [00:54:44]. The L1 and this group of native L2s are expected to converge on a shared tech stack, enabling seamless user experience, immediate finality, and same-slot async composability [00:59:40]. This shared infrastructure aims to make interactions on L2s feel as fast and secure as on L1, effectively creating one large, infinite compute space [00:42:08].

## Coordination and Leadership

The shift in strategy also involves changes within the Ethereum Foundation (EF). The EF is moving from solely a public goods funding organization to one that takes more responsibility for guiding Ethereum holistically, encompassing product experience and strategy [01:19:03]. This includes a shift in leadership and a greater openness to communication and a "product mindset" [01:21:54].

The overall sentiment is that the "Ethereum ship is slowly turning itself around" [00:39:40]. While the actual path of the ship hasn't moved far, the "mindset" of the community and the EF has significantly shifted towards acknowledging problems and actively pursuing solutions [01:29:33]. This renewed focus on [[the_importance_of_ethereums_layer_1_and_layer_2_dynamics | the importance of Ethereum's Layer 1 and Layer 2 dynamics]] aims to ensure Ethereum's continued growth and competitive edge.