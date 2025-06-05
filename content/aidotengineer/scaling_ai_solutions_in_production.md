---
title: Scaling AI solutions in production
videoId: kPL-6-9MVyA
---

From: [[aidotengineer]] <br/> 

D. Kila, CEO at Contextual AI, shares insights from his experience in enterprise AI, focusing on the challenges and opportunities in [[scaling_ai_agents_in_production | scaling AI agents]] and solutions for businesses <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Enterprise AI Paradox

While there is a significant opportunity with AI, estimated to add $4.4 trillion to the global economy according to McKenzie, many enterprises face frustration <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. A Forbes study indicates that only one in four businesses actually derive value from AI investments, leading to questions about ROI <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

This situation echoes Moravec's Paradox from robotics, where tasks seemingly hard for humans (like beating chess grandmasters) are easier for computers, while tasks easy for humans (like vacuuming a house or self-driving) are much harder <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. In enterprise AI, language models excel at complex tasks like code generation and mathematical problems <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. However, they struggle with "context," which humans effortlessly provide based on expertise and intuition <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### The Context Paradox and Differentiated Value

The "context paradox" is crucial for unlocking ROI with AI <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Current general-purpose AI assistants often focus on convenience <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. To achieve [[building_and_scaling_ai_use_cases_for_enterprises | differentiated value]] and business transformation, enterprises must become proficient at handling internal context <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Key Lessons for Building and Scaling AI Systems

Drawing from experience at Contextual AI, several [[best_practices_for_building_ai_systems | best practices for building AI systems]] have emerged:

### 1. Focus on Systems, Not Just Models
Language models typically constitute only about 20% of a complete enterprise AI deployment <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Retrieval Augmented Generation (RAG) has become the standard method for enabling generative AI to operate effectively on an organization's proprietary data <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. An effective RAG pipeline around a "mediocre" language model will outperform an "amazing" model with a poor RAG pipeline <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The focus should be on the entire system that solves the problem, not just the model <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 2. Prioritize Specialization Over AGI
Enterprise expertise is a valuable fuel for AI <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. While Artificial General Intelligence (AGI) has its applications, solving specific, difficult, domain-specific problems within an enterprise is best achieved through specialization, allowing the AI to better capture and utilize institutional knowledge <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### 3. Leverage Data as Your Moat
An enterprise's data is its long-term asset, even more so than its people <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The challenge is enabling AI to work on noisy data at scale <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Successfully doing so allows for the creation of [[building_and_scaling_ai_use_cases_for_enterprises | differentiated value]] and a competitive moat <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### 4. Design for Production from Day One
Pilots are relatively easy to build <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. [[challenges_and_solutions_in_scaling_ai_agents | Scaling AI models and their impact on development tools]] from a pilot (e.g., 10 users, a few documents) to production (e.g., thousands of users, millions of documents, 20,000 use cases) is significantly harder <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Existing open-source tools often struggle at this scale <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Enterprise requirements like security and compliance add further complexity <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Therefore, design for production from the outset to bridge the gap effectively <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### 5. Prioritize Speed Over Perfection
For successful production rollouts of RAG agents, speed is paramount <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Deploy solutions to real users early, even if they are only "barely functional" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. This enables iterative improvement ("hill climbing") to achieve a "good enough" state. Delaying for perfection can make the transition from pilot to production very difficult <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### 6. Empower Engineers to Focus on Value
Engineers should focus on delivering business value and competitive advantage, not on mundane tasks like optimizing chunking strategies or basic prompt engineering <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. State-of-the-art platforms for RAG agents can abstract away these lower-level concerns <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### 7. Make AI Easy to Consume
A common pitfall is that even when AI solutions run in production, internal usage can be zero <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Solutions must be integrated into existing workflows to maximize real production usage <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### 8. Design for "Wow" Moments and Sticky Usage
User adoption and stickiness are key <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. Design user onboarding experiences to deliver "wow" moments quickly, where users immediately grasp the value and potential of the AI <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. For example, a Qualcomm engineer found a 7-year-old hidden document through the system, answering long-standing questions and changing their workflow <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### 9. Manage Inaccuracy Through Observability
Accuracy is table stakes for AI <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. Enterprises are increasingly concerned with managing the 5-10% inaccuracy <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This requires robust observability, proper audit trails (especially in regulated industries), and attribution <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. In RAG systems, clear attribution of answers to source documents is vital for dealing with inaccuracies <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

### 10. Be Ambitious
Many AI projects fail not from aiming too high, but too low <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Projects that merely answer basic questions about HR policies, for instance, often lack significant ROI and become gimmicks <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. Enterprises should aim for ambitious goals that, if solved, deliver substantial ROI and drive business transformation <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. The current era of AI presents a unique opportunity to effect significant societal and business change <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

By understanding the "context paradox" and applying these lessons—focusing on systems, specializing for expertise, and being ambitious—enterprises can turn [[implementing_ai_in_enterprises | challenges and solutions in scaling AI agents]] into significant opportunities <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.