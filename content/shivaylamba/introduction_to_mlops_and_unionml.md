---
title: Introduction to MLOps and UnionML
videoId: Ja9OmuhKv8M
---

From: [[shivaylamba]] <br/> 

[[Introduction to MLOps and UnionML]] addresses the challenges of deploying machine learning models and streamlines the machine learning (ML) workflow, particularly for data scientists and DevOps engineers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## What is MLOps?

MLOps is the practice of applying standard DevOps principles and practices to machine learning <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It aims to bridge the gap between data scientists, who often focus on model development, and DevOps engineers, who handle deployment and infrastructure <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Challenges in ML Deployment

A significant challenge for data scientists is [[deployment_challenges_in_machine_learning | deploying their models]] into production <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. While creating a model in a notebook is straightforward, putting it on the web or elsewhere can be complex <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Data scientists typically prefer not to get involved with DevOps tasks, and similarly, DevOps engineers often want to avoid machine learning specifics <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

MLOps seeks to:
*   Enable data scientists to automatically deploy their models <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Simplify the post-production process for models <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   Facilitate continuous evaluation and management of models in production <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## UnionML Framework

[[unionml_framework_for_reducing_boilerplate_code | UnionML]] is an open-source Python framework built on top of Flight, an open-source machine learning orchestration platform <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Flight provides end-to-end workflows and can easily manage operations on platforms like Kubernetes <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. UnionML aims to streamline the deployment process, making it smoother and faster <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It also supports scaling models and contexts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Reducing Boilerplate Code

A common complaint from data scientists is the extensive amount of boilerplate code required for various stages of an ML workflow <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This includes:
*   **Data Conversion:** Converting data from sources like SQL or NoSQL databases into formats usable by ML tools (e.g., Pandas DataFrames) often requires 15-20 lines of code <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Model Definition:** Defining model parameters and conducting hyperparameter tuning for models like TensorFlow, PyTorch, or ONNX also adds significant lines of code <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

[[unionml_framework_for_reducing_boilerplate_code | UnionML]] addresses this by providing ready-to-use decorator functions that abstract away the boilerplate code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. These decorators allow data scientists to focus primarily on model evaluation, which is the most critical part of an ML workflow <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For example:
*   A `data_reader` decorator can handle data transformation from SQL to CSV <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   A `model` decorator is used for initializing a model, which can be easily swapped between different frameworks like Scikit-learn, TensorFlow, or PyTorch <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   A `predictor` decorator is used for estimating objects with a data frame <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   An `evaluator` decorator is used for evaluating model performance <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### [[Machine learning integration and ecosystem in UnionML | Ecosystem and Integration]]

A significant strength of [[machine_learning_integration_and_ecosystem_in_unionml | UnionML]] is its ecosystem of integrations <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. It offers flexibility in:
*   **Model Integration:** Deploying models using frameworks like Fast API or Flight, or even to storage like an S3 bucket <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Data Store Integration:** Defining the type of data store to use <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **ML Model Types:** Working with various machine learning model types <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Deployment Targets:** Choosing where to deploy, such as a Fast API, web frameworks like Django or Flask, or Kubernetes-native environments like Seldon or KubeFlow <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Observability:** Providing tools for continuous evaluation and observability to monitor model performance in production <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

The core idea is that data scientists don't need to understand the underlying complexities; they can simply use decorator functions to define their desired outcomes <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### [[Building machine learning microservices | ML Microservices]]

UnionML enables the creation of [[building_machine_learning_microservices | machine learning-based microservices]] <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Just as microservices are prevalent in software development, UnionML allows data scientists and ML engineers to create their own ML-based microservices, fitting well within the broader MLOps framework <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.