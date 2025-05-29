---
title: Impact of custom model development in AI tools
videoId: En5cSXgGvZM
---

From: [[lennyspodcast]] <br/> 

The company behind Cursor, Any Sphere, initially did not expect to engage in [[ai_development_and_model_improvement | model development]] for its AI code editor <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. However, it turned out to be a counterintuitive necessity <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. Today, every "magic moment" within Cursor involves a custom model <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Necessity of Custom Models

Early in their journey, when exploring the idea of automating mechanical engineering, they realized the need to develop their own models from the outset due to a lack of relevant data <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. This principle transferred to their focus on software development.

Cursor's product development is characterized by "dogfooding"—intensely using their own tool daily <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. This process instilled realism about the current state of AI technology <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. While optimistic about AI's long-term maturation, they acknowledge that models have significant issues today <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Therefore, ensuring humans remain in the driver's seat is crucial, making an exclusive model-based or end-to-end automation approach less viable <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.

The company operates as a hybrid: a software company focused on a product for millions of users, and a foundation model company that prioritizes scientific and model-side improvements to enhance product quality <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.

## Benefits and Use Cases

Custom [[ai_model_training_and_implementation | model development]] has been a significant win for Cursor's product quality <a class="yt-timestamp" data-t="00:33:19">[00:33:19]</a>. They strategically pick specific use cases where foundation models might not be efficient or capable <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.

Specific areas where custom models are used:
*   **Autocomplete Experience** Cursor's autocomplete feature predicts the next actions across multiple files and places within a file <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>. This requires models to be extremely fast (completing within 300 milliseconds) <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a> and cost-effective due to frequent use (every keystroke) <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Generic text sequence models are insufficient; specialized models are needed for autocompleting "diffs" (changes in codebase) <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. This core part of Cursor is entirely powered by their own models <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>.
*   **Assisting Foundation Models** Cursor also uses its own models to enhance the performance of larger foundation models (like Sonnet, Gemini, or GPT) <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>:
    *   **Input Side** Custom models search through the codebase to identify relevant parts to show to the larger models, acting as a specialized "mini Google search" <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.
    *   **Output Side** After the large models suggest high-level changes, smaller, faster specialty models, combined with inference tracks, fill in the details and turn these suggestions into full code diffs <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

This "ensemble of models" approach <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a> allows Cursor to push for quality in specialized tasks and achieve crucial speed, which is a vital dimension of product quality <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>. They often start with open-source pre-trained models and post-train them, sometimes in collaboration with closed-source providers <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

## Defensibility and Strategic Focus

Custom models are considered a "moat" or a defense mechanism in the AI space <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. In a market where the ceiling for improvement is incredibly high and switching costs can be low, continuous innovation and building the "best thing" are paramount <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>. This approach mirrors consumer markets more than traditional enterprise software <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>.

Companies like Cursor, which build both the underlying technology (including custom models) and the product experience for a specific area of knowledge work, are seen as highly consequential for driving [[ai_development_and_model_improvement | AI development and model improvement]] forward <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>.