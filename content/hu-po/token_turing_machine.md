---
title: Token Turing machine
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

A Token Turing Machine is a recurrent sequential model that incorporates [[tokenformer_architecture_and_its_implications | Transformers]] and token-based operations, designed to maintain an external memory [00:59:40].

## Functionality
Given inputs, a Token Turing Machine first reads features from the input features and its external memory [00:59:55]. These features are then passed to a processor, which is also a Transformer. This processor generates a set of intermediate output features [01:00:03]. These intermediate outputs are subsequently used to update the memory and produce the final output [01:00:07].

This architecture suggests that the model takes in audio-visual information, processes it, and sometimes stores it in this memory, which is then used to generate output [01:00:48].

## Comparison to Traditional Transformers
The benefit of having an external memory in a Token Turing Machine is that it reduces the total time complexity of the model to be constant with respect to 'T' (time or sequence length), specifically O(T), instead of O(T^2) [01:02:54]. In traditional [[tokenformer_architecture_and_its_implications | Transformers]], computation is based on consuming the entire sequence every time, leading to a quadratic increase in time with sequence length [01:03:11]. With an external memory, the model only consumes the fixed size of the memory, regardless of the input sequence length [01:03:30].

## Analogy to LSTMs
A Token Turing Machine can be effectively thought of as a Long Short-Term Memory (LSTM) network [01:03:56]. Like LSTMs, it possesses a fixed-size memory (or hidden state `H`) and incorporates mechanisms akin to forget gates and input gates [01:04:01]. Information is added to and removed from this memory, which then aids in predicting the next output [01:04:20]. The key difference is that while LSTMs implement these gates and memory operations at a microscopic, neuron-level, the Token Turing Machine implements these functionalities using [[tokenformer_architecture_and_its_implications | Transformers]] as its core components (processor, memory update mechanisms) [01:04:47].

## Implications
The concept of a Token Turing Machine, with its integrated memory, is considered a significant advancement, exemplified by its presence in models like [[capabilities_of_gpt4 | GPT-4o]] [01:01:02]. For instance, in a [[capabilities_of_gpt4 | GPT-4o]] demo, the model demonstrated the ability to recall events that occurred seconds earlier, even after the visual stimulus was gone [01:01:09]. This suggests the model stores information in its memory, similar to a built-in Retrieval-Augmented Generation (RAG) system [01:01:18]. This architecture hints at a future where models can maintain ongoing context and memory, moving beyond stateless inference to more stateful and continuous interaction [01:11:34].

It implies that models will become capable of more complex, context-aware behaviors by storing and retrieving relevant information over time, similar to human memory [01:14:09]. This "memory" is distinct from traditional RAG, which involves finding information in a database; here, it's more deeply integrated within the model's processing [01:13:31].