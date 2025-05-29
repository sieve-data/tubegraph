---
title: Comparison between welding and adhesive bonding
videoId: EeEhS3zmnDg
---

From: [[dgelbart]] <br/> 

This article compares two primary methods for constructing large structures: welding and [[adhesive_bonded_joints_in_large_structures | adhesive bonding]], highlighting their respective advantages and disadvantages, particularly in the context of temporary setups and achieving high precision.

## Welding

Welding is generally considered the cheapest and simplest method for permanently building large structures from materials like pipes and plates <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>, offering high strength <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. However, it presents several challenges, especially for students or researchers:

*   **Difficulty and Skill Acquisition**: Becoming a proficient welder is challenging, requiring significant experience and skill <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
*   **Distortion**: Welding causes substantial distortions in welded parts as the weld cools, pulling the components out of alignment <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. Minimizing this requires numerous tricks, and even then, post-welding machining is often necessary to correct the distortions <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This adds significant work to the construction process <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## Adhesive Bonding

[[adhesive_bonded_joints_in_large_structures | Adhesive bonding]] offers a very effective alternative for building large structures, especially when stiffness is more critical than ultimate strength <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. It is particularly suitable for temporary experimental setups where precise alignment is required <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Construction Process

1.  **Part Preparation**: Components are typically cut using a water jet, which produces a small, consistent taper. This taper allows parts to fit easily from one direction but not the other, aiding in temporary assembly <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
2.  **Temporary Assembly and Testing**: The structure can be temporarily assembled by simply pressing parts together without adhesive, allowing for testing and modifications before final bonding <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. This provides "self-registration" or "self-jigging," eliminating the need for external jigs to achieve accurate assembly because everything locks into slots <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
3.  **Adhesive Application**: For bonding, epoxy (e.g., 5-minute epoxy) is applied to both surfaces to be joined <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.
    *   **Curing Time**: While some epoxies are labeled "5-minute," they typically require at least an hour to achieve reasonable strength <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
    *   **Working Time**: To extend the working time of fast-setting epoxies, they can be mixed on a chilled metal surface, such as a piece of aluminum, as cold temperatures slow down the curing process <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
4.  **Achieving Planarity**: If surfaces need to be co-planar, the entire assembly should be cured upside down on a granite plate to ensure flatness upon completion <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
5.  **Disassembly**: Unlike welding, [[adhesive_bonded_joints_in_large_structures | adhesive bonded joints]] can be disassembled. By heating the entire structure, either with a torch or in an oven, to approximately 150-300°C (300°F) <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>, the adhesive bond can be weakened, allowing the parts to be knocked apart <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

### Advantages over Bolted Structures (e.g., T-slot extrusions)

Commercial extrusions with T-slots, designed for rapid assembly and disassembly, are often used for structures. However, [[adhesive_bonded_joints_in_large_structures | adhesive bonding]] offers superior rigidity:

*   **Higher Rigidity**: [[adhesive_bonded_joints_in_large_structures | Adhesively bonded]] structures are significantly more rigid than bolted assemblies <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.
*   **Elimination of Play**: Bolted connections can stretch screws or allow twisting, leading to a lack of rigidity. [[adhesive_bonded_joints_in_large_structures | Adhesive bonding]] eliminates this play, effectively making the structure into one continuous, rigid piece <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. This is crucial for applications requiring high accuracy, not just an enclosure <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

### Designing [[adhesion_failure_modes_and_design_considerations | Adhesive Joints]]

For optimal performance, [[adhesive_bonded_joints_in_large_structures | adhesive joints]] should be designed with specific load conditions in mind:

*   **Shear Mode (Preferred)**: A properly designed [[adhesion_failure_modes_and_design_considerations | adhesive joint]] should work in shear mode <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. In shear, the load is distributed across the entire joint area instantaneously <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>. A 1/10 scale shear joint example demonstrated a strength of 2 tons, which extrapolates to 200 tons for a full-sized structure (due to the area scaling by the square of the linear dimension) <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>, <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **Tension Mode (Acceptable but Weaker)**: Designing for tension is the next best option but results in significantly weaker joints compared to shear <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
*   **Peel Mode (Avoid at All Costs)**: [[adhesion_failure_modes_and_design_considerations | Adhesive joints]] should *never* be designed to work in peel mode <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. In peel, all the stress is concentrated on a single line where the material starts to lift off, theoretically resulting in infinite stress and causing the joint to fail instantly, even with robust adhesives like epoxy <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>, <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. Many seemingly tension-loaded joints, like a bracket glued to a surface, can actually fail in peel mode when bent <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>. This principle also applies to soldering <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>. Flexible adhesives like polyurethanes or RTV silicone perform better in peel mode because they stretch, distributing the stress over a larger area <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.

### [[adhesive_types_and_their_specific_applications | Adhesive Types]]

For laboratory use, primarily four types of adhesives are needed:

1.  **Epoxy**: The most common, such as 5-minute epoxy, preferred for its quick setting time <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.
2.  **Silicone RTV**:
    *   **High Temperature Resistance**: Can withstand high temperatures; clear RTV handles 250°C, while red (iron cure) can reach 300°C or more, making it suitable for hot applications <a class="yt-timestamp" data-t="18:09:00">[18:09:00]</a>.
    *   **Elasticity**: Stays elastic permanently <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.
    *   **Bonding to Glass/Ceramics**: Forms a tenacious chemical bond to glass and certain ceramics without needing surface preparation like sand blasting, unlike most other adhesives <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>, <a class="yt-timestamp" data-t="19:13:00">[19:13:00]</a>.
3.  **Polyurethane**:
    *   **Flexibility**: Bit flexible and bonds tenaciously to rubber and other flexible materials, where rigid adhesives often fail <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.
    *   **Foaming Properties**: Certain types can foam to fill gaps <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>.
    *   **Performance**: Often a better adhesive than epoxy, including good peel strengths, but requires overnight curing <a class="yt-timestamp" data-t="20:23:00">[20:23:00]</a>.
4.  **Spray Contact Cement**: Useful for covering large sheets uniformly. Requires application to both surfaces <a class="yt-timestamp" data-t="20:31:00">[20:31:00]</a>.

### Adhesives to Avoid in Scientific Work

*   **Cyanoacrylates (Super Glue)**: Generally not recommended for scientific applications for several reasons:
    *   **Rigidity**: Very rigid, making joints prone to breaking under shock loads <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.
    *   **Outgassing**: Slowly emits gas that can fog optics in sealed environments within weeks <a class="yt-timestamp" data-t="22:44:00">[22:44:00]</a>.
    *   **Plastic Damage**: Can cause plastics to "craze" (develop micro-cracks) <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>. Other adhesives outgas less and can be baked to accelerate outgassing <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>.

### Temperature Considerations for Adhesive Bonding

When bonding components where precision with temperature is critical (e.g., mirrors to metal), consider:

*   **Differential Thermal Expansion**: Polymers (adhesives) have significantly higher thermal expansion coefficients (roughly an order of magnitude more) than metals, unless heavily filled <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.
*   **Bond Layer Thickness**: A parallel shift due to the adhesive layer expanding (e.g., 5 microns for a 50-micron bond changing 10% in thickness) is usually not a problem for optics <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.
*   **Wedge-shaped Bonds**: If the adhesive forms a wedge (e.g., when used to align a component and then cured), the angle of the component (like a mirror or bracket) will change with temperature <a class="yt-timestamp" data-t="25:15:00">[25:15:00]</a>. This angular change can be significantly multiplied by the optical or structural lever arm, leading to larger errors <a class="yt-timestamp" data-t="25:27:00">[25:27:00]</a>.