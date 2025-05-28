---
title: Bias and Variance in Machine Learning
videoId: F1ka6a13S9I
---

From: [[lexfridman]] <br/> 

Bias and variance are fundamental concepts in machine learning that have been around for quite some time, yet their dynamics are shifting with advancements in deep learning. Understanding these concepts is crucial for developing effective machine learning models and making informed decisions about model training and optimization.

## Understanding Bias and Variance

Bias refers to the error due to overly simplistic assumptions in the learning algorithm. It can lead to underfitting, where the model is too simple to capture the underlying trends in the data. Variance, on the other hand, is the error due to too much complexity in the learning model. It results in overfitting, where the model captures noise along with the signal in the training data <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### The Bias-Variance Trade-off

Traditionally, bias and variance are thought to have a trade-off, meaning that decreasing one typically increases the other. This is a core consideration when developing machine learning models. Understanding whether a model suffers from high bias or high variance guides practitioners in deciding how to modify the model or data to improve performance <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

## Changes in the Deep Learning Era

In the era of deep learning, however, the relationship between bias and variance is becoming less rigid. With large neural networks and vast amounts of data, it has become possible to reduce both bias and variance simultaneously, a significant shift from the earlier paradigms <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

### Addressing High Bias and High Variance

When developing a machine learning system, if you observe high training error, this indicates high bias, suggesting the need to increase model complexity, such as by using a larger neural network or exploring new model architectures <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

Conversely, if the system shows high variance, indicated by significant discrepancies between training and dev set performance, strategies like acquiring more data, applying regularization, or adjusting model complexity can help <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.

### Workflow for Managing Bias and Variance

A practical approach involves first ensuring that your model performs well on the training set before addressing dev set performance. This sequential focus helps isolate whether the predominant issue is due to bias, variance, or other factors such as dev-test set mismatch <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

## Human-Level Performance

Benchmarking against human-level performance is another strategy to deepen the understanding of bias and variance. By aligning model performance with that of humans, it’s possible to better estimate the optimal error rate and gauge the extent of bias or variance issues <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>.

### Practical Steps

1. **Collect Human-Level Performance Data:** This serves as a baseline to determine how much improvement is achievable.
2. **Analyze Error Sources:** Break down system errors into components such as bias, variance, and train-test distribution mismatch to effectively target improvement efforts.
3. **Iterate with Focused Adjustments:** Use specific tactics based on whether bias or variance is predominant to incrementally enhance model performance <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

> [!info] Key Insight
> In the deep learning paradigm, managing bias and variance effectively involves leveraging vast data and large model architectures while also employing strategic benchmarking against human capabilities.

Understanding and balancing bias and variance remain pivotal in developing robust machine learning models. With deep learning, this balance is more manageable, providing broader pathways to enhance model generalization and performance.