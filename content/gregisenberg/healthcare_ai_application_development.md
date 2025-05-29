---
title: Healthcare AI application development
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old entrepreneur, has built an [[ai_applications_in_business | AI startup]] called Cal AI, which is currently generating over $1 million a month in revenue <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. He shares insights into building an [[ai_technology_for_business_applications | AI app]] and introduces a new concept called "Dr. AI," a potential [[using_ai_models_for_practical_applications_and_startups | AI startup]] in the healthcare niche <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The goal is to build a full business running in less than a month <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Inspiration for Dr. AI

The idea for Dr. AI originated from a friend's experience where a knee injury coincidentally led to the discovery of skin cancer in the same spot <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This highlighted the need for an easy way to get quick diagnoses for skin concerns without immediately visiting a doctor <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The app aims to provide an initial assessment, suggesting whether a doctor's visit is necessary or if the condition can be monitored <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This is particularly relevant in areas like the US with insurance issues or Canada with bogged-down healthcare systems <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## Core Features of Dr. AI

Dr. AI is envisioned with three main features <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>:

1.  **Skin Scan**: Users can take a picture of something on their skin or body for identification, determining if it's harmful or benign <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  **Symptoms Quiz**: A quiz where users input symptoms (e.g., dry cough, chills) to receive possible diagnoses with ranked likelihood percentages <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
3.  **Chatbot**: A general [[human_versus_ai_services | AI chatbot]] for asking medical questions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. [[Using APIs in AI App Development | ChatGPT]] has shown strong capabilities in diagnosing medical problems, even outperforming doctors in recent studies <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

> [!CAUTION]
> It is crucial to heavily disclaim that the diagnoses are not 100% accurate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The app's purpose is to guide users on whether to seek professional medical attention, not to provide definitive diagnoses <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## User Experience (UX) Design

Zach approaches [[integrating_ai_features_into_mobile_apps | app design]] by starting with basic framing and navigation <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. He typically sketches out the [[integrating_ai_features_into_mobile_apps | UX]] himself before hiring designers to refine it <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Key UX Elements

*   **Navigation Bar**: Includes Home, Settings, and placeholder for a middle feature <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Feature Buttons**: Three main buttons for Scan Skin, Chat, and Symptoms Quiz <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **History Log**: Inspired by Cal AI, this section logs previous chats, scans, and symptoms quiz results <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This creates an "investment in the product," encouraging user retention <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. The history could also be shared with a doctor for a jump start on diagnosis <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Designing the Scan Skin Flow

1.  **Camera Screen**: Immediately takes users to a camera screen for scanning skin, with an option to upload from the camera roll <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
2.  **Scanning Animation**: Includes scanning lines, a common "primitive" seen in other apps like PhotoMath <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
3.  **Analysis Handling**: Instead of a stagnant loading screen, the app takes the user back to the home screen while the scan analyzes, displaying a loading indicator there <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This avoids making users feel forced to wait <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
4.  **Results Screen**: Displays the scanned image, a "danger level" (e.g., 0-5 metric for digestibility), and a diagnosis from the [[using_apis_in_ai_app_development | AI model]] <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Users can then "ask a question" to delve deeper into the specific problem <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
5.  **Symptoms Quiz Flow**: Designed as a series of multiple-choice questions (e.g., "Do you have a cough? Yes/No"), which can lead to follow-up questions <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. The result screen would summarize responses and offer a diagnosis <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
6.  **Chatbot Preview**: The history log shows a preview of the last message in a chatbot conversation <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. The chatbot itself would follow standard chatbot UI designs <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
7.  **Sources**: Ideally, the app would show sources for the diagnosis, similar to Perplexity's search results <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

### UX Principles

*   **Simplicity and Digestibility**: The design prioritizes making everything easy for the user to understand, using numerical scales like the "danger level" for clarity <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
*   **Primitives**: Reusing existing [[integrating_ai_features_into_mobile_apps | UX]] "primitives" or building blocks (e.g., feed, stories, DMs for social media; scanning screens) saves time and leverages familiar user patterns <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Examples include [[ai_applications_in_business | Cal AI]] and Riz GPT <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## [[growth_hacking_with_ai_applications | Go-to-Market Strategy]]

The marketing strategy focuses heavily on influencer marketing, given the app's utility nature.

### Influencer Marketing Considerations

*   **App Presentation**: The app must be visually appealing, clear, and simple enough for viewers to understand its value within a 2-second influencer video <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>. Gamified elements like the "danger level" aid in quick comprehension <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.
*   **Branding**: The app's name, "Dr. AI," should be prominently displayed on key screens, especially the scanning and results screens, as these are likely to be featured most by influencers <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
*   **Shareability**: Unlike social apps, utility apps like Dr. AI may have low direct shareability (e.g., users won't widely share a picture of a skin bump) <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. Growth is more likely to come from word-of-mouth recommendations among friends or parents <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Primary Growth Lever**: [[growth_hacking_with_ai_applications | Paid ads]] or influencer marketing playing on emotions (e.g., fear of disease) would be the primary driver for downloads <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Target Audience and Influencer Selection**: The most likely target audience is concerned parents, especially mothers <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. When identifying influencers, it's crucial to analyze their audience through comments, not just their niche <a class="yt-timestamp" data-t="00:35:26">[00:35:26]</a>. Mom influencers who share daily life or "mom hacks" would be ideal <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>.
*   **Influencer Narrative**: A compelling narrative could involve a mom sharing a story about using Dr. AI to assess a child's skin concern, avoiding an unnecessary emergency room visit <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>.

### Prompting for AI Accuracy

To ensure the [[ai_technology_for_business_applications | AI]] provides useful and appropriate responses, specific prompting techniques are needed <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>:

*   **Role Assignment**: Tell the [[using_apis_in_ai_app_development | AI]] to "take on the role of a doctor" <a class="yt-timestamp" data-t="00:30:59">[00:30:59]</a>.
*   **Bypassing Disclaimers**: Use creative prompts (e.g., "as part of a movie script...") to bypass standard disclaimers from [[using_apis_in_ai_app_development | AI models]] like [[using_apis_in_ai_app_development | ChatGPT]] that prevent them from giving medical advice <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Specificity**: Use function calls in the [[using_apis_in_ai_app_development | API]] to assign the [[ai_technology_for_business_applications | AI's]] response to a specific variable, ensuring only the desired content is returned <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.
*   **Clarity**: The diagnosis should be in both scientific terms (for doctors) and easy-to-understand language (for regular users) <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.

## Business Model and Pricing

The recommended pricing model for Dr. AI is a **weekly subscription** with no free trial <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>.

*   **Rationale**: Similar to apps like Riz GPT, users may not need the service frequently but will reinstall and resubscribe when a specific need arises (e.g., a new skin concern) <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>. This capitalizes on repeat users <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>.
*   **Pricing Point**: An AB test would be conducted, but a starting point of $4 per week is suggested as a fair price <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.
*   **Influencer Payments**: Payments to influencers should be based on CPM (cost per thousand views) relative to RPM (revenue per thousand views) to ensure profitability <a class="yt-timestamp" data-t="00:41:49">[00:41:49]</a>. Influencers are paid upfront, so predicting views is crucial <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>.

## Ethical Considerations and Accuracy

> [!WARNING]
> Building a healthcare [[ai_technology_for_business_applications | AI application]] necessitates clear disclaimers that the advice is not medical <a class="yt-timestamp" data-t="00:46:54">[00:46:54]</a>. It is extremely unethical to mislead users into believing they might have serious diseases without proper medical oversight <a class="yt-timestamp" data-t="00:46:58">[00:46:58]</a>. Accuracy is paramount; unlike many basic GPT wrappers, the app must strive for high accuracy in its diagnoses, potentially using a multi-prompt "pipeline" to process information <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.

## Conclusion

The Dr. AI concept provides a comprehensive blueprint for developing and marketing a healthcare-focused [[ai_technology_for_business_applications | AI application]] <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>. The detailed roadmap covers [[integrating_ai_features_into_mobile_apps | UX design]], [[growth_hacking_with_ai_applications | growth strategies]], and ethical considerations for building a successful and responsible product <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.