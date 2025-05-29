---
title: Phase space and population dynamics
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

The concept of phase space can be applied to understand the dynamics of systems that are not inherently spatial, such as population sizes over time <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## State of the System
In the context of population dynamics, the "state" of a system at a given time refers to the population sizes of different species <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. For example, tracking the populations of two species, one of which preys on the other (e.g., foxes and rabbits), would involve two variables <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Phase Space
The collection of these population sizes can be represented as a point in a two-dimensional space, which is referred to as the [[applications_of_phase_space_in_differential_equations | phase space]] of the system <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Vector Fields and Population Change
The rates at which these population sizes change are influenced by factors such as reproductive rates or predator-prey interactions <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. These rates of change are typically described analytically by a set of [[differential_equations_in_physics | differential equations]] <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

A powerful way to visualize what these equations represent is to associate each point in the phase space (each pair of population sizes) with a vector <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This vector indicates the direction and magnitude of change for both variables <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

For instance, if there are many foxes but few rabbits, the fox population might decrease due to limited food, while the rabbit population might also decline due to predation, potentially faster than they can reproduce <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This vector field therefore illustrates how quickly and in what direction a given pair of population sizes tends to change <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Phase Flow
The "flow" associated with this vector field is known as the *phase flow* for the [[differential_equations_in_physics | differential equation]] <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. It provides a visual representation of how various possible starting states of the system would evolve over time <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Insights from Divergence and Curl
Operations like divergence and curl can offer insights into the system's behavior within this [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   Do the population sizes converge towards a specific set of numbers <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>?
*   Are there values from which they tend to diverge <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>?
*   Do cyclic patterns exist, and are these cycles stable or unstable <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>?

While divergence and curl are valuable tools, a complete understanding of such systems often requires additional mathematical machinery <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. However, the conceptual framework gained from studying these ideas is highly applicable to other dynamic systems <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.