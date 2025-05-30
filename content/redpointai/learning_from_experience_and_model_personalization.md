---
title: Learning from experience and model personalization
videoId: sLsYzhk_4CY
---

From: [[redpointai]] <br/> 

The ability for AI models to [[personalization_and_steerability_of_ai_models | learn from experience]] and personalize their interactions is a crucial, yet currently missing, property of intelligence <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Currently, models often forget past interactions, leading to wasted time when users provide feedback <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>. Humans learn from experience, starting as novices and becoming experts over time through practice and feedback <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. AI models should possess the same capability to learn from their real-world experiences and human feedback <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## The Need for Learning from Experience
When a model doesn't remember previous chats or feedback, every new interaction is like starting with a new intern who has forgotten everything <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>, <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This lack of persistent learning makes the user experience frustrating and limits deeper engagement <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. If models could learn from feedback and avoid repeating past mistakes, users would be more invested, turning the model from a basic intern into a personalized "me 2.0" that understands their preferences and needs <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

While the exact implementation doesn't fully exist yet, a likely approach involves storing interaction history in a queryable database, making it always available to the model during generation <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>. This capability is expected to significantly unlock what can be built with AI <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>.

## Custom and Specialized Models
While general models are extraordinary and [[pretraining_and_finetuning_ai_models | synthetic data]] can considerably close certain gaps, [[personalization_and_steerability_of_ai_models | custom models]] remain important <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. They address the fundamental context about specific businesses or domains that is often missing from models trained solely on public web data <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. The web contains vast amounts of information about humanity, history, culture, and science, but it lacks specific proprietary data <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

Examples of such missing data include:
*   Manufacturing data <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>
*   Customer transactions <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>
*   Detailed personal health records <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>

Coher partners with organizations possessing this unique data to create custom models accessible only to them, making the models highly effective within those specific domains <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. While there won't be hundreds of models within an organization, a handful of specialized models might be necessary <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Custom models are relevant when the data type is different from what the pre-trained model has been exposed to, necessitating [[pretraining_and_finetuning_ai_models | fine-tuning]] or even basic [[pretraining_and_finetuning_ai_models | pre-training]] <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

## Impact on Model Development
The field has moved beyond simple RHF (Reinforcement Learning from Human Feedback) data to expert data labelers for encoding reasoning tasks and synthetic data generation <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>, <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Human evaluation remains the gold standard for model usefulness, especially in evaluation loops, as humans are the intended users <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

However, human data generation for specialized domains (e.g., teaching a model medicine with 100,000 doctors) is too expensive <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. The ability of models to "chitchat" unlocked a degree of freedom for synthetic data generation, which can then be applied to specific domains like medicine with a much smaller pool of human data (e.g., 100 doctors) <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>, <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. This trusted human data can then generate a thousandfold more synthetic lookalike data <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. In verifiable domains like code and math, it's easier to check results and filter out garbage from synthetic data <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Currently, an overwhelming majority of data generated by Coher for new models is synthetic <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.