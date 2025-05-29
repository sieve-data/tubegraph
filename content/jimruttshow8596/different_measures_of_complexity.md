---
title: Different Measures of Complexity
videoId: nPpn_IpzBk8
---

From: [[jimruttshow8596]] <br/> 

The concept of [[measuring_complexity | measuring complexity]] is inherently difficult due to the multifaceted nature of "complexity" itself <a class="yt-timestamp" data-t="01:29:17">[01:29:17]</a>. When attempting to define it mathematically, researchers often encounter numerous approaches, each with its own strengths and limitations <a class="yt-timestamp" data-t="01:28:47">[01:28:47]</a>. This challenge is evident in the historical attempts to quantify complexity, leading to a diverse array of measures applicable across various domains <a class="yt-timestamp" data-t="02:24:30">[02:24:30]</a>.

## The Challenge of Defining Complexity

From early attempts in the mid-1980s by researchers like Seth Lloyd, the goal was to find a single mathematical measure, akin to Spock's precise readings <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. However, this proved elusive, as discussions with experts at the Santa Fe Institute in 2002 yielded 20 different ideas on how to [[measuring_complexity | measure complexity]] <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. In fact, Lloyd's own research in 1988 identified "31 measures of complexity," a number far from exhaustive <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

A core difficulty lies in [[distinguishing_complex_systems_from_complicated_systems | distinguishing complex systems from complicated systems]] or simple ones <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. A single electron, for instance, is simple but requires complex theory to understand, while three interacting electrons become complex <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Systems like the metabolism of a bacterium are clearly complex due to thousands of interacting chemical reactions and feedback loops <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. Yet, assigning a single number to its complexity is challenging <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

A key distinction often made is that complex things should require a lot of information to describe, but *shouldn't be random* <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. This highlights a fundamental problem: what one measure considers complex, another might deem simple <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Different fields often develop their own context-specific measures <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

## Types of Complexity Measures

### Algorithmic Complexity (Kolmogorov Complexity)

This measure, also known as Kolmogorov Complexity, defines the complexity of an object (like a string of numbers or a picture) as the length of the shortest computer program required to generate it <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.

*   **Pros**: It accurately reflects the simplicity of highly ordered sequences. For example, a billion ones (`1111...`) is algorithmically simple because a short program can generate it (`print 1 billion times`) <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   **Cons**: It assigns the highest complexity to random sequences (like static on a TV screen or a coin flip sequence) because the shortest program to describe them is essentially the sequence itself <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. This clashes with the intuitive understanding of "complexity" as being distinct from mere randomness <a class="yt-timestamp" data-t="09:17:00">[09:17:17]</a>.

### Shannon Entropy (Information)

Shannon entropy, developed by Claude Shannon for communications theory, measures the amount of information required to describe something, taking into account statistical regularities <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. It's the same mathematical formula independently discovered in the 19th century for thermodynamic entropy by Maxwell, Boltzmann, and Gibbs, illustrating that entropy is the information needed to describe atomic positions <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.

*   **Application**: Useful for compressing messages by assigning shorter codes to more frequent letters or patterns, as seen in Morse code or digital file compression (e.g., ZIP, GIF) <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.
*   **Limitations**: Like algorithmic complexity, it can be high for purely random systems, which are not typically considered "complex" in the intuitive sense <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

### Logical Depth (Charles Bennett)

Introduced by Charles Bennett, logical depth attempts to capture the "effort" or "time" required to produce a complex object from its simplest description <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

*   **Definition**: It measures the number of computational steps a computer must take to produce an output, starting from the shortest program for that output <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.
*   **Examples**:
    *   A string of a billion ones has low logical depth because its short generating program executes quickly <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>.
    *   A random bit string also has low logical depth because its "shortest program" is simply printing the string itself, which is fast <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
    *   The first billion digits of Pi, despite having a short mathematical description (program), require a very long computational time to produce <a class="yt-timestamp" data-t="13:51:00">[13:51:51]</a>. Thus, Pi's digits exhibit high logical depth <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
    *   Patterns generated by cellular automata, particularly those computationally universal like Rule 110, can also be logically deep because their complex output emerges from many steps of a simple rule <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>.

### Thermodynamic Depth (Pagels & Lloyd)

Developed by Seth Lloyd and Hein Pagels, thermodynamic depth is a physical analogue of logical depth <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

*   **Definition**: It quantifies the amount of physical resources (specifically, free energy) that had to be consumed and dissipated to assemble a system from its actual historical formation process <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
*   **Example**: The metabolism of a bacterium has "humongous" thermodynamic depth because it took billions of years of evolution and immense energy expenditure through natural selection to achieve its current complex state <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.
*   **Connection**: It connects physical and computational definitions of complexity via the physics of computation <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

### Effective Complexity (Gell-Mann & Lloyd)

Co-developed by Murray Gell-Mann and Seth Lloyd, effective complexity aims to combine physical and computational notions of complexity by distinguishing between random and non-random information <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.

*   **Definition**: It focuses on the "non-random" algorithmic part of a system's description <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>. It describes the organized, functional information, distinct from purely random noise (entropy) <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>.
*   **Application**:
    *   For gas in a room, the effective complexity describes macroscopic properties like percentages of gases, temperature, and pressure, not the random motion of individual molecules <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>.
    *   For a bacterium, it would encompass the organized metabolic pathways, DNA, and structures necessary for its function (e.g., taking in food, reproducing), excluding the random molecular wiggling <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.
    *   For engineered systems like a car, effective complexity refers to the blueprints and descriptions required for its functional requirements and manufacturing, not the state of every atom <a class="yt-timestamp" data-t="47:35:00">[47:35:00]</a>.
*   **Subjectivity**: Defining effective complexity often requires a subjective decision about what information is "important" based on the system's purpose or context <a class="yt-timestamp" data-t="26:01:00">[26:01:01]</a>. This leads to the concept of coarse-graining.

### Coarse-Graining

A concept developed in the 19th century by Gibbs and Maxwell, coarse-graining involves describing a system at a particular scale, effectively "tossing out" information below that scale <a class="yt-timestamp" data-t="29:14:00">[29:14:00]</a>. This approach is fundamental to defining effective complexity, as it helps determine the level of detail necessary for a given purpose <a class="yt-timestamp" data-t="29:47:00">[29:47:00]</a>.

### Fractal Dimensions

Emerging from the study of [[theoretical_and_practical_implications_of_complexity_measures | nonlinear dynamical systems]] and chaos, fractal dimensions describe patterns that are self-similar across different scales, like snowflakes or the Lorenz attractor for weather systems <a class="yt-timestamp" data-t="30:37:00">[30:37:00]</a>.

*   **Application**: While chaotic systems are intrinsically unpredictable at a micro-level, they are confined to these fractal structures (strange attractors), which allows for some level of predictability <a class="yt-timestamp" data-t="31:11:00">[31:11:00]</a>.
*   **Relevance**: Useful in fields like meteorology, where weather patterns, though complex, can be understood and partially predicted through these fractal structures <a class="yt-timestamp" data-t="34:00:00">[34:00:00]</a>.

### Mutual Information

Mutual information quantifies the information shared between different parts of a multi-subsystem complex system <a class="yt-timestamp" data-t="48:23:00">[48:23:00]</a>.

*   **Definition**: It is calculated as the sum of the information of individual pieces minus the total information, representing how much information is common between parts <a class="yt-timestamp" data-t="49:13:00">[49:13:00]</a>.
*   **Role**: While a necessary condition for complex systems (e.g., a bacterium's metabolism has vast mutual information due to communication and chemical exchanges), it is not sufficient. A system of a billion identical bits has high mutual information but is not complex <a class="yt-timestamp" data-t="49:53:00">[49:53:00]</a>.

### Integrated Information (Giulio Tononi)

Integrated information is a more intricate form of mutual information, often associated with theories of consciousness <a class="yt-timestamp" data-t="51:31:00">[51:31:00]</a>.

*   **Definition**: It measures not only shared information but also the degree to which the operation of different parts of a complex system can be inferred from each other dynamically <a class="yt-timestamp" data-t="52:03:00">[52:03:00]</a>.
*   **Application**: Brains and bacteria, which perform complex information processing, exhibit high integrated information <a class="yt-timestamp" data-t="52:19:00">[52:19:00]</a>.
*   **Controversy**: While proponents suggest high integrated information is linked to consciousness, critics argue that even simple error-correcting codes can have high integrated information without being conscious <a class="yt-timestamp" data-t="53:00:00">[53:00:00]</a>. This points to the need for clear definitions when discussing concepts like consciousness <a class="yt-timestamp" data-t="54:46:00">[54:46:00]</a>.

### Network Complexity

This broad class of measures addresses complex systems structured as networks <a class="yt-timestamp" data-t="57:21:00">[57:21:00]</a>.

*   **Examples**: Communication networks, neural connections in the brain, and power grids <a class="yt-timestamp" data-t="57:29:00">[57:29:00]</a>.
*   **Analysis**: Network complexity involves understanding the structure (e.g., different types of power plants, transmission lines) and dynamics (e.g., electricity spread, unforeseen behaviors) <a class="yt-timestamp" data-t="58:02:00">[58:02:00]</a>. These systems can exhibit chaotic regimes, especially when pushed to their limits, leading to complex emergent behaviors <a class="yt-timestamp" data-t="58:45:00">[58:45:00]</a>.

### Multiscale Entropy

Multiscale entropy relates to [[measuring_complexity | measuring complexity]] at different levels of coarse-graining <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>.

*   **Concept**: It examines how much information exists within a system at various scales. A system with high multiscale entropy possesses significant information regardless of the scale at which it's observed <a class="yt-timestamp" data-t="01:01:24">[01:01:24]</a>.
*   **Examples**: Living systems like humans, or large networks like the power grid, exhibit high multiscale entropy, with complexity at the macroscopic level down to individual cells and subcellular mechanisms (e.g., mitochondria) <a class="yt-timestamp" data-t="01:01:27">[01:01:27]</a>.
*   **Role**: Similar to mutual and integrated information, high multiscale entropy is often a symptom of [[complexity_science_and_its_implications | complex systems]], but not a definitive cause <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>. Simple fractal systems, for instance, can also have high multiscale information but may not be considered complex <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>.

## Conclusion

The core takeaway is that there is no single, universally applicable measure of complexity <a class="yt-timestamp" data-t="01:03:14">[01:03:14]</a>. Instead, there are many different ways of [[measuring_complexity | measuring complexity]], each with its own practicality and suitability for specific applications <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>. The choice of measure often depends on the domain (e.g., computer science, biology, ecology, engineering) and the specific "purpose" or aspect of complexity one wishes to study <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>. Ultimately, one should use the measure that is most useful for the task at hand <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.