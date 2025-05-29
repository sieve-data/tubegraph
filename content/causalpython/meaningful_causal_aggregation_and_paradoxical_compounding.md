---
title: Meaningful Causal Aggregation and Paradoxical Compounding
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

"Meaningful Causal Aggregation and Paradoxical Compounding" is a research paper presented by Utan Drew, a PhD student at UCL, based on work conducted during an internship at Amazon Research Chingan <a class="yt-timestamp" data-t="02:57:42">[02:57:42]</a>. The research was a joint effort with Kyash Bui, Jonas Kubler, and Dominic Yaning <a class="yt-timestamp" data-t="03:02:18">[03:02:18]</a>.

## Key Findings

The paper highlights an interesting paradox found when working with aggregated [[abstractions_and_causal_models | causal models]]: even the property of confounding, which is a structural characteristic of [[abstractions_and_causal_models | causal models]], becomes ill-defined when ambiguous interventions are considered on aggregated variables <a class="yt-timestamp" data-t="03:08:08">[03:08:08]</a>.

To mitigate this problem, the researchers propose a "Natural Intervention," a simple realization that can help address the issue <a class="yt-timestamp" data-t="03:31:02">[03:31:02]</a>. The observation is also generalized to "laric rocks" <a class="yt-timestamp" data-t="03:36:25">[03:36:25]</a>.

## The Problem: Ambiguous Interventions

An "ambiguous intervention" arises when variables considered are aggregated versions of finer-grained, micro-level variables <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. When an intervention is applied to an aggregated variable, there are numerous ways this intervention could be realized at the micro-level <a class="yt-timestamp" data-t="03:57:07">[03:57:07]</a>. This becomes problematic as it's assumed a robust [[abstractions_and_causal_models | causal model]] exists at the micro-level <a class="yt-timestamp" data-t="04:04:12">[04:04:12]</a>.

### Example
Amazon, with millions of products, faces this challenge <a class="yt-timestamp" data-t="04:12:06">[04:12:06]</a>. If Amazon wants to understand the impact of selling more "cleaning products" (an aggregated variable) on downstream revenue, the ambiguity arises because different cleaning products have different prices <a class="yt-timestamp" data-t="04:18:24">[04:18:24]</a>. The specific way in which more cleaning products are sold (e.g., selling more high-priced vs. low-priced ones) will have different impacts on revenue <a class="yt-timestamp" data-t="04:39:04">[04:39:04]</a>.

## Real-World Implications

Most variables in real-world applications are aggregated <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>, yet there is limited academic work on the consequences of ambiguous interventions <a class="yt-timestamp" data-t="04:54:32">[04:54:32]</a>. The desired impact of this work is to encourage more analysis of this problem in real-world applications <a class="yt-timestamp" data-t="05:07:08">[05:07:08]</a>. Ideally, the research community would also develop methods to learn a set of macro variables from data that completely summarize the underlying micro model <a class="yt-timestamp" data-t="05:14:11">[05:14:11]</a>.

## How to Find the Work

To find the paper, one can search for the title "Meaningful Causal Aggregation and Related Paradoxes" or search for Utan Drew's name on Google Scholar <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

## Recommended Reading

Utan Drew recommends the paper "Multi-level Cause Effect Systems" by Kristoff Kupka, published around 2016 or 2017 <a class="yt-timestamp" data-t="05:52:16">[05:52:16]</a>. This paper focuses on learning sufficient macro variables for a specific model <a class="yt-timestamp" data-t="06:03:58">[06:03:58]</a>. It has provided inspiration for understanding how to mitigate reward hacking in large models, which often involves transferring knowledge from lower-dimensional models <a class="yt-timestamp" data-t="06:16:16">[06:16:16]</a>.