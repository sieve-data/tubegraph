---
title: Open-source AI models and licensing considerations
videoId: rYXeQbTuVl0
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article:

Meta has continued its commitment to open-source artificial intelligence with the launch of its Llama 4 series of models [00:00:50]. This article details Meta's approach to its Llama models, the broader [[open_source_ai_models_and_their_implications | open-source AI landscape]], and the specific licensing considerations associated with Meta's releases.

## Meta's Llama 4 Family

Following the [[llama_3_and_ai_advancements_at_meta | Llama 3 series]] [00:00:50], which saw releases like the 405 billion parameter Llama 3.1 and the multimodal Llama 3.2 [00:03:45], Meta has introduced the Llama 4 family.

### Current and Upcoming Llama 4 Models
*   **Scout and Maverick**: The first two Llama 4 models released are mid-size to small models [00:01:56]. They are designed for:
    *   High intelligence per cost [00:02:28].
    *   Native multimodality [00:02:28].
    *   Efficiency and low latency, capable of running on a single host [00:02:37].
*   **"Little Llama"**: An 8 billion parameter model in the Llama 4 series, similar in size to the popular Llama 3 8B model, is expected "probably over the next few months" [00:02:04], [00:02:12], [00:02:19].
*   **"Behemoth"**: A "frontier" model with over 2 trillion parameters [00:02:55], [00:03:02]. Meta is exploring how to make such a large model useful, potentially by distilling it into smaller, runnable models, as its size presents significant infrastructure challenges even for post-training [00:03:13], [00:03:28].
*   **Llama 4 Reasoning Model**: A Llama 4 model focused on [[reasoning_in_ai_models | reasoning capabilities]] is also in development and "will come out at some point" [00:05:43].

Meta's general strategy is to build models for its internal use cases and then open-source them [00:02:44].

## The Open-Source AI Landscape

### Growth and Competition
The past year has been described as "a very good year for open source overall" [00:04:30]. While Llama was previously a dominant innovative open-source model, there are now "a bunch of them in the field" [00:04:43], [00:05:02]. This includes models like DeepSeek [00:36:03]. OpenAI has also publicly stated an intention to [[potential_future_scenarios_of_artificial_intelligence_development | release an open-source state-of-the-art (SOTA) reasoning model]] [00:40:34].

### Benchmarking and Performance
Public benchmarks like Chatbot Arena, where Llama 4 Maverick was ranked #35 at the time of the podcast, are viewed with caution by Meta [00:04:13]. It is argued that such benchmarks can be "skewed toward a very specific set of use cases" [00:07:17] and are often "quite easily gameable" [00:08:23]. Meta's team found it relatively easy to tune a version of Llama 4 Maverick to perform much higher on such benchmarks, but the released "pure model" has no such tuning [00:08:32].
Meta primarily anchors its model development on "user value in Meta AI" and its product north star use cases, rather than optimizing for specific public benchmarks [00:07:03], [00:08:52].

### Distillation
Model distillation has emerged as a "very powerful technique" [00:52:20]. It allows capturing a significant percentage (e.g., 90-95%) of a larger model's intelligence in a much smaller model (e.g., 10% of the size) [00:52:30]. This is particularly relevant for large models like Behemoth [00:52:09]. With multiple open-source models available, users can distill from various sources to create something optimized for their specific use case [00:52:53].

## Licensing Considerations for Llama

### The Llama License
The Llama license includes specific conditions:
*   Applications using Llama models may be required to state "built with Llama" [00:40:55].
*   Derivative models trained using Llama may need to begin with the word "Llama" [00:40:58].
*   A notable clause, referenced by others like Sam Altman [00:40:34], requires entities with over 700 million users to request a license from Meta before using the models [00:40:46], [00:43:15]. DeepSeek, in contrast, uses an MIT license [00:40:55].

### Meta's Rationale for the License
Meta's reasoning for these license terms includes:
*   **Pioneering Role**: Meta asserts they "pioneered the open-source LLM thing" and invested heavily in making it viable and safe [00:41:07], [00:41:42].
*   **Engagement with Large Tech Companies**: The primary goal of the 700 million user clause is to ensure that large cloud companies (e.g., Microsoft, Amazon, Google) or other large tech companies like Apple, engage in a discussion about a "business arrangement" before selling Llama models [00:42:00], [00:42:27].
*   **Not a Deterrent**: Meta claims the license terms have not, in practice, been a significant deterrent to adoption. The concerns are more often raised by "open-source purists" rather than by companies seeking to use the models [00:43:08], [00:43:21].
*   **Re-evaluation**: Meta would re-evaluate its licensing strategy if it became a substantial reason people chose not to use Llama models [00:42:49].

## Broader Implications of Open Source and Licensing

### Strategic Importance for Meta
Meta continues its open-source efforts because building its own models provides control over its destiny, allowing customization of architecture, size, latency, and inference costs crucial for its large-scale operations [00:44:44], [00:45:40].
There's also a concern that other companies now engaging in open source might only be doing so to compete with Meta's push. If Meta were to stop, these other entities might revert from open-sourcing, similar to how Android, initially open-source, has become more closed over time [00:46:16], [00:47:08].

### Geopolitical and Value-Alignment Considerations
It is argued that AI models "encode values and ways of thinking about the world" [00:48:47]. An early Llama version translated into French, for example, was perceived by French speakers as sounding like an "American who learned to speak French" rather than a native French person, indicating subtle embedded cultural traits [00:48:55]. This underlies the idea that it's important for American models like Llama to help establish standards [00:48:00]. Models from other countries, such as China, may have different values encoded, which are not easily changed by light fine-tuning [00:49:48].

The performance and focus of international models like DeepSeek are also influenced by [[the_relationship_between_ai_government_and_geopolitical_dynamics | geopolitical factors]] such as U.S. export controls on advanced chips to China. These restrictions compelled DeepSeek to dedicate significant resources to "low-level infrastructure optimizations" for less capable chips, potentially at the expense of developing features like multimodality, where Llama 4 currently has an edge [00:37:10], [00:37:40], [00:38:05], [00:38:42]. While DeepSeek's text capabilities are impressive, Llama 4 is considered competitive on text with a smaller model (implying lower cost-per-intelligence) and offers multimodality which DeepSeek lacks [00:38:19], [00:38:47].

### Security and Safe Distillation
When using or distilling models, especially for coding tasks, there are security concerns about potentially embedding vulnerabilities if the source model has ties to other governments [00:50:53].
Meta believes that:
*   Distilling language world models is "quite fraught" due to deeply embedded values, unless one is indifferent to adopting the source model's values [00:53:33], [00:53:40].
*   Reasoning models, especially when limited to "verifiable domains" (like math problems or coding), can be distilled more securely [00:53:59]. This involves using code cleanliness and security filters (such as Meta's open-source Llama Guard and Code Shield tools) and extensive red teaming [00:54:09], [00:54:27].

Meta views its open-source strategy as vital for fostering a competitive AI ecosystem, emphasizing the benefits of distillation while remaining cautious about the strategic and security challenges in the evolving global AI landscape.