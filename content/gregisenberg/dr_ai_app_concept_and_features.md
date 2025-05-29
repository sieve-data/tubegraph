---
title: Dr AI app concept and features
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old entrepreneur behind the successful AI startup [[cal_ai_app|Cal AI]], which generates over $1 million a month in revenue, has outlined a new AI startup concept called "Dr AI" <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This idea is presented as a full business that could be built and launched in less than a month <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Concept Origin

The idea for Dr AI originated from a personal experience of Yagari's friend <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. His friend scraped his knee, and during a doctor's visit for the injury, a previously unnoticed skin cancer in the same area was discovered by coincidence <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This prompted Yagari to consider how frequently people encounter unidentifiable skin issues that cause concern, highlighting the need for a quick way to get an initial diagnosis without immediately seeing a doctor <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Problem Dr AI Aims to Solve

Dr AI addresses a significant problem in healthcare access, particularly in countries like the US, where many are uninsured, and Canada, where healthcare systems can be bogged down, leading to millions without access to primary doctors <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The app's goal is not to provide definitive medical diagnoses, but to offer an initial assessment to help users decide if a medical professional visit is necessary or if they can safely wait it out <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Core Features

Dr AI is designed with three main features leveraging [[using_ai_tools_for_app_functionality_and_innovation|AI capabilities]] <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>:

1.  **Skin Scan**: Users can take a picture of a skin anomaly or body part to identify what it is and determine if it's harmful or benign <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  **Symptoms Quiz**: Users input their symptoms (e.g., dry cough, chills), and the app provides potential sicknesses, possibly ranked by likelihood <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The quiz would likely use a series of multiple-choice questions to guide the user <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
3.  **Chatbot**: A general AI chatbot allows users to ask any health-related questions. Studies have shown that ChatGPT is very effective at diagnosing medical problems, often beating doctors in various areas <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Important Disclaimers

Given the medical nature of the app, Yagari emphasizes the critical need for heavy disclaimers, stating that the diagnosis is not 100% accurate <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The app aims to guide users on whether to seek professional medical attention rather than replacing it <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## User Experience (UX) Design

[[building_an_ios_app_with_ai | Building an iOS app with AI]] involves a deliberate UX strategy:

*   **Simple Framing**: Yagari starts with basic framing, including a navigation bar with sections like Home, Settings, and History <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Feature Buttons**: The three main features (Scan, Chat, Symptoms Quiz) would be accessible via distinct buttons on the home screen <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History Log**: Inspired by [[cal_ai_app|Cal AI]], a history section allows users to scroll through past chats, scans, and quiz results <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This creates user investment, as their data is stored, potentially making them less likely to switch to a competitor <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. The history could even be presented in a format digestible for doctors <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Scan Flow**:
    *   Clicking "Scan Skin" leads directly to a camera screen with options to take a picture or upload from the camera roll <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
    *   After taking a picture, instead of a lengthy "analyzing" screen, the app returns the user to the home screen with a subtle loading indicator <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   **Results Screen**: Displays the scanned image, a "danger level" metric (e.g., 0-5), and a diagnosis <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. Users can then "ask a question" to delve deeper into their specific problem, aiding retention <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Simplicity and Digestibility**: The design prioritizes simplicity and making information digestible, often using numbers or charts (like the danger level) rather than verbose text <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This "gamified" approach helps users quickly understand the severity of a condition <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
*   **Inspiration from "Primitives"**: When designing, Yagari looks at existing similar apps or "primitives" – fundamental building blocks of app design – and repurposes them for the new use case <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. For Dr AI, inspiration came from [[cal_ai_app|Cal AI]] and Riz GPT, which featured a similar three-feature pop-up layout <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Technical Considerations: Prompting

[[integrating_ai_features_in_app_development | Integrating AI features in app development]] and [[api_usage_in_ai_app_development | API usage in AI app development]] requires careful prompting:

*   **Role Assignment**: When using [[API Usage in AI App Development | APIs]] like ChatGPT, it's crucial to assign a specific role to the AI (e.g., "You are a doctor") to guide its responses <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
*   **Circumventing Disclaimers**: Directly asking ChatGPT for medical diagnosis will trigger disclaimers <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. A workaround involves framing the request within a fictional context, like a "movie script," to get a diagnostic response <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>.
*   **Function Calls**: Using function calls in the API allows developers to specify the desired output format, ensuring only the relevant diagnostic information is returned <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.
*   **Accuracy**: Yagari stresses the importance of accuracy in the AI model, differentiating Dr AI from basic GPT wrappers <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>. For example, [[cal_ai_app|Cal AI]] uses a complex pipeline of multiple prompts to ensure accurate calorie estimations from images, avoiding errors that could negatively impact users <a class="yt-timestamp" data-t="00:47:18">[00:47:18]</a>.

## Marketing and Growth Strategy

[[role_of_ai_in_product_development_and_marketing_for_apps | The role of AI in product development and marketing for apps]] is considered from the outset:

*   **Designing for Influencer Marketing**: The app's design takes into account how influencers will showcase it, ensuring clarity and a "wow factor" within a short video clip <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. The "Scan Skin" feature is identified as the primary "wow factor" <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Branding Placement**: The app's name ("Dr AI") should be prominently displayed on key screens, especially those most likely to be shown in marketing materials, like the scanning screen and result screen <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>.
*   **Shareability**: While some apps thrive on high shareability (e.g., social media posts), utility apps like Dr AI might have low shareability for private health matters <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. Growth is more likely through word-of-mouth recommendations among friends or parents <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   **Target Audience and Influencer Selection**: The primary target audience for Dr AI is identified as concerned parents <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>. Marketing efforts would focus on mom influencers, leveraging scenarios where the app helps alleviate parental anxiety about their child's symptoms <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>. When selecting influencers, it's crucial to analyze their audience through comments, not just their niche <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>.
*   **Pricing Strategy**:
    *   **Weekly Model**: A weekly subscription model, possibly around $4/week, is suggested to capitalize on repeat users who may subscribe only when needed <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>. This model has proven effective for other utility AI apps like Riz GPT <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
    *   **AB Testing**: Zach emphasizes extensive AB testing of various pricing structures (weekly, monthly, annual, with/without free trials) to find the highest "proceeds per download" <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>.
*   **Influencer Compensation**: Payment for influencers is typically upfront, not per view <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. To ensure profitability (RPM > CPM), it's essential to predict likely views and set a budget, e.g., paying an influencer under $5,000 for 1 million views based on a $5 RPM <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>.

This detailed blueprint for Dr AI serves as a comprehensive guide for anyone looking to build a consumer-facing [[ai_driven_mobile_app_startup_ideas | AI driven mobile app startup ideas]], especially for health and wellness applications.