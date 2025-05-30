---
title: Data labeling and the role of synthetic data in AI
videoId: sLsYzhk_4CY
---

From: [[redpointai]] <br/> 

The evolution of generative AI models highlights the critical importance of effective data labeling and the increasing role of synthetic data in improving model capabilities <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Aiden, speaking on Unsupervised Learning, emphasized that the best application companies will also build their own models, necessitating specific approaches to data <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## The Challenge of Enterprise AI Data

For AI agents to function effectively and drive automation within enterprises, they require extensive access to data, including emails, chats, calls, CRM, ERP, and HR software, to gain necessary context <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This presents significant challenges:

*   **[[data_privacy_and_ethical_considerations_in_generative_ai | Data Privacy]]**: Very little software currently requires this degree of access, making [[data_privacy_and_ethical_considerations_in_generative_ai | privacy]] a much larger issue for AI and agents compared to other enterprise software <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Customization and Integration**: Each company uses a unique "tapestry" or "mosaic" of software, meaning there's no standard setup <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This necessitates a degree of custom setup to integrate all the relevant context into the AI model <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While AI agents might eventually alleviate some complexity, complete self-serve setup remains a "fantasy" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **[[trust_and_data_security_in_ai | Data Security]]**: The high stakes of mistakes involving sensitive data like salary or customer information demand substantial guardrails <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## The Enduring Role of Human Data Labeling

Humans remain the "gold standard" for evaluating AI model usefulness, especially when building models for people <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Therefore, evaluation (Eval) is an area where humans cannot be removed from the loop, unless an expert AI model, superior to the current one, can perform the observation <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This creates a "hard dependency on humans within Eval" <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

## The Emergence and Importance of Synthetic Data

While human data is still necessary, the cost of generating large volumes of specialized human data is prohibitive <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. For example, finding 100,000 doctors to teach a model medicine is not a viable strategy <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. However, teaching models general conversational abilities, often achieved with data from a large pool of average people, has "unlocked a certain degree of freedom in terms of synthetic data generation" <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

Synthetic data plays a crucial role in:

*   **Scaling Data Generation**: It allows for the application of a much smaller pool of human data to specific domains like medicine <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. A small, known good, and trustworthy pool of human data (e.g., from 100 doctors) can be used to generate a thousand-fold amount of synthetic lookalike data <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Addressing Data Scarcity/Siloing**: While some domains like cancer research don't necessarily have a "token scarcity," the data is often siloed and locked up across different institutions <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>. Synthetic data can help bridge these gaps or facilitate the exploration of such data, even if the primary issue is a "human problem" of data sharing rather than data generation <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
*   **Verifiable Domains**: In domains like code and math, it's easier to check results, allowing for effective filtering of synthetic data to remove "garbage" and find "gold" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. While more complex, it is still viable in other domains <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

At Coher, an "overwhelming majority" of the data generated for new models is synthetic <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

## Custom Models and Data Context

Custom models remain important because "fundamental context about a particular business or a particular domain" is often missing from models trained solely on web data <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Data not typically found on the web includes:

*   Manufacturing data <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
*   Customer transactions <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>
*   Detailed personal health records <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>

Companies like Coher partner with organizations that possess this domain-specific data to create custom models, which only those organizations can access <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. While synthetic data can significantly close the gap for general models, a handful of custom models might operate within an organization, but it's unlikely for every single team to have their own fine-tuned model <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## Future of Model Improvement and User Interaction

A key missing capability in current models is the "notion of learning from experience" <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Humans start as novices and become experts over time, and models should have the same ability to learn from real-world experience and user feedback <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This ongoing learning process, where models remember past interactions and user feedback, would significantly increase user investment and enable a personalized "me 2.0" system <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>. This could be actuated by storing interaction history in a queryable database, ensuring the model always has context of previous interactions <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.

The "scale is all you need" hypothesis is breaking, as there are heavy diminishing returns on capital and compute <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Future advancements will require smarter and more creative approaches <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. While test-time compute still requires significant resources (making inference 3 to 10 times more expensive <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>), it's not simply a matter of building larger computers <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>. The focus is shifting to data diversity and finding demonstrations for models to problem-solve in specific domains <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.