---
title: Importance of system thinking over model thinking in RAG systems
videoId: kPL-6-9MVyA
---

From: [[aidotengineer]] <br/> 

D. Kiela, CEO at Contextual AI and a pioneer of RAG at Facebook AI Research, emphasizes that focusing on the entire system rather than just the language model is crucial for successful AI deployment in enterprises, especially for RAG agents in production <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Enterprise AI Paradox

While there's an estimated $4.4 trillion added value to the global economy from AI, according to McKinsey, many enterprises experience frustration, with only one in four businesses actually getting value from AI <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This creates a paradox.

### Moravec's Paradox in AI
Drawing a parallel to Moravec's Paradox in robotics—where beating humans at chess was easier than vacuum cleaning a house—a similar "context paradox" exists in Enterprise AI <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Large Language Models (LLMs) excel at tasks like generating code or solving mathematical problems, which seem complex to humans <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. However, they struggle with putting information into the right context, a task humans perform effortlessly using intuition and expertise <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

The "context paradox" is key to unlocking ROI with AI <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Current general-purpose assistants offer convenience, but true business transformation and "differentiated value" require much better handling of enterprise-specific context <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Systems, Not Just Models

A core lesson is that while language models are powerful, they often constitute only 20% of a larger system in an Enterprise AI deployment <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Such deployments are typically built as a [[components_of_rag_stack | RAG system]] (Retrieval Augmented Generation), a method originally pioneered by Kiela and his team at Facebook AI Research <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

> A "mediocre language model" surrounded by an "amazing RAG pipeline" will outperform an "amazing language model" with a "terrible RAG pipeline" <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

Therefore, the focus should be on designing the entire system that solves the problem, not just on the language model itself <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Key Observations for Production RAG Systems

### 1. Specialization Over AGI
Enterprises should aim to specialize their AI solutions to capture and leverage their unique institutional knowledge and expertise <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. While Artificial General Intelligence (AGI) has its uses, solving specific, difficult, domain-specific problems is more effectively achieved through specialization <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### 2. Data as Your Moat
A company's enduring asset is its data <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The ability to make AI work effectively on noisy, real-world data at scale is incredibly difficult but creates differentiated value and a competitive "moat" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### 3. Design for Production from Day One
Building a pilot RAG system is relatively easy <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. However, scaling it to millions of documents, thousands of users, and numerous use cases, while meeting enterprise security and compliance requirements, is far more challenging <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Success hinges on designing for production from the outset, not just for a pilot <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### 4. Speed Over Perfection
In production rollouts of RAG agents, speed is paramount <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Getting a barely functional solution to real users early for feedback allows for iterative improvement and "Hill Climbing" to a "good enough" level, avoiding delays caused by striving for initial perfection <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### 5. Empower Engineers
Engineers should focus on delivering business value and differentiated solutions, rather than spending time on tedious tasks like optimizing chunking strategies or basic prompt engineering <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. These foundational tasks can be abstracted away by state-of-the-art platforms for RAG agents <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### 6. Make AI Easy to Consume
A common issue is that GenAI running in production is barely used <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Success requires making solutions easy to consume and integrating them closely into existing enterprise workflows, ensuring actual adoption and usage <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

### 7. Engineer for "Wow" Moments
Getting users to quickly experience a "spark" or "wow" moment with the AI system is crucial for sticky usage and evangelism <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. An example from Qualcomm illustrated a customer engineer finding a seven-year-old hidden document that answered long-standing questions, profoundly impacting their work <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### 8. Focus on Inaccuracy (Observability)
While accuracy is a minimum requirement, dealing with the inevitable 5-10% inaccuracy is critical <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This involves robust observability, proper audit trails (especially in regulated industries), and attribution in [[components_of_rag_stack | RAG systems]] to show *why* an answer was generated <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. Post-processing to check claims and ensure proper attributions is key <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

### 9. Be Ambitious
Projects often fail not from aiming too high, but too low <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Aiming for basic Q&A on simple topics will not yield significant ROI <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. Enterprises should be ambitious and target problems that, if solved, will deliver substantial business value and truly transform the organization <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

By understanding the context paradox and applying these lessons—building better systems, specializing for expertise, and being ambitious—enterprises can turn challenges into opportunities in AI <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.