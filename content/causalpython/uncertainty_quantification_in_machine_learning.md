---
title: Uncertainty Quantification in Machine Learning
videoId: _mJclm_aJlc
---

From: [[causalpython]] <br/> 

Uncertainty quantification is considered a "hugely important" aspect of [[machine_learning_and_explainability | machine learning]] (ML) that is sometimes overlooked, especially when compared to its standard practice in medicine <a class="yt-timestamp" data-t="07:34:49">[07:34:49]</a>.

## Importance in Practice

In medical fields, it is a standard practice for nearly every paper to rigorously report uncertainty intervals for estimates, even in abstracts <a class="yt-timestamp" data-t="08:51:52">[08:51:52]</a>. This practice is crucial for reliable decision-making in medicine, particularly for treatment recommendation and selection <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>, as medical professionals will not use methods that rely solely on point estimates <a class="yt-timestamp" data-t="09:43:52">[09:43:52]</a>.

## Challenges and Gaps

Despite its importance, many current [[causality_and_machine_learning | causal machine learning]] methods for causal inference and treatment effect estimation are not yet capable of reliable uncertainty quantification <a class="yt-timestamp" data-t="09:07:10">[09:07:10]</a>. This capability is seen as the "holy grail" for bringing these methods into widespread medical practice <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

Key areas of focus for improving uncertainty quantification include:
*   **Conformal Prediction** <a class="yt-timestamp" data-t="07:22:15">[07:22:15]</a>
*   **Sensitivity Analysis** <a class="yt-timestamp" data-t="07:26:54">[07:26:54]</a>
*   **[[integration_of_uncertainty_estimation_in_data_science | Partial Identification]]** <a class="yt-timestamp" data-t="07:29:43">[07:29:43]</a> <a class="yt-timestamp" data-t="31:21:44">[31:21:44]</a>

The development of new methods and improved models is necessary for making reliable inferences in medical practice and other fields <a class="yt-timestamp" data-t="07:34:49">[07:34:49]</a>. Furthermore, professionals need education on best practice [[role_of_assumptions_in_machine_learning_models | robustness checks]], especially because causal inference relies on numerous [[role_of_assumptions_in_machine_learning_models | assumptions]] <a class="yt-timestamp" data-t="19:37:39">[19:37:39]</a>.

## Future Directions

There is a need for more comprehensive software tools and packages, such as those for [[integration_of_uncertainty_estimation_in_data_science | partial identification]], to facilitate the uptake of these ideas and methods in the broader [[causality_and_machine_learning | causal machine learning]] community <a class="yt-timestamp" data-t="31:18:20">[31:18:20]</a>.