---
title: Multiresolution hash grids
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

Multiresolution hash grids are a powerful data structure used in neural scene representations, particularly for achieving high-fidelity 3D surface reconstruction and novel view synthesis <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. They combine the representation power of multi-resolution 3D hash grids with neural volume rendering <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.

## Core Concept and Functionality
A hash is fundamentally a map, establishing a correspondence between a key and a value <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. In the context of 3D hash grids, the key is a 3D position in space, which maps to some stored value <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This allows for quick access to information within a 3D volume <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

The "multi-resolution" aspect means there are different sizes or scales at which this hash map is created with respect to the volume <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This can involve coarse, fine, and even extra-fine resolutions <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### How it Works
1.  **Multiple Grids:** Instead of a single grid, there are multiple grids (L total grids) at different spatial resolutions, from V1 to VL <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>. For example, the Neural Angelo paper uses 16 total grids <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>.
2.  **Position Mapping:** An input 3D position `x` is mapped to a corresponding position within each grid resolution `V_L` <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>.
3.  **Feature Storage:** Each hash entry (or item in the map) stores an "encoding feature" <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>. This feature is a vector (e.g., 8 elements in the Neural Angelo paper) <a class="yt-timestamp" data-t="01:50:06">[01:50:06]</a>.
4.  **Tri-linear Interpolation:** For a given position, the feature vector for each resolution is obtained by tri-linear interpolation of the hash entries at the grid cell corners <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>. This allows for meaningful interpolation between feature vectors encoded within a spatial grid <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.
5.  **Concatenation:** The encoding features from all spatial resolutions are concatenated to form a single, larger feature vector <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>. This combined feature vector then serves as input to a shallow multi-layer perceptron (MLP) <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>.

## Advantages
*   **High Representation Power:** The hybrid representation greatly increases the capacity to represent very fine-grained details <a class="yt-timestamp" data-t="02:05:01">[02:05:01]</a>.
*   **Scalability and Efficiency:** It enables lightweight MLPs that are more expressive with a memory footprint that is log-linear to the resolution <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. This addresses the high computational cost associated with traditional [[Memory and Computational Efficiency in PointBased Methods | neural volume rendering]] methods like Nerfs, where inference is required for every pixel <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>.
*   **Implicit Levels of Detail (LOD):** The multi-resolution nature naturally lends itself to creating different levels of detail for an object, allowing for faster processing when high detail isn't necessary <a class="yt-timestamp" data-t="02:00:20">[02:00:20]</a>.

## Comparison to Other Methods
Unlike sparse voxel structures such as Octrees, which use a hierarchical spatial decomposition and can struggle to recover surfaces misrepresented by coarser resolutions, hash encoding assumes no spatial hierarchy <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>. Instead, it automatically resolves collisions based on gradient averaging <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>.

## Application in Neural Angelo
In Neural Angelo, multi-resolution hash encodings are a core component for [[Rendering Technology and Algorithms | neural volume rendering]] and [[3D content generation using gaussian splatting | 3D surface reconstruction]] from RGB images <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It adopts the Instant NGP (Neural Graphics Primitives) framework, which introduced the multi-resolution hash encoding <a class="yt-timestamp" data-t="01:59:57">[01:59:57]</a>.

Neural Angelo uses the hash encoding to combine with a Neural SDF (Signed Distance Function) representation of the underlying 3D scene <a class="yt-timestamp" data-t="02:05:03">[02:05:03]</a>. Key aspects of its implementation include:
*   **Numerical Gradients:** Because the analytical gradients of hash encoding are not continuous across space under tri-linear interpolation (due to rounding operations for sampling locations), Neural Angelo computes surface normals using numerical gradients <a class="yt-timestamp" data-t="01:15:32">[01:15:32]</a>. This allows backpropagation updates to extend beyond just the local hash grid cell, acting as a smoothing operation <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.
*   **Course-to-Fine Optimization:** A progressive optimization schedule is employed, utilizing the multi-resolution aspect <a class="yt-timestamp" data-t="02:09:57">[02:09:57]</a>.
    *   The optimization starts with a larger step size (epsilon) for numerical gradients and coarser hash grids <a class="yt-timestamp" data-t="01:40:44">[01:40:44]</a>.
    *   As optimization progresses (e.g., every 5000 iterations), new, finer hash resolutions are progressively activated, and the step size decreases to match the grid size <a class="yt-timestamp" data-t="01:51:49">[01:51:49]</a>. This prevents finer grids from having to "unlearn" from coarser optimization and enables [[Patchbased depth prediction techniques | progressive levels of detail]] <a class="yt-timestamp" data-t="01:41:15">[01:41:15]</a>.
    *   Weight decay is applied to all parameters to prevent single-resolution features from dominating the final result <a class="yt-timestamp" data-t="01:42:43">[01:42:43]</a>.

## Implementation Details
In the experiments, Neural Angelo used:
*   16 levels of hash grid resolutions, ranging from 2^5 to 2^16 <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>.
*   Each hash entry had a channel size of 8 <a class="yt-timestamp" data-t="01:50:06">[01:50:06]</a>.
*   The maximum number of hash entries per resolution was 2^22 <a class="yt-timestamp" data-t="01:50:51">[01:50:51]</a>.
*   The optimization started by activating 4 or 8 hash resolutions depending on the dataset <a class="yt-timestamp" data-t="01:50:59">[01:50:59]</a>.
*   A new hash resolution was enabled every 5000 iterations when the step size equaled its grid size <a class="yt-timestamp" data-t="01:51:49">[01:51:49]</a>.