---
title: Challenges in causal machine learning versus traditional machine learning
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

[[Causal AI and machine learning | Causal machine learning]] engineering presents distinct challenges compared to traditional [[Machine learning versus causal inference for decisionmaking | machine learning engineering]] <a class="yt-timestamp" data-t="13:16"></a>. While traditional [[causal AI and machine learning | machine learning]] often focuses on predictive accuracy, [[Causality and Machine Learning | causal machine learning]] aims to understand cause-and-effect relationships, which requires a more rigorous approach to data and model assumptions <a class="yt-timestamp" data-t="13:23"></a>.

## The Problem with Naive Confounder Control
A primary challenge is the need for additional work to prevent misspecification of variables from leading to significant changes in predicted outcomes <a class="yt-timestamp" data-t="13:23"></a>. It might seem intuitive to include all potential confounding variables in a model, especially in applications like Spotify where thousands of potential confounders could exist <a class="yt-timestamp" data-t="13:37"></a>. However, naively controlling for numerous variables can actually worsen causal effect estimates rather than improving them <a class="yt-timestamp" data-t="14:04"></a>.

This is because:
*   **Not all variables are confounders:** Some variables might not be true confounders; they could be "colliders" between the treatment and the outcome <a class="yt-timestamp" data-t="14:14"></a>.
*   **Worse estimates:** Including colliders in the adjustment set can lead to incorrect causal identification <a class="yt-timestamp" data-t="14:08"></a>.

## The Importance of Causal Graphs and Prior Thinking
Before the engineering phase of plugging variables into estimators, it's crucial to engage in deep conceptual thinking <a class="yt-timestamp" data-t="14:25"></a>. This involves:
*   **Defining the DAG (Directed Acyclic Graph):** Understanding the causal graph helps in identifying which variables are true confounders and should be part of the adjustment set <a class="yt-timestamp" data-t="14:26"></a>.
*   **Assumptions:** While traditional deep learning practitioners might be wary of making explicit assumptions for [[causal AI and machine learning | causal methods]], having to think about these assumptions upfront is a "bonus" in [[causal AI and machine learning | causal inference]] <a class="yt-timestamp" data-t="10:20"></a>. It forces a deep consideration of whether the data generation process for a specific problem is reasonable for the chosen assumptions <a class="yt-timestamp" data-t="10:51"></a>.

> "you have to think a bit more deeply than just plugging everything into a black box and then trusting what the outcome is you to think before you even do that and then when you look at the data you think about okay what methodology should I be using here to really get confidence in the out in in the outcome but also get as much out of the specific data I have as as possible" <a class="yt-timestamp" data-t="15:07"></a>

## Methodology Selection and Data Characteristics
The specific characteristics of the data also influence the choice of [[Integration of causal reasoning in machine learning | causal methodology]] <a class="yt-timestamp" data-t="14:34"></a>:
*   **Data noise and variance:** Understanding the noise and variances in the data can guide the selection of appropriate methods, such as double [[causal AI and machine learning | machine learning]] <a class="yt-timestamp" data-t="14:39"></a>.
*   **Action space and confounder set:** Standard techniques like inverse propensity weighting might not be suitable if the action space or confounder set has very large variances in their values, making it difficult to control the variance of causal effect estimates <a class="yt-timestamp" data-t="14:50"></a>.

In essence, [[challenges and advancements in causal AI | causal machine learning]] requires a more conceptual framework and a deeper understanding of the data generation process, both before and after the application of methodologies <a class="yt-timestamp" data-t="15:24"></a>. This contrasts with traditional [[causal AI and machine learning | machine learning]] where the focus might be more on optimizing algorithms and models without as much explicit attention to causal identification and underlying assumptions <a class="yt-timestamp" data-t="15:07"></a>.