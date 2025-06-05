---
title: Comparison between Gemini and GPT 4
videoId: q5qAVmXSecQ
---

From: [[fireship]] <br/> 

Google's [[Googles response to GPT 4 with Gemini | Gemini]] model was unleashed on December 7, 2023, as a direct competitor to OpenAI's GPT-4, following what some described as Google being "obliterated" by Microsoft's "blitzk attack" with GPT-4 in 2023 [00:00:00]. [[Googles response to GPT 4 with Gemini | Gemini]] was highly anticipated and demonstrated capabilities that, according to initial claims, beat GPT-4 on nearly every benchmark [00:00:16].

## What is Gemini?

[[Googles response to GPT 4 with Gemini | Gemini]] first became known to the public at Google I/O [00:00:27]. It is a [[Multimodal capabilities of Gemini | multimodal]] large language model designed to replace Lambda and Palm 2 [00:00:34]. Similar to GPT-4, [[Multimodal capabilities of Gemini | Gemini]] is trained not only on text but also on sound, images, and video [00:00:40].

### Multimodal Capabilities
[[Multimodal capabilities of Gemini | Gemini]] showcases impressive [[Multimodal capabilities of Gemini | multimodal]] capabilities, including:
*   **Real-time Video Recognition** It can recognize what is happening in a video feed and respond in real time, such as identifying a drawing of a duck [00:00:47].
*   **Object Tracking** It can keep track of objects in an ongoing video feed, demonstrated by playing "find the ball under the cup" and knowing the ball's location even after scrambling [00:00:58].
*   **Connect the Dots** It can perform tasks like connecting dots [00:01:07].
*   **Multimodal Outputs** [[Multimodal capabilities of Gemini | Gemini]] can generate images on the fly, similar to Stable Diffusion, and create music based on prompts, including converting images to audio [00:01:11]. This makes it an "anything to anything" model [00:01:23].
*   **Logic and Spatial Reasoning** It can analyze two pictures to determine which car would go faster based on aerodynamics [00:01:25]. In the future, it's envisioned that a civil engineer could take a picture of land and the AI could instantly generate bridge blueprints [00:01:33].

### Coding Prowess: AlphaCode 2
Google also unveiled AlphaCode 2, which performs better than 90% of competitive programmers, capable of solving highly complex, abstract problems found in competitions like Codeforces [00:01:46]. AlphaCode 2 can break down problems into smaller ones using techniques like dynamic programming [00:01:56].

## Gemini Model Sizes and Availability

[[Googles response to GPT 4 with Gemini | Gemini]] comes in three sizes:
*   **Nano:** The smallest version, designed for embedding on devices like Android phones [00:02:11].
*   **Pro:** A more general-purpose model [00:02:14].
*   **Ultra:** Described as the "Magnum XL of the [[Googles response to GPT 4 with Gemini | Gemini]] family" [00:02:17].

Currently, users in the United States can access [[Googles response to GPT 4 with Gemini | Gemini]] Pro through Google's Bard chatbot [00:02:22]. While Bard has significantly improved and is extremely fast, it is not yet considered as good as GPT-4 [00:02:29]. The [[Googles response to GPT 4 with Gemini | Gemini]] Nano and Pro models became available on Google Cloud on December 13th [00:04:24]. However, the [[Googles response to GPT 4 with Gemini | Gemini]] Ultra version will not be available until next year, pending additional safety tests [00:04:28].

## Performance Benchmarks: Gemini vs. GPT-4

### Gemini Pro vs. GPT-4
[[Geminis performance benchmarks | Gemini Pro]] generally underperforms GPT-4 in most situations [00:02:46].

### Gemini Ultra vs. GPT-4
[[Geminis performance benchmarks | Gemini Ultra]], however, outperforms GPT-4 in almost every category [00:02:50]. Notably, it is the first model to surpass human experts on the Massive Multitask Language Understanding (MMLU) benchmark, which is a multiple-choice test across a wide array of subjects, similar to the SATs for AI [00:02:53].

### Hellaswag Benchmark
Surprisingly, [[Geminis performance benchmarks | Gemini Ultra]] underperforms GPT-4 on the Hellaswag benchmark [00:03:05]. This benchmark is designed to evaluate common-sense natural language by having the AI finish often vague and ambiguous sentences [00:03:09]. GPT-4's ability to handle vague prompts and typos and still understand user intent makes it feel more human-like [00:03:28]. The fact that GPT-4 performs significantly better on Hellaswag is considered concerning for [[Googles response to GPT 4 with Gemini | Gemini]] [00:03:34].

## Training Infrastructure and Data

To train [[Googles response to GPT 4 with Gemini | Gemini]], Google utilized its newly unveiled version 5 Tensor Processing Units (TPUs) [00:03:40]. These TPUs are deployed in "super PODS" consisting of 4,096 chips each [00:03:43]. Each super pod has a dedicated optical switch to facilitate quick data transfer for parallel training [00:03:48]. They can dynamically reconfigure into 3D torus topologies, effectively "shape-shifting into donuts" to reduce latency between chips [00:03:54]. The scale of [[Googles response to GPT 4 with Gemini | Gemini]] Ultra's training was so vast that it required communication between multiple data centers [00:04:01].

The training dataset for [[Googles response to GPT 4 with Gemini | Gemini]] includes virtually everything available on the internet, such as web pages, YouTube videos, scientific papers, and books [00:04:07]. This data is filtered for quality, and then reinforcement learning through human feedback is used to fine-tune the quality and minimize hallucinations [00:04:14].