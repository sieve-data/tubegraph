---
title: Challenges and limitations of metal 3D printing
videoId: nyYcomX7Lus
---

From: [[dgelbart]] <br/> 

While [[metal_3d_printing_process | metal 3D printing]] holds significant promise as a production method, especially for complex parts, it faces several challenges and limitations.

## General Challenges

Many parts commonly showcased by metal 3D printing companies could often be produced more quickly and affordably using [[CNC machining | CNC machining]] <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. For instance, a wrench or locking pliers might take minutes to machine but require about a day to 3D print due to post-processing requirements <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. Simple parts without internal structures are particularly well-suited for [[CNC machining | CNC machining]] and are very inexpensive to produce <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.

## Challenges with Laser-Based (SLS/SLM) Systems

Laser-based systems, such as Direct Metal Laser Sintering (DMLS), Selective Laser Sintering (SLS), or Selective Laser Melting (SLM), present specific drawbacks:

*   **High Cost**
    These systems are expensive, with an installation typically costing around $1 million <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>. This cost includes the printer itself, as well as necessary backroom equipment <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

*   **Support Structures and Post-Processing**
    All laser-based systems require extensive support structures for the printed parts <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. These supports are crucial not only to compress the powder during printing but, more importantly, to prevent warping caused by the rapid cooling and stress build-up as layers of molten metal are deposited <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>, <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
    Removing these "organically" connected support legs is a significant challenge <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a> and involves an "ugly backroom operation" not typically highlighted by vendors <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This post-processing often includes:
    *   **Heat Treatment:** Parts must be heat-treated in an inert or controlled atmosphere furnace to anneal them and relieve stresses, preventing oxidation <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>, <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. These furnaces are expensive <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
    *   **[[Wire EDM | Wire EDM]]:** For precise removal of supports, [[Wire EDM | Wire EDM]] machines are used to cut along contours <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>, <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
    *   **Manual Finishing:** Areas inaccessible by [[Wire EDM | Wire EDM]] may require old-fashioned belt sanders or other manual methods <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
    These post-processing steps significantly extend the overall time required to produce a finished part <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

*   **Facility Requirements and Safety**
    The metal powders used in these systems can be explosive <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. This necessitates specialized installations with full respiration gear, fire protection, explosion-proof features, and Halon fire extinguishers <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Consequently, these systems cannot be placed in a standard office environment and are generally reserved for dedicated production facilities <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>, <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

*   **"Organic Design" Challenges**
    The "organic design" philosophy, often promoted with metal 3D printing, features parts with free-flowing forms <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. However, most metal 3D printed parts still require post-machining for features like precise holes or accurate threads <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>. Fully organic shapes can be difficult to clamp securely for machining, potentially requiring the 3D printing of special clamps, which adds to the overall cost and effort <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>, <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.

## Challenges with Sintering-Based Systems

While generally simpler and less expensive, sintering-based metal 3D printing systems also have limitations:

*   **Object Size Limitation**
    A fundamental limitation is the maximum object size that can be reliably sintered <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>, <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>. During the [[sintering_in_metal_3d_printing | sintering]] process, the part becomes soft, akin to Play-Doh, at high temperatures <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. Attempting to sinter objects larger than approximately a shoebox can lead to sagging and distortion, even with support structures <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>, <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. This limitation is also seen in other [[sintering_in_metal_3d_printing | sintering]] processes like powder metallurgy (PM) and metal injection molding (MIM) <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

*   **Limited Metal Choice**
    The selection of available metals for sintering-based systems is not as wide as for laser systems <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. Currently, only a few metals and ceramics are available, though more may be developed in the future <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>, <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.