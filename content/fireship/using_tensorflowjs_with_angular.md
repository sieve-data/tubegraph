---
title: Using TensorFlowjs with Angular
videoId: Y_XM3Bu-4yc
---

From: [[fireship]] <br/> 

The announcement of [[introduction_to_tensorflowjs | TensorFlow.js]], a JavaScript library, allows users to build, train, and make predictions from machine learning models directly in the browser <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This opens up new possibilities to combine web development with machine learning <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. One application is using [[introduction_to_tensorflowjs | TensorFlow.js]] with [[implementing_the_javascript_sdk_in_angular | Angular]] to predict the numeric value of a hand-drawn digit image <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What is TensorFlow?

TensorFlow is a library primarily known for performing mathematical computations <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It is famous for building deep neural networks that power impressive artificial intelligence technology <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. While it can be challenging to use without a machine learning background <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, it is possible to learn <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Learning Machine Learning

To become proficient in machine learning, it's recommended to spend half your time with traditional courses like Coursera or Google's machine learning crash course <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The other half should be spent applying what you learn in data science competitions on Kaggle, a hub for data science competitions <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, though these competitions can be very addicting <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### High-Level Overview of ML Models

Machine learning models typically involve a dataset where each item has a label <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For instance, in the context of hand-drawn digits, the MNIST dataset is used, which consists of images of hand-drawn digits <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. While humans can easily recognize these digits <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, to a computer, each image is a matrix of values without inherent context or meaning <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

A typical image recognition convolutional neural network examines many samples of these images to extract features that distinguish one digit from another <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The algorithm begins randomly and progressively corrects itself by observing more samples <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Building a Basic [[introduction_to_tensorflowjs | TensorFlow.js]] Model (Linear Regression)

To start, you can generate a new [[implementing_the_javascript_sdk_in_angular | Angular]] app using the [[implementing_the_javascript_sdk_in_angular | Angular]] CLI, then install [[introduction_to_tensorflowjs | TensorFlow.js]] <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Model Definition

A basic [[introduction_to_tensorflowjs | TensorFlow.js]] model, such as a linear regression, can be built <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This model would predict a value based on an input, similar to predicting a person's weight from their height <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

In an [[implementing_the_javascript_sdk_in_angular | Angular]] application, the model can be trained when the component initializes <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, and predictions can be run when a user enters a new value into a form field <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

To implement this, you can import [[introduction_to_tensorflowjs | TensorFlow.js]] under the namespace `tf` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

The `sequential` API in [[introduction_to_tensorflowjs | TensorFlow.js]] is a higher-level, easier-to-use interface, similar to Keras in [[transferring_machine_learning_models_from_python_to_tensorflowjs | Python]] <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

An asynchronous function, such as `trainNewModel`, defines an empty model by calling `tf.sequential()` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. For linear regression, a `dense` layer (or fully connected layer) is added, which outputs a shape of one and takes an input shape of one <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The model also needs a **loss metric**, which for linear regression is typically `meanSquaredError` (minimizing the mean squared error of predictions) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. An **optimizer** is also defined, which is the function determining how the model reaches the minimum error point (e.g., `SGD` for stochastic gradient descent) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Data and Training

Data must be fed to the model in the form of a **tensor** <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. For practical purposes, a tensor can be thought of as an array <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

*   **X variable**: Represents the actual training features for the dataset <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Y variable**: Represents the label for the data, which is the value the machine learning algorithm aims to predict <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

Training the model is done by calling `linearModel.fit()` with the X and Y data <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. The result is a statistical model capable of predicting values based on the provided dataset <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Making Predictions

To make a prediction, `linearModel.predict()` is called, passing the input value as a tensor <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Since the prediction is returned as a tensor, it needs to be converted into a usable format for [[implementing_the_javascript_sdk_in_angular | Angular]] <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. This is done by creating an array and calling `dataSync()` on the tensor, as [[introduction_to_tensorflowjs | TensorFlow.js]] runs in the context of a session <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

This prediction method can be linked to an HTML form input, allowing the application to display real-time predictions based on user input <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Advanced Example: Image Recognition with Neural Networks

Neural networks have significantly advanced image recognition <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. For instance, a neural network can predict the value of a handwritten digit drawn on an HTML canvas <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Importing Pre-trained Models

Training complex algorithms like those for image recognition can be too CPU and memory intensive to run directly in the browser <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. A key feature of [[introduction_to_tensorflowjs | TensorFlow.js]] is the ability to [[transferring_machine_learning_models_from_python_to_tensorflowjs | import models that have been trained in Python]] <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This means a machine learning model can be built and trained on a local system (e.g., using Keras in [[transferring_machine_learning_models_from_python_to_tensorflowjs | Python]]) and then uploaded to a web app for user access <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

To convert a Keras model for [[introduction_to_tensorflowjs | TensorFlow.js]], you need to install [[introduction_to_tensorflowjs | TensorFlow.js]] using the [[transferring_machine_learning_models_from_python_to_tensorflowjs | Python]] package manager `pip` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This provides a command to convert the Keras file to a [[introduction_to_tensorflowjs | TensorFlow.js]]-compatible format and shard the file for efficient web loading <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. In a real-world scenario, a cloud storage bucket would be used instead of the [[implementing_the_javascript_sdk_in_angular | Angular]] assets directory for storing the model <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Loading and Predicting with the Model

After conversion, a `loadModel` method can be added to the [[implementing_the_javascript_sdk_in_angular | Angular]] app component's `ngOnInit` lifecycle hook <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This time, the model will be of type `tf.Model`, which is a lower-level API <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Predictions will be an array of ten values, each representing the probability that a specific index is the correct value for the drawing <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The index with the highest probability is assumed to be the drawn number <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

Since the model is pre-trained, it can be loaded with `tf.loadLayersModel()` <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

The prediction method for image recognition requires careful memory management. All code can be run inside `tf.tidy()` to ensure that all tensors are released from memory once the prediction is complete, preventing memory leaks in client-side applications <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

Image data from an HTML canvas (extracted as `ImageData` type) can be passed to [[introduction_to_tensorflowjs | TensorFlow.js]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The image needs to be reshaped into the dimensions the model was trained on (e.g., 28x28 pixels with one color channel) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The first value in the shape is the batch size, typically 1 for a single image <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. If the model was trained with an integer data type, [[introduction_to_tensorflowjs | TensorFlow.js]] may require a floating-point type, which can be achieved using `tf.cast()` <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, ensuring all data types in a tensor are consistent <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Once the data is in the correct format, it is passed to the model, and `predict()` is called <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. The prediction, returned as a tensor, is then converted to an array using `dataSync()` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This prediction method can be set to run every time a new image is drawn onto the canvas <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Visualization and Further Resources

For visualizing how neural networks operate, the [[introduction_to_tensorflowjs | TensorFlow]] Playground is highly recommended. It was the original inspiration for [[introduction_to_tensorflowjs | TensorFlow.js]] and demonstrates how neural networks create complex boundaries around datasets to make predictions <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

For more content on [[introduction_to_tensorflowjs | TensorFlow]] or to learn how to build modern JavaScript apps for any platform, consider becoming a pro member at AngularFirebase.com <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.