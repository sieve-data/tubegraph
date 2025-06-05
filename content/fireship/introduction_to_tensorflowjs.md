---
title: Introduction to TensorFlowjs
videoId: Y_XM3Bu-4yc
---

From: [[fireship]] <br/> 

TensorFlow.js is a JavaScript library that enables the building, training, and prediction from machine learning models directly within the browser <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its announcement was considered the most exciting development in the week it was released, opening up new possibilities to combine web development with machine learning <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## What is TensorFlow?

At its core, TensorFlow is a library for performing mathematical computations <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It is widely recognized for its ability to build deep neural networks that power impressive artificial intelligence technologies <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. While not always easy for those without a machine learning background <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, resources like Coursera courses, Google's machine learning crash course, and participation in data science competitions on Kaggle can help individuals develop expertise <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## How Machine Learning Models Work (High-Level)

Typically, machine learning involves a dataset where each item has a label <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For example, in the M-NIST dataset, which consists of hand-drawn digits, humans can easily recognize the digits, but to a computer, each image is just a matrix of values without inherent meaning <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A convolutional neural network for image recognition analyzes many samples to extract distinguishing features <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The algorithm starts randomly and gradually corrects itself as it processes more samples <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Building and Training Models with TensorFlow.js

TensorFlow.js enables the process of building, training, and making predictions from models directly in the browser <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Basic Linear Regression Example

A simple example involves building a linear regression model <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
1.  **Setup**: Install TensorFlow.js in your project (e.g., an [[Angular]] app) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
2.  **Model Definition**: Define an empty model using `tf.sequential()` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This is part of the Sequential API, a higher-level API similar to Keras in Python <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. For linear regression, a single "dense" or fully connected layer is added, taking and outputting a shape of one <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
3.  **Compilation**: Define a `loss` metric (e.g., mean squared error) and an `optimizer` (e.g., stochastic gradient descent or SGD) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The optimizer determines how the model reaches the minimum error <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
4.  **Data Preparation**: Data is fed to the model in the form of a "tensor," which can be thought of simply as an array <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. `xs` represents the training features, and `ys` represents the labels (the values to predict) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  **Training**: The model is trained by calling `linearModel.fit()` with the `xs` and `ys` data <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This process creates a statistical model that can predict values <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
6.  **Prediction**: To make a prediction, `linearModel.predict()` is called, passing the input value as a tensor <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. The result, also a tensor, is then converted to an array for use in the UI <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Complex Neural Networks and Pre-trained Models

For more complex tasks like image recognition, TensorFlow.js can utilize models pre-trained in Python <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This is crucial because training intensive algorithms is too CPU and memory-heavy to run directly in the browser <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

#### Transferring Models from Python
[[Transferring machine learning models from Python to TensorFlowjs | Transferring models]] involves:
1.  **Training in Python**: Build a machine learning model using a library like Keras <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  **Export and Convert**:
    *   Export the trained Keras model <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Install the TensorFlow.js Python package (`pip install tensorflowjs`) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   Use the provided command to convert the Keras file to a TensorFlow.js-compatible format and shard the file for efficient web loading <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
3.  **Loading in Browser**: Use `tf.loadLayersModel()` to load the pre-trained model into the browser <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

#### Image Recognition Example (Handwritten Digits)
Using a pre-trained model for handwritten digit recognition with an HTML canvas:
*   **Prediction Output**: Predictions will be an array of ten values, each representing the probability that an index (0-9) is the correct value for the drawing <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The index with the highest probability is assumed to be the correct digit <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Memory Management**: To prevent memory leaks, especially with neural networks that use a lot of memory, code should be run inside `tf.tidy()` <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This ensures all tensors are released from memory after the prediction is finished <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Image Data Handling**: Image data from an HTML canvas (e.g., `ImageData` type) can be converted into a tensor <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. It's crucial to reshape the data to match the model's training input shape (e.g., 28x28 pixels with one color channel) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Data types also need to be consistent (e.g., casting integers to floating-point numbers) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Making Predictions**: Once the data is correctly formatted, pass it to the model's `predict()` method <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Convert the resulting tensor to an array using `dataSync()` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Learning More

For those interested in visualizing how neural networks build complex boundaries around datasets, the TensorFlow Playground is a recommended resource, having served as the original inspiration for TensorFlow.js <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.