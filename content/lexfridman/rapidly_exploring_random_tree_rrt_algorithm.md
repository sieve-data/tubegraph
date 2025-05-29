---
title: Rapidly exploring random tree RRT algorithm
videoId: 0fLSf3NO0-s
---

From: [[lexfridman]] <br/> 

The Rapidly Exploring Random Tree (RRT) algorithm is a popular motion planning algorithm used in robotics to navigate complex environments. It is particularly noted for its application in autonomous vehicle systems where navigation through intricate and varied terrains is required.

## Overview

RRT is designed to efficiently explore high-dimensional spaces by randomly sampling points and connecting them to the nearest node in an existing tree of paths. This method allows the algorithm to cover a wide area quickly, making it suitable for complex motion planning problems where obstacles and constraints exist <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

> [!info] Algorithm Characteristics
> - **Random Sampling**: Adopts a probabilistic approach by sampling random points within the space.
> - **Incremental Construction**: Builds the tree incrementally by adding new nodes that connect to the closest existing node.
> - **Balancing Exploration and Exploitation**: Balances between exploring new areas and connecting existing nodes to optimize coverage and path efficiency.

## Computational Challenges

RRT was formulated to handle the computational difficulties associated with high-dimensional motion planning problems. Given the exponential growth of complexity with increases in dimensionality, the RRT algorithm provides an efficient framework that can be computationally less expensive than exhaustive search methods <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

However, a limitation identified in RRT is its tendency to converge towards non-optimal paths. Early trajectories can constrain the exploration space, leading to suboptimal outcomes due to a lack of trajectory correction mechanisms <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Advancements with RRT*

This realization led to the development of RRT*, a variant that ensures asymptotic optimality. By incorporating local path correction, RRT* iteratively refines paths to converge towards the optimal solution while maintaining the core features of the original RRT algorithm <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Applications in Autonomous Systems

RRT algorithms have been instrumental in projects such as the DARPA Urban Challenge, where autonomous vehicles were tasked with navigating complex urban terrains autonomously. The use of RRT facilitated the efficient path planning required to complete challenges such as high-density traffic navigation and intricate maneuvering around obstacles <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

## Simulation and Implementation

Simulation plays a crucial role in refining the performance of RRT algorithms. Through extensive simulation, researchers can test and iterate on the algorithmic parameters to ensure robustness and reliability under various conditions. While the RRT algorithm provided a foundational framework, its limitations necessitated ongoing testing and adaptation during real-world applications <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

## Conclusion

The RRT algorithm and its derivatives like RRT* represent a significant advancement in the field of motion planning for autonomous systems. Their ability to handle complex, high-dimensional spaces with relative computational efficiency makes them invaluable in the development and deployment of autonomous vehicles and robots. Though challenges remain in optimizing these paths under real-world constraints, continued innovation in this area promises to enhance the capabilities of intelligent autonomous systems further.