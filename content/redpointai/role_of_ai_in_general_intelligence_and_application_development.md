---
title: Role of AI in general intelligence and application development
videoId: atMRWzgHEGg
---

From: [[redpointai]] <br/> 

Noam Shazeer and Jack Rae, at the forefront of Google's Gemini LLM efforts and key contributors to AI discoveries in the last decade, discuss the advancements, challenges, and future direction of AI, particularly concerning general intelligence and application development <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Milestones and Progress in AI

A significant milestone for AI is when a model like Gemini 3.0 can write Gemini 4.0, representing a reinforcement loop where AI builds upon itself <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This concept of AI creating the next better AI, particularly an automated software engineer or researcher, is seen as crucial for self-acceleration <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. The "mom vibe check" serves as the ultimate test for AI's transition from the "Twitter sphere" to the real world <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

### Gemini Models and "Thinking"
The Gemini 2.0 models, especially Gemini Flash, initially focused on reasoning tasks like math and code <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. A surprising discovery was the models' ability to generalize "thinking" to creative tasks, such as composing essays, where the thought process and revisions were valuable to observe <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The latest Gemini app integration with "thinking" models, while introducing slight latency, offers better quality answers that users appreciate <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>.

### Multimodal Capabilities
The multimodal capabilities of Gemini, particularly with image input and "thinking," are remarkably strong but remain underexplored from an application perspective <a class="yt-timestamp" data-t="01:13:41">[01:13:41]</a>, <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>. Integrating multimodal understanding with agentic tasks, like the Mariner agent that uses a browser and understands web screens, is a very exciting development <a class="yt-timestamp" data-t="01:14:25">[01:14:25]</a>. Historically, text-based models were prioritized due to text's information density and abundant training data compared to image generation <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.

## Challenges in AI Development and Evaluation

### Evolving Benchmarks
AI evaluations constantly evolve as models quickly saturate existing benchmarks <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. What was once considered challenging becomes trivial within months <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The issue of "leaked" evals also renders them useless once models learn the problems <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. There is a need for new, incrementally harder benchmarks, especially in areas like math, to bridge the gap from competitive exams to generating useful scientific contributions <a class="yt-timestamp" data-t="02:00:54">[02:00:54]</a>.

### Reliability and Complexity
For agents to be widely adopted, issues of reasoning complexity and reliability must be solved <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>. The path forward includes making models smarter and developing general solutions for control problems, as users will employ AI in unforeseen ways <a class="yt-timestamp" data-t="01:06:20">[01:06:20]</a>, <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>.

## The Role of AI in Application Development

### Enhancing Software Development
AI is already being integrated into development tooling at Google, assisting with pull requests, bug fixes, and code reviews <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. The potential for [[advancements_in_ai_developer_tools | agentic coding]] is significant, enabling models to tackle more open-ended and difficult tasks <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. The structured monorepo environment at Google facilitates rapid iteration of libraries through AI <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Beyond Verifiable Domains
In less easily verifiable domains, like creative tasks, models are improving at following abstract instructions <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. The challenge is training models to apply reward signals based on broad criteria, which was once abstract but is now showing results with reinforcement learning <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## The [[future_of_artificial_general_intelligence_AGI | Future of Artificial General Intelligence (AGI)]]

### Test Time Compute and AGI
While test time compute is powerful due to the low cost of LLM searches, allowing for more computation at inference time, it is not expected to lead all the way to [[path_to_artificial_general_intelligence_AGI | AGI]] on its own <a class="yt-timestamp" data-t="01:51:50">[01:51:50]</a>, <a class="yt-timestamp" data-t="02:29:57">[02:29:57]</a>. Other components, such as the ability to act in complex environments, are crucial <a class="yt-timestamp" data-t="02:33:30">[02:33:30]</a>.

### AI as Researchers and Novelty
A significant goal is for AI models to not just think longer but to think deeply, create useful knowledge, and dramatically improve data efficiency <a class="yt-timestamp" data-t="02:40:02">[02:40:02]</a>, <a class="yt-timestamp" data-t="02:48:48">[02:48:48]</a>. This involves models acting like researchers, posing novel questions in fields like mathematics, which is considered an infinite space for discovery <a class="yt-timestamp" data-t="03:06:36">[03:06:36]</a>, <a class="yt-timestamp" data-t="03:10:07">[03:10:07]</a>, <a class="yt-timestamp" data-t="03:47:01">[03:47:01]</a>. The "learning to mimic people" critique, suggesting AI can only relearn known information, is challenged by AI's ability to create novel discoveries through interpolation of disjoint information <a class="yt-timestamp" data-t="02:55:03">[02:55:03]</a>, <a class="yt-timestamp" data-t="02:58:12">[02:58:12]</a>.

### Infrastructure Needs for AI Development
The infrastructure for test time compute models will differ from pre-training, moving towards a more distributed and flexible inference problem, which can drive down costs <a class="yt-timestamp" data-t="03:57:04">[03:57:04]</a>, <a class="yt-timestamp" data-t="04:06:50">[04:06:50]</a>. Co-design with hardware teams like Google's TPU team allows for optimization of chip and data center designs <a class="yt-timestamp" data-t="04:07:39">[04:07:39]</a>.

## The Culture of AI Research

AI research is often described as "alchemy" — highly experimental with proofs in trying things out, often leading to unexpected discoveries <a class="yt-timestamp" data-t="03:28:28">[03:28:28]</a>. A key aspect of effective research is collaboration and the willingness to share ideas, even if credit assignment can be complicated <a class="yt-timestamp" data-t="03:32:57">[03:32:57]</a>.

### Organizational Models
Google's approach to compute allocation involves a blend of "bottom-up" (researchers initiating projects and attracting resources) and "top-down" (mandated bets on specific areas) <a class="yt-timestamp" data-t="03:15:09">[03:15:09]</a>. The bottom-up approach fosters collaboration and allows for abstraction-breaking ideas that don't fit neat categories <a class="yt-timestamp" data-t="03:37:07">[03:37:07]</a>. However, top-down vision is also necessary for driving large-scale projects and strategic investments <a class="yt-timestamp" data-t="03:41:09">[03:41:09]</a>.

### Pace of Advancement
The speed at which scientific advancements propagate in the AI field has dramatically increased <a class="yt-timestamp" data-t="04:47:01">[04:47:01]</a>. What once took 6-9 months (like the Transformer) now takes months for labs to make breakthroughs and release models based on new paradigms <a class="yt-timestamp" data-t="04:49:09">[04:49:09]</a>. This is attributed to the increased compute power and the large number of smart, creative people working in AI <a class="yt-timestamp" data-t="04:55:06">[04:55:06]</a>.

### Open Source vs. Closed Source Models
The ability of open-source models to remain competitive with frontier closed-source models is persisting, with the time gap between them shrinking <a class="yt-timestamp" data-t="04:43:43">[04:43:43]</a>, <a class="yt-timestamp" data-t="04:48:45">[04:48:45]</a>. This is driven by the passion, creativity, and access to compute within the open-source community <a class="yt-timestamp" data-t="04:50:09">[04:50:09]</a>.

## Societal Implications and Personal Reflections

### [[ai_in_education_and_human_interaction | AI in Education]]
AI, particularly with multimodal capabilities, holds incredible potential for education <a class="yt-timestamp" data-t="05:07:07">[05:07:07]</a>. Children can use AI as a "personalized encyclopedia," taking pictures of plants or animals and receiving detailed, accurate information, fostering a new type of learning <a class="yt-timestamp" data-t="05:20:07">[05:20:07]</a>.

### [[challenges_and_opportunities_in_ai_development | AGI Risks]] and Meaning
Concerns about [[challenges_and_opportunities_in_ai_development | AGI risks]] include the challenge of ensuring a more intelligent creation acts predictably for its creator, as well as practical implications for the economy and employment landscape <a class="yt-timestamp" data-t="05:55:49">[05:55:49]</a>. Internal groups within companies like Google focus on safety and mitigating unintended consequences of AI launches <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. In a future where AI might reduce the material necessity of human labor, humanity will need to find new sources of meaning <a class="yt-timestamp" data-t="05:27:07">[05:27:07]</a>, <a class="yt-timestamp" data-t="05:53:02">[05:53:02]</a>.

### General-Purpose vs. Task-Specific Models
For high-value applications like an "AI doctor," general-purpose models are preferred over task-specific ones, as the cost of LLM interaction is significantly cheaper than human consultation <a class="yt-timestamp" data-t="05:41:15">[05:41:15]</a>. If there's positive transfer of knowledge between domains, it's more efficient to consolidate into one large model, unless serving it becomes prohibitively expensive <a class="yt-timestamp" data-t="05:58:58">[05:58:58]</a>.

## Overhyped and Underhyped in AI

*   **Overhyped**: The ARC AGI eval is considered overhyped because researchers are not particularly inspired by these specific puzzle types, which can lead to progress in niche areas rather than true [[path_to_artificial_general_intelligence_AGI | AGI]] <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>.
*   **Underhyped**: [[future_of_artificial_general_intelligence_AGI | AGI]] itself and LLMs are still massively underhyped <a class="yt-timestamp" data-t="01:04:13">[01:04:13]</a>. The potential of code generation is also underhyped, as humans are not exceptionally good at it, and it enables the self-acceleration of AI development <a class="yt-timestamp" data-t="01:05:49">[01:05:49]</a>.

## The Future of [[future_of_software_development_and_AI | Software Development and AI]] Applications

There is significant value in agentic applications that go beyond chat experiences, allowing models to automate useful tasks <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. While agentic code is a crowded space, other areas could benefit from similar automation <a class="yt-timestamp" data-t="01:05:31">[01:05:31]</a>. The future of AI companions and human interaction will likely involve models that feel more human, driven by improvements in model capabilities and user-defined interfaces <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.