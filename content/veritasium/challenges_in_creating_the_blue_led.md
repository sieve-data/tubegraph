---
title: Challenges in creating the blue LED
videoId: AF8d72mA41M
---

From: [[veritasium]] <br/> 

The development of a blue Light Emitting Diode (LED) was a significant hurdle in the [[history_of_led_development | history of LED development]] and a major **challenge** for the electronics industry for decades. Without a blue LED, it was impossible to mix red, green, and blue light to create white light, which limited the use of LEDs to applications like indicators, calculators, and watches [00:00:28].

## Early Limitations and Attempts

In 1962, General Electric engineer Nick Holonyak created the first visible LED, which glowed a faint red [00:00:15]. A few years later, engineers at Monsanto developed a green LED [00:00:23]. However, for decades, these were the only two colors available [00:00:28]. This meant LEDs could not be used for general lighting [00:00:45].

Throughout the 1960s, major electronics companies worldwide, including IBM, GE, and Bell Labs, competed to create the blue LED, recognizing its immense potential value [00:01:00]. Despite the efforts of thousands of researchers, no one succeeded [00:01:12]. By the 1980s, after hundreds of millions of dollars had been spent, every company had come up empty-handed [00:09:40]. According to a director at Monsanto, LEDs "won't ever replace the kitchen light" [00:01:26].

## Core Scientific Obstacles

The fundamental challenge in creating a blue LED stemmed from the physics of light emission. The color of light emitted by an LED is determined by the size of its band gap [00:09:06]. A photon of blue light requires more energy, and therefore a larger band gap, compared to red or green light [00:09:33].

Researchers identified three primary technical hurdles:

### 1. Achieving High-Quality Crystal Structure

Regardless of the material used, a near-perfect crystal structure was essential for a functional blue LED [00:09:54]. Any defects in the crystal lattice disrupt the flow of electrons, causing energy to dissipate as heat instead of being emitted as visible light [00:10:00].

Two main material candidates emerged: zinc selenide and gallium nitride [00:12:21].
*   **Zinc Selenide:** This material was considered more promising because, when grown in an MOCVD reactor, it had only a 0.3% lattice mismatch with its gallium arsenide substrate, resulting in about 1,000 defects per square centimeter—within the acceptable limit for LED function [00:12:36]. However, a significant problem was the inability to create p-type zinc selenide [00:12:51].
*   **Gallium Nitride:** This material had been largely abandoned by the scientific community due to several issues [00:13:00]:
    *   **High Lattice Mismatch:** The best substrate for growing gallium nitride was sapphire, but it had a substantial 16% lattice mismatch [00:13:10]. This led to an extremely high defect density, over 10 billion per square centimeter [00:13:16], making it exceptionally difficult to grow a high-quality crystal [00:13:06].
    *   **Initial Growth Difficulties:** Even for [[shji_nakamuras_contributions_to_led_technology | Shūji Nakamura]], getting gallium nitride to grow normally in his new MOCVD reactor was a challenge, taking him six months of continuous work [00:15:24].
    *   **Conventional Wisdom:** Scientists widely avoided adding a second stream to MOCVD reactors, believing it would introduce more turbulence [00:17:06].

### 2. Creating P-Type Gallium Nitride

Similar to zinc selenide, a major obstacle for gallium nitride was the inability to create a stable p-type semiconductor [00:13:22].
*   While Dr. Isamu Akasaki and Dr. Hiroshi Amano had achieved p-type gallium nitride by doping it with magnesium and exposing it to an electron beam, the reason it worked was unknown, and the process was too slow for commercial production [00:19:26].
*   The underlying problem was later discovered to be hydrogen atoms, introduced from ammonia during the MOCVD process, which bonded with the magnesium dopant and plugged the holes needed for p-type conductivity [00:20:30].

### 3. Achieving Sufficient Light Output Power

To be commercially viable, a blue LED needed a total light output power of at least 1,000 microwatts [00:13:32]. Early prototypes, such as [[shji_nakamuras_contributions_to_led_technology | Shūji Nakamura]]'s initial blue-violet LED, only achieved 42 microwatts, falling well below the practical threshold [00:21:22].

*   A known method to increase LED efficiency was to create an "active layer" (a "well") at the p-n junction to shrink the band gap slightly and encourage electron flow [00:22:02]. Indium gallium nitride was identified as the best material for this layer, which would also narrow the band gap to achieve a true blue color [00:22:21].
*   However, growing indium gallium nitride was challenging; as Amano recalled, "It was generally said that gallium nitride and indium nitride would not mix, like water and oil" [00:22:39].
*   Even after successfully growing the active layer, initial designs led to the "well" overflowing with electrons, causing them to leak back into the gallium nitride layers [00:23:16].

## Overcoming the Challenges

[[shji_nakamuras_contributions_to_led_technology | Shūji Nakamura]] at Nichia, a small Japanese chemical company, defied conventional wisdom and achieved the breakthroughs necessary to solve these challenges [00:01:42].
*   He developed the "two-flow reactor" by adding a second nozzle to his MOCVD system, which pinned the reactant gases to the substrate, enabling the growth of the highest quality gallium nitride crystals ever made [00:16:45]. This allowed him to use gallium nitride itself as a buffer layer on sapphire, avoiding the issues of aluminum [00:17:26].
*   He discovered that simply heating (annealing) magnesium-doped gallium nitride to 400 degrees Celsius would release the hydrogen atoms, thus freeing up the holes and creating a completely p-type sample [00:20:09]. This process was quick and scalable [00:20:26].
*   Using his customized MOCVD reactor, he managed to grow clean indium gallium nitride crystal for the active layer [00:22:56]. He then solved the "overflow" problem by creating a "hill" with aluminum gallium nitride, a compound with a larger band gap, to block electrons from escaping the well [00:23:28].

By 1992, Nakamura had created a bright blue LED with a light output power of 1,500 microwatts, exceeding the necessary threshold and marking the end of a 30-year search [00:24:27]. This invention paved the way for the creation of the white LED and sparked a revolution in lighting technology, leading to the widespread [[transition_from_incandescent_to_led_lighting_technology | transition from incandescent to LED lighting technology]] and a significant [[impact_of_led_technology_on_modern_lighting | impact of LED technology on modern lighting]] [00:25:33].

Today, research continues into [[future_innovations_in_led_technology | future innovations in LED technology]], including micro LEDs and UV LEDs, building upon the foundational breakthroughs made by Nakamura and others [00:29:21].