---
title: Reversal Methods in Precision Instruments and Metrology
videoId: cwdoUjynpEk
---

From: [[dgelbart]] <br/> 

Reversal methods represent a powerful concept in [[techniques_for_measuring_and_ensuring_precision_in_mechanical_parts | precision instruments]] and metrology, particularly useful for determining the accuracy of a part or surface when a perfect reference is unavailable [00:23:55]. These methods allow for the measurement of properties like straightness, flatness, or roundness without a known, perfect reference standard [00:23:37].

## Core Principle

The fundamental idea behind reversal methods is to use multiple independent measurements of unknown components to resolve their individual characteristics [00:27:31]. If there are multiple unknowns, enough independent equations must be obtained to solve for each unknown [00:27:31].

For example, when measuring how straight or flat a surface is without a perfect reference, two surfaces (e.g., a part and a table) are treated as unknowns [00:24:46].

1.  **First Measurement:** A dial gauge or similar instrument is used to scan the first unknown surface (e.g., an unknown straight edge) against a second unknown surface (e.g., a table) [00:24:16]. The readings (deviation) are recorded at intervals, representing a function, let's call it `(f(x) + g(x))` [00:25:50]. Here, `f(x)` is the deviation of the first surface, and `g(x)` is the deviation of the second [00:25:35].
2.  **Second Measurement:** The first part is then flipped over [00:24:55] or its orientation is reversed, and it is scanned again against the same second surface, ensuring the same trajectory [00:25:15]. This yields a second function, for instance, `(g(x) - f(x))` due to the inversion of the first part [00:26:00].
3.  **Solving for Unknowns:** With two independent equations (`f(x) + g(x)` and `g(x) - f(x)`) for each point, the individual functions `f(x)` and `g(x)` can be resolved separately by taking the sum and difference of the recorded functions [00:26:23].
4.  **Removing Tilt Error:** If the two surfaces are not at the exact same height during measurement, a tilt error might be introduced into the function [00:26:51]. However, this fixed tilt term can be removed from the measurement, as straightness only concerns the relative deviation of one point to another [00:27:06].

## Applications

Reversal methods are widely used in various [[high_precision_machinery_and_applications | high precision machine tools]] and metrology applications:

*   **Spindle Runout and Roundness:** They are used to separate the actual roundness of a spindle from its runout, which is caused by mounting imperfections [00:21:00]. By mounting a perfect ball or cylinder on the spindle and using two probes at right angles, two independent signals are obtained. These signals, representing runout and roundness, can be separated using the reversal method [00:22:19].
*   **Straightness Measurement:** As described in the core principle, this method allows for the measurement of straightness without relying on a perfectly straight reference [00:23:33].
*   **Accurate Circle Division:** In applications requiring precise angular division, reversal methods can help determine the accuracy of a circle's divisions. If the sum of angles doesn't equal 360 degrees, it indicates an error which can then be isolated through multiple measurements [00:27:52].

This concept is considered one of the more powerful principles in [[techniques_for_measuring_and_ensuring_precision_in_mechanical_parts | precision instruments]] and metrology, enabling the accurate determination of how [[understanding_and_detecting_high_accuracy_parts | high accuracy parts]] are, even without absolute references [00:27:36].