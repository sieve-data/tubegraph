---
title: Scott Muellers journey from computer science to causal AI
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

Scott Muller, a guest on the Causal Bandits podcast, shares his unconventional path from a computer science background and successful tech entrepreneurship to dedicating his full attention to studying [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. His journey highlights a deep-seated desire for fundamental understanding and a commitment to advancing [[advancements_in_causal_modeling_and_ai | causal modeling and AI]].

## Early Life and Education

During his high school years in Los Angeles, Scott Muller was a skilled tennis player <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. However, his passion for computers was stronger than his love for tennis <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. He pursued computer science for his undergraduate, master's, and Ph.D. degrees <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>, appreciating its mathematical nature and the joy of creating things through programming <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>.

## Transition to Tech and Business

After college, Muller declined an offer from a large tech company to join a startup <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The tech world was exciting, with the prospect of his software being widely used and making significant contributions <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. He eventually founded a successful business <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, which led to a series of other startups he founded or co-founded <a class="yt-timestamp" data-t="00:28:31">[00:28:31]</a>. This period shifted him from hands-on software development to a more business-oriented mindset <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>, though he never lost his love for coding, finding it therapeutic <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>. He ran a company, *Ucode*, that taught computer science to over 10,000 children and made significant impacts on their lives, which he found very fulfilling <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>.

## Shift to Academia and Causality

Despite his success in tech, Muller harbored a "deep hidden desire" to return to academia <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>, believing his brain was better suited for more mathematical and academic thinking <a class="yt-timestamp" data-t="00:31:48">[00:31:48]</a>. His decision was catalyzed by the growing impact of [[Causal AI and machine learning intersection | AI]] <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a> and the dream of achieving artificial general intelligence (AGI) <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>, which he believes could "change the world" by solving significant problems like cancer <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

While preparing to apply for graduate programs in AI, he discovered Judea Pearl's "Book of Why" <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>. Reading it was a "woke me up" moment <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>, as he realized his previous confidence in interpreting data and making business decisions based on high-level statistics was unwarranted <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>. He recognized he had likely made poor decisions in the past <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. This realization made him feel that understanding [[Causality in AI | causal thinking]] and counterfactual reasoning was fundamental to human reasoning and crucial for developing human-level AI <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.

## Focus on Causal AI and Decision Making

Muller's current research focuses on making better decisions at both individual and population levels using counterfactual reasoning <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. He highlights the "fundamental problem of causal inference," which states that one cannot observe outcomes for two different treatments on the same individual <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. While averages can be estimated at a population level (e.g., through randomized control trials) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, obtaining point estimates or identified probabilities for individual counterfactual outcomes is difficult <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

He references Jin Tian and Judea Pearl's work on bounds for counterfactual probabilities, such as probability of necessity and sufficiency <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Although these bounds are proven to be mathematically tight, they are often "too loose" to be useful for basing decisions <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. His challenge is to narrow these bounds, ideally to the point of identification, by exploring additional, reasonable assumptions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### The Monotonicity Assumption

One such assumption is **monotonicity** <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This assumption implies there is "no possibility of harm in the counterfactual sense" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For example, if a medicine is taken, it's assumed it won't prevent recovery if the person would have gotten better on their own without it <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. If this assumption holds, it allows for the point identification of probabilities like benefit, harm (which would be zero), necessity, and sufficiency <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

The main challenge in applying this method broadly is knowing if monotonicity truly holds <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Muller is working on a paper with Judea Pearl that explores how data can sometimes *disprove* monotonicity <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, which is much more feasible than proving its presence from data alone <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Even when monotonicity is violated, they propose methods to limit the extent of the violation, thereby narrowing the bounds on counterfactual probabilities further <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This process is akin to "putting a bound on the bound" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

### Practical Application of Causal AI

Muller emphasizes the importance of making theoretical findings accessible to practitioners <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. He plans to develop software applications and frameworks and contribute to [[open_source_causal_ai_libraries | open source causal AI libraries]] like *DoWhy* <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. He believes *DoWhy* could become the "scikit-learn of causal inference" <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>, providing a consistent API for various causal models and making it easier for people without coding expertise, such as those in marketing or epidemiology, to apply these methods <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

One key application is in improving upon traditional A/B testing in marketing through the **Unit Selection Framework** <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

#### Unit Selection Framework

The unit selection framework, created by Angley and Judea Pearl <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>, allows marketers to assign values to four different types of responders when showing an ad (treatment) to encourage a product purchase (response):
*   **Complier**: Buys if shown the ad, doesn't buy if not shown the ad <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. These are the desired targets for advertising <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Always Taker**: Buys whether or not shown the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Never Taker**: Does not buy whether or not shown the ad <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
*   **Defier**: Does not buy if shown the ad, but *would* buy if not shown the ad <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a> (e.g., ad is offensive or makes them reconsider) <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. Marketers definitely want to avoid advertising to defiers <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

While individual-level treatment effects cannot be identified, this framework, using observational and experimental data, can provide bounds on the overall value of advertising to a subpopulation <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>. This allows for better decision-making, even if precise point estimates are not available <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.

### Advancing AI with Causal Understanding

Muller believes that [[causal_discovery_and_inference_in_ai | causality]], with its established mathematics and science, "needs to be baked in" to machine learning architectures to achieve more intelligent AI <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. He remains optimistic that his expertise in causal inference can be applied to these architectures, noting that work is already underway in this area <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. This contributes to addressing the [[Challenges in developing AI with causal understanding | challenges in developing AI with causal understanding]].

## Influences and Mentors

Muller credits several people with profoundly influencing his life and career:

*   **Judea Pearl**: His Ph.D. adviser, whom he considers one of the "great minds" in history, on par with Isaac Newton and Albert Einstein <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. Muller feels incredibly lucky to work with him and highlights Pearl's amazing human qualities and entertaining personality <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.
*   **Clouse Schafer**: His computer science professor from undergraduate years, who later became an investor in two of Muller's businesses <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>. Schafer, a highly successful entrepreneur (founder of GoToMyPC and AppFolio) <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>, served as a mentor, providing resources, introductions, and valuable lessons, including managing "irrational exuberance" as an entrepreneur <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>.

## Advice and Philosophy

When asked for advice on persevering through challenges, Muller offers a nuanced perspective:
> "Sometimes you do want to stop, you do want to be derailed because you really are headed in a wrong direction" <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>.

He emphasizes that recognizing when to pivot or exit entirely is crucial, especially in business <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>. His main advice for decision-making in the face of obstacles is to "learn counterfactual analysis" <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>.

For academic challenges, he notes that hard problems can be "very interesting to solve" and are like "puzzles" <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. His personal approach is to find problems he feels confident he can solve and then not stop until he finds the solution <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>.

Scott Muller's work can be found on Judea Pearl's UCLA website, where most of their co-authored papers are listed <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>. He also maintains a presence on Twitter <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>.