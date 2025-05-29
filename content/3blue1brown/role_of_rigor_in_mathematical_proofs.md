---
title: Role of rigor in mathematical proofs
videoId: VYQVlVoWoPY
---

From: [[3blue1brown]] <br/> 

Mathematical proofs are the bedrock of mathematical understanding, but not all "proofs" are created equal. The concept of rigor is paramount in distinguishing valid [[mathematical_proofs_and_logical_deduction | mathematical proofs]] from [[fake_visual_proofs_in_mathematics | misleading arguments]] that may appear intuitive or elegant but lead to incorrect conclusions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Limitations of Visual Intuition

Visual or intuitive arguments, while often helpful for [[conceptualizing_mathematical_problems | understanding complex problems]], can be deceptive <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. An example is an elegant but flawed "proof" for the surface area of a sphere, which arrives at $\pi^2 R^2$ instead of the correct $4\pi R^2$ <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Similarly, a classic argument suggesting that pi equals 4 by approximating a circle with increasingly jagged polygons appears compelling <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

The flaw in such visual arguments often lies in hidden assumptions or misinterpretations of geometric properties:
*   **Sphere Surface Area** The unravelling of spherical wedges into "triangles" is problematic because, to preserve area, the wedges should bulge outward non-linearly, rather than being straight-sided triangles <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This non-linearity leads to an overlap that persists even with finer subdivisions, accounting for the incorrect result <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. This highlights that the geometry of a curved surface fundamentally differs from flat space, and flattening it without losing information is not possible <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. Limiting arguments involving small pieces on a sphere only work if the pieces get smaller in *both* directions, allowing them to appear locally flat <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Pi equals 4** In the argument where a sequence of curves converges to a circle, the *limiting curve* itself truly is the smooth circle, and the *limit of the lengths* of the approximating curves is 8 <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. The core issue is that there is no inherent reason for the limit of the lengths of the curves to be the same as the length of the limit of the curves <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This specific case serves as a counter-example, underscoring the need for careful application of limiting arguments <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## The Necessity of Mathematical Precision

To avoid such pitfalls, [[approaches_to_mathematical_problem_solving | mathematical problem solving]] demands precision and rigor:

### Defining Limits Precisely
When dealing with sequences of curves or approximations, it's crucial to be mathematically precise about what a "limit of a sequence of curves" means <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This involves parameterizing curves as functions and considering the limit of points for each parameter value <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Explicit Error Analysis
In calculus, when approximating an area under a curve with rectangles, rigor requires being explicit about the error between the approximation and the true value <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. One must argue that this error approaches zero in the limiting process <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

## Identifying Hidden Assumptions and Edge Cases

The most subtle kind of error in a proof often comes from hidden assumptions or overlooked edge cases. A prime example is the "proof" that all triangles are isosceles, which appears to follow the strict deductive style of Euclid <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

This proof involves drawing an angle bisector and a perpendicular bisector within a triangle, identifying congruent sub-triangles, and then summing side lengths <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. All the congruence relations used are valid <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

However, the proof breaks down at the very end when it sums line segments. The hidden assumption is that the intersection point (E) lies *between* the vertices A and C <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. When the geometric construction is done accurately, this intersection point for many triangles actually sits *outside* the triangle <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. This subtle positional error invalidates the additive step (e.g., AE + EC = AC) that is crucial to the argument <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## Conclusion

The "fake proofs" serve as powerful illustrations of why rigor is indispensable in mathematics. While [[mathematical_intuition_versus_analysis | visual intuition]] and elegant diagrams can guide understanding, they can never replace the need for critical thinking and rigorous deduction <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. Mathematicians, following in the footsteps of figures like Euclid, rely on deriving truths step-by-step from axioms <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. It is this commitment to rigor that ensures the validity of [[mathematical_proofs_and_logical_deduction | mathematical proofs]] and guards against false conclusions arising from hidden assumptions or subtle errors <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.