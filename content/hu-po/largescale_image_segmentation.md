---
title: Largescale image segmentation
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

Largescale image segmentation involves training models on vast amounts of data to achieve robust and generalizable segmentation capabilities. A notable example is the "Segment Anything" (SAM) project by Meta AI Research, which introduces a new task, model, and dataset for image segmentation <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This project aims to build a foundation model for segmentation <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## The Segment Anything Model (SAM)

SAM is designed as a large segmentation model pre-trained on a massive amount of data over a long period, a type of research typically undertaken by major AI companies <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. It exhibits zero-shot transfer capabilities, meaning it can generalize to new image segmentation tasks without additional training <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Core Components
The model consists of three interconnected components <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>:
*   **Image Encoder:** A powerful vision transformer (ViT) that processes the input image once to create an image embedding <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a> <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. This is typically the largest and most memory-intensive part of the model <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. SAM uses pre-trained ViT models, specifically ViT-B (91 million parameters) and ViT-H (636 million parameters) <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a> <a class="yt-timestamp" data-t="01:45:47">[01:45:47]</a>.
*   **Prompt Encoder:** This component embeds various types of prompts, including sparse prompts (points, boxes) using positional encodings, and dense prompts (masks) using convolutions <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a> <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>. For text prompts, it leverages the text encoder from CLIP <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Mask Decoder:** A lightweight component that efficiently maps the image embedding and prompt embedding to output masks <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a> <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>. It predicts multiple masks and associated confidence scores for ambiguous prompts, using a modified transformer decoder block <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a> <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>. The mask decoder operates in amortized real-time, predicting a mask in approximately 50 milliseconds in a web browser <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a> <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.

### Promptable Segmentation Task
The [[promptbased_learning_and_segmentation | promptable segmentation task]] defines the model's objective: to return valid segmentations given any prompt <a class="yt-timestamp" data-t="00:11:54">[00:11:56]</a>. Prompts can be spatial (mouse clicks indicating points or bounding boxes) or textual (e.g., "segment out the cat") <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a> <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. Even when a prompt is ambiguous, the model is designed to return a reasonable mask <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

## The SA-1B Dataset

A key contribution of the Segment Anything project is the creation of the SA-1B dataset, the largest segmentation dataset to date <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Scale and Collection
The SA-1B dataset contains over 1 billion masks on 11 million licensed and privacy-respecting images <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. It is 400 times larger in terms of masks than any existing segmentation dataset <a class="yt-timestamp" data-t="01:00:36">[01:00:36]</a>.

The data collection process involved a "data engine" with three stages <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>:
1.  **Assisted Manual Annotation:** SAM assists professional annotators in creating masks, similar to interactive segmentation setups <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a> <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>. Annotators refined model-generated masks using brush and eraser tools <a class="yt-timestamp" data-t="01:01:01">[01:01:03]</a>.
2.  **Semi-Automatic Stage:** SAM automatically generates masks for a subset of objects by prompting itself with likely object locations <a class="yt-timestamp" data-t="00:17:59">[00:18:01]</a>. Annotators then focus on objects not confidently detected, increasing mask diversity <a class="yt-timestamp" data-t="00:54:10">[00:54:12]</a>.
3.  **Fully Automatic Stage:** The final stage uses a 32x32 regular grid of foreground points to prompt the model, yielding hundreds of high-quality masks per image <a class="yt-timestamp" data-t="00:18:16">[00:18:18]</a> <a class="yt-timestamp" data-t="00:56:23">[00:56:25]</a>. Techniques like non-maximum suppression (NMS) are used to filter overlapping masks <a class="yt-timestamp" data-t="00:57:04">[00:57:06]</a>. To improve quality for smaller masks, the model processes multiple overlapping, zoomed-in image crops <a class="yt-timestamp" data-t="01:17:19">[01:17:21]</a>.

This iterative process of model-assisted data collection and retraining is a form of [[selfsupervised_learning_for_images | self-supervised learning]] or pseudo-labeling <a class="yt-timestamp" data-t="00:11:04">[00:11:07]</a> <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. SAM was retrained six times during this loop <a class="yt-timestamp" data-t="00:54:01">[00:54:04]</a>.

### Quality and Diversity
The automatically generated masks in SA-1B are of high quality, with 94% having an Intersection Over Union (IOU) greater than 90% when compared to professionally corrected masks <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>. The dataset also includes a greater percentage of small and medium-sized masks compared to older datasets like COCO, and features more masks per image <a class="yt-timestamp" data-t="01:03:38">[01:03:40]</a> <a class="yt-timestamp" data-t="01:05:13">[01:05:13]</a>. The images in SA-1B come from a diverse set of geographies, ensuring a broader distribution of data <a class="yt-timestamp" data-t="01:08:46">[01:08:48]</a>.

## Performance and Zero-Shot Transfer

SAM's capabilities are evaluated across numerous tasks, often performing competitively with or even superior to prior full-size models in zero-shot settings <a class="yt-timestamp" data-t="00:05:36">[00:05:38]</a>.

### Evaluation Tasks
SAM was evaluated on a suite of 23 diverse segmentation datasets, including novel image distributions like underwater, egocentric, X-ray, and biological images <a class="yt-timestamp" data-t="01:15:22">[01:15:25]</a> <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>. The tasks included:
*   **Edge Detection:** SAM, although not trained for this task, produces reasonable edge maps <a class="yt-timestamp" data-t="01:27:07">[01:27:09]</a>.
*   **Object Proposal Generation:** The model performs well on this mid-level task <a class="yt-timestamp" data-t="01:29:22">[01:29:24]</a>.
*   **Instance Segmentation:** SAM can be used as a segmentation module within an instance segmenter, by taking bounding box outputs from an object detector as prompts <a class="yt-timestamp" data-t="01:32:11">[01:32:13]</a> <a class="yt-timestamp" data-t="01:32:17">[01:32:19]</a>.
*   **Text-to-Mask Segmentation:** SAM can segment objects from freeform text prompts by using CLIP embeddings to represent the text <a class="yt-timestamp" data-t="01:38:54">[01:38:56]</a> <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. It also supports combining text prompts with spatial prompts for nuanced results <a class="yt-timestamp" data-t="01:43:05">[01:43:09]</a>.

### Limitations
While powerful, SAM is not perfect. It can hallucinate small, disconnected components and may not always produce boundaries as crisply as dedicated interactive segmentation models <a class="yt-timestamp" data-t="01:49:35">[01:49:36]</a>. Its text-to-mask capability is still exploratory and not entirely robust <a class="yt-timestamp" data-t="01:50:31">[01:50:33]</a>.

## Implications and Future Directions

The Segment Anything project represents a significant step towards bringing image segmentation into the era of [[large_language_models_llms_and_scaling | large language models (LLMs) and scaling]] and foundation models <a class="yt-timestamp" data-t="01:50:49">[01:50:52]</a>.

SAM's open-source release, including its model and dataset, is intended to foster research and potentially replace older datasets like COCO <a class="yt-timestamp" data-t="00:26:26">[00:26:28]</a>. The model binaries (checkpoints) are available in ONNX format, allowing use across different deep learning frameworks <a class="yt-timestamp" data-t="00:02:26">[00:02:27]</a>.

The model's design aligns with the concept of "tool former" models, where [[large_language_models_llms_and_scaling | Large Language Models (LLMs) and scaling]] can leverage specialized tools like SAM for specific tasks <a class="yt-timestamp" data-t="00:35:05">[00:35:08]</a>. For example, a larger system could use SAM to segment an object of interest for [[3d_surface_reconstruction_from_rgb_images | 3D surface reconstruction from RGB images]] <a class="yt-timestamp" data-t="01:49:03">[01:49:09]</a>. Its real-time performance and ability to respond to gaze points from wearable devices point towards applications in augmented reality and virtual reality, aligning with Meta's broader vision for the metaverse <a class="yt-timestamp" data-t="01:43:55">[01:43:57]</a> <a class="yt-timestamp" data-t="01:49:20">[01:49:25]</a>.

Despite its advancements, there is ongoing debate about whether SAM qualifies as a true "foundation model" given its specialized focus on segmentation, unlike more general models like CLIP that can handle diverse text-image alignment tasks <a class="yt-timestamp" data-t="01:46:43">[01:46:45]</a> <a class="yt-timestamp" data-t="01:47:31">[01:47:31]</a>. Nevertheless, [[metas_open_source_segmentation_models | Meta's Open Source Segmentation Models]] like SAM are expected to become a valuable component in future computer vision pipelines, improving overall system performance where accurate segmentation masks are required <a class="yt-timestamp" data-t="01:52:43">[01:52:46]</a>.