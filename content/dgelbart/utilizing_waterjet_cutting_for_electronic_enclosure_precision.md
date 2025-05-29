---
title: Utilizing Waterjet Cutting for Electronic Enclosure Precision
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

Creating an electronic enclosure from sheet metal involves a multi-step process, from initial design and cutting to bending, welding, and finishing. [[Waterjet cutter for prototyping|Waterjet cutting]] plays a crucial role in achieving high precision and efficient fabrication.

## Design and Initial Preparation

The process begins by downloading the enclosure design, typically in a DRD or DXF file, and converting it for the fabrication system [00:00:20]. Once the design is ready, the material is clamped down, and its thickness is entered into the system [00:00:31]. The cutting head's height is set by bringing it to touch the material and then raising it half a millimeter [00:00:37].

After the initial cut, the first step is to break any sharp edges to protect hands and ensure that subsequent parts lie flat [00:01:21]. This is particularly important for patterned cuts which can be rough [00:01:37].

## Correcting Mistakes with Spot Welding

Mistakes, such as an extra cut or a misplaced hole, can occur [00:01:52]. Instead of scrapping the part, errors can be repaired using a spot welder [00:01:59]. The technique involves placing a slightly oversized piece of material over the defect and melting it into the hole [00:02:14]. For a slot, a strip slightly wider than the slot (by about 0.5 to 1 mm) is cut and melted over the area using a high setting [00:02:31]. After welding, the excess material is cut off and the corner touched up [00:03:06]. A perfectionist might even sand the top surface [00:03:22]. The plug doesn't need to be round; a square plug slightly larger than the hole will work, as the high current melts and overfills the area, allowing for sanding of the excess [00:03:31].

## Bending Operations

Bending is a critical phase where precision and planning are essential [00:04:04].

### Order of Bends
It is crucial to think through the order of bends, as some parts can only be bent in a specific sequence to avoid the part jamming in the machine [00:04:09]. For example, outer edges might need to be bent up first before inner bends, to ensure the die can fit between the already bent edges [00:04:22]. Bending in the wrong order can make subsequent bends impossible [00:04:37].

### Orientation and Tooling
Unless a part is symmetric, it's vital to correctly orient the part to avoid creating a mirror image [00:04:51]. This is a common mistake that can lead to extensive straightening [00:04:59].

When bending the periphery, the correct tooling must be selected [00:06:03]. The length of the die should match the bend length; if a single long die isn't available, segmented dies can be used [00:07:10]. Minor gaps in segmented dies typically do not affect the quality of the bend, but can be touched up if necessary [00:07:51].

### Incorporating Inserts
Before completing all bends, it is often much easier to spot weld in components like rivet nuts or threaded inserts [00:10:00]. While possible to do after bending, flat parts are simpler to work with [00:10:07].

## Cover Fitting and Design Considerations

Creating a perfectly fitting cover requires accounting for material thickness and bend radius, which are complex calculations [00:11:23]. A simpler and more reliable method is to cut a test strip of the same width as the cover [00:11:40]. CAD programs like SolidWorks sheet metal option can provide initial bend calculations [00:11:48]. The test strip is bent according to these calculations, and then tested against the main enclosure [00:12:00]. Adjustments are made based on the fit until it's perfect [00:12:03].

A common design practice is to recess the cover a couple of millimeters from the end [00:14:26]. This allows the rounded edge of the bend to be exposed, preventing sharp edges that can cause injury or lead to paint chipping [00:14:41].

## Waterjet Advantages for Enclosure Design

[[Efficient fabrication methods using water jets|Waterjet cutting]] offers several advantages for enclosure design:

*   **Integrated Features**: The [[Benefits and applications of water jet cutting|waterjet]] can cut specific features like "keys" for toggle switches or double-D shaped holes for components with anti-rotation features [00:18:11]. This prevents components from rotating after installation [00:18:48].
*   **Knockouts**: To provide flexibility for future modifications, [[waterjet cutter for prototyping|knockouts]] can be incorporated [00:19:01]. These are partially cut holes held in place by small tabs that can be easily punched out later, even after assembly [00:19:10].
*   **Component Integration**: Any small brackets, clamps for cables, or other internal components can be laid out and cut from the same sheet of metal as the main enclosure [00:19:40]. This ensures consistent material and allows all parts to be painted together [00:19:53].
*   **Precision**: All holes in a single plane will be perfectly registered, as the machine is accurate to about 0.1 mm [00:20:25]. However, registration is lost across bend lines because of variations in bend squareness and material deformation during bending [00:20:36].
*   **Avoiding Distortion**: Holes or openings placed too close to a bend line can distort significantly [00:21:35]. For example, a round hole near a bend line will lose its roundness [00:21:55]. It is advisable to keep any openings at least 10-15 mm away from bend lines to avoid distortion [00:22:22]. If a hole *must* be on a bend line, making it a U-shape where the flat sides align with the bend can help maintain shape [00:22:06].

## Hardware Installation

All necessary studs and nuts should be installed *before* sandblasting and painting [00:22:41]. [[High precision machining techniques|Captive hardware]] is highly important in electronic assembly to prevent screws from falling and shorting out circuit boards [00:24:28]. For standard round head studs, the waterjet can drill a slightly larger hole, allowing the installer to feel when the stud head is properly seated [00:23:56].

## Finishing: Sandblasting and Painting

Before painting, areas where paint is not desired (like studs) are masked off using silicone rubber tubes or Kapton tape, which can withstand high temperatures [00:25:33]. Hangers are used to suspend the part, designed to touch in invisible areas to avoid leaving marks [00:26:02]. Hangers cannot be reused for powder coating because they are designed to ground the part, and once coated, they lose their conductivity [00:26:28].

The powder coating process typically involves baking the part in an oven. A nominal procedure is five minutes at 235°C (380°F) for the paint to flow, followed by fifteen minutes at 190°C (less than 350°F) for crosslinking [00:27:09]. Crosslinking is crucial for paint hardness [00:28:07]. Leaving it at the higher temperature for the entire duration can cause white paint to yellow slightly to a light beige, which may be acceptable [00:27:39].

During electrostatic painting, voltage can be reduced for inside corners to minimize electrostatic shielding and ensure even coating [00:28:29]. A proper enclosure made of non-metal would attract powder directly to the workpiece, reducing overspray [00:29:22]. In a professional setup, the part would hang on a rotating shaft for even coverage [00:29:51]. If the powder is accidentally touched before baking, it can be oversprayed [00:30:46].

After cooling, any protective covers are removed [00:31:39]. Threads are then cleaned to remove residue from spot welding and painting [00:32:03].

## Final Assembly

The final step is to mount the cover and ensure all components align perfectly [00:32:37]. The design should prioritize the use of keyholes and slots with captive hardware wherever possible [00:33:04]. This allows the cover to be slid off without completely removing screws, significantly speeding up assembly and maintenance [00:32:57].