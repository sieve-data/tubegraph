---
title: Comparison of Deep Reinforcement Learning with Supervised Learning
videoId: PtAIh9KSnjo
---

From: [[lexfridman]] <br/> 
## Comparison of Deep Reinforcement Learning with Supervised Learning

Deep reinforcement learning (DRL) and supervised learning are two prominent branches of machine learning, each with unique approaches and objectives. In this article, we explore their key differences, providing a comprehensive comparison of these machine learning paradigms.

### Overview of Deep Reinforcement Learning

DRL is a subset of [[deep_reinforcement_learning_overview | reinforcement learning]] where neural networks approximate functions such as policies or value functions. In DRL, an agent interacts with an unknown environment, taking actions with the aim of maximizing cumulative rewards over time, as defined by a reward function <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This is opposed to supervised learning, which involves predicting an output based on given input-output pairs.

### Key Concepts in Deep Reinforcement Learning

1. **Agent and Environment**: The agent interacts with the environment by taking actions that lead to rewards, defining a process conditioned on actions and states both past and upcoming <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

2. **Reward Function**: The goal in DRL is defined in terms of maximizing cumulative rewards. This function quantifies the success of actions taken by the agent in achieving its goal <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

3. **Markov Decision Process**: DRL problems are often modeled as Markov Decision Processes (MDPs) involving states, actions, rewards, and transition probabilities <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Overview of Supervised Learning

In contrast, supervised learning involves learning a mapping from inputs to desired outputs based on input-output pair samples from a distribution. The model learns to minimize the classification error or regression error based on a loss function derived from training data <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Differences Between DRL and Supervised Learning

1. **Learning Approach**:
   - **DRL**: Learns via exploration and exploitation balanced by policies that maximize cumulative returns rather than fitting an explicit target <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
   - **Supervised Learning**: Involves fitting a function from labeled data points and minimizes a loss function calculated directly from prediction deviations from the known desired output <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

2. **Feedback**:
   - **DRL**: Feedback comes as reinforcement signals (rewards) which are often sparse and delayed <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
   - **Supervised Learning**: Direct feedback in the form of loss between predicted and actual labels is provided for every training sample.

3. **Objective**:
   - **DRL**: Focuses on maximizing a long-term reward, involving the acquisition of a strategy (policy) that dictates actions in various states for optimal results <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
   - **Supervised Learning**: Targets the attainment of high prediction accuracy or minimal error on unseen data from the same distribution as the training data.

4. **Application Domains**:
   - **DRL**: Suited for tasks where the sequence of actions heavily influences outcomes, such as robotics, gaming, and decision-making problems <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
   - **Supervised Learning**: Commonly used for classification and regression tasks, where clear labels for available data exist, prevalent in fields like image and speech recognition.

### Conclusion

While DRL and supervised learning share commonalities as part of the broader [[machine_learning_and_reinforcement_learning | machine learning]] landscape, their distinct approaches make each suitable for different types of problems. Understanding the specific requirements and benefits of each method enables practitioners to choose the most appropriate technique for their machine learning challenges.