---
title: Scroll Prize competition
videoId: 9l9-2FbSccg
---

From: [[hu-po]] <br/> 

## Overview

The Scroll Prize is a competition that involves a unique and somewhat obscure data modality <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The primary objective of the competition is segmentation, specifically to take input images and output a segmentation map or a binary segmentation mask <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. For this competition, researchers are fine-tuning the [[Promptbased learning and segmentation | Segment Anything]] model, a segmentation foundation model developed by Meta AI Research <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. A version of the Scroll Prize training script has been adapted to utilize the [[Promptbased learning and segmentation | Segment Anything]] model <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Unique Data Modality

The Scroll Prize dataset consists of unusual x-ray images <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. These are slices taken through a piece of an ancient scroll <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This differs significantly from the data [[Promptbased learning and segmentation | Segment Anything]] was originally trained on, which primarily comprised object-centric, 3-channel RGB cell phone images <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Challenges

The Scroll Prize presents several challenges:
*   **Visual Complexity:** The x-ray images are difficult to interpret visually, not resembling typical objects <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Processing Strategy:** It is unclear how to best process the 65 different slices available for each scroll <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Questions remain regarding whether to run the segmenter on every slice, on random tuples of slices, or apply filtering <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Fine-Tuning the [[Promptbased learning and segmentation | Segment Anything]] Model

The [[Promptbased learning and segmentation | Segment Anything]] model has three main components <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>:
1.  **Image Encoder:** Takes a batch of images and outputs them as 256-channel encoded images (64x64 resolution) <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
2.  **Prompt Encoder:** Receives permutations of masks, points, boxes, or text as input <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For the Scroll Prize, points, masks, and potentially boxes are most relevant <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. The prompt encoder translates these inputs into a language the mask decoder can understand <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  **Mask Decoder:** Takes embeddings from the prompt encoder (sparse for points/boxes/text, dense for masks) and uses them to generate actual masks, including a low-resolution mask and an IOU prediction (confidence score) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The training of the [[Promptbased learning and segmentation | Segment Anything]] model is iterative, initially using a supervised learning paradigm on existing datasets and then auto-labeling <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Fine-tuning also follows a similar approach, not training the entire model simultaneously <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

The loss function used for training is a combination of focal loss and Dice loss <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Additionally, an IOU prediction head is trained with mean squared error between the predicted IOU and the IOU of the predicted masks <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The current implementation uses a combined loss, including an MSE loss for IOU prediction and a binary cross-entropy with logits loss for the binary segmentation mask output <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Initial "Toy Problem" Approach

Given the difficulty of the scroll x-ray images, the team is initially focusing on a simpler "toy problem" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This involves segmenting infrared images, which closely match the 3-channel RGB (or grayscale convertible to RGB) modality used by the [[Promptbased learning and segmentation | Segment Anything]] model <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The strategy is to successfully fine-tune the model on this easier problem before attempting the more challenging x-ray images <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Development and Debugging

The development process involves extensive debugging to resolve issues related to tensor dimensions, data types, and CUDA memory limitations <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Debugging on CPU is preferred during streaming to prevent system freezes <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. A key strategy for debugging batch dimensions is to use unusual batch sizes (e.g., 3, 5, or 7) to make it more obvious if dimensions are incorrect <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

The point sampling method used for input is currently a grid, which differs from the paper's more sophisticated point sampling technique that chooses points deterministically based on distance from object boundaries and error regions <a class="yt-timestamp" data-t="01:59:49">[01:59:49]</a>.

## Resources

All the code for this project is available on a public repository called `hoopo Ashen Venus` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It is under an MIT license, allowing for adaptation and use <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.