---
title: Development of a healthfocused AI app
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old entrepreneur who built an AI startup called Cal AI, generating over $1 million a month in revenue, shares a complete AI startup idea called "Dr. AI" from concept to market strategy <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This idea, similar to Cal AI, is designed to be built and launched as a full business in less than a month <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## The Inspiration for Dr. AI

The idea for Dr. AI stemmed from a personal anecdote involving a friend who discovered skin cancer coincidentally after scraping his knee in the same spot <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This made Yagari reflect on the common concern of unexplained skin marks or rashes and the desire for quick, accessible medical insights without immediately needing a doctor's visit <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The app aims to address issues like lack of insurance in the US or overloaded healthcare systems in places like Canada, where many lack access to primary doctors <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

The core purpose of Dr. AI is not to provide definitive diagnoses, but to offer an initial assessment that helps users decide if a doctor's visit is immediately necessary or if they can safely wait a few days <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Core Features of Dr. AI

Dr. AI is designed with three main features:
1.  **Skin Scan**: Users can take a picture of something on their skin or body for identification, determining if it's potentially harmful or benign <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
2.  **Symptoms Quiz**: Users input their symptoms (e.g., dry cough, chills), and the app suggests possible illnesses with a likelihood percentage for each <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Chatbot**: A general AI chatbot for asking any medical questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. ChatGPT has shown strong capabilities in diagnosing medical problems, even outperforming doctors in some studies <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## User Experience (UX) and Design

Yagari's approach to UX design emphasizes simplicity and digestibility <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. He typically sketches out the basic framing and then hires a designer to refine it <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.

### Key Design Elements:
*   **Navigation Bar**: A straightforward navigation bar with Home and Settings <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Feature Buttons**: Three prominent buttons for Scan, Chat, and Symptoms Quiz on the home screen <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History Log**: A scrollable log, inspired by Cal AI, that displays previous chats, scans, and symptom quiz results. This creates user investment and aids retention, as users will want to stick with the app where their history is stored <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This history could also be shared with a doctor for a faster diagnosis <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Scanning Screen**: A simple camera interface for scanning skin, including an upload option from the camera roll <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. It uses scanning lines, a common "primitive" seen in other apps like Photomath <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>, <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Result Screen**: Instead of an analyzing screen that forces users to wait, the app returns to the home screen with a loading indicator while the AI processes <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. The results show the scanned image, a "danger level" (e.g., 0-5), and a diagnosis from the chatbot <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. Users can then "Ask Question" to dive deeper into that specific issue, enhancing [[embedding_ai_to_enhance_app_functionality | app functionality]] and retention <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Symptoms Quiz Flow**: Designed as a series of multiple-choice questions for better digestibility, rather than a checkbox list <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
*   **Chatbot Preview**: The history shows a preview of the last chatbot message <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. The chat interface itself can mimic existing chatbot UIs <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
*   **Gamification**: While not intentionally gamified, presenting information like "danger level" on a 0-5 scale makes it highly digestible, similar to game design <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

## Technical Implementation (Prompting AI)

A significant [[challenges_and_solutions_in_ai_app_development | challenge]] in [[building_apps_with_ai_tools | building apps with AI tools]] like this is prompting the AI to bypass its default disclaimers (e.g., "I'm not a medical doctor") and provide useful information <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. Yagari demonstrates a "movie script" workaround, asking the AI to respond *as if* it were a doctor in a fictional scenario <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>. When [[embedding_ai_to_enhance_app_functionality | using the AI API directly]], developers can assign specific roles and use function calls to extract only the desired information into a variable, avoiding extraneous text <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. The app should provide diagnoses in both scientific terms (for doctors) and easy-to-understand terms (for users) <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. Incorporating sources for AI responses would also be valuable <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Go-to-Market Strategy: Influencer Marketing

The [[integration_of_ai_in_app_development_and_marketing | marketing strategy]] for Dr. AI primarily relies on influencer marketing and paid ads, as the app has low direct shareability (users are unlikely to share pictures of their medical conditions) <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. Word-of-mouth growth might occur among parents sharing the app's utility, but paid channels will be crucial <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

### Key Marketing Considerations:
*   **Clarity and Simplicity**: The app's design must be simple enough for a viewer to understand its value within a 2-second glimpse in an influencer video <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>.
*   **Branding**: The app's name ("Dr. AI") should be prominently displayed on the home screen and especially on the "wow factor" screens, like the scanning result <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   **"Wow Factor"**: The skin scanning feature, particularly showing the scan and its danger level diagnosis, is identified as the biggest "wow factor" for marketing <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>.
*   **Target Audience**: The primary target audience is concerned parents, especially mothers <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.
*   **Influencer Selection**: Identify influencers whose *audience* matches the target demographic, even if the influencer's niche seems different <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. Yagari suggests looking for "mom of seven" type influencers and exploring their followers or "similar accounts" for more leads <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
*   **Content Angle**: Influencers should tell a realistic story of concern (e.g., a child getting a bump) and how Dr. AI quickly provided reassurance or guidance <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.
*   **Influencer Pricing**: Deals are typically structured as upfront payments for multiple posts (e.g., four posts a month) <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. Profitability is determined by ensuring RPM (revenue per thousand views) is greater than CPM (cost per thousand views) <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>. Yagari aims for an RPM of $5 and tries to keep CPM under that <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.

## Pricing Model

The recommended pricing model for Dr. AI is a weekly subscription, likely around $4 a week, with no free trial <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>. This model capitalizes on "repeat users" who might unsubscribe after a single use but resubscribe whenever a new medical concern arises <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>. This is common for other [[developing_ai_character_apps_with_customization | AI character apps]] or [[building_a_social_app_with_ai | AI wingman apps]] where users return on a "need basis" <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

Yagari recommends extensive A/B testing using tools like Superwall to find the optimal price point and trial variations (e.g., $4/week, $7/week, monthly, yearly, with/without free trials) to maximize proceeds per download <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.

## Ethical Considerations and Accuracy

A critical aspect of [[innovative_ai_functionalities_in_apps | developing AI character apps with customization]] in the health sector is the ethical responsibility to include clear disclaimers, stating that the app's advice is not 100% accurate <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>, <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>. Furthermore, ensuring the AI's accuracy is paramount. Unlike many "GPT wrappers" that offer basic prompts, a reliable health app requires a complex "pipeline" of prompts and data processing to achieve high accuracy, preventing potentially harmful misinformation <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

This detailed roadmap and go-to-market strategy provide a blueprint for anyone looking to build and market a health-focused AI app quickly, emphasizing user experience, strategic AI prompting, and targeted marketing <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.