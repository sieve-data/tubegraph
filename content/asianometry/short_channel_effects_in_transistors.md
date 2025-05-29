---
title: Short channel effects in transistors
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

In an ideal scenario, a transistor would switch instantly, with zero current flow when the gate is closed and no resistance when open <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. However, this perfection is not achieved in reality <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. After decades of shrinking the size of the original planar MOSFETs, the semiconductor industry began to experience a series of issues known as "short-channel effects" <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## Manifestations of Short Channel Effects

Short channel effects primarily manifest in two forms:

### Threshold Voltage Roll-Off
The threshold voltage is the voltage at which the transistor's gate opens, creating a current between the source and the drain <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. When transistor channels were longer, this voltage was constant and independent of external factors <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. However, as the channel length decreased, the threshold voltage was observed to decrease, or "roll off" <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

This roll-off exacerbates "sub-threshold leakage" <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Sub-threshold leakage is the residual current that flows when the gate's voltage is below the threshold, even though it is supposed to cleanly shut down the current <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. A lower threshold voltage directly leads to higher sub-threshold leakage <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

### Drain-Induced Barrier Lowering (DIBL)
[[DIBL]] occurs when the source and the drain are so close together that electrons from the source can diffuse into the drain, sometimes "burrowing under the gate" <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>. This results in a tiny parasitic current flow, causing the transistor to consume power even when it is in "standby" mode <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

## Consequences
When these two short channel effects are multiplied across billions of transistors in an integrated circuit, they lead to a serious power consumption problem <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Origin and Mitigation

Short channel effects originate from the interference of electric fields from the source and drain <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. While the original planar gate only touches the channel on one side and projects an electric field downwards, the source and drain project their own electric fields horizontally into the channel <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. This encroaching field "steals" control away from the gate <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

For years, the industry anticipated these issues and managed to alleviate them by:
*   Lowering the voltage <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
*   Heavily doping the channel <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
*   Reducing the depths of the source and drain <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

A significant advancement was replacing the silicon dioxide gate oxide with one having a higher dielectric constant (High-K dielectric) <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>. This strengthened the gate's capacitance, making its electric field more powerful and better able to dominate the channel <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. Intel famously used High-K dielectrics like hafnium oxide in 2007 for their High-K metal gate, which also paved the way for advanced atomic layer deposition techniques <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

However, these methods eventually ran their course, necessitating an entirely new structure to regain control of the channel <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

## Moving to Multigate Transistors
To address short channel effects structurally, [[advancements_in_semiconductor_technology | multi-gate transistors]] were proposed <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. In 1984, Japanese researchers Sekigawa and Hayashi proposed a "double-gate MOS" transistor (XMOS) with two connected gates <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.

This concept led to the development of the [[FinFET]], which intensified the gate's control by wrapping it around the channel (the "fin") on three sides <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. The first commercial [[FinFET]] devices were produced by Intel in 2011 at the 22-nanometer process node, with TSMC and Samsung following in 2013 <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. This marked a significant [[transition_from_vacuum_tubes_to_transistors | transition from planar to 3D transistors]] <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

The next evolution is the [[gateallaround_transistor_technology | Gate-All-Around (GAAFET)]], which takes the [[FinFET]] concept further by completely wrapping the gate around the channel <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. This design was first described in a 1990 paper <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>. [[GAAFET]]s are a class of transistors where the gate fully surrounds the channel <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. Within the [[GAAFET]] category, there are nanowire and nanosheet sub-categories, referring to the shape of the channel <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

The [[gateallaround_transistor_technology | Gate-All-Around]] transition offers significant benefits, particularly in power draw. A 2020 study found that a nanosheet [[gateallaround_transistor_technology | GAAFET]] draws approximately 20-35% less power when turned off compared to a [[FinFET]] <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>. While speed and density gains are less dramatic (around 10% for speed at constant power and 15% for density), the power efficiency is highly attractive for mobile and AI processing applications <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>. This has led to "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage" for TSMC's upcoming N2 process node, which will incorporate [[gateallaround_transistor_technology | GAAFETs]] <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.