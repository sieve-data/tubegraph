---
title: Visualizing derivatives beyond graphs
videoId: CfW845LNObM
---

From: [[3blue1brown]] <br/> 

While many initial [[visualizing_derivatives_using_graphs | visual intuitions from that first year are based on graphs]] in calculus, and [[geometric_interpretation_of_derivatives | the derivative is the slope of a graph]], this approach becomes limited when you [[calculating_derivatives_and_their_applications | generalize calculus beyond functions]] whose inputs and outputs are simple numbers. If your [[understanding_what_a_derivative_is | intuitions for the fundamental ideas, like derivatives]] are too rigidly rooted in graphs, it can create unnecessary conceptual hurdles for advanced topics like multivariable calculus and complex analysis <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

An alternative perspective, referred to as the [[transformational_view_of_derivatives | transformational view]], offers a more seamless generalization into broader contexts where calculus is applied <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

## The Standard Graphical View (and its Limitations)

In typical calculus courses, the [[visualizing_mathematical_concepts | standard visual]] for a function with real number inputs and outputs is its graph. Here, the [[geometric_interpretation_of_derivatives | derivative gives you the slope of this graph]] <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. This means the derivative of a function is a new function that returns the slope for every input `x` <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

However, it's important not to consider this "derivative as slope" idea as the sole [[understanding_what_a_derivative_is | definition of a derivative]] <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. Fundamentally, a derivative is about [[understanding_what_a_derivative_is | how sensitive the function is to tiny little nudges around the input]] <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. The slope is merely one way to conceptualize this sensitivity within the context of graphs <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

## The Transformational View of Derivatives

The basic idea behind the [[transformational_view_of_derivatives | alternate visual for the derivative]] is to conceive of a function as mapping input points on one number line to their corresponding outputs on a different number line <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. In this context, what the [[transformational_view_of_derivatives | derivative gives you is a measure of how much the input space gets stretched or squished]] in different regions <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. If you zoom in on evenly spaced points around a specific input, the derivative indicates how spread out or contracted those points become after the function's mapping <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

### Examples with `x^2`

*   **Stretching (Derivative > 1)**: For the function `x^2`, if you zoom in on points around the input `x = 1`, they tend to get stretched out by a factor of approximately 2 <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. This represents the [[computing_derivatives_of_functions | derivative of x2 at the input x equals 1 to be 2]] <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. Similarly, around `x = 3`, points are stretched by a factor of 6, meaning the [[computing_derivatives_of_functions | derivative of this function at the input 3 to equal 6]] <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   **Contracting (Derivative < 1)**: Around `x = 0.25`, a small region gets contracted by a factor of 0.5 <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. This is what it looks like for a [[calculating_derivatives_and_their_applications | derivative to be smaller than 1]] <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
*   **Collapsing (Derivative = 0)**: At the input `x = 0`, as you zoom in closer and closer, a small neighborhood of points appears to collapse into 0 itself <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. This represents the [[calculating_derivatives_and_their_applications | derivative to be 0]] <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **Flipping and Stretching/Contracting (Negative Derivative)**: For negative inputs like `x = -2`, the points in a small neighborhood not only get stretched out but also get flipped around <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. The action looks increasingly like multiplying by -4 as you zoom in <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. This demonstrates what it looks like for the [[calculating_derivatives_and_their_applications | derivative of a function to be negative]] <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

While visualizing entire functions as transformations can be clunky due to output values colliding, this view is highly effective for understanding local behavior around a given input <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Application: Analyzing Fixed Points of Functions

This transformational understanding of derivatives is particularly useful for [[applications_of_derivatives_in_realworld_phenomena | solving a problem]] related to repeated function application, such as evaluating an infinite fraction like `1 + 1/(1 + 1/(1 + ...))` <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

This infinite fraction is a fixed point of the function `f(x) = 1 + 1/x` <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. Solving `x = 1 + 1/x` yields two solutions:
1.  The golden ratio, phi (approximately 1.618) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
2.  Negative 1 divided by phi (approximately -0.618) <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

A common approach to seeing which value the infinite fraction converges to is to numerically apply the function repeatedly. Starting with almost any random number and repeatedly plugging it into `1 + 1/x` will consistently lead to 1.618 <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

### Graph-Based Visualization vs. Transformational View for Fixed Points

Traditionally, problems like this are taught using [[visualizing_derivatives_using_graphs | graphs]] with a "spiderweb" diagram <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. By plotting `y = f(x)` and `y = x`, you trace from an input `x` to its output `y = f(x)`, then horizontally to `y = x` to make that output the new input `x`, and then vertically back to `f(x)` <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>. This process visually shows convergence or divergence from fixed points based on the slopes of the function relative to `y = x` <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

However, the [[understanding_what_a_derivative_is | transformational view]] offers a more intuitive understanding <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. When repeatedly applying a function like `1 + 1/x` in this view:
*   **Stable Fixed Point (Attractor)**: For phi (1.618), zooming in on a neighborhood around it shows that points in that region get *contracted* towards phi with each application <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. The derivative of `1 + 1/x` at `x = phi` has a magnitude less than 1 (specifically, the [[calculating_derivatives_and_their_applications | derivative works out to be around negative 0.38]]) <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>. This contraction acts like a gravitational pull, explaining why numerical iterations converge to phi <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Unstable Fixed Point (Repeller)**: For phi's little brother (-0.618), the derivative actually has a [[calculating_derivatives_and_their_applications | magnitude larger than 1]] <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. This means points near this fixed point are *repelled* away from it, getting stretched by more than a factor of 2 in each iteration <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

This demonstrates a useful fact: the stability of a fixed point is determined by whether the magnitude of its derivative is larger or smaller than 1 <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.

## Conclusion

While [[transformational_view_of_derivatives | viewing derivatives as this change in density]] might be clunkier for visualizing entire functions compared to the [[visualizing_derivatives_using_graphs | graphical intuition]], it offers a more flexible and robust understanding of the derivative concept <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>. This perspective is particularly valuable for topics beyond single-variable calculus, preparing students for more advanced mathematical concepts <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.