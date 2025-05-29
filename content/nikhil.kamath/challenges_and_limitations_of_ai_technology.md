---
title: Challenges and limitations of AI technology
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

The field of [[Understanding AI | Artificial Intelligence (AI)]] has seen remarkable progress, but it still faces significant [[Challenges in regulating AI development and usage | challenges and limitations]], particularly concerning its ability to truly comprehend the world and reason like humans.

## Early AI Limitations and Perceptrons
Early [[History and future of AI | AI research]] in the 1950s focused on different [[Perspectives on AI and its significance | aspects of intelligence]]. One dominant view was that intelligence revolved around reasoning and searching for solutions to problems, often formulated as "optimization" in mathematics [01:12:00](01:12:00), [01:14:27](01:14:27), [01:50:00](01:50:00). This approach, sometimes jokingly called "Good Old-Fashioned AI" (GOFAI), involved human-programmed rules and heuristic searches, as seen in expert systems [01:29:00](01:29:00), [01:40:50](01:40:50), [03:00:00](03:00:00).

However, this early AI branch largely ignored concepts like perception and abstract thought [01:14:52](01:14:52), [01:15:16](01:15:16). A second branch, also starting in the 1950s, sought to reproduce intelligence mechanisms observed in animal and human brains, focusing on learning [01:31:00](01:31:00), [01:52:00](01:52:00), [01:59:00](01:59:00). The perceptron, a simple electronic circuit proposed in 1957, was an early machine designed to recognize simple shapes by adjusting connection strengths between simulated neurons [02:00:59](02:00:59), [02:01:01](02:01:01), [02:22:00](02:22:00).

Despite initial success, the perceptron model was found to be "extremely limited" in the late 1960s [01:48:00](01:48:00). Marvin Minsky, a prominent AI pioneer, co-authored a book in the mid-1960s demonstrating these limitations [02:52:00](02:52:00), [02:55:00](02:55:00). It was not powerful enough to process complex functions, such as recognizing objects in natural images [02:28:02](02:28:02), [02:32:00](02:32:00). This led to a decline in interest until the 1980s, when breakthroughs in "deep learning" and backpropagation algorithms, along with the availability of more data and faster computers, renewed progress [02:28:30](02:28:30), [02:41:56](02:41:56), [02:44:00](02:44:00).

## Limitations of Modern AI (LLMs)
While modern Large Language Models (LLMs) like those powering chatbots have achieved impressive linguistic capabilities, they face critical limitations that prevent them from achieving human-level intelligence:

*   **Discrete vs. Continuous Worlds**
    LLMs excel in discrete worlds, such as text, where there is a finite number of possible words or tokens [01:00:05](01:00:05), [01:00:10](01:00:10), [01:00:48](01:00:48). However, they do not work effectively in continuous, high-dimensional worlds, like video, where the number of possible outcomes (e.g., pixel combinations) is essentially infinite [01:00:00](01:00:00), [01:02:00](01:02:00), [01:06:02](01:06:02). Predicting every pixel in a video is "completely impractical" [01:16:17](01:16:17).

*   **Lack of Physical World Understanding**
    A major limitation is that LLMs "do not understand the physical world" [01:02:07](01:02:07), [01:02:12](01:02:12). This can lead to "very stupid mistakes" despite their impressive language manipulation [01:02:23](01:02:23). For example, while an LLM can pass a bar exam or write an essay, it cannot perform basic tasks like a domestic robot or fully autonomous self-driving car because it lacks fundamental comprehension of how the world works [01:02:35](01:02:35), [01:02:43](01:02:43). Some suggest that the "smartest LLMs are not as smart as your house cat" in terms of physical world understanding [01:02:50](01:02:50).

*   **Limited Memory**
    LLMs have two primary types of memory:
    1.  **Parameters/Coefficients**: Knowledge is stored implicitly in the vast number of adjustable parameters during training. This allows them to recall statistical patterns of words but not precisely regurgitate entire texts [01:03:28](01:03:28), [01:03:59](01:03:59).
    2.  **Context/Prompt**: The input prompt acts as a limited "working memory" where generated tokens are injected into the system's input, creating a conversational context [01:04:09](01:04:09), [01:04:22](01:04:22).
    However, LLMs lack a "persistent memory" similar to the human hippocampus, which stores long-term and episodic memories, enabling recall beyond immediate context [01:03:09](01:03:09), [01:04:26](01:04:26), [01:09:07](01:09:07).

*   **Inefficient Learning and Reasoning ("System 1" vs. "System 2")**
    Reinforcement learning, where systems learn from "good" or "bad" feedback without explicit correct answers, is inefficient for real-world scenarios due to the "many, many many trials" required [00:43:35](00:43:35), [00:43:43](00:43:43). It works well for games like chess or Go because systems can play millions of games against themselves [00:43:50](00:43:50).

    Current LLMs primarily operate as "System 1" intelligence, which is reactive and subconscious, similar to actions taken without thinking [01:08:07](01:08:07), [01:14:14](01:14:14). The next major challenge in [[History and future of AI | AI development]] is to build "System 2" capabilities, which involve deliberate planning, complex reasoning, and abstract thought [01:08:16](01:08:16), [01:16:04](01:16:04).

## Overcoming Future Challenges
The next few years of [[History and future of AI | AI development]] will focus on building systems that overcome the current limitations of LLMs and achieve more human-like intelligence.

*   **New Architectures for Physical World Understanding**
    New architectures, such as "Joint Embedding Predictive Architectures" (JEPA), are being developed to enable AI to learn from videos and images [01:05:00](01:05:00), [01:10:25](01:10:25). Instead of predicting every pixel, JEPA systems predict abstract representations of videos, eliminating unpredictable elements [01:10:44](01:10:44), [01:11:31](01:11:31), [01:11:46](01:11:46). This allows the system to build "World Models" that can predict the consequences of actions, facilitating planning [01:13:23](01:13:23), [01:14:06](01:14:06). These world models would be hierarchical, enabling both short-term, precise predictions and long-term, more abstract predictions [01:13:35](01:13:35), [01:14:51](01:14:51). This type of "objective-driven AI" aims to embody "System 2" reasoning [01:16:15](01:16:15).

*   **Addressing Data Bias and Accessibility**
    Current LLMs are trained on publicly available data, which is heavily biased towards English and lacks representation for many other languages, cultures, and value systems [01:17:31](01:17:31), [01:17:41](01:17:41), [01:18:00](01:18:00). Future AI will require "more encompassing" datasets to understand the world's diversity [01:18:03](01:18:03). This necessitates a collaborative project to build common [[the_impact_of_artificial_intelligence_on_society | AI infrastructure]] and distributed training models, preventing any single entity from monopolizing [[Understanding AI | human knowledge]] [01:18:14](01:18:14), [01:18:36](01:18:36), [01:18:40](01:18:40).

*   **Computational Infrastructure**
    Local computing infrastructure is crucial for both training diverse models and providing low-cost access to AI inference [01:19:24](01:19:24), [01:19:37](01:19:37). The cost of LLM inference has dropped significantly, by a factor of 100 in two years, but further improvements are needed for widespread global adoption [01:20:26](01:20:26), [01:20:33](01:20:33).

*   **Impact on Human Intelligence and Work**
    As AI systems take over tasks, human intelligence will shift to more abstract roles, focusing on "deciding what to do" rather than the execution [01:29:30](01:29:30), [01:30:09](01:30:09). This will enable humans to be more creative and productive by elevating the abstraction level of their work [01:31:17](01:31:17), [01:31:21](01:31:21). Economists suggest that humans will not run out of jobs, but rather find "better solutions to problems with the help of AI" [01:31:55](01:31:55), [01:32:04](01:32:04).

## Defining Intelligence
In the context of AI, intelligence can be understood as a combination of three key abilities:
1.  **Possessing a number of skills and experience** in solving problems and accomplishing tasks [01:32:51](01:32:51), [01:32:55](01:32:55).
2.  **Learning new tasks quickly** with minimal trials [01:32:57](01:32:57), [01:32:59](01:32:59).
3.  **Solving new problems from scratch** (zero-shot learning) without needing to learn anything new, by using a mental model of the situation [01:32:26](01:32:26), [01:32:49](01:32:49).