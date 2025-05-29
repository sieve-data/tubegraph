---
title: Benefits of using directed acyclic graphs DAGs in causal inference
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

Directed Acyclic Graphs (DAGs) serve as a fundamental tool in [[causal_inference_concepts_and_applications|causal inference]], providing an intuitive and powerful way to understand and model causal relationships <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Intuitive Characterization of Causal Systems

DAGs offer a clear and visual representation of a causal system, making complex relationships easier to comprehend <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>. They allow researchers to describe the flow of information between variables <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>.

## Facilitating Identification and Bounding

One of the significant benefits of DAGs lies in their ability to aid in the identification of causal effects and the establishment of causal bounds.

### Partial Identification and Causal Bounds
Assumptions in [[causal_inference_concepts_and_applications|causal inference]] are not binary; instead, they exist on a range <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Partial identification, or causal bounding, offers a way to move beyond an "all or nothing" approach to causal effect analysis <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Instead of a single number, this method provides a lower and upper bound on the true causal effect <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. As more assumptions are added, these bounds become tighter, eventually collapsing into a point identification <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

DAGs can be visualized as a "polytope," like a multi-dimensional cube representing the causal problem <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a> <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. Each causal assumption made effectively "slices" off parts of this polytope, narrowing down the potential range of the causal effect <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a> <a class="yt-timestamp" data-t="00:49:59">[00:49:59]</a>. The upper and lower bounds correspond to the maximum and minimum points on this polytope <a class="yt-timestamp" data-t="00:49:55">[00:49:55]</a>.

### Characterizing Synthetic Control
DAGs are instrumental in formally characterizing methods like Synthetic Control <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>. This characterization makes the problem easier to analyze and discuss <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a> <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.

## Integration of Expert Knowledge

DAGs provide a framework to incorporate expert knowledge into causal models <a class="yt-timestamp" data-t="01:02:45">[01:02:45]</a> <a class="yt-timestamp" data-t="00:55:17">[00:55:17]</a>. By defining the edges and directions within a DAG, expert knowledge can constrain the search space for parameters and help build more robust models <a class="yt-timestamp" data-t="00:55:48">[00:55:48]</a>. This process, known as preference elicitation, ensures that valuable human insights are leveraged efficiently <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a> <a class="yt-timestamp" data-t="00:56:22">[00:56:22]</a>. For instance, in the causal marginal polytope framework, integrating expert knowledge about edges can continuously impact and constrain the causal bounds <a class="yt-timestamp" data-t="00:57:39">[00:57:39]</a> <a class="yt-timestamp" data-t="00:58:09">[00:58:09]</a>.

## Understanding the Causal Hierarchy (Pearl's Ladder of Causation)

The [[causal_inference_concepts_and_applications|causal hierarchy]], also known as Pearl's Causal Ladder, is an "incredibly important" concept that DAGs help to articulate <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a> <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. It clarifies the limitations of what can be inferred from different types of data:
*   **Observation Data (Level 1)**: Cheap and abundant, this data allows for statements about associations <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   **Interventional Data (Level 2)**: Such as Randomized Controlled Trials (RCTs), this data is more expensive to obtain <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. While observational data can inform about interventions, it requires making difficult-to-defend assumptions <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
*   **Counterfactual Data (Level 3)**: This level allows for "what if" questions, but counterfactual data "basically doesn't exist" in raw form <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. Moving from interventional data to counterfactual conclusions also requires strong assumptions <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.

The cost of justifying assumptions significantly increases as one moves up this ladder <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.

## Comparison with Potential Outcomes

While both DAGs and potential outcomes frameworks can be used for [[causal_inference_concepts_and_applications|causal inference]], they are "mathematically basically interchangeable" <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. DAGs, particularly through Single World Intervention Graphs (SWIGs), provide a visual and intuitive way to represent these systems <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>. While potential outcomes can sometimes be more expressive for complex causal systems, DAGs are often preferred for their clarity, especially for whiteboard discussions and collaboration <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a> <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.

## Addressing Complexity: The Divide and Conquer Approach

For complex graphs with many nodes, performing partial identification can be computationally challenging <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. However, DAGs facilitate a "divide and conquer" approach <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. Methods like the causal marginal polytope use ideas from belief propagation to break down a large graph into smaller, more manageable sub-graphs (e.g., reducing a four-node graph into four three-node graphs) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a> <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This allows for tackling causal bounding questions for larger systems, even up to 10 nodes, by overlapping these sub-worlds and adding expert knowledge <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a> <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

## Conclusion

DAGs offer significant benefits by making [[causal_inference_concepts_and_applications|causal inference]] more accessible, enabling more flexible analysis through partial identification, providing a framework for incorporating expert knowledge, and clarifying the fundamental limitations of causal inquiry through the causal hierarchy.