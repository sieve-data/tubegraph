---
title: deep learning algorithms for feature matching
videoId: LBFiKtUBHc0
---

From: [[hu-po]] <br/> 

[[feature_matching_in_computer_vision | Feature matching]] is a classic and crucial problem in [[Computer_vision_deep_dive | computer vision]] <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. It involves identifying correspondences between two images of the same subject <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This means finding points in one image that correspond to points in another, creating matching pairs across multiple images <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Importance of Feature Matching

Once correspondences are found, it's possible to perform geometric calculations, like triangle camera math, to determine the position of cameras and points, enabling the creation of 3D reconstructions from 2D images <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

[[feature_matching_in_computer_vision | Feature matching]] is fundamental to many [[Computer_vision_deep_dive | computer vision]] applications, including:
*   **VR Headsets:** Devices like the Quest 3 use [[feature_matching_in_computer_vision | feature matching]] for Simultaneous Localization and Mapping (SLAM), simultaneously building a 3D map of the environment and localizing itself within it <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="01:21:36">[01:21:36]</a>.
*   **Gaussian Splats:** To create a Gaussian Splat from a series of images, the first step involves an algorithm called COLMAP, which has a [[feature_matching_in_computer_vision | feature matching]] component <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Robotics:** Robots build their own maps for navigation, often relying on SLAM, which incorporates [[feature_matching_in_computer_vision | feature matching]] <a class="yt-timestamp" data-t="01:24:48">[01:24:48]</a>, <a class="yt-timestamp" data-t="01:29:53">[01:29:53]</a>.

## Evolution of Feature Matching Algorithms

Historically, [[feature_matching_in_computer_vision | feature matching]] relied on hand-designed features, a practice sometimes referred to as "computer vision archaeology" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>, <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### SIFT: The Hand-Designed Era
Scale-Invariant Feature Transform (SIFT) is an example of a hand-designed feature <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. SIFT uses gradients (changes in image brightness) in local regions to create a feature vector, which can then be matched across different images <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>, <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   COLMAP, used for Gaussian Splats, still relies on SIFT features <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Other hand-designed features include ORB, BRIEF, SURF, and HOG <a class="yt-timestamp" data-t="02:28:25">[02:28:25]</a>.

### Transition to [[Deep_Learning_and_Neural_Networks | Deep Learning]]
The field has largely moved from hand-designed features to learned features, where [[Deep_Learning_and_Neural_Networks | deep learning]] models (often [[Deep_Learning_and_Neural_Networks | neural networks]] like vision Transformers) learn low-level features that become semantically meaningful <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This means the computer determines what features to use, rather than a human <a class="yt-timestamp" data-t="02:28:51">[02:28:51]</a>, <a class="yt-timestamp" data-t="02:29:54">[02:29:54]</a>.

### SuperGlue: A [[Deep_Learning_and_Neural_Networks | Deep Learning]] Predecessor
SuperGlue, an earlier [[Deep_Learning_and_Neural_Networks | deep learning]] approach by Magic Leap, introduced a paradigm where a [[Deep_Learning_and_Neural_Networks | deep network]] simultaneously considers two images to match sparse points and reject outliers <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>, <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>.
*   **Architecture:** SuperGlue used Convolutional Neural Networks (ConVNets) and Graph Neural Networks (GNNs) <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>, <a class="yt-timestamp" data-t="01:10:03">[01:10:03]</a>.
*   **Limitations:**
    *   **Computational Expense:** SuperGlue was computationally expensive, requiring significant compute resources to train <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.
    *   **Complexity:** Its complexity grew quadratically with the number of key points due to its Transformer-based architecture and self-attention mechanism <a class="yt-timestamp" data-t="01:18:45">[01:18:45]</a>, <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>.
    *   **Training:** It could only make predictions and be supervised at its very last layer, hindering training speed and convergence <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>, <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a>.
    *   **Positional Encoding:** It used an MLP to encode absolute point positions, which were fused early with descriptors <a class="yt-timestamp" data-t="01:20:35">[01:20:35]</a>, <a class="yt-timestamp" data-t="01:21:11">[01:21:11]</a>.

## LightGlue: A Modern Approach

LightGlue is a modern [[Deep_Learning_and_Neural_Networks | deep learning]]-based approach to [[feature_matching_in_computer_vision | feature matching]], building upon SuperGlue but incorporating more recent innovations in Transformers from 2023 <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>. It is developed by Microsoft Mixed Reality and AI Lab (HoloLens team) <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Key Improvements and Design Decisions
LightGlue re-evaluates SuperGlue's design to make it more efficient in terms of memory and computation, crucial for deployment on devices like VR headsets <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>, <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>.

1.  **Transformer Architecture:** LightGlue uses a Transformer architecture for its core processing <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   It consists of a stack of identical layers, each with a self-attention and cross-attention unit <a class="yt-timestamp" data-t="01:28:45">[01:28:45]</a>, <a class="yt-timestamp" data-t="01:34:45">[01:34:45]</a>.
    *   Self-attention operates within a single image, while cross-attention pulls information from the other image <a class="yt-timestamp" data-t="01:38:51">[01:38:51]</a>, <a class="yt-timestamp" data-t="01:39:03">[01:39:03]</a>.
2.  **Adaptive Computation (Depth & Width):**
    *   **Early Halting:** LightGlue can adapt to the difficulty of image pairs. If an image pair is "easy" (e.g., large visual overlap, limited appearance change), the model can halt inference earlier, avoiding unnecessary computation <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>, <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
    *   **Confidence Classifier:** A small, lightweight classifier within each layer determines whether to prune points that are confidently unmatchable <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>, <a class="yt-timestamp" data-t="01:03:22">[01:03:22]</a>. This continuously reduces the number of points in subsequent layers, saving memory and computation due to the quadratic complexity of attention <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>, <a class="yt-timestamp" data-t="01:04:03">[01:04:03]</a>, <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>, <a class="yt-timestamp" data-t="01:41:43">[01:41:43]</a>.
3.  **Rotary Positional Encoding (RoPE):**
    *   LightGlue uses Rotary Positional Encodings to incorporate positional information <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, <a class="yt-timestamp" data-t="01:52:54">[01:52:54]</a>.
    *   RoPE emphasizes the *relative* position between points, which is more critical for [[feature_matching_in_computer_vision | feature matching]] than absolute position, especially given camera geometry <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>, <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>, <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>, <a class="yt-timestamp" data-t="01:37:32">[01:37:32]</a>, <a class="yt-timestamp" data-t="01:42:26">[01:42:26]</a>.
    *   Unlike traditional sinusoidal embeddings that are added, RoPE applies rotations to the query and key vectors themselves <a class="yt-timestamp" data-t="00:44:17">[00:44:17]</a>, <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.
    *   Positional encoding is only applied during self-attention, not cross-attention <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.
    *   The positional encodings can be pre-computed and cached as they are identical across layers <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>, <a class="yt-timestamp" data-t="01:46:25">[01:46:25]</a>.
4.  **Disentangled Similarity and Matchability:** LightGlue separates the prediction of similarity (how alike two points are) and matchability (the likelihood of a point having a correspondence) <a class="yt-timestamp" data-t="01:21:40">[01:21:40]</a>, <a class="yt-timestamp" data-t="01:22:21">[01:22:21]</a>.
5.  **Multi-Layer Supervision:** LightGlue computes and supervises assignments at *every* layer, enabling cleaner gradients and faster convergence compared to SuperGlue, which only supervised at the last layer <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>, <a class="yt-timestamp" data-t="01:24:14">[01:24:14]</a>, <a class="yt-timestamp" data-t="01:38:45">[01:38:45]</a>.

> [!WARNING] Hyperparameter Dependency
> LightGlue utilizes hardcoded thresholds for pruning points at each layer, with a specific decay rate per layer <a class="yt-timestamp" data-t="01:12:15">[01:12:15]</a>. These thresholds are tuned based on validation accuracy, making them specific to the training data. This reliance on data-specific hyperparameters could limit generalization to different environments <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>, <a class="yt-timestamp" data-t="01:24:50">[01:24:50]</a>.

## Training LightGlue
LightGlue's training involves two main stages:
1.  **Pre-training:** The model is pre-trained using [[synthetic_data_in_feature_detection | synthetic data]] composed of homographies <a class="yt-timestamp" data-t="01:24:32">[01:24:32]</a>. These homographies are sampled from a million images, including those from datasets like MegaDepth (tourism landmarks) <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>, <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>. This pre-training is crucial for generalization and prevents overfitting to distinctive scenes <a class="yt-timestamp" data-t="01:25:30">[01:25:30]</a>.
2.  **Confidence Classifier Training:** The confidence classifier, which prunes points, is trained separately after the main model <a class="yt-timestamp" data-t="01:16:31">[01:16:31]</a>.

The training uses fully supervised learning. Ground truth labels for correspondences are estimated from two-view transformations (like homographies or pixel-wise depth and relative pose) <a class="yt-timestamp" data-t="01:17:47">[01:17:47]</a>. Points with large reprojection or depth errors are labeled as unmatchable <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.

## Performance and Limitations
LightGlue is generally faster than SuperGlue, achieving about four times the speed (e.g., 26.1 pairs per second vs. 6.5 pairs per second) <a class="yt-timestamp" data-t="01:30:38">[01:30:38]</a>, <a class="yt-timestamp" data-t="01:31:04">[01:31:04]</a>. While the paper claims higher accuracy, quantitative results show it is only slightly more accurate (e.g., 0.1% difference) or comparable to SuperGlue <a class="yt-timestamp" data-t="01:28:27">[01:28:27]</a>, <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>. It is also simpler and easier to train <a class="yt-timestamp" data-t="01:31:13">[01:31:13]</a>, <a class="yt-timestamp" data-t="01:42:59">[01:42:59]</a>.

Despite its advancements, LightGlue still relies on external feature extraction models like SuperPoint (from 2018 Magic Leap research) or SIFT features <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>, <a class="yt-timestamp" data-t="01:27:27">[01:27:27]</a>, <a class="yt-timestamp" data-t="01:29:28">[01:29:28]</a>. This means the quality of the initial features heavily influences the overall performance <a class="yt-timestamp" data-t="01:36:52">[01:36:52]</a>.

> [!NOTE] Failure Cases
> LightGlue can struggle with matching repeated objects in a scene because its feature descriptors are too local. For instance, it might incorrectly match two identical-looking chairs that are actually distinct objects <a class="yt-timestamp" data-t="01:45:15">[01:45:15]</a>. More global feature descriptors might help mitigate this issue <a class="yt-timestamp" data-t="01:46:03">[01:46:03]</a>.

## Future Outlook
There's a recognized opportunity to improve the initial feature extraction component, potentially by developing newer, more advanced models than SuperPoint <a class="yt-timestamp" data-t="01:29:28">[01:29:28]</a>, <a class="yt-timestamp" data-t="01:37:13">[01:37:13]</a>. Ultimately, the ideal future for such complex [[Computer_vision_deep_dive | computer vision]] pipelines (like those for Gaussian Splatting) is to move towards end-to-end learning, where the entire process from raw video frames to 3D representation is handled by a single, combined model, rather than a series of individually trained, modular pieces <a class="yt-timestamp" data-t="01:37:20">[01:37:20]</a>, <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>, <a class="yt-timestamp" data-t="01:51:36">[01:51:36]</a>.