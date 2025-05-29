---
title: Reaming and Boring Processes
videoId: a_E-tYRxBkU
---

From: [[dgelbart]] <br/> 

When creating holes in metal, especially for precision applications, more advanced techniques beyond simple drilling are often required. Two such processes are reaming and boring, which offer improved accuracy and surface finish.

## Initial Hole Preparation

Before performing reaming or boring, a preliminary hole is typically drilled. It is crucial to start with a smaller diameter hole before enlarging it to the final size [00:02:51]. This is because a larger drill's web width can straddle the center mark, preventing accurate self-centering. A smaller drill will center itself precisely on the marked point, guiding the subsequent larger operations [00:03:46].

### Locating the Hole Accurately
To precisely locate a hole, the following steps are recommended:
1.  **Center Punching**: Guide the drill by center punching the desired location [00:00:27].
2.  **Scribing Lines**: Lay out and scribe lines using a scriber to define the hole's position [00:00:37].
3.  **Feel for Accuracy**: Do not rely on visual alignment. Instead, locate the center punch by feel, sliding it along the scribed lines until it locks into the intersection [00:00:50]. This method is significantly more accurate than looking [00:00:53].
4.  **Light Mark, Then Reinforce**: Make a light center mark first, then reinforce it with a bigger mark [00:01:31].
5.  **Sharp Punches**: Ensure center punches are very sharp, typically sharpened at about a 90-degree tip angle, to allow for tactile feedback [00:01:41].
6.  **Enhance Visibility**: If lines are difficult to see, apply a washable marker over the area. The marker will highlight the scribed lines, which can then be wiped off instantly after marking [00:02:05].

For improved precision, starting with a center drill is advisable, especially if a center punch wasn't used [00:06:27]. A center drill is very rigid and will not wander off [00:06:30].

## Reaming

Reaming is used when drilling alone does not provide sufficient diameter accuracy or surface finish, such as for a bearing or shaft fit [00:07:24].

### Process for Reaming
1.  **Undersized Drill**: Drill a hole that is undersized by typically 0.1 to 0.2 millimeters [00:06:46].
2.  **Lubrication**: Apply cutting oil or wax to the reamer, particularly for materials like aluminum that can stick to the tool [00:07:43].
3.  **Low Speed**: Perform the reaming operation at a low speed [00:07:54].
4.  **Self-Alignment**: Do not be concerned about run-out; the reamer is flexible and will find its own place in the hole [00:08:01].
5.  **Result**: A reamed hole provides a nice, tight fit, for example, for a 10-millimeter dowel pin [00:08:15].

### Important Considerations for Reaming
Reamers are slightly tapered and require going all the way through the material to achieve accuracy [00:09:50]. This means they are not suitable for blind holes [00:09:48].

### Inserting Precise Shafts into Holes
When fitting a very precise shaft into a very precise hole, binding can occur due to fundamental geometry [00:08:33]. To avoid this "locking condition" [00:08:48]:
*   Machine a recess in the shaft [00:08:51].
*   Leave about one millimeter of the full diameter, followed by a groove a few millimeters wide, and then resume the full diameter [00:08:54].
*   This design allows a narrow ring of the shaft to tilt within the hole, preventing binding. As it goes deeper, the second correct diameter aligns itself [00:09:06]. This trick is essential for large shafts and bearings, preventing hours spent trying to fit them [00:09:24].

## Boring

Boring is another method for creating accurate holes, offering comparable accuracy to reaming but with the advantage of variable size capability [00:06:08]. It is particularly suitable for large holes where large reamers are difficult to obtain, or for creating blind holes [00:09:58].

### Process for Boring
1.  **Boring Head**: Use a boring head for the operation [00:10:00].
2.  **Single-Point Cutting**: Boring involves a single-point cutting action, unlike drilling which has two cutting lips that balance forces [00:10:10]. This makes machine rigidity critically important [00:10:06].
3.  **Machine Rigidity**:
    *   Lock the machine [00:10:31].
    *   Minimize quill overhang [00:10:25].
    *   Ensure everything is tight and rigid [00:10:40].
4.  **Adjust Diameter**: Adjust the boring head to achieve the desired diameter [00:10:42].
5.  **Material-Specific Speed**: Adjust cutting speed based on the material, for example, faster for aluminum [00:11:00].
6.  **Steps and Blind Holes**: Boring can machine to a specific step and doesn't require going all the way through, making it suitable for blind holes [00:11:13].
7.  **Finishing Pass**: Make one or two final passes to remove any flagship (burrs or rough edges) from the tool [00:11:22].

A properly bored hole provides a nice finish, suitable for a shaft [00:11:36].

## General Machining Considerations

### Mill Stiffness
When [[Milling with Ball Nose and Regular Cutters | milling]] or boring, the stiffness of the mill (or the machine setup) is crucial for speed and accuracy. The stiffness relates to how much the mill can deflect [00:12:59]. The formula for stiffness is approximately D^4 / L^3, where D is the diameter and L is the length [00:13:12]. This means:
*   A twice-larger diameter and half the length can result in 128 times higher stiffness [00:13:28].
*   Design parts to allow for the biggest possible mill diameter and the shortest possible mill length [00:13:40]. This implies leaving the largest possible radii for corners if sharp corners are not strictly needed [00:13:49].
*   When designing housings for [[modifications_for_milling_machines | milling machines]], try to split them in the middle rather than having a deep housing and a shallow top. A deeper housing requires a longer mill, making it significantly less stiff [00:13:57].

### Clamping Strategy
Minimizing the number of clamping operations is vital for both accuracy and efficiency [00:14:44].
*   **Accuracy Loss**: Re-clamping a workpiece causes a loss of accuracy because features are no longer registered to each other consistently [00:15:53].
*   **Time Saving**: Less clamping means less manual intervention, allowing CNC machines to operate for longer periods unsupervised [00:16:10].
*   **Strategic Clamping**: By clever clamping, it's possible to machine multiple sides (e.g., inside, top, and two sides) in one clamping [00:14:57].
*   **Tooling Holes**: Consider adding "tooling holes" or clamping holes in areas that are not critical or will be covered later (e.g., by a cover). These holes allow the workpiece to be bolted directly to the T-slots of the machine, enabling five out of six sides to be machined in a single clamping operation [00:15:16].