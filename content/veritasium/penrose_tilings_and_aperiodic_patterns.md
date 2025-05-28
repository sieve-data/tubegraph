---
title: Penrose tilings and aperiodic patterns
videoId: 48sCx-wBs34
---

From: [[veritasium]] <br/> 

[[Penrose tilings and aperiodic patterns | Penrose tilings]] describe a pattern of shapes that can cover an infinite flat surface without ever repeating a periodic pattern <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. This concept was once thought to be impossible <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Historical Context: Johannes Kepler

The story of aperiodic patterns begins over 400 years ago in Prague with Johannes Kepler <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Kepler's Planetary Models
Kepler is most famous for discovering that planetary orbits are ellipses <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. Before this, he devised a solar system model where planets were on nested spheres separated by the [[Platonic Solids | Platonic solids]] <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. [[Platonic Solids | Platonic solids]] are objects with identical faces and vertices, allowing them to be rotated without changing their appearance <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. There are only five [[Platonic Solids | Platonic solids]]: the cube, tetrahedron, octahedron, dodecahedron (12 pentagonal sides), and icosahedron (20 sides) <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. This conveniently matched the six planets known at the time, allowing Kepler to place a unique [[Platonic Solids | Platonic solid]] between each planetary sphere as a spacer <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. He arranged them to match astronomical observations of planetary distances as closely as possible <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, driven by a deep belief in geometric regularity in the universe <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

### Kepler's Conjecture on Sphere Packing
Kepler's interest in geometry extended to practical matters, such as optimally stacking cannonballs <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. By 1611, he concluded that hexagonal close packing and face-centered cubic arrangements are the most efficient, with cannonballs occupying about 74% of the volume <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. This became known as [[Kepler's Conjecture | Kepler's Conjecture]] <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, which was only formally proven in 2017, nearly 400 years later <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

### Snowflakes and Crystal Structure
Kepler published his conjecture in a pamphlet titled *Deniva Sexangula* ("On the Six-Cornered Snowflake") <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. He wondered why snowflakes always form with six corners, never five or seven <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Though atomic theory didn't exist then, Kepler speculated about the arrangement of "smallest natural units" of water forming hexagonal crystals, similar to his cannonball stacking <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

### Tiling the Plane and Five-Fold Symmetry
Kepler knew that regular hexagons can perfectly tile a flat surface without gaps <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>, which is called periodic tiling in mathematical jargon <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. A tiling is periodic if a portion can be duplicated and the pattern continued through translation, without rotations or reflections <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

Periodic tilings can also have rotational symmetry:
*   Rhombus pattern: two-fold symmetry (180-degree rotation) <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>
*   Equilateral triangles: three-fold symmetry <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>
*   Squares: four-fold symmetry <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>
*   Hexagons: six-fold symmetry <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>

The only rotational symmetries possible for periodic tilings are two-fold, three-fold, four-fold, and six-fold <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. There is no five-fold symmetry in periodic tilings because regular pentagons do not tile the plane <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. However, Kepler attempted to create a pattern with five-fold symmetry, which he published in his book *Harmonices Mundi* ("Harmony of the World") <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. This pattern had a "certain five-fold symmetry" but was not entirely clear how it would tile the whole plane <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

Some shapes can tile the plane both periodically and non-periodically, such as isosceles triangles or sphinx tiles <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. This led to the question: can some tiles *only* tile the plane non-periodically <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>?

## The Development of Aperiodic Tilings

In 1961, Hao Wang studied multi-colored square tiles, with rules that touching edges must be the same color and tiles cannot be rotated or reflected <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. Wang conjectured that if a set of these tiles could tile the plane, they could do so periodically <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

However, Wang's conjecture was proven false by his student, Robert Berger, who found a set of 20,426 tiles that could tile the plane *only* non-periodically <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. This means the finite set of tiles could tile out to infinity without ever repeating the same pattern <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. A set of tiles that can only tile the plane non-periodically is called an aperiodic tiling <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.

Mathematicians then sought to find aperiodic tilings with fewer tiles:
*   Robert Berger: 104 tiles <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>
*   Donald Knuth: 92 tiles <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>
*   Raphael Robinson: 6 tiles <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>

### Roger Penrose's Two-Tile Solution

Ultimately, Roger Penrose reduced the number of tiles needed to just two <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. He started with a pentagon, observing that surrounding it with other pentagons left gaps <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>. His insight was to subdivide the pentagons repeatedly, revealing that the remaining gaps could be filled with specific shapes: rhombuses, stars, and a "justice cap" <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. By continuing this subdivision indefinitely, only these specific shapes would appear <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

Penrose distilled this geometry down to two specific tiles: a thick rhombus and a thin rhombus <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. Rules for how they connect (enforced by bumps, notches, or matching colors) ensure that these two tiles can *only* tile the plane non-periodically <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. His favorite pattern is made from two other shapes, called kites and darts, which have specific angles and must connect so that curves drawn on them are continuous <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

Notably, Kepler's pentagon pattern, when overlaid on Penrose's pattern, matches up perfectly <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.

## Properties of Penrose Tilings

[[Penrose tilings and aperiodic patterns | Penrose tilings]] exhibit several fascinating characteristics:

*   **Non-Repetitive but Orderly:** They extend to infinity without repeating, yet contain regularities like stars and suns that don't quite repeat as expected <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
*   **Uncountably Infinite Variations:** There are an uncountably infinite number of different [[Penrose tilings and aperiodic patterns | Penrose tiling]] patterns <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.
*   **Local Indistinguishability:** Despite infinite variations, any finite region of one tiling appears infinitely many times in all other versions <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. This makes it impossible to tell which specific pattern you are on by observing only a finite region <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Moire Patterns:** Overlapping two copies of a Penrose pattern (one on a transparency) creates a [[Moire patterns | Moire pattern]], where dark areas show pattern misalignment and light spots indicate matching <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. This demonstrates that no section can ever perfectly match the one beneath it across the entire pattern <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

### Connection to the [[The Golden Ratio | Golden Ratio]]

[[Penrose tilings and aperiodic patterns | Penrose tilings]] are intimately connected to the [[The Golden Ratio | golden ratio]] (approximately 1.618) <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>.
*   **Ratio of Kites to Darts:** The ratio of kites to darts in a Penrose pattern approaches the [[The Golden Ratio | golden ratio]] <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>. This irrational ratio is a key indicator of its non-periodic nature; if it were periodic, the ratio would be a ratio of two whole numbers <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.
*   **Five-Fold Symmetry:** The [[The Golden Ratio | golden ratio]] is considered the "most five-ish" of constants <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>, and is heavily associated with pentagons (e.g., the ratio of a pentagon's diagonal to its edge is the [[The Golden Ratio | golden ratio]]) <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. The kite and dart pieces themselves are sections of pentagons, embedding the [[The Golden Ratio | golden ratio]] directly into their construction <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
*   **Fibonacci Sequence in Parallel Lines:** Drawing specific straight lines on the tiles reveals five sets of parallel lines <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>. Within any set, there are two different spacings, "long" and "short" <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. The arrangement of these long and short gaps does not follow a periodic pattern <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>. However, counting the number of long and short sections in any portion yields numbers from the [[Fibonacci sequence | Fibonacci sequence]] (e.g., 13 shorts and 21 longs) <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>. The ratio of successive Fibonacci numbers approaches the [[The Golden Ratio | golden ratio]] <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

## Quasicrystals: A Physical Analog

For a long time, scientists doubted whether [[Penrose tilings and aperiodic patterns | Penrose tilings]] could have a physical analog in nature, particularly in crystal structures <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>. Crystals were believed to be made of repeating units, and the 14 basic unit cells that compose all crystals were well-established, with no known crystal failing to fit these patterns <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.

Another challenge was that crystals are built by local atomic arrangements, whereas [[Penrose tilings and aperiodic patterns | Penrose tilings]] appeared to require long-range coordination <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. If one locally places tiles that initially seem to obey the rules, a pattern can fail later on, suggesting a need for foresight or long-range information <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.

### Discovery of Quasicrystals

In the early 1980s, Paul Steinhardt and his students used computers to model atomic arrangements in condensed matter <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>. They found that atoms locally formed icosahedrons <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>, a "forbidden shape" in traditional crystallography due to its five-fold symmetries <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>. Inspired by Penrose tilings, they designed a new kind of structure, a 3D analog of Penrose tilings, now known as a **quasi-crystal** <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>. Their simulations of X-ray diffraction from such a structure showed a pattern with rings of 10 points, reflecting the five-fold symmetry <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>.

Concurrently, completely unaware of Steinhardt's work, Dan Shechtman created a flaky material from aluminum and manganese <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. When he scattered electrons off this material, the resulting diffraction pattern almost perfectly matched Steinhardt's simulation <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.

The solution to the "long-range coordination" problem in quasicrystals lies in the local matching rules. While edge-matching rules for tiles are not strong enough and can lead to errors, rules governing how vertices connect are strong enough locally to ensure the pattern can extend to infinity without mistakes <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.

One of the seminal papers on quasicrystals was titled *Deniva Quinquangula* ("On the Pentagonal Snowflake"), a direct shout-out to Kepler <a class="yt-timestamp" data-t="18:32:00">[18:32:00]</a>.

### Recognition and Applications
The discovery of quasicrystals was met with skepticism; Nobel laureate Linus Pauling famously remarked, "There are no quasicrystals, only quasi scientists" <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>. However, Dan Shechtman was awarded the Nobel Prize in Chemistry in 2011 for his discovery <a class="yt-timestamp" data-t="19:01:00">[19:01:00]</a>.

Quasicrystals have since been grown into beautiful dodecahedral shapes <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a> and are being explored for various applications, including:
*   Non-stick electrical insulation <a class="yt-timestamp" data-t="19:12:00">[19:12:00]</a>
*   Cookware <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>
*   Ultra-durable steel <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>

The story of [[Penrose tilings and aperiodic patterns | Penrose tilings]] and quasicrystals highlights how patterns once considered impossible can exist in nature, challenging established perceptions of geometric symmetry and material science <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>.