---
title: Testing and measurement for flexure systems
videoId: PaypcVFPs48
---

From: [[dgelbart]] <br/> 

When working with [[flexures]], particularly those made from sheet metal using tools like a water jet, precise testing and measurement are crucial to ensure their performance and accuracy <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This includes verifying linear motion, straightness of travel, and understanding environmental influences like temperature.

## Measuring Linear Motion and Precision

The precision of a flexure's linear stage can be measured using sensitive instruments like a capacitance gauge <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, a meter hooked up to a capacitance gauge can be set to a high gain, such as 10 nanometers per division, demonstrating the ability to move the flexure 10 nanometers at a time without backlash <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This allows for precise forward and backward movement and accurate setting of positions <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Temperature Sensitivity

The material chosen for a flexure significantly impacts its stability and thus its measurement accuracy <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. For instance, flexures made of aluminum are highly temperature-sensitive, with a coefficient of about 22-23 PPM per degree <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

> "Even you can't have aluminum if you want the stability so in real life this will have to be cut out of invar or maybe some glass like quartz or some other material which is very stable with temperature" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>

Even radiated heat from a hand can cause an aluminum flexure to drift by 100 nanometers <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. For high stability, [[materials_used_for_flexures_and_their_properties | materials]] like Invar, quartz, or other temperature-stable options are preferred <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Achieving and Verifying Straightness of Travel

The linearity of a flexure's motion, meaning how closely it follows a straight line, depends on the exact matching of its pivot points, also known as elastic pivots <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Pre-processing for Accuracy

For [[techniques_for_achieving_high_accuracy_in_flexures | very high accuracy flexures]], it is recommended to pre-drill the holes for the pivot points <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A water jet alone may not be accurate enough to achieve straightness of travel in the one-micron range <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Therefore, holes should be drilled and reamed, and then the water jet can be aligned to one of these holes to make the remaining cuts <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. This method can achieve a travel range of approximately 2 mm following a straight line to one micron <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For [[precision_and_adjustability_in_mechanical_components | flexures constructed from multiple pieces]], such as those made of Nitinol, careful measurement and matching of spring lengths are essential for straight line travel <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Using a jig as a spacer during assembly can ensure consistent spacing and alignment <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Post-Assembly Correction

Even after assembly, [[techniques_for_achieving_high_accuracy_in_flexures | flexures can be modified]] to improve their straightness <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This involves adjusting the springs by grinding them or clamping something onto them to alter the stiffness of the pivot point <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. Many flexures are corrected post-assembly to achieve ultimate straightness <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Testing Straightness

#### Visual Laser Pointer Method
A simple way to test straightness is by attaching a laser pointer to the moving part of the flexure <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. By clamping the flexure to a table and projecting the laser beam across a room (e.g., 10 meters away) onto a wall, one can observe the laser spot while the flexure moves <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. A one milliradian error over 10 meters will result in a 10 mm deviation, which is easily visible, allowing measurement down to 50 microradians <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

#### Autocollimator for Precision Angular Measurement
For more precise measurement of straightness, an autocollimator can be used <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. An autocollimator measures the reflection of a target <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. By placing a mirror on the moving part of the flexure and setting up the autocollimator, sub-arc second angular motions can be measured <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Any deviation from linearity is accompanied by an angular motion, as one is the integral of the other <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Measuring the angular motion of the reflected light allows for integration to determine the deviation from straightness <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.