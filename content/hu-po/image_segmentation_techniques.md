---
title: Image segmentation techniques
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

Image segmentation is a fundamental task in computer vision, involving the division of a digital image into multiple segments (sets of pixels, also known as image objects) to simplify or change the representation of an image into something more meaningful and easier to analyze <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

## The Promptable Segmentation Task

A novel approach introduced by Meta AI Research defines a [[promptable_segmentation_task | promptable segmentation task]] <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>. This task requires a model to return a valid segmentation given any flexible prompt, such as points, boxes, text, or other information indicating what to segment <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. The goal is to provide a powerful generalization capability to future models <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Key requirements for this task include:
*   **Flexible prompts** The model must support various input types, including spatial (points, boxes) and text <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
*   **Real-time mask computation** Masks need to be computed in amortized real-time <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Ambiguity awareness** Even if a prompt is ambiguous, the model should return valid segmentation masks for at least one of the possible objects <a class="yt-timestamp" data-t="01:11:42">[01:11:42]</a>. It can predict multiple masks from a single prompt <a class="yt-timestamp" data-t="01:11:42">[01:11:42]</a>.

## The [[Segment Anything model | Segment Anything Model (SAM)]]

The [[Segment Anything model | Segment Anything Model]] (SAM) is a large segmentation model pre-trained on an extensive dataset <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Developed by Meta AI Research, it is designed for zero-shot generalization to new images and tasks <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

### Architecture
SAM consists of three main components <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a>:
1.  **Image Encoder:** A powerful [[transformer_architecture_in_image_processing | Vision Transformer]] (ViT) that generates an image embedding <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>. This encoder runs once per image and is the most computationally intensive part, typically taking the longest to perform inference <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>. It can be scaled to different sizes, such as ViT-B (91 million parameters) or ViT-H (636 million parameters) <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
2.  **Prompt Encoder:** Embeds various types of prompts <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>:
    *   **Sparse prompts** (points, boxes) are represented by positional encodings <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>.
    *   **Dense prompts** (masks) are embedded using convolutions <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.
    *   **Text prompts** are converted into visual tokens using models like [[feature_matching_in_computer_vision | CLIP]] <a class="yt-timestamp" data-t="00:44:40">[00:44:40]</a>.
3.  **Mask Decoder:** A lightweight component that combines the image embedding and prompt embedding to predict a mask <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>. This design employs a modification of a Transformer decoder block, using prompt self-attention and cross-attention mechanisms <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>. It can predict masks in around 50 milliseconds in a web browser <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. The mask decoder proposes a variety of masks with associated confidence scores <a class="yt-timestamp" data-t="00:37:17">[00:37:17]</a> and uses a dynamic linear classifier to predict foreground probability <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. It can output multiple valid masks (typically three) to handle ambiguous prompts <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.

### Training
SAM was trained using a combination of focal loss and dice loss, with a 20:1 ratio favoring focal loss <a class="yt-timestamp" data-t="01:59:03">[01:59:03]</a>. The training process utilized an AdamW optimizer, linear learning rate warm-up, and a decay schedule <a class="yt-timestamp" data-t="02:00:25">[02:00:25]</a>. Training was distributed across 256 GPUs, likely A100s, for an extended period <a class="yt-timestamp" data-t="02:00:59">[02:00:59]</a>.

## The SA-1B Dataset
SAM was trained on the SA-1B dataset, which comprises over 1 billion masks on 11 million licensed and privacy-respecting images <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This is considered the largest dataset for segmentation to date <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>.

### Data Engine
The SA-1B dataset was collected through a three-stage data engine, demonstrating a novel approach to self-supervised learning:
1.  **Assisted Manual Annotation Stage:** SAM assists professional annotators in creating masks <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. Annotators use tools like pixel-precise brush and eraser to refine model-generated masks <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>. The model was initially trained on common public datasets like COCO <a class="yt-timestamp" data-t="00:50:16">[00:50:16]</a>. As the model improved, annotation time decreased significantly (e.g., from 34 to 14 seconds per image) <a class="yt-timestamp" data-t="00:53:17">[00:53:17]</a>.
2.  **Semi-Automatic Stage:** Focuses on increasing the diversity of masks, with annotators labeling less prominent or challenging objects <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>.
3.  **Fully Automatic Stage:** With sufficient data and an ambiguity-aware model, mask generation becomes fully automatic <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. The model is prompted with a 32x32 rectangular grid of foreground points, predicting a set of masks for each point <a class="yt-timestamp" data-t="00:56:23">[00:56:23]</a>. Non-maximum suppression (NMS) is used to filter masks, and multiple overlapping zoomed-in image crops are processed to improve small mask quality <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. Approximately 99% of the masks in SA-1B were generated automatically <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.

### Data Characteristics
SA-1B exhibits diverse properties:
*   **Mask Density:** The dataset has a significantly higher number of masks per image compared to older datasets like COCO (e.g., commonly 51-200 masks per image versus fewer than 50 in COCO) <a class="yt-timestamp" data-t="01:04:54">[01:04:54]</a>.
*   **Mask Size:** It includes a greater percentage of small and medium-relative-size masks, indicating its ability to segment objects across various scales <a class="yt-timestamp" data-t="01:03:38">[01:03:38]</a>. This addresses a common [[challenges_in_visual_segmentation_and_encoding | challenge in segmentation]] <a class="yt-timestamp" data-t="02:11:15">[02:11:15]</a> where detecting small and large objects simultaneously is difficult <a class="yt-timestamp" data-t="02:11:15">[02:11:15]</a>.
*   **Geographic Distribution:** Efforts were made to ensure geographic diversity in the images to mitigate biases <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>.
*   **Quality:** 94% of automatically generated masks had an Intersection over Union (IOU) greater than 90% when compared to professionally corrected masks <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.

## Applications and Capabilities
SAM demonstrates strong zero-shot transfer capabilities across various tasks:

*   **General Segmentation:** It performs well in segmenting objects from single foreground points, consistently generating high-quality masks even with minimal input <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Edge Detection:** By prompting SAM with a regular grid of points and applying Sobel filtering to the generated masks, it can produce reasonable edge maps <a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>.
*   **Object Proposal Generation:** SAM can generate object proposals, outperforming some established methods on medium, large, and rare objects <a class="yt-timestamp" data-t="01:31:41">[01:31:41]</a>.
*   **Instance Segmentation:** By integrating with an object detector (e.g., using its bounding box outputs as prompts), SAM acts as a segmentation module for instance segmentation <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
*   **Text-to-Mask Segmentation:** SAM can segment objects from freeform text prompts by converting text into embeddings using CLIP's text encoder and comparing them to image embeddings <a class="yt-timestamp" data-t="01:40:43">[01:40:43]</a>. It also allows for combining text and spatial prompts (e.g., "wiper + point") for more nuanced control <a class="yt-timestamp" data-t="01:43:05">[01:43:05]</a>.

SAM's capabilities are particularly relevant for applications requiring real-time performance and rich spatial understanding, such as augmented reality (AR) and virtual reality (VR) headsets <a class="yt-timestamp" data-t="01:43:55">[01:43:55]</a>. Its architecture also facilitates its use as a component in larger computer vision systems, for example, in [[repurposing_diffusionbased_image_generators_for_depth_estimation | 3D reconstruction]] pipelines that require object masks <a class="yt-timestamp" data-t="01:51:55">[01:51:55]</a>.

## Limitations and Future Outlook
While powerful, SAM has limitations:
*   It may find structures, hallucinate small disconnected components, or produce boundaries that are not as crisp as specialized models <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>.
*   Its exploratory text-to-mask capabilities are not entirely robust <a class="yt-timestamp" data-t="01:50:31">[01:50:31]</a>.
*   It is unclear how to design simple prompts that implement semantic and panoptic segmentation <a class="yt-timestamp" data-t="01:50:38">[01:50:38]</a>.

The development of SAM and the SA-1B dataset represents an effort to push image segmentation into the era of "foundation models" <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. Whether SAM achieves the status of a true foundation model (i.e., a model adaptable to a wide range of *unrelated* downstream tasks, beyond just segmentation variants) remains to be seen <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>. However, its release aims to foster further research and development in this area <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.