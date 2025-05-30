---
title: Prospects and challenges in robotics and AI integration
videoId: a0bEU83P8g8
---

From: [[redpointai]] <br/> 

Bob McGrew, former Chief Research Officer at OpenAI for six and a half years, recently discussed the future of AI, including the integration of AI into robotics, its challenges, and opportunities <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Current State and Future of AI Model Capabilities

There's a significant divergence between the outside perception and the inside view of AI progress. From the outside, after the rapid release of ChatGPT and GPT-4, it might appear that progress has slowed <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. However, scaling pre-training progress requires massive increases in compute, often 100x for a new generation (e.g., GPT-2 to GPT-3, GPT-3 to GPT-4) <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This necessitates building new data centers, a slow, multi-year process <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

### Test-Time Compute and O1
While pre-training continues, significant progress is being made through techniques like reinforcement learning for test-time compute <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. O1, for example, represents a 100x compute increase over GPT-4 by leveraging reinforcement learning to create longer, more coherent "Chain of Thought" reasoning <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. This approach doesn't require new data centers and has significant room for algorithmic improvements <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. In theory, these techniques could extend thinking time from seconds to hours or even days <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

### Multimodal Models: Video and Beyond
Multimodal AI, which integrates vision, audio, and other data types, is a particularly exciting area <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. While LLMs (language models) were invented around 2018, applying Transformer techniques to other modalities like images (DALL-E) and audio (Whisper) eventually led to their integration into main models <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

Video, however, has been the most resistant modality <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Sora, for instance, marks a significant demo in video generation <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. Unlike image generation, video creation requires extended sequences of events and thoughtful user interfaces for story unfolding <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. Video models are also very expensive to train and run <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. Over the next few years, video model quality, especially for extended coherent generations, is expected to improve significantly, and costs will dramatically decrease, similar to the price drops seen with GPT-3 quality tokens <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. It's predicted that AI-generated full-length movies, driven by directors with creative vision, could be seen in about two years <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

## Prospects and [[Progress and bottlenecks in AI and robotics|Challenges in Robotics]]

Bob McGrew initially joined OpenAI to focus on robotics, believing it would be the domain where deep learning became widely adopted <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. While his 2015 prediction of five years for widespread adoption was "very wrong," he now believes it is correct for the present <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Foundation models are a "huge breakthrough" for robotics because they enable faster setup and better generalization <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. The ability to use vision and translate it into action plans comes "for free" with these models <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. The ecosystem has also developed, making it easier to interact with robots, even conversing with them to direct actions <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

### Key Challenges in Robotics
*   **Reliability**: This is the most immediate problem <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>. If an AI agent makes a mistake while performing a task, especially one involving real-world actions (e.g., buying something, sending an email), the consequences can range from wasted time to embarrassment or financial loss <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. Achieving higher reliability (e.g., from 90% to 99% or 99% to 99.9%) requires an order of magnitude increase in compute and is a slow, multi-year process <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
*   **Learning Environment**: A major differentiator for robotics is whether learning occurs in simulation or the real world <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. While simulators offer benefits (similar to programming without production system pain), they struggle with "floppy" objects like cloth or cardboard, which are common in the real world <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. For general applications, real-world demonstrations are currently the only effective approach <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   **Unconstrained Environments**: Mass consumer adoption of robotics, particularly in homes, faces challenges because homes are unconstrained environments, and robot arms can pose safety risks <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   **Context for Enterprise Deployment**: For AI agents to automate tasks in an enterprise setting, they need vast amounts of context (co-workers, projects, codebases, preferences) that are ambiently present in the organization's data (Slack, documents, Figma) <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. Connecting to this data requires building libraries of connectors or using "computer use" models <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

### Deployment and Adoption
The deployment of AI, especially in enterprises, often requires "handholding" from consulting firms to integrate with data and define guardrails <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. While general-purpose "computer use" models (like Anthropic's) are compelling, achieving high reliability (e.g., 99.999%) is difficult due to the many steps involved <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. A mix of approaches is likely, with some using specific API integrations and others using computer use as a backup <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. Salesforce-specific computer use agents are unlikely, as application providers would want their data to be public and part of every foundation model <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Widespread computer use follows a pattern: compelling demos appear, but it's too painful to use initially <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. A year later, it's 10x better and used for limited cases; in two years, it's surprisingly effective but not entirely reliable <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. Adoption depends on the required level of reliability; tasks tolerating mistakes will be automated faster <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

For robotics, widespread adoption is expected in retail and work environments within five years, particularly in warehouse settings where mobility is already solved and pick-and-place is being addressed <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

## Broader [[Challenges and opportunities in AI integration|AI Integration and Societal Impact]]

Despite significant advancements, AI's impact on overall productivity statistics remains less visible than expected, similar to the internet in the 1990s <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. This is partly because jobs comprise many tasks, and even if AI automates some, a critical non-automatable task often remains <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

### The Role of AI in "Boring" Tasks
One underexplored area is applying AI to "boring" problems where human intelligence, despite being capable, would get bored <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. For example, AI could rigorously comparison shop across all company expenditures <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. AI is "infinitely patient" and doesn't need to be infinitely smart for such tasks <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. This concept explains why productivity gains from AI are first showing up in areas like consulting, where the job involves producing output <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. AI's ability to help "bottom half of performers" by enabling them to write code or execute tasks they conceptually understand but couldn't implement is seen as a hopeful aspect <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

### [[Challenges and future directions for AI in various domains|Societal Implications and the Future of Agency]]
As intelligence becomes ubiquitous and free due to AI, the scarce factor of production will shift <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. Bob McGrew speculates that this scarce factor will be "agency" – the ability to ask the right questions, identify projects to pursue, and define desired outcomes <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. While AI can generate content based on vague prompts, the human element of defining specific choices and desired outcomes will remain critical <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. This shift will feel continuous, as AI progress occurs on an exponential curve <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

### AGI and the Nature of Progress
Bob McGrew has a "deep critique of AGI" (Artificial General Intelligence), believing there won't be a single "moment" of AGI because problems are fractal, leading to continuous automation of more things <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. The future with AGI might even feel "banal," with self-driving cars and AI armies still resembling mundane office life <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

The fundamental challenges have been largely solved: pre-training, inferencing, and reasoning <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. The remaining challenge is "scaling," which is incredibly difficult and involves systems, hardware, optimization, and data problems <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. In this sense, reaching AGI feels "predestined" by continued scaling efforts <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

## OpenAI's Culture and Pivotal Decisions

OpenAI's culture is marked by frequent "re-foundings" or pivots <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. Key shifts included:
*   Transitioning from a non-profit to a for-profit entity, driven by the need to raise money <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.
*   The partnership with Microsoft <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   The decision to build their own products with the API <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
*   The move from enterprise to consumer with ChatGPT, which, though deliberate, happened somewhat by "accident" <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

These pivots fundamentally changed the company's purpose and the identity of its workforce every 18 months to two years <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. The early mission of achieving AGI by writing papers evolved into building one model that everyone in the world could use, a path discovered through exploration and necessity <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

A critical, though less famous, decision was to "double down on language modeling" as the central focus <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. This involved a painful restructure, shutting down exploratory projects like robotics and games teams, despite successes like the Dota 2 AI <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This decision stemmed from the conviction that increasing scale could solve problems, and it led to refocusing on language models and generative modeling <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

## Personal Reflections on AI Research

Bob McGrew highlights the importance of "grit" in top AI researchers <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. He cites the example of Adithya Ramesh, who worked for 18 months to two years on DALL-E to generate a "pink panda skating on ice," a challenge to prove neural networks were creative rather than just memorizing <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Such foundational problems require researchers to commit years to make their vision a reality <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

Building a research organization, according to McGrew, is like managing artists, especially "100x the artist of any engineer" <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. It requires a "very high touch" approach to avoid "snuffing out the artistry," as their dedication to their vision drives them through the pain of production <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. Unlike academia's focus on individual credit and competition, OpenAI fostered collaboration and aimed to build "one thing" rather than just publish papers <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

## Overhyped and Underhyped in AI

*   **Overhyped**: New architectures, as many tend to "fall apart at scale" <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Underhyped**: O1, which, despite being highly discussed, is still not appropriately recognized for its significance <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

Bob McGrew left OpenAI after eight years, feeling he had accomplished his initial goals, especially with the shipment of O1 preview, which completed the research program on pre-training, multimodal, and reasoning <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. He plans to take time to explore new areas, much like he did between Palantir and OpenAI, learning and developing new theses <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>. He continues to connect with founders and researchers, exploring topics like robotics that were outside OpenAI's focus <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

AI progress will continue and remain exciting, changing in its manifestations but not slowing down <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.