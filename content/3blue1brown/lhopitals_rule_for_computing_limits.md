---
title: LHopitals Rule for computing limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a [[Limits in calculus | limit]] is fundamental in calculus, essentially formalizing the idea of one value "approaching" another <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It is crucial for the formal definition of [[Derivative definitions and their relation to limits | derivatives]] and helps to avoid the paradoxical idea of infinitely small changes by instead asking what happens as the size of a small change approaches zero <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

While [[Epsilondelta definition of limits | the epsilon-delta definition]] provides a rigorous way to understand what "approach" means <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, a practical tool for computing [[Limits in calculus | limits]], especially in indeterminate forms, is L'Hopital's Rule <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## The Problem: Indeterminate Forms (0/0)

Many functions, while appearing continuous, may have specific points where they are undefined. Consider the function $f(x) = \frac{\sin(\pi x)}{x^2 - 1}$ <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. When attempting to evaluate this function at $x=1$, both the numerator ($\sin(\pi \cdot 1) = \sin(\pi) = 0$) and the denominator ($1^2 - 1 = 0$) become zero <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. This results in the indeterminate form $\frac{0}{0}$, meaning the function is not defined at $x=1$, and its graph would show a hole at that point <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Even though the function is undefined, the graph visually appears to approach a specific value as $x$ gets very close to 1 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. One could approximate this by plugging in a value very close to 1, like $1.00001$, which would yield a number around $-1.57$ <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. However, the question remains: is there a precise, systematic method to find this limiting value? <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>

## The Solution: L'Hopital's Rule

[[Derivative definitions and their relation to limits | Derivatives]] can be used to evaluate [[Limits in calculus | limits]] of this indeterminate form <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Intuition Behind the Rule

When two functions, $f(x)$ and $g(x)$, both equal zero at a common point $x=a$ (i.e., $f(a)=0$ and $g(a)=0$), the ratio $\frac{f(x)}{g(x)}$ is undefined at $x=a$ <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. However, we can investigate its [[Limits in calculus | limit]] as $x$ approaches $a$.

Consider a tiny "nudge" $dx$ away from $a$ <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   The change in $f(x)$ due to this nudge ($df$) is approximately $f'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. Since $f(a)=0$, the value of $f$ at the nudged point is approximately $f'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   Similarly, the change in $g(x)$ due to this nudge ($dg$) is approximately $g'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Since $g(a)=0$, the value of $g$ at the nudged point is approximately $g'(a) \cdot dx$ <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

Therefore, near the trouble point $x=a$, the ratio $\frac{f(x)}{g(x)}$ is approximately $\frac{f'(a) \cdot dx}{g'(a) \cdot dx}$ <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The $dx$ terms cancel out, leaving $\frac{f'(a)}{g'(a)}$ <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. As the nudge $dx$ becomes infinitesimally small (approaching 0), these approximations become exact, meaning this ratio of [[Derivative definitions and their relation to limits | derivatives]] gives the precise [[Limits in calculus | limit]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Rule Statement

L'Hopital's Rule states that if the [[Limits in calculus | limit]] of $\frac{f(x)}{g(x)}$ as $x$ approaches $a$ is of the indeterminate form $\frac{0}{0}$ (or $\frac{\infty}{\infty}$), then:

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
...provided the [[Limits in calculus | limit]] on the right-hand side exists <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

### Example Application

Returning to the example function $f(x) = \frac{\sin(\pi x)}{x^2 - 1}$, we want to find $\lim_{x \to 1} \frac{\sin(\pi x)}{x^2 - 1}$ <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

1.  Identify $f(x) = \sin(\pi x)$ and $g(x) = x^2 - 1$.
2.  Calculate their [[Derivative definitions and their relation to limits | derivatives]]:
    *   $f'(x) = \frac{d}{dx}(\sin(\pi x)) = \cos(\pi x) \cdot \pi$ (using the [[Sum rule for derivatives | chain rule]]) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>
    *   $g'(x) = \frac{d}{dx}(x^2 - 1) = 2x$ <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>
3.  Apply L'Hopital's Rule by taking the [[Limits in calculus | limit]] of the ratio of the derivatives:
    $\lim_{x \to 1} \frac{\pi \cos(\pi x)}{2x}$ <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>
4.  Now, plug in $x=1$ to the new expression:
    $\frac{\pi \cos(\pi \cdot 1)}{2 \cdot 1} = \frac{\pi \cdot (-1)}{2} = -\frac{\pi}{2}$ <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>, <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>

The precise limiting value is $-\frac{\pi}{2}$ <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Historical Note

Interestingly, L'Hopital's Rule was actually discovered by Johann Bernoulli. Guillaume de l'Hôpital, a wealthy mathematician, purchased the rights to some of Bernoulli's mathematical discoveries, leading to the rule being named after him <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

## Limitations and Significance

While L'Hopital's Rule is a powerful tool for computing [[Limits in calculus | limits]], it cannot be used to discover new [[Derivative definitions and their relation to limits | derivative]] formulas <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This is because applying the rule requires knowing the [[Derivative definitions and their relation to limits | derivatives]] of the numerator and denominator, which would already imply knowledge of the derivative being sought <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

Nonetheless, this rule demonstrates how [[Derivative definitions and their relation to limits | derivatives]], initially defined using [[Limits in calculus | limits]], can then be used in turn to evaluate complex [[Limits in calculus | limit]] expressions <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. It highlights the interconnectedness of concepts in calculus and provides a systematic way to deal with indeterminate forms.

> [!NOTE]
> The discussion of [[Limits in calculus | limits]] will continue with the concept of integrals and the [[Application of limits in integral calculus | Fundamental Theorem of Calculus]], further illustrating how [[Limits in calculus | limits]] provide clear meaning to delicate ideas that "flirt with infinity" <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.