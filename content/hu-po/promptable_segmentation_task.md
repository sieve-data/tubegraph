---
title: Promptable segmentation task
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

The "promptable segmentation task" is a novel concept introduced as a core component of the [[segment_anything_model | Segment Anything Model]] (SAM) developed by Meta AI Research [00:04:57]. Its primary goal is to return valid segmentations based on various types of prompts [00:11:56]. This task aims to enable powerful generalization and allow SAM to transfer zero-shot to new [[Image segmentation techniques | image segmentation]] tasks [00:09:42], moving towards the development of a foundation model for segmentation [00:11:11].

## Key Characteristics

### Flexible Prompting
A fundamental requirement of the promptable segmentation task is its support for flexible prompts [00:10:41]. This allows users to specify what to segment using diverse inputs:
*   **Spatial Prompts**: These include points (e.g., mouse clicks at specific positions in an image), rough bounding boxes, or existing masks [00:12:10]. The use of spatial information as a prompt is a significant modification to traditional segmentation problems [00:12:48]. Points and boxes are represented by positional encodings within the model [00:39:05].
*   **Text Prompts**: Handcrafted text can also be used, enabling zero-shot generalization to novel visual concepts [00:08:25]. SAM leverages Clip's text encoder to process these text prompts [01:41:10].
*   **Combined Prompts**: The model can also combine text prompts with spatial prompts, such as a text description along with a point [01:43:13].

### Ambiguity Awareness
The task requires the model to return a reasonable mask even when a prompt is ambiguous and could refer to multiple objects [00:13:02]. SAM is designed to predict multiple masks from a single prompt, making it ambiguity-aware [00:15:10]. It typically outputs three masks, which is found to be sufficient for most common cases [01:42:13].

### Real-time Performance
The model is designed to compute masks in "amortized real-time" [00:13:32]. The prompt encoder and mask decoder components of SAM can predict a mask in approximately 50 milliseconds in a web browser, after the initial image embedding has been pre-computed by the image encoder [00:14:51]. This low latency for the prompt-dependent parts is crucial for interactive applications [00:43:02].

## Components of the Promptable Segmentation Task within SAM

The [[segment_anything_model | Segment Anything Model]] (SAM) architecture, designed to perform the promptable segmentation task, consists of three main components [00:13:50]:

1.  **Image Encoder**: This powerful component embeds the input image [00:13:54]. It is typically a Vision Transformer (ViT) [00:38:03], minimally adapted [00:38:15]. This encoder runs once per image and can be applied prior to prompting the model [00:38:28]. It is the largest and most memory-intensive part of the model [00:43:10].
2.  **Prompt Encoder**: This component embeds the diverse prompts, whether they are sparse (points, boxes, text) or dense (masks) [00:14:01]. Sparse prompts (points and boxes) are represented by positional encodings, while dense prompts (masks) are embedded using convolutions [00:39:03].
3.  **Mask Decoder**: This lightweight component efficiently maps the image embedding and prompt embedding to an output mask [00:14:28]. It employs a modification of a Transformer decoder block, using prompt self-attention and cross-attention [00:40:56]. The mask decoder proposes a variety of masks with a confidence score for each [00:37:15]. It uses a binary classification approach to classify pixels as either foreground or background [00:41:57]. The loss function used for training is a combination of focal loss and Dice loss [00:59:03].

## Pre-training Objective and Data Engine

The promptable segmentation task suggests a natural pre-training algorithm that simulates various prompts for each training sample and compares the model's output mask against a "ground truth" (or pseudo-ground truth) [00:26:45]. This process adapts methods from interactive segmentation, aiming to always predict a valid mask for any given prompt [00:27:03].

The development of SAM and its promptable segmentation task was powered by a "data engine" that collected an unprecedented dataset of over 1 billion masks on 11 million licensed, privacy-respecting images [00:04:38]. This data engine operated in three stages [00:37:05]:

1.  **Assisted Manual Annotation**: SAM assisted annotators in labeling masks, making the process more efficient than traditional interactive segmentation [00:45:42].
2.  **Semi-automatic Annotation**: In this stage, SAM automatically generated masks for a subset of objects by prompting itself with likely object locations [00:46:03]. Annotators focused on less prominent objects to increase diversity [00:54:19].
3.  **Fully Automatic Annotation**: The final stage involved Sam prompting itself with a regular grid of foreground points (e.g., 32x32), yielding on average 100 high-quality masks per image [00:18:16]. Techniques like non-maximum suppression (NMS) were used to filter overlapping masks [00:57:04], and processing multiple overlapping zoomed-in image crops further improved quality, especially for smaller masks [00:57:16].

This iterative process allowed the model to improve and generate more masks in each subsequent stage, demonstrating a "self-supervised" approach where the model helps create its own training data [00:50:16].

## Zero-Shot Generalization and Downstream Tasks

The promptable segmentation task enables zero-shot generalization to numerous downstream tasks [00:53:36]. SAM's capability to respond to any prompt means it can act as a component in a larger algorithmic system [00:31:24], similar to how [[Segment Anything model | Clip]] is used within models like DALL-E [00:32:29].

SAM has been evaluated on various tasks that differ significantly from the promptable segmentation task, including [01:10:00]:
*   Edge detection [01:11:06]
*   Object proposal generation [01:11:06]
*   Instance segmentation [01:11:06]
*   Text-based segmentation [01:11:15]

While these tasks are all variants of segmentation, their differences in input and output formats test the model's ability to generalize. For example, in instance segmentation, an existing object detector's bounding box output can be provided as a prompt to SAM, which then segments the object within that box [01:32:13]. The model's performance on these diverse tasks, even those involving novel image distributions (e.g., underwater, egocentric, X-ray images, satellite imagery), showcases its strong zero-shot transfer capabilities [01:15:28].

## Foundation Model Status

The authors of SAM pose the question of whether it achieves the status of a "foundation model" [01:51:06]. While SAM is a very large model trained on a massive dataset for a long time, fitting the definition of a foundation model as a large model trained on a large dataset for a generic task [00:31:15], its primary utility remains within the realm of segmentation [01:46:47]. The debate centers on whether a model must be adaptable to a wide range of *unrelated* downstream tasks (like [[Segment Anything model | Clip]] with text-image alignment) or simply be very large and trained on vast data for a broadly applicable task (like segmentation). SAM's strong performance in segmentation tasks positions it as a significant advancement within [[Image segmentation techniques | image segmentation techniques]] [01:52:50].