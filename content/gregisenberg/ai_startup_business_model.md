---
title: AI Startup Business Model
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

This article provides an in-depth look into the thought process of Zach Yagari, a 17-year-old entrepreneur who built an [[ai_apps_and_ai_startups | AI app]] generating over $1 million a month in revenue <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Yagari shares a complete blueprint for another [[ai_startup_ideas | AI startup idea]] called Dr. AI, covering everything from design and user experience to growth, pricing, and essential tools <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Introducing Dr. AI: A Medical AI App

Dr. AI is an [[ai_apps_and_ai_startups | AI app]] designed to offer quick, preliminary medical insights based on user input <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The idea for Dr. AI stemmed from a friend's experience with a skin issue that coincidentally led to a skin cancer diagnosis, highlighting the need for easily accessible initial assessments <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

The app aims to address common issues like concerns over skin marks or rashes, especially in regions with healthcare access challenges, such as uninsured individuals in the US or long wait times in countries like Canada <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Key Features of Dr. AI

Dr. AI would feature three main functionalities:
1.  **Skin Scan:** Users can take a picture of a skin mark or rash to get an identification and an assessment of whether it's harmful or benign <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This feature would include a "danger level" metric (e.g., 0-5) and a diagnosis from the AI, heavily disclaimed as not 100% accurate, but indicating if a doctor's visit is recommended <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Users could also initiate a follow-up chat about their scan <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
2.  **Symptoms Quiz:** Users answer a series of multiple-choice questions about their symptoms (e.g., "Do you have a cough?", "Is it a dry cough?") <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The AI would then provide possible sicknesses with a likelihood percentage <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Chatbot:** A general health chatbot for users to ask any medical questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This feature leverages the diagnostic capabilities of GPT technology, which has shown to perform well in medical problem diagnosis <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

It is crucial for Dr. AI to include disclaimers, making it clear that it's not a substitute for professional medical advice <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The primary goal is to help users decide if they should seek immediate medical attention or if it's safe to wait <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## UX and Product Design Philosophy

Yagari's design process for [[ai_apps_and_ai_startups | AI apps]] emphasizes simplicity and digestibility <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. He starts with basic framing and sketches, then hires a professional designer to refine his "bad designs" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Key design principles include:
*   **Navigation:** A simple navigation bar with "Home," "Settings," and potentially other core features <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Feature Buttons:** Clear buttons for the three main features: Scan, Chat, and Symptoms Quiz <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History Log:** An "in-script feed" or log of previous interactions (chats, scans, quiz results) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This feature builds user investment and retention, as their data is stored within the app <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This history could even be made digestible for sharing with a doctor <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Analyzing Screen:** Instead of making users wait on a loading screen, the app should return them to the home screen while analysis happens in the background, providing a loading indicator <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **"Primitives" Concept:** When designing a new app, Yagari looks at existing similar apps or successful [[ai_apps_and_ai_startups | AI apps]] (like Cal AI and Riz GPT) for established UI "Primitives" or building blocks (e.g., scanning screens, chatbot interfaces) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These can be repurposed for the new use case, rather than reinventing the wheel <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Gamification (Digestibility):** While not explicitly aiming for gamification, making information digestible (e.g., a 0-5 danger level scale) naturally aligns with game design principles and improves user understanding <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

## AI Prompting and Accuracy

A significant challenge for a medical [[ai_apps_and_ai_startups | AI app]] like Dr. AI is overcoming the generic disclaimers from AI models like ChatGPT <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. To get a useful diagnosis, Yagari suggests creative prompting, such as:
*   **Role Assignment:** Tell the AI to "take on the role of a doctor" <a class="yt-timestamp" data-t="00:30:54">[00:30:54]</a>.
*   **Contextual Framing:** Frame the request as part of a "movie script" where the AI is acting as a doctor, clearly stating that it's "not real" <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>.
*   **API vs. Chatbot:** Using the AI's API directly offers more control over the prompt, allowing for precise output formatting (e.g., using a function call to assign the diagnosis to a specific variable) <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

It is crucial for [[ai_apps_and_ai_startups | AI startups]] to prioritize accuracy, even if it means complex prompt pipelines, to avoid providing misleading information that could harm users (e.g., a calorie-tracking app being inaccurate) <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

## Go-To-Market Strategy: Influencer Marketing

Zach Yagari's primary go-to-market strategy for [[ai_apps_and_ai_startups | AI apps]] is influencer marketing, particularly on platforms like TikTok <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

### Key Considerations for Influencer Marketing:
*   **Clarity and Simplicity:** The app must be clear and simple enough for a viewer to understand its value within a 2-second phone screen appearance in an influencer video <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.
*   **Branding:** Prominently display the app's name (e.g., "Dr. AI") on the homepage and especially on "wow factor" screens that influencers are likely to feature, such as the scanning or results screens <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   **Identifying Target Audience:** Focus on the influencer's *audience* rather than just their niche <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. For Dr. AI, concerned parents (especially mothers) are a key target <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>. This often means finding "mom influencers" and analyzing their comments to confirm their audience demographic <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>.
*   **Video Angles:** Create realistic, emotion-driven narratives. For example, a mom influencer could share a story about a scare with their child's bump on the skin, using Dr. AI to alleviate fears or confirm a need for a doctor, leading to a "long story short, I'm okay now" type of resolution <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.
*   **Shareability:** While Dr. AI might not have high organic shareability (e.g., users sharing scan results), it could spread through word-of-mouth among parents sharing the *idea* of the app <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. Paid ads are therefore crucial <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Reaching Out:** Contact influencers via both email and direct message <a class="yt-timestamp" data-t="00:40:57">[00:40:57]</a>.

### Influencer Pricing Structure (RPM vs. CPM)
*   **RPM (Revenue Per Mille/Thousand Views):** The revenue generated per thousand views on an influencer's post <a class="yt-timestamp" data-t="00:41:16">[00:41:16]</a>.
*   **CPM (Cost Per Mille/Thousand Views):** The money spent on an influencer post per thousand views <a class="yt-timestamp" data-t="00:41:23">[00:41:23]</a>.
*   **Profitability:** Ensure RPM is greater than CPM for a profitable campaign <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>.
*   **Prediction:** Predict likely views to structure upfront payments <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>. Yagari often aims for four posts a month from an influencer <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. For example, if an influencer averages 250K views per video, four videos would yield 1 million views <a class="yt-timestamp" data-t="00:42:08">[00:42:08]</a>.
*   **Budgeting:** Assuming an initial RPM of $5 (which is measured and adjusted over time), a profitable CPM would be anything under $5,000 for 1 million views <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>.

## App Pricing Strategy

For an app like Dr. AI, which may be used on a "need basis" rather than daily, Yagari suggests a **weekly pricing model with no free trial** <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>.
*   **Rationale:** Users might download, use once for a specific issue, unsubscribe, and then reinstall/resubscribe when another need arises <a class="yt-timestamp" data-t="00:43:30">[00:43:30]</a>. This strategy capitalizes on repeat users who subscribe periodically <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>.
*   **Pricing Tiers:** Recommended starting points are $4 or $7 a week, though $7 is considered steep <a class="yt-timestamp" data-t="00:45:18">[00:45:18]</a>.
*   **AB Testing:** Crucially, Yagari recommends extensive AB testing of various pricing structures (e.g., $4/week, $7/week, monthly, yearly, with and without free trials) to find what yields the highest "proceeds per download" <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. Tools like Superwall can be used for this <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.

## Conclusion for [[ai_startup_ideas | AI Startup Ideas]]

This comprehensive guide from Zach Yagari offers a solid roadmap for not only building a new [[ai_startup_ideas | AI startup idea]] like Dr. AI but also for effectively marketing and monetizing it <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>. The emphasis on user experience, strategic prompting, and a data-driven approach to marketing and pricing provides valuable insights for aspiring [[ai_startup_ideas | AI startup]] founders. It is vital for such apps to include disclaimers and ensure high accuracy to be ethical and beneficial to users <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>.