---
title: Challenges with AI models including hallucinations and bias
videoId: MvxtIIqJRUQ
---

From: [[redpointai]] <br/> 

Peter Welinder, VP of Product and Partnerships at OpenAI, discusses the [[challenges_and_advancements_in_ai_model_development | challenges]] and strategic approaches OpenAI takes concerning their AI models, including the prevalent issues of hallucinations and bias, and the broader implications of advanced AI development <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Current Gaps in AI Model Development
Welinder notes that the biggest gap currently preventing widespread enterprise adoption of AI models is the problem of hallucinations <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

### Hallucinations
Hallucinations occur when AI models generate factual statements that are not true or cannot be verified <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
*   **Impact**: Users cannot entirely trust the models, which is a major barrier to adoption <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.
*   **Solution Approaches**:
    *   OpenAI invests significant effort to make their models more robust against hallucinations <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
    *   Companies commonly address this by "grounding" models in external data <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>. This involves:
        *   Embedding questions and internal company documentation <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
        *   Using vector databases for relevant document retrieval <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>.
        *   Instructing the language model to synthesize answers from these documents or to state "I don't know" if the answer isn't found <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Nature of the Problem**: Hallucinations remain an open [[challenges_in_ai_research_and_potential_solutions | research problem]] at the [[challenges_and_advancements_in_ai_model_development | cutting edge]] of the field <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.

### Bias
Bias in AI models is considered impossible to eliminate entirely <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
*   **OpenAI's Approach**: Provide tools for product developers and users to instruct the model to have desired biases within certain bounds <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.
*   **Goal**: Models should not possess a particular political orientation; the user should be able to choose the model's behavior <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.

## Broader Safety Concerns and the Path to Superintelligence
Welinder distinguishes between "surmountable" risks and the more profound risk posed by superintelligence <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.

### Surmountable Risks
Risks such as misinformation, deepfakes, and job displacement are seen as largely surmountable <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.
*   **Misinformation**: Primarily a distribution channel problem, leveraging existing platforms (social media, email) which already have infrastructure to protect against it <a class="yt-timestamp" data-t="00:31:03">[00:31:03]</a>.
*   **Bias**: As discussed, can be managed by providing tools for user-defined alignment <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.

### Superintelligence Risk
The most critical and under-addressed risk is the emergence of superintelligence—AI models that become far smarter than humans <a class="yt-timestamp" data-t="00:32:19">[00:32:19]</a>.
*   **Lack of Research**: There is a surprising scarcity of [[challenges_in_ai_research_and_potential_solutions | research]] into ensuring a positive outcome from superintelligence <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>, with no dedicated "superintelligence safety departments" at universities <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>.
*   **OpenAI's Strategy**:
    *   **Gradual Deployment**: Release models when stakes are low to learn from risks like misinformation and bias <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. This approach aims to build the necessary organizational processes, frameworks, and safety safeguards *before* encountering superintelligence <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
    *   **Cautionary Holds**: OpenAI delayed the release of GPT-4 by nearly half a year to gain clarity on its potential downsides <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.
    *   **Setting an Example**: As a leader, OpenAI hopes its cautious approach will encourage accountability among other developers in the field <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>.
*   **Potential Timeline**: Welinder speculates that something resembling AGI (Artificial General Intelligence) could emerge by the end of this decade (before 2030) <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>. Superintelligence might follow, characterized by abilities such as thinking faster than humans, parallel processing, or conducting more experiments than a human <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>. He places the early signs of superintelligence around 2030 <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>.
*   **Optimism**: Despite the risks, Welinder is optimistic that humanity can navigate these challenges, similar to avoiding nuclear war due to self-preservation <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
*   **Upside Potential**: Superintelligence holds immense promise for solving global [[the_limitations_and_potential_of_current_ai_models_towards_agi | problems]] like climate change, cancer, and aging, leading to greater abundance and a higher standard of living <a class="yt-timestamp" data-t="00:40:23">[00:40:23]</a>.

### Research Areas for Superintelligence Safety
If leading a superintelligence safety department, Welinder would focus on:
1.  **Interpretability**: Understanding what is happening inside black-box models by studying activations within deep neural networks <a class="yt-timestamp" data-t="00:41:18">[00:41:18]</a>. This can move faster than traditional neuroscience <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>.
2.  **Defining Alignment**: Achieving crisper specifications for goals and guardrails for AI <a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>. This requires collaboration between technical experts, social scientists, and philosophers <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.
3.  **Technical Approaches**: Exploring methods such as shaping reward functions for reinforcement learning, or having one AI model oversee and report on the actions of another <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.

## OpenAI's Focus and Competitive Landscape
OpenAI's primary focus is on continually improving the intelligence and safety of its core models <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>.
*   **Prioritization**: Key priorities include lower prices, higher reliability, and lower latency for their models <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. These are considered fundamental, as external tooling is less effective without a strong core intelligence product <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
*   **Developer Tooling**: While the ecosystem will build most tooling, OpenAI will provide tools for common needs to help developers get started quickly <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

A significant concern for OpenAI is the risk of losing touch with its users and developers due to rapid growth <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a>. As models become more capable, they might replace functionality that developers have built, creating tension <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>. Maintaining a strong relationship and excellent customer experience, even with millions of users, is crucial to ensuring continued embrace and development on OpenAI's platform <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>.