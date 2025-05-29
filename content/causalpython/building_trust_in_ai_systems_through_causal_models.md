---
title: Building Trust in AI Systems Through Causal Models
videoId: pKhUuwxBdX4
---

From: [[causalpython]] <br/> 

Calends was founded in 2017 with a focus on [[causal_ai_and_machine_learning | Causal AI]], which at the time was a very niche topic <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The early experience of building this community felt "very lonely" <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, but there was a strong conviction from the start that it would grow significantly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. By 2023, the community is indeed growing exponentially, with support for real-world success stories <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## The Contrarian Bet on Causal AI

The decision to pursue [[causal_ai_and_machine_learning | Causal AI]] was a "contrarian bet" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Both co-founders, including Max, came from the hedge fund world <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

At the time of Calends' inception, around 2017, the AI community was highly enthusiastic about deep learning, especially after breakthroughs like AlphaGo beating the world champion at Go <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Many AI researchers were pivoting their efforts towards deep learning, believing it would solve everything <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

However, the co-founders held a contrarian view:
*   Deep learning is excellent for specific situations, like board games with fixed rules <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   In the real world, relying solely on learning historical patterns (correlations) can lead to problems, as observed in the hedge fund world where the past rarely repeats in financial markets <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   A key lesson from hedge funds is that significant success comes from taking a contrarian, yet correct, view <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   [[causal_ai_and_machine_learning | Causal AI]] proved to be a contrarian bet that was right, and is becoming "more right by the day" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

These experiences highlighted two critical lessons: the dynamic nature of real-world patterns (the past is not necessarily predictive of the future) and the value of contrarian bets <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Why Causality? Lessons from Computer Vision

The journey into causality was also influenced by experiences in computer science, specifically during PhD research in computer vision focused on biometrics (recognizing things at a distance with cameras) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

In the lab, deep learning models showed excellent performance because the background and conditions were controlled and consistent <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. However, when these deep learning models were deployed in the real world, they experienced "catastrophic" breakdown, not just small deteriorations <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

A model-based approach, which inherently incorporates understanding of cause and effect (e.g., how body parts move, 3D face shapes and eye placement), showed slightly worse performance in the lab but retained its performance remarkably well in the real world <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This highlighted that without a model and understanding of cause-and-effect mechanisms, real-world generalization is severely limited <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### The Enterprise Challenge

Today, in the enterprise, 85% to 90% of AI projects never make it out of the lab <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This is because:
1.  Incredible lab results fail in the field <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  Humans using the algorithms do not trust them because they don't understand the underlying [[generative_ai_and_causal_models | causal model]] <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

To successfully transition AI from the lab to the real world, two things must be solved:
1.  Ensuring the AI works reliably in real-world conditions <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
2.  Building human trust and understanding of how the AI operates <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

[[causal_ai_and_machine_learning | Causality]] helps achieve both <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

## Real-World Application of Causal Models

A concrete example involves a recent client modeling a physical system, like a manufacturing process or a device within a machine, which inherently has a true cause-and-effect reality <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. In such systems, there are clear causal links (e.g., one cog moving causes another to move) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

This client initially tried to solve the problem with deep learning, throwing a lot of data at it. While it worked well in the lab, it "failed catastrophically" in the real world because the real-world conditions differed from the lab data <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. They then engaged six deep learning companies, achieving some performance improvement, but senior leadership lacked understanding and trust because the models couldn't explain the real-world connectivity of the machine <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. They were close to abandoning AI entirely <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Upon discovering [[causal_ai_and_machine_learning | Causal AI]]:
1.  They applied automated causal discovery on their data <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
2.  This process helped discover a "digital twin" of the machine <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
3.  The proposed causal diagram was then presented to human domain experts <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
4.  The humans could validate the diagram, identifying correct and incorrect causal links based on their deep understanding of the machine (e.g., a missing link because a fault never occurred there, so the algorithm couldn't detect it) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. They were able to insert missing causal links themselves <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

This highlights the iterative nature of [[Causal AI and machine learning | causal discovery]], where humans are involved from the very beginning, unlike deep learning or [[Generative AI and Causal Models | generative AI]] where data is simply fed to a model <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This process typically involves a few rounds of expert knowledge, algorithm processing, and expert consultation before building the final causal model <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Origins and Inspiration

A strong desire to "make an impact" and "help people have a better life" has been a guiding principle since childhood <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. An early entrepreneurial venture involved building and selling ultrasound devices to chase mosquitoes, inspired by a cousin <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This experience taught lessons about product building and the importance of payment terms <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

The transition to software was motivated by the realization that it offered a much faster and more scalable way to make an impact compared to soldering physical devices <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Learning to code in Pascal and Delphi opened up a new world of "software that is going to change the world" <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The cousin served as a very important role model, highlighting the crucial role of mentors in formative years <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Advice for Getting Started with Causal AI

For those starting with [[causal_ai_and_machine_learning | causality]] and feeling overwhelmed:
*   **Be confident**: [[causal_ai_and_its_connection_to_machine_learning | Causal AI]] is now accessible <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   **Read "The Book of Why"**: This book is incredibly important for foundational causal theory and understanding terminology <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Play with open-source tooling**: Many new [[causal_ai_and_machine_learning | causal packages]] are emerging with great examples <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. Calends plans to open-source some of its algorithms and make its enterprise platform free or community-accessible to ease this journey <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
*   **Read relevant blogs**: There are great blogs available for learning <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   **Attend the Causal AI conference**: This community event is designed for learning and connecting without sales or marketing <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

## The Future: Integrating Generative AI and Causal AI

While some believe [[Generative AI and Causal Models | generative AI]] is the future, [[causal_ai_and_machine_learning | Causal AI]] will also play an important role in developing intelligent and decision-making systems <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

The key lies in combining these technologies. Both [[Generative AI and Causal Models | generative AI]] and [[causal_ai_and_machine_learning | Causal AI]] are powerful for different things, and combining them leads to a synergistic effect where "1 + 1 equals 3" <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. There's a huge, largely unexploited potential in their combination <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

While these are great building blocks, more will be needed to reach Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. The next step involves combining [[The Evolution of AI Technologies Deep Learning vs Causal AI | these two technologies]] to identify where gaps remain, requiring new theories and research <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. Even with just [[Causality Robustness and Fairness in AI Models | causal AI]] and [[Generative AI and Causal Models | generative AI]], significant progress can be made <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

A current significant gap is the "lack of harmonization" of [[causal_ai_and_its_connection_to_machine_learning | causal packages]] <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. A unified interface, similar to Scikit-learn for machine learning, is needed for [[Causal inference models and AI workshops | causal discovery]], causal modeling, and decision intelligence engines <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. Calends aims to contribute to this by open-sourcing its interfaces to help unify the community and accelerate adoption <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.