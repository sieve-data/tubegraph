---
title: Challenges in causal inference and statistical analysis
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Dr. Stephen Senn, author of *Statistical Issues in Drug Development* and *Dicing with Death*, discusses various [[challenges_and_methodologies_in_causal_inference | challenges and methodologies in causal inference]] and statistical analysis, particularly within the context of clinical trials <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. He highlights misunderstandings about randomization, the limitations of trials, and practical considerations in research <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Randomization: Misconceptions and Reality

Dr. Senn notes that randomization, despite its importance, remains a controversial idea among statisticians and scientists <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The core of this controversy stems from a misunderstanding: critics often assume the goal of randomization is "perfect estimation" or that it will "perfectly balance" groups <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

However, as R.A. Fisher, who proposed randomization, realized, perfect estimation is impossible <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The true goal of randomization is to allow researchers to estimate *how imperfect* any estimate is <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Critics point out that when hundreds of factors could affect an outcome, randomization won't perfectly balance them, leading to bias in the estimate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Dr. Senn explains that this imperfection is accepted and accounted for in standard statistical analysis, which "allows for the fact that they will not be perfectly balanced" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Failure to grasp this leads to "endless tedious conversations" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Comparison of Trial Designs

Dr. Senn illustrates this point by comparing two common clinical trial designs:

*   **Parallel Group Trial**: The most common type, where patients are randomized to receive either a new treatment or a standard treatment (e.g., half receive new stroke prevention, half receive standard) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Each group serves as a "counterfactual group" for the other <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Crossover Trial**: Applicable to chronic, reversible diseases (e.g., asthma), where each patient can serve as their own control <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Patients receive one treatment for a period, then another, with the order randomized <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This approach balances for "20,000 genes, all life history to date," leading to "much narrower confidence intervals" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

The wider confidence intervals in parallel group trials reflect the inherent imbalance that randomization accounts for <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Five Questions in Randomized Trials

Dr. Senn outlines five levels of questions that randomized trials attempt to answer, progressively increasing in difficulty <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>:

1.  **Was there a difference between treatments in the trial?** (Was there a treatment effect?) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  **What was the average effect for the patients actually treated?** (What difference did it make to them?) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
5.  **What will it be like in future patients not in the trial?** (Generalizability outside the trial) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Dr. Senn notes that most statistical work is limited to answering questions one and two <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Answering question five, which involves future prediction, entails a degree of uncertainty not fully captured by formal statistical analysis <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The example of streptomycin for tuberculosis illustrates this: it was effective when discovered, but later became ineffective due to bacterial mutation <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This highlights [[challenges_of_causal_inference_and_counterfactual_thinking | challenges of causal inference and counterfactual thinking]] and the inherent contingency of predictions <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

## Practical Challenges in Clinical Trials

Clinical trials face numerous [[papers_on_practical_challenges_in_causal_research | practical challenges]]:

*   **Missing Counterfactuals**: In parallel group trials, the "alternative reality" for an individual receiving a different treatment is not observed <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Changing Circumstances**: Even in crossover trials, circumstances can change from occasion to occasion, making perfect control difficult <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Resource Constraints**: Financial and ethical limitations often prevent trials from being large enough to answer questions about subgroups (e.g., specific genders) with sufficient precision <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **Ethical Dilemmas**: Decisions by data safety monitoring boards involve balancing potential toxicities with uncertain future benefits, especially in serious conditions like cancer <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

Dr. Senn emphasizes that these are not just problems for clinical trials but for experimentation in general, citing examples from the automobile industry's need for accelerated life testing to predict long-term durability <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## History and Evolution of Experimental Design

Experimental design has a long history, formally theorized for over 100 years <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. R.A. Fisher's work at Rothamsted in 1919 on agricultural experiments, dealing with fertility gradients and correlation structures, was foundational <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. He developed methods to ensure that the estimate of error correctly reflected the variation, leading to valid standard errors <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. This led to designs like incomplete block designs and fractional factorial designs, which were further developed in industry from the 1940s <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. Clinical trials adopted these ideas relatively late <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

## Improving Efficiency in Experimentation

Dr. Senn points out a significant disconnect between theoretical optimal experimental design and practical application in medicine <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>. Optimal design theories are often "austere and beautiful" but fail to account for real-world constraints like patient recruitment rates or the order of treatment <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>.

He advocates for bridging the gap between statistical theory and practice. Regarding [[causal_inference_methods_and_applications | causal inference methods and applications]] and [[causal_inference_and_its_applications | causal inference and its applications]], he feels it's plausible that combining observational data sets and clinical trial data sets could yield more power, though current proposals have limitations <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. He emphasizes the need for better communication within statistics and between statisticians and other fields <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>.

## Statistical Analysis Practices

Dr. Senn identifies simple, yet often overlooked, ways to improve efficiency in clinical trials:

*   **Avoid Dichotomization**: Many clinical trials still dichotomize continuous data (e.g., "responders" vs. "non-responders"), which is "very wasteful and misleading" and leads to a huge loss of statistical power <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.
*   **Utilize Covariates**: Incorporating covariates (e.g., patient characteristics) into models can "get much greater precision [and] greater understanding" <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. While statisticians often underuse this ability, it's generally safe to include multiple covariates in large trials <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.
*   **Understand Model Specifications**: In nonlinear models (e.g., logistic regression), missing predictive covariates can lead to model misspecification and attenuation of the treatment effect estimate <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.

He points out a "contradiction in thinking" where researchers might balance covariates during randomization but then fail to fit them in the model <a class="yt-timestamp" data-t="01:16:51">[01:16:51]</a>. This highlights ingrained habits and a lack of understanding of the underlying data structure and relationships <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>.

## Communication and Intuition in Statistics

Dr. Senn stresses the importance of simple, understandable explanations when communicating statistical ideas to stakeholders <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>. He uses an analogy of a mother observing her children fighting to explain why an overall treatment effect can be detected without specific pairwise differences being significant <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>. He advocates for graphical methods over algebraic proofs when teaching complex concepts like regression to the mean <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.

For statisticians, he advises understanding concepts in at least two ways: mathematically and intuitively. "If you don't have the intuition that goes with the math, you don't understand it" <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

## Career Reflections and Advice

Dr. Senn believes his career in statistics, which he "came across by accident," was "pre-ordained" despite acknowledging that "most of anything that happens in life is luck" <a class="yt-timestamp" data-t="01:11:03">[01:11:03]</a>.

His advice for newcomers to advanced fields like statistics or [[causal_inference_concepts_and_applications | causality]] includes:

*   **Find concrete problems**: Work on specific problems to develop the habit of solving them <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.
*   **Look wider**: Explore other fields and borrow ideas, as seen in the development of N-of-1 trials from psychology to medicine <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.
*   **Embrace reality**: "Rub your noses in reality" to understand practical constraints and challenges <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>.