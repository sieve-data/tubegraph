---
title: Machine Learning Techniques
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

[[Introduction to Artificial Intelligence | Artificial Intelligence]] (AI) is a field of investigation that addresses the problem of intelligence itself <a class="yt-timestamp" data-t="02:53:55">[02:53:55]</a>. Historically, different approaches have been taken to define and build intelligent systems <a class="yt-timestamp" data-t="02:55:07">[02:55:07]</a>.

## Good Old-Fashioned AI (GOFAI)
One early aspect of intelligence addressed in the 1950s focused on reasoning, logical processing, and searching for solutions to problems <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This approach, sometimes jokingly referred to as "Good Old-Fashioned [[Introduction to Artificial Intelligence | AI]] (GOFAI)," involves writing programs that internally search for solutions, often using heuristics to navigate the exponentially large number of possibilities, such as in chess <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. It also includes systems based on logic, where facts are deduced from rules and existing facts <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. This led to expert systems or rule-based systems, dominant until the 1990s <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This approach typically ignored aspects like perception, such as understanding images or sounds <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Machine Learning
In contrast to GOFAI, [[Understanding Neural Networks | machine learning]] involves training machines from data rather than completely programming them to do something <a class="yt-timestamp" data-t="02:59:11">[02:59:11]</a>. It views intelligence as the ability to learn <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This approach draws inspiration from biology, attempting to reproduce the mechanisms of intelligence seen in animal and human brains <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Fundamental Concept: Neurons and Connections
The brain's intelligence is seen as an emerging phenomenon of networks of very simple elements (neurons) connected in large numbers <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Memory and intelligence stem from the strength of connections between these neurons, which are modified as the brain learns <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. In [[Understanding Neural Networks | neural networks]], a "neuron" is a computational element that calculates a weighted sum of its inputs and compares it to a threshold <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>.

### Types of Machine Learning

#### 1. Supervised Learning
In supervised learning, a system is given an input and produces an output <a class="yt-timestamp" data-t="02:52:10">[02:52:10]</a>. If the output is not the desired one, coefficients (weights) are adjusted to bring the output closer to the target <a class="yt-timestamp" data-t="02:55:07">[02:55:07]</a>. This iterative adjustment process, repeated over millions or billions of examples, allows the system to learn if it is powerful enough <a class="yt-timestamp" data-t="02:57:48">[02:57:48]</a>. The perceptron, an early [[Understanding Neural Networks | neural network]] proposed in 1957, used this method to recognize simple shapes by adjusting weights <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

#### 2. Reinforcement Learning
Reinforcement learning involves a system where the correct answer is not explicitly provided <a class="yt-timestamp" data-t="03:26:27">[03:26:27]</a>. Instead, the system is given a "reward" or "penalty" (a single number indicating good or bad) for its output <a class="yt-timestamp" data-t="03:30:20">[03:30:20]</a>. This method is inefficient as it requires many trials and works well for games like chess or Go, where the system can play millions of games against itself to learn optimal strategies <a class="yt-timestamp" data-t="03:47:47">[03:47:47]</a>.

#### 3. Self-Supervised Learning
Self-supervised learning has become highly prominent in the last five to six years, contributing significantly to the success of [[Large Language Models and their limitations | chatbots]] and [[Large Language Models and their limitations | natural language understanding]] systems <a class="yt-timestamp" data-t="03:21:09">[03:21:09]</a>. It is similar to supervised learning but does not require manually labeled input-output pairs <a class="yt-timestamp" data-t="03:40:02">[03:40:02]</a>. Instead, the system learns by predicting missing or corrupted parts of its input <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

Examples:
*   **Text:** A piece of text is corrupted by removing words, and the machine is trained to predict the missing words using the visible context <a class="yt-timestamp" data-t="03:51:10">[03:51:10]</a>.
*   **Images:** An image is corrupted or transformed (e.g., colors changed), and the system is trained to recover the original image from the altered version <a class="yt-timestamp" data-t="03:44:06">[03:44:06]</a>. This helps the system understand the internal structure of the input <a class="yt-timestamp" data-t="03:50:18">[03:50:18]</a>.

## [[the_evolution_of_neural_networks_and_applications_in_AI | Deep Learning]] and its Architectures
[[the_evolution_of_neural_networks_and_applications_in_AI | Deep learning]] is a subcategory of [[Understanding Neural Networks | machine learning]] and is the reason for much of the recent excitement around [[Introduction to Artificial Intelligence | AI]] <a class="yt-timestamp" data-t="02:59:22">[02:59:22]</a>. It is essentially a new name for [[Understanding Neural Networks | neural networks]] <a class="yt-timestamp" data-t="02:59:30">[02:59:30]</a>. The breakthrough occurred in the 1980s with the ability to stack multiple layers of neurons, allowing the system to compute more complex functions than single-layer perceptrons <a class="yt-timestamp" data-t="03:26:26">[03:26:26]</a>. This was made possible by the "backpropagation" algorithm, which efficiently adjusts the weights in a multi-layered network during training <a class="yt-timestamp" data-t="04:20:19">[04:20:19]</a>.

Key [[the_evolution_of_neural_networks_and_applications_in_AI | deep learning]] architectures:

### Convolutional Neural Networks (ConvNets)
Inspired by the architecture of the visual cortex, ConvNets are designed for data with local spatial correlation, such as images or audio signals <a class="yt-timestamp" data-t="04:41:54">[04:41:54]</a>. In a ConvNet, each neuron observes only a small area of the input, and the same "neuron" (with the same weights) is replicated across different locations of the input, allowing it to detect the same patterns (motifs) regardless of their position <a class="yt-timestamp" data-t="04:52:19">[04:52:19]</a>. This gives them a property called "shift equivariance," meaning if the input shifts, the output also shifts but otherwise remains unchanged <a class="yt-timestamp" data-t="04:46:10">[04:46:10]</a>.

### Transformers
Transformers are a different way of arranging neurons, particularly effective for sequences of "tokens" (lists of numbers or vectors) <a class="yt-timestamp" data-t="04:23:23">[04:23:23]</a>. A key property of a Transformer layer is "permutation equivariance": if the order of inputs is permuted, the outputs will be similarly permuted but otherwise unchanged <a class="yt-timestamp" data-t="04:46:23">[04:46:23]</a>. This means the system views the inputs as a set where the order does not inherently matter <a class="yt-timestamp" data-t="04:48:50">[04:48:50]</a>.

#### Large Language Models (LLMs)
[[Large Language Models and their limitations | Large Language Models]] are a special case of self-supervised learning using Transformer architectures <a class="yt-timestamp" data-t="03:46:46">[03:46:46]</a>. They are trained to predict the next word in a sequence, looking only at preceding words <a class="yt-timestamp" data-t="03:56:52">[03:56:52]</a>. When trained on vast amounts of text (e.g., the entire public internet), with billions of adjustable parameters, these models develop "emerging properties" like answering questions and manipulating language impressively, capturing grammar and syntax across multiple languages <a class="yt-timestamp" data-t="03:59:15">[03:59:15]</a>. This process of predicting the next word sequentially is called "auto-regressive prediction" <a class="yt-timestamp" data-t="04:59:02">[04:59:02]</a>.

Despite their linguistic prowess, [[Large Language Models and their limitations | LLMs]] have limitations:
*   They work best for discrete data like text <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   They do not understand the physical world, which is continuous and multi-dimensional (e.g., video) <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   They can make very stupid mistakes that reveal a lack of real-world understanding <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>.
*   Their memory is limited to parameters learned during training and the current "context" (the prompt and generated tokens), lacking a persistent, hippocampus-like memory <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>.

## Next Challenges in [[Applications and Future of AI | AI]]
The next major challenge in [[Applications and Future of AI | AI]] is to build systems that can learn how the world works by observing continuous data like videos and images <a class="yt-timestamp" data-t="01:01:30">[01:01:30]</a>. This requires new architectures, such as "Joint Embedding Predictive Architectures" (JEPAs), which aim to predict abstract representations of future video frames rather than every pixel, filtering out unpredictable details <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>.

Such "world models" would allow [[Applications and Future of AI | AI]] systems to imagine the consequences of actions, plan complex sequences hierarchically, and make both precise short-term predictions (like muscle movements) and abstract long-term predictions (like career paths) <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>. This capability, known as "system 2" thinking (deliberate planning) as opposed to [[Large Language Models and their limitations | LLMs]]' "system 1" (subconscious, reactive), is seen as a key to achieving human-level intelligence <a class="yt-timestamp" data-t="01:14:56">[01:14:56]</a>.

The development of these systems will be crucial for the advancement of [[Robotics and AI | domestic robots]] and fully autonomous self-driving cars <a class="yt-timestamp" data-t="01:03:37">[01:03:37]</a>.

## [[Career advice for aspiring AI professionals | Career Advice]] in [[Applications and Future of AI | AI]]
For aspiring [[Career advice for aspiring AI professionals | AI]] professionals and entrepreneurs, a master's or PhD is recommended to learn deep theoretical knowledge, understand existing possibilities, and gain legitimacy <a class="yt-timestamp" data-t="01:21:57">[01:21:57]</a>.

The most likely business model involves:
1.  Taking an open-source foundation model (like LLaMA) <a class="yt-timestamp" data-t="01:23:11">[01:23:11]</a>.
2.  Fine-tuning it for a specific vertical application <a class="yt-timestamp" data-t="01:23:40">[01:23:40]</a>.
3.  Becoming an expert in that vertical <a class="yt-timestamp" data-t="01:23:45">[01:23:45]</a>.

Promising verticals for [[Utilizing AI and platforms like Google and Microsoft | AI applications]] include:
*   Legal <a class="yt-timestamp" data-t="01:23:57">[01:23:57]</a>
*   Accounting <a class="yt-timestamp" data-t="01:24:10">[01:24:10]</a>
*   Business information/Fintech/Finance <a class="yt-timestamp" data-t="01:24:14">[01:24:14]</a>
*   Internal company information systems <a class="yt-timestamp" data-t="01:24:26">[01:24:26]</a>
*   Consumer assistance <a class="yt-timestamp" data-t="01:24:54">[01:24:54]</a>
*   Education (though funding often comes from government contracts) <a class="yt-timestamp" data-t="01:25:02">[01:25:02]</a>
*   Health (especially in developing countries to provide medical assistance) <a class="yt-timestamp" data-t="01:25:10">[01:25:10]</a>
*   [[Applications and Future of AI | AI]] assistants speaking local languages, serving populations with lower literacy, in areas like agriculture <a class="yt-timestamp" data-t="01:25:51">[01:25:51]</a>.

### Investment Perspective
The future of [[Applications and Future of AI | AI]] is expected to be dominated by open-source platforms, similar to how Linux dominates embedded devices <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>. Open-source [[Applications and Future of AI | AI]] platforms are more portable, flexible, secure, and cheaper <a class="yt-timestamp" data-t="01:27:08">[01:27:08]</a>. This enables an ecosystem where startups can build tailored products by fine-tuning open-source engines <a class="yt-timestamp" data-t="01:28:07">[01:28:07]</a>.

Local computing infrastructure is considered crucial for:
1.  Local ability to train models <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>.
2.  Low-cost access to inference for [[Applications and Future of AI | AI]] systems, which is necessary for widespread adoption <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>. The cost of [[Large Language Models and their limitations | LLM]] inference has dropped significantly, by a factor of 100 in two years <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.

## What is Intelligence?
Intelligence is defined as:
1.  Having a number of existing skills and experience in solving problems and accomplishing tasks <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.
2.  The ability to learn new tasks very quickly with few trials <a class="yt-timestamp" data-t="01:32:57">[01:32:57]</a>.
3.  The ability to solve new problems "zero-shot," without needing to learn anything new or having faced similar problems before, by thinking and using a mental model of the situation <a class="yt-timestamp" data-t="01:33:06">[01:33:06]</a>.