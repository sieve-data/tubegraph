---
title: Overfitting and test set considerations
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

In the context of the Wordle-solving algorithm, a significant discussion point arises around the concept of overfitting to a test set <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Overfitting Defined in Wordle Context

When developing an algorithm to solve Wordle, one approach involves using the official list of all possible answers <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This method is likened to "overfitting to a test set" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The alternative, and generally preferred, approach is to build a more resilient algorithm that doesn't rely on this specific list <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. A resilient algorithm, for example, might consider [[modeling_probabilities_based_on_limited_data | relative word frequencies]] in the English language to estimate the likelihood of a word being a final answer <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Purpose of Shameless Overfitting

Despite the drawbacks, the Wordle problem explored in the video "shamelessly overfits to the test set" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> to find the absolute best possible performance <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This means:
*   The algorithm directly incorporates the official Wordle answer list <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   It operates with certainty about which words are included in the answer list <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   A uniform probability is assigned to each possible answer <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   To determine the likelihood of seeing a particular pattern from an opening guess, the algorithm counts how many of the possible answers produce that specific pattern <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

This "shameless overfitting" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a> is a method to achieve the theoretically optimal score for that *specific* list <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Consequences and Limitations

The high degree of overfitting has significant implications:
*   **Vulnerability to Change** Should the New York Times, or whoever maintains the game, alter the official answer list, all the derived optimal strategies would become irrelevant <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Inapplicability to Human Play** This overfitted approach is not practical for human players <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Humans do not memorize the entire word list or perform exhaustive searches <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Human intuition, focusing on elements like vowel placement, differs greatly from how these algorithms operate <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The purpose of such algorithmic analysis is not to influence human play, but to hone skills in algorithm design for other contexts <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.