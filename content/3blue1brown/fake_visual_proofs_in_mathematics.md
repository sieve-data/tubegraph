---
title: Fake visual proofs in mathematics
videoId: VYQVlVoWoPY
---

From: [[3blue1brown]] <br/> 

Visual proofs can be intuitive and surprising, often simplifying complex problems into understandable situations <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. However, not all visually compelling arguments are mathematically sound. Exploring "fake" visual proofs reveals important lessons about the [[role_of_rigor_in_mathematical_proofs | role of rigor in mathematical proofs]], hidden assumptions, and the limitations of [[visual_intuition_in_calculus | visual intuition in calculus]] <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

## Case Study 1: The Surface Area of a Sphere is Pi Squared R Squared

### The 'Proof'
This proof attempts to derive a formula for the surface area of a sphere <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
1.  The sphere is subdivided into vertical slices, similar to chopping an orange <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
2.  These wedge slices from the northern hemisphere are "unraveled" to poke upwards <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
3.  Symmetrically, slices from the southern hemisphere are unraveled downwards <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
4.  These pieces are then interlaced to form a shape <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
5.  The base of this shape is the sphere's unraveled circumference (equator), with a length of `2πR` <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
6.  The height of this shape is a quarter walk around the sphere, `π/2 R` <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.
7.  As the slices become finer, the shape approaches a perfect rectangle <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.
8.  The area of this rectangle would be `(π/2 R) * (2πR) = π²R²` <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

### The Flaw
The result `π²R²` is incorrect; the true surface area of a sphere is `4πR²` <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.
*   **Misrepresentation of Wedge Shape**: When flattened accurately while preserving area, the orange wedges do not look like triangles; they should bulge outward <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
*   **Non-Linear Width**: The width across a wedge, representing a portion of a line of latitude, does not vary linearly from pole to equator; instead, it grows according to a sine curve <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **Persistent Overlap**: When interlacing the wedges, the non-linear edges cause a meaningful amount of overlap that persists even with finer subdivisions <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a> <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. This overlap accounts for the difference between the false `π²` and the true `4π` <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   **Curved Surface Geometry**: The fundamental issue is that the geometry of a curved surface is different from that of flat space, relating to [[dandelin_spheres_in_mathematical_proofs | Gaussian curvature]] <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a> <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a> <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Flattening a sphere without losing geometric information is impossible <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. Limiting arguments involving curved surfaces only work if the pieces get smaller in *both* directions to appear locally flat <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a> <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The orange wedge argument fails because pieces only get thin in one direction, maintaining curvature in the other <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

> [!EXAMPLE|Rearrangement Puzzle]
> This phenomenon is akin to "rearrangement puzzles" where pieces are moved around to seemingly create or lose area <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a> <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. The visual trick lies in subtle bulges or dents along the edges, which appear straight but are not, accounting for the area difference <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a> <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a> <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

## Case Study 2: Proving Pi = 4

### The 'Proof'
This argument attempts to show that `π = 4` <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
1.  Start with a circle (e.g., radius 1) inside a square whose sides are tangent to the circle <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. The perimeter of this square is 8 <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
2.  A sequence of curves is produced, all with a perimeter of 8, which increasingly approximate the circle <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
3.  Each iteration involves folding in the corners of the previous shape to just "kiss" the circle <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
4.  It's demonstrated that during each fold, the perimeter does not change <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
5.  While the approximations remain jagged, the claim is that the *limit* of these approximations equals the smooth circle itself <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a> <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
6.  By parameterizing the curves (`c_n(t)`) and taking the limit of points (`c_infinity(t) = lim(n->inf) c_n(t)`), this limiting function *is* the smooth circular curve <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a> <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
7.  The limit of the lengths of all the approximating curves is 8, since each individual curve has a perimeter of 8 <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
8.  Therefore, if the limit of the curves is the circle and the limit of their lengths is 8, `π` (half the circle's circumference, which is `2πR` for `R=1`) should be 4 <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

### The Flaw
*   **Order of Operations for Limits**: The fundamental issue is that the "limit of the lengths of the curves" is not necessarily the same as the "length of the limit of the curves" <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a> <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
*   **Jaggedness**: Although the sequence of curves converges pointwise to the circle, the *jaggedness* of the curves never disappears. The approximations take "inefficient steps" along the circle <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. The length operation (measuring perimeter) is not continuous with respect to this type of pointwise convergence.

> [!NOTE|Relevance to Calculus]
> This example highlights why [[visualization_in_calculus | visualization in calculus]] and limiting arguments, like those used to find the area under a curve by approximating with rectangles, require rigor <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a> <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. To make such arguments rigorous, one must explicitly account for the error between approximations and the true value, ensuring this error approaches zero in the limit <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a> <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.

## Case Study 3: All Triangles are Isosceles

### The 'Proof'
This is a [[mathematical_proofs_and_logical_deduction | Euclid-style proof]] to show that any triangle ABC is isosceles (AB = AC), which implies it must be equilateral <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a> <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a> <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

1.  Draw a triangle ABC.
2.  Draw the perpendicular bisector of side BC, intersecting BC at D <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.
3.  Draw the angle bisector of angle A, intersecting the perpendicular bisector at point P <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a> <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
4.  From P, draw a line perpendicular to AC, intersecting at E <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.
5.  From P, draw a line perpendicular to AB, intersecting at F <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
6.  **Claim 1**: Triangle AFP is congruent to triangle AEP (Angle-Angle-Side congruence: they share side AP, have angle `α` at A, and a 90-degree angle at F and E) <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a> <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.
    *   This implies AF = AE <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
    *   And PF = PE <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
7.  Draw lines PB and PC <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
8.  **Claim 2**: Triangle PDB is congruent to triangle PDC (Side-Angle-Side congruence: PD is shared, BD = CD by definition, and both have a 90-degree angle at D) <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a> <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
    *   This implies PB = PC <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
9.  **Claim 3**: Triangle PFB is congruent to triangle PEC (Side-Side-Angle congruence: PF=PE from Claim 1, PB=PC from Claim 2, and both have a 90-degree angle at F and E) <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a> <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
    *   This implies FB = EC <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a> <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
10. **Conclusion**: AB = AF + FB <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>. AC = AE + EC <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. Since AF = AE and FB = EC, then AB = AC <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.

### The Flaw
The result is [[paradoxical_and_nonintuitive_mathematical_truths | obviously false]] <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. The flaw is subtle <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.
*   **Hidden Assumption**: The proof relies on a hidden assumption that point E (and F) must lie *in between* A and C (and A and B, respectively) <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a> <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
*   **Incorrect Diagram**: In many triangles, the intersection point P of the angle bisector and the perpendicular bisector actually lies *outside* the triangle <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a> <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a> <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **Segment Addition Failure**: When P is outside, E (or F) may not lie between A and C. In such cases, the segment addition `AC = AE + EC` might be incorrect. It could be `AC = AE - EC` or `AC = EC - AE`, depending on the order of points <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.

## Conclusion

These examples demonstrate that while [[visual_proofs_and_triangle_isosceles | visual proofs]] and diagrams can offer significant intuition and clarity <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a> <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>, they do not replace the need for critical thinking and [[role_of_rigor_in_mathematical_proofs | mathematical rigor]] <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a> <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. In mathematics, it is crucial to identify hidden assumptions and consider edge cases that might invalidate an otherwise compelling argument <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. This vigilance is a cornerstone of [[mathematical_proofs_and_logical_deduction | mathematical proofs]] <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.