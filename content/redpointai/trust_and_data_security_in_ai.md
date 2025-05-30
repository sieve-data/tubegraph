---
title: Trust and data security in AI
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 
Trust and data security are paramount concerns in the development and deployment of AI, particularly within enterprise environments. Salesforce, as a leading incumbent in the data space, places significant emphasis on engineering trust into its AI products <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Salesforce's Multi-Layered Approach to Trust
Salesforce addresses [[Trust and safety in digital platforms | trust]] on three distinct levels to ensure responsible AI deployment <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>:

1.  **Technological Safeguards (Einstein Trust Layer)**:
    This layer is engineered directly into the product to mitigate [[Data privacy and ethical considerations in generative AI | data security]], [[Data privacy and ethical considerations in generative AI | data privacy]], and ethical risks <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Key features include:
    *   Data masking: Proactively suggests masking sensitive data fields that could introduce bias in AI models, a practice that dates back to predictive AI days <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   Data grounding: Utilizes Salesforce's Data Cloud to reduce hallucinations by grounding AI responses in customer data <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   Citations: Provides sources for AI-generated content <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Audit Trail: Records AI interactions for accountability <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
    *   Prompt defense: Protects against malicious inputs <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   Zero retention prompts: Ensures customer data used in prompts is not retained by the model providers <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

2.  **Policy Frameworks (Acceptable Use Policy)**:
    This layer sets clear guidelines for AI usage. For example, AI bots deployed by customers are required to self-identify as AI to consumers <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

3.  **Stakeholder Engagement**:
    Salesforce has developed and open-sourced a set of "trusted AI guiding principles" centered around accuracy, honesty, and empowerment. These principles are shared with the industry and government regulators, contributing to broader [[Concerns and considerations for AI safety and regulation | AI safety and regulation]] discussions <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Data Security and Privacy Considerations
For enterprises, [[AI governance and data security within enterprise environments | data security]] and privacy are critical. Salesforce emphasizes that the data belongs to its customers, not Salesforce, distinguishing itself from many consumer companies <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

Key aspects include:
*   **Data Protection**: Mitigating risks of data leaking out of an organization or unauthorized access to workflows and data within different departments <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
*   **Sharing Rules and Entitlements**: Honoring existing sharing rules and entitlements for different employees and departments is crucial to ensure AI respects data access permissions <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.
*   **Customer Control**: Customers have control over which existing workflows and Apex functions their AI co-pilot can access, allowing them to designate access levels. This enables a cautious, step-by-step approach, starting with less harmful actions like data lookups before potentially enabling more impactful actions <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

### Addressing Broader Concerns
The shift from deterministic to stochastic AI models presents new challenges in development and operation <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Salesforce actively engages with users to build products that empower rather than replace jobs <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The naming of "co-pilot" (not "autopilot") reflects this philosophy, positioning AI as a helpful coworker <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

The biggest [[Enterprise AI adoption challenges | barriers to Enterprise AI adoption]] today are related to [[Trust and safety in digital platforms | trust]] due to real [[Data privacy and ethical considerations in generative AI | data security]] and [[Data privacy and ethical considerations in generative AI | data privacy]] risks <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. Once these trust concerns are addressed, customers are generally eager to explore and customize AI capabilities <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>.