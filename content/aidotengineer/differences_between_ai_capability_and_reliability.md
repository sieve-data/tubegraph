---
title: Differences Between AI Capability and Reliability
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The concepts of AI capability and reliability are distinct, and understanding their differences is crucial for the successful deployment of AI systems, particularly [[challenges_and_benefits_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="01:46:06">[01:46:06]</a>. While models may possess high capabilities, achieving real-world reliability requires a focused [[role_of_ai_engineering_in_reliability | AI engineering]] approach <a class="yt-timestamp" data-t="01:59:57">[01:59:57]</a>.

## Defining Capability

Capability, in the context of AI models, refers to what a model *could* do at certain times <a class="yt-timestamp" data-t="01:53:51">[01:53:51]</a>. For technically-minded individuals, this often translates to the "pass@K accuracy" of a model, meaning that at least one of K answers outputted by the model is correct <a class="yt-timestamp" data-t="01:59:57">[01:59:57]</a>. Language models are already capable of many things <a class="yt-timestamp" data-t="02:24:06">[02:24:06]</a>.

## Defining Reliability

Reliability, on the other hand, means consistently getting the answer right *each and every single time* <a class="yt-timestamp" data-t="01:50:58">[01:50:58]</a>. This is often referred to as "5 9s of reliability" (99.999%) <a class="yt-timestamp" data-t="01:57:07">[01:57:07]</a>. When [[building_trust_in_ai_systems | AI agents]] are deployed for consequential decisions in the real world, reliability is paramount <a class="yt-timestamp" data-t="01:55:58">[01:55:58]</a>.

## The Gap Between Capability and Reliability

A significant challenge in [[challenges_in_ai_development | AI development]] is bridging the gap between a model's capabilities and its real-world reliability <a class="yt-timestamp" data-t="01:52:10">[01:52:10]</a>. Training methods that achieve 90% capability do not necessarily lead to 99.999% reliability <a class="yt-timestamp" data-t="01:57:07">[01:57:07]</a>. Believing that high capability automatically translates to a reliable user experience is where real-world products can fail <a class="yt-timestamp" data-t="01:52:10">[01:52:10]</a>.

### Consequences of Lacking Reliability

Failure to account for reliability can lead to significant product failures <a class="yt-timestamp" data-t="02:08:52">[02:08:52]</a>. For example, if a personal assistant only orders food correctly 80% of the time, this constitutes a catastrophic product failure <a class="yt-timestamp" data-t="02:15:37">[02:15:37]</a>. Products like Humane Spin and Rabbit R1 have faced issues because developers did not anticipate that a lack of reliability would lead to product failure <a class="yt-timestamp" data-t="02:05:07">[02:05:07]</a>.

### Challenges in Measuring Reliability

[[evaluating_ai_system_performance | Evaluating AI system performance]] and reliability is inherently difficult <a class="yt-timestamp" data-t="02:40:02">[02:40:02]</a>.
*   [[challenges_in_ai_agent_evaluation | Evaluating AI agents]] is "genuinely hard" <a class="yt-timestamp" data-t="02:40:02">[02:40:02]</a>.
*   Static benchmarks can be misleading <a class="yt-timestamp" data-t="07:18:29">[07:18:29]</a>.
*   Unlike language models (LLMs) with bounded context windows, agents take open-ended actions, making cost a critical evaluation metric <a class="yt-timestamp" data-t="08:08:09">[08:08:09]</a>. Cost must be a "first-class citizen" in all agent evaluations alongside accuracy or performance <a class="yt-timestamp" data-t="08:37:05">[08:37:05]</a>.
*   Agents are often purpose-built, meaning a single benchmark cannot evaluate all agents (e.g., a coding agent cannot be evaluated by a web agent benchmark) <a class="yt-timestamp" data-t="08:50:07">[08:50:07]</a>.
*   There is an overreliance on static benchmarks, which rarely translates into real-world performance <a class="yt-timestamp" data-t="03:29:05">[03:29:05]</a>, as seen with Cognition's Devon agent, which succeeded in only 3 out of 20 tasks over a month of real-world use <a class="yt-timestamp" data-t="01:50:07">[01:50:07]</a>.
*   Verifiers (like unit tests) can also be imperfect, leading to false positives where incorrect code passes tests, causing model performance curves to bend downwards <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.

### The Role of AI Engineering in Reliability

The core job of an [[role_of_ai_engineering_in_reliability | AI engineer]] is to close the gap between 90% capability and 99.999% reliability <a class="yt-timestamp" data-t="01:59:57">[01:59:57]</a>. This requires a shift in mindset, treating [[role_of_ai_engineering_in_reliability | AI engineering]] as a reliability engineering field rather than solely software or machine learning engineering <a class="yt-timestamp" data-t="01:57:07">[01:57:07]</a>.

It involves:
*   Figuring out the necessary software optimizations and abstractions for working with inherently stochastic components like LLMs <a class="yt-timestamp" data-t="01:29:04">[01:29:04]</a>.
*   Approaching it as a system design problem, working around the constraints of an inherently stochastic system <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   Prioritizing the fixing of reliability issues that plague agents using stochastic models <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

## Historical Precedent

The challenge of reliability in new computing paradigms is not new. The 1946 ENIAC computer, with over 17,000 vacuum tubes, initially failed so often it was unavailable half the time <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. The engineers' primary job for the first two years was to fix these reliability issues to make the computer usable for end users <a class="yt-timestamp" data-t="01:29:04">[01:29:04]</a>. Similarly, [[role_of_ai_engineering_in_reliability | AI engineers]] today must focus on ensuring the reliability of this next wave of computing for end users <a class="yt-timestamp" data-t="01:29:04">[01:29:04]</a>.