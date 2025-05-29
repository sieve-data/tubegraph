---
title: Challenges of working with healthcare data and practitioners
videoId: Q7sinHrknC8
---

From: [[causalpython]] <br/> 

Working with healthcare data and collaborating with medical practitioners in the field of causal inference presents unique and significant challenges. These challenges range from the inherent nature of the data itself to the expectations and understanding of domain experts <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.

## Data Preparation Complexities

A primary hurdle in applied causal inference, particularly in healthcare, is the complex process of transforming raw data into a format suitable for analysis <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

*   **Data Purpose Mismatch** Healthcare databases, such as insurance claims or electronic health records (EHRs), are typically not created with research or causal analysis in mind <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. They serve different purposes, like audits, and must be repurposed for research, which is a difficult task <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
*   **Structural Requirements for Causal Analysis** To perform a causal inference analysis, data needs to be structured into matrices of covariates, treatments, and outcomes <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. This requires significant knowledge of causality to properly organize the data <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
    *   **Covariate Selection and Timing** Researchers must determine which covariates to adjust for and ensure they are captured at specific points in time, ideally before the treatment occurs <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
    *   **Outcome Definition and Time Zero** Establishing the follow-up time for outcomes and defining a clear "Time Zero" for the intervention are also critical and complex steps <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   **Need for Automation** There is a recognized need for tools that can automate the preparation phase, allowing researchers to more easily reshape existing event-based databases into a format consumable by causal inference machinery <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. Such solutions would provide a greater leap in making causal inference more accessible than new methodological packages <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

## Bridging the Gap with Domain Experts

Effective collaboration with medical practitioners is crucial, but it involves navigating communication barriers and differing perspectives <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>.

*   **Understanding the Domain** Before even looking at data, it is essential to deeply understand the domain through interviews with experts like doctors and physicians <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This helps in setting up the problem, understanding the questions to be answered, and identifying the complexities involved <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
*   **Distilling Knowledge into Causal Models** Extracting knowledge from domain experts and distilling it into a sensible representation, such as a directed acyclic graph (DAG), is challenging <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. Physicians often have a better understanding of the treatment decision process than what determines an outcome <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>. They can identify "fuzziness" (variability) in treatment decisions that can be leveraged for causal modeling <a class="yt-timestamp" data-t="00:22:43">[00:22:43]</a>.
*   **Communication Challenges** The interaction requires careful listening and conveying information, as practitioners may describe complexities (e.g., specific patient types receiving different treatments) that indicate crucial covariates needed for adjustment <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
*   **Passion as a Driver** Despite the challenges, working with deeply ingrained domain experts is rewarding due to their passion for solving real problems, which strongly drives good work <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

## Managing Expectations and Misconceptions

Practitioners often approach causal inference with expectations shaped by popular media and the general perception of machine learning, leading to potential disappointment <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

*   **"Bait and Switch" Perception** Experts may arrive excited about using specific tools (like `causal_lib`) to "get some causal effects" <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. However, when discussions turn to theoretical concepts like causal roadmap, target trial emulation, time zero, and self-inflicted biases, their engagement can drop <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. This can feel like a "teaching session" rather than the expected "easy solution" <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.
*   **The Deep Learning Revolution's Impact** The rise of deep learning, particularly post-2012, instilled the idea that one can simply input raw data and "let the model figure it out" <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>. This contrasts sharply with causal inference, where "identification cannot be automated" and always requires metadata and rigorous understanding of the underlying data generating processes <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
    *   This expectation makes it harder for causal inference practitioners to "sell" the importance of carefully thinking about input data, variable selection, and temporal relationships <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.
*   **Debiasing and Conceptual Understanding** It's crucial to explain that while the underlying machinery might be a regular machine learning model, causal inference software makes "counterfactual prediction explicit," helping users conceptually grasp the difference from standard regression <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

## The Importance of Data Respect

There is a significant [[the_importance_of_process_and_data_in_generating_insights | challenge_of_implementing_causality_in_research_and_industry | ethical and practical issue]] in how data is treated, especially given the effort and hope invested in its collection <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>.

> "They spend millions of dollars Gathering data recruiting patients recruiting healthy controls taking measurements some of the measurements are done by doctors by physicians that's they bring them for days and they measure them it's it's an entire operation and they capture all those all these data and when the time comes they treat it like junk they don't respect the data generating process they do a T Test in some sense now they were not taught anything better than that but it's it's somehow it's lazy and it's ineffective it's it's a waste of money to gather all that data but not to analyze it properly and it's also I think it's like it's disrespectful to the patients who gave their time and their hope and thinking like things might be better like they will be the ones who will help make things better and then like being used uh for a T Test even though repeated binary measures in some sense" <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>

Proper data analysis, which prioritizes science and thoughtful application of statistics over automatic adherence to standard machinery, is essential to honor the data and the patients who provided it <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>.

## Advice for New Causal Inference Researchers

For machine learning researchers transitioning into causal inference, the hardest part is understanding "identification" and recognizing that the "kitchen sink approach" (feeding raw data and letting the model figure it out) does not apply <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. They must grasp that each problem has a unique structure that needs to be respected <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.