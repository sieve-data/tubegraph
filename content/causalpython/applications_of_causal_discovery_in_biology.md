---
title: Applications of Causal Discovery in Biology
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

Dr. Robert Ness, a Senior Researcher at Microsoft Research, has an academic background rooted in economics that gradually shifted towards computation and ultimately [[causal_inference_methods_and_applications | causal inference]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. His interest in modeling natural phenomena led him to pursue systems biology over financial markets during his PhD, an experience that significantly shaped his understanding of causality <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Transition to Systems Biology

Ness was drawn to systems biology because of its connection to natural science, where there is a "ground truth in reality" that models aim to approximate <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This contrasted with financial markets, which he felt "lacked a certain type of anchor in reality" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His work in computational biology and systems biology introduced him to the challenge of using structure learning, or [[causal_discovery_algorithms | causal discovery algorithms]], to reconstruct biological pathways, such as signal transduction pathways, from single-cell data <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Single-cell data provided sufficient "degrees of freedom" to apply these algorithms and approximate biological realities <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Challenges in Applying Causal Discovery to Biological Data

One of the primary challenges in this field was building something practically useful for biologists <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. [[Causal Discovery and Analysis | Causal discovery]] involves inferring the causal properties of a system from data, typically by learning the structure of a Causal Directed Acyclic Graph (DAG) <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. With the explosion of molecular biology measurement technologies that produced large, rich datasets, it became easy to generate a graph using a [[causal_discovery_algorithms | causal discovery algorithm]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. However, the crucial question was "then what?" <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Biologists generally don't just want a DAG; they seek to use it for practical applications like discovering new biomarkers, aiding drug discovery, or understanding previously unknown signaling pathways <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

Initially, evaluating the correctness of a discovered structure involved comparing the learned graph to a known "ground truth" graph using metrics like precision-recall or structural Hamming distance <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This method is only useful when the ground truth is available <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Bayesian Experimental Design as a Solution

To address the practical utility gap and the challenge of evaluation without ground truth, Ness advocated for Bayesian experimental design methods <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This approach focuses on incorporating prior knowledge about the system's structure and dealing with uncertainty <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. The DAG itself becomes an intermediate step towards a final outcome, such as guiding experimental design questions (e.g., "what should I measure? how much?") within a sequential workflow for laboratory settings <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This allows for guarantees that, with more data, the process moves towards the correct answer, even if the absolute ground truth is unknown <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Causal Discovery in Probabilistic Programming

Dr. Ness also contributed to bridging the gap between causal inference and probabilistic machine learning, particularly through a paper with S. Mohammad Taheri and Karen Sachs <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. This work demonstrated that if an intervention distribution is identifiable using the rules of "do-calculus" or other graphical identification frameworks, then sampling procedures from probabilistic programming frameworks (like PyMC or Pyro) are valid estimators for that estimand <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>.

This means that models built with latent variables in probabilistic programming, which can be represented as DAGs, can be confidently used for causal inference if their identification is proven by tools like `y0` (a Python library) or `RCI` (an R library) <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>. This opens up the world of causal reasoning to researchers familiar with model-based probabilistic machine learning, enabling them to leverage these high-dimensional systems for answering causal queries <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.