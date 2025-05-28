---
title: Normal maps in 3D modeling
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

Normal maps are a crucial component in 3D modeling, providing detailed geometric information that enhances the visual quality of rendered objects <a class="yt-timestamp" data-t="09:59:01">[09:59:01]</a>. Unlike standard RGB images, which represent color, the value at each pixel in a normal map represents the direction of the normal vector <a class="yt-timestamp" data-t="09:17:15">[09:17:15]</a>. A normal vector is a vector perpendicular to a surface at a given point <a class="yt-timestamp" data-t="09:19:20">[09:19:20]</a>.

## Purpose and Application

Normal maps have been utilized in 3D pipelines for a significant period to achieve a more pronounced 3D effect <a class="yt-timestamp" data-t="09:37:59">[09:37:59]</a>. This effect is an illusion, as physically based rendering pipelines calculate how light rays intersect with an object and consider those angles <a class="yt-timestamp" data-t="10:01:43">[10:01:43]</a>. By knowing the direction of the normal vector of a surface, rendering engines can better calculate how light will bounce, resulting in a higher quality 3D appearance <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. This allows for fine-grained geometric details to be rendered without explicitly modeling every surface undulation <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.

Most [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | graphics rendering pipelines]], including game engines like [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | Unreal Engine]] and Unity, can utilize normal maps to produce an "extra crispy" visual output, making an object appear much better even with the same underlying mesh and texture <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>.

## Generation of Normal Maps

Historically, obtaining normal maps for arbitrary meshes was a challenge <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. However, a key insight in recent research, such as the MeshFormer paper, is the use of [[techniques_for_text_to_3d_conversion_involving_diffusion_models | diffusion models]] to generate these normal maps <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. These 2D [[techniques_for_text_to_3d_conversion_involving_diffusion_models | diffusion models]], trained on billions of natural images, possess extensive priors and can be fine-tuned to predict normal maps from standard RGB images <a class="yt-timestamp" data-t="35:19:00">[35:19:00]</a>. This capability allows for generating additional signal and intelligence for 3D reconstruction models, improving the quality of generated meshes compared to using only explicit 3D and RGB data <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>.

### Normal Maps vs. Depth Maps

While similar in concept, normal maps and depth maps convey different types of geometric information <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.
*   **Normal Map:** Tells you the direction of the surface normal at each pixel <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
*   **Depth Map:** Tells you the distance of that pixel to the camera <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>.

Both can be generated from RGB images using [[techniques_for_text_to_3d_conversion_involving_diffusion_models | diffusion models]] trained on large datasets where ground-truth depth or normal information is available <a class="yt-timestamp" data-t="42:12:00">[42:12:00]</a>. The generalization capability of these models allows them to produce good estimations for arbitrary images <a class="yt-timestamp" data-t="42:50:00">[42:50:00]</a>.

## Integration in Mesh Reconstruction

The MeshFormer paper utilizes multiview RGB images along with their corresponding normal maps as input to reconstruct high-quality 3D textured meshes <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. Each input image has an aligned normal map, pixel by pixel <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. The model uses 3D sparse convolutions and Transformers, leveraging a 3D inductive bias and projective awareness to reconstruct the object <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>. The normal maps, estimated using existing 2D [[techniques_for_text_to_3d_conversion_involving_diffusion_models | diffusion models]], provide crucial guidance for 3D reconstruction, enabling the generation of meshes with enhanced sharp details <a class="yt-timestamp" data-t="35:13:00">[35:13:00]</a>.

After the mesh is generated, the learned 3D normal texture can be exported alongside the color texture, making it compatible with various [[creating_and_managing_3d_assets_and_materials_in_unreal_engine | graphics rendering pipelines]] <a class="yt-timestamp" data-t="35:41:00">[35:41:00]</a>.