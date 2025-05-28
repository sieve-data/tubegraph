---
title: Finetuning Segment Anything model
videoId: 9l9-2FbSccg
---

From: [[hu-po]] <br/> 

The video details the process of [[finetuning_machine_learning_models|finetuning]] the [[meta_ai_and_segment_anything_model|Segment Anything model]] (SAM) for a specific and challenging dataset known as the Scroll Prize [00:00:30]. This [[meta_ai_and_segment_anything_model|segmentation foundation model]] was developed by [[meta_ai_and_segment_anything_model|Meta AI Research]] [00:00:38].

## The Scroll Prize Challenge
The Scroll Prize dataset presents a unique and obscure data modality [00:01:22]. Unlike the standard [[meta_ai_and_segment_anything_model|Segment Anything model]] training data, which consists of cell phone images with an object-centric bias [00:01:31], the Scroll Prize images are unusual X-rays [00:01:52]. These X-rays are slices through pieces of an ancient scroll, aiming to output a binary [[meta_ai_and_segment_anything_model|segmentation map]] [00:02:04].

The problem is challenging because the X-ray images are very difficult to interpret [00:02:22]. Questions arise about how to process the data, such as whether to run the segmenter on every single slice, on random tuples of slices, or if any filtering is needed [00:02:35].

To address this, a "toy problem" was introduced: finetuning SAM on infrared images of the scroll [00:03:01]. Segmenting infrared images is much easier and aligns with the 3-channel RGB image modality used by SAM [00:03:06]. The strategy is to first get the model working on this simpler problem before switching to the complex X-ray images [00:03:20].

The code for this project is available on GitHub under the repository `hoopo Ashen Venus` [00:03:39].

## [[meta_ai_and_segment_anything_model|Segment Anything Model]] Architecture
The [[meta_ai_and_segment_anything_model|Segment Anything model]] has three main components [00:03:57]:
1.  **Image Encoder**: This component takes a batch of images and outputs them as embeddings [00:04:23]. It converts 3-channel RGB images into 256-channel encoded images, typically 64x64 pixels [00:04:39].
2.  **Prompt Encoder**: This encoder takes various inputs such as masks, points, boxes, or text [00:04:51]. For the Scroll Prize, points, masks, and potentially boxes are most relevant [00:05:12]. The prompt encoder's role is to convert these prompts into a language the mask decoder can understand [00:05:53].
3.  **Mask Decoder**: This component receives embeddings from the prompt encoder (sparse embeddings from points/boxes/text, and dense embeddings from masks) [00:06:05]. It then produces the actual segmentation masks and an IOU (Intersection Over Union) prediction, which acts as a confidence score for the mask [00:06:17].

## Loss Function
The original [[meta_ai_and_segment_anything_model|Segment Anything model]] was trained iteratively using a combination of focal loss and Dice loss [00:07:25]. It also included an IOU prediction head trained with mean squared error (MSE) between the IOU prediction and the predicted masks' IOU [00:07:34].

For the finetuning process, a "combined loss" function is used [00:07:49]. This loss is a combination of:
*   An MSE loss between the predicted IOU and the actual IOU, which trains the model's confidence score [00:07:57].
*   A binary cross-entropy with logits loss, as the mask output from the decoder is in logits form [00:08:16]. This is suitable for the binary segmentation problem of the Scroll Prize [00:08:30].

## Debugging and [[Efficiency and performance of finetuning methods|Performance]] Challenges
The [[finetuning_machine_learning_models|finetuning]] process involved significant debugging to address various errors [00:08:45].

### Initial Errors and Data Handling
*   **Index Out of Bounds**: Errors occurred due to incorrect indexing when accessing `Point labels` [00:09:31]. This was resolved by correcting the array access `Point labels of I` to `Point labels[I]` [00:10:15].
*   **Tensor to NumPy Conversion**: An error arose when converting a PyTorch tensor to a NumPy array without first moving it to the CPU (`.cpu()`) [00:10:53].
*   **Normalized vs. Pixel Coordinates**: The `point grid` was in normalized coordinates (0 to 1), but the labels required pixel coordinates [00:15:31]. Points had to be converted to pixel space using `int(np.clip(point * crop_size + start_offset))` [00:15:41].
*   **Pin Memory Error**: The `pin_memory=True` setting in the DataLoader caused an error because some tensors were not "pinnable" [00:17:31]. Pinning memory generally makes data loading faster [00:17:42], but it was disabled for debugging [00:17:39].

### [[Efficiency and performance of finetuning methods|CUDA Out of Memory]] and Batching
*   **CUDA Out of Memory**: The model, even the smallest version, quickly ran out of GPU memory, trying to allocate 3.75 GB [01:19:02].
    *   **Solution**: Switched to using the CPU for debugging [01:19:25] and reduced the batch size from a default (likely larger) to 3 [01:19:54], and later to 1 [01:31:23]. While training on CPU is undesirable for [[Efficiency and performance of finetuning methods|performance]], it's suitable for debugging [01:19:44].

### Model Input Dimensionality Issues
*   **Prompt Encoder Missing Arguments**: The `Prompt encoder` required `boxes` and `masks` arguments, even if they were `None` [01:21:00]. Explicitly passing `boxes=None` and `masks=None` resolved this [00:23:20].
*   **Mask Decoder Input Mismatch**: The `Image embeddings` (e.g., 9x256x64x64) and `Dense embeddings` (e.g., 3x256x64x64) had mismatched batch dimensions, leading to an error [00:25:26].
    *   **Problem**: The prompt encoder was losing the batch size information [01:17:47].
    *   **Observation**: The official [[meta_ai_and_segment_anything_model|Segment Anything model]] example processes images one at a time, suggesting that the `prompt encoder` might not be correctly implemented to work with batches [01:05:41]. Reducing the batch size to 1 was a workaround [01:31:23].
*   **Sparse Embeddings Dimensionality**: The `sparse embeddings` output from the `prompt encoder` showed an unexpected dimension (e.g., 3x65x256 where 65 felt "weird") [00:24:59]. This was later identified to be related to the `Point labels` having an extra dimension [01:00:59] and the model internally adding a padding token, resulting in 65 dimensions (64 points + 1 padding token) [01:12:06].

### Data Type and Shape Corrections
*   **Point Data Types**: `Point chords` were expected to be `float32` and `Point labels` `int32` [00:43:49]. Initial `numpy.uint8` types were converted to `torch.float32` and `torch.int32` respectively [00:44:12].
*   **Point and Label Shapes**: Initial shapes for points (e.g., 3x64x2) and labels (e.g., 3x64) did not match the expected 64x1x2 and 64x1 formats from the example [00:47:05]. `unsqueeze` operations were used to add dimensions where necessary [00:54:25].
*   **Image Normalization**: Infrared images were not normalized (values up to 255) [01:50:14]. Dividing the image tensor by 255.0 made it a float in the 0-1 range, which is more typical for model inputs [01:50:42].
*   **Label Reshaping for Loss Calculation**: The `low-res labels` for the `dice score` and `add_images` functions had incorrect shapes [01:34:23]. An `unsqueeze` operation was added to the `labels` tensor [01:36:56], ensuring correct formatting for both the loss calculation and visualization [01:37:15].

## Progress and Next Steps
After extensive debugging, the model was observed to be running, processing images and generating masks [02:00:26]. Visualization showed that the infrared image, its correct [[meta_ai_and_segment_anything_model|segmentation mask]], and corresponding points were being processed correctly [01:52:17]. The points on the mask were visually correct, with red indicating outside the mask and green indicating inside [01:59:34].

The combined loss function was observed to be going down [02:02:31], although at one point it showed an increase [02:03:48], suggesting that longer training or further hyperparameter tuning might be needed. The current point sampling strategy is a simple grid, which differs from the more sophisticated deterministic sampling described in the original SAM paper [02:00:02].

The next step is to run the [[finetuning_machine_learning_models|finetuning]] for a longer duration, disabling image logging to potentially speed up the process [02:04:41].