---
title: Causal Discovery Algorithms and Techniques
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

[[Causal discovery algorithms]] and techniques are fundamental in [[causal machine learning]], aiming to identify causal relationships from data and often resulting in a causal graph <a class="yt-timestamp" data-t="10:05:05">[10:05:05]</a>. These methods are crucial for moving beyond mere predictions to provide actionable business recommendations and support "what if" or counterfactual scenarios <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

## Advantages in Practice

One significant advantage of [[causal discovery algorithms]] is their ability to enhance explainability <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Unlike traditional black-box models that only offer predictions, [[causal discovery algorithms]] provide understandable models through causal graphs that allow stakeholders to see how factors are connected <a class="yt-timestamp" data-t="10:05:05">[10:05:05]</a>. This transparency builds trust with management, as the models can incorporate their domain knowledge and are seen as an extension of their own understanding <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>, <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.

Furthermore, these algorithms enable "what if" simulations and counterfactual scenarios, which are highly desired by management for making data-backed decisions <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>, <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>, <a class="yt-timestamp" data-t="25:09:00">[25:09:00]</a>. They can be applied across various industries, from supply chain management—where they help address complex issues like geopolitical conflicts, pandemics, and semiconductor shortages <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>, <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>—to sports, for root cause analysis of injuries or predicting match performance <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>.

## Challenges and Limitations

Despite their benefits, [[causal discovery algorithms]] face challenges. There's no absolute guarantee that these methods will yield perfectly reliable results in real-world settings due to inherent limitations <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>, <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. However, it is argued that while these models may not be perfect, they help reduce human biases present in decision-making <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.

## Practical Implementation and Validation

For practical implementation of [[causal discovery algorithms]], key steps include:
*   **Getting hands-on**: Experimenting with different algorithms and visualizations <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>, <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>.
*   **Data preparation**: Ensuring clean data and understanding the relationships (linear, nonlinear) between variables <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>, <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>.
*   **Expert validation**: Collaborating closely with domain experts is crucial. The insights derived from algorithms should always be validated by business experts to confirm logical sense and correct any inconsistencies <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>, <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.
*   **Iterative approach**: Starting with a simplified model, triangulating results with real data, and continuously incorporating more expert knowledge and data over time to improve the model's structural information <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>, <a class="yt-timestamp" data-t="46:16:00">[46:16:00]</a>. This fosters trust among stakeholders <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.

When evaluating [[causal discovery algorithms]], specific metrics like Hamming distance and the number of indirect edges can be used <a class="yt-timestamp" data-t="25:37:00">[25:37:00]</a>, <a class="yt-timestamp" data-t="30:08:00">[30:08:00]</a>. However, direct involvement and validation from business experts remain paramount, as they can "testify" if the causal relationships make sense <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>, <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>, <a class="yt-timestamp" data-t="30:23:00">[30:23:00]</a>. Multiple experts should be consulted to mitigate human biases <a class="yt-timestamp" data-t="30:55:00">[30:55:00]</a>.

## Specific Algorithms and Tools
While the effectiveness of an algorithm depends on the specific task and data <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>, some algorithms that have shown good performance include:
*   **PC Algorithm**: A generally good algorithm for [[causal discovery algorithms]] <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.
*   **Resist**: Performed "beautifully well" in a use case involving comparing tribal knowledge graphs with algorithmically discovered graphs <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.
*   **DoWhy**: An open-source Python library for [[causal inference methods and applications]] <a class="yt-timestamp" data-t="33:04:00">[33:04:00]</a>.

## Integration with Large Language Models (LLMs)

The intersection of [[causal discovery algorithms]] and Large Language Models (LLMs) is an exciting and rapidly developing area <a class="yt-timestamp" data-t="21:11:00">[21:11:11]</a>. LLMs can significantly expedite the initial [[causal discovery algorithms]] process <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. Instead of starting from scratch, LLMs can be used to generate preliminary causal relationships and a causal graph from available text data <a class="yt-timestamp" data-t="22:05:00">[22:05:00]</a>. This pre-built graph can then be presented to experts for validation, criticism, and refinement <a class="yt-timestamp" data-t="22:14:00">[22:14:00]</a>. This approach not only boosts efficiency but also motivates experts to engage and share their unique knowledge by providing a starting point for discussion <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>. Early research suggests that LLMs can generate causal graphs "really close to the ground truth" with just a few prompts <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>. Retrieval augmented generation (RAG) can further reduce hallucinations in LLM-generated causal models <a class="yt-timestamp" data-t="47:35:00">[47:35:00]</a>.

This integration offers a future where dashboards and applications might combine [[causal AI]] with LLMs, allowing users to query and quantify the impact of various events, such as a natural disaster on a supply chain <a class="yt-timestamp" data-t="44:33:00">[44:33:00]</a>.

## Educational Resources

For data scientists interested in starting with [[causal discovery algorithms]] and [[causal inference concepts and applications]], recommended resources include:
*   "The Book of Why" by Judea Pearl <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>, <a class="yt-timestamp" data-t="31:56:00">[31:56:00]</a>.
*   "Causal Inference and Discovery in Python" <a class="yt-timestamp" data-t="32:06:00">[32:06:00]</a>, which emphasizes learning by doing <a class="yt-timestamp" data-t="32:17:00">[32:17:00]</a>.
*   Research papers, particularly those combining LLMs and [[causal AI]] methods, such as those from Microsoft <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.
*   Actively engaging with the [[causal AI]] community on platforms like LinkedIn to stay updated on trends and research <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a>, <a class="yt-timestamp" data-t="34:18:00">[34:18:00]</a>.

There is also a growing trend in academia to incorporate causality into university programs, providing students with opportunities to learn about it during their studies <a class="yt-timestamp" data-t="40:10:00">[40:10:00]</a>, <a class="yt-timestamp" data-t="40:42:00">[40:42:00]</a>.