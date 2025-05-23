---
title: 25 Years at Google - Evolution and Impact
videoId: v0gjI__RyCY
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article with backlinks added:

Jeff Dean, Google's Chief Scientist, and Noam Shazeer, a key architect of modern Large Language Models (LLMs), have both been pivotal figures at Google for nearly 25 years. They are also two of the three co-leads of Gemini at Google DeepMind <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This article, based on a podcast discussion, explores their experiences, insights into Google's technological evolution, and perspectives on the future of AI.

## Early Days at Google

### Joining and Mentorship

Noam Shazeer joined Google at the end of 2000 and was mentored by Jeff Dean, who, according to Shazeer, "knew everything because he had basically written everything" at the company at that point <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> - <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Dean joined when Google had around 25-26 employees <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Losing Track of "Everything"

Dean described the process of a growing company where one gradually loses track of individual names, then all software engineers' names, then all projects. He humorously noted the point where an email announces "Project Platypus is launching on Friday," and one has no idea what it is <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> - <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. However, he emphasized the value of maintaining a high-level understanding and a strong internal network <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Recruitment

Jeff Dean initiated contact with Google himself <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Noam Shazeer first saw Google at a job fair in 1999 but didn't apply, assuming it was already too large. He sent a resume on a whim in 2000 because it was his favorite search engine <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> - <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. He was impressed by the smart people, a crayon chart showing exponential growth in search queries, and the interesting problems, initially planning to work there briefly to fund his AI research aspirations <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> - <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Shazeer rejoined Google in 2000, 2012 (joining Google Brain after a lunch with Jeff Dean), and 2024 <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a> - <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## Evolution of Systems and Hardware

### Moore's Law and Its Changing Impact

Dean noted that two decades ago, Moore's Law meant hardware rapidly improved every 18 months without effort. More recently, general-purpose CPU scaling has slowed, with fabrication improvements taking longer (e.g., three years instead of two) and architectural improvements yielding smaller boosts <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a> - <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. However, this has been offset by the rise of specialized computational devices like TPUs and ML-focused GPUs <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a> - <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Hardware-Algorithm Co-evolution

Shazeer explained that algorithms have followed hardware capabilities: arithmetic became very cheap, while data movement became comparatively expensive. This led to the rise of deep learning, heavily reliant on matrix multiplications (N<sup>3</sup> operations, N<sup>2</sup> data communication) <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a> - <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Dean highlighted the pivot to hardware like TPUs—reduced-precision linear algebra machines—as crucial <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> - <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Shazeer cited Larry Page's emphasis on opportunity costs, suggesting the missed opportunity was not filling chips with more arithmetic units <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a> - <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

The trend towards reduced precision in models and hardware is significant. TPUv1 was built around 8-bit integers for inference <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a> - <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Now, precisions like INT4, FP4, and even 1-bit or 2-bit quantization are being used for training and inference <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> - <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Shazeer stressed that this requires co-design: algorithm designers must understand the performance gains from lower precision to overcome the "irritation" of quantization <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a> - <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Pioneering AI and Language Models

### Jeff Dean's Early Work

In 1990, Jeff Dean's undergraduate honors thesis focused on parallelizing backpropagation for neural nets. He implemented model parallelism ("pattern partitioning") and data parallelism on a 32-processor Hypercube machine <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a> - <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. While excited by the abstraction, he realized much more compute (about a million times more) was needed for real-world problems, which became feasible around 2008-2010 <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a> - <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### The 2 Trillion Token N-gram Model (2007)

In 2007, Dean worked with Franz Och's machine translation team, which had won a DARPA contest but whose system took 12 hours to translate a sentence due to massive disk seeks in its language model <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a> - <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Dean spent months designing an in-memory compressed representation for 5-gram data from a 2 trillion-word web corpus, distributed across 200 machines. This reduced translation time to about 100 milliseconds <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a> - <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. This system was subsequently used for other applications like query completion <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Early Language Modeling Applications

Noam Shazeer built an impressive spelling correction system around 2000-2001, which Dean recalled handling highly butchered queries like "scrumbled uggs Bundict" for "scrambled eggs benedict" <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a> - <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. Shazeer noted that language modeling—predicting the next word—was an ideal problem due to its simple statement, nearly infinite self-supervised training data from the web, and its AI-complete nature <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a> - <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

### The "Cat Detector" and Scaling Neural Nets

In the early days of the Google Brain team (around 2012), they built infrastructure for training large neural nets on CPUs. An unsupervised learning system trained on 10 million YouTube frames using 16,000 CPU cores developed a neuron that specifically activated for images of cats, without ever being explicitly told what a cat was <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a> - <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>. This model, about 50x larger than previous ones, significantly advanced the state of the art on the ImageNet 20,000 category challenge, reinforcing the idea that scaling up neural nets was a fruitful direction <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a> - <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.

## Google's Mission and AI's Expanding Role

Dean described Google's mission as "organizing the world's information and making it universally accessible and useful" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This has evolved to include not just information retrieval but also _creating_ new information based on user guidance, such as drafting letters or summarizing videos <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a> - <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. He emphasized the importance of multimodal capabilities—understanding text, images, video, audio, and even non-human-oriented data like lidar, genomic, or health information—to extract useful insights <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a> - <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. A key goal is making all information usable by anyone, regardless of language <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a> - <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.

## The Future of AI Development

### Longer Context Windows

A significant challenge is extending the context window of LLMs. While current models handle millions of tokens (hundreds of PDF pages, hours of video), the aspiration is to attend to trillions of tokens—the entire internet or all of a user's personal data (emails, documents, photos) <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a> - <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>. This is computationally difficult due to the quadratic nature of naive attention algorithms, necessitating algorithmic approximations <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a> - <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>. Shazeer noted the memory inefficiency of tokens in context compared to model parameters [[understanding_and_leveraging_long_context_lengths_in_llms]] <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a> - <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.

### AI-Assisted Coding and Research

Google has already further trained a Gemini model on its internal codebase, with AI-generated code (with human oversight) accounting for 25% of characters checked into the codebase [[impact_of_ai_on_software_development_and_productivity]] <a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a> - <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. Dean mentioned an experimental coding model that, from a simple prompt, generated a C-based SQL processing database system with a parser, tokenizer, query planner, and storage format <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a> - <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. They envision AI systems that can explore research ideas, generate experimental code, and manage complex workflows with intermittent human input <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a> - <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>, <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>.

### The AI-Improving-AI Feedback Loop

#### Algorithmic Advancements

Dean emphasized that generational improvements in AI models are driven as much, or more, by algorithmic improvements and changes in architecture/data mix as by hardware/scale <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a> - <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>. Automated exploration of ideas could vet more concepts and accelerate this process, allowing researchers to steer rather than hand-babysit experiments <a class="yt-timestamp" data-t="00:46:54">[00:46:54]</a> - <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>. Shazeer added that with vast compute, trying numerous ideas (e.g., 100,000 ideas on a 1/1000th scale problem) could lead to more breakthroughs [[ai_scalability_and_breakthroughs]] <a class="yt-timestamp" data-t="00:42:37">[00:42:37]</a> - <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.

#### Accelerating Chip Design

Dean discussed the potential to dramatically speed up chip design using AI. The current 18-month design cycle (before 4-month fabrication) could potentially be shrunk to a few people using an automated search process, making fab time the dominant portion [[innovations_and_challenges_in_ai_hardware]] <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a> - <a class="yt-timestamp" data-t="00:50:11">[00:50:11]</a>. This would enable more rapid hardware iteration and specialization, better aligning hardware with current ML algorithms <a class="yt-timestamp" data-t="00:50:19">[00:50:19]</a> - <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>.

### Inference-Time Compute

Shazeer highlighted the vast headroom for increasing inference-time compute ("think harder"). Comparing the cost of LLM tokens to reading a paperback or hiring a professional shows that current AI is significantly cheaper, allowing for more computation to achieve smarter results <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a> - <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>. Dean added that having a dial to trade more inference compute for better answers is desirable, with techniques like iterative exploration and search (per Rich Sutton's "Bitter Lesson") being key [[ai_alignment_and_safety_concerns]] <a class="yt-timestamp" data-t="00:55:04">[00:55:04]</a> - <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>. Specialized hardware for inference, like the first TPU, might see a resurgence [[machine_learning_hardware_and_tpus]] <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a> - <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>. Algorithmic improvements like drafter models (a small model proposes tokens for a large model to verify) also boost inference efficiency <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a> - <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>.

## Infrastructure and Training

### Data Center Planning and Multi-Data Center Training

Google is already conducting multi-data center training [[data_center_energy_requirements_and_scaling]]. The Gemini 1.5 tech report mentioned using multiple metro areas connected by long-latency, high-bandwidth links <a class="yt-timestamp" data-t="01:03:10">[01:03:10]</a> - <a class="yt-timestamp" data-t="01:03:27">[01:03:27]</a>. For training, as long as parameter synchronization and gradient accumulation fit within the step time (often a few seconds), inter-data center latency is manageable <a class="yt-timestamp" data-t="01:03:33">[01:03:33]</a> - <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a>. Future compute demand is expected to be astronomical, driven by wider adoption, more intensive use per user, and more powerful (and potentially inference-heavy) models <a class="yt-timestamp" data-t="01:28:31">[01:28:31]</a> - <a class="yt-timestamp" data-t="01:32:34">[01:32:34]</a>.

### Synchronous vs. Asynchronous Training

Early Google Brain work used asynchronous training on CPUs, where model copies updated parameters independently. This allowed scaling but made experiments less replicable <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a> - <a class="yt-timestamp" data-t="01:04:32">[01:04:32]</a>. The advent of fast TPU pods with high inter-chip bandwidth led to a preference for fully synchronous training, which is easier to manage mentally <a class="yt-timestamp" data-t="01:04:35">[01:04:35]</a> - <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>, <a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a> - <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>. However, Dean suggested that as scale increases further, a push towards more asynchrony might occur, perhaps with methods to ensure replicability like recording the sequence of operations <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a> <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a> - <a class="yt-timestamp" data-t="01:05:29">[01:05:29]</a>.

### Debugging and Iteration

Debugging large-scale neural net training is challenging because models are tolerant of noise and can even learn around bugs, which sometimes leads to worse, or surprisingly, better results <a class="yt-timestamp" data-t="01:07:46">[01:07:46]</a> - <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. Research involves small-scale experiments to invent improvements, followed by scaling and integration to see how they interact. Shazeer estimated that interactions cause issues about 50% of the time when stacking improvements <a class="yt-timestamp" data-t="01:08:33">[01:08:33]</a> - <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>. Complexity in the codebase and algorithms is a constant concern [[challenges_and_methodologies_in_ai_research_and_development]] <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a> - <a class="yt-timestamp" data-t="01:11:24">[01:11:24]</a>.

## Continual Learning and Modular AI (Pathways Vision)

### The Concept

Dean has long advocated for more "organic," less rigidly structured ML models, drawing inspiration from specialized brain areas <a class="yt-timestamp" data-t="01:53:23">[01:53:23]</a> - <a class="yt-timestamp" data-t="01:54:24">[01:54:24]</a>. This involves:

- **Sparsity and Mixture of Experts (MoE):** Different parts of the model specialize in different tasks (e.g., math vs. cat images) <a class="yt-timestamp" data-t="01:34:38">[01:34:38]</a> - <a class="yt-timestamp" data-t="01:35:08">[01:35:08]</a>. Current MoE models are still very regular; the vision is for more varied expert sizes and non-merging branches <a class="yt-timestamp" data-t="01:35:26">[01:35:26]</a> - <a class="yt-timestamp" data-t="01:35:43">[01:35:43]</a>.
- **Independent Module Development:** Small teams could develop specialized modules (e.g., for Southeast Asian languages or Haskell code reasoning) that can be plugged into a larger model <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a> - <a class="yt-timestamp" data-t="01:36:41">[01:36:41]</a>. This decomposes the problem and allows for parallel development <a class="yt-timestamp" data-t="01:36:53">[01:36:53]</a> - <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>.
- **Adaptive Connectivity:** Model connectivity could adapt to hardware hierarchy: dense connections within a chip, sparser connections to nearby chips, and even sparser, bottlenecked connections across pods or metro areas <a class="yt-timestamp" data-t="01:54:46">[01:54:46]</a> - <a class="yt-timestamp" data-t="01:55:39">[01:55:39]</a>.

### Benefits and Challenges

Benefits include improved quality, parallelizable development, faster research by upgrading modules cheaply, and fine-grained data control (e.g., personal modules, data restricted to certain uses) <a class="yt-timestamp" data-t="01:38:56">[01:38:56]</a> - <a class="yt-timestamp" data-t="01:39:17">[01:39:17]</a>, <a class="yt-timestamp" data-t="01:51:56">[01:51:56]</a> - <a class="yt-timestamp" data-t="01:52:48">[01:52:48]</a>. Challenges include moving away from current monolithic development and scientifically validating the benefits <a class="yt-timestamp" data-t="01:51:35">[01:51:35]</a> - <a class="yt-timestamp" data-t="01:52:15">[01:52:15]</a>. Distillation is a key tool for transforming models between architectures or creating efficient serving versions from larger, organic models <a class="yt-timestamp" data-t="01:41:18">[01:41:18]</a>, <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a> - <a class="yt-timestamp" data-t="01:57:45">[01:57:45]</a>.

### Implications for Infrastructure and Research

The Pathways system was designed to support such twisty, asynchronous models, though these capabilities are not fully utilized by current Gemini models <a class="yt-timestamp" data-t="01:39:53">[01:39:53]</a> - <a class="yt-timestamp" data-t="01:40:14">[01:40:14]</a>. Such an architecture would leverage large, interconnected hardware like TPU pods <a class="yt-timestamp" data-t="01:45:15">[01:45:15]</a>. Shazeer noted that MoE serving requires all experts in memory due to large batch sizes of independent requests, with different parts of the batch routed through different experts <a class="yt-timestamp" data-t="01:45:28">[01:45:28]</a> - <a class="yt-timestamp" data-t="01:47:01">[01:47:01]</a>. Future systems might feature experts of vastly different computational costs, requiring asynchronous inference <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a> - <a class="yt-timestamp" data-t="01:47:57">[01:47:57]</a>.

## Reflections and Perspectives

### Publication Strategy

Google's publication strategy varies. The Transformer paper was openly published <a class="yt-timestamp" data-t="02:03:22">[02:03:22]</a>. For other innovations, like in Pixel computational photography, techniques are often productized first, then published <a class="yt-timestamp" data-t="02:05:17">[02:05:17]</a> - <a class="yt-timestamp" data-t="02:05:44">[02:05:44]</a>. Some critical developments might not be published at all, while others are shared to advance the field <a class="yt-timestamp" data-t="02:05:52">[02:05:52]</a> - <a class="yt-timestamp" data-t="02:06:28">[02:06:28]</a>.

### Google's AI Journey and Competition

Dean acknowledged that while Google had early language model work (Meena chatbot internally pre-ChatGPT <a class="yt-timestamp" data-t="02:07:44">[02:07:44]</a> - <a class="yt-timestamp" data-t="02:08:14">[02:08:14]</a>), their search-centric view focused heavily on factuality and safety, as early models hallucinated and had safety issues <a class="yt-timestamp" data-t="02:08:14">[02:08:14]</a> - <a class="yt-timestamp" data-t="02:09:04">[02:09:04]</a>. They perhaps underestimated the utility of chatbots for non-search tasks (e.g., drafting notes, summarization) <a class="yt-timestamp" data-t="02:09:04">[02:09:04]</a> - <a class="yt-timestamp" data-t="02:09:29">[02:09:29]</a>.

### Career Longevity and Breadth

Dean attributed his longevity and breadth to diving into new areas, working with colleagues with diverse expertise, and continuous on-the-job learning [[jeff_dean_and_noam_shazeers_contributions_to_ai]] <a class="yt-timestamp" data-t="02:10:43">[02:10:43]</a> - <a class="yt-timestamp" data-t="02:11:57">[02:11:57]</a>. He also maintains a slide deck of "Go, Jeff, Wacky Ideas" to bootstrap new directions <a class="yt-timestamp" data-t="02:14:42">[02:14:42]</a> - <a class="yt-timestamp" data-t="02:15:10">[02:15:10]</a>. Shazeer emphasized humility, being willing to drop ideas for better ones, and an environment that incentivizes both collaboration and flexibility (balancing top-down and bottom-up resource allocation) <a class="yt-timestamp" data-t="02:12:02">[02:12:02]</a> - <a class="yt-timestamp" data-t="02:14:35">[02:14:35]</a>.

### Nostalgia and Current Excitement

Dean fondly recalled the early years of Google working on search and indexing with tremendous traffic growth [[the_evolution_and_future_of_the_tech_industry]] <a class="yt-timestamp" data-t="02:04:34">[02:04:34]</a> - <a class="yt-timestamp" data-t="02:24:57">[02:24:57]</a>. Both he and Shazeer expressed equal excitement about the current Gemini team and the rapid progress in model capabilities, often congregating in a micro-kitchen area dubbed "Gradient Canopy" for informal collaboration <a class="yt-timestamp" data-t="02:25:10">[02:25:10]</a> - <a class="yt-timestamp" data-t="02:27:46">[02:27:46]</a>.

## Addressing Rapid AI Advancement

Shazeer anticipates significant acceleration in AI capabilities. Dean expects models a few generations from now to be capable of breaking down very high-level tasks into 100-1,000 steps with high accuracy, a major step up from current abilities <a class="yt-timestamp" data-t="01:14:08">[01:14:08]</a> - <a class="yt-timestamp" data-t="01:14:29">[01:14:29]</a>. He stressed the importance of understanding these trends, maximizing societal benefits (e.g., education, healthcare), and mitigating risks (e.g., misinformation, automated hacking) through safeguards and frameworks like Google's Responsible AI principles [[ai_alignment_and_safety]] <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a> - <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>.

Dean advocated for "shaping AI" development (referencing a co-authored paper) rather than a laissez-faire approach, engineering safe systems, and steering AI towards beneficial applications while using technical and policy measures to avoid negative outcomes [[impact_of_ai_on_future_technology_and_society]] <a class="yt-timestamp" data-t="01:17:21">[01:17:21]</a> - <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>. Shazeer believes language models' ability to analyze output will be key to control issues. Both emphasized human oversight, especially as AI helps in its own research, and using APIs to control how model capabilities are exposed and used <a class="yt-timestamp" data-t="01:21:45">[01:21:45]</a> - <a class="yt-timestamp" data-t="01:23:41">[01:23:41]</a>.
