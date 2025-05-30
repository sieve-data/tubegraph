---
title: Hardware and compute scalability challenges in AI
videoId: P6y0gr-W2-k
---

From: [[redpointai]] <br/> 

The realm of AI is rapidly evolving, bringing with it significant challenges and opportunities related to hardware and compute scalability. Experts are continually assessing what surprises them most, what's overhyped or underhyped, and the biggest unanswered questions in the field <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>.

## Shifting Scaling Laws and Compute Demands

Initially, pre-training was a key focus, but its scaling limits became apparent. The release of advanced models, particularly right after a talk on "scaling is dead," highlighted a swift transition in focus <a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>. This shift suggests that [[advancements_in_ai_model_infrastructure_for_testtime_compute | inference time]] is now seen as the new scaling law <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>.

There's a prevailing challenge in [[scaling_ai_models_and_test_time_compute | scaling AI models and test time compute]] due to the "rule of nines" at OpenAI: to increase reliability from 90% to 99%, or from 99% to 99.9%, requires an order of magnitude increase in compute, occurring every 2 to 3 years <a class="yt-timestamp" data-t="01:51:36">[01:51:36]</a>. This exponential demand raises significant questions about future hardware and compute availability <a class="yt-timestamp" data-t="01:51:54">[01:51:54]</a>.

## GPU Availability and Vendor Dominance

A major concern within [[trends_and_challenges_in_ai_infrastructure | AI infrastructure]] is the availability of GPUs <a class="yt-timestamp" data-t="01:42:55">[01:42:55]</a>. Enterprises, accustomed to running everything privately in VPCs, now struggle to secure enough GPUs for their needs, pushing them towards multi-tenant architectures <a class="yt-timestamp" data-t="01:43:41">[01:43:41]</a>.

The dominance of Nvidia in the GPU market is a significant factor <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. While Nvidia experienced a 15% drop in stock value due to perceptions around DeepSeek's open-sourcing <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>, the company's strong ecosystem around CUDA has allowed it to maintain its leading position <a class="yt-timestamp" data-t="01:53:15">[01:53:15]</a>. Despite competition from other chip developers like AWS (Trainium and Inferentia) <a class="yt-timestamp" data-t="01:52:03">[01:52:03]</a>, AMD <a class="yt-timestamp" data-t="01:53:13">[01:53:13]</a>, Microsoft <a class="yt-timestamp" data-t="01:53:20">[01:53:20]</a>, and Facebook <a class="yt-timestamp" data-t="01:53:21">[01:53:21]</a>, no one has yet made a substantial dent in Nvidia's market share <a class="yt-timestamp" data-t="01:53:32">[01:53:32]</a>.

### Dedicated Silicon and Workload Stability
The general-purpose nature of GPUs, which supports gaming, crypto, and AI, underpins their broad utility <a class="yt-timestamp" data-t="01:52:56">[01:52:56]</a>. The stability of the transformer architecture suggests a strong case for developing ASICs (Application-Specific Integrated Circuits) tailored for transformers, which could offer greater efficiency <a class="yt-timestamp" data-t="01:54:08">[01:54:08]</a>. New companies entering this space typically need to have started after 2019 or 2020, as earlier ventures might have been too general-purpose before transformers became dominant <a class="yt-timestamp" data-t="01:54:25">[01:54:25]</a>.

## The Role of Private Cloud Compute (PCC)

Apple's Private Cloud Compute (PCC) is an underhyped area that could be very significant <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>. It aims to bring on-device security to the cloud through architecturally interesting methods <a class="yt-timestamp" data-t="01:45:51">[01:45:51]</a>. While many AI workloads will remain on-device, larger LLMs will still require cloud interaction <a class="yt-timestamp" data-t="01:46:09">[01:46:09]</a>. This approach addresses the need for "single-tenant guarantees in multi-tenant environments" <a class="yt-timestamp" data-t="01:47:01">[01:47:01]</a>.

## The Infrastructure Space: Beyond Bare Metal

The [[challenges_and_opportunities_in_ai_infrastructure_development | AI infrastructure development]] space is broad, with focus extending beyond bare metal to the "LLM OS" – the infrastructure around models <a class="yt-timestamp" data-t="01:42:55">[01:42:55]</a>. Key areas of interest include:
*   **Code execution** <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>
*   **Memory (stateful AI)** <a class="yt-timestamp" data-t="01:43:16">[01:43:16]</a>
*   **Search** <a class="yt-timestamp" data-t="01:43:21">[01:43:21]</a>
*   **Security (email, identity, binary inspection)** <a class="yt-timestamp" data-t="01:43:37">[01:43:37]</a>: As AI is used for offense, AI must be applied for defense <a class="yt-timestamp" data-t="01:43:44">[01:43:44]</a>. The ability of models to infer semantics from code, beyond just syntax, is promising <a class="yt-timestamp" data-t="01:44:09">[01:44:09]</a>.

However, some areas of [[building_and_scaling_ai_infrastructure_companies | AI infrastructure companies]] are viewed with less bullishness due to their capital-intensive nature or market challenges:
*   **Serving models (GPU clouds)** <a class="yt-timestamp" data-t="01:45:51">[01:45:51]</a>: While great people can make money, it's a very capital-intensive business <a class="yt-timestamp" data-t="01:45:56">[01:45:56]</a>.
*   **Finetuning companies** <a class="yt-timestamp" data-t="01:47:56">[01:47:56]</a>: It's hard to see them as a standalone "big thing" and typically need to be part of a broader enterprise AI company or service offering <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
*   **AI DevOps/AIOps** <a class="yt-timestamp" data-t="01:48:20">[01:48:20]</a>: While there's potential, particularly for anomaly detection and improving Mean Time to Resolution (MTTR), the technology isn't fully mature yet for autonomous operations <a class="yt-timestamp" data-t="01:48:54">[01:48:54]</a>.
*   **Voice real-time infra** <a class="yt-timestamp" data-t="01:48:37">[01:48:37]</a>: Though hot and interesting, its market size remains a question <a class="yt-timestamp" data-t="01:48:40">[01:48:40]</a>.

Ultimately, the application layer is seen as significantly more interesting than infrastructure due to its ability to charge for utility rather than simply reducing to a "cost-plus" model <a class="yt-timestamp" data-t="01:47:17">[01:47:17]</a>.