---
title: Scaling AI models and test time compute
videoId: OoL8K_AFqkw
---

From: [[redpointai]] <br/> 

Noam Brown, a research scientist at OpenAI, was a key part of their work on O1 models, which are at the forefront of reasoning in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. His background includes work on problems in diplomacy and poker at Fair <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Brown discusses the current state of AI model capabilities, emphasizing the importance of [[scaling_testtime_compute_in_ai_models | test-time compute]] and how it has changed his perspective on AGI timelines <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Evolution of AI Timelines and Compute

In late 2021, Noam Brown expressed skepticism to Ilya Sutskever about AGI timelines, believing it would take over a decade <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. His primary reason was the lack of a general method for [[scaling_testtime_compute_in_ai_models | scaling inference compute]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. He observed that while models were becoming smarter through [[pretraining_and_finetuning_ai_models | pre-training]], they still struggled with basic tasks like Tic-Tac-Toe, leading him to believe that [[pretraining_and_finetuning_ai_models | scaling pre-training]] alone wouldn't lead to superintelligence <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

To Brown's surprise, Sutskever agreed that [[pretraining_and_finetuning_ai_models | scaling pre-training]] alone wouldn't achieve superintelligence and was also focused on the [[scaling_testtime_compute_in_ai_models | test-time compute]] direction <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The problem Brown thought would take at least a decade to solve was largely addressed in two or three years <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. He now believes that while other research questions remain, none will be harder than the problems already solved <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, and progress will continue rapidly <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## The Role of Scaling in AI Model Development

### Scaling Pre-training

Scaling [[pretraining_and_finetuning_ai_models | pre-training]] has shown continued improvements in models <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The significant advancements from GPT-2 (costing $5-$50,000) to GPT-4 (costing hundreds of millions of dollars for some labs) primarily reflect increased resources <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Brown asserts that throwing more money, resources, and data will continue to yield better models <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

However, the cost of further scaling becomes intractable, hitting a "soft wall" where it's no longer economically viable to pursue a 10x improvement, potentially costing billions or tens of billions of dollars <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This economic barrier, rather than a hard technical limit, eventually makes it not "economically worth it to push that further" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### [[scaling_testtime_compute_in_ai_models | Test-Time Compute]]

Brown is particularly excited about [[scaling_testtime_compute_in_ai_models | test-time compute]] because it is still in its early stages, akin to the GPT-2 era of [[pretraining_and_finetuning_ai_models | pre-training]], with significant room for 1,000x scaling and algorithmic improvements <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

The ceiling for [[scaling_testtime_compute_in_ai_models | test-time compute]] is envisioned in terms of dollar value <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. While a ChatGPT query currently costs about a penny <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, Brown believes people would pay millions of dollars for solutions to critical societal problems <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This represents eight orders of magnitude of potential growth, indicating substantial room for further advancement through both increased investment and algorithmic enhancements <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## OpenAI's Approach to [[scaling_testtime_compute_in_ai_models | Test-Time Compute]]

When Noam Brown joined OpenAI, he found a surprising openness to the idea of [[scaling_testtime_compute_in_ai_models | scaling test-time compute]], despite OpenAI being the pioneer of large-scale [[pretraining_and_finetuning_ai_models | pre-training]] <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Initially, OpenAI's motivation for this direction was to overcome the "data wall" rather than directly focusing on [[scaling_testtime_compute_in_ai_models | test-time compute]] scalability <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. However, their agendas proved compatible <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

The development of O1 involved an exploratory research direction <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. A key breakthrough occurred when allowing the model to "think for longer," which led to the emergent display of desired behaviors such as trying different strategies, breaking down problems, and self-correcting mistakes <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This qualitative shift, observed around October 2023, was a significant moment, even more so than the immediate performance improvements <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

Brown attributes OpenAI's success in this area to its "organizational excellence," recognizing the potential of [[scaling_testtime_compute_in_ai_models | test-time compute]] and investing heavily in it <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This willingness to pursue a "risky direction" that is disruptive to its own pioneering paradigm demonstrates that OpenAI is not trapped in the "innovator's dilemma" <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

### The Bitter Lesson

Noam Brown refers to Richard Sutton's "Bitter Lesson" in Reinforcement Learning (RL), which states that methods leveraging more compute and data consistently outperform those that try to inject human knowledge or clever tricks <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>. Applied to LLMs, Brown argues that current scaffolding techniques and prompting tricks, while providing short-term gains, are unlikely to scale well with more data and compute <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. He believes that [[advancements_in_ai_model_infrastructure_for_testtime_compute | advancements in AI model infrastructure for testtime compute]], like O1, which inherently scale well, will eventually replace these temporary solutions <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.

For startups and builders, Brown advises caution against over-investing in custom scaffolding or specialized agentic workflows that might become obsolete as core model capabilities improve out of the box <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

## O1 Model Capabilities and Future Vision

The O1 model takes images as input <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. It is particularly adept at tackling very hard reasoning tasks, making it a "real power user" for researchers at universities, capable of handling complex research questions that would normally require a PhD <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. While O1 is more intelligent for hard problems, GPT-4o offers faster responses for less complex reasoning tasks <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

Ultimately, Brown envisions a future with a single, highly capable model that can handle any query, performing deep thinking when required or providing immediate responses for simpler tasks <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

He highlights the shift from problem-specific reasoning (like Monte Carlo search for Go) to a more general [[scaling_testtime_compute_in_ai_models | inference compute]] capability <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. His experience with Diplomacy, where domain-specific techniques hit a ceiling, convinced him that a "start from everything" mindset was necessary to achieve superhuman performance, rather than trying to extend a technique from one domain to many <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.

## Future Directions and Impact

### Agentic Models

Brown is excited about models becoming more "agentic" <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>. Historically, models were too brittle for long-horizon tasks requiring many intermediate steps <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. O1 serves as a proof of concept that models can independently figure out and tackle intermediate steps for complex problems without excessive prompting <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

### Specialized Tools and [[cost_optimization_and_economic_considerations_for_ai_model_deployment | Cost Optimization]]

While a single general model is the goal, Brown acknowledges the role of specialized tools <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. For instance, instead of O1 performing large number multiplication internally (an expensive process), it should ideally call a calculator tool or write a Python script for efficiency <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. These tools offer speed and cost savings, and sometimes even flat-out better performance than a general model <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

### [[hardware_and_compute_scalability_challenges_in_ai | Hardware and Compute Scalability Challenges in AI]]

The rise of O1 fundamentally shifts the focus for hardware development <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>. Previously, the mindset was on massive [[pretraining_and_finetuning_ai_models | pre-training]] runs with cheap inference costs <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. However, Brown anticipates a major shift towards inference compute, creating opportunities for hardware optimization around this new paradigm <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>.

### Role of Academia

Noam Brown notes the [[challenges_in_ai_model_training_and_deployment | challenges in AI model training and deployment]] for PhD students in academia, as pushing the frontier increasingly relies on access to significant data and compute resources <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>. He advises against competing directly with frontier industry labs on capabilities that require massive resources <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>. Instead, he suggests focusing on investigating novel architectures or approaches that demonstrate promising scaling trends with more data and compute, even if they don't immediately achieve state-of-the-art performance on current evaluations <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>. Such research, he states, will gain attention from industry labs willing to invest resources to explore its potential at large scale <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>.

### Underexplored Applications

Brown is particularly excited about the potential of AI models to advance scientific research <a class="yt-timestamp" data-t="00:42:10">[00:42:10]</a>. As models surpass human expert capabilities in various domains, they can act as partners to researchers, enabling new discoveries or accelerating existing processes <a class="yt-timestamp" data-t="00:42:41">[00:42:41]</a>. Specific areas where O1 has shown impressive results include math and coding <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>.

Another promising area is using models for social science experiments, including economics and game theory <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. Models trained on vast human data can imitate human behavior, providing a scalable and cost-effective alternative to human subjects <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>. This also opens up possibilities for experiments that might be ethically problematic or cost-prohibitive with human participants, such as the ultimatum game with large sums of money <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.

## Conclusion

Noam Brown encourages skeptics to examine the progress in AI, particularly the [[advancements_in_ai_model_infrastructure_for_testtime_compute | advancements in AI model infrastructure for testtime compute]] <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a>. He emphasizes that the current state of AI is "complete science fiction" compared to just five or ten years ago <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>, and this paradigm significantly addresses concerns about hitting a progress wall <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>. He predicts that model progress will accelerate in 2025 <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.