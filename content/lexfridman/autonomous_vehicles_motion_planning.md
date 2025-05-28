---
title: Autonomous vehicles motion planning
videoId: 0fLSf3NO0-s
---

From: [[lexfridman]] <br/> 

## Introduction

Autonomous vehicles, an area of significant research and development, involve various intricate technologies and methodologies that enable them to self-navigate and operate without human intervention. One of the critical components of this technology is motion planning. This article delves into the methodologies, challenges, and advancements in motion planning for autonomous vehicles as discussed by MIT professor Sertac Karaman.

## The Role of Motion Planning

Motion planning is a fundamental problem in autonomous vehicle technology, focused on finding a path for a vehicle from its current state to a desired state while avoiding obstacles. This problem is computationally challenging, especially as the dimensionality of the environment increases [00:02:22]. Motion planning in autonomous vehicles requires both computational efficiency and pathway optimization.

## Historical Context

Professor Karaman noted that about a decade ago, advancements in autonomous vehicles prompted intense research in motion planning. His involvement began with the DARPA Urban Challenge, a pivotal event demonstrating the potential of autonomous vehicles in urban environments [00:03:05].

> [!info] DARPA Urban Challenge
> 
> The DARPA Urban Challenge was a landmark competition where university teams designed autonomous vehicles to navigate complex urban environments. Teams equipped street-legal vehicles with cutting-edge sensors and computing technology to complete a course autonomously [00:23:00].

## Methodologies in Motion Planning

### RRT and RRT*

The **Rapidly-exploring Random Tree (RRT)** is a popular algorithm used in motion planning. It generates potential paths by randomly sampling the environment and connecting these samples to form a tree of possible trajectories. However, RRT can be limited by its tendency to become trapped in suboptimal paths due to its initial samples [00:05:16].

To address this limitation, Karaman introduced the **RRT* algorithm**, which improves on RRT by ensuring asymptotic optimality, meaning it can converge on the most efficient solution over time. RRT* can locally adjust paths to better solutions as more samples are added, thus correcting suboptimal trajectories [00:08:52].

### Application in Autonomous Vehicles

The RRT* algorithm has been applied in various projects within Karaman's research group, notably in developing autonomous forklifts and race car simulations. These applications illustrate RRT*'s capability to adaptively plan optimal paths in real-time [00:09:23].

## Challenges in Motion Planning

### Computational Complexity

One of the primary challenges in motion planning is computational complexity. As the state space's dimensions increase, the computation required to solve the motion planning problem scales exponentially [00:05:18].

### Dynamic Environments

Dynamic environments, where the positions of obstacles and other vehicles constantly change, pose another significant challenge. Autonomous systems must rapidly adapt their path in response to these changes to avoid collisions [00:07:36].

### Robustness and Reliability

Ensuring robustness in motion planning is crucial, especially in high-density environments where a small error can lead to significant system failures [00:18:58]. Collaborative and distributed control systems are being explored to enhance reliability in these scenarios [00:33:00].

## Future Directions

Motion planning for autonomous vehicles continues to evolve with advancements in artificial intelligence, particularly deep learning. These technologies are integrated to improve the perception and decision-making capabilities of autonomous systems [00:46:00].

Moreover, the future of autonomous vehicle systems involves improving not just the technology but also the legal, regulatory, and societal aspects to fully integrate these vehicles into everyday use [00:54:35].

### Conclusion

Motion planning is a cornerstone of autonomous vehicle technology, involving sophisticated algorithms and methodologies. Innovations like RRT* exemplify the strides being made to overcome the inherent challenges, moving towards a future where autonomous vehicles operate seamlessly and safely in complex environments.