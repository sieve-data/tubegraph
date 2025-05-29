---
title: Double descent phenomenon in machine learning
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

The double descent phenomenon is a recently observed behavior in [[Developing Effective Machine Learning Models | machine learning]] models, which challenges traditional statistical understanding of model complexity and performance <a class="yt-timestamp" data-t="03:40:42">[03:40:42]</a>.

## Traditional vs. Double Descent
Traditionally, it was understood that as model complexity increases, there is a U-shaped trade-off with model performance <a class="yt-timestamp" data-t="03:49:51">[03:49:51]</a>. This means test error would first decrease, then increase <a class="yt-timestamp" data-t="05:54:54">[05:54:54]</a>. The double descent phenomenon, however, shows a *second descent* in test error as the number of parameters exceeds the number of training examples <a class="yt-timestamp" data-t="04:03:03">[04:03:03]</a>. This counterintuitive finding suggests that performance can improve again even after overfitting <a class="yt-timestamp" data-t="04:16:16">[04:16:16]</a>.

## Unraveling the "Why"
Research by Alicia Court and co-authors focuses on understanding *why* this phenomenon occurs, rather than just demonstrating *that* it happens <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. This approach aims to uncover the root cause and align new observations with established statistical intuition <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>, rather than dismissing prior knowledge <a class="yt-timestamp" data-t="04:14:11">[04:14:11]</a>.

## Geometric Explanation
The double descent curve, typically presented as a 2D plot, showing test error decreasing, then increasing, and then decreasing again <a class="yt-timestamp" data-t="05:56:56">[05:56:56]</a>, can be understood geometrically as a projection of a 3D plot <a class="yt-timestamp" data-t="06:12:12">[06:12:12]</a>.

This 3D plot involves two separate, orthogonal complexity axes <a class="yt-timestamp" data-t="06:18:18">[06:18:18]</a>. The apparent double descent arises because these axes are traversed sequentially <a class="yt-timestamp" data-t="06:25:25">[06:25:25]</a>. Each of these underlying complexity axes independently exhibits the traditional convex, U-shaped performance curve <a class="yt-timestamp" data-t="06:40:40">[06:40:40]</a>.

## Mechanism Shift and Complexity Axes
The underlying reason for double descent is a "mechanism shift" in how parameters are increased <a class="yt-timestamp" data-t="04:47:47">[04:47:47]</a>. The two complexity axes play different roles <a class="yt-timestamp" data-t="08:20:20">[08:20:20]</a>:
*   **One axis has a limit:** For instance, in decision trees, a single tree can only have as many terminal leaf nodes as there are examples in the dataset (N) <a class="yt-timestamp" data-t="08:54:54">[08:54:54]</a>.
*   **The other axis allows indefinite parameter increase:** After reaching the limit on the first axis (e.g., full-depth trees), models must switch to increasing parameters in a different way, such as adding more trees instead of more leaves to a single tree <a class="yt-timestamp" data-t="09:02:02">[09:02:02]</a>.

This transition between parameter adding mechanisms, triggered by reaching the interpolation threshold (where parameters equal training examples), creates the appearance of double descent <a class="yt-timestamp" data-t="09:16:16">[09:16:16]</a>. The threshold itself is not the cause, but rather the point where the mechanism naturally shifts <a class="yt-timestamp" data-t="09:56:56">[09:56:56]</a>.

## Implications for Understanding Machine Learning
This research underscores the importance of understanding the underlying mechanisms and "why" [[Developing Effective Machine Learning Models | machine learning]] models work, rather than just "that" they work <a class="yt-timestamp" data-t="02:25:25">[02:25:25]</a>. It highlights that the complexity of models often goes beyond a single dimension, and a deeper understanding of these multi-dimensional aspects is crucial for future advancements <a class="yt-timestamp" data-t="06:12:12">[06:12:12]</a>.

> [!NOTE] Statistical Intuition
> Alicia emphasizes the value of maintaining statistical intuition and not viewing [[Developing Effective Machine Learning Models | machine learning]] as a "magic bullet" that defies known statistical laws <a class="yt-timestamp" data-t="14:15:15">[14:15:15]</a>. Understanding failure modes is especially important for developing reliable methods <a class="yt-timestamp" data-t="14:49:49">[14:49:49]</a>.

> [!INFO] Broader Application
> While initially focused on treatment effect estimation within [[Causality and Machine Learning | machine learning and causality]], the study of double descent applies more broadly to all of supervised learning <a class="yt-timestamp" data-t="07:30:30">[07:30:30]</a>, offering insights into the general behavior of complex models.