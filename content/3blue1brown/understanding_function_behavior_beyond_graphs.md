---
title: Understanding Function Behavior Beyond Graphs
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

Traditional introductions to calculus often base visual intuition on [[Mathematical functions and graphs | graphs]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. While useful, this approach can become a conceptual hurdle when generalizing calculus beyond [[Mathematical functions and graphs | functions]] whose inputs and outputs are simple numbers <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For more advanced topics like multivariable calculus and complex analysis, it's not always possible to graph the [[Mathematical functions and graphs | function]] being analyzed <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Transformational View of [[Derivatives of simple functions and their intuition | Derivatives]]

Instead of rigidly rooting intuition in [[Mathematical functions and graphs | graphs]] where the [[Derivatives of simple functions and their intuition | derivative]] is the slope <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, a "transformational view" offers a more flexible understanding <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This perspective views a [[Mathematical functions and graphs | function]] as mapping input points on one number line to their corresponding outputs on another <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

In this view, the [[Derivatives of simple functions and their intuition | derivative]] measures how much the input space is stretched or squished in various regions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. If you zoom in around a specific input, the [[Derivatives of simple functions and their intuition | derivative]] indicates how spread out or contracted evenly spaced points become after the mapping <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Examples of the Transformational View

*   **`x^2` function:**
    *   For an input around 1, points get stretched by a factor of 2, meaning the [[Derivatives of simple functions and their intuition | derivative]] at `x=1` is 2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Around an input of 3, points are stretched by a factor of 6, indicating the [[Derivatives of simple functions and their intuition | derivative]] at `x=3` is 6 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   Around an input of 1/4, a small region is contracted by a factor of 1/2, showing what a [[Derivatives of simple functions and their intuition | derivative]] smaller than 1 looks like <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   Near an input of 0, a small neighborhood of points collapses into 0 itself, signifying a [[Derivatives of simple functions and their intuition | derivative]] of 0 <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   For negative inputs, like -2, the neighborhood not only gets stretched but also flipped around, resembling multiplication by a negative factor (e.g., -4 for -2 input), which is what a negative [[Derivatives of simple functions and their intuition | derivative]] implies <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## Application: Analyzing Repeated Fractions

The transformational view is particularly useful for understanding the behavior of repeatedly applied [[Mathematical functions and graphs | functions]]. Consider the infinite fraction `1 + 1/(1 + 1/(1 + ...))` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Finding Fixed Points

This expression can be analyzed by setting it equal to `x`, noting the self-similarity, and solving `x = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This is equivalent to finding the fixed points of the [[Mathematical functions and graphs | function]] `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. There are two solutions for `x`:
*   The golden ratio, phi (approximately 1.618) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   Negative 1 divided by phi (approximately -0.618) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Why One Fixed Point is Favored

When you repeatedly apply the [[Mathematical functions and graphs | function]] `1 + 1/x` starting with almost any random number, the result consistently converges to the golden ratio (phi) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This behavior is difficult to fully grasp with the traditional [[Mathematical functions and graphs | graph]]-based "spiderweb" method for iterating [[Mathematical functions and graphs | functions]], which can be awkward to visualize <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

The transformational view provides a clear explanation:
*   **Golden Ratio (phi):** When zooming in on a neighborhood around phi, points get **contracted** during the mapping <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. The [[Derivatives of simple functions and their intuition | derivative]] of `f(x) = 1 + 1/x` at phi has a magnitude less than 1 (approximately -0.38) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This means each repeated application scrunches the neighborhood smaller, creating a "gravitational pull" towards phi <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This is known as a **stable fixed point** <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Negative 1/phi:** In contrast, for the other fixed point, the [[Derivatives of simple functions and their intuition | derivative]] has a magnitude greater than 1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. Points near this fixed point are **repelled** away from it, being stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This is an **unstable fixed point** <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

This demonstrates a useful fact: the stability of a fixed point is determined by whether the magnitude of its [[Derivatives of simple functions and their intuition | derivative]] is larger or smaller than 1 <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. This explains why phi consistently appears in numerical calculations, while its "little brother" does not <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Broader Implications

While visualizing an entire [[Mathematical functions and graphs | function]] using the transformational view can sometimes be clunky compared to traditional [[Mathematical functions and graphs | graphs]] <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>, this perspective offers a more flexible understanding of the [[Derivatives of simple functions and their intuition | derivative]] <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. It significantly aids in comprehending advanced topics in calculus that extend beyond simple [[Mathematical functions and graphs | functions]] of numbers <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.