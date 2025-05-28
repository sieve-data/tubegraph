---
title: Foundation models in AI
videoId: eMFfMz9uYlc
---

From: [[hu-po]] <br/> 

Foundation models represent a significant paradigm shift in artificial intelligence, drawing inspiration from advancements in [[Natural Language Processing | NLP]] <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>. The concept of a foundation model, a term thought to originate from Stanford <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, involves training a very large model on an extensive dataset with a relatively generic task <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Core Characteristics

### Scale and Training
A primary characteristic of foundation models is their immense scale <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. They are very large models trained on very large datasets for extended periods <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This type of research is typically only feasible for major AI companies due to the significant computational resources required, such as numerous A100 GPUs <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a><a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Empirical trends indicate that model scale, dataset size, and total training time lead to improved performance <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a><a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Generic Tasks and Self-Supervision
Foundation models are often trained on generic, [[SelfImprovement in AI Models | self-supervised learning | self-supervised]] tasks <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, such as:
*   Filling in masks <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>
*   Next-word or next-token prediction <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a><a class="yt-timestamp" data-t="02:51:18">[02:51:18]</a>
For images, this can involve cutting out a chunk and asking the model to generate the missing piece, creating an infinite [[SelfImprovement in AI Models | self-supervised]] task <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The self-supervised nature of these tasks allows for training on vast amounts of unlabeled data <a class="yt-timestamp" data-t="02:52:27">[02:52:27]</a><a class="yt-timestamp" data-t="02:52:51">[02:52:51]</a>.

### Generalization and Promptability
A key advantage of foundation models is their ability to generalize to tasks beyond those seen during initial training <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This capability is often implemented through prompt engineering <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. When scaled and trained with abundant data, these models perform surprisingly well in zero-shot and few-shot scenarios compared to fine-tuning models <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Role in AI Research and Development

### Pushing State of the Art
The development of foundation models, particularly in [[Natural Language Processing | NLP]], has revolutionized the field by leveraging web-scale datasets <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. In computer vision, prominent illustrations include aligned text and images models like [[Meta AI research | CLIP]] <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a><a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Once trained, [[Meta AI research | CLIP]] encoders enable zero-shot generalization to novel visual concepts through text prompts and can compose effectively with other modules for downstream tasks like image retrieval <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

The "power laws" in machine learning are real, indicating that larger models trained on larger datasets tend to yield better results than smaller, fully supervised datasets <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a><a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Data Engine and [[Data Generation for AI Models | Self-Improvement in AI Models]]
Some foundation models employ a "data engine" approach, which iterates through stages to collect and refine massive datasets <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a><a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This can involve:
1.  **Assisted Manual Annotation**: A model assists human annotators, making the process faster <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. Modern annotation often involves correcting model-generated pseudo-labels rather than drawing from scratch <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
2.  **Semi-Automatic Stage**: The model can automatically generate masks for subsets of objects using likely object locations <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
3.  **Fully Automatic Stage**: The model prompts itself (e.g., with a regular grid of foreground points) to generate masks, then uses techniques like non-maximum suppression (NMS) to filter them <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a><a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. This process can significantly increase the number of masks per image <a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>.

This iterative process of using a model to generate data, which is then used to retrain and improve the model, is a form of [[SelfImprovement in AI Models | self-supervised learning]] or pseudo-labeling <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a><a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>. An example of this is the [[Meta AI research | Alpaca]] model, which was fine-tuned on a dataset generated by [[Structured chain of thought in AI models | GPT]] <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>.

## Case Study: Segment Anything Model (SAM)

The Segment Anything Model (SAM), developed by [[Meta AI research | Meta AI research]] (formerly Facebook AI Research or FAIR) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, is a large segmentation model pre-trained on a massive amount of data <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Architecture
SAM has three interconnected components <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>:
1.  **Image Encoder**: A powerful [[Platonic representation in AI models | Vision Transformer]] <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a> that runs once per image <a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>. This is typically the largest part of the model and takes the most memory <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>.
2.  **Prompt Encoder**: Embeds user prompts, which can be:
    *   **Spatial**: Points (e.g., mouse clicks) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a> or bounding boxes <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. These are represented using positional encodings <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.
    *   **Text**: Natural language descriptions <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>, often embedded using [[Meta AI research | CLIP]]'s text encoder <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>.
3.  **Mask Decoder**: A lightweight component <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a> that combines the image embedding and prompt embedding to predict masks in near real-time (around 50 milliseconds in a web browser) <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. It employs a modified Transformer decoder block <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a> and can predict multiple masks with confidence scores <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

### Dataset: SA-1B
SAM's strength comes from its training on the SA-1B dataset, which consists of over 1 billion masks on 11 million licensed, privacy-respecting images <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a><a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This is significantly larger than previous datasets like COCO, with 400 times more masks <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. The dataset includes high-resolution images, with faces and license plates blurred for privacy <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a><a class="yt-timestamp" data-t="01:00:22">[01:00:22]</a>. Ninety-nine percent of these masks were generated automatically <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.

### Performance and Generalization
SAM is designed to transfer zero-shot to new image segmentation tasks <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Its zero-shot performance is often competitive with or even superior to prior full-size results <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It excels at detecting both large and small objects within the same image <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a> and can segment a large number of individual objects <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

SAM has been evaluated on 23 diverse segmentation datasets, including underwater, egocentric, x-ray, and even oil painting images <a class="yt-timestamp" data-t="01:15:23">[01:15:23]</a>. It performs well on tasks such as:
*   Edge detection <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a>
*   Object proposal generation <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>
*   Instance segmentation <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>
*   Text-to-mask prediction <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>

The model can also combine prompts, allowing users to specify an object via text and refine it with a point <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>.

## Debating the "Foundation Model" Label

While SAM is a very large model trained on an enormous dataset, there's a debate about whether it truly qualifies as a "foundation model" in the broadest sense:

*   **Argument for**: If a foundation model is defined by its massive scale and training on vast data for a long duration, then SAM fits this definition <a class="yt-timestamp" data-t="01:47:11">[01:47:11]</a>. It pushes the boundaries of data size for segmentation <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Argument against**: If a foundation model is defined by its general-purpose applicability to a wide range of downstream tasks, then SAM may be too specialized. It is primarily a segmentation model, albeit capable of different *types* of segmentation tasks <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a><a class="yt-timestamp" data-t="01:47:22">[01:47:22]</a>. Other models like [[Meta AI research | CLIP]] are considered more task-agnostic <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

> [01:46:56] "Are our foundation models Foundation models because they're adaptable to a wide range of Downstream tasks or are they really Foundation models because they're trained on a big data set so I think that if your definition of foundation model is that it it's a huge model trained on a huge amount of data for a huge amount of time then yes Sam is a foundation model if your definition of foundation models is a general purpose model that can be used for a huge amount of Downstream applications then no I do not think Sam is a foundation model."

## [[Future directions and potential breakthroughs in AI models | Future Directions and Potential Breakthroughs]]

Foundation models like SAM are seen as components in larger AI systems, analogous to how [[Meta AI research | CLIP]] is used within models like [[Structured chain of thought in AI models | DALL-E]] <a class="yt-timestamp" data-t="01:48:53">[01:48:53]</a>. In a "toolformer" world, where large language models are enabled to use external tools <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>, a powerful segmentation model like SAM becomes a valuable resource for other AI systems <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

For [[Meta AI research | Meta]], SAM's real-time performance and ability to respond to spatial and text prompts align with potential applications in virtual and augmented reality (VR/AR) headsets, where users might gaze at an object and segment it using a verbal command <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a><a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a>.

The widespread availability of SAM under an [[Open Source vs Proprietary AI Models | Apache license]] <a class="yt-timestamp" data-t="02:09:44">[02:09:44]</a> is expected to [[future_directions_and_potential_breakthroughs_in_ai_models | foster further research]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a> and development of new foundation models <a class="yt-timestamp" data-t="01:59:29">[01:59:29]</a>.