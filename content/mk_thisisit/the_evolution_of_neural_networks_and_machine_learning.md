---
title: The evolution of neural networks and machine learning
videoId: 6QhGUQ5iTdk
---

From: [[mk_thisisit]] <br/> 

Artificial Intelligence (AI) is rapidly becoming the central topic of conversation globally, with machines being built that are demonstrably smarter than humans <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While AI is expected to solve many existing problems, it will also create new ones <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Neural Networks: Beyond Statistics

Wojtek Zaręba, a co-creator of ChatGPT, refutes the idea that AI is "only statistics" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. He argues that current models exhibit abilities that go beyond simple statistical recall:

*   **Reasoning and Generalization** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>: AI models can solve problems requiring reasoning that they have never explicitly seen, demonstrating an ability to generalize intelligently across very different data <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
    *   **Example**: A model trained on images of numbers with a black background can still recognize those numbers if a single black pixel is changed to white <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This occurs despite the new data being "completely different" from the training data <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Empirical vs. Theoretical Understanding** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>: There is an empirical understanding of how neural networks achieve such results, but a deep theoretical understanding of *why* this happens is lacking <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For instance, unlike many traditional models (e.g., decision trees), transformers do not "fall apart" when moved away from training data <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Limitations and Contextual Understanding in AI

Despite advancements, AI still faces significant limitations, particularly in [[human_vs_machine_intelligence | contextual understanding]]:

*   **Spatial and Cultural Context**: While humans perceive the world spatially and understand context, models often struggle. An example is an autonomous taxi that drove into a sacred zone during a Corpus Christi procession in San Francisco's Chinatown. The model knew to stop at a distance from people but did not understand the cultural significance of the "sacred zone" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Multimodal Data**: The lack of contextual understanding in models trained solely on image data highlights the need for multimodal inputs (images, text, video, sound, voice) for a deeper comprehension of the world <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Sensory Experience**: Models currently lack "senses" akin to humans, and their data acquisition differs fundamentally <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Training Differences ([[neural_networks_and_biological_systems | Human vs. Machine Intelligence]])**:
    *   **Human Brain**: Training and testing are integrated into one continuous process. Humans learn from their own real-world experiences, including positive and negative outcomes <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
    *   **Computers**: Typically, training and testing are separate processes. Models learn primarily from vast datasets collected by others <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. For example, a robot doesn't learn to avoid stairs because it fell; it learns because someone recorded such an event and fed it the data <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   **Reinforcement Learning**: An exception where models learn from their own experience, such as those that mastered Rubik's Cube manipulation or games like Dota and StarCraft <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **Limits of Physics and Knowledge**: A fundamental limitation is that models cannot be fed data about phenomena we don't understand (e.g., the source of gravity, quantum effects, or how human consciousness is born) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Creating a faithful copy of reality in a model is challenging if reality's functions are unknown to us <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

## OpenAI's Classification of AI Development Levels

OpenAI considers two main processes for imparting knowledge to models:

1.  **Large-scale Data Collection**: Training models to predict the next word in vast datasets (like the internet) enables them to understand what humanity has already understood <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
2.  **[[development_and_impact_of_deep_learning | Reinforcement Learning]]**: Rewarding models for correct behavior in limited domains. This approach allowed models to discover moves in Go that humans had not in thousands of years <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

Based on these, OpenAI classifies AI development into five levels:

*   **Level 1: Conversational (Turing Test)**:
    *   Models can hold conversations and pass the Turing Test, making it difficult for a person to distinguish between talking to a human or a computer <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Current language models are approaching this level, with distinctions sometimes only noticeable through response delays <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Level 2: Reasoning**:
    *   Models can solve problems requiring approximately 10 minutes of complex reasoning, like non-trivial mathematical or scientific tasks <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. This level requires deep understanding beyond immediate answers <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
*   **Level 3: Agents**:
    *   Models act as "agents" capable of performing multi-hour or multi-day tasks in the real world <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. For example, being instructed to build a website, the agent would handle domain acquisition, coding, deployment, and even communication (e.g., sending design options or email updates) <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This is a significant leap from current models like ChatGPT, which quickly get lost with multi-step actions <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Level 4: Scientist**:
    *   Models function as scientists, dedicating months to deep thought, re-examining existing assumptions, and inventing new things <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This implies questioning fundamental beliefs, similar to Albert Einstein realizing that time might not be constant <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
*   **Level 5: Organizational**:
    *   AI becomes competent enough to autonomously run entire organizations, managing planning, analysis, and decision-making for entities like a 1000-person company <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

Reaching Level 5 is predicted to occur in less than 10 years, reflecting an accelerating pace of [[artificial_intelligence_progress_and_future | technological innovation]] analogous to human history, where stages of development (e.g., cities, industrialization, computers, internet) have progressively shortened <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

## The Concept of Consciousness and AI

The discussion extends to whether AI can achieve consciousness:

*   **Definition of Consciousness**: The human brain receives information as electrical signals (bits) and creates an "immersive simulation of reality" <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>. Consciousness is described as our experience of this simulation <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>.
*   **Philosophical Zombie**: This thought experiment describes a being that behaves exactly like a conscious person but lacks internal subjective experience <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. The question is whether AI could possess this "internal cinema" <a class="yt-timestamp" data-t="00:35:46">[00:35:46]</a>.
*   **Hypothesis on Self-Awareness**: It is hypothesized that at some point, a model within a simulation might begin to simulate its own existence, leading to a form of self-awareness <a class="yt-timestamp" data-t="00:37:42">[00:37:42]</a>. This "click" could be when the model starts to understand its own participation in changing reality <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.
*   **Building Consciousness**: If consciousness is understood, it can be built <a class="yt-timestamp" data-t="00:39:55">[00:39:55]</a>. If it's not understood, it's difficult to build. The idea that consciousness results from quantum effects (as suggested by Roger Penrose) is noted <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   **Thought Experiments on AI Consciousness**:
    1.  Train a model on data *excluding* any mention of consciousness. If it then spontaneously discusses having such experiences, it could hint at consciousness <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>.
    2.  Connect AI to a human brain. If the human's consciousness expands, it doesn't necessarily mean the AI itself is conscious (similar to how psychedelics can expand consciousness without being conscious themselves) <a class="yt-timestamp" data-t="00:41:25">[00:41:25]</a>.
*   **AI as a "Power Bank" for the Brain**: The possibility of models serving as a "power bank" for the brain is considered plausible <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a>.

## Challenges and Future of AI

*   **Defective Nature of Current AI**: While the human brain operates on ~20 watts, current language models require exponentially more power (10^9 watts) <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. This suggests that current AI is "defective" compared to biological efficiency <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.
    *   This is likened to comparing a bird to an airplane: birds are efficient and acrobatic, while airplanes are heavy but can carry hundreds of people across oceans <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. AI models might be similar: less efficient but capable of massive tasks <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.
*   **[[evolutionary_algorithms_and_natural_selection | Evolution and Data Efficiency]]**: The human brain's efficiency is partly due to DNA, which contains information on how to effectively use reality, a product of billions of years of [[evolutionary_algorithms_and_natural_selection | evolution]] <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>. Evolution itself is a computationally powerful process that has discovered general intelligence multiple times (humans, elephants, ravens, dolphins) <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. Current AI models require huge datasets for initial training, but then gain the "incredible property" of learning quickly within a single conversation <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>. The ultimate goal is a model that can solve new, complex problems (like global warming) with minimal new data <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   **Hallucinations in Models**: Current training methods (predicting the next word, then post-training with human preferences) lead models to always provide an answer, even if they don't know it. Humans tend to reward models for providing answers, even if they're guesses, rather than admitting ignorance <a class="yt-timestamp" data-t="00:43:45">[00:43:45]</a>.
    *   **Solution**: Train models to express certainty (probabilities) and understand the boundary between their knowledge and ignorance <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.
*   **Memory in Neural Networks**: Like a character with short-term memory loss (e.g., in "Memento"), current neural networks remember within a single conversation, but then the memory disappears <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>.
    *   **Future**: Models need to "live" longer, either by having a context window long enough to encompass a "whole life of experience" or by incorporating new algorithms for continuous learning and weight updates based on new interactions <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>. This would give them more "sense of self" and continuity <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>.
*   **Energy and Computing Power**: Currently, the limitation is a lack of computing power. In the future, it might shift to a lack of energy <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>. However, just as computers have evolved from room-sized machines to powerful mobile phones, AI will likely undergo significant optimization to become more economical <a class="yt-timestamp" data-t="00:54:17">[00:54:17]</a>.

## Phases of AI Development ([[artificial_intelligence_evolution_and_misconceptions | Artificial Intelligence Evolution]])

Wojtek Zaręba outlines three phases of AI development:

1.  **Product Phase**: Current stage where companies create and integrate AI products into most software <a class="yt-timestamp" data-t="00:55:18">[00:55:18]</a>.
2.  **Geopolitical Phase**: Countries recognize that investment in AI is crucial for their geopolitical position <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>. Within a year and a half (perhaps 2025-2026), AI will likely be the main topic of global conversation <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>. This phase will see many "agents" doing different things, potentially impacting the labor market <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.
3.  **Superintelligence Phase**: Machines become significantly smarter than humans <a class="yt-timestamp" data-t="00:58:25">[00:58:25]</a>. At this stage, international cooperation will become critical <a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>. Such superintelligence could create new chips, deeply understand scientific literature, invent new things, and even run virtual companies <a class="yt-timestamp" data-t="00:59:23">[00:59:23]</a>.

## Risks and Mitigation

AI brings inherent risks:

*   **Misuse (Misi)**: AI can be used for negative purposes, such as deepfakes, military applications, or creating biological pandemics. A key concern is that AI could significantly increase the number of people capable of synthesizing dangerous viruses <a class="yt-timestamp" data-t="01:17:13">[01:17:13]</a>. AI can also assist in hacking, nuclear, or chemical weapon development <a class="yt-timestamp" data-t="01:18:55">[01:18:55]</a>.
    *   **Mitigation Efforts (OpenAI)**: OpenAI uses a framework called "PR" to assess model capabilities across categories like biological risk, chemical, nuclear, cybersecurity, and persuasion (convincing people) <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. They define levels (low, medium, high, critical) and work to reduce risk levels (e.g., from high to medium or low) <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.
*   **AI Race**: Dangers arise from organizations intensely competing to develop AI <a class="yt-timestamp" data-t="01:22:43">[01:22:43]</a>.
*   **Accidents**: Unintentional negative outcomes due to inattention <a class="yt-timestamp" data-t="01:22:58">[01:22:58]</a>.
*   **Alignment/Control (Misalignment)**: Ensuring that powerful AI models with broad skills actually "listen to us" and behave as expected <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>.

Zaręba is optimistic about minimizing negative applications, believing specific protective steps can be taken <a class="yt-timestamp" data-t="01:19:45">[01:19:45]</a>.

## Societal Impact and Worldcoin

*   **Impact on Society**: AI's integration into society will be non-trivial <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While some might resist (like the Luddite movement destroying textile machines due to job fears), historical trends show that technological development is difficult to stop, and it has often addressed societal problems <a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>.
*   **Worldcoin**: This project, co-founded by OpenAI's Sam Altman, aims to create a system for distributing future AI-generated prosperity and addressing issues like distinguishing humans from bots <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>. It identifies individuals uniquely through iris scans (stored cryptographically) to ensure fair distribution and prevent one person from taking the value of many <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>. The project emphasizes decentralization to prevent centralized attacks <a class="yt-timestamp" data-t="01:15:42">[01:15:42]</a>.
    *   This initiative reflects a potential shift from "zero-sum games" (where one gains at another's expense) to a "positive-sum game" where prosperity is vastly expanded, changing the dynamics of what is considered right or wrong <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>.

## Wojtek Zaręba's Journey and Philosophy

Wojtek Zaręba, a co-founder of OpenAI, hails from Kluczbork, Poland <a class="yt-timestamp" data-t="01:27:55">[01:27:55]</a>. He entered the field when AI was less developed, knowing many of the pioneers from conferences <a class="yt-timestamp" data-t="01:28:08">[01:28:08]</a>. His academic background (PhD in AI from New York) and strong publications positioned him to join OpenAI when Greg Brockman approached him <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.

He attributes his belief in AI's potential to a 2012 ImageNet competition where Geoffrey Hinton's team demonstrated neural networks' superior results, vastly outperforming other approaches <a class="yt-timestamp" data-t="01:31:18">[01:31:18]</a>. This convinced him of the technology's capabilities <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.

Zaręba led the robotics group at OpenAI, where they successfully trained a network to solve a Rubik's Cube with a robot hand, a complex task that could not be directly programmed <a class="yt-timestamp" data-t="01:34:18">[01:34:18]</a>. His work also contributed significantly to projects like Copilot, which uses AI to generate code, aiding millions of programmers <a class="yt-timestamp" data-t="01:37:17">[01:37:17]</a>.

He defines himself primarily as a scientist, also acknowledging elements of a futurologist and philosopher <a class="yt-timestamp" data-t="01:39:32">[01:39:32]</a>. His personal philosophy emphasizes kindness, close relationships, and the importance of love, drawing from long-term studies on human well-being <a class="yt-timestamp" data-t="01:40:28">[01:40:28]</a>. He has financially supported his old high school, establishing a lab and scholarships to provide opportunities for smart students who might lack them <a class="yt-timestamp" data-t="01:44:21">[01:44:21]</a>.

His dream for the [[future_of_artificial_intelligence | future of AI]] is to unlock its incredible opportunities for humanity, hoping for decisions that foster happiness and peace, pushing towards a better collective future <a class="yt-timestamp" data-t="01:47:03">[01:47:03]</a>.