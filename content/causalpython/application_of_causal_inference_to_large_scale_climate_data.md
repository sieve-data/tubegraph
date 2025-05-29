---
title: Application of causal inference to large scale climate data
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

Applying [[causal_inference_and_machine_learning | causal inference]] and causal representation learning to large-scale climate data is a promising area of research [00:20:49]. The goal is to extract causal information and formulate causal models regarding macroclimate phenomena using high-dimensional measurements [00:20:54].

## Challenges and Approaches

A significant challenge in applying [[application_of_causal_models_in_climate_science | causal inference in climate science]] is the inability to actively perform interventions on the climate [00:21:15]. Despite this, researchers are exploring methods that can work with heterogeneous data collected from different environments [00:21:12].

One important step in this direction is moving away from the assumption of single-node interventions to allow for multi-node interventional environments [00:21:21]. This approach is crucial because in real-world scenarios, particularly with climate data, interventions are often complex and affect multiple variables simultaneously [00:19:36].

## Research Focus

Current research in this domain aims to:
*   Characterize a specific notion of sparsity [00:19:48].
*   Operationalize the sparse mechanism shift hypothesis, which posits that changes in underlying causal models across environments are sparse [00:19:52].
*   Regularize for sparsity when there's a linear mixing function from latent to observed variables [00:20:15].
*   Ensure the coverage of interventions across environments is sufficiently diverse and sparse [00:20:24].

These principles can help recover underlying causal variables, even with the inherent indeterminacy of permutation and element-wise rescaling [00:20:31]. The ultimate goal is to build a foundation for work that can be applied to real-world climate data [00:21:07].