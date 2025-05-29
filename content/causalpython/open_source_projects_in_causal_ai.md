---
title: Open source projects in causal AI
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

The development and widespread adoption of open-source projects are crucial for advancing [[Causal AI and machine learning | causal AI]] and enabling broader application of its methods <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>, <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. By providing accessible tools and fostering collaboration, these initiatives help democratize [[Causal AI applications in various industries | causal analysis]] and integrate it into diverse decision-making processes.

## The DoWhy Library

The DoWhy library originated as a pedagogical example to educate more people about [[causal inference models and AI workshops | causal approaches]] <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>, <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>. Its primary driver was the desire to broaden the usage of [[causal AI and machine learning | causal analysis methods]] <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. The library highlights the importance of [[causal AI applications in business and technology | causal analysis]] in decision-making, which clarifies assumptions and identifies the limits of an analysis <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>, <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.

DoWhy is structured around four stages of causal analysis <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>:
1.  **Modeling and Assumptions**: Formulating causal models and their underlying assumptions <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
2.  **Identification**: Analyzing models to identify a causal estimand and determine an approach to answer a causal question <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
3.  **Estimation**: Performing statistical estimation to calculate values from data <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
4.  **Refutation/Validation**: Testing assumptions by attempting to refute them <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. This step is inspired by Karl Popper's philosophy of falsifiability, recognizing that while theories cannot be proven correct, data can contradict assumptions <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>, <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

Originally a pedagogical example, DoWhy grew to be more robust and practically useful, broadening its initiative with many contributors <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a>, <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

## The PyWhy Organization

The DoWhy library transitioned from being an open-source project under Microsoft's GitHub organization to an independent entity called PyWhy <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. This move was driven by the desire to foster a broader community around causal inference and allow other organizations to contribute <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.

Key collaborators in the PyWhy organization include:
*   Amazon <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>, <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>
*   MIT <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>
*   Columbia University <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>
*   Carnegie Mellon University, which contributed the Causal Learn package (a Python version of Tetrad algorithms) <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>, <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>, <a class="yt-timestamp" data-t="16:39:00">[16:39:00]</a>
*   Wise <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>

The collaboration of major market players like Microsoft and Amazon on a single [[open_source_contributions_in_causal_modeling | open-source tool]] is seen as inspiring and beneficial for empowering the community to make better decisions with [[causal AI applications in business and technology | causal analysis]] <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>, <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.

### Future Developments for PyWhy

A significant project for PyWhy is **PyWhy-LLM**, an experimental library focused on incorporating large language models (LLMs) into the causal analysis process <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>, <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>. The goal is to use LLMs to:
*   Generate causal graphs <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
*   Critique causal assumptions <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>.
*   Suggest potential missing data and confounders <a class="yt-timestamp" data-t="40:54:00">[40:54:00]</a>.
*   Potentially assist with identification-style analyses, such as identifying instrumental variables, and provide support for coding analyses <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>, <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>.

Additionally, there is interest in exploring how foundation models might assist in better modeling more complex, physics-style systems <a class="yt-timestamp" data-t="41:07:00">[41:07:00]</a>, <a class="yt-timestamp" data-t="41:10:00">[41:10:00]</a>.

## The Causal Python Community

The [[open_source_contributions_in_causal_modeling | causal Python community]] is considered healthy, with several libraries beyond PyWhy, such as CausalPy <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>, <a class="yt-timestamp" data-t="35:40:00">[35:40:00]</a>.

A key recommendation for the community is to remain focused on the end goal: solving real-world problems with [[causal AI applications in business and technology | causal analysis]] <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>, <a class="yt-timestamp" data-t="36:03:00">[36:03:00]</a>. This involves looking broadly at various approaches, including:
*   Deep algorithmic advancements <a class="yt-timestamp" data-t="36:16:00">[36:16:00]</a>.
*   Software engineering aspects to ease data ingestion <a class="yt-timestamp" data-t="36:22:00">[36:22:00]</a>.
*   Improved documentation <a class="yt-timestamp" data-t="36:32:00">[36:32:00]</a>.

### Challenges and Opportunities

One significant challenge in [[challenges_and_advancements_in_causal_ai | causal AI]] is making tools for partial identification, sensitivity analysis, and proximal learning more accessible <a class="yt-timestamp" data-t="37:42:00">[37:42:00]</a>. Many practitioners are unaware that sensitivity analysis might suffice for optimal decision-making even with partially specified models <a class="yt-timestamp" data-t="38:23:00">[38:23:00]</a>. Furthermore, even those who recognize its utility may lack the technical knowledge or time to implement these methods from scratch <a class="yt-timestamp" data-t="38:37:00">[38:37:00]</a>, <a class="yt-timestamp" data-t="38:52:00">[38:52:00]</a>.

DoWhy already incorporates a method for sensitivity analysis by Carlos Cinelli <a class="yt-timestamp" data-t="39:14:00">[39:14:00]</a>. Early work is also underway within the PyWhy ecosystem on graph representations for partial graphs, which could lead to a broader set of identification algorithms <a class="yt-timestamp" data-t="39:50:00">[39:50:00]</a>.