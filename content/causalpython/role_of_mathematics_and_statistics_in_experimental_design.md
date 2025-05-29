---
title: Role of mathematics and statistics in experimental design
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Experimental design is a critical field that leverages both mathematics and statistics to ensure robust and interpretable results, particularly in complex areas like clinical trials. The history of this field shows a continuous evolution, integrating theoretical advancements with practical applications.

## Foundational Concepts and History

Experimental design aims to achieve valid and precise estimates, especially when perfect control over all factors is impossible <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The field has a long history, with formal theory dating back at least 100 years <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

### Origins in Agriculture
Modern experimental design gained significant impetus with R.A. Fisher's arrival at Rothamsted in 1919, where he began working on agricultural experiments <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. These experiments were complex, involving fertility gradients in fields and correlation structures where closer soil pieces yielded similar results <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. Fisher quickly realized the need to ensure that contributions to the estimate of error accurately reflected how variations would affect differences between treatments <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. This led to the development of valid standard errors <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.

Further developments included:
*   **Incomplete block designs:** Where not all treatments could be compared in the same block <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **Fractional factorial designs:** For comparing many treatment combinations when experimental material is limited, by assuming higher-order interactions are not important <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.

### Industrial Applications and Modern Frameworks
The principles of experimental design were further developed in industry starting around the 1940s <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. Clinical trials adopted these methodologies relatively late <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. A key milestone was John Nelder's 1965 development of a front-end way of thinking for linear models, which could dictate the analysis of an experiment based on its blocking and treatment structures, ensuring correct standard errors <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

## The Role of Statistics in Experimental Design

### Randomization and Estimation
Randomization, proposed by R.A. Fisher, is a core principle in experimental design. Its purpose is not to achieve perfect balance or estimation, but to allow for the estimation of how imperfect any estimate is <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Critics often misunderstand that randomization does not perfectly balance all factors, leading to perceived bias <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. However, statisticians acknowledge and account for this imbalance in their estimation of error, meaning standard analyses are designed to allow for imperfect balance <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Types of Clinical Trials
Experimental design is crucial in clinical trials, with common types including:
*   **Parallel Group Trials:** The most common design, where patients are randomized to receive either a new treatment or a standard treatment. Each patient receives only one treatment <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This design acts as a way of estimating a counterfactual, as one group substitutes for what would have happened to the other group under different conditions <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Crossover Trials:** Used for chronic diseases where treatments are reversible. Patients receive both treatments sequentially, with the order randomized <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. In crossover trials, each subject serves as their own control, balancing for numerous individual factors (e.g., 20,000 genes, life history), which leads to much narrower confidence intervals compared to parallel group trials <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Statistical Modeling and Covariates
Statistical models play a key role in analyzing trial data. One important aspect is the use of covariates. In a linear model, fitting a predictive covariate can reduce the mean square error, leading to narrower confidence intervals and greater power <a class="yt-timestamp" data-t="00:45:16">[00:45:16]</a>. Although non-orthogonal covariates can slightly inflate variance, this effect is usually small in large trials <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. Loss of degrees of freedom is another consideration, but its impact lessens with larger sample sizes <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.

In nonlinear models (e.g., logistic regression), covariates can prevent attenuation of the treatment estimate, as missing predictive covariates can lead to model misspecification <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>. The penalty for loss of orthogonality remains consistent across different model types <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.

### The Five Questions of Clinical Trials
A presentation titled "Seven Myths of Randomization," based on an earlier paper called "Added Values," outlines five key questions randomized trials can address:
1.  **Was there a difference between treatments in the trial?** (Was there an effect of treatment?) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  **What was the average effect for the patients actually treated?** (What difference did it make to them?) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>
5.  **What will it be like in future patients not in the trial?** <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Statisticians often focus on questions one and two, with occasional ability to address question three. Meaningful statements about subgroups (question four) are rare, and question five, which involves prediction into the future, carries an inherent degree of uncertainty not fully captured by formal statistical analysis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. The future holds surprises, as illustrated by streptomycin's changing effectiveness against tuberculosis due to bacterial mutation <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## The Role of Mathematics

Mathematics provides the formal framework for statistical theory. Fisher, though sometimes underestimated as a mathematician, used a form of mathematics that relied heavily on geometrical intuition and rigorous geometrical proofs, rather than the formal algebraic proofs that later became prevalent <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

Linear algebra is fundamental to understanding statistical models, particularly in concepts like linear combinations of cells in experimental designs <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>. Understanding the underlying mathematical structure, such as how weights in a linear combination behave to eliminate patient or period effects in a crossover trial, is crucial for deep comprehension of experimental designs <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.

## Challenges and Limitations

### Practical Constraints
Real-world application of experimental design faces practical constraints, such as recruiting sufficient numbers of specific patient demographics within reasonable timelines <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For instance, if a disease affects two men for every woman, achieving equal precision for both sexes would significantly lengthen trial duration <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>. Financial and ethical considerations also limit the scope of trials <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### Data Quality and Assumptions
[[data_preparation_for_causal_analysis | Data preparation]] is vital. Data collected for official purposes may not be as "innocent" as they seem, often having underlying stories (e.g., population figures recalibrated after a census) that must be understood for proper use <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>. In observational studies, unobserved processing factors (e.g., different labs processing different groups) can introduce bias that is inherently designed out of double-blind randomized clinical trials <a class="yt-timestamp" data-t="01:18:47">[01:18:47]</a>.

### Communication Gaps
There is a need for better [[communication_between_statisticians_and_industry_professionals | communication between statisticians]] and practitioners in other fields <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>, and even within different "ghettos" of statistics <a class="yt-timestamp" data-t="00:57:03">[00:57:03]</a>. Theoretical optimal experimental design, though mathematically beautiful, can be impractical if not considering real-world constraints such as patient recruitment timelines or the impossibility of reaching final doses in dose escalation studies <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

## Improving Efficiency and Understanding

To enhance efficiency in clinical trials, simple modeling steps can be implemented:
*   **Avoid dichotomizing data:** Dichotomization (e.g., responders/non-responders) is wasteful and misleading, leading to significant loss of statistical power and requiring much larger sample sizes <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.
*   **Utilize covariate information:** Including covariates can increase precision and understanding <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. It is contradictory to balance for covariates during randomization but then not include them in the model <a class="yt-timestamp" data-t="01:16:39">[01:16:39]</a>.

These methods often rely on theory that is a century old, yet their widespread adoption is resisted <a class="yt-timestamp" data-t="01:15:53">[01:15:53]</a>.

## Influential Works

For those seeking to bridge the gap between theoretical causality and practical limitations, "Statistical Issues in Drug Development" by Steven Sen offers insights into practical issues in pharmaceutical clinical trials <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>. For industrial experimentation, "Box, Hunter, and Hunter" is recommended for its blend of theory and practice <a class="yt-timestamp" data-t="01:04:16">[01:04:16]</a>.

Understanding statistics requires both mathematical grounding and intuition. Concepts should be explainable through simple stories or graphical methods to foster understanding, rather than relying solely on algebraic proofs <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.