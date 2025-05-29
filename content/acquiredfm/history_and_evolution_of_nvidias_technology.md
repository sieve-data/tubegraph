---
title: History and evolution of Nvidias technology
videoId: y6NfxiemvHg
---

From: [[acquiredfm]] <br/> 

Nvidia's technological journey has been characterized by strategic pivots, audacious bets, and a deep understanding of future computing needs. From its early days as a graphics chip designer to its current standing as a powerhouse in artificial intelligence, Nvidia's evolution is a testament to its forward-thinking approach.

## The Early Days: Graphics and Near-Death Experiences
Founded in 1993 <a class="yt-timestamp" data-t="04:45:10">[04:45:10]</a>, Nvidia initially focused on transforming the PC into an accelerated computing platform for 3D graphics <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. However, their initial architectures (MV1 and MV2) were based on forward texture mapping and curves, not triangles, which proved to be the "completely wrong answer" for rendering <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

### The "Reset" with Riva 128
By 1997, Nvidia faced a critical juncture: they had months of cash left, Microsoft had rolled out DirectX (incompatible with Nvidia's architecture), and 30 competitors had emerged <a class="yt-timestamp" data-t="05:06:40">[05:06:40]</a>. This led to a "reset" of the company with the development of the Riva 128 chip <a class="yt-timestamp" data-t="04:40:53">[04:40:53]</a>.

Facing immense pressure, Nvidia made a series of "extraordinarily good decisions" <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>:
*   **Embracing DirectX**: Instead of fighting it, they decided to build the "best thing in the world" for DirectX <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **Riva 128**: This chip became the world's first fully hardware-accelerated pipeline for 3D rendering, accelerating every element from transform to frame buffer <a class="yt-timestamp" data-t="06:01:03">[06:01:03]</a>. It was the biggest chip ever imagined at the time, using the fastest memories <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.
*   **Simulate Everything, Bet the Farm**: Due to limited time and money, Nvidia taped out the Riva 128 directly into production without a physical prototype <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. They used an emulator, acquired from a company called iOS, to virtually prototype and test the chip and its software in advance, ensuring it would be "perfect" upon tape-out <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. This philosophy of pulling future risks into the present remains a core principle <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Targeting Enthusiasts**: Nvidia identified and focused on the PC enthusiast market, where users were willing to pay for the "next fastest thing" and "best of everything" <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
*   **3D Graphics as a "Sustainable Technology Opportunity"**: Nvidia recognized that 3D graphics would "never be good enough," ensuring continuous demand for better technology <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.

## The Birth of CUDA and General Purpose Computing
A crucial step in Nvidia's evolution was the development of CUDA (Compute Unified Device Architecture). This began with playing with concepts like CG, exploring how to create an abstraction layer above their chips that could be expressed in a higher-level language <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. This initiative aimed to use GPUs for general-purpose computing tasks like CT reconstruction and image processing <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>.

While Nvidia invested thousands of person-years into building the CUDA platform, it was initially "ahead of the demand" for machine learning <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>. However, this foresight allowed them to democratize supercomputing, making CUDA applicable across various scientific fields, including molecular dynamics, imaging, seismic processing, weather simulations, and quantum chemistry <a class="yt-timestamp" data-t="18:48:58">[18:48:58]</a>.

## [[Nvidias role in the AI Revolution | Nvidia's Pivotal Role in AI]]
The moment that catalyzed Nvidia's current trajectory was the emergence of deep learning.
*   **AlexNet and Universal Function Approximators**: Upon seeing the "incredible effectiveness" of AlexNet in computer vision, Nvidia asked why it was so successful and if it was scalable <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>. They realized that deep learning had discovered a "universal function approximator" capable of making predictions from large example data, applicable to problems where causality doesn't matter as much as predictability (e.g., predicting toothpaste preference, music, weather, social media feeds) <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Transforming Computing**: This insight led to the realization that AI could affect "a very large part of the world's industries" <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>, and fundamentally change "how you build a computer and how you build a chip" <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.
*   **Deep Researcher Relationships**: Nvidia leveraged its existing relationships with university researchers, who were early adopters of CUDA, to assist every AI researcher on the planet in advancing their work <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>. This included pioneers like Yann LeCun, Andrew Ng, Geoff Hinton, and Ilya Sutskever <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>.
*   **Scaling Language Models**: Nvidia observed the "sensible" exponential progress in deep learning through papers and believed that large language models would scale by making data sets and models larger, leading to better results <a class="yt-timestamp" data-t="20:04:00">[20:04:00]</a>. The cleverness of self-supervised learning for predicting masked words in models like BERT suggested that reasoning could be encoded in language, leading to emergent capabilities <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>.

## [[Nvidias data center and hardware innovations | Expansion into the Data Center]]
Nvidia's venture into the data center began almost 17 years ago with the insight that separating computing from the viewing device would "explode" their market opportunity <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>. This vision led to three key product evolutions:
1.  **GeForce Now (GFN)**: Nvidia's first cloud product, started around 2006, focused on cloud gaming by capturing, encoding, and streaming frame buffers to a remote device <a class="yt-timestamp" data-t="35:59:00">[35:59:00]</a>. This taught them to build data center computers and overcome challenges like latency <a class="yt-timestamp" data-t="36:06:00">[36:06:00]</a>.
2.  **Remote Graphics**: Putting GPUs into enterprise data centers <a class="yt-timestamp" data-t="36:26:00">[36:26:00]</a>.
3.  **CUDA + GPU as Supercomputer**: Combining CUDA with their GPUs to create supercomputers <a class="yt-timestamp" data-t="36:33:00">[36:33:00]</a>.

### The Mellanox Acquisition
A pivotal strategic decision was the acquisition of Mellanox, a high-performance networking company <a class="yt-timestamp" data-t="39:44:00">[39:44:00]</a>. This was crucial for several reasons:
*   **Data Center Identity**: Nvidia concluded that to be a true data center company, they needed to be in networking, as data centers are distinguished by their networking infrastructure, not just the processing chip <a class="yt-timestamp" data-t="40:03:00">[40:03:00]</a>.
*   **Distributed AI Computing**: Unlike hyperscale cloud computing (virtualizing many users on commodity components), AI demands distributed computing where one job is orchestrated across millions of processors <a class="yt-timestamp" data-t="41:10:00">[41:10:00]</a>. This requires high-performance networking like InfiniBand, which Mellanox provided <a class="yt-timestamp" data-t="41:41:00">[41:41:00]</a>.
*   **Strategic Positioning**: This acquisition positioned Nvidia to meet the future demands of large language models (LLMs) and other AI workloads, recognizing that the market for intelligent work would be "enormous" and measured in trillions <a class="yt-timestamp" data-t="1:26:07">[1:26:07]</a>.

## Nvidia's Platform Strategy
Nvidia has always envisioned itself as a platform company. From day one, their architecture, initially called "Direct NV," aimed to enable developers to program to their chips, creating a platform similar to how game consoles rely on developers <a class="yt-timestamp" data-t="51:01:00">[51:01:00]</a>. This led to hiring a developer relations person very early on <a class="yt-timestamp" data-t="51:45:00">[51:45:00]</a>.

The company's [[key_technological_innovations_by_nvidia | core technological innovation]] and unwavering rule is architectural compatibility across all its accelerators <a class="yt-timestamp" data-t="53:51:00">[53:51:00]</a>. Every Nvidia chip, from early designs to the latest, runs CUDA <a class="yt-timestamp" data-t="54:41:00">[54:41:00]</a>. This consistent, compatible installed base of hundreds of millions of active CUDA GPUs <a class="yt-timestamp" data-t="53:57:00">[53:57:00]</a> is a key aspect of its platform strategy, fostering an ecosystem of developers and applications.

## Outlook on the Future
Nvidia operates by positioning itself in "zero billion dollar markets," anticipating needs that have not yet emerged <a class="yt-timestamp" data-t="46:40:53">[46:40:53]</a>. This strategy minimizes initial competition and allows them to shape and lead new markets, as seen in PC gaming, design workstations, supercomputing, and now AI <a class="yt-timestamp" data-t="47:49:00">[47:49:00]</a>. The company aims to operate about a decade in advance in these markets <a class="yt-timestamp" data-t="48:24:00">[48:24:00]</a>.

Nvidia's success is attributed to consistently building a network that enables other people and the ecosystem to succeed with them, rather than solely focusing on defensive "moats" <a class="yt-timestamp" data-t="49:15:00">[49:15:00]</a>.

Looking ahead, Nvidia believes that AI will drive "more ideas," leading to increased productivity, prosperity, and ultimately more jobs, as technology enables humans to "do more" with infinite ambition <a class="yt-timestamp" data-t="1:03:00">[1:03:00]</a>. The company sees its role in the "manufacturing of intelligence" and "manufacturing of work" as an enormous market opportunity, measured in trillions, a thousand times larger than being just a chip company <a class="yt-timestamp" data-t="1:25:56">[1:25:56]</a>.