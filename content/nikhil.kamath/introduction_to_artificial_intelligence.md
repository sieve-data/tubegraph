---
title: Introduction to Artificial Intelligence
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

[[definition_and_origins_of_ai | Artificial intelligence]] (AI) is a field of investigation that explores the problem of intelligence itself <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. A core obsession in this field is uncovering the mysteries of intelligence, which, from an engineering perspective, involves building a machine that is intelligent <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. This pursuit involves both understanding intelligence at a theoretical level and the practical consequences of building intelligent machines for humanity <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Historical Perspectives on Intelligence and AI

Historically, the problem of defining "what is intelligence" has been compared to the story of the blind men and the elephant, where different people focus on different aspects of intelligence while ignoring others <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.

### Intelligence as Reasoning and Search (GOFAI)
One early perspective on intelligence, prominent in the 1950s, was that intelligence is primarily about reasoning, specifically logical reasoning and searching for solutions to problems <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. This approach can be formulated as an optimization problem where one searches for the best solution (e.g., the shortest path in a "traveling salesman problem") <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. This involves defining a "space of possible solutions" and a numerical way to evaluate if a solution is good <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.

This branch of AI, sometimes jokingly referred to as "Good Old-Fashioned AI" (GOFAI), was dominant until the 1990s <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>, <a class="yt-timestamp" data-t="28:58:00">[28:58:00]</a>. It focuses on:
*   **Heuristic Programming**: Programs internally search for solutions, using heuristics to avoid exhaustively searching all possibilities, especially in problems like chess where the number of possible moves explodes exponentially <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.
*   **Logic-based Systems**: Using rules and facts to deduce new facts through logical inference <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>. This led to "expert systems" or "rule-based systems" in the 1980s <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>.

This approach largely ignored aspects like perception and abstract thought <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.

### Intelligence as Learning (Neural Networks and Deep Learning)
A parallel branch of [[history_and_evolution_of_ai | AI]], also started in the 1950s, aimed to reproduce the mechanisms of intelligence observed in animals and humans, particularly how brains organize themselves and learn <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>. This view posits that intelligence emerges from networks of simple, interconnected elements <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.

Key concepts in this branch include:
*   **Neural Networks**: Inspired by the brain's learning through modifying the strength of connections between neurons <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. Early theoretical models appeared in the 1940s <a class="yt-timestamp" data-t="20:42:00">[20:42:42]</a>.
*   **Perceptron**: Proposed in 1957, it was one of the first machines of this type <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>. It learned to recognize simple shapes by adjusting "weights" (coefficients) based on whether its output was correct <a class="yt-timestamp" data-t="21:09:00">[21:09:00]</a>.
*   **Limitations and Revival**: Early perceptrons had limited capabilities and this branch of AI experienced a decline in the late 1960s <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. However, the concept was revived in the 1980s with the development of "backpropagation," an algorithm that allowed multi-layer neural networks to adjust parameters more effectively <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>, <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>. This lifted previous limitations, but still required significant data and fast computers, which were scarce before the internet era <a class="yt-timestamp" data-t="41:36:00">[41:36:00]</a>.

## Machine Learning Paradigms

[[definition_and_origins_of_ai | Machine learning]] is a particular way of approaching the [[definition_and_origins_of_ai | AI]] problem where machines are trained from data rather than being fully programmed <a class="yt-timestamp" data-t="29:11:00">[29:11:00]</a>.

### Types of Machine Learning
*   **Supervised Learning**: The system is given an input and told the correct output; if the output is incorrect, its internal coefficients are adjusted to bring it closer to the desired output <a class="yt-timestamp" data-t="27:36:00">[27:36:00]</a>. This iterative adjustment can involve hundreds, thousands, or billions of examples <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a>.
*   **Reinforcement Learning**: The system is not told the correct answer, but rather whether its produced answer was "good" or "bad" (given a single numerical "reward") <a class="yt-timestamp" data-t="32:23:00">[32:23:23]</a>, <a class="yt-timestamp" data-t="42:55:00">[42:55:00]</a>. This method is generally inefficient due to the need for many trials, but it works very well for games (like chess or Go) where a system can play millions of games against itself to learn optimal strategies <a class="yt-timestamp" data-t="43:43:00">[43:43:00]</a>.
*   **Self-Supervised Learning**: This has become very prominent in recent years and is a main component of modern AI systems like chatbots <a class="yt-timestamp" data-t="33:20:00">[33:20:00]</a>. While similar to supervised learning in its algorithms, the key difference is that there is no explicit "labeling" by a human <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>. Instead, the data itself provides the supervision. For example, a system might be given a corrupted piece of text (with missing words) and trained to predict the missing words, or given a corrupted image and trained to recover the original <a class="yt-timestamp" data-t="34:00:00">[34:00:00]</a>, <a class="yt-timestamp" data-t="34:41:00">[34:41:00]</a>. This approach allows systems to learn the internal structure of input data by filling in the blanks <a class="yt-timestamp" data-t="35:02:00">[35:02:00]</a>.

### Deep Learning and Network Architectures
[[applications_and_future_of_ai | Deep learning]] is a subcategory of [[definition_and_origins_of_ai | machine learning]], and the reason for much of the recent excitement around AI <a class="yt-timestamp" data-t="29:22:00">[29:22:00]</a>. It's essentially a new name for neural networks with multiple layers <a class="yt-timestamp" data-t="29:30:00">[29:30:00]</a>. A "neuron" in a neural network is a simplified computational element that computes a weighted sum of its inputs and activates its output if the sum exceeds a threshold <a class="yt-timestamp" data-t="49:15:00">[49:15:00]</a>. This involves linear operations with adjustable coefficients and a non-linear activation function <a class="yt-timestamp" data-t="50:00:00">[50:00:00]</a>.

Important architectural components include:
*   **Convolutional Neural Networks (ConvNets)**: Good for data from the natural world like images or audio signals where nearby values are similar <a class="yt-timestamp" data-t="44:38:00">[44:38:00]</a>. Inspired by the visual cortex, they involve neurons looking at small, overlapping areas of an image and sharing weights, allowing them to detect patterns at different locations and be "equivariant to translation" (shift invariance) <a class="yt-timestamp" data-t="45:54:00">[45:54:00]</a>, <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>.
*   **Transformers**: A different way of arranging neurons, where inputs are treated as a set of "tokens" (vectors), and the order of the inputs does not matter (equivariant to permutation) <a class="yt-timestamp" data-t="46:23:00">[46:23:00]</a>. This architecture is crucial for understanding relationships between different parts of a sequence, regardless of their position <a class="yt-timestamp" data-t="47:49:00">[47:49:00]</a>.

### Language Models and LLMs
A language model, a concept dating back to Claude Shannon in the 1940s, predicts the next symbol (letter, word, etc.) in a sequence given the previous context <a class="yt-timestamp" data-t="50:24:00">[50:24:00]</a>. Early N-gram models used tables of conditional probabilities, but these become impractical with larger contexts due to memory and sparsity issues <a class="yt-timestamp" data-t="52:53:00">[52:53:00]</a>.

*   **Neural Network Language Models**: In the late 1990s, the idea of using a neural network to predict the next word, instead of filling up probability tables, emerged <a class="yt-timestamp" data-t="55:07:00">[55:07:07]</a>.
*   **Large Language Models (LLMs)**: These are auto-regressive transformers trained on vast amounts of publicly available text data <a class="yt-timestamp" data-t="56:17:00">[56:17:00]</a>. By taking a context of words and predicting the next word, and making the context very large (thousands or millions of words), these systems exhibit "emerging properties" like answering questions and manipulating language impressively, including grammar and syntax across multiple languages <a class="yt-timestamp" data-t="56:37:00">[56:37:00]</a>, <a class="yt-timestamp" data-t="57:29:00">[57:29:00]</a>. LLMs are primarily "System 1" intelligence, meaning they are reactive and operate without deliberate planning or thinking <a class="yt-timestamp" data-t="01:16:14">[01:16:14]</a>.

## [[future_directions_of_ai | Future Directions of AI]]

### Limitations of Current LLMs
While LLMs are powerful for language manipulation, they operate in "discrete worlds" (text) and do not work for "continuous, high-dimensional worlds" like video <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>, <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. This means they do not understand the physical world, which leads to "very stupid mistakes" revealing a lack of underlying comprehension <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>, <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. This is why we have LLMs that can pass bar exams but not domestic robots or fully autonomous self-driving cars <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>.

### Next Challenges in AI
The next major challenge in [[applications_and_future_of_ai | AI]] is to build systems that can learn how the world works by observing videos and images <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This requires architectures different from auto-regressive LLMs, applicable to continuous data like video <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

Key areas of development include:
*   **Understanding the Physical World**: Creating systems that can predict what will happen next in a video, indicating an understanding of underlying world structure <a class="yt-timestamp" data-t="01:05:18">[01:05:18]</a>.
*   **Persistent Memory**: Current LLMs have limited memory (parameters from training, and the immediate prompt) <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. Future systems need persistent memory, akin to the brain's hippocampus, to store and retrieve facts over long periods <a class="yt-timestamp" data-t="01:04:26">[01:04:26]</a>.
*   **Objective-Driven AI (System 2 Intelligence)**: Moving beyond reactive "System 1" AI to "System 2" intelligence, which involves deliberate planning and thinking <a class="yt-timestamp" data-t="01:07:55">[01:07:55]</a>. This means building "world models" that can predict the outcome of actions and sequences of actions, allowing systems to plan complex tasks hierarchically <a class="yt-timestamp" data-t="01:13:23">[01:13:23]</a>.
*   **JEPA (Joint Embedding Predictive Architecture)**: An approach to self-supervised learning for video that predicts abstract representations of future video segments rather than every pixel, filtering out unpredictable details <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>. The longer the prediction into the future, the more abstract the representation <a class="yt-timestamp" data-t="01:12:41">[01:12:41]</a>.

While achieving human-level intelligence (AGI) may be a decade away, it is not as far as some might think <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>, <a class="yt-timestamp" data-t="01:15:28">[01:15:28]</a>. However, it will require new architectures and approaches beyond simply scaling up current LLMs <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.

## [[artificial_intelligence_and_its_future_impact_on_society | Impact of AI on Society]]

### The Future of AI Infrastructure
The [[the_role_of_ai_in_the_future | future of AI]] is expected to be dominated by open-source platforms, similar to how Linux dominates operating systems <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>. Open-source platforms are more portable, flexible, secure, and cheaper <a class="yt-timestamp" data-t="01:27:08">[01:27:08]</a>. Training models may become distributed globally, meaning models are trained on diverse local data without needing to copy it centrally <a class="yt-timestamp" data-t="01:18:40">[01:18:40]</a>. This also implies a need for local computing infrastructure for both training and inference (running AI models) <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>. The cost of AI inference has seen dramatic reductions, much faster than Moore's Law <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.

### Applications of AI
*   **Vertical Applications**: Fine-tuning open-source models for specific industries like legal, accounting, finance (fintech), or internal business information systems <a class="yt-timestamp" data-t="01:23:40">[01:23:40]</a>, <a class="yt-timestamp" data-t="01:24:10">[01:24:10]</a>.
*   [[impact_of_artificial_intelligence_on_future_education | **Education**]]: While not always highly lucrative, AI can assist in education <a class="yt-timestamp" data-t="01:25:02">[01:25:02]</a>.
*   **Health**: AI, especially LLMs, can provide medical assistance, particularly in areas where access to doctors is limited <a class="yt-timestamp" data-t="01:25:10">[01:25:10]</a>.
*   **Accessibility**: AI assistants that speak local languages and interact via speech can serve people not comfortable with literacy, opening up [[applications_and_future_of_ai | applications]] in agriculture and other rural areas <a class="yt-timestamp" data-t="01:25:51">[01:25:51]</a>.
*   [[robotics_and_ai | **Robotics**]]: The development of domestic robots and fully autonomous self-driving cars depends on AI systems that understand the real world from video <a class="yt-timestamp" data-t="01:30:37">[01:30:37]</a>.

### The Evolution of Human Intelligence
[[artificial_intelligence_and_its_future_impact_on_society | AI will amplify human intelligence]] by shifting human tasks to a more abstract level <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>, <a class="yt-timestamp" data-t="01:29:55">[01:29:55]</a>. Humans will focus on deciding what to do and strategizing, delegating execution to AI systems <a class="yt-timestamp" data-t="01:29:40">[01:29:40]</a>. This will enable greater creativity and productivity <a class="yt-timestamp" data-t="01:31:21">[01:31:21]</a>. While some tasks we learn today may be handled by machines in the future, humans will continue to compete and solve new problems, ensuring there will always be jobs <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

## Defining Intelligence in AI

Intelligence, in the context of AI, can be described as a combination of three abilities:
1.  **Possessing existing skills**: Having experience with solving problems and accomplishing tasks <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.
2.  **Learning new skills quickly**: Being able to learn new tasks with few trials <a class="yt-timestamp" data-t="01:32:57">[01:32:57]</a>.
3.  **Zero-shot problem solving**: The ability to solve new problems without explicitly learning a new skill, by thinking and using a mental model of the situation <a class="yt-timestamp" data-t="01:32:26">[01:32:26]</a>.

## [[career_advice_for_aspiring_ai_professionals | Career Advice for Aspiring AI Professionals]]

For a young aspiring entrepreneur or professional in [[career_advice_for_aspiring_ai_professionals | AI]], pursuing a PhD or Master's degree is highly recommended <a class="yt-timestamp" data-t="01:21:28">[01:21:28]</a>. This trains individuals to invent new things, develop robust methodologies, and gain legitimacy in the field <a class="yt-timestamp" data-t="01:21:35">[01:21:35]</a>.

A common business model today involves:
*   Taking an open-source foundation model (e.g., LLaMA) <a class="yt-timestamp" data-t="01:23:16">[01:23:16]</a>.
*   Fine-tuning it for a particular vertical application <a class="yt-timestamp" data-t="01:23:40">[01:23:40]</a>.
*   Becoming an expert in that specific vertical <a class="yt-timestamp" data-t="01:23:45">[01:23:45]</a>.

This approach allows for building tailored products more effectively than using generic APIs <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>.