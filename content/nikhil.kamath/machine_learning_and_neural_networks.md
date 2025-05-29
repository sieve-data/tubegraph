---
title: Machine learning and neural networks
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

## Understanding AI: A Historical Perspective
Artificial Intelligence (AI) is broadly defined as a field of investigation, rather than a singular solution <a class="yt-timestamp" data-t="02:28:51">[02:28:51]</a>. Historically, the pursuit of understanding [[Understanding AI | intelligence]] has been likened to the parable of the blind men and the elephant, where different researchers focused on isolated aspects of intelligence, neglecting others <a class="yt-timestamp" data-t="02:28:51">[02:28:51]</a>.

### Engineer vs. Scientist
A key distinction often drawn in the field is between an engineer and a scientist. A scientist endeavors to understand the world, while an engineer strives to create new things <a class="yt-timestamp" data-t="02:03">[02:03]</a>. Often, understanding the world necessitates creating new things, as scientific progress is deeply intertwined with technological advancements that enable data collection <a class="yt-timestamp" data-t="02:08">[02:08]</a>. The invention of the telescope, for instance, led to discoveries about planets, and the microscope opened doors to new fields of study <a class="yt-timestamp" data-t="02:17">[02:17]</a>. For Yann LeCun, the long-standing obsession has been uncovering the mysteries of intelligence, and as an engineer, the only way to achieve this is to build an intelligent machine <a class="yt-timestamp" data-t="02:41">[02:41]</a>.

### Early Approaches to AI
The history of AI saw two competing branches emerge from the 1950s:

1.  **Good Old-Fashioned AI (GOFAI)**: This approach defined [[Understanding AI | intelligence]] as the ability to solve problems through reasoning and search <a class="yt-timestamp" data-t="02:27">[02:27]</a>.
    *   Problems like the "traveling salesman problem" (finding the shortest path through cities) were framed as optimization problems, where solutions were searched for in a space of possibilities <a class="yt-timestamp" data-t="02:09">[02:09]</a>.
    *   This involved "heuristic programming," where programs internally search for solutions, avoiding exhaustive searches due to the exponentially large number of possibilities (e.g., in chess) <a class="yt-timestamp" data-t="02:39">[02:39]</a>.
    *   It also encompassed logic-based systems, using rules and facts to deduce new facts (logical inference), leading to "expert systems" or "rule-based systems" prevalent in the 1980s <a class="yt-timestamp" data-t="02:23">[02:23]</a>.
    *   This branch dominated AI until the 1990s <a class="yt-timestamp" data-t="02:12">[02:12]</a>.

2.  **Neural Networks and Learning**: This "bottom-up" approach sought to reproduce the mechanisms of intelligence observed in animals and humans <a class="yt-timestamp" data-t="02:27">[02:27]</a>.
    *   The core idea was that brains learn and organize themselves through modifications in the strength of connections between neurons <a class="yt-timestamp" data-t="02:14">[02:14]</a>.
    *   Early theoretical models of neurons emerged in the 1940s, followed by the first machine of this type, the **Perceptron**, proposed in 1957 <a class="yt-timestamp" data-t="02:20">[02:20]</a>.
    *   **Perceptron Training**: To train a system (e.g., to distinguish shapes like 'C' from 'D'):
        1.  An image (array of numbers/voltages) is fed into the system <a class="yt-timestamp" data-t="02:14">[02:14]</a>.
        2.  The output is a "weighted sum" of input values, where weights are like adjustable resistors <a class="yt-timestamp" data-t="02:39">[02:39]</a>.
        3.  If the system makes a mistake, the weights are adjusted (increased or decreased) to guide the output towards the desired result <a class="yt-timestamp" data-t="02:20">[02:20]</a>.
    *   Early perceptrons had limited capabilities and could only recognize simple shapes <a class="yt-timestamp" data-t="02:13">[02:13]</a>.
    *   This branch saw success in the late 1950s and early 1960s but then "died" in the late 1960s due to perceived limitations of the learning procedures <a class="yt-timestamp" data-t="02:46">[02:46]</a>. However, its principles continued to influence fields like "pattern recognition" and "adaptive filter theory" <a class="yt-timestamp" data-t="02:17">[02:17]</a>.

## Machine Learning
[[Neural Networks and Machine Learning | Machine learning]] is a field within AI where machines are trained from data, rather than being completely programmed for a specific task <a class="yt-timestamp" data-t="02:55">[02:55]</a>. It involves systems with "tunable parameters" whose input-output function is determined by these parameters, which are adjusted iteratively through training <a class="yt-timestamp" data-t="03:45">[03:45]</a>.

### Types of Machine Learning
1.  **Supervised Learning**: The system is given an input and a "correct" desired output. Coefficients are adjusted to make the system's output closer to the desired one <a class="yt-timestamp" data-t="02:36">[02:36]</a>. This is the most common form of training, requiring hundreds, thousands, or even billions of examples <a class="yt-timestamp" data-t="02:52">[02:52]</a>.
2.  **Reinforcement Learning**: The system is not told the correct answer, but merely whether its produced answer was "good or bad" <a class="yt-timestamp" data-t="03:23">[03:23]</a>.
    *   It is very inefficient, requiring many trials, as the system must explore many possibilities to find a better answer <a class="yt-timestamp" data-t="03:37">[03:37]</a>.
    *   This approach is effective for games like chess, Go, or poker, where systems can play millions of games against themselves to learn winning "policies" <a class="yt-timestamp" data-t="03:47">[03:47]</a>.
    *   While popular a decade ago, it has seen less prominence recently compared to other methods <a class="yt-timestamp" data-t="03:03">[03:03]</a>.
3.  **Self-Supervised Learning**: This has gained significant prominence in recent years and is a core component of modern successes like chatbots and [[Role of large language models in AI | natural language understanding]] systems <a class="yt-timestamp" data-t="03:21">[03:21]</a>.
    *   Unlike traditional supervised learning, there's no explicit "input" and "output" differentiation <a class="yt-timestamp" data-t="03:42">[03:42]</a>.
    *   The system learns by predicting missing or corrupted parts of its own input data. For example, by removing words from a text and training the system to predict them, or by corrupting an image and training the system to recover the original <a class="yt-timestamp" data-t="03:51">[03:51]</a>.
    *   It's "self-supervised" because it doesn't require human-labeled data (e.g., millions of images tagged as "cat" or "dog") <a class="yt-timestamp" data-t="03:55">[03:55]</a>. The task itself generates the supervision signal <a class="yt-timestamp" data-t="03:48">[03:48]</a>.
    *   This process allows the system to understand the internal structure of the input by "filling in the blanks" <a class="yt-timestamp" data-t="03:02">[03:02]</a>.

## Deep Learning and Modern Neural Networks
[[Neural Networks and Machine Learning | Deep learning]] is essentially a "new name" for [[Neural Networks and Machine Learning | neural networks]] <a class="yt-timestamp" data-t="02:30">[02:30]</a>. The key innovation in the 1980s was the ability to stack **multiple layers of neurons** <a class="yt-timestamp" data-t="03:26">[03:26]</a>.

### The Neuron Concept
A "neuron" in a neural network is a simplified computational element that performs a weighted sum of its inputs and then passes this sum through a non-linear "threshold function" (activating if above a threshold, zero if below) <a class="yt-timestamp" data-t="03:32">[03:32]</a>. The "weights" are adjustable coefficients that change during training <a class="yt-timestamp" data-t="03:56">[03:56]</a>. These "neurons" are not identical to biological neurons but share conceptual similarities <a class="yt-timestamp" data-t="04:15">[04:15]</a>.

### Backpropagation
The breakthrough algorithm that enabled training multi-layer [[Neural Networks and Machine Learning | neural networks]] in the 1980s was **backpropagation** <a class="yt-timestamp" data-t="04:19">[04:19]</a>. This algorithm allows the system to adjust parameters by propagating signals backward through the layers to figure out how sensitive the output is to each weight, thereby bringing the output closer to the desired one <a class="yt-timestamp" data-t="04:21">[04:21]</a>. This capability lifted the limitations that hindered earlier perceptrons <a class="yt-timestamp" data-t="04:20">[04:20]</a>.

### Key Architectural Components
The architecture of [[Neural Networks and Machine Learning | neural networks]] refers to how neurons are connected to each other, biasing the system towards finding good solutions for certain types of data <a class="yt-timestamp" data-t="04:54">[04:54]</a>.

1.  **Convolutional Neural Networks (ConvNets)**:
    *   Inspired by the architecture of the visual cortex in biology <a class="yt-timestamp" data-t="04:16">[04:16]</a>.
    *   Ideal for data from the natural world (images, audio signals) where nearby values are generally very similar <a class="yt-timestamp" data-t="04:41">[04:41]</a>.
    *   Neurons in a ConvNet look at small, local areas of the input, and the same function is replicated across different parts of the input <a class="yt-timestamp" data-t="04:42">[04:42]</a>.
    *   This design provides **equivariance to translation** (shift equivariance): if the input shifts, the output shifts similarly but remains otherwise unchanged, which is crucial for recognizing objects regardless of their position <a class="yt-timestamp" data-t="04:05">[04:05]</a>.
    *   ConvNets learn faster and with fewer samples by leveraging the underlying structure of natural data <a class="yt-timestamp" data-t="04:24">[04:24]</a>.

2.  **Transformers**:
    *   A different way of arranging neurons, designed to process inputs as a *set* of items (tokens/vectors) where the order of items generally doesn't matter <a class="yt-timestamp" data-t="04:23">[04:23]</a>.
    *   They exhibit **permutation equivariance**: if the input items are permuted, the output items will be permuted similarly but otherwise remain unchanged <a class="yt-timestamp" data-t="04:47">[04:47]</a>.
    *   This architecture is particularly effective for [[Role of large language models in AI | natural language understanding]] <a class="yt-timestamp" data-t="04:44">[04:44]</a>.

## Language Models and Large Language Models (LLMs)
The concept of a language model dates back to Claude Shannon in the 1940s, who explored predicting the next symbol (e.g., letter) in a sequence based on prior context <a class="yt-timestamp" data-t="04:24">[04:24]</a>. This is where the term "generative" comes from, as such models can generate new sequences <a class="yt-timestamp" data-t="05:37">[05:37]</a>.

### Challenges of Traditional Language Models
Early "N-gram models" involved building tables of conditional probabilities (e.g., probability of 'U' following 'Q') <a class="yt-timestamp" data-t="05:26">[05:26]</a>. However, as the "context" length (N) increased, these tables became astronomically large and sparsely populated, making them impractical <a class="yt-timestamp" data-t="05:53">[05:53]</a>.

### Neural Network Language Models
In the late 1990s, researchers like Yoshua Bengio proposed using [[Neural Networks and Machine Learning | neural networks]] to predict the next word instead of relying on explicit probability tables <a class="yt-timestamp" data-t="05:07">[05:07]</a>. This involved training a network to produce a probability distribution over the next word from a given context of words <a class="yt-timestamp" data-t="05:22">[05:22]</a>.

### Large Language Models (LLMs)
Modern [[Role of large language models in AI | Large Language Models]] (LLMs) are a specific type of [[Role of large language models in AI | autoregressive Transformer]] architecture <a class="yt-timestamp" data-t="05:15">[05:15]</a>.
*   They are trained on the entirety of publicly available text on the internet <a class="yt-timestamp" data-t="05:23">[05:23]</a>.
*   Their architecture allows them to predict the next word by looking at preceding words in a potentially very large context (thousands to millions of words) <a class="yt-timestamp" data-t="05:31">[05:31]</a>.
*   With tens to hundreds of billions of adjustable parameters, LLMs possess a vast amount of memory and appear to store extensive knowledge about the data they are trained on <a class="yt-timestamp" data-t="05:53">[05:53]</a>.
*   This enables "emerging properties" like answering questions, solving puzzles, and manipulating language with impressive fluency, grammar, and syntax across multiple languages <a class="yt-timestamp" data-t="05:46">[05:46]</a>.

## Limitations of Current LLMs and the Future of AI
Despite their impressive capabilities, LLMs have significant limitations:
*   **Discrete vs. Continuous Worlds**: LLMs excel in "discrete" worlds (like text, where there's a finite number of words) but struggle with "continuous," high-dimensional data like images and videos <a class="yt-timestamp" data-t="05:57">[05:57]</a>.
*   **Lack of Physical World Understanding**: LLMs do not inherently understand the physical world, which is why they can make "very stupid mistakes" despite their linguistic prowess <a class="yt-timestamp" data-t="06:07">[06:07]</a>. This explains why we have systems that can pass the bar exam but lack domestic robots or fully autonomous self-driving cars <a class="yt-timestamp" data-t="06:32">[06:32]</a>.
*   **Limited Memory**: LLMs have two forms of memory:
    1.  **Parameters**: Knowledge stored implicitly in the billions of parameters during training (like a human remembering statistical patterns from novels, not exact words) <a class="yt-timestamp" data-t="06:28">[06:28]</a>.
    2.  **Context/Prompt**: The current conversation or "prompt" acts as a limited working memory <a class="yt-timestamp" data-t="06:11">[06:11]</a>.
    They lack "persistent memory" akin to the human hippocampus, which stores long-term and short-term factual memories <a class="yt-timestamp" data-t="06:11">[06:11]</a>.
*   **System 1 vs. System 2 Reasoning**: LLMs operate primarily as "System 1" intelligence (subconscious, reactive actions without explicit planning) <a class="yt-timestamp" data-t="06:07">[06:07]</a>. The future challenge is to build "System 2" intelligence, which involves deliberate planning, thinking, and reasoning about sequences of actions to achieve goals <a class="yt-timestamp" data-t="06:12">[06:12]</a>.

### Joint Embedding Predictive Architecture (JEPA)
A promising path forward, as proposed by Yann LeCun, is the [[Artificial intelligence and brain interfacing | Joint Embedding Predictive Architecture]] (JEPA) <a class="yt-timestamp" data-t="06:28">[06:28]</a>.
*   Unlike autoregressive models that try to predict every pixel in a video (which is intractable), JEPA uses "encoders" to produce **abstract representations** of video segments <a class="yt-timestamp" data-t="06:35">[06:35]</a>.
*   The system then predicts these abstract representations of future video segments, rather than raw pixels <a class="yt-timestamp" data-t="06:47">[06:47]</a>. This filters out unpredictable details, focusing on the underlying predictable structure <a class="yt-timestamp" data-t="06:52">[06:52]</a>.
*   The goal is to build "world models" that can predict the consequences of actions, allowing systems to plan complex, hierarchical sequences of actions <a class="yt-timestamp" data-t="07:23">[07:23]</a>.
*   **Prediction Horizon**: Such models can predict very long-term outcomes, but the longer the prediction, the more abstract the representation level becomes <a class="yt-timestamp" data-t="07:41">[07:41]</a>.

### Timeline for Human-Level AI
Achieving human-level [[Understanding AI | intelligence]] is likely *not* imminent (e.g., next year), but possibly within a decade (5-10 years) if all goes well <a class="yt-timestamp" data-t="08:28">[08:28]</a>. This will require new architectures like JEPA and systems that learn from the real world, rather than merely scaling up existing LLMs <a class="yt-timestamp" data-t="08:57">[08:57]</a>.

## [[Applications and future of AI in various industries | Applications and Career Paths in AI]]

### Business Opportunities
The most likely business model involves taking an open-source foundation model (like Meta's LLaMA) and fine-tuning it for a particular vertical application <a class="yt-timestamp" data-t="09:16">[09:16]</a>. This allows companies to become experts in specific domains.

Industries ripe for [[Applications and future of AI in various industries | disruption]] by AI include:
*   Legal <a class="yt-timestamp" data-t="09:57">[09:57]</a>
*   Accounting <a class="yt-timestamp" data-t="10:07">[10:07]</a>
*   Business information/FinTech/Finance <a class="yt-timestamp" data-t="10:14">[10:14]</a>
*   Internal company information systems (e.g., for employee queries) <a class="yt-timestamp" data-t="10:26">[10:26]</a>
*   Consumer assistance <a class="yt-timestamp" data-t="10:54">[10:54]</a>
*   Education (though often government-contract dependent) <a class="yt-timestamp" data-t="11:02">[11:02]</a>
*   Health (especially in developing countries where access to doctors is limited) <a class="yt-timestamp" data-t="11:10">[11:10]</a>
*   Agriculture and rural areas, enabled by AI assistants that can speak local languages and serve non-literate populations through speech <a class="yt-timestamp" data-t="11:46">[11:46]</a>.

### Investing in AI
*   The future of AI will likely be dominated by open-source platforms (similar to Linux dominating operating systems) <a class="yt-timestamp" data-t="12:48">[12:48]</a>. These are more portable, flexible, secure, and cheaper <a class="yt-timestamp" data-t="12:08">[12:08]</a>.
*   Proprietary engines may become less important as open-source alternatives catch up in performance <a class="yt-timestamp" data-t="12:44">[12:44]</a>.
*   Investing in **local computing infrastructure** (data centers) is crucial for:
    1.  Local ability to train models <a class="yt-timestamp" data-t="11:51">[11:51]</a>.
    2.  Providing low-cost access to AI "inference" (running AI models) <a class="yt-timestamp" data-t="11:51">[11:51]</a>. The cost of LLM inference has dropped by a factor of 100 in two years <a class="yt-timestamp" data-t="12:25">[12:25]</a>.
*   The widespread deployment of AI in countries like India will require inference costs to be extremely low (e.g., a few rupees for a million tokens) <a class="yt-timestamp" data-t="12:37">[12:37]</a>.

### [[Career paths in AI | Career Paths]] for Young People
For a 20-year-old aspiring to build a business or [[Career paths in AI | career in AI]], pursuing a PhD or graduate studies is highly recommended <a class="yt-timestamp" data-t="12:25">[12:25]</a>.
*   It trains individuals to invent new things and use sound methodologies to prevent self-deception <a class="yt-timestamp" data-t="12:33">[12:33]</a>.
*   It provides deep knowledge of existing possibilities and limitations <a class="yt-timestamp" data-t="12:06">[12:06]</a>.
*   It offers legitimacy when hiring talented people and can facilitate fundraising if new, impactful techniques are developed and published <a class="yt-timestamp" data-t="12:11">[12:11]</a>.
*   For those without formal degrees, free online resources like deep learning courses (e.g., Yann LeCun's 2021 course on YouTube) offer comprehensive self-education <a class="yt-timestamp" data-t="13:30">[13:30]</a>.

## Impact of AI on Society and [[Understanding AI | Intelligence]]
As AI systems take over many tasks, human [[Understanding AI | intelligence]] will shift to different, more abstract tasks <a class="yt-timestamp" data-t="12:25">[12:25]</a>.
*   Humans will focus less on *doing* things and more on *deciding what to do* or *figuring out what to do* <a class="yt-timestamp" data-t="12:40">[12:40]</a>.
*   Everyone will gain access to AI assistants, enabling them to delegate many tasks in both the virtual and eventually the real world (e.g., domestic robots, self-driving cars) <a class="yt-timestamp" data-t="13:35">[13:35]</a>.
*   This will "lift the abstraction level" at which humans operate, fostering greater creativity and productivity <a class="yt-timestamp" data-t="13:17">[13:17]</a>.
*   While some skills may become obsolete (e.g., fast mental arithmetic), humans will continue to learn, educate themselves, and pursue competition through creativity and innovation <a class="yt-timestamp" data-t="13:42">[13:42]</a>.
*   Economists suggest AI will not lead to a shortage of jobs, as there will always be new problems to solve, but rather better solutions with AI's help <a class="yt-timestamp" data-t="13:55">[13:55]</a>.

## Redefining Intelligence
[[Understanding AI | Intelligence]] can be defined as a combination of three key abilities:
1.  **Possessing a collection of existing skills**: Experience with solving problems and accomplishing tasks <a class="yt-timestamp" data-t="13:19">[13:19]</a>.
2.  **Ability to learn new skills quickly**: Acquiring new tasks with few trials <a class="yt-timestamp" data-t="13:19">[13:19]</a>.
3.  **Ability to solve new problems without explicit learning (Zero-Shot)**: Facing a novel problem and solving it by thinking and applying a mental model of the situation, even if a similar problem has never been encountered before <a class="yt-timestamp" data-t="13:19">[13:19]</a>.