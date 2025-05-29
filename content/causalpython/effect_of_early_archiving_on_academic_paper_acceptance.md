---
title: Effect of early archiving on academic paper acceptance
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

This article discusses research by Yevgeniy Levental on the causal effect of early archiving (preprinting) on academic paper acceptance, particularly within the NLP community.

## Motivation and Research Question

The research aims to estimate the causal effect of archiving papers early on their acceptance rates <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. Historically, the NLP community, specifically conferences like ACL, maintained an anonymity period until very recently (from about 2017) <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. The core assumption behind this policy was to prevent more famous individuals or those with certain affiliations from gaining an unfair advantage when submitting papers to archives <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>, ensuring all papers received equal treatment during the acceptance decision process <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

The study sought to verify whether this anonymity assumption held true in practice <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Using observational data on paper acceptance, authors, and other variables, the researchers investigated if different groups experienced varying acceptance rates based on these factors <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

## Addressing Hidden Confounders

A significant challenge in this research was the presence of hidden confounders, such as "paper quality" <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
It could be hypothesized that:
*   Authors confident in the high quality of their work might pre-archive their papers to enable early dissemination <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   Conversely, those with papers of lesser quality might primarily submit to conferences to gain feedback and improve their work <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

To address this strong yet hidden confounder, the study utilized the negative control outcome framework <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This framework requires identifying another variable that shares the same confounders, such as paper quality <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. The chosen variable for this purpose was the number of citations a paper received after a certain number of years <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. By applying a difference-in-difference framework, researchers were able to de-confound the variable and estimate the exact effect of interest <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

## Key Results

The study's findings, subject to various setups and assumptions, were significant:
*   Initially, without accounting for the quality confounding factor, benefits of early archiving were observed <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   However, after employing the negative control outcome and difference-in-difference framework, the research showed there was "actually not much of an effect" <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   Even in cases where an effect was present, it was not statistically different across various groups, specifically those based on the number of citations and institution ranking <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. These groups were the primary reason for the initial anonymity period <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

A curious coincidence noted by the researcher was that the day their paper on these findings was accepted coincided with the day the anonymity period was removed from the NLP community <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## Impact and Future Work

The immediate impact of this work is reflected in the removal of the anonymity period in the NLP community <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. More broadly, the researcher emphasizes the importance of continually monitoring and checking if such issues (like bias due to early archiving) arise in practice <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

This specific project was a side endeavor <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. The researcher's general interests lie in the connection between data and model behavior, particularly regarding the interpretability of models through data <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. The hope is to see more work that fosters a better understanding of models and underlying mechanisms <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.