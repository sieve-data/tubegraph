---
title: NVIDIAs risktaking and decisionmaking in technology development
videoId: y6NfxiemvHg
---

From: [[acquiredfm]] <br/> 

NVIDIA, a company valued at $1.1 trillion at the time of recording and the sixth most valuable in the world, has a history marked by significant risk-taking and strategic decision-making, particularly in technology development. CEO Jensen Huang emphasizes that the company's approach is not about blind bets, but rather about calculated moves based on deep anticipation and thorough preparation [00:11:12]. This philosophy has guided NVIDIA through multiple near-death experiences and positioned it at the forefront of major technological shifts, including the current [[nvidias_role_in_the_growth_of_artificial_intelligence and deep learning | AI explosion]] [00:01:11].

## Early High-Stakes Bets: Revo 128

One of NVIDIA's most critical early decisions revolved around the development of the Revo 128 graphics chip in 1997 [00:03:02]. This period was described by Jensen Huang as "NVIDIA's best moment" because the company's "backs were up against the wall" [00:05:39].

At the time:
*   NVIDIA, founded in 1993 as the only consumer 3D Graphics Company [00:04:45], had pursued a wrong architectural path with MV1 and MV2 that was incompatible with Microsoft's newly released DirectX [00:05:05].
*   Thirty competitors had emerged [00:05:12].
*   The company had only "months of cash left" [00:03:20] and employees were "running out of Hope" [00:05:46].

Facing these challenges, NVIDIA made a sequence of "extraordinarily good decisions" [00:05:35]:
*   **Embracing DirectX**: Instead of fighting the new standard, NVIDIA decided to build the best product for it [00:05:52].
*   **Aggressive Design**: The Revo 128 was designed as the world's first fully hardware-accelerated pipeline for 3D rendering [00:06:01]. It was the biggest chip ever imagined for its time, using the fastest memories and setting a substantially higher cost point than competitors [00:06:24].
*   **Targeting Enthusiasts**: NVIDIA correctly identified a large market of PC enthusiasts willing to pay for the best performance [00:07:27], a segment where "3D graphics is never good enough" [00:07:44].
*   **Virtual Prototyping**: With limited time and money for multiple chip tape-outs, NVIDIA acquired emulation technology from a company (iOS) that was shutting down [00:08:01]. This allowed them to virtually prototype the entire chip, develop the software stack, and run QA before the physical tape-out [00:09:22]. Jensen's mantra was: "If it's not perfect, we'll be out of business" [00:09:15].
*   **Direct-to-Production**: Confidence in the virtual prototype led to the unprecedented decision to go directly to production after the first tape-out [00:10:08].

This experience taught Jensen Huang a crucial lesson: "When you push your chips in... what you really doing is you're when you bet the farm you're saying I'm going to take everything in the future all the risky things and going to pull it in advance" [00:11:37].

## Long-Term Vision: CUDA and AI

NVIDIA's long-term vision and willingness to invest heavily in future opportunities, even when the market demand was not yet apparent, are exemplified by CUDA. The concept for CUDA (Compute Unified Device Architecture) predates its formal release, evolving from earlier experimentation with a "CG" abstraction layer that allowed GPUs to be used for general-purpose computing like CT reconstruction and image processing [00:12:12].

*   **Anticipating General-Purpose Computing**: NVIDIA recognized the highly parallel and massively threaded nature of its programmable shaders, suggesting their potential for general-purpose computing [00:12:40].
*   **Investing Ahead of Demand**: NVIDIA invested "10,000 person years" in building the CUDA platform [00:13:14] years before the mainstream realization of machine learning's potential.
*   **Deep Learning Insight**: When AlexNet demonstrated "incredible effectiveness" in computer vision, NVIDIA went back to first principles, asking why it was so successful and if it was scalable [00:13:40]. They realized deep learning had discovered a "universal function approximator" [00:14:17] that could solve a vast array of problems beyond computer vision, from predicting consumer preferences to weather [00:15:16].
*   **Cultivating the Ecosystem**: NVIDIA worked closely with universities and researchers, democraticizing supercomputing through CUDA [00:18:39]. This proactive engagement with AI researchers like Yann LeCun, Andrew Ng, and Geoff Hinton allowed them to help "advance the research" [00:19:24], even when the technology "looked like a toy" [00:19:48] with blurry 32x32 GAN images [00:19:51]. This relationship led to a "positive feedback system" [01:00:20] that informed NVIDIA's continued investments.
*   **Supporting Open AI**: NVIDIA delivered the first DGX system, their purpose-built AI supercomputer, to OpenAI, emphasizing their commitment to advancing the field [02:11:25].

This foresight and sustained investment played a crucial [[nvidias_role_in_the_growth_of_artificial_intelligence and deep learning | role in the growth of artificial intelligence and deep learning]], leading to NVIDIA's current [[nvidias_dominance_in_ai | dominance in AI]] [00:01:11].

## Anticipating Market Shifts: The Data Center Journey

NVIDIA's [[nvidias_transition_from_gaming_to_enterprise_and_scientific_computing | transition from gaming to enterprise and scientific computing]] and entry into the data center market began nearly two decades ago [00:34:53]. Jensen observed that being limited by a GPU being plugged into a physical PC sitting next to a monitor would eventually "limit our opportunity" [00:35:15].

*   **Separating Computing from Viewing**: The core insight was to separate computing from the viewing device, allowing computation to occur elsewhere [00:35:30].
*   **Cloud Gaming (GFN)**: This led to the development of GeForce Now (GFN), NVIDIA's first cloud product [00:35:59]. Despite facing significant challenges like the speed of light and latency, NVIDIA embarked on this long-term journey [00:36:04].
*   **Remote Graphics**: The second data center product was remote graphics, placing GPUs in enterprise data centers [00:36:26].
*   **Supercomputing**: This then led to the combination of CUDA and GPUs to create supercomputers [00:36:33].

This groundwork in the data center, built through these "three plus previous products," made NVIDIA uniquely ready for the explosion of AI [00:37:26]. The ability to disconnect where computing is done from where it is enjoyed "explodes" the market opportunity [00:36:49].

## Strategic Acquisitions: Mellanox

The acquisition of Mellanox, a high-performance networking company, is considered one of NVIDIA's "best strategic decisions" [00:42:13]. This move, initially surprising to many given NVIDIA's core business, was driven by key insights:

*   **Data Center Foundation**: Jensen concluded that to be a data center company, networking was as critical as the processing chip itself, distinguishing data centers from desktop computers [00:40:03].
*   **Distributed AI**: He observed that AI workloads, unlike traditional hyperscale cloud computing (which virtualizes many users on commodity components), involve "one job... orchestrated across millions of processors" [00:41:10]. This distributed computing model required a different type of networking, akin to supercomputing networks like Infiniband, which Mellanox specialized in [00:41:39].
*   **Pre-Positioning**: The acquisition was an act of "position[ing] yourself near opportunities" [00:42:50], anticipating the need for high-performance networking to train large language models before it became widely apparent [00:43:09].

## Core Principles of NVIDIA's Decision Making

Jensen Huang's approach to decision-making and [[nvidias_innovation_and_adaptation_strategies | innovation and adaptation strategies]] can be summarized by several principles:

*   **"Push Your Chips In When You Know It's Going to Work"**: This means pulling all future risks into the present and thoroughly simulating them in advance [00:11:58]. NVIDIA relies on extensive virtual prototyping and full software stack development before committing to production [00:11:20].
*   **"Mission is the Boss"**: NVIDIA's organizational structure is likened to a computing stack rather than a military hierarchy [00:28:10]. Teams are wired together like a neural network, cutting across traditional organizational boundaries to achieve specific missions [00:30:04]. Information is disseminated quickly and broadly, ensuring everyone from new college graduates to executives hears decisions simultaneously, fostering a meritocracy where influence is earned through reasoning and helping others succeed [00:31:37].
*   **Learning, Not Imitating**: Jensen reads many business books and learns from others' experiences, but emphasizes asking "what does it mean to me in my world?" rather than simply adopting their strategies [00:33:10]. This allows NVIDIA to develop its own unique strategies tailored to its specific context [00:33:41].
*   **Anticipating Future Opportunities**: A CEO's job is to "look around corners and anticipate where will opportunity be someday" [00:37:52]. This involves positioning the company to be "near" potential future markets, ready to "do a diving catch when the Apple falls" [00:38:06]. This foresight explains NVIDIA's early entry into markets like automotive and its long-term investments [00:46:58].

## Philosophy on Competition and Market Creation

NVIDIA prefers to "position ourselves in a way that serves a need that usually hasn't emerged" [00:46:32], often entering "zero billion dollar markets" [00:46:41]. This strategy means that by the time a market emerges, there are few competitors "shaped that way" [00:47:42].

Examples include:
*   Early entry into PC gaming [00:47:49].
*   Reimagining design workstations [00:47:56].
*   Democratizing supercomputing [00:48:03].
*   Reimagining software and computing through AI and machine learning [00:48:15].
*   Current investments in Omniverse, another "zero billion dollar business" [00:48:32].

To maintain a lead, especially after a decade of pioneering, NVIDIA focuses on building platforms that enable an entire ecosystem to succeed. This creates a "network of networks" of developers and customers built around NVIDIA's technology, forming a "moat" [00:49:10].

## The Platform Strategy: UDA and Architectural Compatibility

NVIDIA has always considered itself a platform company internally [00:50:56], even when its external products were seen as pure technology. This goes back to its "UDA" (Universal Device Architecture) concept from day one, which later evolved into CUDA [00:51:06].

*   **Developer-Oriented Foundation**: NVIDIA's initial business strategy was to be a "game console inside the PC" requiring developers [00:51:35]. This led to hiring developer relations personnel early on, fostering relationships with game and 3D developers [00:51:48].
*   **Architectural Compatibility**: A core "unnegotiable rule" at NVIDIA is that every accelerator must be architecturally compatible with others [00:54:23]. This commitment ensures a stable "installed base" for CUDA, currently hundreds of millions of active GPUs [00:54:02]. This consistency is crucial for a computing platform, allowing developers to build on a reliable foundation over decades [00:54:10].

## Reflections on Leadership and Risk

Jensen Huang acknowledges that building a successful company is "insanely hard" and "a million times harder than I expected" [00:55:04]. He believes the "superpower of an entrepreneur" is not knowing the full extent of the difficulty, or "trick[ing] my brain into thinking how hard can it be" [02:10:52].

He emphasizes the importance of:
*   **Prioritization**: Managing time effectively and not letting external schedules dictate one's priorities [01:12:00].
*   **Support System**: The "unwavering support" of family, friends, and long-term colleagues (many at NVIDIA for 30 years) is essential for enduring the "emotional trauma" and challenges, especially during significant market downturns [02:21:58].

Despite the challenges, Jensen remains driven by the desire to "not let the employees down" and ensure they can build great lives and careers [02:12:51]. He sees NVIDIA's journey as one of continuous growth, where improved productivity leads to prosperity, enabling companies to expand into new areas and create more jobs, driven by humanity's "infinite ambition" [01:03:00]. NVIDIA's ability to transcend being just a "chip company" to becoming an "AI company" has expanded its market opportunity by "a thousand times" [02:17:08], enabling it to manufacture intelligence and address a market measured in trillions [02:16:07].