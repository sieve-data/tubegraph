---
title: Visualizing mathematical operations using vector fields
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Mathematical operations, particularly those involving differential equations, can be [[visualizing_mathematical_concepts | visualized]] using [[understanding_vector_fields | vector fields]] <a class="yt-timestamp" data-t="22:15">[22:15]</a>. This approach offers an intuitive understanding of how systems evolve over time.

## Vector Fields and Differential Equations

The concept of a [[understanding_vector_fields | vector field]] is particularly useful for [[visualizing mathematical concepts | visualizing]] differential equations where the rate of change of a state is entirely determined by its current position <a class="yt-timestamp" data-t="22:20">[22:20]</a>.

In such a [[understanding_vector_fields | vector field]], at every point 'v' in space, a small vector is drawn <a class="yt-timestamp" data-t="22:29">[22:29]</a>. This vector indicates the velocity a state must have if it passes through that specific point <a class="yt-timestamp" data-t="22:29">[22:29]</a>. For differential equations where the rate of change of a vector equals a matrix 'M' times the vector itself (e.g., `dv/dt = Mv`), the [[understanding_vector_fields | vector field]] is constructed by attaching the vector `M * v` to each point `v` <a class="yt-timestamp" data-t="22:35">[22:35]</a>. This visually represents the rule that the rate of change of a state must always equal 'M' times itself <a class="yt-timestamp" data-t="24:07">[24:07]</a>.

To understand how any initial condition will evolve, one can imagine it "flowing" along this [[understanding_vector_fields | vector field]] <a class="yt-timestamp" data-t="22:54">[22:54]</a>. The velocity of this flow always matches the vector it is currently sitting on <a class="yt-timestamp" data-t="22:57">[22:57]</a>.

## Visualizing Matrix Exponents with Flow

Matrix exponentiation (`e^(M*t)`) provides a way to solve systems of differential equations <a class="yt-timestamp" data-t="16:46">[16:46]</a>. When applied to an initial condition, it yields a solution <a class="yt-timestamp" data-t="16:54">[16:54]</a>. The matrix `e^(M*t)` itself changes with time, and it acts on an initial condition, which is a vector <a class="yt-timestamp" data-t="16:58">[16:58]</a>.

The operation of matrix exponentiation can be [[visualizing mathematical concepts | visualized]] by imagining every possible initial condition flowing along the [[understanding_vector_fields | vector field]] for 't' units of time <a class="yt-timestamp" data-t="23:10">[23:10]</a>. The resulting transformation from the start to the finish is described by the matrix `e^(M*t)` <a class="yt-timestamp" data-t="23:25">[23:25]</a>.

### Examples

*   **Romeo and Juliet (90-degree rotation matrix):**
    For a system where the rate of change of love (represented by a 2D vector) is given by a 90-degree rotation matrix times itself <a class="yt-timestamp" data-t="11:30">[11:30]</a>, the corresponding [[understanding_vector_fields | vector field]] shows vectors perpendicular to the position vectors <a class="yt-timestamp" data-t="23:36">[23:36]</a>. The flow along this field is circular motion around the origin <a class="yt-timestamp" data-t="11:46">[11:46]</a>. In this case, `e^(M*t)` describes this rotation, aligning with the geometric flow <a class="yt-timestamp" data-t="23:39">[23:39]</a>. This specific scenario takes `2π` units of time to make a full revolution <a class="yt-timestamp" data-t="12:15">[12:15]</a>.

*   **Shakespearean Romeo and Juliet (Mutual Infatuation):**
    A different scenario, where Juliet's and Romeo's affections feed off each other, results in a distinct [[understanding_vector_fields | vector field]] <a class="yt-timestamp" data-t="23:45">[23:45]</a>. If they start in the upper right half of the plane (both loving each other), their feelings tend towards infinity, causing them to "feed off each other" <a class="yt-timestamp" data-t="24:19">[24:19]</a>. If they start in the other half, their feelings decline <a class="yt-timestamp" data-t="24:30">[24:30]</a>. Even without calculating `e^(M*t)`, the flow of this [[understanding_vector_fields | vector field]] suggests that the resulting matrix will "squish along one diagonal while stretching along another," becoming more extreme as time passes <a class="yt-timestamp" data-t="24:50">[24:50]</a>.

### Importance

While graphs are helpful for [[visualizing mathematical concepts | visualizing]] one-dimensional differential equations <a class="yt-timestamp" data-t="14:55">[14:55]</a>, they become less useful for higher-dimensional variants <a class="yt-timestamp" data-t="15:04">[15:04]</a>. [[Understanding vector fields | Vector fields]] provide a powerful way to [[visualizing mathematical concepts | visualize]] and intuit the behavior of such systems <a class="yt-timestamp" data-t="22:11">[22:11]</a>.