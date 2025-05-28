---
title: Historical use of analog computers for tide prediction
videoId: IgF3OX8nT0w
---

From: [[veritasium]] <br/> 

The [[analog_computers_history_and_resurgence | history of analog computers]] dates back to antiquity, with one of the earliest known examples being used for astronomical predictions. These machines later evolved to tackle complex engineering problems, most notably the prediction of tides.

## Early Analog Computing: The Antikythera Mechanism

Discovered in 1901 from a shipwreck off the island of Antikythera, an ancient Greek artifact constructed around 100 or 200 BC represents a sophisticated early computer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Three-dimensional X-ray scans have revealed that this device, known as the [[the_antikythera_mechanism_as_an_early_analog_computer | Antikythera mechanism]], contains 37 interlocking bronze gears <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. These gears allowed it to model the motions of the sun and moon and predict eclipses decades in advance <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

Unlike modern digital computers, the Antikythera mechanism operated by analogy <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Its gears were designed so that the motions of certain dials were analogous to the celestial bodies they represented, making it an [[analog_computers_history_and_resurgence | analog computer]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Analog vs. Digital Computers

The fundamental [[differences_between_analog_and_digital_computers | differences between analog and digital computers]] can be illustrated with simple examples:
*   An [[analog_computers_history_and_resurgence | analog computer]] for addition might use rotating wheels where the sum of two rotations is shown on a third wheel <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. [[analog_computers_history_and_resurgence | Analog computers]] have a continuous range of inputs and outputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Quantities are represented by physical attributes, such as the amount a wheel has turned <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   A digital mechanical computer, in contrast, would work with discrete values, like adding single-bit numbers (e.g., 0+0=0, 0+1=1, 1+1=2) <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Digital computers operate on symbols, typically zeros and ones <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

For thousands of years, both [[analog_computers_history_and_resurgence | analog devices]] (like the [[the_antikythera_mechanism_as_an_early_analog_computer | Antikythera mechanism]] or slide rules) and digital devices (like abacuses) were in use <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Up until the 1960s, the most powerful computers were actually analog <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## The Challenge of Tide Prediction

Predicting tides has been a critical problem for millennia <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Historically, miscalculations could lead to disaster, as in Napoleon's near-death experience crossing the Red Sea <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, or ships running aground <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Most coastal locations experience two high and two low tides daily, but their exact timing and magnitude vary due to local factors like sea bed depth and shoreline shape <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Laplace's Equations and Fourier Analysis

In the late 1700s, Pierre-Simon Laplace derived complex differential equations to describe oceanic tidal flow <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. While these equations had no analytical solution at the time, Laplace made a key finding: tides are driven by a few specific astronomical frequencies, including the moon, sun, and lunar orbit eccentricity <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Each factor contributes a sine wave of a particular amplitude and phase to the total tide curve <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. The challenge became how to correctly combine these frequency components to predict tides <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

It took nearly a century, but in the 1860s, William Thompson, later known as Lord Kelvin, took on the challenge <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Inspired by his work laying the first transatlantic telegraph cable, he dedicated himself to measuring and predicting tides <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Kelvin applied the work of French mathematician Joseph Fourier, who had shown how any function could be decomposed into a sum of sine waves <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Although applying Fourier's analysis to tidal curves was straightforward, the computation required was enormous <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. To characterize tides at one location, Kelvin needed 10 different frequency components, requiring extensive multiplication and addition <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This had to be repeated for every new location <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Once these coefficients were known, the next step was to add the sine functions to predict future tides <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Lord Kelvin's Tide Predicting Machines

Lord Kelvin spent years manually analyzing and predicting tides before conceiving the idea of designing a machine to automate these calculations <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. His goal was to "substitute brass for brains" <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The resulting [[analog_computers_history_and_resurgence | analog computers]] were used for nearly a century <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### The Tide Predictor (Addition Machine)

Kelvin first addressed the prediction problem: adding sine waves together given their amplitudes and phases <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. He knew a scotch yoke device could create sinusoidal motion from uniform circular motion <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. For mechanical addition of 10 sine waves, a chance encounter on a train with inventor Beauchamp Tower in 1872 provided the solution <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Tower suggested using Wheatstone's plan of a chain passing around multiple pulleys <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

By attaching a pulley to each scotch yoke and running a weighted cord around them, Kelvin could mechanically add all their contributions simultaneously <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. He sketched the entire plan for this predictor machine on the train and secured funding to build it <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This machine automated the tedious task of predicting future tides, with four hours of cranking yielding a full year of predictions <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### The Harmonic Analyzer (Integration Machine)

The harder part of the problem – decomposing an existing tide curve into its component frequencies – remained manual for many years <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. To automate this, Kelvin needed a machine capable of multiplying the tide curve by a sine wave and then integrating the result <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

With his older brother, James Thompson, Kelvin developed a mechanical integrator based on a ball on a rotating disk <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The ball's rotation speed depends on its distance from the disk's center <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. A stylus traces the function to be integrated, controlling the ball's position and speed <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The ball's motion is converted to an output by a roller, plotting the integral <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

To decompose a tide curve, the disk was made to oscillate back and forth at a specific frequency <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. By tracing the tide curve with the stylus, the roller summed the integral of the tide curve multiplied by the sine wave <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Multiple ball and disk integrators could be connected in parallel, each oscillating at a different frequency, to calculate coefficients for many frequency components simultaneously <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

## Impact and Legacy

Kelvin's [[analog_computers_history_and_resurgence | analog computers]] revolutionized tide prediction <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Tidal curves from anywhere could be analyzed into sinusoidal coefficients using the harmonic analyzer, and these could then be added by the predictor machine to forecast future tides <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

Kelvin's tide predicting machines were used well into the 1960s <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. They were even overhauled to include 26 frequency components and played a critical role in planning the Allied invasion on D-Day <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The invasion times were staggered across the five landing beaches according to precise tide predictions, allowing demolition teams to clear obstacles at low tide before the main forces landed as the water rose <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

### Other [[analog_computers_in_military_applications_during_world_war_ii | Military Applications During World War II]]

Beyond tide prediction, [[analog_computers_history_and_resurgence | analog computers]] were crucial in [[analog_computers_in_military_applications_during_world_war_ii | World War II]] for applications such as aiming anti-aircraft guns <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. The M9 Gun Director, developed by Bell Labs using operational amplifiers, could rapidly calculate the correct trajectory and fuse settings for anti-aircraft guns based on radar and optical data <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. This dramatically improved accuracy, reducing the average rounds needed to take down an airplane from 17,000 in World War I to just 90 in 1943 <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

However, not all [[analog_computers_in_military_applications_during_world_war_ii | analog computers]] were successful. The Norden bombsight, an incredibly complex mechanical [[analog_computers_history_and_resurgence | analog computer]] and the third-largest single expense in the U.S. military budget during the war, failed to deliver its promised high precision <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Its 2,000 fine parts meant that any manufacturing inaccuracy translated directly into computational inaccuracy, and repeat calculations would not yield the exact same answer <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This highlights one of the inherent [[challenges_and_potential_of_analog_computing_in_modern_technology | challenges]] of analog computing: physical imperfections affect results <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

## The Rise of Digital Computing

As [[analog_computers_in_military_applications_during_world_war_ii | World War II]] progressed, digital computers began to gain traction <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. The electronic Colossus machines at Bletchley Park were crucial for breaking German codes <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. In the U.S., the ENIAC, designed to speed up artillery firing table calculations previously done by [[analog_computers_history_and_resurgence | analog]] differential analyzers, demonstrated the power of digital computing and is considered by many to be the first modern computer <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

Claude Shannon's 1936 master's thesis, which showed that any numerical operation could be performed using Boolean algebra (true/false or one/zero, and/or/not operations), truly opened the door to the digital revolution <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. This made digital computers ideal versatile machines, resilient to noise since it takes a large error to mistake a one for a zero <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. In contrast, each [[analog_computers_history_and_resurgence | analog computer]] is typically designed for only one type of problem, and small errors can accumulate <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

Today, nearly everything is digital <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. Digital devices provide exact, repeatable answers and are robust to noise <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Their components have been miniaturized and optimized, making them universal computing machines <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. Despite this dominance, [[the_resurgence_and_potential_of_modern_analog_computing | analog computing may now be making a comeback]], with startups actively working on them, hinting at potential benefits in areas like [[applications_of_analog_computers_in_ai | artificial intelligence]] <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.