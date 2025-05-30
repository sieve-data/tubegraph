---
title: Perplexity AIs approach to model development and integration
videoId: A2uBXF8iPKY
---

From: [[redpointai]] <br/> 

Perplexity AI, an "incredible next-gen search product," has gained significant traction, raising $500 million in valuation recently <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. The simplicity of its user experience belies the underlying complexity of its development, which involves intricate model building and integration strategies <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

## Evolution of Model Strategy

Perplexity AI's approach to [[Model architectures in AI | model development]] has evolved strategically. Initially, the company started by using off-the-shelf OpenAI models <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. Over time, they transitioned to fine-tuning smaller, faster models, and have since incorporated [[challenges_and_advancements_in_ai_model_development | open-source models]], even releasing their own <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. This journey is seen as a deliberate, pragmatic choice, with the CEO stating he would "100% want to... do it exactly the same way" if he were to go back <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.

The company's strategy involves:
*   **Starting with readily available models:** For product-focused companies, it's advised not to "waste your time building your own models" initially <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. The primary goal is to get a product out, ensure it has users, and sustain usage to attract funding and talent <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Building internal expertise:** While starting with external models, Perplexity benefits from co-founding team members being former AI researchers who understand model training <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Waiting for the "next wave":** Decisions to build proprietary models or leverage open-source solutions (like Llama 2 or Mistral) were timed to coincide with major advancements in the open-source community <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## Balancing Product Focus and Model Development

Perplexity's strategy emphasizes product focus over raw model development, especially in the early stages. The philosophy is that a great engineer will join a company with a product that has users, rather than one solely focused on infrastructure or foundational models without a market <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

A core belief is that the "user is never wrong" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This user-centric approach drives decisions on [[challenges_and_strategies_in_ai_model_development | product features]] and model choices. For example, the "Co-pilot" feature was introduced to help users formulate better queries, acknowledging that "we're not very good at asking follow-ups" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Combating Hallucinations and Improving Search Quality

A key challenge in AI, particularly for search, is the phenomenon of hallucinations. Perplexity uses Retrieval-Augmented Generation (RAG) to address this, backing answers with citations <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. However, solving hallucinations isn't a simple "plug-and-play" solution, especially for [[Enterprise AI model management | enterprise AI model management]] or internal search <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

Key aspects of Perplexity's approach to search quality and RAG include:
*   **Holistic Approach:** It's not just about training a large embedding model. The process involves significant work in indexing, snippet generation, text retrieval, and advanced ranking signals beyond just vector dot products <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.
*   **Context Management:** Counter-intuitively, throwing more information at long-context models can increase the chance of hallucinations; therefore, precise retrieval is crucial <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>.
*   **Personalization:** The goal is to maximize "knowledge velocity" or "IQ velocity," providing fast, high-bandwidth access to personalized knowledge, unlike static platforms like Wikipedia <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

## Organizational Philosophy and Vertical Integration

Perplexity operates with a vertically integrated approach, where designers, product engineers, and backend teams work closely together <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This ensures that design decisions can feed data back into AI models, making the product smarter <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The company's core values—quality, truth, and velocity—are aligned with its product goals, ensuring everyone appreciates the importance of good design, great answers, speed, and reliability <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## The "Rapper" Analogy and Strategic Independence

Perplexity openly embraces the initial "rapper" label (companies that "wrap" around foundation models like ChatGPT). The CEO states, "I would rather be a rapper with 100,000 users than having some model inside and like nobody even knows who I am" <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. The strategy is to gain users and then gradually build the capabilities to serve their own models, reducing dependence on third-party providers, especially those building competing products <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

> "You earn the user trust right like a lot of users are concerned about using our products simply because they think that we cannot build our own infrastructure so we just a rapper so at some point we're going to fiz out we're going to run out of money we don't have any business so that's that's the number one part that we um want to address hey guys listen you know we we're not a rapper we're slowly building our muscle to serve everything ourselves" <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>

Perplexity aims to be "model agnostic," prioritizing the best answer for the user regardless of the underlying model <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. However, having the option to control their destiny and drive down costs by serving their own models is crucial <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

## Future Outlook on Models and AI Development

Perplexity believes that what is currently possible with state-of-the-art closed models (like GPT-4) will eventually be achievable with open-source models at a lower cost and faster latency <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>. This will continuously open up new possibilities for advanced features like dynamic prompt engineering and generative user interfaces.

The long-term vision for search involves becoming "answers," provided by "agents that just do tasks for you," simulating natural conversations with friends <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This aligns with the broader trend of [[compound_ai_systems_and_their_development | compound AI systems]], enabling complex tasks and multimodal reasoning (e.g., uploading a video and asking questions about it) <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>.

Regarding [[challenges_and_opportunities_in_ai_integration | AI regulation]], Perplexity's CEO considers it "too premature" given that the widespread economic benefits haven't been fully realized <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. He argues that stifling development now could be detrimental, and that more "eyeballs" and widespread development are better for addressing safety concerns than centralizing control <a class="yt-timestamp" data-t="00:55:03">[00:55:03]</a>.