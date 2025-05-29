---
title: Adhesive types and their specific applications
videoId: EeEhS3zmnDg
---

From: [[dgelbart]] <br/> 

This article explores various types of adhesives commonly used in laboratory and engineering applications, their properties, ideal uses, and limitations. It also touches on general principles for designing strong adhesive joints.

## General Principles of Adhesive Bonding

Adhesive bonding is an effective method for assembling structures, particularly for temporary setups or when high precision and stiffness are required without the distortions associated with welding <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. Adhesive bonds can also be temporary; many adhesives can be heated to around 150-300°C to allow for disassembly <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

### Designing for Strength
*   **Shear Mode**: A proper adhesive joint should always be designed to work in [[adhesion_failure_modes_and_design_considerations | shear mode]] <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. In shear mode, the load is instantly applied to the entire joint area, distributing the stress efficiently <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>. A properly prepared and cured epoxy shear joint can withstand significant force (e.g., 2 tons on a 1/10th scale model, equating to 200 tons for a full-sized structure) <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.
*   **Tension Mode**: Designing joints for tension is possible but generally results in weaker bonds compared to shear <a class="yt-timestamp" data-t="14:11:00">[14:11:11]</a>.
*   **Peel Mode**: Adhesives should *never* be designed to work in [[adhesion_failure_modes_and_design_considerations | peel mode]] <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. Rigid adhesives like epoxy have virtually zero strength in peel mode because all the stress is concentrated on a single line where separation begins, leading to instant failure <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. Even joints that appear to be in tension might actually be in peel mode under load <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>. Flexible adhesives, like RTV or polyurethane, perform better in peel mode as they can stretch and distribute the stress over a larger area <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>.

### Surface Preparation
For most adhesives, proper [[preparing_surfaces_for_painting_and_bonding | surface preparation]] is crucial for a strong bond. This is similar to preparing surfaces for painting <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.
*   **Preferred Method**: [[sand_blasting_for_adhesion_and_painting | Sand blasting]] is the preferred method for preparing surfaces <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.
*   **Alternatives**: Bluing or using bathroom cleaners like Comet or Ajax can also be effective <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
*   **Exceptions**: Some adhesives, like RTV silicone, form tenacious bonds to certain materials (e.g., [[Unique Properties of Glass in Engineering Applications|glass]]) without extensive surface preparation <a class="yt-timestamp" data-t="19:13:00">[19:13:00]</a>.

### Thermal Expansion Considerations
Adhesives, being polymers, have coefficients of thermal expansion roughly an order of magnitude higher than metals <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>. This means they expand about ten times faster with temperature changes. When bonding components that require high precision, such as mirrors to metal, consider:
*   **Differential Expansion**: The base materials (e.g., [[Unique Properties of Glass in Engineering Applications|glass]] and metal) will have different expansion coefficients <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.
*   **Bonding Layer Expansion**: The adhesive layer itself will expand significantly <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>. If the bond is a uniform, parallel layer, the resulting parallel shift (e.g., 5 microns for a 50-micron layer with 10% thickness change) might be acceptable <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>. However, if the adhesive forms a wedge (e.g., for alignment purposes), temperature changes can cause the component (like a mirror or bracket) to tilt, with the error magnified by the optical or physical lever <a class="yt-timestamp" data-t="25:15:00">[25:15:00]</a>.

## Types of Adhesives

There are about four main types of adhesives commonly needed in a lab environment <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>:

### 1. Epoxy
*   **Properties**: Commonly used, rigid, and available in fast-curing formulas (e.g., 5-minute epoxy) <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>. To extend the working time of fast epoxy, mix it on a chilled piece of metal like aluminum <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. While it may set quickly, reasonable strength requires an hour or more of curing <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Applications**: Good for shear joints in [[adhesive_bonded_joints_in_large_structures | building large structures]] where rigidity is desired <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. Can be used for temporary structures that are heated to disassemble <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
*   **Limitations**: Poor in peel mode <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. Prone to outgassing, which can be accelerated by baking <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.

### 2. Silicone RTV (Room Temperature Vulcanizing)
*   **Properties**:
    *   **High Temperature Resistance**: One of the few common adhesives that can withstand high temperatures; clear RTV handles up to 250°C, and red (iron cure) RTV can take 300°C or more <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.
    *   **Elasticity**: Stays elastic indefinitely <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
    *   **Bonding to Specific Materials**: Forms a tenacious bond to [[Unique Properties of Glass in Engineering Applications|glass]] and certain ceramics, often without the need for [[preparing_surfaces_for_painting_and_bonding | sand blasting]] or other surface preparation <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>. This is due to its ability to form a chemical bond <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>.
    *   **Peel Strength**: Better peel strength than epoxy due to its flexibility, which distributes stress over a larger area <a class="yt-timestamp" data-t="21:21:00">[21:21:00]</a>.
*   **Applications**: Ideal for components exposed to heat, such as heaters <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>. Widely used in aquariums to bond glass plates <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>. Suitable for applications where some flexibility is needed, or where joints may inadvertently enter peel mode <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>.

### 3. Polyurethane
*   **Properties**: Flexible and forms a tenacious bond to flexible materials like rubber <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. Unlike rigid adhesives, it bonds well to slightly flexible materials <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. Some types are designed to foam up and fill gaps (e.g., Gorilla Glue) <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>. It has good peel strength <a class="yt-timestamp" data-t="20:23:00">[20:23:00]</a> and is considered a better adhesive than epoxy for certain applications <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.
*   **Applications**: Excellent for bonding sheets together <a class="yt-timestamp" data-t="20:18:00">[20:18:00]</a>. Useful when flexibility is desired or where joints may enter peel mode <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>.
*   **Limitations**: Typically requires overnight curing <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>.

### 4. Spray Contact Cement
*   **Properties**: Designed for covering large surfaces uniformly <a class="yt-timestamp" data-t="20:34:00">[20:34:00]</a>.
*   **Applications**: Used for attaching large sheets.
*   **Limitations**: Requires application to both surfaces to be bonded <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>. Other adhesives usually only need application to one side <a class="yt-timestamp" data-t="20:43:00">[20:43:00]</a>.

### Adhesives to Avoid (for Scientific Work)

### Cyanoacrylates (Super Glue / Magic Glue)
*   **Properties**: Very rigid and brittle, making joints susceptible to shock loads <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>.
*   **Applications**: Good for bonding rubber instantly, such as O-rings <a class="yt-timestamp" data-t="22:38:00">[22:38:00]</a>.
*   **Major Drawbacks (especially for scientific/optical work)**:
    *   **Outgassing**: Slowly emits gas, which can fog up optics within a few weeks, rendering them unusable <a class="yt-timestamp" data-t="22:44:00">[22:44:00]</a>.
    *   **Plastic Degradation**: Can cause plastics to "craze," meaning they develop micro-cracks over time <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>.
*   **Recommendation**: Generally not recommended for scientific work due to these side effects and significant ongoing outgassing <a class="yt-timestamp" data-t="23:21:00">[23:21:00]</a>.