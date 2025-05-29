---
title: Understanding and defining artificial intelligence
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

The field of [[understanding_ai|Artificial Intelligence]] ([[understanding_ai|AI]]) aims to understand and create intelligent machines. This pursuit involves both scientific inquiry into the nature of intelligence and engineering efforts to build systems that exhibit it <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## What is Intelligence?

Defining intelligence is complex, often likened to the story of the blind men and the elephant, where different researchers focus on distinct aspects and miss the whole picture <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Historically, [[understanding_ai|AI]] has approached intelligence from various perspectives:

### Intelligence as Reasoning and Search (Good Old-Fashioned AI - GOFAI)
One early perspective, dominant from the 1950s until the 1990s, defined intelligence primarily as the ability to reason logically and search for solutions to problems <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Logical Reasoning**: This involved formulating problems in terms of searching for optimal solutions within a space of possibilities, often called "optimization" <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. An example is the "traveling salesman problem," finding the shortest circuit through a set of cities <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Heuristic Programming**: Since exhaustively searching all solutions is often impossible (e.g., in chess, due to exponential explosion of possibilities), early [[understanding_ai|AI]] used "heuristics" – rules or methods that guide the search to find good solutions without checking every single one <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   **Rule-Based Systems/Expert Systems**: A related approach from the 1980s focused on logical inference, deducing new facts from existing rules and facts <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>, leading to "expert systems" <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

### Intelligence as Learning (Inspired by Biology)
A parallel branch of [[history_and_evolution_of_artificial_intelligence|AI]], also beginning in the 1950s, sought to reproduce the biological mechanisms of intelligence observed in animal and human brains <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Brain as a Learning System**: The idea is that brains organize themselves and learn, with intelligence emerging from networks of simple elements (neurons) connected to each other <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Learning occurs by modifying the strength of these connections <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **The Perceptron (1957)**: This was an early electronic circuit model that simulated a neuron. It could be trained to recognize simple shapes by adjusting the "weights" (connection strengths) between its inputs and output based on feedback <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
    *   **Limitations**: Early perceptrons had limited capabilities and could not process complex functions like recognizing objects in natural images <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
    *   **Shift in Terminology**: Following critiques (e.g., by Marvin Minsky in the 1960s), research in this area continued under new names like "statistical pattern recognition" or "adaptive filter theory," which had significant engineering applications <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

## AI Subfields and Techniques

Today, the landscape of [[understanding_ai|AI]] is broadly categorized:

*   **[[understanding_ai|Artificial Intelligence]] (AI)**: The overarching field of investigation and problem <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
*   **[[understanding_ai|Machine Learning]] (ML)**: A specific approach where machines are trained from data rather than being explicitly programmed <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
*   **[[understanding_ai|Deep Learning]] (DL)**: A subcategory of [[understanding_ai|Machine Learning]] that uses neural networks with multiple layers, which became prominent in the 1980s with algorithms like "backpropagation" <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. This is the foundation of most modern [[understanding_ai|AI]] <a class="yt-timestamp" data-t="00:58:38">[00:58:38]</a>.

### Machine Learning Paradigms

Within [[understanding_ai|Machine Learning]], several learning paradigms exist:

*   **Supervised Learning**: The system is given an input and a desired output, and it adjusts its parameters to produce outputs closer to the desired ones based on vast amounts of examples <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.
*   **Reinforcement Learning (RL)**: The system is not given a correct answer but rather feedback (a "reward" signal) indicating whether its actions were good or bad. It learns through trial and error, making it very effective for games like chess or Go, where millions of trials can be simulated <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. However, it is generally inefficient for real-world applications due to the number of trials required <a class="yt-timestamp" data-t="00:43:43">[00:43:43]</a>.
*   **Self-Supervised Learning (SSL)**: This paradigm, highly prominent in recent years, generates its own supervision signals from the input data itself <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>. For example, a system might be trained to predict masked-out words in a text or to recover an original image from a corrupted version <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. This eliminates the need for manual labeling of large datasets <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.

### Neural Network Architectures

Neural networks, despite their name, are simplified computational elements ("simulated neurons") that compute a weighted sum of inputs and pass it through a non-linear threshold function <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. Different ways of connecting these "neurons" lead to different architectures:

*   **Convolutional Neural Networks (ConvNets)**: Inspired by the visual cortex, ConvNets arrange neurons in layers where each neuron looks at a small, localized area of the input (e.g., an image). They replicate the same set of weights across different locations, allowing the network to recognize patterns regardless of their position. This property, called "equivariance to translation," makes them highly effective for processing natural data like images and audio signals <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.
*   **Transformers**: A more recent architecture, popular for processing sequences of data like text. Transformers view inputs as a set of independent "tokens" (vectors) where the order doesn't inherently matter (though positional information is often added) <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>. Their key property is "equivariance to permutation," meaning permuting inputs results in a similarly permuted output <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a>.

### Language Models

A "language model" predicts the next symbol (e.g., letter or word) in a sequence based on the preceding context <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. Early models, like N-gram models, used tables of probabilities, but these become impractical with longer contexts due to the exponential growth of possibilities <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.

*   **Neural Network Language Models**: In the late 1990s, the idea emerged to use neural networks to predict the next word, which allows for much larger contexts and more complex patterns than traditional table-based models <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>.
*   **[[understanding_ai|Large Language Models]] (LLMs)**: Modern LLMs, often built using Transformer architectures, are trained on vast amounts of public text data to predict the next word in a sequence <a class="yt-timestamp" data-t="00:56:17">[00:56:17]</a>. These models, with billions of parameters, exhibit surprising abilities to manipulate language, capture grammar, and store knowledge, leading to applications like chatbots <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. They learn in an "auto-regressive" fashion, using previously generated words as part of the input for the next prediction <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>.

### Limitations of Current [[understanding_ai|AI]] and the Path Forward

Despite their impressive language abilities, current LLMs have significant limitations:
*   **Lack of Physical World Understanding**: LLMs operate in discrete, textual domains and do not understand the continuous, high-dimensional physical world <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. They can make "stupid mistakes" that reveal a lack of common-sense understanding <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>.
*   **Limited Memory**: LLMs primarily have two forms of memory: knowledge stored in their training parameters (like humans remembering general facts from novels) and a limited working memory provided by the prompt context <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. They lack persistent memory akin to the hippocampus in the human brain, which stores long-term and episodic memories <a class="yt-timestamp" data-t="01:04:26">[01:04:26]</a>.
*   **System 1 vs. System 2 Thinking**: LLMs primarily exhibit "System 1" thinking (fast, reactive, subconscious), but lack "System 2" thinking (deliberate planning, reasoning, and problem-solving) <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.

The next major [[challenges_and_limitations_of_ai_technology|challenge in AI]] is to build systems that can learn how the world works by observing videos and images <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>. This requires new architectures, such as **Joint Embedding Predictive Architectures (JEPAs)** <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>. Instead of predicting every pixel in a video, JEPAs predict abstract representations of future video segments, filtering out unpredictable details <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. Such "world models" would allow [[understanding_ai|AI]] to:
*   Imagine the consequences of actions <a class="yt-timestamp" data-t="01:13:28">[01:13:28]</a>.
*   Plan complex sequences of actions hierarchically, from short-term precise movements to long-term abstract goals <a class="yt-timestamp" data-t="01:13:55">[01:13:55]</a>.
*   Achieve a form of "zero-shot" problem-solving, where they can tackle new problems without explicit training, by leveraging their mental model of the world <a class="yt-timestamp" data-t="01:32:26">[01:32:26]</a>.

## The Future of [[understanding_ai|AI]]

The aim is to develop [[understanding_ai|AI]] systems that can reach [[ai_and_general_intelligence|human-level intelligence]] within perhaps 5 to 10 years, though unexpected obstacles are likely <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. This will not be achieved by merely scaling up existing LLMs, but by developing new architectures capable of understanding and planning in the real world <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.

### [[the_impact_of_artificial_intelligence_on_society|Societal Impact]]
As [[understanding_ai|AI]] advances, human intelligence will shift focus to more abstract tasks, deciding *what to do* rather than merely *how to do* it <a class="yt-timestamp" data-t="01:29:40">[01:29:40]</a>. [[understanding_ai|AI]] assistants, accessible via devices like smartphones and smart glasses, will enable individuals to delegate many tasks, fostering greater creativity and productivity <a class="yt-timestamp" data-t="01:31:17">[01:31:17]</a>. This will not lead to a lack of jobs but rather a focus on solving new and existing problems more effectively <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

### Defining Intelligence Revisited
Ultimately, intelligence can be viewed as a combination of:
1.  Having a collection of existing skills and experience in solving problems <a class="yt-timestamp" data-t="01:32:19">[01:32:19]</a>.
2.  The ability to learn new skills quickly with minimal trials <a class="yt-timestamp" data-t="01:32:21">[01:32:21]</a>.
3.  The capacity to solve novel problems without prior learning, relying on a mental model of the situation ("zero-shot learning") <a class="yt-timestamp" data-t="01:32:24">[01:32:24]</a>.