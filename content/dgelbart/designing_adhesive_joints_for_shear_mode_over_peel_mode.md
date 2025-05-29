---
title: Designing adhesive joints for shear mode over peel mode
videoId: EeEhS3zmnDg
---

From: [[dgelbart]] <br/> 

When designing structures that utilize adhesive bonding, it is crucial to understand how different loading modes affect joint strength. Proper design dictates that adhesive joints should primarily be designed to work in shear mode <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Tension mode is a less effective alternative, being much weaker <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>, while peel mode should be avoided entirely <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Understanding Loading Modes

Adhesive joints are typically subjected to three primary loading modes:

1.  **Shear Mode**: In this mode, the forces act parallel to the bonded surfaces, attempting to slide one surface past the other <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
2.  **Tension Mode**: Here, the forces act perpendicular to the bonded surfaces, attempting to pull them directly apart <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
3.  **Peel Mode**: This mode involves forces that try to separate the bonded surfaces by peeling one layer away from the other, starting from an edge <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Why Shear Mode is Superior

The fundamental difference in strength between shear and peel modes lies in how the load is distributed across the bonded area.

*   **Shear Mode**: In shear, the load is applied simultaneously across the entire bonded area <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This means the stress is distributed, allowing the full strength of the adhesive to be utilized. A properly prepared and cured shear joint, even with a 5-minute epoxy, can withstand significant forces <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. For example, a small demonstration joint might hold 2 tons <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>, scaling up to potentially hundreds of tons for a full-sized structure due to the proportional increase in area <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Peel Mode**: In stark contrast, peel mode concentrates all the load on a single line at the edge where separation begins <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. The area under stress is theoretically zero <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>, causing the joint to fail instantly, often with "zero strength" <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This phenomenon occurs regardless of the adhesive type, even with proper surface [[preparing_surfaces_for_adhesive_bonding|preparation]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Avoiding Peel Mode in Design

It is crucial to recognize that a joint may not always appear to be in peel mode but can behave as such under load <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

*   **Bracket Example**: If a bracket is glued to a surface, it might seem to be loaded in tension, but if a bending force is applied, it will peel off from one end <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Lifting Tab Example**: Even a seemingly shear-loaded tab, if lifted, will lift up and engage in peel mode <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

Any design that allows for this concentrated "peel line" will fail instantly <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

> [!CAUTION]
> Always assume an adhesive joint will fail if loaded in peel mode. This principle also applies to other bonding methods like soldering; a soldered joint can easily be ripped apart by hand if pulled in peel mode <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

## Adhesive Properties and Peel Strength

The rigidity of the adhesive plays a role in how it performs under peel stress, though it doesn't fundamentally change the design rule:

*   **Rigid Adhesives (e.g., Epoxies)**: For rigid adhesives like epoxy, the stress concentration in peel mode is nearly infinite, leading to immediate failure <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **Semi-Flexible Adhesives (e.g., Polyurethane, RTV Silicone)**: These adhesives, such as [[pros_and_cons_of_different_types_of_adhesives|polyurethane]] or [[pros_and_cons_of_different_types_of_adhesives|RTV silicone]], offer better peel strength because they can stretch and distribute the stress over a larger area behind the peel line <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. While they perform better, it is still preferable not to design joints that operate in peel mode <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.

In summary, for strong and reliable adhesive joints, always prioritize designs that direct forces into shear mode, distributing the load across the entire bonded area.