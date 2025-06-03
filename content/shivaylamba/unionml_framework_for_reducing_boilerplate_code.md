---
title: UnionML framework for reducing boilerplate code
videoId: Ja9OmuhKv8M
---

From: [[shivaylamba]] <br/> 

UnionML is an open-source Python framework built on top of Flyte, an open-source machine learning orchestration platform that provides end-to-end workflows and can manage environments like Kubernetes [02:20:41]. The primary goal of UnionML is to streamline the deployment of machine learning models into production and make the process smoother [02:48:07].

## Addressing Data Scientist Challenges in MLOps

A common challenge for data scientists is deploying their machine learning models [01:10:48]. While building a model might be relatively easy, deployment often presents the main hurdle [01:19:64]. Data scientists typically write a lot of Python code, often in notebooks, Python files, or PySpark [00:54:19]. However, they generally prefer not to get involved with DevOps practices [01:31:07]. Similarly, DevOps engineers don't want to get involved with machine learning [01:34:64].

[[introduction_to_mlops_and_unionml | MLOps]] aims to bridge this gap by applying standard software development practices to machine learning [01:38:59]. UnionML specifically tries to connect data scientists and DevOps engineers, providing tooling that enables data scientists to automatically deploy their models written in notebooks, making post-production easier [01:51:71]. This tooling also facilitates continuous model evaluation and managing changes to models once they are in production [02:04:22].

## Reducing Boilerplate Code with Decorator Functions

In a typical machine learning workflow, after training data, a significant amount of boilerplate code is often required for various steps [03:14:02]. For instance, data conversion from SQL or NoSQL databases to formats usable by tools like Pandas can require 15-20 lines of code [03:40:48]. Defining a machine learning model (e.g., TensorFlow, PyTorch, ONNX) and performing hyperparameter tuning can also add another 10-15 lines of code [04:01:83].

UnionML primarily addresses this by eliminating much of this boilerplate code [04:24:60]. It provides ready-to-use decorator functions that abstract away the complexities of data preprocessing, model training, and deployment [04:36:27]. These functions allow data scientists to:
*   Perform data transformations, such as converting SQL data to CSV files, within a `data_reader` decorator [06:52:16].
*   Define different types of models (e.g., Scikit-learn, TensorFlow, PyTorch) by simply replacing the model initialization function [06:30:17].
*   Manage hyperparameter tuning within the training function [06:43:08].
*   Choose deployment targets like Fast API, Django, Flask, or Kubernetes-native environments like Flyte or Kubeflow using specific decorator functions [07:11:47].

This approach allows data scientists to focus primarily on model evaluation, which is the most important part of any machine learning workflow [04:47:62]. They don't need to know what's happening behind the scenes, only to use the decorative function and define the target for deployment [08:26:75].

## Ecosystem and Integration

UnionML's significant strength lies in its [[machine_learning_integration_and_ecosystem_in_unionml | ecosystem of integration]] [07:44:03]. It supports various integrations, including:
*   **Model Integration**: Fast API, Flyte, or even deploying models to an S3 bucket [07:48:47].
*   **Data Stores**: Defining the type of data store to use [07:58:81].
*   **ML Models**: Choosing different machine learning model types [08:02:18].
*   **Observability**: Bringing in observability to continuously evaluate how models perform in production [08:05:37].

The framework enables the creation of [[building_machine_learning_microservices | machine learning-based microservices]], similar to how microservices are used in software development [08:34:03]. This allows data scientists or machine learning engineers to build these services, which aligns well with the overall [[introduction_to_mlops_and_unionml | MLOps]] workflow [08:45:34].