---
title: Applications of neural networks in image recognition
videoId: Y_XM3Bu-4yc
---

From: [[fireship]] <br/> 

Neural networks have significantly advanced image recognition capabilities, revolutionizing the field <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. TensorFlow, a library for mathematical computations, is particularly known for building deep neural networks that power some of the most impressive [[artificial_intelligence_and_aidriven_tools | artificial intelligence]] technologies available today <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Core Process of Image Recognition

For a computer, an image is merely a matrix of values without inherent context or meaning <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. A typical image recognition convolutional neural network addresses this by analyzing many samples of images to extract features that distinguish one item from another <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The algorithm begins randomly and then progressively self-corrects as it processes more and more image samples <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Example: Hand-Drawn Digit Prediction

A compelling application involves using neural networks to predict the actual numeric value of a hand-drawn digit image <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.

### Dataset and Training

*   **MNIST Dataset** This process often utilizes a dataset like MNIST, which consists of images of hand-drawn digits <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Feature Extraction** The neural network learns to extract features from these images that allow it to differentiate between various digits <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   **Output** For a pre-trained model, predictions are typically an array of ten values, with each value representing the probability that a specific index (0-9) is the correct value for the drawing <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. The index with the highest probability is then considered the predicted number <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>.
*   **Image Preprocessing** The model requires input images to be reshaped to the format it was trained on, for instance, 28 pixels by 28 pixels with one color channel <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. Data types also need to be consistent, typically floating-point <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

### Deployment with TensorFlow.js

While training such an algorithm can be computationally and memory intensive, TensorFlow.js allows for the importation of models that have been trained in Python environments <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. This means a machine learning model can be built and trained offline, then uploaded to a web application for users to interact with directly in their browser <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a> <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

Tools exist to [[transferring_machine_learning_models_from_python_to_tensorflowjs | convert models from Keras]] into a TensorFlow.js compatible format, which can also shard the file for efficient loading on the web <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. Memory management is crucial in client-side applications using neural networks, and methods like `tensorflow.tidy` can ensure tensors are released from memory after a prediction is complete <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.