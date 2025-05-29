---
title: Design and manufacturing processes of MEMS
videoId: RiRyap-EVg0
---

From: [[asianometry]] <br/> 

[[introduction_to_mems_and_their_applications | Microelectromechanical Systems (MEMS)]] are microsystems that integrate both electric and mechanical functions, fabricated using advanced techniques similar to those for integrated circuits (ICs) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite their widespread presence and miraculous technology, the [[challenges_in_mems_production_and_economic_issues | MEMS industry]] has faced significant economic and production challenges <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Historical Context and Early Manufacturing
The dream of making extremely small devices has existed for a long time <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. In 1959, Richard Feynman's lecture "There's Plenty of Room at the Bottom" discussed directly manipulating atoms to create useful tools <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

While a prize offered by Feynman for a tiny motor was claimed by a Caltech engineer using conventional tools <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, the spirit of micro-machining emerged later. In 1967, Harvey Nathanson at Westinghouse developed the resonant gate transistor using pre-modern micro-machining techniques <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This gold transistor, about one millimeter long, could move, allowing researchers to control the distance between its gate and electrode using electricity <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. It functioned as a frequency filter, marking it as the first true MEMS product <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

A major breakthrough for MEMS came in 1979 when Hewlett-Packard (HP) utilized [[silicon_wafer_manufacturing_process_and_challenges | silicon micro-machining techniques]] to create an inkjet nozzle for thermal inkjet technology <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. These nozzles became one of the technology's most successful applications <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The inkjet process involves rapidly heating ink to approximately 100 degrees Celsius, creating tiny bubbles that push ink through the micro-machined nozzle onto paper <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. When bubbles collapse, a vacuum draws in more ink <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Though the nozzles themselves aren't mechanical, MEMS technology enabled their creation and tiny size, allowing HP to array many together for increased printer resolution <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## MEMS Manufacturing Workflows

The primary approach for [[commercial_applications_of_mems_in_industry_sectors | commercial MEMS production]] involves using high-volume IC techniques, such as photolithography and etching, to add or remove layers on a 2D substrate, ultimately forming a 3D shape <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

However, there isn't a single, universally applicable methodology for the MEMS industry <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Companies have explored alternative micro-machining methods to achieve more economical production and machining, including:
*   **Electrochemical Micro-machining (ECM)**: Originally a manufacturing technology for low-end PC boards, ECM can create MEMS by locally and selectively etching metals with an electrode tip <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Laser Beam Machining** <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>
*   **Electrode Discharge Machining** <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   **LIGA**: An acronym for a complex process, LIGA is another micro-machining method <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## MEMS Design Challenges

While MEMS and ICs share commonalities, there are fundamental differences, particularly in design <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Miniaturization Effects
Designing MEMS is highly specialized. Simply miniaturizing existing designs does not work because physical forces behave differently at the micro-scale <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>:
*   Friction forces become significantly stronger than inertia <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Tiny flow spaces are much more susceptible to fluid blockages, which require specific design amelioration <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   Certain biochips can utilize electro-osmotic effects, which only exist at the micrometer scale, to pump reactants <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Philosophical Differences from IC Design
There are fundamental philosophical differences between semiconductor and mechanical design <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>:
*   **VLSI (Very Large Scale Integration)** revolutionized semiconductor design through a modular approach, allowing entire systems and chips to be built by combining parts from generic modules and standardized cell libraries <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. These libraries are often designed independently of the final product and in conjunction with the production process, such as TSMC's nodes, to ensure high yields <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Mechanical Design** lacks such a modular system, with the exception of standardized components like bolts, fasteners, and pipe fittings <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Instead, mechanical components must be custom-tailored to accommodate specific weight, space, and energy restrictions of the product <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Functionality**: While VLSI objects primarily process signals (usually logic) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, mechanical objects must contain liquids, rotate, slide, or support loads, often simultaneously <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This inherent complexity makes mechanical design, including MEMS, highly custom <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

### CAD and Design Automation
Despite these complexities, companies like CoventorWare and IntelliCAD are developing CAD and design automation software suites specifically for the MEMS industry <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. These tools significantly help MEMS designers understand microstructure design and its electromechanical behaviors <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Back-End Processes: Testing and Packaging

Testing and packaging are critical "back-end" steps in semiconductor production, transforming a finished die into a chip ready for integration into a final product <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. For MEMS-based sensors, packaging accounts for the majority of the final cost, typically 75% to 80% <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This is a significant reversal compared to integrated chips, where packaging is a smaller proportion of the total cost <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

For example, a pressure sensor for the HVAC market might cost $20-$30, with packaging representing the bulk of this price <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. A raw, unpackaged die from a foundry could cost less than 50 cents <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

The fundamental difference lies in functionality:
*   An IC is a self-contained system, so its packaging primarily serves a secondary, supportive role of protection and interfacing with the outside world, often in a plastic or ceramic case <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   A MEMS device, by its nature, must intimately interact with the external environment <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. A pressure sensor, for instance, cannot be sealed in a hard plastic case if it needs to sense pressure <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

Consequently, the packaging for each MEMS die must be custom-designed for its specific application <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. A pressure sensor MEMS requires different packaging than a micro-mirror array, and a microfluidic MEMS differs from an electrostatic actuator <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. This customization adds substantial cost and engineering effort <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

## Economic Impacts on Production

The [[challenges_in_mems_production_and_economic_issues | economic issues plaguing MEMS production]] are deeply intertwined with its design and manufacturing complexities.
*   **High Hurdles for Payback**: Better machining costs are essential because they set a high hurdle for payback and profit <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Analog Devices' Experience**: Analog Devices, an early investor in MEMS with their accelerometer, built an in-house manufacturing facility that took nine years to become profitable <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. They had to agree to automatic price declines from $11 to $6 per unit over six years for their first automotive sensor deal <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Yield Issues**: Yield is the single biggest influencing factor on product cost <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. A 10% yield means 9 out of 10 MEMS products are unusable <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. While doubling the yield halves the cost, achieving this is difficult <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Market Price Erosion**: Relentless market price erosion, as high as 3-5% each quarter, erodes margins and discourages investment in new MEMS possibilities like micropropulsion for cube satellites or MEMS-based LiDAR mirrors for autonomous cars <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Moving Forward
The MEMS industry, though often called the "second silicon revolution" due to its ability to create microscopic moving parts that are smaller, cheaper, and work better than larger equivalents, faces significant hurdles <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Its inherent creativity and diversity make it challenging to establish widespread standards, and it lacks unifying bodies like Sematech or DARPA that have guided the [[historical_development_of_mems_technology | semiconductor industry]] <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. To realize its full potential, the various players—designers, foundries, vendors, and end-users—need to collaborate more closely to create standards and address the under-invested issues that hinder progress <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.