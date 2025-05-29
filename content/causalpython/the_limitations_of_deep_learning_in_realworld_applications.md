---
title: The limitations of deep learning in realworld applications
videoId: pKhUuwxBdX4
---

From: [[causalpython]] <br/> 

While deep learning has achieved remarkable feats in controlled environments, its application in dynamic, real-world scenarios presents significant [[challenges_of_machine_learning_integration_in_business | challenges]]. The core limitation often stems from its reliance on learning historical patterns without a fundamental understanding of cause-and-effect mechanisms <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

## Contrarian View on Deep Learning's Efficacy

Initially, the AI community was captivated by successes like AlphaGo beating the world champion at the game of Go, leading many to believe that deep learning would solve everything <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. However, a "contrarian view" recognized that while deep learning excels in situations with fixed rules, like board games <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, its effectiveness diminishes significantly in the real world <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.

## Lessons from the Hedge Fund World

Experience in hedge funds highlighted a critical flaw: solely relying on correlations or historical patterns is unreliable in financial markets, where the past almost never repeats itself <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. This environment underscored how learning historical patterns can lead to trouble when applied to unpredictable real-world situations <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

## Catastrophic Failures in Computer Vision

Further evidence of deep learning's limitations emerged from practical experience in computer vision, specifically in biometrics. While deep learning models demonstrated "incredible performance" in lab settings, where backgrounds and conditions were consistent and more data consistently improved results <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>, they "broke down catastrophically" when deployed in the real world <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. This stark contrast revealed that deep learning's performance was not generalizing beyond controlled environments <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

## Enterprise Adoption Challenges

This pattern of lab success and real-world failure is a widespread issue in the enterprise sector. Depending on the statistics, an estimated 85% to 90% of AI projects never make it out of the lab <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. The fundamental reasons are twofold:
1.  **Failure to Deliver:** The algorithms often do not work as expected in diverse, real-world conditions <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
2.  **Lack of Trust:** Humans using these algorithms often do not trust them because they do not understand the underlying causal model or mechanisms <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.

### Case Study: Manufacturing Process

A concrete example from a client modeling a physical manufacturing system illustrates these points:
*   The client initially applied deep learning, feeding it vast amounts of data. This approach "worked really well in the lab" <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   However, upon real-world deployment, the system "failed catastrophically" because conditions outside the lab differed significantly from the collected data <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   Even after consulting six deep learning companies, while performance improved somewhat, senior leadership still couldn't understand or explain the real-world connectivity of the machine to the deep learning model <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.
*   This led them to abandon AI altogether, believing it would "never going to work" <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.

This highlights the [[challenges_in_developing_ai_with_causal_understanding | challenges in developing AI with causal understanding]] using traditional deep learning.

## Addressing Limitations with Causal AI

The critical difference is that deep learning often operates as a "black box" where you "just throw a lot of data and you have a model and then you know good luck" <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>. Conversely, approaches like causal AI emphasize understanding the "cause and effect mechanisms" <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a> and involve human experts from the very beginning of the model-building process <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. This ensures models are generalizable to real-world conditions and are trusted by users.

## The Future: Combining Generative AI and Causal AI

Looking ahead, it is clear that [[large_language_models_llms_learning_limitations | large language models LLMs learning limitations]] exist when used in isolation. The future of AI likely lies in combining strengths. Generative AI is "amazing for certain things," and causal AI is "really amazing with other things" <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>. The true potential lies in combining these technologies, where "1 + 1 equals 3," leading to a largely "unexploited potential" <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. While more building blocks may be needed, integrating these two approaches is a crucial first step toward more robust and trustworthy intelligent systems <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>.