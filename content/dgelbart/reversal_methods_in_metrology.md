---
title: reversal methods in metrology
videoId: cwdoUjynpEk
---

From: [[dgelbart]] <br/> 

Reversal methods represent a fundamental principle in metrology and precision instrumentation, enabling accurate measurements of geometric properties even without a perfect reference standard <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. This concept is often challenging to find extensively detailed in textbooks <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>.

## Core Principle

The basic premise of reversal methods addresses the challenge of measuring attributes like straightness, roundness, or squareness when a known, perfect reference is unavailable <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. The technique allows for the measurement of these properties without such a reference <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>.

The method involves two unknown entities. For instance, to measure the straightness of a surface (f(X)) against another surface (G(X), e.g., a table), both of which are unknown:
1.  **First Measurement**: A dial gauge scans the first unknown surface while it's positioned on the second unknown surface, recording deviations at various points along a fixed trajectory <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. This yields a measurement that is the sum of the deviations from both surfaces, represented as f(X) + G(X) <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. The individual contributions of each surface remain unknown at this stage <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.
2.  **Reversal and Second Measurement**: The first part is then flipped over, and the measurement is repeated, scanning from underneath <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. This provides a second set of readings, where the inverted part's deviation is effectively subtracted, yielding G(X) - f(X) <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

With two independent equations (f(X) + G(X) and G(X) - f(X)) and two unknowns (f(X) and G(X)) for each point, both functions can be resolved separately by taking the sum and difference of the recorded measurements <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. Any introduced tilt error due to unmatched heights between the two measurement setups can be removed from the resulting function, as it relates to the relative position rather than the intrinsic straightness <a class="yt-timestamp" data-t="00:26:48">[00:26:48]</a>.

## Applications

This concept of having multiple unknowns but enough independent equations to resolve them is highly powerful <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. It is applied in various precision tests:

*   **Spindle Measurement**: Separating runout from [[testing_and_measurement_for_flexure_systems | roundness]] when measuring a spindle <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>, <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. This can be achieved by using two probes at right angles on a perfect ball or cylinder mounted on the spindle, generating two independent signals that allow for the calculation of both runout and roundness <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.
*   **Straightness and Flatness**: Measuring the [[importance_of_surface_flatness | flatness]] or straightness of a surface without relying on a pre-calibrated reference <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>, <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>.
*   **Accurate Circle Division**: Ensuring a circle is divided accurately, as all angles must sum to 360 degrees. If the sum doesn't close, an error is detected, allowing for multiple measurements to identify and correct the error <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

The ability to expand the reversal method concept to numerous metrology tests makes it a fundamental tool in determining the [[high accuracy in machining | accuracy]] of components and systems <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.