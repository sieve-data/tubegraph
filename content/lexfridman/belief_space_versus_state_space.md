---
title: Belief space versus state space
videoId: Er7Dy8rvqOc
---

From: [[lexfridman]] <br/> 
## Belief Space versus State Space

The distinction between belief space and state space is a critical concept in artificial intelligence, particularly in the context of decision-making under uncertainty. This section explores the nuances of these two conceptual spaces, as discussed by Leslie Kaelbling, a renowned roboticist and Professor at MIT.

### Understanding State Space

In robotics and AI, the state space is a representation of all possible states that a system can occupy. Each state is characterized by a set of variables or conditions that fully describe the system at a given moment. For a system modeled as a Markov Decision Process (MDP), the state space encompasses all the information needed to make optimal decisions about future actions, assuming complete observability <a class="yt-timestamp" data-t="19:00">[19:00]</a>.

> [!info] Markov Decision Processes
> 
> An MDP is a framework used to model decision-making in environments where outcomes are partly random and partly under the control of a decision maker. The key assumption is that the current state contains all the information necessary to predict future outcomes, making it a "memoryless" process <a class="yt-timestamp" data-t="20:51">[20:51]</a>.

### Challenges with State Space

One of the primary challenges with state space is that in most real-world scenarios, complete observability is not feasible. Many systems are inherently partially observable, leading to uncertainties about the system's true state. For instance, a robot may have incomplete or noisy sensor input, making it impossible to know the exact state of the environment or the system <a class="yt-timestamp" data-t="19:23">[19:23]</a>.

### Introducing Belief Space

Belief space addresses the limitations of operating purely in state space by incorporating uncertainty into the representation. Instead of focusing on a single observed state, belief space considers a probability distribution over all possible states, representing the robot's knowledge and uncertainty about the world <a class="yt-timestamp" data-t="26:33">[26:33]</a>.

> [!info] Conceptualizing Belief Space
>
> In belief space, rather than controlling and reasoning about a definitive state, systems control their beliefs about states. This involves maintaining and updating a probability distribution over states, which can guide actions more effectively in uncertain environments <a class="yt-timestamp" data-t="26:47">[26:47]</a>.

### Applications and Advantages

Belief space is particularly advantageous in scenarios that require active information gathering. For example, autonomous vehicles constantly update their belief spaces to account for uncertainties in their sensor data and environment, making informed decisions about navigation <a class="yt-timestamp" data-t="28:58">[28:58]</a>.

### Challenges in Belief Space

While belief space provides a more robust framework for decision-making under uncertainty, it does present computational challenges. Planning within belief space can be complex and computationally expensive, necessitating approximations and heuristics to make the problems tractable <a class="yt-timestamp" data-t="22:00">[22:00]</a>.

### Conclusion

The transition from state space to belief space represents a significant advancement in the capability of AI systems to handle real-world complexities. By accounting for uncertainty and enabling more adaptive and informed decision-making, belief space offers a more sophisticated toolset for developing intelligent systems <a class="yt-timestamp" data-t="26:00">[26:00]</a>.

Kaelbling highlights that the ongoing challenge in AI is to create systems that efficiently combine learning and decision-making in complex, uncertain environments, striving towards the integration of belief space approaches in practical applications <a class="yt-timestamp" data-t="59:00">[59:00]</a>.