---
title: Strength versus stiffness in mechanical design
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

In classical mechanical engineering, strength is often the primary concern, such as in the construction of bridges, steel cables, or airplanes <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, in the design of instruments and machine tools, stiffness is paramount <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Importance of Stiffness

For example, a microscope frame might be designed to support one ton, even though it only needs to support a glass slide, to ensure it remains completely stiff when touched <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Similarly, a lathe bed, made of cast iron, could support 10 tons, far exceeding the 10 kilograms of a typical workpiece, because stiffness, not strength, determines its necessary dimensions <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A square used for measurement also prioritizes stiffness, even though it doesn't bear any force, to prevent deflection during use <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In many industries, the focus is on stiffness over strength, and there is a significant difference between the two <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Demonstrating the Difference: Solid Bar vs. Rubber-Banded Bar

To illustrate this difference, an experiment compares the stiffness of a solid aluminum bar to an identical bar cut into two pieces and held together by rubber bands <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. While the strength of the rubber-banded bar is clearly limited by the rubber bands <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, its stiffness can be surprising.

### Experiment Setup and Results
1.  **Preparation**: Both bars were rounded at one end to prevent rocking and rested on three points <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Any play was removed by preloading, and a gauge was set to zero <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  **Solid Bar Test**: When loaded with a steel block, the solid bar showed a deflection of 12 microns <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
3.  **Rubber-Banded Bar Test**: The solid bar was replaced with the cut bar, careful to ensure it wasn't sitting on the rubber band <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. After preloading and nulling the gauge, the same load was applied <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
4.  **Surprising Outcome**: The deflection for the rubber-banded bar was only 7 microns <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

This demonstrates that the bar held together by rubber bands was significantly stiffer than the solid bar <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Explanation
The reason for this counter-intuitive result is that as long as the two pieces of the cut bar do not separate, the section in the middle behaves like a solid piece that is effectively twice as thick as the original bar <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Theoretically, doubling the thickness makes a section eight times stiffer <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Therefore, despite having virtually no strength, the rubber-banded bar was almost twice as stiff as the solid bar <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Implications for [[Design philosophy and aesthetics for functional parts | Design Philosophy]]

When designing components, understanding whether strength or stiffness is the primary requirement is crucial <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This distinction influences [[Precision and adjustability in mechanical components | design choices]] regarding materials and geometry.

The ease of manufacturing components is also a key consideration. The hierarchy of materials by ease of making is:
1.  **Wire**: Easiest and cheapest, with zero waste and minimal finishing, often bent by CNC machines without complex tooling <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
2.  **Sheet Metal**: Often very effective, sometimes even better than solid parts, especially for structures requiring many surfaces for friction-based locking mechanisms, similar to a multi-disk clutch <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
3.  **Solid**: Used when wire or sheet metal are not viable, requiring more attention to accuracy and precision <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

For parts requiring a "precision feel" or [[Precision and adjustability in mechanical components | adjustability]], rather than absolute brute-force precision, small enhancements can be made. For instance, inserting a ball bearing between an adjusting screw and a surface can provide a smooth adjustment feel, as a rough surface sliding on a very smooth one feels completely smooth <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. Precision pins like dowel pins or roller bearing pins can also be used with shafts and holes to achieve precision without machining the entire shaft <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

Furthermore, a distinction exists between designing for instruments (low load, high accuracy) and machines (high load, high stiffness, wear resistance) <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Instruments might use kinematic mounts (point contacts) for convenience, but these are unsuitable for heavy loads due to infinite pressure at contact points <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. Machine tools, conversely, rely on over-constrained designs or full surface bearings <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Aesthetics and Functionality

A good rule in [[Design philosophy and aesthetics for functional parts | design philosophy]] is that something 100% functional is often inherently beautiful <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. For example, a nail or a hammer are rarely considered ugly because they are purely functional, unlike cars which may have non-functional aesthetic additions <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. If a part has no extra material and is designed to minimize stress, it will often appear beautiful <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. Removing all unneeded material results in an aesthetically pleasing and functional design <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.