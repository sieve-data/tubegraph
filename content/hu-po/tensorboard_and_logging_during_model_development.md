---
title: Tensorboard and logging during model development
videoId: 9l9-2FbSccg
---

From: [[hu-po]] <br/> 

During the [[debugging_neural_network_training | debugging]] and [[finetuning_machine_learning_models | fine-tuning]] process of models like Segment Anything, effective logging and visualization tools such as Tensorboard are crucial for monitoring training progress and identifying issues <a class="yt-timestamp" data-t="02:04:54">[02:04:54]</a>.

## Purpose of Logging

Logging provides insights into various aspects of model performance and behavior, including:
*   **Loss Tracking**: Monitoring the combined loss (e.g., mean squared error, binary cross entropy) over training steps helps to determine if the model is learning <a class="yt-timestamp" data-t="01:56:45">[01:56:45]</a> <a class="yt-timestamp" data-t="02:02:31">[02:02:31]</a>.
*   **Image Visualization**: Logging images allows for visual inspection of model inputs, ground truth, predictions, and other intermediate outputs, which is vital for understanding why a model might not be performing as expected <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>. For instance, input infrared images, correct segmentation masks, and point prompts can be logged and viewed <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a> <a class="yt-timestamp" data-t="01:59:15">[01:59:15]</a>.
*   **Debugging**: By logging specific data points or states, developers can pinpoint where errors occur or where data transformations might be incorrect <a class="yt-timestamp" data-t="08:45:">[08:45]</a>.

## Setting Up Tensorboard

Tensorboard can be initiated from the command line once the logging output directory is established <a class="yt-timestamp" data-t="01:26:09">[01:26:09]</a>. For example, navigating to the project's root directory (`Dev/hoopo_Ashen_Venus`) and running `tensorboard --logdir logger_output` will launch the visualization interface <a class="yt-timestamp" data-t="01:26:51">[01:26:51]</a> <a class="yt-timestamp" data-t="01:27:35">[01:27:35]</a>.

## Logged Data Types

The following types of data can be logged to Tensorboard for analysis:
*   **Scalars**: Numerical values such as the combined loss, which should ideally decrease over training <a class="yt-timestamp" data-t="01:56:45">[01:56:45]</a> <a class="yt-timestamp" data-t="02:02:31">[02:02:31]</a>.
*   **Images**: Visual data including input images, predicted masks, and point annotations <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>. These images help verify transformations and model outputs visually <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>.

## Debugging Logging Issues

Several issues can arise during the logging process that require [[troubleshooting_and_debugging_machine_learning_code | debugging]]:

### Loss Not Appearing in Tensorboard
If the loss graph does not appear or shows as "greyed out" in Tensorboard <a class="yt-timestamp" data-t="01:56:51">[01:56:51]</a>, it indicates that the loss values are not being properly written or are not being detected by Tensorboard. This can often be resolved by checking the logging configuration and ensuring scalars are added correctly <a class="yt-timestamp" data-t="01:57:49">[01:57:49]</a>.

### Images Not Logging
When images are not appearing in Tensorboard, even if `log_images` is set to `True` <a class="yt-timestamp" data-t="01:34:04">[01:34:04]</a>, potential issues include:
*   **Incorrect Dimensions**: Tensorboard might complain about the input tensor shape for images (e.g., `1 by 1024 by 1024`) <a class="yt-timestamp" data-t="01:35:40">[01:35:40]</a>. This often requires careful re-shaping or unsqueezing of the image tensors to match the expected format (e.g., `B x C x H x W`) <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a> <a class="yt-timestamp" data-t="01:37:07">[01:37:07]</a>.
*   **Data Type Issues**: Ensure image data is in the correct format (e.g., float) and range (e.g., 0.0 to 1.0) <a class="yt-timestamp" data-t="01:50:14">[01:50:14]</a>. If images are initially `uint8` with values up to 255, they might need to be converted to `float32` and normalized by dividing by 255 <a class="yt-timestamp" data-t="01:50:42">[01:50:42]</a>.
*   **Point Label Discrepancies**: The visualization of points on images relies on correct point labels (e.g., 0 or 1 for background/foreground) <a class="yt-timestamp" data-t="01:52:51">[01:52:51]</a>. If points are not correctly colored (e.g., green for inside mask, red for outside mask), it indicates an issue with how point labels are generated or applied <a class="yt-timestamp" data-t="01:52:32">[01:52:32]</a> <a class="yt-timestamp" data-t="01:59:36">[01:59:36]</a>. This can be due to incorrect coordinate transformations, especially if points are meant to be relative to the entire image rather than a cropped section <a class="yt-timestamp" data-t="01:53:04">[01:53:04]</a>.

### Performance Considerations
Logging images, especially large ones or many of them, can significantly slow down the [[parallelizable_training_and_efficient_inference | training]] process as it involves saving data to disk <a class="yt-timestamp" data-t="02:04:44">[02:04:44]</a>. It is common practice to set `log_images` to `False` during initial [[debugging_neural_network_training | debugging]] or when running longer training sessions to prioritize speed <a class="yt-timestamp" data-t="02:04:37">[02:04:37]</a>. If encountering a [[hardware_for_ai_training_and_deployment | Cuda out of memory error]], switching to [[hardware_for_ai_training and deployment | CPU]] for debugging or reducing the [[parallelizable_training_and_efficient_inference | batch size]] (e.g., to 1 or 2) can help mitigate resource issues <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a> <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a> <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>.