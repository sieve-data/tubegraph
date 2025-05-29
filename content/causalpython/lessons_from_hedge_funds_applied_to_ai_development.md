---
title: Lessons from Hedge Funds Applied to AI Development
videoId: pKhUuwxBdX4
---

From: [[causalpython]] <br/> 

The founding of Cal Bandits in 2017 emerged from a period when causal AI was considered a very niche topic, and the community felt "very lonely" <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Despite this, there was a conviction from day one that it would eventually become significant, leading the founders to lay foundations to support the community when it grew exponentially, as it has by 2023 <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

## A Contrarian Bet on Causal AI

The decision to pursue causal AI was a "contrarian bet" <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. Both the speaker and co-founder Max had backgrounds in hedge funds before starting Cal Bandits; the speaker as a computer scientist and Max as a physicist <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

At the time, the AI community was highly enthusiastic about deep learning, especially after AlphaGo beat the world champion at Go, leading many to believe deep learning would solve everything <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. However, the founders held a contrarian view, recognizing that while deep learning excelled in fixed-rule environments like board games <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>, it could lead to trouble in the real world by merely learning historical patterns <a class="yt-timestamp" data-t="02:07:10">[02:07:10]</a>. This challenge is relevant to [[developing_effective_machine_learning_models]].

### Key Lessons from the Hedge Fund World

Working in the hedge fund world provided two fundamental lessons that guided their shift to causal AI:
1.  **The Nature of Real-World Patterns**: In financial markets, historical patterns rarely repeat, and relying solely on correlations can be misleading <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This highlighted that the past is not necessarily predictive of the future in dynamic real-world scenarios <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This insight is critical for understanding [[causality_and_ai_challenges_and_opportunities]].
2.  **The Value of Contrarian Views**: To achieve significant success, it's often necessary to take a contrarian view rather than follow what everyone else is doing <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. The founders realized that being "contrarian and right" was key to unlocking substantial gains <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. For them, causal AI proved to be a "contrarian bet that was right and is becoming more right by the day" <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>, aligning with [[trends_in_causal_ai]].

## The Real-World Performance Gap of AI

The speaker's PhD work in computer vision, specifically biometrics, further reinforced these lessons. While deep learning models performed exceptionally well in the lab due to consistent backgrounds and abundant data, they "catastrophically" broke down when deployed in the real world <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. This common issue, where 85% to 90% of AI projects never make it out of the lab, stems from their failure to generalize to diverse, real-world conditions <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. This challenge is at the heart of [[translating_ai_methods_for_practical_use]].

In contrast, a model-based approach, which involved understanding the inherent structure and cause-and-effect mechanisms (e.g., how body parts move in biometrics, or 3D face shapes in face recognition), demonstrated better generalization. Although these models had slightly worse performance in controlled lab settings, they "retained their performance" in the real world <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

This experience solidified the belief that to successfully transition AI from the lab to the real world, two crucial problems must be solved:
1.  Ensuring the AI system will function effectively in varied real-world conditions <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
2.  Building trust with human users by ensuring they understand how the AI works and the causal model behind its decisions <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

## Causal AI in Practice: A Manufacturing Example

A concrete application showcasing these principles involves a client modeling a physical manufacturing system with a true cause-and-effect reality <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>. Initially, the client attempted to solve the problem with deep learning, which performed well in the lab but failed catastrophically when applied to the real manufacturing line because real-world conditions differed from the training data <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>. Even after engaging six deep learning companies, their senior leadership could not understand or trust the models because they couldn't explain the "real-world connectivity" within the machine <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.

Upon trying causal AI, specifically automated causal discovery, a "digital twin" of the machine was generated <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. This proposed causal diagram was then presented to domain experts, who could validate its accuracy and even insert missing causal links that the algorithm hadn't detected due to a lack of historical faults in specific machine parts <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. This iterative process, involving human experts from the very beginning, distinguishes causal AI from deep learning and generative AI, where data is simply fed into a model with less initial human input <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.