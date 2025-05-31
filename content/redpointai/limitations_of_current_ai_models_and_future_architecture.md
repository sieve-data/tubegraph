---
title: Limitations of current AI models and future architecture
videoId: sLsYzhk_4CY
---

From: [[redpointai]] <br/> 

Aidan Gomez discusses the current [[limitations_of_ai_language_models | limitations of AI models]] and the anticipated architectural and developmental shifts in the field, emphasizing the need for smarter, more adaptable AI systems <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Current Limitations of AI Models

Current AI models, despite their advancements, still face significant challenges:
*   **Frozen Nature** Models are typically trained once, resulting in a final, frozen version of weights that does not learn from new interactions <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This means they do not remember past conversations or adapt based on user feedback <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Lack of Learning from Experience** Unlike humans who improve with practice, existing models lack the ability to learn from their experiences in the world or from direct feedback from users <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This means if a model makes a mistake or needs guidance, that feedback is often forgotten in a new interaction <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>.
*   **Diminishing Returns on Scale** The hypothesis that "scale is all you need" is breaking down, with current methods showing "very heavy diminishing returns of capital and compute" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Future advancements will require more creative and smarter approaches rather than simply increasing computational resources <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Privacy and Integration Challenges for Agents** [[the_future_and_current_state_of_ai_agents | AI agents]] require extensive access to sensitive enterprise data (emails, chat, CRM, ERP, HR software) to be effective, which raises significant privacy concerns unique to AI compared to other enterprise software <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Additionally, each company uses a unique "tapestry" of software, necessitating custom setup and integration <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Future Architecture and Model Improvements

Future AI development aims to address these limitations through several key areas:
*   **Learning from Experience** The most significant desired capability is for models to learn from user interactions and feedback, allowing them to become "experts" over time, similar to human learning <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>, <a class="yt-timestamp" data-t="00:44:46">[00:44:46]</a>. This could involve models accessing a database of previous interactions and user preferences to inform future responses <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.
*   **Reasoning Capabilities** The introduction of reasoning models has been a "complete step change in terms of improvement," enabling AI to solve problems that were previously "impossible" by reflecting on failures and finding alternative paths <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>, <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This allows models to spend different amounts of energy on problems of varying complexity <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Beyond Transformers** Despite the current dominance of the Transformer architecture, there is a strong hope and expectation for new architectures to emerge in the next 5-10 years <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>. While State Space Models (SSMs) and discrete diffusion models have shown promise, their superiority over Transformers for general language modeling is not yet clear <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.
*   **Smarter and More Creative Approaches** The field must move beyond simply scaling up compute and capital, fostering greater innovation and creativity to achieve the next leap in AI technology <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Shift to Test-Time Compute** While still requiring significant compute, the focus is shifting to test-time compute, which is crucial for enabling models to reason through problems in business applications by interacting with various tools and data sources <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

## Specialized vs. General Models

The debate between a single "one model to rule them all" and a world of specialized models is evolving:
*   **Self-Developing Experts** Models are increasingly able to self-develop "experts" or sub-networks within themselves, which alleviates some pressure for entirely specialized models <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Importance of Custom Models** Custom models remain vital for incorporating fundamental context from specific businesses or domains not available on the public web, such as manufacturing data, customer transactions, or detailed personal health records <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Companies like Coher partner with organizations possessing this private data to build specialized models <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Role of Synthetic Data** [[future_of_ai_and_pretraining_challenges | Synthetic data]] is significantly closing the gap between general and specialized models <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. While human data is still necessary, especially for evaluation, synthetic data forms an overwhelming majority of what Coher generates for new models <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This approach allows using smaller pools of human experts to generate much larger synthetic datasets <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

## Role of Data Labeling and Eval

Human input remains critical, particularly in evaluation:
*   **Eval as a Human-Dependent Process** For building models for people, humans are the best evaluators of usefulness <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Evaluation (Eval) is where humans currently cannot be taken out of the loop <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Synthetic Data Generation for Training** While direct human data generation (e.g., 100,000 doctors teaching a model medicine) is too expensive and not viable, synthetic data generation, enabled by models' ability to "chitchat," allows using smaller, trustworthy human datasets to create vast synthetic lookalike data <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This process is easier in verifiable domains like code and math where results can be checked and filtered <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## [[future_trends_in_ai_and_multimodal_models | Future Trends in AI and Multimodal Models]]

The future holds promise for new generations of AI models beyond current large language models:
*   **Domain-Specific Foundation Models** New foundation models are expected to emerge for specific scientific and industrial domains, such as biology, chemistry, and material science <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   **Addressing Data Silos** In fields like cancer research, vast amounts of data exist but are siloed and inaccessible <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. A global effort similar to the GPT moment could unlock incredible advancements if capital is applied to this data <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>. This is primarily a human problem of sharing, not a data generation problem <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>.
*   **Hardware Evolution** [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | Hardware needs]] are evolving, with test-time compute still requiring significant resources, but the overall trend points to cheaper and more abundant compute <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>. The ability to combine different types of chips to build effective supercomputers is a positive development <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>.