---
title: History and Evolution of AI
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

The field of [[introduction_to_artificial_intelligence | Artificial Intelligence (AI)]] encompasses various approaches and definitions of [[definition_and_origins_of_ai | intelligence]]. Its history shows a progression from theoretical concepts to practical applications, constantly evolving to tackle more complex problems <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Defining Intelligence

Defining [[definition_and_origins_of_ai | intelligence]] itself is complex, often compared to the parable of the blind men and the elephant, where different researchers focus on distinct aspects <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Two primary views emerged early in the history of [[introduction_to_artificial_intelligence | AI]]:
*   **Intelligence as Reasoning and Problem-Solving**: This perspective, dominant from the 1950s until the 1990s, viewed [[definition_and_origins_of_ai | intelligence]] as the ability to reason logically and search for solutions to problems <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Intelligence as the Ability to Learn**: This branch sought to reproduce the mechanisms of [[definition_and_origins_of_ai | intelligence]] observed in animals and humans, focusing on how brains learn and organize themselves <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

## Good Old-Fashioned AI (GOFAI)

This traditional approach to [[introduction_to_artificial_intelligence | AI]] relies on programming machines to explicitly search for solutions using predefined rules and logic <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

### Reasoning and Search
In the 1950s, researchers explored how problems like the Traveling Salesman Problem (finding the shortest path visiting all cities) could be formulated as optimization problems, where the system searches for a solution that minimizes or maximizes a certain value <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Every reasoning problem could, to some extent, be reduced to such an optimization problem <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

This approach was heavily reliant on:
*   **Heuristic Programming**: Since exhaustively searching all possible solutions is often impractical (e.g., in chess, due to "exponential explosion" of possible moves), programs used heuristics to guide the search for good solutions without exploring the entire problem space <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   **Rule-Based Systems/Expert Systems**: Prevalent in the 1980s, these systems used logical rules and facts to deduce new facts or actions, mimicking human expert knowledge <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.

GOFAI focused heavily on planning and sequential actions but largely ignored aspects like perception—how machines interpret images or sounds <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## [[the_evolution_of_neural_networks_and_applications_in_ai | The Evolution of Neural Networks and Applications in AI]]

Parallel to GOFAI, another branch of [[introduction_to_artificial_intelligence | AI]] sought to simulate biological [[definition_and_origins_of_ai | intelligence]] by building systems that could learn <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Early Neural Networks: The Perceptron
Inspired by the brain's structure where memory and [[definition_and_origins_of_ai | intelligence]] arise from the strength of connections between neurons, researchers in the 1940s and 50s proposed models where learning involves modifying these connection strengths <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.

*   **The Perceptron (1957)**: This was one of the first machines of its type. It used an array of photo sensors (pixels) and trained a simulated neuron to recognize simple shapes like 'C' or 'D' <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. Training involved adjusting "weights" (simulated resistors) of connections based on whether the output was correct or incorrect <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.
*   **Limitations and the "AI Winter"**: Despite early successes, the perceptron's capabilities were shown to be extremely limited by figures like Marvin Minsky in the mid-1960s <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. This led to a decline in interest in neural networks until the 1980s, with researchers shifting their focus to "statistical pattern recognition" or "adaptive filter theory" <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

### Rise of Deep Learning
A significant breakthrough occurred in the 1980s with the idea of stacking multiple layers of neurons, creating "deep" neural networks <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

*   **Backpropagation Algorithm**: This algorithm, which became widely recognized in the 1980s, allowed the efficient training of multi-layered neural networks by propagating signals backward to adjust parameters and minimize errors <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>. This enabled systems to learn more complex functions, like classifying handwritten digits <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
*   **Early Challenges**: Despite the algorithmic advancements, the widespread adoption of neural networks was hindered by the lack of large datasets and fast enough computers in the late 1980s and early 1990s <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>.
*   **Convolutional Neural Networks (CNNs)**: Introduced in the late 1980s and early 1990s, CNNs were inspired by the architecture of the visual cortex <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>. They use "convolutional" layers where neurons look at small, local areas of an input (like an image) and share weights, making them highly effective for processing natural data like images and audio signals due to their "shift equivariance" property <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.

## Modern Machine Learning Paradigms

Today, [[the_evolution_of_neural_networks_and_applications_in_ai | AI]] is primarily built upon machine learning, where systems are trained from data rather than being explicitly programmed <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. Deep learning is a subcategory of machine learning that utilizes multi-layered neural networks <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.

### Types of Machine Learning
*   **Supervised Learning**: The system receives an input and a desired output, adjusting its parameters to make its output closer to the target <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. This requires labeled data.
*   **Reinforcement Learning (RL)**: The system is not given correct answers but instead receives a "good" or "bad" signal (a reward or penalty) for its actions <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>. RL is highly effective for tasks like training systems to play games (chess, Go, poker) because they can perform millions of trials against themselves <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>. It is less efficient for general problems due to the need for extensive trials <a class="yt-timestamp" data-t="00:43:43">[00:43:43]</a>.
*   **Self-Supervised Learning (SSL)**: This method has gained significant prominence in recent years. It's similar to supervised learning in its underlying algorithms but doesn't require explicit human labeling <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>. Instead, the system learns by predicting missing or corrupted parts of its own input data. For example, it might predict masked words in a text or recover an original image from a transformed version <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.

### Language Models and Transformers
[[the_evolution_of_neural_networks_and_applications_in_ai | Language models]] aim to predict the next word or character in a sequence. The concept dates back to Claude Shannon's work on information theory in the 1940s, initially using tables of probabilities for sequences of letters (N-gram models) <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>.

*   **Neural Network Language Models**: In the late 1990s, researchers like Y. Bengio proposed using neural networks to predict the next word, overcoming the limitations of large, sparse probability tables <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>.
*   **Transformers**: These are a specific architectural component in neural networks, popular today, that allow systems to process sequences by comparing every input element to each other and producing weighted connections <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a>. They are characterized by their "permutation equivariance," meaning the order of inputs (tokens) doesn't inherently matter, though mechanisms are added to account for sequence <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.
*   **Large Language Models (LLMs)**: LLMs, such as those used in chatbots like ChatGPT, are auto-regressive Transformers <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>. They are trained on vast amounts of publicly available text data to predict the next word based on a potentially very large context <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. Their immense number of parameters allows them to store vast knowledge and manipulate language impressively, capturing grammar and syntax across multiple languages <a class="yt-timestamp" data-t="00:57:31">[00:57:31]</a>.

## [[future_directions_of_ai | Future Directions of AI]] and [[future_of_ai_and_technology | Technology]]

While LLMs are powerful for discrete data like text, they have significant limitations.

### Beyond Language Models
LLMs primarily operate in discrete worlds and do not inherently understand the continuous, high-dimensional physical world <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This is why LLMs can make "stupid mistakes" that reveal a lack of real-world understanding <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>. For example, they can pass legal exams but cannot drive a car or operate as a domestic robot <a class="yt-timestamp" data-t="01:02:32">[01:02:32]</a>.

*   **Understanding the Physical World**: The next major challenge in [[introduction_to_artificial_intelligence | AI]] is to build systems that can learn about the world by watching videos and processing images <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. This requires architectures different from auto-regressive models, as predicting every pixel in a video is computationally intractable <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>.
*   **Joint Embedding Predictive Architectures (JEPAs)**: One proposed solution, JEPAs, trains systems to predict abstract representations of future video segments rather than raw pixels. This allows the system to learn the underlying structure of the world by filling in unpredictable elements <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>.
*   **Hierarchical World Models and System 2 Thinking**: These future [[applications_and_future_of_ai | AI]] systems would learn "world models" that predict the consequences of actions, enabling complex, hierarchical planning <a class="yt-timestamp" data-t="01:13:23">[01:13:23]</a>. This aligns with Daniel Kahneman's "System 2" thinking, which involves deliberate planning and reasoning, as opposed to the more reactive "System 1" behavior of current LLMs <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.
*   **Persistent Memory**: Unlike current LLMs, which have limited memory tied to their parameters or input context, future [[applications_and_future_of_ai | AI]] systems will need persistent memory, similar to the human hippocampus, to store and retrieve long-term facts and experiences <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.

### The Trajectory Towards Human-Level Intelligence
Achieving human-level [[definition_and_origins_of_ai | intelligence]] in [[introduction_to_artificial_intelligence | AI]] is seen as a goal potentially reachable within a decade, though this is an optimistic timeline <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. It will require new architectures like JEPAs and systems that learn from the real world, rather than merely scaling up existing LLMs <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.

### [[artificial_intelligence_and_its_future_impact_on_society | Artificial intelligence and its future impact on society]]
*   **Democratization and Open Source**: The future of [[introduction_to_artificial_intelligence | AI]] is likely to be dominated by open-source platforms, similar to Linux in operating systems. This democratizes the technology, making it more portable, flexible, secure, and cheaper for developers and startups <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>.
*   **Distributed Training and Local Infrastructure**: To overcome biases in current datasets (e.g., English-centric text) and to encompass all world languages, cultures, and values, future [[introduction_to_artificial_intelligence | AI]] models will need to be trained in a distributed fashion globally, with local computing infrastructure being crucial <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.
*   **Cost Reduction in Inference**: The cost of running [[introduction_to_artificial_intelligence | AI]] models (inference) is rapidly decreasing, making it accessible to a wider population, potentially enabling new applications in remote areas and for non-literate users through speech-based interactions <a class="yt-timestamp" data-t="01:20:20">[01:20:20]</a>.
*   **Shifting Human Roles**: [[artificial_intelligence_and_its_future_impact_on_society | AI]] will likely shift human [[definition_and_origins_of_ai | intelligence]] to higher-level tasks. Instead of performing routine actions, humans will focus on strategic decision-making, figuring out "what to do" rather than "how to do it," thereby enhancing creativity and productivity <a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>.
*   **Evolution of Human Intelligence**: As [[introduction_to_artificial_intelligence | AI]] takes over more tasks, humans will learn different skills, focusing on higher levels of abstraction. This does not imply a lack of jobs but rather a shift in the nature of work and problem-solving <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>.

## Re-defining Intelligence in the Context of AI
In essence, [[definition_and_origins_of_ai | intelligence]] can be seen as a combination of three abilities:
1.  Having a collection of skills and experience in solving problems <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.
2.  The ability to learn new skills quickly with few trials <a class="yt-timestamp" data-t="01:32:57">[01:32:57]</a>.
3.  The ability to solve novel problems "zero-shot" — without prior learning or similar experience, purely through reasoning and a mental model of the situation <a class="yt-timestamp" data-t="01:32:26">[01:32:26]</a>.