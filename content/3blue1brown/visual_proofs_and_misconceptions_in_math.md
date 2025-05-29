---
title: visual proofs and misconceptions in math
videoId: VYQVlVoWoPY
---

From: [[3blue1brown]] <br/> 

[[Visual approach to math concepts | Visual approaches]] and diagrams can be powerful tools for understanding and [[visualizing mathematical concepts | visualizing mathematical concepts]], often providing intuitive insights into complex problems. However, they can also lead to misconceptions if not rigorously applied. Three examples illustrate how [[creative approaches in mathematical proofs | creative approaches in mathematical proofs]] can be misleading, highlighting the critical need for precision and the dangers of hidden assumptions in mathematics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Misleading Visual Proofs

### The Surface Area of a Sphere

One deceptive proof attempts to derive the surface area of a sphere <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

#### The Fake Proof
The method involves:
1.  Subdividing a sphere into vertical slices, similar to chopping an orange <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
2.  Unraveling these wedge slices from the northern hemisphere, then symmetrically from the southern hemisphere <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
3.  Interlacing these pieces to form a shape whose area is to be determined <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
4.  The base of this shape would be the unraveled circumference of the sphere (an equator), `2 * pi * R` <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
5.  The "height" of each wedge would be a quarter-walk around the sphere, `pi/2 * R` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
6.  The idea is that as slices become finer, this shape approximates a perfect rectangle <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
7.  The area would then be `(pi/2 * R) * (2 * pi * R)`, simplifying to `pi^2 * R^2` <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

This proof is elegant, translating a hard problem into an intuitive one, but it is fundamentally incorrect <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> - <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The true surface area of a sphere is `4 * pi * R^2` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

#### Why it Fails
The core problem is that when the orange wedges are flattened accurately while preserving their area, they do not look like triangles; they bulge outward <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. The width across a wedge, as one moves from top to bottom, grows according to a sine curve (`R * sin(phi)`), not linearly <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a> - <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

When these non-linear wedges are interlaced, there is a meaningful amount of overlap that persists even with finer subdivisions <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> - <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. This overlap accounts for the difference between the incorrect `pi^2 * R^2` and the true `4 * pi * R^2` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a> - <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

The fundamental issue lies in the nature of curved surfaces. The geometry of a curved surface is fundamentally different from flat space <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a> - <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. One cannot flatten objects from a sphere without losing geometric information (related to [[Gaussian curvature]]) <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Limiting arguments that involve flattening pieces from a sphere only work if the pieces get smaller in *both* directions, allowing them to appear locally flat <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a> - <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. The orange wedges only got thin in one direction, maintaining their curvature in the other <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a> - <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

This phenomenon is similar to [[Mathematical intuition and counterintuitive results | rearrangement puzzles]] where area seems to appear or disappear due to subtle bulges or dents along seemingly straight edges <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

#### Valid Comparison: Area of a Circle
In contrast, a famous and valid visual proof for the area of a circle works similarly <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. It divides a circle into pizza wedges, straightens them out, and interlaces them to form a rectangle <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a> - <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. As slices get thinner, this approximates a perfect rectangle with width `pi * R` (half the circumference) and height `R` (the radius), yielding an area of `pi * R^2` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a> - <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This works because a circle can be flattened onto a plane without inherent distortion in the same way a sphere cannot.

### The Proof that Pi Equals 4

Another classic argument attempts to prove that `pi = 4` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

#### The Fake Proof
1.  Start with a circle of radius 1 (circumference `2 * pi`) <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  Draw a square whose sides are tangent to the circle. Its perimeter is 8 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a> - <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
3.  Generate a sequence of curves by repeatedly folding in the corners of the previous shape, so they "kiss" the circle <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> - <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
4.  At each fold, the perimeter remains 8 because a path (e.g., up then left) is replaced by an equivalent path (left then up), preserving total length <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> - <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
5.  As the number of iterations increases, the jagged curves more closely approximate the circle <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> - <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
6.  The *limit* of these curves is the smooth circle itself <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> - <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a> - <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
7.  Since each approximating curve has a perimeter of 8, the limit of their lengths is also 8 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> - <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
8.  Therefore, the circumference of the circle (which is `2 * pi`) must be 8, implying `pi = 4` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

#### Why it Fails
The crucial error here lies in a common misconception about limits:
> [05:25] There is no reason to expect that the limit of the lengths of the curves is the same as the length of the limits of the curves.

While the *limit* of the sequence of jagged curves *is* the smooth circle <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a> - <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, and the *limit* of their lengths is 8 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, these two limits are not interchangeable when dealing with properties like length in this specific context <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> - <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. The jagged approximations always take "inefficient steps" along the curve <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a> - <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

This example serves as a vital [[mathematical_intuition_and_counterintuitive_results | counter-example]] to highlight the care required when applying limiting arguments, especially in calculus <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> - <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. For instance, when approximating the area under a curve with rectangles, the error between the approximation and the true area must approach zero as the rectangles become thinner <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a> - <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This requires rigorous definitions of error bounds, which are not met in the pi=4 case for length.

### The Proof that All Triangles are Isosceles

A more subtle example uses Euclid-style geometric deduction to "prove" that all triangles are isosceles (and by extension, equilateral) <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> - <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

#### The Fake Proof
Given an arbitrary triangle ABC:
1.  Draw the perpendicular bisector of side BC <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
2.  Draw the angle bisector at vertex A <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
3.  Let P be the intersection of these two lines <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
4.  Draw lines from P perpendicular to sides AC (at E) and AB (at F) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> - <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
5.  **Claim 1:** Triangle AFP is congruent to triangle AEP (by Angle-Side-Angle: AP shared, angle A bisected, right angles at F and E) <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a> - <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This implies AF = AE and PF = PE.
6.  Draw lines PB and PC <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
7.  **Claim 2:** Triangle PDB is congruent to triangle PDC (by Side-Angle-Side: PD shared, BD = CD, right angles at D) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a> - <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This implies PB = PC.
8.  **Claim 3:** Triangle PFB is congruent to triangle PEC (by Side-Side-Angle: PF = PE (from Claim 1), PB = PC (from Claim 2), right angles at F and E) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a> - <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This implies FB = EC.
9.  From Claim 1, AF = AE <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. From Claim 3, FB = EC <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
10. Adding these lengths: `AF + FB = AB` and `AE + EC = AC` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a> - <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
11. Therefore, `AB = AC`, proving the triangle is isosceles <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a> - <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

The visual representation of this proof initially appears convincing <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

#### Why it Fails
Every single congruence claim in this proof is mathematically valid <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a> - <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. The error is extremely subtle and relies on a hidden assumption in the final step.

The breakdown occurs when summing the lengths: `AE + EC = AC` <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. This equality is only true if point E lies *between* A and C <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a> - <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. For many triangles, when the construction is done carefully, the intersection point P (of the angle bisector and perpendicular bisector) actually sits *outside* the triangle <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a> - <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. In such cases, point E would lie *outside* the segment AC, making the sum `AE + EC` not equal to `AC` (it would be `AE - EC` or `EC - AE` depending on the configuration) <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

This example powerfully demonstrates the dangers of relying solely on [[role_of_visual_reasoning_in_mathematical_proofs | visual reasoning]] and diagrams without rigorous proof, highlighting the importance of considering all possible configurations and edge cases in geometry <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a> - <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. [[Understanding difficult math problems | Understanding difficult math problems]] and developing [[problemsolving strategies in mathematics | problemsolving strategies in mathematics]] often requires looking beyond initial visual impressions.

## Conclusion

While visual intuition is invaluable for generating hypotheses and understanding mathematical concepts, it must always be supported by rigorous proofs <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a> - <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. [[Spatial intuition in math | Spatial intuition]] can be a powerful guide, but cannot replace the need for critical thinking, explicit confirmation of assumptions, and careful consideration of all potential edge cases in mathematical reasoning <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.