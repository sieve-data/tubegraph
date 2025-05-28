---
title: Data handling for obscure image modalities
videoId: 9l9-2FbSccg
---

From: [[hu-po]] <br/> 

This article discusses the challenges and strategies involved in adapting machine learning models, specifically segmentation models, to work with obscure or unique data modalities that differ significantly from the data they were originally trained on.

## The Challenge of Obscure Modalities: The Scroll Prize Example

The **Scroll Prize** is a competition that utilizes a very unique and obscure data modality <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. Unlike standard cell phone images (three-channel RGB images with an object-centric bias) <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>, the Scroll Prize data consists of x-ray slices through a piece of an ancient scroll <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

While the fundamental task is still segmentation (outputting a binary segmentation mask) <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>, the visual nature of these x-rays makes it a very challenging problem <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. Key challenges include:
*   The obscure appearance of the images, making segmentation difficult <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   Uncertainty about how to process multiple slices (e.g., running the segmenter on every slice, on random tuples, or filtering slices) <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
*   Problems related to the actual data modality that require further investigation <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

## Strategy: The "Toy Problem" Approach

To address the complexities of the Scroll Prize data, a phased approach is adopted. The immediate strategy is to first fine-tune the **Segment Anything Model (SAM)** on a "toy problem" that more closely matches SAM's original training modality <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

This "toy problem" involves segmenting infrared images <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Segmenting these infrared images is considerably easier <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a> because:
*   They match the 3-channel RGB image modality that Segment Anything was trained on (even if grayscale, they can be converted to RGB) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   This allows for debugging and initial fine-tuning of the model on a simpler, more compatible dataset <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

Once the model performs well on this toy problem, the images will be switched to the x-ray data from the Scroll Prize to see if insights gained can be applied <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## Segment Anything Model (SAM) and its Components

The Segment Anything model, developed by Meta AI Research, is a segmentation foundation model <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. It consists of three main parts <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>:
1.  **Image Encoder**: Takes an image (or batch of images) and outputs them as embeddings <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. It converts 3-channel RGB images into 256-channel encoded images (64x64) <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
2.  **Prompt Encoder**: Takes permutations of masks, points, boxes, or text as input <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. For the Scroll Prize, points, masks, and potentially boxes are most relevant <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. The prompt encoder translates these prompts into a language the mask decoder can understand <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
3.  **Mask Decoder**: Listens to the prompt encoder and provides the actual segmentation masks <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. It takes sparse embeddings (from points/boxes) and dense embeddings (from masks) to output a low-resolution mask and an IOU (Intersection Over Union) prediction, which acts as a confidence score <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

SAM was trained iteratively using a supervised learning paradigm on existing datasets and then used for auto-labeling <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>. This modular training approach means fine-tuning does not necessarily involve tuning the entire model at once <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.

## Fine-tuning and Debugging

The fine-tuning process for SAM on new data involves adapting the training script. The loss function used for training SAM is a combination of focal loss and dice loss, with an IOU prediction head trained using mean squared error <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. For binary segmentation problems, a binary cross-entropy with logits loss is used <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.

Debugging the fine-tuning process involves identifying and resolving errors related to data dimensionality, data types (e.g., float32 vs. int32, numpy vs. tensor), and batching <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>. Challenges encountered include:
*   CUDA out-of-memory errors, necessitating switching to CPU for debugging and reducing batch size <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   Mismatching tensor dimensions between model components (e.g., image embeddings and dense prompt embeddings) <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   Incorrect data types for inputs (e.g., masks as `uint8` instead of float) <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   Incorrect point coordinates (normalized vs. pixel space) <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   Issues with batching and how the prompt encoder handles multiple inputs <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   Ensuring correct scaling of image pixel values (e.g., dividing by 255.0 to normalize) <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   Correct representation of point labels (e.g., red for outside mask, green for inside mask) <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

The point sampling method used for prompts (a simple grid) differs from the paper's more sophisticated approach (farthest from boundary, then farthest from error region) <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. Despite initial debugging challenges, the loss function showed a downward trend, indicating progress in the fine-tuning process <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.