---
title: Integration of AI and data platforms in enterprises
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 

Jonathan Frankle, Chief AI Scientist at Databricks (joining via the Mosaic acquisition), shares insights on the [[enterprise_ai_adoption_challenges_and_solutions | integration of AI and data platforms]] in enterprises. His discussions cover how businesses can strategically adopt AI, from model selection to deployment and evaluation, drawing lessons from Databricks' extensive customer base <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Databricks and Mosaic: A Synergistic Acquisition

Databricks acquired Mosaic due to a natural synergy: Mosaic had a strong AI platform, and Databricks had a robust data platform <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. AI fundamentally requires data, making the combination logical <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The leadership teams, composed largely of academics and scientists, shared a common understanding, facilitating the merger despite initial reluctance from both sides <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. The initial discussions that led to the acquisition reportedly took place at the Cal Valley Conference <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Enterprise AI Adoption Strategies

Enterprises often struggle to determine the best approach for integrating AI: training custom models, fine-tuning, or simply using prompt engineering <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Frankle advises keeping options open and starting small, gradually scaling up based on rigorous ROI justification <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Phased Approach to AI Adoption
*   **Start with Prompting**: Begin by simply prompting a model (e.g., OpenAI or Llama on Databricks) to litmus test if AI is suitable for a given use case <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Implement RAG (Retrieval-Augmented Generation)**: If initial prompting shows promise, leverage RAG to incorporate proprietary enterprise data, as generic models cannot inherently know about internal data <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Databricks refers to this as "data intelligence" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Fine-tuning**: If RAG yields value, fine-tuning can bake data into the model, improving quality and reducing inference costs <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Continued Pre-training / Full Pre-training**: For extensive usage and specific needs, further pre-training can lead to highly specialized and cost-effective models, though this is a significant undertaking <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

Frankle stresses an agile approach: do not wait for "perfect" data or evaluations <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. The utility of data and evaluations is measured by the success of the AI system in real-world scenarios <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### Evaluation and Benchmarking
Evaluating AI models is crucial but challenging <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Frankle advises starting with simple, even imperfect, benchmarks and iteratively improving them <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Human testing, even from a single external person, provides invaluable real-world feedback compared to synthetic benchmarks <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Databricks has released a new "agent eval" product, aimed at helping users create meaningful evaluation sets quickly, ideally in an afternoon, to measure their models effectively <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This product is now in public preview <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Databricks' Internal AI Journey with dbrx
Databricks utilized its own comprehensive platform to build its dbrx language model, showcasing the full [[role_of_custom_models_and_enterprise_ai_integration | enterprise AI integration]] capabilities <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. They used:
*   **Spark**: For data ingestion and ETL, significantly reducing processing time from weeks to minutes <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **Delta tables**: For data storage <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Unity Catalog**: For tracking and managing datasets, proving "incredibly useful" <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **MLflow**: As their experiment tracker, noting its phenomenal and free nature <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Mosaic inference service**: For model serving <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

## Use Cases for Domain-Specific Models
While large general models are advancing, there are specific scenarios where domain or company-specific models offer significant advantages:
1.  **Language/Cultural Specificity**: Models not well-tuned for non-English languages (e.g., Japanese, Korean) due to tokenizer issues or data scarcity <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. Companies like NTS and Ola have built impressive models for their respective regions (Japan, India) <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
2.  **Fundamentally Different Tasks**: For tasks vastly different from general language understanding, like protein modeling, specialized models are necessary <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
3.  **Speed and Specificity**: Applications requiring extremely fast and highly specific responses, such as code completion tools (e.g., Replit), benefit from models built for speed and tailored to the task <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
4.  **Cost Optimization**: For models with high usage, the upfront investment in pre-training can lead to substantial long-term cost savings or significantly improved quality at the same cost, by shifting the cost-quality trade-off <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

## AI Product-Market Fit Patterns
AI has found strong product-market fit in two main patterns:
1.  **Brainstorming and Creative Applications**: Scenarios where "being right" is not strictly required, and multiple correct answers exist, such as creative tasks, marketing, or general information surfacing (e.g., Glean) <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
2.  **Human-in-the-Loop Validation**: Cases where generating a proposed answer is costly for a human, but checking it is relatively quick (analogous to P vs. NP problems in complexity theory) <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. Examples include coding co-pilots like GitHub Copilot and potentially customer support, where AI can draft responses for human review <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

## Future of AI Development: Quality vs. Fuzziness
While chaining models and agents can improve quality by running more tokens through the model in creative ways, it pushes along the cost-quality curve but doesn't eliminate the fundamental "fuzziness" of AI systems <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. Achieving "perfection" or "five nines of quality" remains challenging with current generation technology <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. This means continuous learning is required to leverage AI's strengths and mitigate its weaknesses, similar to the decades-long journey of developing software engineering practices <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>. Even without further technological breakthroughs, learning to use existing tools better will lead to enormous creativity <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.

## AI and Societal Comfort: Policy and Philosophy
The discussion touches on the broader societal implications of AI, particularly in high-stakes fields like [[challenges_and_opportunities_of_ai_integration_in_healthcare | healthcare]] and autonomous vehicles <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **Trust and Explainability**: Human intuition about human errors differs from AI errors, making AI mistakes harder to accept, especially when the reasoning is unpredictable <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. Building trust requires transparency and understanding where AI systems fail <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   **Setting Standards**: AI's capabilities challenge us to reconsider the standards we hold humans to in certain tasks. For example, automated facial recognition systems highlighted human fallibility, prompting a re-evaluation of human performance standards <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>. Similarly, autonomous vehicles push us to rethink driver's tests <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.
*   **Responsible Policy**: AI practitioners have a responsibility to participate in policy conversations, not just for self-interest, but to ensure AI is used responsibly <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. This requires scientific honesty, clear communication of biases, and earning trust <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.
*   **Contextual Regulation**: Blanket regulation of AI is not ideal; instead, careful, application-by-application consideration is needed <a class="yt-timestamp" data-t="00:56:24">[00:56:24]</a>. In high-stakes areas like law enforcement, medicine, and autonomous vehicles, extraordinary caution is necessary due to the potential for severe consequences <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.

## AI Infrastructure Landscape and Databricks' Role
Databricks aims to provide an end-to-end platform for AI, integrating tools for data, model training, and evaluation <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. This involves partnering with numerous startups and even acquiring companies like Lilac, whose tools were highly valued internally <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. The goal is to provide customers with a complete, well-integrated set of tools without needing to cobble together disparate systems <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

There is significant investment in large open-source models by major companies like Meta (Llama models) <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>. Databricks focuses its efforts on other gaps in the ecosystem, such as eval creation, navigating the space of fine-tuning versus RAG, and helping customers connect their diverse data (even imperfect data) to build AI systems <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. This includes exploring "compound AI systems" and agents to connect different pieces <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

## Reflections on AI Progress
Frankle expresses humility about predicting the future of AI, admitting past incorrect predictions, such as underestimating GPT-3 <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>. He emphasizes that the field works in "big leaps" followed by consolidation <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.

### Recent Developments in AI Research
*   **01 Model (OpenAI)**: Frankle finds it exciting and acknowledges OpenAI's impressive engineering achievement in scaling up existing ideas <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>. Its impact will be determined by its ability to generalize beyond constrained, mathematical problems <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>.
*   **Anthropic's Computer Use Work**: This work is considered an important application, indicative of a new phase of experimentation in AI products. Frankle admires Anthropic's creativity and willingness to take risks <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

## Academia's Role in AI Research
Academia plays a vital role by "zagging" when industry "zigs" <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>. Academics can ask difficult questions that companies might avoid, build critical benchmarks and leaderboards, and take risks on new technologies and models <a class="yt-timestamp" data-t="00:49:27">[00:49:27]</a>. Key areas for academic focus include human-AI interaction (HCI), data research, and product development <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

## Data Labeling Market
Data annotation is "really important" for AI <a class="yt-timestamp" data-t="00:51:18">[00:51:18]</a>. The challenge lies in efficiently turning human labor into high-quality data annotations, requiring significant expertise and trust in the service providers and their supply chains <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

## [[Role of AI in Future Business Operations | Future of AI Applications]] and Jonathan Frankle's Role
Frankle finds his current role at Databricks fascinating because he is at the "nexus" of science, policy, and society, witnessing how AI is being applied to "most economically useful tasks" by Databricks' 12,000 customers <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>. He is excited about the potential of embodied systems and robotics, though acknowledging the inherent risks and long development cycles <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>.

Databricks' commitment as "the data and AI company" means AI is integrated into every job function <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. Frankle invites interested individuals to explore Databricks products like the AI Model Gateway, Agent Platform, Agent Evaluation product, and new fine-tuning techniques (e.g., "soft" fine-tuning for fragmented data) <a class="yt-timestamp" data-t="01:02:49">[01:02:49]</a>.