---
title: Building a healthcarerelated AI app
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old who built an [[building_an_ai_startup_workflow | AI startup]] called Cal AI, shared his vision for a new [[building_an_ai_startup_workflow | AI startup]] idea named Dr. AI, which is a healthcare-related [[using_ai_for_app_development | AI app]] that could be built and launched quickly <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. He provided a roadmap for how to [[building_and_deploying_apps_with_ai_integration | build it]], [[designing_user_experience_for_ai_apps | design the user experience]], grow it, and price it <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Inspiration for Dr. AI

The idea for Dr. AI stemmed from a friend's experience where a scraped knee led to the coincidental discovery of skin cancer <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This highlighted the need for an accessible tool for quick diagnoses of skin concerns, similar to how Cal AI uses GPT technology for calorie tracking from a picture <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The app aims to provide an idea of whether a condition warrants a doctor's visit or can be waited out <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, addressing issues like lack of insurance in the US or bogged-down healthcare systems in places like Canada <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Core Features

Dr. AI would offer three main features:
1.  **Skin Scan**: Take a picture of skin abnormalities (mark or rash) for identification of harm or benignity <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Symptoms Quiz**: Input symptoms (e.g., dry cough, chills) to receive possible sickness diagnoses with likely percentage chances <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Chatbot**: A general chatbot for medical questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. ChatGPT has shown promise in diagnosing medical problems, with studies indicating it can outperform doctors in various areas, despite its current limitations like hallucination <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

> "The goal of this app isn't to tell you do you have something or do you not, it's to tell you is it safe to just wait it out or should you go see a doctor right away." <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>
>
> --- Zach Yagari

It is crucial to heavily disclaim that the app's diagnoses are not 100% accurate <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> and should not be considered definitive medical advice <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

## User Experience (UX) Design

When designing apps, the process often starts with basic framing and sketches for the [[designing_user_experience_for_ai_apps | user experience]] (UX) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The goal is to make everything simple and digestible for the user <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Designers can be hired later to refine these initial concepts <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Key UX Elements

*   **Navigation Bar**: A straightforward app requires a simple navigation bar, potentially including Home, Settings, and three main feature buttons (Scan, Chat, Symptoms Quiz) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **History Feature**: A log-like feed displaying previous chats, scans, and symptoms quiz results. This creates an investment in the product, making users more likely to stick with it even if competitors emerge <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This history could also be digestible for doctors <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Scan Skin Workflow**:
    *   Directly take the user to a camera screen to scan their skin <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   Include an upload button for existing camera roll images <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   Instead of making the user wait on an "analyzing" screen, return them to the home screen with a loading indicator <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   Display results with the image taken, a "danger level" (e.g., 0-5), and a diagnosis from the AI <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
    *   Allow users to "Ask Question" to delve deeper into a specific problem, with the ability to revisit past results in their history <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Symptoms Quiz Workflow**: A series of multiple-choice questions (e.g., yes/no, or specific cough types) to gather information, leading to a diagnosis <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. The result screen would summarize responses and offer potential diagnoses <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Chatbot**: A standard chatbot interface, with the primary innovation being the prompting <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
*   **Borrowing Primitives**: When designing, looking at existing apps for "primitives" (building blocks like feeds, stories, scanning screens) and repurposing them can significantly simplify the UX process <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Prompting the AI

To bypass AI models' inherent disclaimers about not providing medical advice, creative prompting is necessary <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. For example, framing the request as part of a "movie script" where the AI acts "as if you were a doctor for a movie script" can yield diagnostic responses <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>. When using the API directly, a function call can be used to assign the AI's response to a specific variable, ensuring only the desired diagnostic text is returned <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>. The prompt should direct the AI to provide diagnoses in both scientific terms and easily understandable language <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.

## Go-to-Market Strategy: Influencer Marketing

The marketing strategy should be considered early in the design process, specifically thinking about how influencers will showcase the app <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.
*   **Simplicity for Marketing**: An app needs to be clear and simple enough for a viewer to understand its value in a short video clip (e.g., 2 seconds on screen) <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
*   **Branding**: Prominently display the app's name (Dr. AI) on key screens, especially the "wow factor" screens like the skin scanning result <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   **Identifying "Wow Factor"**: For Dr. AI, the "scan skin" feature with its danger level and diagnosis is the most impactful to showcase <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Target Audience and Influencer Selection**:
    *   While doctors might seem like a target, their audience may primarily consist of aspiring medical professionals <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.
    *   The most interested demographic for Dr. AI is likely concerned parents (moms) <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>.
    *   Influencers should be selected based on their *audience*, not just their niche <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. Reading comments on influencer posts helps determine their audience <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
    *   Target "mom influencers" who share daily life content, as their audience is primarily other moms <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   **Influencer Storytelling**: Develop a realistic scenario where a mom uses Dr. AI to alleviate fear about a child's skin issue, demonstrating its utility and quick resolution <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.
*   **Shareability**: This app may have low direct shareability (people won't typically share pictures of their bumps online), but it can spread through word-of-mouth among parent networks <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. Paid ads and influencer marketing would be primary drivers for downloads <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, playing on potential health concerns <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

## Pricing Strategy

*   **RPM vs. CPM**: Influencer marketing relies on understanding Revenue Per Mille (RPM) and Cost Per Mille (CPM) <a class="yt-timestamp" data-t="00:41:16">[00:41:16]</a>. To be profitable, RPM must exceed CPM. Influencers are paid upfront, so predicting views is crucial <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
*   **Subscription Model**: A weekly pricing model is suggested, around $4 a week, with no free trial <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>.
*   **Capitalizing on Repeat Users**: For utility apps like Dr. AI, users might subscribe for a short period (e.g., a week) when a need arises, then unsubscribe, only to re-subscribe later when another issue occurs <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>. This "need-based" repeat usage is a key monetization strategy <a class="yt-timestamp" data-t="00:44:40">[00:44:40]</a>.
*   **A/B Testing**: Continuously A/B test various price points (e.g., $4/week, $7/week, $10/month, annual subscriptions) and free trial variations to determine the highest proceeds per download <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.

## Ethical Considerations

It is critically important to include disclaimers in the app, stating that the diagnoses are not 100% accurate and are not a substitute for professional medical advice <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>. Accuracy of the AI model is also paramount; simply wrapping a basic prompt around GPT is insufficient. Like Cal AI, the process should involve breaking down analysis into multiple prompts within a sophisticated pipeline to ensure reliability <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.