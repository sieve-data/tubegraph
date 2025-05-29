---
title: Impacts of early archiving on paper acceptance
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

Research by Y. Lahav from the Allen Institute for AI and the University of Washington investigates the causal effect of early archiving (preprints) on paper acceptance rates <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

## Motivation for the Study
The motivation for this research stems from the practice in the NLP community (and similar fields) of maintaining an anonymity period, which was in effect from approximately 2017 until very recently <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>, <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. The primary reason for this policy was to prevent authors with certain affiliations or more famous individuals from gaining an advantage in paper acceptance decisions by putting their work on arXiv before the review process <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>, <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. The study aimed to empirically verify whether this assumption of equal treatment held true in practice <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Methodology
The study utilized observational data from papers, including information on acceptance, authors, and various other variables <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. The core challenge was addressing hidden confounders, most notably "paper quality" <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. It's plausible that authors highly confident in their high-quality work would opt for early archiving, whereas those with potentially lower-quality papers might submit solely for feedback <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

To de-confound this effect, the researchers employed a framework called "negative control outcome" <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This method requires identifying another variable that is subject to the same confounders, such as "paper quality," but is not directly influenced by the treatment (early archiving) in the same way as the primary outcome (acceptance). For this study, the number of citations a paper received after a certain number of years was used as the negative control outcome <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. By combining this approach with a "difference in difference framework," they were able to estimate the causal effect of early archiving <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

## Key Results
The findings revealed distinct outcomes depending on how confounding factors were addressed:
*   **Without Confounder Adjustment**: Initially, without accounting for the "quality" confounder, the analysis suggested that putting a paper on arXiv early did offer benefits in terms of acceptance <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   **With Confounder Adjustment**: After applying the negative control outcome and difference in difference framework, the study concluded that there was "not much of an effect" of early archiving on paper acceptance <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. Even in instances where an effect was observed, it was not statistically different between groups based on the number of citations or institutional ranking, which were the original concerns leading to the anonymity period <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Coincidence**: Coincidentally, the day the paper was accepted was also the day the anonymity period was removed from the AI community <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## Real-World Impact
Y. Lahav believes this work highlights the importance of continued monitoring of such practices and assumptions within academic communities <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. More broadly, the researcher is interested in the connection between data and model behavior, and the interpretability of models through data <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. This work contributes to a better understanding of underlying mechanisms in data and model interactions <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.