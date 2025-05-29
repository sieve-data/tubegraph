---
title: Uncertainty quantification in causal machine learning
videoId: _mJclm_aJlc
---

From: [[causalpython]] <br/> 

Uncertainty quantification is a critical area of focus within [[causal_inference_and_machine_learning | causal machine learning]], particularly for ensuring reliable real-world applications <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## Importance of Uncertainty Quantification
In contrast to traditional machine learning, the medical field routinely reports uncertainty intervals for estimates in nearly every paper, even in abstracts, emphasizing its importance for reliable decision-making <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. However, many current [[machine_learning_and_causal_inference_methodologies | machine learning methods for causal inference]] and treatment effect estimation are not yet capable of providing reliable uncertainty quantification <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This is a significant challenge for the broader [[causal_inference_and_machine_learning | causal machine learning]] community <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

For [[application_of_causal_machine_learning_in_medicine | medical applications]], especially regarding treatment recommendation and selection, methods that rely solely on point estimates are insufficient <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The ability to provide rigorous uncertainty quantification is considered a "holy grail" for integrating [[machine_learning_and_causal_inference_methodologies | causal machine learning methods]] into medical practice <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Key Areas of Research
Research in this area is focused on methods such as:
*   Conformal prediction <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>
*   Sensitivity analysis models <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
*   Partial identification <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, where comprehensive Python packages are still needed <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>.

## Challenges and Future Directions
The primary [[challenges_in_causal_machine_learning_compared_to_traditional_methods | challenge]] lies in the unobservable nature of counterfactual values <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. This necessitates extensive testing and robust methodologies to determine what works effectively in practice <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. Progress in the community is seen in making concepts more accessible through simplified language and popularizing these ideas <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. While there has been significant [[advances_in_causal_machine_learning_research | progress]], more resources are needed to guide users in understanding and applying these methods <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>, such as accessible books and "role model papers" that outline best practices and robustness checks for the assumptions underlying [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.