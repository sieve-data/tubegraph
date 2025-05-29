---
title: Applications and Future of AI
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

Artificial Intelligence (AI) is a field of investigation that explores the nature of intelligence itself and how to create intelligent machines <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. The pursuit of AI aims to amplify human intelligence and the overall intelligence of humanity, potentially solving many existing problems <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

## What is AI?
The concept of intelligence, and by extension AI, can be likened to the story of the blind man and the elephant, where different aspects are addressed by different approaches <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

### Historical Branches of AI
Historically, AI has been approached from two main perspectives <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>:

1.  **Reasoning and Search (Good Old-Fashioned AI - GOFAI)**
    This approach, dominant from the 1950s until the 1990s, views intelligence primarily as the ability to reason logically and search for solutions to problems <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. Examples include:
    *   **Optimization Problems** Tasks like the traveling salesman problem, where the goal is to find the shortest path through multiple cities <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
    *   **Planning** Determining a sequence of actions to achieve a goal, such as stacking objects or planning a robot arm's trajectory around obstacles <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
    *   **Heuristic Programming** Involves writing programs that use heuristics (rules of thumb) to efficiently search for solutions in vast problem spaces, like in chess, where exhaustive search is impossible due to exponential complexity <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.
    *   **Expert Systems/Rule-Based Systems** These systems use logical inference to deduce new facts from existing rules and facts (e.g., "if this, then that" statements) <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>.

2.  **Learning and Neural Networks (Biological Inspiration)**
    Starting also in the 1950s, this branch aimed to reproduce the mechanisms of intelligence observed in animal and human brains <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>. The core idea is that intelligence emerges from networks of simple elements (neurons) that learn by modifying the strength of connections between them <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
    *   **Perceptron** Proposed in 1957, it was an early electronic circuit model that could be trained to recognize simple shapes by adjusting weighted connections based on correct or incorrect outputs <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a>.
    *   **Limitations** Early neural networks, like the perceptron, had limited capabilities and could not handle complex tasks such as recognizing objects in natural images <a class="yt-timestamp" data-t="28:02:00">[28:02:00]</a>.

### Machine Learning (ML)
Machine learning is a field where machines are trained from data rather than being completely programmed <a class="yt-timestamp" data-t="29:11:00">[29:11:00]</a>. It's a particular way of approaching the AI problem <a class="yt-timestamp" data-t="58:30:00">[58:30:00]</a>.

#### Types of Machine Learning
1.  **Supervised Learning**
    The system is given an input and told the desired output. It adjusts its internal parameters (coefficients) iteratively to produce outputs closer to the desired ones based on hundreds, thousands, or billions of examples <a class="yt-timestamp" data-t="27:36:00">[27:36:00]</a>.

2.  **Reinforcement Learning**
    Instead of being told the correct answer, the system is only given feedback on whether its produced answer was "good" or "bad" <a class="yt-timestamp" data-t="32:25:00">[32:25:00]</a>. This method is often inefficient as it requires many trials and errors <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>. It is particularly effective for games like chess, Go, or poker, where systems can play millions of games against themselves to refine their strategies <a class="yt-timestamp" data-t="43:47:00">[43:47:00]</a>.

3.  **Self-Supervised Learning**
    This method has gained prominence in recent years and is a key component of modern language understanding systems <a class="yt-timestamp" data-t="33:21:00">[33:21:00]</a>. It is similar to supervised learning, but the "supervision" comes from the data itself, without needing human labeling <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>.
    *   **Text Example** A piece of text is "corrupted" by removing some words, and the machine is trained to predict the missing words using the visible context <a class="yt-timestamp" data-t="33:58:00">[33:58:00]</a>.
    *   **Image Example** An image is transformed or corrupted (e.g., colors changed), and the system is trained to recover the original image from the altered version <a class="yt-timestamp" data-t="34:45:00">[34:45:00]</a>.

### Deep Learning and Neural Networks
Deep learning is a subcategory of machine learning that utilizes neural networks with multiple layers <a class="yt-timestamp" data-t="29:22:00">[29:22:00]</a>. The breakthrough in the 1980s was the ability to stack multiple layers of neurons, each computing a weighted sum and passing it through a non-linear threshold function <a class="yt-timestamp" data-t="39:26:00">[39:26:00]</a>.

*   **Backpropagation** This algorithm, popularized in the 1980s, enabled the efficient adjustment of parameters in multi-layer neural networks by propagating error signals backward <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>.
*   **Convolutional Neural Networks (ConvNets)** Inspired by the architecture of the visual cortex, ConvNets are designed to process natural data like images and audio signals <a class="yt-timestamp" data-t="45:12:00">[45:12:00]</a>. Neurons in a ConvNet look at small areas of the input and apply the same function across different locations, which allows for shift equivariance (if the input shifts, the output shifts similarly) <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a>.
*   **Transformers** A different architecture where inputs are treated as a set of items (tokens) and processed in a way that is equivariant to permutation (the order of input items does not matter for the output content, only its order) <a class="yt-timestamp" data-t="46:23:00">[46:23:00]</a>.

### Large Language Models (LLMs)
[[large_language_models | LLMs]] are a special case of self-supervised learning, specifically auto-regressive Transformers <a class="yt-timestamp" data-t="59:17:00">[59:17:00]</a>. They are trained to predict the next word in a sequence based on the preceding words <a class="yt-timestamp" data-t="36:52:00">[36:52:00]</a>.

*   **Generative Nature** [[large_language_models | LLMs]] are called "generative" because they can generate text by predicting subsequent words based on measured probabilities <a class="yt-timestamp" data-t="51:36:00">[51:36:00]</a>.
*   **Scale and Capabilities** When trained on vast amounts of public internet text and made very large (tens to hundreds of billions of parameters), [[large_language_models | LLMs]] exhibit impressive abilities in language manipulation, grammar, and syntax across multiple languages <a class="yt-timestamp" data-t="56:23:00">[56:23:00]</a>. They can answer questions and solve puzzles, primarily through retrieval of stored knowledge <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>.
*   **Limitations** [[large_language_models | LLMs]] operate well in discrete, symbolic worlds (like text) but struggle with continuous, high-dimensional data (like images or video) <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. They do not truly understand the physical world and can make very stupid mistakes, highlighting their lack of real-world comprehension <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. [[large_language_models | LLMs]] also lack persistent memory beyond their current context and parameters <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

## [[future_directions_of_ai | Future Directions of AI]]

The next major challenge in [[future_directions_of_ai | AI development]] is to build systems that can learn how the world works by observing videos and images <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>. This requires architectures different from [[large_language_models | LLMs]] that can handle continuous data and understand the physical world <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>.

*   **World Models** The goal is to develop AI systems that can learn "world models," enabling them to predict the consequences of actions and plan complex sequences of actions <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>. This is analogous to human "System 2" thinking (deliberate planning) <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.
*   **Joint Embedding Predictive Architecture (JEPA)** A proposed architecture for learning from video involves training a neural net to predict abstract representations of future video segments, rather than predicting every pixel <a class="yt-timestamp" data-t="01:10:25">[01:10:25]</a>. This allows for prediction at different levels of abstraction; the longer the prediction horizon, the more abstract the representation <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   **Persistent Memory** Future AI systems will need persistent memory, similar to the hippocampus in human brains, to store long-term facts and retrieve them as needed <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### [[future_of_ai_and_technology | Impact of AI on the Future]]

The [[artificial_intelligence_and_its_future_impact_on_society | impact of artificial intelligence on future society]] and [[impact_of_ai_on_future_workforce_and_society | workforce]] will be significant:

*   **Utopian Future** If AI can learn to predict the future and plan actions, it could lead to a more utopian future by accumulating more knowledge and possessing abilities beyond human limitations <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>. Human-level intelligence could potentially be reached within a decade <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.
*   **Shifting Human Intelligence** As AI systems take over many current tasks, human intelligence will shift towards more abstract tasks like deciding what to do and strategizing, rather than execution <a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>.
*   **No Job Shortage** Economists suggest that we will not run out of jobs because we will not run out of problems; instead, we will find better solutions with AI's help <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>.
*   **Technological Shift** The way we interact with technology will likely move from smartphones to devices like smart glasses, offering AI assistance in real-world scenarios such as language translation <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a>.

### [[regulation_and_future_developments_in_ai_technology | Future of AI Development and Investment]]

*   **Data Quality and Encompassing Datasets** Future AI systems require more encompassing datasets that reflect all world languages, cultures, and value systems, which cannot be built by a single entity <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.
*   **Distributed Training and Local Infrastructure** The future of AI will involve distributed training of models and the importance of local computing infrastructure to allow countries to retain their data and provide low-cost access to AI inference <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.
*   **Open Source AI** The AI landscape is expected to be dominated by open-source platforms (e.g., Lama), similar to how Linux dominates operating systems <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>. Open-source platforms are more portable, flexible, secure, and cheaper, enabling a thriving ecosystem of startups and tailored vertical applications <a class="yt-timestamp" data-t="01:27:06">[01:27:06]</a>.
*   **Investment Opportunities** Investors should focus on companies that fine-tune open-source models for specific vertical applications (e.g., legal, accounting, fintech, health, agriculture) or develop consumer-facing AI assistants <a class="yt-timestamp" data-t="01:23:16">[01:23:16]</a>.

## Defining Intelligence

Intelligence can be defined as a combination of three key aspects <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>:
1.  **Possessing a collection of skills** and experience in solving problems and accomplishing tasks <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
2.  **Ability to learn new skills quickly** with few trials <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
3.  **Ability to solve new problems (zero-shot learning)** without prior learning, by using a mental model of the situation <a class="yt-timestamp" data-t="01:32:24">[01:32:24]</a>.