---
title: Symbolic and neural approaches to language understanding
videoId: -LKF_wYAQDQ
---

From: [[jimruttshow8596]] <br/> 

The field of Artificial General Intelligence ([[possibilities_for_achieving_humanlevel_agi | AGI]]) distinguishes itself from "narrow AI," which involves software and hardware systems designed to perform specific, intelligent-seeming tasks in narrowly defined ways, often different from human methods [00:01:33]. For instance, a chess program might play expertly but cannot play other games without reprogramming [00:02:00]. This "narrow AI revolution" has produced systems capable of intelligent actions that do not generalize beyond their specific contexts [00:02:20].

Artificial General Intelligence (AGI), a term coined about 15 years ago, refers to AI systems capable of achieving intelligence with at least the same generality of contexts as humans [00:02:49]. This requires the ability to transfer knowledge from one domain to qualitatively different domains, a concept related to "transfer learning" and "lifelong learning" [00:03:13].

## The OpenCog Framework: A Hybrid Approach

Ben Goertzel's OpenCog project is an example of an AGI approach that differs significantly from current deep learning methods [00:14:10]. OpenCog utilizes a hybrid "neural-symbolic" architecture, combining symbolic and sub-symbolic processing [00:22:04].

### OpenCog's Architecture
OpenCog's core components include:
*   **Knowledge Graph (AtomSpace):** A weighted, labeled hypergraph storing knowledge, including nodes, links, truth values, and attention values [00:16:31].
*   **AI Algorithms:** Multiple algorithms act on the AtomSpace, dynamically rewriting it and assisting each other [00:16:47]. These include:
    *   **Probabilistic Logic Networks (PLN):** A probabilistic logic engine for reasoning [00:17:00].
    *   **Moses:** A probabilistic evolutionary program learning algorithm that learns AtomSpace sub-networks representing executable programs [00:17:07].
    *   **Economic Attention Networks (Ekan):** Propagates attention values through the distributed network of nodes [00:17:20].
    *   **Deep Neural Networks:** Used to recognize perceptual patterns or patterns in other data, creating nodes in the knowledge graph that represent sub-networks or layers in the deep neural networks [00:17:26].

### Cognitive Synergy
The concept of "cognitive synergy" describes how different AI algorithms cooperate on the same knowledge graph [00:17:45]. If one algorithm gets stuck or makes slow progress, others can understand its intermediate state and intervene to help it progress [00:17:51]. This cooperation is bidirectional and concurrent, with algorithms helping each other out in cycles within complex networks [00:20:44]. For example, a reasoning engine stuck on a logical inference might be aided by evolutionary learning introducing creative ideas or perception providing sensory-level metaphors [00:18:12].

This approach contrasts with modular systems that rely on clean API interfaces between different AI algorithms [00:18:52]. Instead, OpenCog's algorithms cooperate in real-time on a dynamic, in-RAM, weighted, labeled hypergraph [00:19:08].

## Language Understanding in OpenCog
Language understanding is considered critical to the AGI project [00:27:04]. OpenCog's approach to language understanding involves hybridizing symbolic methods with deep neural nets [00:27:25].

### Syntax Parsing
OpenCog uses a combination of symbolic pattern recognition and deep neural networks to guide the symbolic pattern recognition for automatically learning grammar from large text corpora [00:27:37]. The goal is to map grammatical parses of sentences into semantic representations [00:27:49].

### Semantic Interpretation
A core aspect of sentence semantics is believed to be a logic expression or something homomorphic to it [00:28:38]. Semantic interpretation involves mapping syntax parses into a logic expression, complemented by other associated elements like images, episodic memories, and sounds [00:28:48].

This mapping of syntax parses into logic expressions is the second part of the language understanding problem, following syntax learning [00:29:04].

### Pragmatics
Pragmatics, the third part, involves mapping semantics into broader context [00:29:13]. This is largely treated as a problem of association learning and reasoning within OpenCog [00:29:21].

### Learning Approaches
OpenCog explores different learning paradigms for language:
*   **Unsupervised Language Acquisition:** Efforts are made to automatically learn dependency grammars from text corpora [00:29:49].
*   **Partially Supervised Learning:** Starting with a small amount of "supervised data," such as partial parsing or semantic tracing information, can significantly improve accuracy in unsupervised learning [00:30:28].
*   **Cross-Modal Learning:** Using captioned images where relationships in images are recognized by neural networks and correlated with syntax parses of captions helps connect sentences to their visual semantics [00:31:39].
*   **Embodied Learning:** Analogous to how human children learn language in the context of achieving practical goals within a multimodal world, integrating linguistic and non-linguistic action and perception patterns [00:34:00]. This approach contrasts with purely unsupervised or traditional supervised computational linguistics [00:34:28].

### Limitations of Current Deep Learning in NLP
While models like BERT and Ernie excel at recognizing complex statistical patterns in natural language text and emulating realistic language in the short run, they often fall short in grasping the overall meaning or deeper semantics of documents [00:22:52]. This results in "meaningless aspects" in generated text over medium lengths [00:23:14].

### The Future: Neural-Symbolic AI
Current deep neural networks are expected to "run out of steam" when dealing with problems requiring higher levels of abstraction [00:24:10]. The integration of logic systems with neural nets, a "neural-symbolic approach," is seen as the way forward [00:24:41]. This involves combining knowledge graphs with deep neural nets [00:24:50] and increasingly powerful logic engines to dynamically update knowledge graphs [00:25:02]. A convergence of these two approaches is anticipated [01:00:00].

## Generating Learning Environments
The idea of developing technologies for generating learning environments, particularly for language learning, is considered a potentially fruitful approach [00:37:17]. Such environments could embed pragmatics and semantics, supported by natural language syntax, to generate diverse cases for multi-level language learning systems [00:37:28]. While initial crude attempts to generate learning environments have existed, more sophisticated models are needed to create diverse enough environments that mirror the "endless abundance of weird little distinctions" found in the real world [00:38:03].

This concept involves an AI learning to generate more training examples, which then train a smarter AI, which can then generate even better training data in a self-reinforcing cycle [00:41:03].

## Embodied Cognition and Robotics
While not strictly necessary for achieving AGI, the integration of AGI with robotics provides an "amazingly detailed simulation for free" through interaction with the physical universe [00:43:00]. A human-like mind would benefit from having a human-like body because many aspects of the human mind are attuned to it, such as eye-hand coordination or understanding the "narrative self" and the relation between self and other [00:47:22]. Embodiment could help an AGI understand human values, culture, and psychology, making it more relatable [00:48:30].