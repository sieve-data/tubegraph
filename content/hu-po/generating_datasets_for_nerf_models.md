---
title: Generating datasets for NeRF models
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 

Neural Radiance Fields (NeRFs) require comprehensive datasets, typically composed of multiple images of a scene captured from various viewpoints, along with corresponding camera position data, to reconstruct a 3D scene <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.

## Methods for Dataset Generation

One experimental approach to generate datasets for NeRF creation involves using [[Data Generation for AI Models | generative AI]] tools <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. The goal is to create [[synthetic_data_sets_for_training_ai | synthetic data sets for training AI]] models, specifically for a NeRF <a class="yt-timestamp" data-t="01:02:15">[01:02:15]</a>.

### Using Midjourney

The generative AI tool Midjourney was utilized to produce images for a NeRF dataset <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. The process involved generating images of a subject, such as a white Bengal cat, from different perspectives, including:
*   Facing the camera (portrait shot) <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>, <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>
*   Profile view <a class="yt-timestamp" data-t="01:04:27">[01:04:27]</a>
*   From behind (back of the head) <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>
*   Three-quarter pose <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>

These images are intended to be placed into a "images" folder, alongside `transforms.json` and `Basecamp` files, mirroring the structure of existing NeRF datasets like `Nerf Studio poster` <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>, <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.

## Data Considerations and Challenges

When creating a dataset for NeRFs, several factors are crucial:
*   **Camera Positions:** Precise camera position data (like `call map data`) is essential for the NeRF to understand the spatial relationships between images <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>.
*   **Background Consistency:** For effective 3D reconstruction, it is important that all images of the subject have a consistent or the same background <a class="yt-timestamp" data-t="01:16:48">[01:16:48]</a>.
*   **Variety of Angles:** A sufficient variety of angles is needed to capture the object comprehensively <a class="yt-timestamp" data-t="01:12:06">[01:12:06]</a>.

Despite generating images from various angles, initial expectations suggested that a dataset created with this method might have limitations:
> "This is probably not going to be enough images and the quality of the actual Nerf that comes out of it's pretty probably going to be pretty poor but hopefully it's interesting." <a class="yt-timestamp" data-t="01:21:47">[01:21:47]</a>