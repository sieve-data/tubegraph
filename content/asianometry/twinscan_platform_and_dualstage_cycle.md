---
title: TWINSCAN platform and dualstage cycle
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

The [[technological_advances_in_lithography_tools_by_asml | TWINSCAN platform]] is ASML's primary brand of lithography machine <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. It was developed to address challenges posed by the semiconductor industry's shift from 200-millimeter to 300-millimeter wafers and the demand for processing smaller features <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## Dual-Stage Cycle

The TWINSCAN machine operates on a dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This contrasts with earlier lithography machines that performed measurement, alignment, and exposure sequentially on a single wafer <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

During operation, a wafer is clamped and secured on each stage using electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The chuck holding the wafer has tens of thousands of burls, reducing direct contact to just 2% of the wafer surface area to minimize contamination risk <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The process involves two main phases:
1.  **Measurement Stage**: A robot called the wafer handler loads or unloads the wafer into the machine <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The wafer first enters the measurement stage, where the machine performs a series of scans <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. These scans prepare the computers to align the wafer in relation to the reticle, ensuring precise focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
2.  **Exposure Stage**: After measurement, the machine swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The measured wafer then moves under the objective lens, and the light source is activated to achieve the required light exposure dose <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. During the stage swap, the machine can also exchange the reticle, though this requires a new alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

The wafer movements within the TWINSCAN are coordinated by the Control Architecture Reference Model (CARM) motion control platform <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. CARM is powered by FPGAs and process controllers housed in an external cabinet rack <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Engineering Challenges and Solutions

Implementing the dual-stage setup was a significant engineering feat <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>:
*   **Weight Re-balancing**: The tool's architecture had to be reworked to re-balance the new weight and mass on the machine's frame <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Vibration Management**: With two processes running simultaneously, managing vibrations was critical <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. The lens and metrology equipment, mounted on the "metrology frame," are isolated from the rest of the tool's main frame using air-bearings, which use highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Throughput and Precision

The key to hitting throughput benchmarks in a lithography machine is not the exposure stage, but rather the measurement stage <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a DUV machine processing 175 wafers per hour spends only about 20 seconds exposing each wafer out of a 2-minute cycle, with the rest of the time dedicated to measurement <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

ASML's ability to precisely sequence actions during measurement is crucial for producing a competitive machine <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. The wafer stage, weighing approximately 15 kilograms when fully loaded with a 300-millimeter wafer <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, must be positioned with below-nanometer accuracy <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Overlay requirements can be as small as a few nanometers, and errors can damage device capabilities or cause short-circuits <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## TWINSCAN Today

Today, the TWINSCAN name encompasses several product categories <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   **NXE**: Used for [[overview_of_asmls_extreme_ultraviolet_lithography | EUV lithography]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. An NXE:3350 EUV machine can process 125 wafers per hour <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **NXT**: Uses 193-nanometer ArF DUV light <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **XT**: Uses 248-nanometer KrF DUV light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The numbers in the machines' names relate to their optics systems and lenses <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. These machines are built modularly to meet customer requirements <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a> and are designed to receive upgrades over decades to keep pace with modern demands <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Role of Software

Software plays a crucial role in the precision and performance of ASML's lithography tools. From 1989 to 2000, the number of CPUs and sensors in ASML's tools increased six and eight times, respectively <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, including comments, while the 2003 TWINSCAN contained 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive leveraging of software has been a key driver behind ASML's strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.