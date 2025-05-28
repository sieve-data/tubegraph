---
title: Dynamic Adapter Loading with LauraX
videoId: G7FnlVYRUuY
---

From: [[hu-po]] <br/> 

[[LCMLaura Accelerating Stable Diffusion Models | Laura X]], often referred to as Laura Exchange, is not a traditional research paper but rather a concept discussed in a talk or presentation. It addresses a significant problem in the efficient serving of fine-tuned models, particularly when multiple [[lora_technique_for_model_adaptation | LoRA]] adapters are in use <a class="yt-timestamp" data-t="26:41">[26:41]</a>. While promotional in nature, it frames a key challenge that [[Efficient Serving of FineTuned Models with SLaura | sLoRA]] aims to solve <a class="yt-timestamp" data-t="26:41">[26:41]</a>.

## The Problem: Inefficient Model Serving
When serving fine-tuned models, especially with diverse customer demands, it's common to have many different fine-tuned versions of a base model <a class="yt-timestamp" data-t="27:49">[27:49]</a>. The traditional approach is to load each unique fine-tuned model (base model + specific [[lora_technique_for_model_adaptation | LoRA]]) onto a separate physical computer or GPU <a class="yt-timestamp" data-t="28:17">[28:17]</a>.

This method quickly becomes inefficient and costly <a class="yt-timestamp" data-t="28:41">[28:41]</a>:
*   **High Resource Consumption**: It's undesirable to have dozens or hundreds of dedicated GPUs, each loaded with a different [[lora_technique_for_model_adaptation | LoRA]], simply waiting for a specific customer request <a class="yt-timestamp" data-t="28:48">[28:48]</a>.
*   **Duplication**: A significant portion of these loaded models (the base model weights) would be identical across different instances, leading to wasted memory and compute <a class="yt-timestamp" data-t="28:29">[28:29]</a>.

The ideal scenario is to have a single compute node capable of dynamically serving every type of [[lora_technique_for_model_adaptation | LoRA]] <a class="yt-timestamp" data-t="28:58">[28:58]</a>.

## LauraX's Solution: Dynamic Adapter Loading
[[LCMLaura Accelerating Stable Diffusion Models | Laura X]] proposes "Dynamic Adapter Loading" (where "adapter" refers to a [[lora_technique_for_model_adaptation | LoRA]]) <a class="yt-timestamp" data-t="29:04">[29:04]</a>. Instead of preloading all model weights, [[LCMLaura Accelerating Stable Diffusion Models | Laura X]] only loads the pre-trained [[LLaMAAdapter and its role in adapting language models | LLM]] (Large Language Model) weights <a class="yt-timestamp" data-t="29:52">[29:52]</a>.

Then, it dynamically loads each set of fine-tuned [[lora_technique_for_model_adaptation | LoRA]] adapters *just-in-time* at runtime <a class="yt-timestamp" data-t="29:56">[29:56]</a>. This approach aims to prevent blocking of ongoing requests <a class="yt-timestamp" data-t="30:01">[30:01]</a>.

### Implementation Details
*   [[LCMLaura Accelerating Stable Diffusion Models | Laura X]] maintains an individual request queue for each fine-tuned adapter <a class="yt-timestamp" data-t="30:04">[30:04]</a>.
*   When a new fine-tuned model adapter needs to be dynamically loaded, its associated requests wait in a queue, while other requests proceed as usual <a class="yt-timestamp" data-t="30:10">[30:10]</a>.

### Benefits
The overhead of dynamically loading a new adapter was observed to be around 200 milliseconds <a class="yt-timestamp" data-t="30:17">[30:17]</a>. This is considerably less than typical text generation response times, allowing for interactive evaluation of fine-tuned models immediately after training completion <a class="yt-timestamp" data-t="30:21">[30:21]</a>.

[[LCMLaura Accelerating Stable Diffusion Models | Laura X]] specifically focused on [[LLaMAAdapter and its role in adapting language models | Llama 27B]] with different [[lora_technique_for_model_adaptation | LoRAs]] <a class="yt-timestamp" data-t="29:10">[29:10]</a>, aiming to hot-swap them based on user requests <a class="yt-timestamp" data-t="29:31">[29:31]</a>. This concept highlights the challenge of serving many distinct [[lora_technique_for_model_adaptation | LoRA]] adapters in a compute-efficient manner <a class="yt-timestamp" data-t="30:37">[30:37]</a>.