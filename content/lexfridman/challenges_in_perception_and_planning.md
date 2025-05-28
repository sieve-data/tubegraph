---
title: Challenges in perception and planning
videoId: Er7Dy8rvqOc
---

From: [[lexfridman]] <br/> 

The field of artificial intelligence (AI), specifically in perception and planning, faces several pivotal challenges that researchers and engineers are keen to address. These challenges stem from the complexity involved in creating systems that can understand and interact with the world around them.

## Understanding Perception

Perception is widely recognized as a significant hurdle in AI development. It involves processing and interpreting sensory information, which is vital for any intelligent system aiming to operate effectively in the real world. The difficulty arises from the need to determine what perception systems should deliver and how they should connect with other system components.

> [!quote] Quote
> "I don't think we have a very good idea of what perception should deliver... when what we're going to do with the output of perception... It's less clear when we're trying to make a one integrated intelligent agent" <a class="yt-timestamp" data-t="38:00">[38:00]</a>.

Although modern AI systems can now classify images and predict actions, there remains a fundamental challenge in understanding the structure that should be built into these systems - a structure akin to convolution in spatial reasoning - to enhance efficiency.

## The Role of Planning

AI planning involves making decisions about a system's future actions, considering a variety of potential states and actions. Planning becomes notably difficult in environments characterized by uncertainty and complexity. A core issue is how to perform hierarchical planning effectively, which requires creating abstractions in both the state space and temporal sequences of activities.

> **Hierarchical Planning**
>
> This involves making high-level decisions without delving into every detail immediately, hence leveraging abstractions to simplify complex problems <a class="yt-timestamp" data-t="30:00">[30:00]</a>.

### Markov Decision Processes (MDP) and Partially Observable Markov Decision Processes (POMDP)

MDPs allow for capturing uncertainties in decision-making processes by modeling probabilistic outcomes. However, for most real-world problems, it's hard to observe the complete state of the system, which is where POMDPs come in. They aim to address the challenge of planning under such uncertainty, but solving POMDPs optimally is often computationally infeasible <a class="yt-timestamp" data-t="21:00">[21:00]</a>.

> **Planning and Uncertainty**
>
> "We can't come up with Optimal Solutions to these problems, so we have to make approximations in modeling and solution algorithms" <a class="yt-timestamp" data-t="22:20">[22:20]</a>.

## The Intersection of Perception and Planning

A significant challenge lies in the intersection of perception and planning, where AI systems must not only interpret sensory data but also use that data to make informed decisions about future actions. The integration of these processes must account for:
- **Belief Spaces**: Understanding and utilizing a belief about the world, rather than the state itself, is crucial for reasoning under uncertainty <a class="yt-timestamp" data-t="26:30">[26:30]</a>.
- **Abstraction and Decomposition**: Both spatial and temporal abstraction are necessary to make reasoning and decision-making more manageable <a class="yt-timestamp" data-t="16:00">[16:00]</a>.

In summary, the challenges in perception and planning for AI revolve around effectively integrating complex sensory data into actionable plans and creating systems that can navigate and reason about an unpredictable world. As research continues, the aim is to find the right balance between automated learning and engineered components to build efficient and intelligent systems.