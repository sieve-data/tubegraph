---
title: Double Descent Phenomenon in Machine Learning
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

The Double Descent phenomenon is a counterintuitive finding in [[Machine learning and causality | machine learning]] where, unlike traditional statistical understanding, increasing model complexity does not always lead to a simple U-shaped trade-off between model complexity and performance <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Instead, after an initial decrease and increase in test error, a second descent is observed as the number of parameters exceeds the number of training examples <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This means model loss goes down, then up, but then drops again <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Understanding the Phenomenon

Alicia, a researcher at the University of Cambridge, questioned why this phenomenon occurs, noting that much prior work focused on *showing* it happens rather than *explaining* it <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Her research sought to find the root cause of this counter-intuitive behavior <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### The Mechanism Shift

Alicia and her co-authors discovered that the Double Descent phenomenon is not caused by the interpolation threshold itself, but by a "mechanism shift" that naturally occurs in the parameter increasing mechanism at this threshold <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. By understanding this root cause, the peak can be moved experimentally, and models can revert to traditional statistical intuition <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Geometric Explanation (3D vs. 2D)

The observed 2D U-shaped curve with a second descent is actually a projection of a more complex 3D phenomenon <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. The underlying reality involves two separate, orthogonal complexity axes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Each of these axes exhibits the expected convex (normal U-shaped) performance curve <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The Double Descent phenomenon appears because these two axes are traversed sequentially <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

One complexity axis typically has a limit to how many parameters can be added (e.g., up to `n`, the number of examples), while the other axis allows for an indefinite increase in parameters <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. The model must switch axes at some point because it can no longer add parameters in the initial way <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

**Example: Decision Trees**
In the case of decision trees, a tree can only have as many terminal leaf nodes as there are examples in the dataset <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Once full depth is reached, adding more parameters requires a different mechanism, such as adding more trees rather than more leaves to a single tree <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This change in the parameter-adding mechanism is distinct from merely adding single leaves <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Similar principles apply to linear regression, though it's less immediately obvious <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

This perspective highlights that the phenomenon arises from projecting 3D information into a 2D space <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>, and once this multi-dimensional aspect is understood, the Double Descent phenomenon can become almost trivial <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Broader Implications

This work applies to all of supervised learning, offering a wider context than specific areas like [[Machine Learning and Treatment Effect Estimation | treatment effect estimation]] <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. It emphasizes the importance of understanding the underlying mechanisms of [[Machine learning and causal inference methodologies | machine learning]] models, rather than just observing their performance <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Alicia advocates for getting back to statistical intuition and understanding *why* things work, not just *that* they work <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.