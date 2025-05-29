---
title: Adhesion failure modes and design considerations
videoId: EeEhS3zmnDg
---

From: [[dgelbart]] <br/> 

## Introduction to Adhesive Bonding for Structures
[[adhesive_bonded_joints_in_large_structures | Adhesive bonding]] is a method for assembling structures, particularly useful for temporary setups or experimental configurations where [[comparison_between_welding_and_adhesive_bonding | welding]] might be too permanent or introduce undesirable distortions <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. If high strength is paramount for a permanent structure, welding remains the primary choice <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. However, for applications requiring stiffness or accuracy, [[adhesive_bonded_joints_in_large_structures | adhesive bonding]] offers significant advantages <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Comparison to Welding
While [[comparison_between_welding_and_adhesive_bonding | welding]] is cost-effective and simple for permanent large structures using pipes and plates <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, it presents several challenges:
*   **Skill Requirement**: Becoming a proficient welder demands significant experience and skill <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Distortion**: Welding induces very large distortions in materials as the weld cools and pulls parts, requiring many tricks to minimize or subsequent machining to correct <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

In contrast, [[adhesive_bonded_joints_in_large_structures | adhesive bonding]] using water jet cut parts allows for precise assembly and can be reversible <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Structures can be temporarily assembled, tested, disassembled, and then permanently bonded <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Adhesive bonds can also be "un-bonded" by heating the structure to around 150°C (300°F), allowing parts to be knocked apart <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Adhesion Failure Modes: Shear vs. Peel
A crucial principle in [[adhesive_bonded_joints_in_large_structures | adhesive joint]] design is understanding how different load applications affect bond strength. A proper [[adhesive_bonded_joints_in_large_structures | adhesive joint]] should always be designed to work in **shear mode** <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Shear Mode**: In shear, the load is distributed across the entire joint area because everything wants to move simultaneously <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. This ensures the load is applied to the whole adhesive area <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
    *   *Demonstration*: A properly sandblasted and cured epoxy joint designed for shear can withstand significant force (e.g., 2 tons for a 1/10 scale model, extrapolating to 200 tons for full size) <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   **Tension Mode**: Designing joints in tension is weaker than shear <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Peel Mode**: Joints should **never** be designed to work in peel mode <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
    *   *Mechanism*: Peel mode concentrates all the load on a single line where the separation begins, effectively a geometrically zero area <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. The adhesive behind this line experiences no load <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
    *   *Demonstration*: An epoxy joint designed for peel shows virtually zero strength, breaking instantly <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This applies to various adhesives and even soldering <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
    *   *Hidden Peel Modes*: Many joints that appear to be in tension or shear can actually fail in peel mode under load, such as a bracket glued flat to a surface which peels when bent <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

## Design Considerations for Adhesive Bonding

### Joint Design and Self-Jigging
*   **Water Jet Cut Parts**: The slight taper from water jet cutting allows parts to fit easily from one side but not the other, enabling temporary assembly without adhesive for testing <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Self-Registration/Jigging**: Designing components with interlocking slots or wedges allows for automatic alignment and rigid temporary assembly, reducing the need for external jigs <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This can create surprisingly strong bonds even without adhesive <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Planarity**: For precise planarity, assemble the structure upside down on a granite plate and allow the adhesive to cure <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### [[preparing_surfaces_for_painting_and_bonding | Surface Preparation]]
For most adhesives to form a strong bond, surfaces must be properly prepared:
*   **Mechanical Roughening**: [[sand_blasting_for_adhesion_and_painting | Sand blasting]] is the preferred method <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. The cut surface from a water jet can behave similarly to a sandblasted surface <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Chemical Cleaning**: Other methods include rubbing with bathroom cleaner (e.g., Comet or Ajax) or "bluing" <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
*   **Application**: Apply adhesive to both surfaces to be joined <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### [[adhesive_types_and_their_specific_applications | Adhesive Types and Their Specific Applications]]
For laboratory and scientific work, four main types of [[adhesive_types_and_their_specific_applications | adhesives]] are commonly used:
1.  **Epoxy (e.g., 5-minute epoxy)**:
    *   **Pros**: Most commonly used <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>, relatively fast curing time (though 5-minute epoxy needs an hour for reasonable strength) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Excellent in shear mode <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   **Cons**: Rigid, poor peel strength <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. Cannot bond well to flexible materials <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Needs surface preparation <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
    *   **Tip**: To extend working time of fast epoxy, mix it on a chilled piece of metal (e.g., aluminum) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Silicone RTV (Room Temperature Vulcanizing)**:
    *   **Pros**: Can withstand high temperatures (clear RTV up to 250°C, red up to 300°C) <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. Stays elastic <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Forms a tenacious chemical bond to glass and certain ceramics without [[sand_blasting_for_adhesion_and_painting | sand blasting]] <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. Better peel strength than epoxy because it stretches and distributes stress <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
    *   **Cons**: Not as rigid as epoxy.
3.  **Polyurethane (e.g., Gorilla Glue)**:
    *   **Pros**: Flexible <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>, bonds tenaciously to flexible materials like rubber <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. Some types foam up and fill gaps <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Good peel strength <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>, better than epoxy for this <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
    *   **Cons**: Requires overnight curing <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. Needs surface preparation.
4.  **Spray Contact Cement**:
    *   **Pros**: Good for uniformly covering large sheets <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
    *   **Cons**: Requires spraying both sides <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

**Adhesives to Avoid (for scientific work):**
*   **Cyanoacrylates (Super Glue/Magic Glue)**:
    *   **Pros**: Bonds instantly, good for rubber and O-rings <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.
    *   **Cons**: Very rigid, prone to breaking from shock loads <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. Emits gas that fogs optics within weeks <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>. Can cause plastics to craze (develop micro-cracks) <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Not recommended for scientific work due to outgassing <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

### [[techniques_to_improve_rigidity_in_structural_assemblies | Techniques to Improve Rigidity in Structural Assemblies]]
*   **Avoid T-slot Extrusions**: While designed for rapid assembly and disassembly, these structures are not rigid because connections at corners and screws allow for stretching and twisting <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. They are suitable only for non-accuracy critical applications like enclosures <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Adhesive Bonding for Rigidity**: For high accuracy, a structure must be rigidly connected everywhere and "over-constrained" to become a single, solid piece <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. [[adhesive_bonded_joints_in_large_structures | Adhesive joints]] achieve this effectively <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### [[use_of_flexures_in_mechanical_designs | Use of Flexures for Removable Parts]]
When parts need to be held securely yet remain removable, traditional set screws are problematic as they apply concentrated load, deform parts, and can crack brittle materials like granite <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Flexure Clamps**: A superior method is to cut a slot and use a flexure clamp <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   **Mechanism**: By tapping the slot with a tapered pipe thread and inserting a pipe plug, the flexure expands gradually, distributing pressure over a larger area <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   **Advantages**: Provides very good clamping, spreads load gently, and allows for disassembly <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. Offers huge leverage due to the small thread angle, generating many tons of force <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This principle can be applied to clamp pulleys or other components <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

### Temperature Effects on Adhesive Joints
*   **Thermal Expansion**: Adhesives (polymers) have coefficients of thermal expansion roughly an order of magnitude higher than metals <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
*   **Parallel Shift**: If a bonded mirror or component shifts parallel due to adhesive expansion, the effect is often minor (e.g., 5 microns for a 50-micron bond layer changing 10% in thickness) <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **Angular Tilt**: If the adhesive forms a wedge or the joint is designed to allow tilting, the angle of the component (e.g., a mirror or bracket) will change significantly with temperature due to a "multiplier effect" from the optical lever or length of the structure <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. Avoid designs where the adhesive bond can create a thermal wedge.
*   **Outgassing**: Adhesives can outgas, which is a concern in sealed environments like vacuum chambers or laser housings, as it can fog optics <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. Most adhesives can be baked to accelerate and reduce outgassing, unlike cyanoacrylates <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.