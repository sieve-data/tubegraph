---
title: Promptbased learning and segmentation
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

The Segment Anything Model (SAM) is a significant development from Meta AI Research (formerly Facebook AI Research or Fair) [00:00:45](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=0m45s). It is a large [[Largescale image segmentation | segmentation model]] pre-trained on an extensive amount of data [00:01:15](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m15s). SAM is designed to perform zero-shot segmentation, meaning it can segment objects in images it has not specifically been trained on [00:01:26](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m26s).

## Core Concepts

### Foundation Models Defined
A foundation model is typically a very large model trained on an exceptionally large dataset using a relatively generic, often self-supervised, task [00:03:23](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=3m23s). Examples of generic tasks include filling in masks or next-word/token prediction [00:03:35](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=3m35s). The purpose of a foundation model is its ability to be fine-tuned for various downstream tasks, serving as a "foundation" for future models [00:03:47](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=3m47s).

While SAM aims to be a foundation model for segmentation, its task-specific nature makes its classification as a truly generic foundation model debatable compared to models like [[Contrastive learning and emergent properties | CLIP]] [00:32:08](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=32m8s).

### The Promptable Segmentation Task
The core idea behind SAM is a "promptable segmentation task," which requires the model to return a valid segmentation given any input prompt [00:11:54](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=11m54s). This prompt can be diverse, including:
*   **Spatial information:** Such as a mouse click, point coordinates, or a bounding box [00:12:12](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=12m12s).
*   **Text:** Natural language descriptions (e.g., "segment out the cat") [00:12:21](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=12m21s).
*   **Masks:** Rough pre-existing masks [02:00:06](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=2m6s).

The model is designed to provide reasonable masks even when a prompt is ambiguous or could refer to multiple objects [00:13:03](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=13m3s).

### SAM Model Architecture
SAM comprises three main components [00:13:52](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=13m52s):
1.  **Image Encoder:** A powerful Vision Transformer (ViT) that generates an image embedding [00:13:54](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=13m54s). This is the largest and most computationally intensive part, running once per image [00:38:32](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=38m32s).
2.  **Prompt Encoder:** Embeds the prompt (points, boxes, or text) [00:13:59](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=13m59s). Spatial prompts like points and boxes are encoded using positional encodings [00:39:03](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=39m3s). Text prompts are processed via [[Contrastive learning and emergent properties | CLIP]]'s text encoder [01:41:00](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m41s).
3.  **Mask Decoder:** A lightweight component that combines the image and prompt embeddings to predict a variety of masks with associated confidence scores (estimated IOU) [00:14:28](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=14m28s, [00:40:48](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=40m48s), [00:42:25](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=42m25s)). It uses a modified Transformer decoder block with self-attention and cross-attention mechanisms [00:40:56](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=40m56s).

### Efficiency and Ambiguity
The prompt encoder and mask decoder are designed to run in amortized real-time (around 50 milliseconds in a web browser demo context) [00:14:51](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=14m51s). SAM can predict multiple valid masks from a single prompt, often yielding three mask outputs to account for ambiguity [00:15:08](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=15m8s). The model uses a combination of focal loss and Dice loss for supervised mask prediction [00:43:51](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=43m51s).

## The SA-1B Dataset and Data Engine

### Scale and Licensing
A key contribution of the SAM project is the SA-1B dataset, currently the largest [[Largescale image segmentation | segmentation dataset]] available [00:05:06](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=5m6s). It contains over 1 billion masks on 11 million licensed and privacy-respecting images [00:05:10](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=5m10s). This is 400 times more masks than any existing [[Comparison of segmentation data sets | segmentation dataset]] [01:00:29](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m0s). The dataset and model are released under an Apache 2.0 license [02:09:01](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=2m9s).

### Data Collection Strategy
The SA-1B dataset was primarily collected using a novel "data engine" approach with three interconnected stages [00:04:27](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=4m27s, [00:16:37](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=16m37s):
1.  **Assisted Manual Annotation:** SAM assisted professional annotators (primarily based in Kenya) in drawing masks [00:16:43](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=16m43s, [02:04:09](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=2m4s). Annotators refined semi-automatic outputs using brush and eraser tools [01:48:12](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m48s). This process significantly reduced annotation time compared to traditional methods (e.g., from 34 seconds to 14 seconds per image) [00:53:17](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=53m17s).
2.  **Semi-Automatic Stage:** The model generated confident masks, and annotators focused on finding and labeling less prominent objects that the model initially missed [00:54:10](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=54m10s).
3.  **Fully Automatic Stage:** With sufficient data collected, the ambiguity-aware SAM model was used to automatically generate masks [00:56:05](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=56m5s). This involved prompting the model with a 32x32 regular grid of foreground points and selecting stable masks based on IOU prediction and non-maximum suppression (NMS) [00:56:23](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=56m23s, [00:57:04](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=57m4s). This stage generated the vast majority (99%) of the 1.1 billion masks [01:00:29](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1m0s). The model was iteratively retrained on newly collected data, scaling up its image encoder (from ViTB to ViTH) as more masks were gathered [00:50:01](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=50m1s, [00:54:01](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=54m1s).

### Dataset Properties and Quality
The SA-1B dataset exhibits key differences and high quality compared to existing datasets like Coco:
*   **Mask Quantity:** SA-1B has a significantly higher number of masks per image, with a large concentration between 51 and 200 masks per image [01:05:13](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h5m13s).
*   **Mask Size:** It includes a greater percentage of small and medium relative-sized masks, allowing for the segmentation of tiny objects alongside large ones [01:03:40](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h3m40s).
*   **Resolution:** Images in SA-1B are high-resolution, unlike the smaller resolutions of datasets like Coco (480x640) [01:00:01](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h0m1s).
*   **Quality Validation:** 94% of automatically generated masks had an IOU greater than 90% when compared to professionally corrected masks [01:01:16](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h1m16s).
*   **Spatial Distribution:** Like other human-curated datasets, SA-1B shows common photographer biases, such as an object-centric bias where main objects are typically centered in images [01:02:11](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h2m11s).

## Zero-Shot Capabilities and Applications

SAM is evaluated on its zero-shot transfer capabilities across a diverse suite of 23 segmentation datasets, including novel image distributions like underwater, egocentric, and X-ray images [01:15:22](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h15m22s).

### Diverse Transfer Tasks
While the paper claims SAM performs well on "significantly different" tasks [01:11:39](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h11m39s), these tasks generally remain within the realm of computer vision and [[Largescale image segmentation | image segmentation]]:
*   **Edge Detection:** SAM effectively generates reasonable edge maps, even though it wasn't specifically trained for this task [01:27:07](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h27m7s).
*   **Object Proposal Generation:** SAM shows strong performance on medium and large objects, as well as rare and common objects [01:31:43](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h31m43s).
*   **[[Largescale image segmentation | Instance Segmentation]]:** By feeding object detector bounding box outputs as prompts, SAM can function as a segmentation module within an instance segmenter pipeline [01:32:13](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h32m13s).
*   **Zero-Shot Text-to-Mask Segmentation:** SAM leverages [[Contrastive learning and emergent properties | CLIP]] embeddings to segment objects based on free-form text prompts [01:39:55](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h39m55s). A powerful feature is the ability to combine text prompts with spatial points (e.g., "wiper plus point") for more nuanced control [01:43:05](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h43m5s).

### Performance Benchmarks
SAM consistently outperforms prior interactive segmentors like SimpleClick, especially with a single prompt point [01:23:49](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h23m49s). In human studies, its mask quality ratings average between seven and nine (on a scale of one to ten) [01:26:01](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h26m1s).

### Real-World Applications
SAM's capabilities are particularly relevant for future applications in augmented reality (AR) and virtual reality (VR) [01:43:55](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h43m55s). For instance, a user wearing a VR headset could gaze at an object (providing a spatial point) and verbally request its segmentation (providing a text prompt), enabling interactive segmentation in real-time [01:43:55](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h43m55s). The model can also be composed into larger systems for tasks like 3D reproduction from a single RGB-D image [01:49:03](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h49m3s).

## Limitations and Future Directions
While powerful, SAM is not perfect. It can:
*   Hallucinate small disconnected components [01:49:38](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h49m38s).
*   Produce boundaries that are not always "crisp" [01:49:41](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h49m41s).
*   Fail to make a correct prediction, requiring additional prompts [01:42:52](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h42m52s).

Its foray into text-to-mask tasks is still exploratory and not entirely robust [01:50:31](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h50m31s). It is also unclear how to design simple prompts for semantic and panoptic segmentation [01:50:38](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h50m38s). Despite these limitations, SAM's ability to provide high-quality masks is expected to greatly benefit other computer vision pipelines, such as those used in Nerf papers, by improving the quality of their segmentation components [01:52:12](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h52m12s).

## Ethical Considerations
The paper includes a responsible AI analysis, noting the geographic distribution of images in SA-1B shows a higher percentage from Europe and Asia, with Russia and Thailand being the top two countries [01:08:00](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h8m0s). Measures were taken to blur sensitive information like faces and vehicle license plates [01:00:22](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h0m22s). The diversity of the dataset is intended to mitigate biases in performance across different perceived skin tones or age groups, an issue that has affected computer vision models in the past [01:09:07](https://www.youtube.com/watch?v=kYmG5IqxK3k&t=1h9m7s).