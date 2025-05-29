---
title: Role of Assumptions in Machine Learning Models
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

The development and application of [[Developing Effective Machine Learning Models | machine learning models]] inherently rely on various assumptions. Understanding and explicitly addressing these assumptions is crucial for building robust, reliable, and generalizable systems, especially in high-stakes domains like medical imaging [00:15:47].

## Implicit and Explicit Assumptions
While transitioning from statistical parametric learning to non-parametric large models like deep learning, some assumptions are relaxed, making models more flexible [00:15:15]. However, the core issue is not the presence or absence of assumptions, but rather the forgetting or implicit nature of certain assumptions [00:16:32].

It's impossible to build [[Developing Effective Machine Learning Models | machine learning models]] without any assumptions [00:15:57]. The goal should be to identify which assumptions are valid and make them explicit [00:16:03]. This transparency allows for testing, challenging, and discussing these assumptions, fostering a more rigorous scientific approach [00:16:45]. Forgetting assumptions can lead to hidden problems that only surface later [00:19:07].

## Challenges from Forgotten Assumptions
One common, often forgotten, assumption in [[Developing Effective Machine Learning Models | machine learning models]] is that models operate within Euclidean latent spaces [00:17:16]. Research has shown that models like Variational Autoencoders (VAEs) might implicitly build highly high-dimensional Riemannian manifolds rather than Euclidean spaces, leading to noise when linear Euclidean interpolations are performed [00:17:40]. Challenging this assumption has led to the development of hyperbolic [[Developing Effective Machine Learning Models | machine learning models]] [00:18:31].

## The Importance of Data Quality and Representation
A fundamental assumption for any [[Developing Effective Machine Learning Models | machine learning]] algorithm is the availability of good quality and representative data [00:06:06]. Poor data quality or bias can lead to models that classify based on spurious correlations rather than true underlying phenomena [00:06:40]. For example, early COVID-19 detection tools built on X-rays were biased because positive cases came from Chinese hospitals and negatives from US hospitals, making the model classify based on image origin rather than disease [00:06:40]. This highlights that data collection itself is part of the system-building process where [[Causality and Machine Learning | causal]] thinking is crucial [00:08:08].

## Assumptions in [[Causality and Machine Learning | Causal Inference]]
While [[Causality and Machine Learning | causal inference]] is sometimes criticized for relying on many assumptions, a key difference is that it aims to make these assumptions explicit [00:16:37]. This allows for a clear understanding of the model's limitations and conditions under which it operates [00:16:45]. For instance, certain identifiability results in [[Causality and Machine Learning | causal models]], like the "no prevention" monotonicity constraint, are derived from fields like epidemiology and are explicitly stated [00:24:09].

The application of [[Causality and Machine Learning | causal reasoning]] helps in better understanding the problem, identifying key elements, and controlling for confounding variables that might affect results, leading to better models [00:24:58].

## Real-World Implications of Assumptions
In real-world applications, especially in critical fields like medical imaging or aeronautics, the impact of invalid assumptions can be severe [00:13:39]. For example, in medical diagnosis, wrong diagnoses by AI models can lead to life-and-death consequences, raising complex legal and ethical questions about accountability [00:04:16].

Current [[Developing Effective Machine Learning Models | machine learning models]], including large language models like ChatGPT, can "hallucinate" or provide incorrect answers because they lack [[Integration of causal reasoning in machine learning | causal]] understanding and operate based on correlational patterns [00:26:16]. These mistakes, though amusing in simple examples (like suggesting a comma before a period), can be very risky when projected onto mission-critical applications [00:26:56].

## Managing Assumptions for Robustness
To make [[Developing Effective Machine Learning Models | machine learning models]] robust and generalize well, acknowledging and dealing with underlying assumptions is paramount [00:14:47]. The application of frameworks like Technology Readiness Levels (TRLs) to [[Developing Effective Machine Learning Models | machine learning models]] emphasizes a steady, step-by-step development process with checks and balances [00:13:10]. This helps ensure accountability and prevents premature deployment of systems that might fail due to unaddressed assumptions [00:13:17].

[[Uncertainty Quantification in Machine Learning | Sensitivity analysis]], for instance, is a technique used to understand when model assumptions might fail and under what circumstances [00:22:21]. This helps in building systems that are robust against real-world complexities and limitations [00:22:33].

In essence, [[Role of assumptions in causal inference | all models are built on assumptions]]. The key is to be explicit about them, test their validity, and understand their implications for the model's performance and applicability [00:27:48]. No model or approach is a panacea, but understanding the tools and their underlying assumptions allows for their appropriate application [00:28:34].