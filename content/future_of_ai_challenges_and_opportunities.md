---
title: Future of AI - Challenges and Opportunities
videoId: v0gjI__RyCY
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article summarizes insights from a podcast discussion featuring Jeff Dean, Google's Chief Scientist, and Noam Shazeer, a key inventor in modern AI, both co-leads of [[jeff_dean_and_noam_shazeers_contributions_to_ai | Gemini]] at Google DeepMind. It focuses on their perspectives regarding the future trajectory of AI, its potential capabilities, and the associated challenges.

## Key Drivers of AI Progress

The development of AI has been significantly influenced by advancements in both hardware and algorithms.

### The Shifting Landscape of Hardware Advancement

Jeff Dean notes that two decades ago, Moore's Law provided rapid hardware improvements without requiring significant algorithmic changes <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. However, in the last decade, general-purpose CPU scaling has slowed <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. This has led to a rise in specialized computational devices like Machine Learning accelerators (TPUs) and ML-focused GPUs, which offer high performance for modern AI computations <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

Noam Shazeer highlights that algorithms have followed hardware trends: arithmetic has become very cheap, while data movement is comparatively expensive <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Deep learning, built on matrix multiplications (N-cubed operations with N-squared data communication), has thrived in this environment <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The development of TPUs, essentially reduced-precision linear algebra machines, was a pivotal transition <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This hardware encouraged filling chip areas with arithmetic units, further enabled by the acceptability of low-precision arithmetic for AI tasks <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Co-design of Algorithms and Hardware

A crucial trend is the increasing use of reduced precision in models. TPUv1 was built around 8-bit integers for inference <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>, and now precisions like INT4, FP4, or even 1-bit or 2-bit are being used for inference and training <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Shazeer emphasizes that this requires a co-design approach: algorithm designers must see the performance benefits of lower precision to overcome the perceived risks and irritation, enabling chip designers to build more efficient hardware <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

## Expanding AI Capabilities

AI models are evolving beyond information retrieval to perform complex tasks like code generation and in-depth analysis.

### Longer Context Windows

A significant area of development is expanding the context window AI models can process. Jeff Dean explains that while model parameters store vast amounts of "squishy" information from training data, information within the context window is "sharp and clear" due to attention mechanisms <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. Current models can handle millions of tokens (hundreds of PDF pages, hours of video) <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>. The aspiration is for models to attend to trillions of tokens, such as the entire internet or a user's complete personal data (emails, documents, photos) <a class="yt-timestamp" data-t="00:33:56">[00:33:56]</a>. This presents a computational challenge due to the quadratic nature of naive attention, necessitating algorithmic approximations <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a>. Noam Shazeer notes the memory inefficiency of tokens in context compared to model parameters and the ongoing innovation to minimize this <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.

### AI in Software Development and Research

AI models are already augmenting software development. Google has further trained Gemini on its internal codebase, and Sundar Pichai has stated that 25% of characters checked into Google's codebase are AI-generated with human oversight <a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a>. Dean envisions AI assisting researchers by taking high-level ideas (e.g., "explore an idea similar to this paper but make it convolutional") and automatically generating experimental code <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>. He cites an example of an experimental coding model implementing a SQL processing database system in C from a paragraph prompt, highlighting the potential for massive productivity boosts <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>. Future systems might handle more complex, longer-running tasks with intermittent human input <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>.

## The Accelerating Pace of AI Development

A key theme is the potential for AI to accelerate its own development through various feedback loops.

### Algorithmic Improvements Driven by AI

Noam Shazeer suggests that the ability to try a vast number of experiments (millions) could lead to breakthroughs more frequently <a class="yt-timestamp" data-t="00:42:37">[00:42:37]</a>, especially if AI systems can automate the exploration of ideas <a class="yt-timestamp" data-t="00:46:54">[00:46:54]</a>. This would allow human researchers to steer a more automated search process, vetting ideas at small scale before scaling up, potentially 100 times faster than current methods <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>. Jeff Dean concurs, noting that generational improvements in models are driven as much by [[ai_scalability_and_breakthroughs | algorithmic and architectural changes]] as by hardware <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>.

### AI-Driven Hardware Design

Jeff Dean is excited about dramatically speeding up the chip design process, currently an 18-month cycle from concept to TSMC handover, followed by a 4-month fabrication <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>. If AI could shrink the design phase from 12-18 months with 150 people to a few people with an automated search process, it would allow for more rapid exploration and specialization <a class="yt-timestamp" data-t="00:49:45">[00:49:45]</a>. This shorter design cycle (e.g., 6-9 months instead of 2-2.5 years) would align hardware better with current ML algorithms <a class="yt-timestamp" data-t="00:50:41">[00:50:41]</a>. While fabrication time (3-5 months for leading-edge nodes) remains a bottleneck <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>, it's comparable to large training runs.

### The Feedback Loop and Its Implications

The combination of AI improving algorithms and AI accelerating hardware design creates a powerful feedback loop. This could lead to a rapid increase in AI capabilities, potentially moving from "pretty good ML researcher" to "superhuman intelligence" more quickly than linear projections suggest <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>. Dean anticipates models two to three generations from now will be capable of breaking down very high-level tasks into 100s or 1000s of steps with high accuracy, a major step up from current abilities <a class="yt-timestamp" data-t="01:14:08">[01:14:08]</a>. Shazeer acknowledges the possibility of an [[intelligence_explosion_and_ai_feedback_loops | "explosion of capabilities"]] <a class="yt-timestamp" data-t="01:13:42">[01:13:42]</a>.

## Harnessing Inference Power

Significant improvements are expected from applying more compute at inference time.

### "Thinking Harder" at Inference

Noam Shazeer argues there's huge headroom to make models smarter by making them more computationally expensive at inference, as current costs per token are extremely low compared to alternatives like reading a book or human labor <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>. He predicts an "explosion" in capabilities by allowing models to "think harder" <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>. Jeff Dean adds that this involves models actively exploring solutions, performing searches, and iteratively refining answers <a class="yt-timestamp" data-t="00:55:04">[00:55:04]</a>. This creates a trade-off: more compute for better answers, allowing users to dial up "thinking" for important problems <a class="yt-timestamp" data-t="00:55:33">[00:55:33]</a>. Rich Sutton's [[the_role_of_deep_learning_and_discrete_program_search_in_ai_development | "Bitter Lesson"]] is invoked, emphasizing learning and search as highly effective, scalable techniques <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.

### Specialized Hardware and Efficient Inference

The growing importance of inference compute may drive further hardware specialization <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>. Algorithmic improvements like using "drafter models" (small models proposing tokens for a larger verifier model) can also significantly boost inference efficiency by enabling parallel computation over multiple tokens <a class="yt-timestamp" data-t="01:01:46">[01:01:46]</a>.

### Asynchronous vs. Synchronous Processing

The nature of inference tasks (latency-sensitive vs. background batch processing) will influence infrastructure design <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a>. Complex, asynchronous tasks (e.g., researching and writing an 8-page report) that take minutes are emerging <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>, requiring new UI/UX for managing interactions. For training, Google already performs multi-data center training synchronously, feasible as long as inter-datacenter communication for parameter syncing is fast relative to the step time <a class="yt-timestamp" data-t="01:03:10">[01:03:10]</a>. While synchronous training offers replicability <a class="yt-timestamp" data-t="01:04:35">[01:04:35]</a>, future scaling might necessitate more asynchrony <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>.

## Evolving Model Architectures: Towards Continual and Modular Learning

A significant future direction involves moving away from monolithic models towards more organic, modular, and continually learning systems.

### Sparsity and Mixture of Experts (MoE)

Jeff Dean is a proponent of sparse models, where different parts specialize in different tasks (e.g., math vs. cat images), as seen in MoE models like Gemini 1.5 Pro <a class="yt-timestamp" data-t="01:34:38">[01:34:38]</a>. Current MoE models still have a regular structure with same-sized experts and rapid path merging. Dean envisions a more "organic structure" with varying expert sizes and branching paths that don't always merge <a class="yt-timestamp" data-t="01:35:26">[01:35:26]</a>.

### Modular Development and Continual Learning

Dean proposes that pieces of a model could be developed independently by specialized teams (e.g., for specific languages or coding in Haskell) and then "hooked up" to a larger model <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. This modularity offers software engineering benefits, decomposing the problem and allowing parallel development by many teams globally <a class="yt-timestamp" data-t="01:36:53">[01:36:53]</a>. This forms a type of continual learning where modules can be upgraded or added without retraining the entire system from scratch <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>. This vision, part of the original Pathways concept <a class="yt-timestamp" data-t="01:39:48">[01:39:48]</a>, could enable faster research progress through cheaper, targeted improvements <a class="yt-timestamp" data-t="01:38:56">[01:38:56]</a>.

### Distillation and Dynamic Routing

Distillation is seen as a key tool to transform modules into different architectures or to create smaller, efficient versions for serving <a class="yt-timestamp" data-t="01:41:18">[01:41:18]</a>. A continual process could involve growing a module, then distilling it to a smaller version, deleting the large one, and adding new capacity to learn more, repeated across the model <a class="yt-timestamp" data-t="01:41:45">[01:41:45]</a>. This could also enable dynamic routing for inference scaling, where a router decides whether to use a large or small/distilled version of an expert based on task difficulty <a class="yt-timestamp" data-t="01:42:25">[01:42:25]</a>.

### Organic Growth and Hardware Adaptation

Dean's long-term vision is for models whose connectivity adapts to hardware topology: dense connections within a chip, fewer to nearby chips, and very limited, salient information passed across pods or metro areas <a class="yt-timestamp" data-t="01:54:04">[01:54:04]</a>. This "organic" growth, potentially dictated by hardware communication latencies, would be a departure from current carefully constructed architectures <a class="yt-timestamp" data-t="01:55:39">[01:55:39]</a>. Such a "blob" model could activate different or larger patterns of itself based on the desired computational output, rather than instantiating multiple separate agents <a class="yt-timestamp" data-t="01:56:24">[01:56:24]</a>.

### Data Efficiency and Learning Objectives

Current models are not as sample-efficient as humans. Dean suggests changing training objectives beyond simple next-token prediction, perhaps incorporating learning from answering questions after reading material, or learning more from visual data and interaction with the world (akin to how infants learn) <a class="yt-timestamp" data-t="02:00:44">[02:00:44]</a>. Noam Shazeer adds that learning can occur through self-play (like AlphaZero for chess) or even "thought experiments" without external data, suggesting models could talk to themselves to become smarter <a class="yt-timestamp" data-t="02:02:15">[02:02:15]</a>. There's also potential to extract more value from existing text data by forcing models to "work harder" on certain tokens or using techniques like dropout over many epochs <a class="yt-timestamp" data-t="01:58:07">[01:58:07]</a>, <a class="yt-timestamp" data-t="01:59:19">[01:59:19]</a>.

## Challenges and Safeguards

The increasing power of AI necessitates careful consideration of safety and societal impact.

### Addressing Misinformation and Misuse

Jeff Dean acknowledges that early models hallucinated and had safety issues (e.g., saying offensive things), which delayed their release <a class="yt-timestamp" data-t="02:08:22">[02:08:22]</a>. As models become more capable, they could be used for misinformation or automated hacking. Google's Responsible AI principles provide a framework for navigating these trade-offs <a class="yt-timestamp" data-t="01:15:03">[01:15:03]</a>.

### Shaping AI Development

Dean advocates for "shaping and steering" AI deployment to maximize benefits (e.g., in education, healthcare) and mitigate risks, rather than a laissez-faire approach <a class="yt-timestamp" data-t="01:17:21">[01:17:21]</a>. This involves engineering safe systems, potentially learning from rigorous software development practices in fields like aviation <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.

### The Role of AI in Ensuring Safety

Noam Shazeer believes that AI's ability to analyze language model output will be key to solving control issues, as recognizing problematic content is often easier than generating it <a class="yt-timestamp" data-t="01:19:06">[01:19:06]</a>. Systems will be used to check themselves and other systems <a class="yt-timestamp" data-t="02:03:02">[02:03:02]</a>.

### Human Oversight in an Accelerating Loop

With AI potentially contributing to its own research and code generation, maintaining human oversight is crucial <a class="yt-timestamp" data-t="01:21:45">[01:21:45]</a>. Dean suggests that humans would still decide which AI-explored algorithmic ideas are incorporated into core systems <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>. Exposing model capabilities through APIs with defined boundaries is another tool for control <a class="yt-timestamp" data-t="01:23:20">[01:23:20]</a>. The goal is to empower people while preventing misuse, like the creation of "a million evil software engineers" <a class="yt-timestamp" data-t="01:24:06">[01:24:06]</a>.

## The Research and Development Landscape

The way AI research is conducted is also evolving.

### Publication and Competitive Dynamics

Historically, Google has been generous with publishing research like the Transformer paper <a class="yt-timestamp" data-t="02:03:22">[02:03:22]</a>. Noam Shazeer reflects that this openness helped spur the field, and since the AI "pie" is not fixed but rapidly growing, this has been beneficial <a class="yt-timestamp" data-t="02:04:09">[02:04:09]</a>. Jeff Dean notes a more nuanced approach now: some critical developments might not be published, others published after product release (like computational photography techniques), and many still shared openly to advance the community <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

### Resource Allocation and Incentives

Noam Shazeer discusses the shift from Google Brain's bottom-up "UBI for chips" model, which incentivized flexibility and dropping unpromising ideas <a class="yt-timestamp" data-t="02:13:21">[02:13:21]</a>, to Gemini's more top-down approach, fostering collaboration but potentially incentivizing researchers to always present their work as successful <a class="yt-timestamp" data-t="02:13:40">[02:13:40]</a>. A future balance of top-down and bottom-up approaches is envisioned to incentivize both collaboration and the flexibility to abandon failing projects <a class="yt-timestamp" data-t="02:14:29">[02:14:29]</a>.

## Looking Ahead: Compute Demand and Vision

The future demand for AI compute is expected to be astronomical.

### Exponential Growth in Compute Needs

Jeff Dean outlines several factors driving up inference compute demand: techniques to improve quality by scaling inference compute ([[role_of_compute_in_ai_development | potentially 100-1000x per request]]), wider adoption of AI interfaces (10-100x), and larger models themselves (another 10-100x) <a class="yt-timestamp" data-t="01:28:31">[01:28:31]</a>. Noam Shazeer envisions a future where AI, perhaps as a personal assistant integrated into daily life and work, becomes so valuable that individuals and society will spend a significant fraction of a vastly increased world GDP on it, limited perhaps only by energy availability and the ability to build data centers <a class="yt-timestamp" data-t="01:30:01">[01:30:01]</a>. This necessitates extremely efficient hardware and model co-design to make these capabilities accessible <a class="yt-timestamp" data-t="01:32:56">[01:32:56]</a>.
