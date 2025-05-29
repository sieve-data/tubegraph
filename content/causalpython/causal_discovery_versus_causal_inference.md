---
title: Causal Discovery versus Causal Inference
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

Science is described as a non-linear process driven by the essence of exploration <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The notion of [[Causal Discovery and Analysis | causality]] is a key driver, not solely emerging from the modeling part <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This concept is central to the work at Spotify and Dr. Athanasios Bonos's PhD research <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Distinguishing [[Causal Discovery Algorithms and Techniques | Causal Discovery]] and [[Causal Inference and Identification | Causal Inference]]

Dr. Athanasios Bonos, a research scientist at the Advanced [[Causal Inference and Identification | Causal Inference]] Lab at Spotify, considers [[Causal Discovery Algorithms and Techniques | Causal Discovery]] a "better riddle" than [[Causal Inference and Identification | Causal Inference]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Core Differences
*   **Difficulty**: [[Causal Discovery Algorithms and Techniques | Causal Discovery]] is "plain and simple more difficult" <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Assumptions**:
    *   [[Causal Inference and Identification | Causal inference]] makes assumptions, such as knowing the Directed Acyclic Graph (DAG) and the causal relationship between variables (e.g., X causes Y) <a class="yt-timestamp" data-t="00:43:23">[00:43:23]</a>. While these assumptions are explicit and can be tested <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>, they might not span the entirety of known causal relationships, and mistakes in these assumptions can occur <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
    *   [[Causal Discovery Algorithms and Techniques | Causal Discovery]], in contrast, *tries to identify* these DAGs, figuring out if X causes Y, often informed by expert knowledge but inherently a very difficult task <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>.

### Why [[Causal Discovery Algorithms and Techniques | Causal Discovery]] is More Compelling
Dr. Bonos finds [[Causal Discovery Algorithms and Techniques | causal discovery]] more interesting and exciting because it involves discovering something unknown <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>. It aligns with the "true science" of exploration, whereas [[Causal Inference and Identification | causal inference]] is seen more as "applied science" or technology <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>.

> "[[Causal Discovery Algorithms and Techniques | Causal Discovery]] at the end of the day it is it is science either you want it or not it is the process that we do science we're trying to see if there is a causal link from X to y or from y to X we can try to make models out of it and try to formalize things that's great you can ENT have science derived from data wonderful sometimes it works sometimes it doesn't but like [[Causal Discovery Algorithms and Techniques | caal Discovery]] at the end of it I find it more interesting because it's more difficult and also it is true science the others is applied science it's technology but like it's exploration called Discovery you're trying to find out something you don't know and this is wonderful" <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>

## The Importance of Assumptions in Models
All models, whether [[Causal Discovery and Analysis | causal]] or not, are built on assumptions <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The key is to make these assumptions explicit, testable, and to understand when a model works or fails <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. While some assumptions can be relaxed (e.g., neural networks being more flexible than linear regression) <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>, others are sometimes forgotten, leading to problems <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

An example of a forgotten assumption is the Euclidean nature of latent spaces in deep learning models, which were later found to be high-dimensional Riemannian manifolds <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Challenging such assumptions has led to advancements like hyperbolic machine learning models <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

## [[Applications of Causal Inference in Science and Medicine | Applications]] and Practicality
[[Causal Discovery and Analysis | Causality]] plays a role across the entire system-building process, from data collection to modeling and robust implementation <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Medical Imaging
In medical imaging, the goal is to provide better tools for radiologists rather than replacing them with AI <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Radiologists perform complex decision-making based on associations between different observations, which deep learning systems cannot yet learn well <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. The medical field requires robust and trustworthy systems, especially given the life-and-death decisions involved and the associated legal and ethical considerations <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. [[Causal Discovery and Analysis | Causal learning]] and [[Causal Inference and Identification | causal inference]] could potentially help achieve this robustness <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### [[Causal Inference and decision making | Causal Reasoning]] in Product Development
People, regardless of their background in formal [[Causal Discovery and Analysis | causality]] frameworks (like Pearl or Rubin's potential outcomes), possess an innate understanding of [[Causal Discovery and Analysis | causality]] <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>. This innate understanding makes it easier to build products based on [[Causal Discovery and Analysis | causal concepts]] because people inherently appreciate the power of controlling for spurious correlations <a class="yt-timestamp" data-t="00:39:08">[00:39:08]</a>.

### Interdisciplinary Approaches
Working in diverse, interdisciplinary teams, such as the Advanced [[Causal Inference and Identification | Causal Inference]] Lab at Spotify, is crucial <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. Bringing together different expertises, like engineering, reinforcement learning, astrophysics, and quantum physics, fosters creativity and leads to unique results <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>. This approach has also been successful in projects like predicting ionospheric problems due to solar weather by combining machine learning, solar physics, and ionospheric physics <a class="yt-timestamp" data-t="00:36:15">[00:36:15]</a>.

## The Nature of Science and Exploration
Science is rarely a linear path; it involves many turns, twists, and explorations <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This "essence of exploration" is what drives discovery <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.

### Addressing Criticisms of [[Causal Inference and its applications | Causal Methods]]
Criticisms of [[Causal Inference and Identification | causal inference]], such as its reliance on assumptions or being in its "early years," are countered by pointing to decades of literature and practical [[applications_of_causal_inference_in_science_and_medicine | applications]] in econometrics and epidemiology <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. While models can fail (e.g., ChatGPT hallucinations) <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>, the key is to make assumptions explicit and understand the tool's appropriate use <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. [[Causal Inference and Identification | Causal inference]] is not a panacea but a valuable tool in many circumstances <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

### [[Causal Discovery Algorithms and Techniques | Causal Discovery]] as True Exploration
A compelling example of [[Causal Discovery Algorithms and Techniques | causal discovery]] comes from the SETI Institute, where impurities in the ionosphere around the equator that affect GNSS (like GPS) are not fully understood, unlike those around the poles <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. Discovering the new physical causal relationship for these equatorial impurities is an exciting challenge <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.

> "it is like that essence of exploration is really really captivating me" <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>

This innate human drive to understand the world, to push limits, and to explore is perfectly encapsulated in [[Causal Discovery Algorithms and Techniques | causal discovery]] <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>.

## Investing in [[Causal Research]]
If given a billion dollars for [[Causal Discovery and Analysis | causal research]], Dr. Bonos would invest:
*   **75% in [[Causal Discovery Algorithms and Techniques | Causal Discovery]]**: Efforts to apply [[Causal Discovery Algorithms and Techniques | causal discovery]] in every imaginable field of science and technology <a class="yt-timestamp" data-t="00:59:41">[00:59:41]</a>.
*   **25% in Education**: To help people realize what [[Causal Discovery and Analysis | causality]] is, become skeptical of spurious correlations, and think more logically about the world <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>. This would increase the burden of proof and decrease mistakes in society <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>.

## Learning [[Causal Inference concepts and applications | Causality]]
For those interested in learning [[Causal Discovery and Analysis | causality]], Dr. Bonos recommends:
*   **Reading**: Textbooks, medium articles, and blog posts provide foundational knowledge <a class="yt-timestamp" data-t="01:05:57">[01:05:57]</a>.
*   **Doing**: The most effective way to learn is by picking up small projects and experimenting to see how different approaches (e.g., associational vs. [[Causal Discovery and Analysis | causal]]) yield different results <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>.