---
title: Prototyping techniques for creating castinglike structures
videoId: Vpt0gdbI4-8
---

From: [[dgelbart]] <br/> 

When dealing with three-dimensional structures that require significant rigidity, heavy weight, and machinability, it's often necessary to create them from solid material <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While [[prototyping_using_water_jet_cutting | water jet]] cutting is versatile, not all complex parts can be produced this way <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Traditional Approaches and Their Limitations

Traditionally, complex solid structures are made by:
*   **Milling from a solid block**: This method is expensive due to both material cost and machine time <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Milling from a near-net shape**: A near-net shape could be a [[casting_processes_for_plastics_and_metals | casting]], a forging, or something bent and then machined <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Most large [[techniques_to_improve_rigidity_in_structural_assemblies | machinery]] is made from [[casting_processes_for_plastics_and_metals | castings]] for this reason <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. However, in an R&D environment, [[casting_processes_for_plastics_and_metals | castings]] are a tedious process requiring patterns, making them difficult to do at home <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Weldments**: Building up structures by welding is common in industry <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. However, welding requires more skill than brazing <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> and comes with two main disadvantages:
    *   **Heavy Distortion**: Even with careful welding, shrinkage of the weld bead causes distortion <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   **Inability to Weld Dissimilar Metals**: It's not possible to weld very dissimilar metals, such as steel and brass, which might be desired for different functional parts of a machine <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Brazing as an Alternative Prototyping Method

An alternate process to create casting-like structures is to build them up from segments by brazing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Advantages of Brazing
*   **Use of Dissimilar Metals**: Brazing allows each segment of an assembly to be made from a different material, chosen for its specific properties, unlike [[casting_processes_for_plastics_and_metals | casting]] or welding which are limited in combining diverse metals <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For example, steel for strength and brass for bearing surfaces can be combined in one assembly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Less Distortion**: Brazing causes less distortion compared to welding <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Strength**: Brazed assemblies can be significantly stronger than [[casting_processes_for_plastics_and_metals | cast iron]] <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. [[casting_processes_for_plastics_and_metals | Cast iron]] is brittle and weaker than steel, often shattering when hit with a hammer <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. Brazed parts, being often made of steel segments, can bend under stress rather than breaking <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Aesthetics**: A brazed assembly, once finished, can look like a perfect [[casting_processes_for_plastics_and_metals | casting]] but with smoother surfaces <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

### The Brazing Process

#### 1. Part Preparation
*   All individual parts are typically cut out using a [[prototyping_using_water_jet_cutting | water jet]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Tabs or holes can be cut to help register the parts during assembly <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Tacking**: Parts can be tacked into place before brazing to hold them steady <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   A dowel pin or spot welder can be used <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
    *   **Laser Welder**: A laser welder, though exotic, is highly versatile for tacking. It can weld in hard-to-reach places, as long as the spot is visible under a microscope <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It can also weld dissimilar metals (e.g., aluminum to steel, silver to lead) because its pulse is so fast that oxidation is minimized, even allowing welding without an inert atmosphere <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

#### 2. Applying Brazing Material
*   Brazing is done by placing small pieces of brazing wire, typically a silver-copper alloy, along the joints <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Flux**: Flux is crucial as it makes the brazing material "wet" the metal by dissolving oxides and protecting the metal from further oxidization <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   **White Flux**: Primarily borax, commonly used for non-ferrous metals and also on iron <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   **Black Flux**: Likely a fluoride salt, more aggressive and used for stainless steel and harder-to-braze materials <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   Apply flux as a paste to create a fillet where the braze material is desired <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Wipe off excess flux for cosmetic reasons, as it can slightly attack the metal at high temperatures <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   Lay small pieces of brazing wire at the corners <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. If good wetting occurs, one piece can run everywhere, but adding more material ensures a nice fillet <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   The wire should be half-buried in the flux <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Gap Considerations**: Gaps between parts should ideally be between zero and half a millimeter for effective capillary action <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Brazing foils can be used for larger areas <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

#### 3. Oven Brazing
*   Place the assembly in an oven, typically set to about 750°C <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   The temperature should be 50-100°C above the melting point of the braze alloy to ensure complete melting and good flow <a class="yt-timestamp" data-t="00:09:57">[00:10:00]</a>. For an alloy melting at 680°C, 750°C is suitable <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   Once the piece reaches temperature, allow it to soak for about an hour per kilo of material to ensure heat absorption and equalization <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. For smaller pieces (e.g., half a kilo), half an hour might be sufficient after reaching temperature <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   After the soaking time, turn off the oven and allow the part to cool down slowly to about 500°C before handling <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

#### 4. Post-Brazing Finishing
*   Once cooled, the part can be sandblasted <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   To achieve a perfect finish for painting, sand the fillets slightly to round them up <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

> [!tip] Brazing vs. Casting
> Brazing offers the advantage of creating a "[[casting_processes_for_plastics_and_metals | casting]]" where each component can be a different metal (e.g., stainless steel inserts, hardened inserts) in a single assembly <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. This allows for tailored material properties within one rigid structure.