---
title: Metal 3D printing process
videoId: nyYcomX7Lus
---

From: [[dgelbart]] <br/> 

[[metal_3d_printing | Metal 3D printing]] is considered more important in the long run than plastic 3D printing, primarily due to its potential for production applications [00:00:22]. While plastic 3D printing is mainly useful for prototypes, with excellent mass production methods like injection molding available for high-volume, low-cost plastic parts, metal production lacks similar efficient mass production methods [00:00:32].

For low-melting metals like zinc alloys, die-casting (similar to injection molding) can be used, as seen in old carburetors or current car engines [00:00:52]. However, these alloys are often not very strong or corrosion-proof [00:01:21]. High-performance metal parts, typically made of steel, stainless steel, or special alloys, are difficult to manufacture, and there isn't a true mass production method for them that is both low-cost and high-quality [00:01:27]. Existing metal production methods like CNC machining, investment casting, regular casting, and forging are costly and time-consuming, affecting per-part cost [00:02:15].

[[metal_3d_printing | Metal 3D printing]] is exciting because it offers not just a prototyping method but also a production method for very complex parts, with costs projected to decrease over time [00:02:40].

## [[advantages_of_metal_3d_printing | Advantages of Metal 3D Printing]]

[[metal_3d_printing | Metal 3D printing]] offers enormous benefits for specific categories of parts [00:04:21]. The benefit is proportional to the amount of internal features or structures within a part [00:04:30].

*   **Internal Complexity**: Parts with internal cavities or undercuts that are difficult or impossible to reach with traditional machining tools are natural candidates for [[metal_3d_printing | metal 3D printing]] [00:04:58]. For example, a miniature manifold with curved passages and thin walls would be impossible to machine, even with EDM, and would be very expensive and time-consuming (weeks) for investment casting [00:05:59]. [[metal_3d_printing | Metal 3D printing]] can produce such complex parts in one to two days [00:06:27].
*   **Thin Walls**: Parts with very thin walls are particularly suited for [[metal_3d_printing | metal 3D printing]] because they require little metal deposition, leading to faster printing times (e.g., two hours) [00:08:28]. Conversely, thick-section parts are much faster and cheaper to produce via CNC machining [00:07:59]. Internal complexity (hollow spaces) makes 3D printing faster while making machining much slower or impossible [00:08:49].
*   **Exotic Alloys**: When purchasing metal in powdered form for 3D printing, the cost difference between plain steel and high-grade stainless steel is negligible [00:09:15]. Printing time is also similar across different metals [00:09:37]. This allows for the use of exotic alloys that would typically be harder to machine but are natural fits for 3D printing processes [00:09:48].

## [[challenges_and_limitations_of_metal_3d_printing | Challenges and Misconceptions of Metal 3D Printing]]

Many sample parts showcased by [[metal_3d_printing | metal 3D printing]] companies, such as wrenches or channel locks, could be produced significantly faster and cheaper using traditional methods like CNC machining [00:03:06]. A simple wrench, for instance, can be made in 10 minutes on a CNC machine, whereas it might take a day to produce with [[metal_3d_printing | metal 3D printing]] due to post-processing like [[sintering_in_metal_3d_printing | sintering]] or finishing operations [00:03:43].

!> **Organic Design Hype**: While some promote "organic design" (free-flowing forms) enabled by [[metal_3d_printing | metal 3D printing]], such parts often require post-machining for features like accurate holes or threads [00:06:46]. Fully organic shapes can be challenging to clamp for post-machining, potentially requiring custom 3D-printed clamps, which adds to the overall cost [00:07:22].

## Materials for Metal 3D Printing

Currently, stainless alloys are the most popular choice for metal 3D printing [00:09:08]. This is because the cost of powdered plain steel and high-grade stainless steel is approximately the same, and printing/[[sintering_in_metal_3d_printing | sintering]] times are similar [00:09:15]. This encourages the use of higher-performance materials [00:09:42].

## [[sintering_in_metal_3d_printing | Sintering in Metal 3D Printing]]

[[sintering_in_metal_3d_printing | Sintering]] is a crucial process in [[metal_3d_printing | metal 3D printing]] [00:10:10]. It involves taking metal powder, shaping it, and lightly holding it together with a binder or pressure [00:10:21]. This shaped part is then heated in a furnace to a temperature below its melting point, but high enough for the individual particles to metallurgically bond and fuse together, densifying the part and increasing its strength [00:10:33].

*   **Astonishing Process**: Intuitively, one might expect significant distortions when heating metal powder, especially irregularly shaped particles, to temperatures near its melting point [00:11:06]. However, the part remarkably shrinks uniformly in all directions with a very predictable ratio and accuracy, typically achieving accuracies within a fraction of 1% [00:12:27]. This uniform shrinkage occurs regardless of the shape's complexity, with no visible distortion [00:12:55].
*   **Historical Significance**: [[sintering_in_metal_3d_printing | Sintering]] is one of the oldest processes in history, dating back 25,000 years for ceramics (e.g., clay pottery) [00:13:16]. Metal [[sintering_in_metal_3d_printing | sintering]] is also thousands of years old [00:13:37]. The Iron Pillar of Delhi, made about 1,500 years ago, is believed to be the largest sintered object ever created (seven meters tall, six tons) [00:13:40]. Ancient civilizations could sinter metals like platinum or steel because it required lower temperatures than casting, which was difficult to achieve with primitive furnaces [00:14:15]. Inca jewelry also utilized platinum [[sintering_in_metal_3d_printing | sintering]] [00:14:57].

## Main Metal 3D Printing Methods

There are two primary methods for 3D printing metal objects with internal complexity:

### 1. Sintering-Based Methods (Pattern-wise Deposition of Powder)

This approach involves depositing metal powder mixed with a binder (plastic or liquid) layer by layer [00:16:00]. The binder holds the shaped powder together, and after printing, the part undergoes a [[sintering_in_metal_3d_printing | sintering]] process [00:16:15].

*   **Process Steps**:
    1.  **Printing**: Metal powder is mixed with a binder (e.g., polymer) to form a paste or filament [00:16:08]. This material is then deposited layer by layer using an FDM-type printer, or a binder is jetted onto a powder bed to selectively bind particles [00:16:22].
    2.  **Green Part**: The printed object, called a "green part," is fragile (e.g., "strength of chalk") but maintains its shape [00:16:53].
    3.  **Sintering**: The green part is placed in a [[sintering_in_metal_3d_printing | sintering]] furnace. During [[sintering_in_metal_3d_printing | sintering]], the binder evaporates, and the metal particles fuse together, causing the part to shrink uniformly (typically 16-17%, sometimes up to 20% if all air gaps disappear) and become a solid metal object [00:17:06].

*   **Rapidia System Example**:
    *   This system comprises a printer (similar to a plastic FDM printer) and a fully automated [[sintering_in_metal_3d_printing | sintering]] furnace [00:29:47].
    *   It uses a metal paste supplied in cartridges [00:30:37].
    *   The furnace operates with a gas mixture (e.g., 3% hydrogen with 97% argon) to prevent oxidation, making it safe for office environments [00:30:07].
    *   Printing typically occurs on aluminum foil, which allows for easy removal of the part [00:31:54].
    *   A typical [[sintering_in_metal_3d_printing | sintering]] cycle (heating, ramp-up, cooling) can take approximately 22-24 hours [00:34:01].

*   **Support Structures**:
    *   Support is often needed during printing to prevent elevated parts from sagging [00:35:28].
    *   The Rapidia system uses a "white material" for support that evaporates during [[sintering_in_metal_3d_printing | sintering]], avoiding wasted metal [00:36:29].
    *   A separation layer of white material can be used with metal supports, allowing them to be easily broken off by hand without tools [00:36:10].
    *   This method generally doesn't require a base raft, further reducing wasted metal [00:36:48].
    *   Complex internal structures can be created without print support by printing parts separately and then bonding them with water (which temporarily re-liquifies the "green" paste) before [[sintering_in_metal_3d_printing | sintering]] [00:37:27]. The bond after [[sintering_in_metal_3d_printing | sintering]] is as strong as printed layers [00:38:09].
    *   Machined parts can be combined with 3D printed parts by using printing paste as an adhesive, then re-sintering to create a single, solid metal piece [00:39:02].
    *   The water-based paste avoids the need for a de-binding machine or infill structures, as the small amount of binder evaporates easily in the furnace [00:40:11]. This allows for 100% solid, strong parts [00:40:35].

*   **[[advantages_of_metal_3d_printing | Advantages]]**:
    *   **Simplicity and Low Cost**: The systems are significantly less expensive than laser systems (under $200,000 for a complete installation, compared to $1 million) [00:41:24].
    *   **Office Friendly**: No solvents, no special power requirements, and minimal ventilation needed [00:41:58].
    *   **Reduced Post-processing**: Less "backroom" work compared to laser systems, saving time and cost [00:41:52].

*   **[[challenges_and_limitations_of_metal_3d_printing | Disadvantages]]**:
    *   **Object Size Limitation**: Due to the softness of the part during [[sintering_in_metal_3d_printing | sintering]], there's a practical limit to object size (e.g., similar to a shoebox) [00:42:10]. Larger objects would sag [00:42:29].
    *   **Limited Metal Choice**: Currently, fewer metal options are available compared to laser systems (e.g., four metals plus ceramics) [00:43:32].

### 2. Laser-Based Methods (Pattern-wise Deposition of Energy)

This approach involves putting metal powder everywhere and then selectively melting it together with a focused energy source, typically a fiber optic laser [00:18:52]. These methods are often referred to as Selective Laser Sintering (SLS) or Selective Laser Melting (SLM), though they involve more melting than [[sintering_in_metal_3d_printing | sintering]] [00:20:18].

*   **Process Steps**:
    1.  **Powder Bed**: A layer of metal powder is spread across a build plate [00:19:55].
    2.  **Melting**: A laser (or electron beam) scans and melts a specific pattern on the powder bed, forming one layer of the object [00:19:24].
    3.  **Layering**: Another layer of powder is applied, and the process is repeated until the part is complete [00:21:22].

*   **Support Structures**:
    *   These systems require extensive support structures for parts with overhangs [00:21:54].
    *   The main reason for support is to counteract stresses built up as molten layers cool rapidly, preventing the part from warping [00:22:33]. Parts must be held firmly to a thick base plate [00:23:13].

*   **Post-processing**: This method requires significant "backroom" operations:
    1.  **Heat Treatment**: The entire part must be heat-treated in a controlled atmosphere furnace (to prevent oxidation) to anneal and remove stresses [00:24:05]. These furnaces are expensive [00:24:37].
    2.  **Support Removal**: Supports, which are integrally connected to the part, must be removed [00:23:34]. This often involves a wire EDM (electrical discharge machining) for steep curvatures, followed by manual methods like belt sanders for complex contours [00:24:47]. This finishing process can take a full day [00:25:53].

*   **[[advantages_of_metal_3d_printing | Advantages]]**:
    *   **Unlimited Object Size**: Can create very large objects (multiple meters in size) [00:44:06].
    *   **Wider Metal Choice**: Offers a broader selection of metals compared to [[sintering_in_metal_3d_printing | sintering]]-based systems [00:43:03].

*   **[[challenges_and_limitations_of_metal_3d_printing | Disadvantages]]**:
    *   **High Cost**: Systems are very expensive, costing around $1 million for a complete installation including necessary post-processing equipment [00:26:25].
    *   **Extensive Post-processing**: Requires significant manual labor and specialized machinery after printing [00:25:33].
    *   **Safety Requirements**: Metal powders can be explosive, necessitating specialized, explosion-proof installations with fire protection (e.g., Halon extinguishers) [00:26:43]. Not suitable for office environments [00:26:54].
    *   **Longer Overall Time**: The total time to produce a finished part is much longer due to the extensive backroom operations [00:45:10].

## Market Segmentation

The two main [[metal_3d_printing | metal 3D printing]] methods serve distinct markets [00:45:25]:

*   **Laser Systems (SLS/SLM)**: Best suited for large production facilities in industries like aerospace or medical, which often require large objects made from high-net-value materials like titanium [00:27:08].
*   **Sintering-Based Systems (FDM-type/Binder Jetting)**: Ideal for R&D labs, prototyping, educational institutions, and small-batch production due to their lower cost, office-friendly nature, and simpler operation [00:45:42]. Binder jetting systems, while faster and generally cheaper than laser systems, fall in between the FDM-type and laser systems in price [00:46:01].

---
_Disclaimer: The speaker discloses his commercial interest as a partner in Rapidia, a company making sintering-type metal 3D printers, and acknowledges potential bias [00:28:02]._