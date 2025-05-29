---
title: Short channel effects in transistors
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

In an ideal scenario, a [[the_commercialization_and_global_impact_of_transistors_in_technology | transistor]] would switch instantly, allowing zero current flow when the gate is closed and no resistance when open <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. However, real-world transistors exhibit imperfections, leading to what are known as short-channel effects <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. These effects began to appear after decades of shrinking the size of the original planar MOSFETs <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## Manifestations of Short Channel Effects

Short channel effects primarily manifest in two forms:

### Threshold Voltage Roll-Off and Sub-Threshold Leakage
The threshold voltage is the voltage at which the gate opens, creating a current between the source and the drain <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. When transistor channels were longer, this voltage was constant and independent of external factors <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. However, as channels shortened, the threshold voltage was observed to decrease, or "roll off" <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

This decrease in threshold voltage exacerbates "sub-threshold leakage" <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. While the gate is supposed to cleanly shut down current when its voltage drops below the threshold, a residual current, known as sub-threshold leakage, can persist <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. A lower threshold voltage directly leads to higher sub-threshold leakage <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

### Drain-Induced Barrier Lowering (DIBL)
[[the_development_and_impact_of_the_point_contact_transistor | Drain-Induced Barrier Lowering]] (DIBL) occurs when the source and drain are so close together that electrons from the source can diffuse into the drain, often bypassing the gate <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>. This results in a tiny parasitic current flow, causing the [[the_commercialization_and_global_impact_of_transistors_in_technology | transistor]] to consume power even when in standby mode <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

## Impact on Power Consumption
When these two short channel effects are multiplied across billions of [[development_of_silicon_transistors_for_tvs | transistors]] within an integrated circuit, they lead to a serious power consumption problem <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Origins and Prior Amelioration Efforts
Short channel effects originate from the interference of electric fields emitted by the source and drain <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. The original planar gate only touches the channel on one side, projecting an electric field downwards <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. However, the source and drain also project their own electric fields, which begin to encroach horizontally into the channel, "stealing" control from the gate <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

For many years, the [[impact_of_generational_shifts_in_the_semiconductor_industry | semiconductor industry]] was able to mitigate these effects <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a> by:
*   Lowering the voltage <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
*   Heavily doping the channel <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   Reducing the depths of the source and drain <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   Replacing the silicon dioxide gate oxide with materials having a higher dielectric constant (High-K dielectrics), which strengthened the gate's capacitance and its electric field to dominate the channel <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>. Intel famously used hafnium oxide in 2007 for their High-K metal gate <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

## The Need for New Structures
Ultimately, these amelioration methods ran their course, necessitating an entirely new structure to regain control of the channel from the source and drain <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. This led to the development of multi-gate [[the_invention_and_significance_of_the_first_transistors | transistors]] like the FinFET <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>, which wraps the gate around the channel on three sides <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. The Gate-All-Around (GAAFET) further iterates on this by completely surrounding the channel with the gate <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.