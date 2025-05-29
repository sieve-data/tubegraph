---
title: Surface area of a sphere visual proof
videoId: VYQVlVoWoPY
---

From: [[3blue1brown]] <br/> 

This article examines a "fake proof" for the [[surface_area_of_a_sphere | surface area of a sphere]], contrasting it with a valid proof for the area of a circle to highlight common pitfalls in visual and limiting arguments in mathematics.

## The Flawed Visual Proof

The method for calculating the [[surface_area_of_a_sphere | surface area of a sphere]] begins by subdividing the sphere into vertical slices, similar to how an orange is chopped <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

The steps are as follows:
1.  **Unraveling Wedges**: All wedge slices from the northern hemisphere are unraveled to poke upwards, and symmetrically, those from the southern hemisphere are unraveled downwards <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  **Interlacing**: These pieces are then interlaced to form a new shape <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
3.  **Dimensions**: The base of this new shape is derived from the circumference of the sphere (an unraveled equator), giving it a length of 2πR, where R is the radius <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The "height" of this shape comes from a quarter-walk around the sphere, which is π/2 * R <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
4.  **Approximation**: The idea is that as finer and finer slices are taken, this shape approximates a perfect rectangle <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
5.  **Calculated Area**: The area of this approximate rectangle would be (π/2 * R) * (2πR), which simplifies to π²R² <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

However, this proof is "completely wrong" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The true [[surface_area_of_a_sphere | surface area of a sphere]] is 4πR² <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Why the Proof Fails

The flaw in this visual proof lies in the assumption that the orange wedges flatten into perfect triangles or maintain their area when unraveled into a rectangle.

### Comparison to Valid Proofs
This flawed proof is similar in spirit to valid [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] and visual proofs, such as the one for the area of a circle <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. In the circle proof, pizza wedges are straightened and interlaced to form a rectangle, whose area (πR²) is correct because the width of the rectangle comes from half the circumference (πR) and its height from the radius (R) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The difference is subtle <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

### The Curvature Problem
When the orange wedges from the sphere are flattened, if done accurately to preserve their area, they do not look like triangles; they should bulge outward <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. The width of a wedge at different latitudes on the sphere does not grow linearly but according to a sine curve <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
This non-linear width means that when the wedges from the northern and southern hemispheres are interlaced, there is a "meaningful amount of overlap" between their non-linear edges <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This overlap persists even with finer subdivisions and accounts for the difference between the incorrect π²R² and the correct 4πR² <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

> [!NOTE] Gaussian Curvature
> The fundamental issue is that the geometry of a curved surface, like a sphere, is distinct from flat space <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This concept is related to [[Gaussian curvature]] <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. You cannot flatten a sphere without losing geometric information <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Limiting arguments involving curved surfaces only work if the pieces shrink in *both* directions, allowing them to appear locally flat <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The orange wedges, however, only got thin in one direction, maintaining their curvature in the other <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

This phenomenon is akin to rearrangement puzzles where area seemingly appears or disappears due to subtle bulges or dents in lines that appear straight <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. One must be wary of lines that appear straight without explicit confirmation <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

> [!WARNING] Visual Intuition vs. Rigor
> Visual arguments and diagrams, while helpful for intuition, "will never obviate the need for critical thinking" <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. In mathematics, it's crucial to look out for hidden assumptions and edge cases <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.