---
title: AI model training and implementation
videoId: qNPPoj1qUG0
---

From: [[lennyspodcast]] <br/> 

Marily Nika, a Product Lead at Meta and former Google employee, teaches a popular course on [[ai_integration_in_product_management | AI and product management]] on Maven. She emphasizes that [[ai_development_and_model_improvement | AI development]] should always be driven by a problem or pain point that needs a smart solution, rather than doing [[ai_development_and_model_improvement | AI]] for its own sake <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## What is an AI Model?

An [[ai_development_and_model_improvement | AI]] model can be thought of as a "kid's brain" <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. Just as a child learns to identify animals by repeated exposure to examples, a model learns to recognize patterns from data <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. It takes an input, like an image or audio, processes it, and then outputs a recognition or classification with a probability of certainty <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. For example, a speech recognition model takes voice audio as input and outputs a text transcription <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.

## Training an AI Model

The purpose of training a model is to provide it with large amounts of labeled data <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. This process involves the model processing the information, learning, and finding patterns in a "smart way" to identify specific things <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

### Data Requirements

The amount of data needed for [[ai_development_and_model_improvement | AI/ML]] to contribute effectively depends on the task <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>:
*   **Simple Classification:** For tasks like classifying a photo as a cat or a dog, as few as 15-20 labeled photos might work <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Complex Applications:** For voice recognizers or complicated Natural Language Processing (NLP) applications, thousands of data points are required <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Data Collection:** Obtaining good data is difficult and may require creative collection methods, sometimes even synthesizing fake data for training and testing <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>.

### When to Build Your Own Model

Building and training a custom model is often undertaken by large tech companies offering specific services like speech recognition or their own GPT-like systems <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. These companies need to use more and more diverse data to train and retrain their models to ensure quality superior to competitors <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. If everyone uses the same data sets, the quality of products will be identical <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

The product manager's role includes deciding when the quality of a product, such as 70% or 80% accuracy in recognition, is "good enough" to launch <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

## Implementing AI Models: [[ai_product_development_and_challenges | AI Product Development and Challenges]]

Implementing [[ai_development_and_model_improvement | AI]] requires a strategic approach focused on solving real problems.

### Avoiding the "Shiny Object Trap"

> "Don't do [[ai_development_and_model_improvement | AI]] for the sake of doing [[ai_development_and_model_improvement | AI]]. Make sure there is a problem there, make sure there is a pain point that needs to be solved in a smart way." <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>
Once a problem and a high-level solution are identified, then one should figure out how to implement it <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. An [[ai_product_management_strategies | AI PM]] helps their team solve the *right* problem, for which a data scientist can create a model <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

### When AI May Not Be a Good Approach

It is generally not advisable to use [[ai_development_and_model_improvement | AI]] for a Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. Training models with powerful machines can take weeks, and this time should not be wasted if buy-in for an idea is still needed <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. For an MVP, it's better to "fake it" with a Figma prototype to show users what the [[ai_development_and_model_improvement | AI]] would do <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

[[ai_development_and_model_improvement | AI]] should be used when there is already some existing data, or data from an adjacent product, that can be leveraged to create something meaningful, such as personalization or recommendations <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. Most startups will not have enough data to build their own models initially <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

### How AI Tools Can Enhance Product Management

Existing [[ai_development_and_model_improvement | AI]] tools can significantly enhance a Product Manager's (PM) job <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>:
*   **Mission Statements:** Tools like Chat GPT can rewrite mission statements to be understood and inspiring for all disciplines, from leadership to junior staff and even competitors <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.
*   **User Segmentation:** Chat GPT can help create user segments in a fantastic way, identifying motivations and pain points that a human mind might not consider <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For example, it can suggest diverse interest groups for a screen-less fitness band <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Idea Generation:** [[ai_development_and_model_improvement | AI]] can provide ideas for [[ai_integration_in_product_management | AI-enhanced]] features <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Challenges in [[ai_product_development_and_challenges | AI Product Development]]

Marily Nika highlights several challenges specific to [[ai_product_development_and_challenges | AI product development]] <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>:
*   **Uncertainty:** Even after extensive research and hypothesis, the results from training a model may not be optimal or answer the intended questions <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. The PM must encourage the team through this uncertainty <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   **Managing Change:** Product adoption and managing it from a leadership perspective can be tricky and challenging <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>.
*   **Data Acquisition:** Getting good data is difficult, requiring creativity to find new ways for data collection <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>.
*   **Career Trajectory:** Unlike traditional product management where launches drive progress, [[ai_development_and_model_improvement | AI]] research often involves less frequent launches <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>. PMs need to clarify assessment criteria for research-focused roles with hiring managers <a class="yt-timestamp" data-t="00:30:54">[00:30:54]</a>.

### Getting Buy-in for [[ai_development_and_model_improvement | AI/ML]] Investment

To get buy-in for [[ai_development_and_model_improvement | ML]] investments, it's helpful to <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>:
*   **Use Adjacent Product Examples:** Leverage examples of successful [[ai_development_and_model_improvement | AI-first]] products already launched by the company or similar companies <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   **Propose a "Kill Clause":** Present a rollback plan and the maximum negative impact, taking all the risk on "zero" to reassure leadership <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.
*   **Build Trust:** Trust in the PM's judgment grows with experience, and a culture that welcomes failure makes it easier to take risks <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.

## Tools and Resources for [[impact_of_custom_model_development_in_ai_tools | AI Tool Implementation]]

For PMs interested in learning how to build [[ai_development_and_model_improvement | AI]] tooling into products, it's important not to be overwhelmed <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### No-Code Tools for Model Training

Even without coding experience, there are no-code approaches for training models <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **AutoML:** Offered by Google Cloud, AutoML allows users to train high-quality custom machine learning models with minimal effort <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>. It requires a lot of pre-corrected photos and images, as it does not perform data collection <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>. An example application includes using drones to photograph wind turbines, uploading images to AutoML, and quickly identifying which turbines need maintenance <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>.

### Learning to Code and Understand Fundamentals

Marily Nika encourages PMs to learn how to code and how to train a small model on their own <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. This provides a different mindset and confidence in understanding how tools work, rather than blindly trusting them <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.

**Resources for Learning:**
*   **Online Courses (Offline Learners):** Coursera offers many courses, including "Introduction to [[ai_development_and_model_improvement | AI]]" by Stanford <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Online Coding Schools (Team-Based Learners):** Career Foundry, General Assembly, and Coding Dojo are recommended for those who enjoy learning with others <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. A few weeks of time and passion can demystify these topics <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.

### Staying Updated

To stay updated on [[ai_development_and_model_improvement | AI]] and Machine Learning, subscribe to newsletters like "The Download" by MIT Technology Review <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Also, explore academia and research blogs like Archive, where new papers and developments often appear first <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.

## Real-World Applications of [[ai_development_and_model_improvement | AI]]

*   **Google Glass Translation:** The [[ai_development_and_model_improvement | AR/VR]] team at Google demonstrated a Google Glass capable of real-time language translation. It took spoken audio input from one person, transcribed and translated it, and displayed it on the glass screen for the other person in their language, breaking down communication barriers <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
*   **Healthcare - Medical Diagnosis:** A student in Marily Nika's course developed an [[ai_development_and_model_improvement | AI]] model that could take an X-ray image as input and identify potential issues with the patient <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. They further aimed to create a recommender system suggesting next steps based on the diagnosis <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
*   **Lensa App:** Lensa is an [[ai_development_and_model_improvement | AI]]-based tool that transforms photos into artistic images, including pet photos <a class="yt-timestamp" data-t="00:46:34">[00:46:34]</a>.

## The Future of [[ai_and_software_development | AI and Software Development]]

Marily Nika believes that in the future, everything will be [[ai_development_and_model_improvement | AI]] by default <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, and all product managers will become [[ai_integration_in_product_management | AI product managers]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

This shift is driven by the need for <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>:
*   **Personalized Experiences:** Like recommender systems in streaming services (e.g., Netflix), which suggest similar content based on viewing habits <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Automation:** Continuous improvement in automation in society requires an [[ai_development_and_model_improvement | AI-centric]] view in every sector <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

PMs will need to become comfortable partnering with research scientists who can produce smart models for automations, personalizations, and recommendations <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This means getting used to the uncertainty inherent in research, where projects might be shut down if they don't work out after a year <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. The ideal product will find the intersection of user desirability, business viability, and technical feasibility from a research and technical perspective <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

[[ai_development_and_model_improvement | AI]] is seen as an enhancement that frees up PMs' time for more strategic tasks, making them smarter and unlocking new areas of product management <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. PMs play a crucial role in bridging the gap between academic research and product commercialization, identifying meaningful use cases and monetization strategies for [[ai_development_and_model_improvement | AI]] research <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>.