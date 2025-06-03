---
title: Machine learning integration and ecosystem in UnionML
videoId: Ja9OmuhKv8M
---

From: [[shivaylamba]] <br/> 

[[UnionML framework for reducing boilerplate code | UnionML]] is an open-source Python framework built on top of Flight, an open-source machine learning orchestration platform. Flight provides end-to-end workflows and can be easily managed on a Kubernetes-native environment [00:02:20].

## Addressing Deployment Challenges and [[introduction_to_mlops_and_unionml | MLOps]]
A significant challenge for data scientists is deploying machine learning models to production [00:01:06]. While building a model might be straightforward, getting it deployed on the web or elsewhere is a common question for beginners [00:01:19]. Data scientists often prefer not to get involved with DevOps, and similarly, DevOps engineers may not want to engage with machine learning [00:01:30].

This is where [[introduction_to_mlops_and_union_ml | MLOps]] comes in, aiming to bring standard DevOps practices to machine learning [00:01:36]. [[UnionML framework for reducing boilerplate code | UnionML]] specifically addresses this gap by creating tooling that enables data scientists and DevOps engineers to collaborate effectively [00:01:48]. It facilitates automatic model deployment, simplifies post-production management, enables continuous model evaluation, and eases changes to models once they are in production [00:01:56]. The framework is designed to decrease friction in deploying models to production, making the process much smoother [00:02:40].

## Streamlining the ML Workflow with Decorator Functions
A common pain point for data scientists is writing extensive boilerplate code for various stages of the machine learning workflow [00:04:20]. For example, converting data from a SQL database to a CSV file for use with Pandas can require 15-20 lines of code [00:03:51]. Similarly, defining a machine learning model, its parameters, and performing hyper-parameter tuning can involve 10-15 lines of code [00:04:07].

[[UnionML framework for reducing boilerplate code | UnionML]] addresses this by offering ready-to-use decorator functions that abstract away much of this boilerplate code [00:04:25]. This allows data scientists to focus primarily on model evaluation, which is the most critical part of any machine learning workflow [00:04:52].

Key areas where these decorator functions simplify the process include:
*   **Data Reading**: A `data_reader` decorator function handles data transformation, such as converting data from SQL to CSV [00:06:58].
*   **Model Initialization**: A `model` decorator function, which can be replaced with specific libraries like `sklearn_model`, `tensorflow_model`, or `pytorch_model`, initializes the chosen machine learning model (e.g., Logistic Regression, TensorFlow, PyTorch) [00:06:30].
*   **Training**: A `trainer` decorator function manages the training process, including hyper-parameter tuning [00:06:43].
*   **Prediction**: A `predictor` decorator function is used to estimate output from the model [00:05:57].
*   **Evaluation**: An `evaluator` decorator function helps assess the model's performance [00:06:00].

The idea is that data scientists can simply "plug and play" these functions, defining their desired accomplishments without writing the underlying boilerplate code [00:07:04].

## Ecosystem of Integration
The true power of [[UnionML framework for reducing boilerplate code | UnionML]] lies in its extensive ecosystem of integration [00:07:44]. It supports various aspects of the machine learning lifecycle:
*   **Model Integration**: Define the type of model you want to use [00:07:48].
*   **Deployment Targets**: Deploy models using options like FastAPI, web frameworks (Django, Robin, Flask), or Kubernetes-native environments like Flyte or KubeFlow [00:07:10].
*   **Data Store Definition**: Specify the kind of data store you wish to use [00:08:00].
*   **Machine Learning Model Types**: Choose from various machine learning models [00:08:02].
*   **Post-Production Management**: After a model goes into production, [[UnionML framework for reducing boilerplate code | UnionML]] helps with continuous evaluation and observability to monitor its performance [00:08:05].

This comprehensive ecosystem ensures that data scientists don't need to know the intricate details happening behind the scenes. They can simply use the decorative functions and define the target for deployment [00:08:26].

## [[building_machine_learning_microservices | Machine Learning Microservices]]
[[UnionML framework for reducing boilerplate code | UnionML]] enables the easy creation of [[building_machine_learning_microservices | machine learning models as microservices]] [00:08:34]. Just as microservices are prevalent in software development, [[UnionML framework for reducing boilerplate code | UnionML]] allows data scientists and machine learning engineers to create their own machine learning-based microservices [00:08:43]. This capability integrates seamlessly with the overall [[introduction_to_mlops_and_union_ml | MLOps]] workflow [00:08:52].