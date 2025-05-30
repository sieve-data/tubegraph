---
title: Google research Lum text to video generation
videoId: oyd1b5Oif84
---

From: [[hrishikeshyadav8883]] <br/> 

Google Research has introduced Lum, a new space-time diffusion model for realistic video generation <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. The paper for Lum was released on January 23rd <a class="yt-timestamp" data-t="08:47:01">[08:47:01]</a>.

## Key Features of Lum

Lum videos are characterized by their realism, higher resolution, and significant consistency <a class="yt-timestamp" data-t="01:21:01">[01:21:01]</a>, particularly in global temporal consistency <a class="yt-timestamp" data-t="10:47:01">[10:47:01]</a>. These three aspects—realistic, consistent, and high-resolution—are highlighted as Lum's main key points <a class="yt-timestamp" data-t="08:28:01">[08:28:01]</a>.

### Enhanced Consistency
A notable advantage of Lum is its ability to maintain consistency throughout generated videos, which is often a challenge in prompt-to-video or text-to-video generation models <a class="yt-timestamp" data-t="01:46:01">[01:46:01]</a>. For instance, in a video of a sailboat sailing on a sunny day, Lum consistently renders reflections and other components <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>. This consistency extends to "stylized" parts of the video as well <a class="yt-timestamp" data-t="01:54:01">[01:54:01]</a>.

### Stylized Generation and Image-to-Video
Lum excels in stylized generation, which has been extensively explored in reference image-to-image processes but is new for reference image-to-video <a class="yt-timestamp" data-t="04:40:01">[04:40:01]</a>. This feature allows for the creation of consistent illustrations, GIFs, or product marketing content from a style reference <a class="yt-timestamp" data-t="05:00:01">[05:00:01]</a>. It can even simplify sticker generation by taking a reference image and a simple prompt <a class="yt-timestamp" data-t="05:30:01">[05:30:01]</a>.

### Video Stylization and Inpainting
The model supports video stylization, allowing a source video (e.g., someone running) to be transformed into different styles like a wooden box or origami <a class="yt-timestamp" data-t="06:40:01">[06:40:01]</a>. Lum also features video inpainting, which is described as being very stable and realistic. An example shows how missing elements in a video (e.g., a hand approaching a scene) are consistently and realistically filled in <a class="yt-timestamp" data-t="07:35:01">[07:35:01]</a>.

### Cinemagraphs
Lum can be used for cinemagraphs, similar to [[Runway Gen 2 model|Runway Gen 2]], which involves adding motion to static images to convert them into videos <a class="yt-timestamp" data-t="06:56:01">[06:56:01]</a>.

## Comparison with Existing Models

Existing models like Pika and Runway Gen 2 often exhibit inconsistency, particularly when trying to increase the duration of a generated video beyond short segments like 3 seconds <a class="yt-timestamp" data-t="02:50:01">[02:50:01]</a>. For example, a Pika generation for "Iron Man fighting the Hulk" or an "anime boy playing game with friends" showed random elements appearing in the background and general inconsistency <a class="yt-timestamp" data-t="03:26:01">[03:26:01]</a>.

Lum aims to solve this consistency problem <a class="yt-timestamp" data-t="03:08:01">[03:08:01]</a>. Previous models like Imagen, Pika, and ZeroScope work "bit by bit," leading to inconsistency <a class="yt-timestamp" data-t="06:16:01">[06:16:01]</a>. In contrast, Lum generates the entire temporal duration of the video simultaneously <a class="yt-timestamp" data-t="10:25:01">[10:25:01]</a>, which is a departure from existing models that rely on "bit-by-bit" generation or "temporal super resolution" that makes global temporal consistency difficult <a class="yt-timestamp" data-t="10:38:01">[10:38:01]</a>.

> [!NOTE] [[Evaluation of text to video models and applications|User Study Results]]
> In [[Evaluation of text to video models and applications|user study results]], Lum (represented by a blue line) showed higher quality and better text alignment compared to models like Imagen Video, Pika, and Runway Gen 2 <a class="yt-timestamp" data-t="18:45:01">[18:45:01]</a>. Lum's performance in image-to-video generation, particularly with reference images, also made it stand out <a class="yt-timestamp" data-t="19:09:01">[19:09:01]</a>.

## Technical Architecture: Space-Time Unit Model

The core of Lum's capability is its Space-Time Unit Model architecture <a class="yt-timestamp" data-t="05:57:01">[05:57:01]</a>. This architecture directly generates a full-frame rate by processing data in multiple space-time cells <a class="yt-timestamp" data-t="11:36:01">[11:36:01]</a>. This approach enables it to detect and resolve inconsistencies within both spatial and temporal dimensions of a video <a class="yt-timestamp" data-t="12:45:01">[12:45:01]</a>.

The model uses "XT slice" analysis to visualize and ensure coherence <a class="yt-timestamp" data-t="15:12:01">[15:12:01]</a>. An XT slice represents a mapping of consistency, where 'X' denotes space and 'T' denotes time, allowing for the identification of inconsistencies <a class="yt-timestamp" data-t="13:16:01">[13:16:01]</a>. This is illustrated by showing how Lum maintains details like a horse's legs, which are often inconsistent in other models <a class="yt-timestamp" data-t="14:15:01">[14:15:01]</a>.

Lum's model leverages pre-trained T21 (text-to-image) layers, with only the newly added temporal layers being trained <a class="yt-timestamp" data-t="16:22:01">[16:22:01]</a>.

## Training and Evaluation

Lum's text-to-video (T2V) diffusion model was trained on a dataset containing 30 million videos, each with corresponding text captions <a class="yt-timestamp" data-t="16:54:01">[16:54:01]</a>. The videos were 80 frames long at 16 frames per second (FPS), equating to 5-second clips <a class="yt-timestamp" data-t="17:10:01">[17:10:01]</a>. The model was evaluated using a collection of 113 text prompts, describing diverse objects and scenes <a class="yt-timestamp" data-t="17:22:01">[17:22:01]</a>.

## Future of AI Video Generation
The speaker believes that 2024 is poised to be the year for mainstream [[Video segment generation and processing|video generation]], with a strong move towards AI-generated short films and movies <a class="yt-timestamp" data-t="11:08:01">[11:08:01]</a>. This trend is seen as just the beginning, with further advancements expected in audio and robotics related to AI <a class="yt-timestamp" data-t="11:18:01">[11:18:01]</a>. New models are frequently emerging, indicating rapid progress in the field <a class="yt-timestamp" data-t="20:36:01">[20:36:01]</a>.