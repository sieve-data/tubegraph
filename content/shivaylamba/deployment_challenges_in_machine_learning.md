---
title: Deployment challenges in machine learning
videoId: Ja9OmuhKv8M
---

From: [[shivaylamba]] <br/> 

Deploying machine learning models into production environments presents significant challenges for data scientists and engineers <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. While building a machine learning model is often perceived as straightforward, the process of deploying it is considered a major hurdle <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Many data scientists can create models in notebooks but struggle with how to deploy them on the web or elsewhere <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## The DevOps Gap

A primary challenge lies in the reluctance of data scientists to engage with DevOps practices, and similarly, DevOps engineers often prefer not to get involved with machine learning <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This creates a gap that hinders the seamless transition of models from development to production.

## [[introduction_to_mlops_and_unionml | MLOps]] as a Solution

[[introduction_to_mlops_and_unionml | MLOps]] aims to bridge this divide by applying standard software development and DevOps practices to machine learning workflows <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. The goal is to enable data scientists and DevOps engineers to collaborate effectively, providing tooling that allows data scientists to automatically deploy their models and manage them post-production <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This includes continuous model evaluation and easy management of model changes once in production <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## [[unionml_framework_for_reducing_boilerplate_code | UnionML]]'s Role in Streamlining Deployment

[[unionml_framework_for_reducing_boilerplate_code | UnionML]] is an open-source Python framework built on top of Flight, an open-source machine learning orchestration platform designed for end-to-end workflows and Kubernetes environments <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. [[unionml_framework_for_reducing_boilerplate_code | UnionML]] directly addresses the deployment friction, aiming to make the process smoother and faster <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. It enables scaling of models and contexts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Reducing Boilerplate Code

A significant pain point for data scientists is the extensive boilerplate code required for various stages of the machine learning workflow, such as:
*   **Data Conversion:** Converting data from different data stores (e.g., SQL, NoSQL) into a usable format like CSV or for Pandas, which can take 15-20 lines of code <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Model Definition:** Defining model parameters and performing hyperparameter tuning for models like TensorFlow, PyTorch, or ONNX, often requiring 10-15 lines of code <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

[[union_ml_framework_for_reducing_boilerplate_code | UnionML]] tackles this by providing ready-to-use decorator functions that abstract away this boilerplate code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This allows data scientists to focus primarily on model evaluation, which is the most critical part of the workflow <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For example, a `model` decorator function helps define the model parameters and algorithms <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, and a `data_reader` decorator helps with data transformation <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. These functions are "plug and play," simplifying the choice of model type or deployment target <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### [[machine_learning_integration_and_ecosystem_in_unionml | Integration and Ecosystem]]

[[union_ml_framework_for_reducing_boilerplate_code | UnionML]]'s "ecosystem of integration" is a significant strength <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. It allows users to:
*   Define the type of model integration <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Deploy models using various frameworks like Fast API, Django, or Flask <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Deploy models to Kubernetes-native environments like Flight or Kubeflow <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   Deploy models to services like S3 buckets <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Choose data stores and machine learning models <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   Continuously evaluate and monitor model performance in production using observability tools <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

The framework is designed so that users do not need to understand the underlying complexities, simply using the decorator functions to define their deployment targets <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## Enabling [[building_machine_learning_microservices | ML Microservices]]

Ultimately, [[union_ml_framework_for_reducing_boilerplate_code | UnionML]] aims to enable the creation of [[building_machine_learning_microservices | machine learning-based microservices]] <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This concept mirrors the use of microservices in standard software development, allowing data scientists and machine learning engineers to create and manage these modular services efficiently within the broader [[introduction_to_mlops_and_unionml | MLOps]] ecosystem <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.