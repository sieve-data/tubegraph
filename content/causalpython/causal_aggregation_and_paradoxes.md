---
title: Causal aggregation and paradoxes
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

## Overview of Meaningful Causal Aggregation
Utan Drew, a PhD student at UCL, presented work titled "Meaningful Causal Aggregation and Paradoxical Confounding" at the Causal Learning and Representation (CLEAR) conference [02:41:40]. This research was conducted during an internship at Amazon Research Chingan, in collaboration with Kaushik Das, Jonas Kubler, and Dominic Janzing [02:57:48].

The core finding of this work is an interesting paradox: even the property of confounding, which is a structural property of causal models, becomes ill-defined when considering ambiguous interventions on aggregated variables [03:08:14].

### Ambiguous Interventions
An "ambiguous intervention" occurs when intervening on an aggregated variable [03:44:00]. Since aggregated variables combine many fine-grained, micro-level variables, there are numerous ways to realize that intervention at the micro-level [03:48:48]. This is problematic because it's assumed that a robust causal model exists at the micro-level [04:04:22].

#### Example: Amazon Product Sales
Consider Amazon, which has millions of products, each with potentially different prices [04:10:00]. When Amazon asks a question like "If I sell more cleaning products, how would that impact my downstream revenue?" [04:21:00], "number of cleaning products sold" is an aggregated variable [04:30:54]. Selling these products in different ways (e.g., varying prices for different types of cleaning products) would have different impacts on downstream revenue [04:35:10].

### Proposed Solution
The research makes a simple realization, which they call "Natural Intervention," that can help mitigate the problem of ambiguous interventions [03:28:31]. They also attempt to generalize this observation to [[abstractions_in_causal_reasoning | laric rocks]] [03:36:00].

## Desired Impact and Future Work
Utan Drew hopes to see more academic work analyzing the consequences of ambiguous interventions, as most variables of practical interest are aggregated variables, yet academic work in this area is limited [04:48:06].

Ideally, there would be work that can learn a set of macro variables from data that are "complete in some sense" in summarizing the micro-model [05:17:00]. This would be highly useful for [[practical_applications_of_causal_methods | real-world applications]] [05:29:00].

## Related Research
Utan Drew frequently refers to a review paper titled "Multi-level Cause Effect Systems" by Christoph Kumke (2016 or 2017) [05:52:00]. This paper discusses learning sufficient macro variables for a specific model [06:03:00]. It has also provided inspiration for understanding how to mitigate "reward hacking" in large models, by considering the transfer from lower-dimensional models [06:16:00].

### How to Find This Work
To find the paper, one can search for the title "Meaningful Causal Aggregation and Related Paradoxes" or search for Utan Drew's name on Google Scholar [05:36:00].