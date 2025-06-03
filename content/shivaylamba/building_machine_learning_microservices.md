---
title: Building machine learning microservices
videoId: Ja9OmuhKv8M
---

From: [[shivaylamba]] <br/> 

The deployment of machine learning (ML) models presents a significant challenge for data scientists <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. While building an ML model can be relatively easy, deploying it is often cited as the main hurdle <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Data scientists typically prefer not to engage with DevOps practices, and similarly, DevOps engineers often avoid involvement with machine learning <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This creates a gap in the ML workflow.

## Bridging the Gap with MLOps and UnionML

MLOps aims to bridge this gap by applying standard DevOps practices from software development to machine learning <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. [[introduction_to_mlops_and_unionml | UnionML]] is a tool designed to facilitate collaboration between data scientists and DevOps engineers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Its goal is to make it easier for data scientists to automatically deploy the models they develop, streamline the post-production process, enable continuous model evaluation, and manage model changes in production <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

[[introduction_to_mlops_and_unionml | UnionML]] is an open-source Python framework built on Flyte <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Flyte itself is an open-source machine learning orchestration platform that offers end-to-end workflows and can be easily managed on environments like Kubernetes <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Reducing Boilerplate Code with UnionML

One of the major problems [[introduction_to_mlops_and_unionml | UnionML]] addresses is reducing the boilerplate code typically required for deploying ML models to production, making the process smoother <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. It also supports scaling models or contexts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

In a typical ML workflow:
*   **Data Conversion** <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>: Data scientists often need to write significant code (e.g., 15-20 lines) to convert data from formats like SQL databases to CSV files for use with tools like Pandas <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Model Definition** <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>: Defining machine learning models (e.g., TensorFlow, PyTorch, ONNX) and performing hyperparameter tuning can also involve 10-15 lines of code <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

[[unionml_framework_for_reducing_boilerplate_code | UnionML]] tackles this by providing ready-to-use decorator functions that eliminate the need to write much of this boilerplate code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. These decorators abstract away the complexities of data preprocessing, model training, and more <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This allows data scientists to focus primarily on model evaluation, which is the most critical part of an ML workflow <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For instance, a data reader decorator can handle data transformation from SQL to CSV <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

## Deploying Models as Microservices

[[introduction_to_mlops_and_unionml | UnionML]] simplifies the process of deploying models by offering plug-and-play functionality with its decorator functions <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Data scientists can choose where to deploy their functions, whether with:
*   A Fast API <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>
*   Web frameworks like Django or Flask <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
*   A Kubernetes-native environment like Flyte or KubeFlow <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>

The core idea is that data scientists no longer need to write extensive boilerplate code for deployment; they can use these pre-defined decorator functions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Ecosystem and Integration

[[machine_learning_integration_and_ecosystem_in_unionml | UnionML]] excels in its [[machine_learning_integration_and_ecosystem_in_unionml | ecosystem integration]] <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. It supports:
*   Different model integrations (Fast API, Flyte) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>
*   Deployment to platforms like S3 buckets <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>
*   Integration with various data stores and machine learning models <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>
*   Continuous evaluation and observability for models in production <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>

The framework allows users to define the target for deployment using decorator functions without needing to understand the underlying complexities <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This enables the easy use of machine learning models as microservices <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>, mirroring the concept of microservices in standard software development <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Data scientists and ML engineers can create these ML-based microservices, fitting well within an MLOps framework <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.