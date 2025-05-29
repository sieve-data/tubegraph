---
title: Ways to measure complexity
videoId: nPpn_IpzBk8
---

From: [[jimruttshow8596]] <br/> 

Measuring complexity is a long-standing challenge, with many different approaches proposed across various fields <a class="yt-timestamp" data-t="01:25:27">[01:25:27]</a>. Seth Lloyd began working on this problem around 1986 or 1987, inspired by a challenge from his supervisor Hein Pagels to develop a mathematical measure of complexity <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. However, complexity is inherently difficult to characterize and measure <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

At the Santa Fe Institute, where [[complexity_theory_and_systems_thinking | complexity theory]] is a core focus, there were as many as 20 different ideas on how to measure it from different researchers <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Lloyd himself once gave a talk titled "31 Measures of Complexity" <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. The fundamental issue is that complexity is a broad class of phenomena that applies to qualitatively different systems, meaning each field often develops its own suitable measures <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Even seemingly simple entities, like an electron, require complex theory to understand, and interactions between multiple simple entities, such as the three-body problem in gravity, quickly become complex <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

The metabolism of a bacterium serves as a good example of a truly complex system, involving thousands of chemical reactions and feedback loops, yet quantifying its complexity with a single number remains difficult <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## Measures of Complexity

### Algorithmic Complexity (Kolmogorov Complexity)
[[Algorithmic complexity and Shannon entropy | Algorithmic complexity]], also known as Kolmogorov complexity, measures the shortest possible computer program required to generate a given sequence or object <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
*   **Ordered Systems**: Highly ordered or simple sequences, like a billion ones ("1111..."), have very low algorithmic complexity because a short program can generate them (e.g., "print one a billion times") <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   **Disordered Systems**: Completely disordered or random sequences, like static on a TV screen or a coin flip sequence, have high algorithmic complexity because the shortest program to describe them is essentially the sequence itself, as there's no way to compress it <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Limitation**: While it accurately captures the simplicity of ordered things, it assigns high complexity to random data, which is often not intuitively considered complex <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. A system desired to be "complex" should require a lot of information to describe but should *not* be random <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

### Shannon Entropy
[[Algorithmic complexity and Shannon entropy | Shannon entropy]] is a measure of information that quantifies the amount of uncertainty or randomness in a system or message <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.
*   **Historical Connection**: It shares the same mathematical formula developed by 19th-century physicists like James Clerk Maxwell, Ludwig Boltzmann, and Josiah Willard Gibbs to describe thermodynamic entropy, realizing that entropy is the information required to describe the positions of atoms and molecules <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **Compression**: Shannon was interested in how efficiently messages could be compressed, taking into account statistical regularities <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. For instance, a billion ones can be easily compressed to a short instruction <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.

### Logical Depth
Introduced by Charles Bennett, logical depth measures complexity by the computational time required to produce an object from its shortest possible description <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.
*   **Distinction**: Unlike algorithmic complexity, logical depth differentiates between simple ordered sequences (e.g., a billion ones, easy to produce) and purely random sequences (which are also easy to produce by simply listing them) <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>, <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.
*   **Example: Pi**: The first billion digits of Pi are considered logically deep <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>. While there are short programs to calculate Pi (e.g., the ancient Greek method of inscribing polygons), these computations take a long time to produce many digits <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>, <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Cellular Automata**: Complex patterns generated by [[Complexity in systems like networks and fractals | cellular automata]], such as Wolfram's Rule 110, are also logically deep because their generation requires executing all intermediate steps <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.

### Thermodynamic Depth
Defined by Seth Lloyd and Hein Pagels for Lloyd's PhD thesis, thermodynamic depth is a physical analogue of logical depth <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.
*   **Physical Resources**: It measures the amount of physical resources, specifically free energy, that had to be consumed and dissipated to assemble a system from its initial state <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
*   **Example: Bacterium Metabolism**: The thermodynamic depth of bacterial metabolism is "humongous" because it took billions of years of evolution and immense energy consumption through natural selection to produce such complex organization <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.
*   **Connection to Computation**: It can be mathematically and physically defined and connected to computational measures through the physics of computation <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.

### [[Effective complexity and integrated information | Effective Complexity]]
Developed by Murray Gell-Mann and Seth Lloyd, [[Effective complexity and integrated information | effective complexity]] combines physical and computational notions of complexity <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.
*   **Distinction**: It focuses on the "non-random" structured information necessary to describe a system, discarding the purely random or chaotic information (entropy) <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>.
*   **Example: Air in a Room**: The effective complexity of air in a room would describe macroscopic properties like percentages of gases, temperature, and pressure (tens to hundreds of thousands of bits), not the vast, random microscopic motions of individual molecules (tens of billions of billions of bits) <a class="yt-timestamp" data-t="21:45:00">[21:45:00]</a>.
*   **Example: Bacterium**: For a bacterium, it would encompass the description of its metabolic organization and DNA required for its function (e.g., reproduction), abstracting away individual molecular wiggling <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.
*   **Subjectivity**: Defining [[Effective complexity and integrated information | effective complexity]] requires defining the "purpose" or important features of the system, which can introduce a subjective element <a class="yt-timestamp" data-t="26:05:00">[26:05:00]</a>.
*   **Coarse-Graining**: This measure utilizes the concept of coarse-graining, a technique for simplifying descriptions by ignoring fine-grained details and focusing only on relevant features at a particular scale <a class="yt-timestamp" data-t="29:12:00">[29:12:00]</a>.

### Fractal Dimensions
[[Complexity in systems like networks and fractals | Fractal dimensions]] are used to characterize the complexity of self-similar patterns found in nonlinear dynamical systems and chaos theory, such as snowflakes or the Lorenz attractor <a class="yt-timestamp" data-t="30:37:00">[30:37:00]</a>.
*   **Unpredictability vs. Predictability**: While systems like weather are intrinsically unpredictable due to their chaotic nature (sensitive dependence on initial conditions), their dynamics are often confined to "strange attractors" with [[Complexity in systems like networks and fractals | fractal structures]]. This confinement means that despite small-scale unpredictability, there can still be large-scale patterns and partial predictability <a class="yt-timestamp" data-t="31:11:00">[31:11:00]</a>, <a class="yt-timestamp" data-t="34:55:00">[34:55:00]</a>.

### Lempel-Ziv Complexity (LZW)
Lempel-Ziv-Welch (LZW) complexity is a measure based on data compression algorithms <a class="yt-timestamp" data-t="38:39:00">[38:39:00]</a>.
*   **Adaptive Compression**: Unlike Shannon entropy, which requires pre-calculating statistical regularities, LZW adaptively learns patterns in a message on the fly. It assigns shorter codes to increasingly frequent combinations of letters or words as it processes the data <a class="yt-timestamp" data-t="38:59:00">[38:59:00]</a>.
*   **Efficiency**: LZW can encode and decode information efficiently, asymptotically achieving the Shannon bound for compression as message length increases <a class="yt-timestamp" data-t="39:42:00">[39:42:00]</a>.
*   **Application**: LZW algorithms are widely used in file compression, such as ZIP and GIF formats <a class="yt-timestamp" data-t="40:04:00">[40:04:00]</a>. A key property is that once a message is compressed, further compression does not reduce its size; rather, it typically makes it larger, as the compressed form is more random <a class="yt-timestamp" data-t="40:51:00">[40:51:00]</a>.

### Statistical Complexity (Epsilon Machines)
Developed by Jim Crutchfield and Young, statistical complexity measures the size of the simplest computational machine (an automaton) that can reproduce a given message or text with the same statistical regularities <a class="yt-timestamp" data-t="41:06:00">[41:06:00]</a>.
*   **Computational Device**: An automaton is a device with different states that produces outputs as it moves from state to state <a class="yt-timestamp" data-t="42:15:00">[42:15:00]</a>.
*   **Epsilon Machine**: The "Epsilon machine" refers to the minimal automaton that can reproduce the statistical properties of a message up to a given accuracy (epsilon) <a class="yt-timestamp" data-t="43:03:00">[43:03:00]</a>.
*   **Relevance**: This concept is relevant to modern large language models, which can be thought of as complex automata trained on vast text corpora to reproduce linguistic patterns <a class="yt-timestamp" data-t="43:25:00">[43:25:00]</a>.

### Mutual Information
Mutual information quantifies the amount of information that different subsystems within a complex system possess in common <a class="yt-timestamp" data-t="48:23:00">[48:23:00]</a>.
*   **Shared Information**: If two bits are always the same (e.g., 00 or 11), they share one bit of mutual information <a class="yt-timestamp" data-t="48:55:00">[48:55:00]</a>.
*   **Symptom of Complexity**: Mutual information is often a symptom of complexity; it is difficult to imagine a complex system without a high degree of shared information and communication between its parts, like the components of a bacterium's metabolism <a class="yt-timestamp" data-t="49:32:00">[49:32:00]</a>.
*   **Limitation**: However, a high mutual information alone does not guarantee complexity. A system of a billion identical bits, for example, has high mutual information but is not considered complex <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. It is a necessary but insufficient condition for complexity <a class="yt-timestamp" data-t="50:44:00">[50:44:00]</a>.

### [[Effective complexity and integrated information | Integrated Information]]
Developed by Giulio Tononi, [[Effective complexity and integrated information | integrated information]] is a more intricate form of mutual information, often associated with theories of consciousness <a class="yt-timestamp" data-t="51:00:00">[51:00:00]</a>.
*   **Interdependence**: It measures the extent to which a system's parts are causally interdependent and contribute to the system's overall state in a way that cannot be reduced to the sum of its parts <a class="yt-timestamp" data-t="52:03:00">[52:03:00]</a>.
*   **High in Complex Systems**: Systems like brains or bacteria have high integrated information due to extensive communication and interconnected processes <a class="yt-timestamp" data-t="51:51:00">[51:51:00]</a>.
*   **Distinction from Complexity**: Like mutual information, a high degree of [[Effective complexity and integrated information | integrated information]] does not necessarily mean a system is complex in an intuitive sense. For example, a simple error-correcting code can have high integrated information because every part of the system redundantly contains information about the message, allowing reconstruction even if many bits are corrupted <a class="yt-timestamp" data-t="52:41:00">[52:41:00]</a>.

### [[Complexity in systems like networks and fractals | Network Complexity]]
[[Complexity in systems like networks and fractals | Network complexity]] refers to a class of ideas concerning the structure and behavior of complex networks <a class="yt-timestamp" data-t="57:21:00">[57:21:00]</a>.
*   **Examples**: These include communication networks, neural connections in the brain, and power grids <a class="yt-timestamp" data-t="57:29:00">[57:29:00]</a>.
*   **Structure and Dynamics**: Network complexity involves understanding the varied components (e.g., power plants of different sizes and types in a grid) and how their interconnections lead to emergent, often unforeseen, dynamic behaviors. These systems can exhibit chaotic regimes, especially when pushed to their operational limits <a class="yt-timestamp" data-t="58:02:00">[58:02:00]</a>.

### Multiscale Entropy
Multiscale entropy assesses the amount of information present in a system at different levels of coarse-graining (or scales) <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>.
*   **Scale-Dependent Information**: A system is described by focusing on specific features at a particular scale, discarding information at finer scales. For example, gas in a room can be described by temperature and pressure, ignoring individual molecule movements <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.
*   **Information Across Scales**: Complex systems, particularly living systems or networks, tend to possess a significant amount of information at each successive scale <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. For instance, a human body is complex at the macroscopic level, the organ level, the cellular level, and even within cellular organelles like mitochondria <a class="yt-timestamp" data-t="01:01:27">[01:01:27]</a>.
*   **Symptom, Not Cause**: Similar to mutual and integrated information, high multiscale entropy is a symptom of complexity, but not a sole determinant. Simple fractal systems, for example, exhibit multiscale information but may not be considered highly complex <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>.

## Conclusion

The discourse on complexity reveals that there is no single, universally applicable measure of complexity <a class="yt-timestamp" data-t="01:03:14">[01:03:14]</a>. Instead, there are many different approaches, each with its own practical applications and limitations <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>. The choice of measure often depends on the specific domain and the purpose of the analysis, whether it's quantifying descriptive difficulty, the effort required to create something, or the functional aspects of an engineered system <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>.