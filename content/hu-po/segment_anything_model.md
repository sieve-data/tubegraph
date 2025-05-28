---
title: Segment Anything model
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

The Segment Anything Model (SAM) is a large [[Image segmentation techniques | segmentation]] model developed by Meta AI Research (formerly Facebook AI Research or Fair) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It has been pre-trained on a massive amount of data for an extended period, representing a type of research primarily undertaken by large AI companies <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Core Concepts

SAM aims to be a **foundation model for segmentation** <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
> [!INFO] What is a Foundation Model?
> A foundation model is typically a very large model trained on a very large dataset with a relatively generic, often self-supervised, task (e.g., filling in masks, next word prediction) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The intention is that these models can be fine-tuned for various downstream tasks, serving as a "foundation" for future models <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. While some argue that [[Image segmentation techniques | segmentation]] is already specific, SAM is designed to be highly adaptable within the [[Image segmentation techniques | segmentation]] domain <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

The project introduces a new task, model, and dataset for image [[Image segmentation techniques | segmentation]] <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Its design allows it to be **promptable**, enabling zero-shot transfer to new image tasks <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Key Components

SAM consists of three interconnected components:
1.  **A [[promptable_segmentation_task | promptable segmentation task]]** <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
2.  **A segmentation model** <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **A data engine** <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Model Architecture

The Segment Anything Model itself has three main parts <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>:
*   **Image Encoder**: This component takes an image and converts it into an image embedding <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. It is a minimally adapted Vision Transformer (ViT), and it's the largest part of the model, running once per image <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>, <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>.
*   **Prompt Encoder**: This component embeds the prompt, which can be spatial (points or boxes) or textual <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Points and boxes are represented by positional encodings, while masks are embedded using convolutions <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>, <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>. For text prompts, SAM uses the text encoder from CLIP to generate embeddings <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, <a class="yt-timestamp" data-t="01:39:04">[01:39:04]</a>.
*   **Mask Decoder**: This lightweight component combines the image embedding and prompt embedding to predict masks <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>. It employs a modification of a Transformer decoder block with prompt self-attention and cross-attention <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>. The decoder is designed to predict multiple masks from a single prompt (typically three) to handle ambiguity, along with a confidence score for each mask <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>, <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>. The mask decoder and prompt encoder are designed to run in amortized real-time (around 50 milliseconds in a web browser) <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## SA-1B Dataset

A significant contribution of the project is the **SA-1B dataset**, the largest segmentation dataset to date <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. It contains over 1 billion masks on 11 million licensed and privacy-respecting images <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, which is 400 times more masks than any existing [[Image segmentation techniques | segmentation]] dataset <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.

### Data Engine and Collection

The data was collected using a three-stage data engine, embodying a form of self-supervised or pseudo-labeling <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>:
1.  **Assisted Manual Annotation Stage**: SAM assists professional annotators in creating masks <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Annotators use interactive tools to refine masks <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. Initially, SAM was trained on public datasets like COCO before being retrained on newly annotated masks <a class="yt-timestamp" data-t="00:50:12">[00:50:12]</a>.
2.  **Semi-automatic Stage**: Annotators focus on less prominent objects not yet confidently detected by SAM. SAM automatically detects confident masks, and annotators fill in additional objects <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>.
3.  **Fully Automatic Stage**: SAM automatically generates masks for images. This stage utilizes a 32x32 grid of foreground points as prompts, yielding hundreds of high-quality masks per image on average <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>, <a class="yt-timestamp" data-t="00:56:23">[00:56:23]</a>. Techniques like non-maximum suppression (NMS) and processing multiple overlapping zoomed-in image crops are used to filter and improve mask quality <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>, <a class="yt-timestamp" data-t="00:57:16">[00:57:16]</a>. 99% of the masks in SA-1B were generated automatically <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.

The process involved retraining the model multiple times (six cycles in total), with each iteration leading to improved annotation speed and a higher number of masks per image <a class="yt-timestamp" data-t="00:53:17">[00:53:17]</a>, <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>. The dataset is notable for its diversity, including a greater percentage of small and medium-sized masks compared to older datasets <a class="yt-timestamp" data-t="01:03:38">[01:03:38]</a>.

## Performance and Applications

SAM demonstrates strong zero-shot transfer capabilities across numerous [[Image segmentation techniques | segmentation]] tasks <a class="yt-timestamp" data-t="00:53:36">[00:53:36]</a>, often performing competitively with or even superior to prior full-size models <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

It was evaluated on a diverse suite of 23 [[Image segmentation techniques | segmentation]] datasets, including novel image distributions like underwater, egocentric, X-ray, and biological images <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>. SAM's performance is particularly strong in:
*   **Edge detection** <a class="yt-timestamp" data-t="01:10:03">[01:10:03]</a>.
*   **Object proposal generation** <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>.
*   **Instance segmentation** <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>.
*   **Zero-shot text-to-mask segmentation** <a class="yt-timestamp" data-t="01:39:04">[01:39:04]</a>.

A notable feature is the ability to combine different prompt types, such as text and spatial points, to refine segmentation <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>. This flexibility makes SAM highly suitable for integration into larger algorithmic systems, similar to how CLIP is used in models like DALL-E <a class="yt-timestamp" data-t="01:32:27">[01:32:27]</a>. A key application area for Meta is in augmented reality (AR) and virtual reality (VR) headsets, where SAM could be prompted by gaze points from wearable devices to enable new interactive experiences <a class="yt-timestamp" data-t="01:43:55">[01:43:55]</a>, <a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a>.

## Limitations and Biases

While powerful, SAM is not perfect <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>. It can:
*   Hallucinate small, disconnected components <a class="yt-timestamp" data-t="01:49:38">[01:49:38]</a>.
*   Produce less "crisp" boundaries compared to dedicated interactive [[Image segmentation techniques | segmentation]] models <a class="yt-timestamp" data-t="01:49:39">[01:49:39]</a>.

The data collection process involved 130 annotators based in Kenya <a class="yt-timestamp" data-t="02:04:07">[02:04:07]</a>. The dataset exhibits common photographer biases, such as objects tending to be centered in images <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. The geographic distribution of images in SA-1B shows a higher percentage from Europe and Asia, with Russia and Thailand being the top two countries <a class="yt-timestamp" data-t="01:08:46">[01:08:46]</a>.

## Availability

The Segment Anything Model and the corresponding SA-1B dataset are released under an Apache 2.0 license, fostering further research in the field <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>, <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>. Checkpoints of the model are available in various sizes (e.g., 2GB, 1GB, 500MB) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The model is implemented in PyTorch and can be used in other deep learning frameworks via the ONNX (Open Neural Net Exchange) format <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

> [!NOTE] Comparison to Other Foundation Models
> SAM's status as a "foundation model" is debated. While it is large and trained on a massive dataset, its applicability is primarily within the realm of [[Image segmentation techniques | segmentation]] (albeit various types like instance, semantic, and panoptic segmentation) <a class="yt-timestamp" data-t="01:31:52">[01:31:52]</a>, <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>. In contrast, models like CLIP are considered more truly task-agnostic as they can be applied to any task involving text and images <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>, <a class="yt-timestamp" data-t="01:33:10">[01:33:10]</a>. Nonetheless, SAM's contribution to improving [[Image segmentation techniques | segmentation]] as a component in larger computer vision systems is significant <a class="yt-timestamp" data-t="01:52:57">[01:52:57]</a>.