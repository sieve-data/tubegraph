---
title: Developing health diagnosis apps using AI
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old entrepreneur behind the successful AI startup Cal AI, shares an in-depth blueprint for an [[ai_app_startups_and_ideas | AI startup idea]] called "Dr. AI," a health diagnosis mobile application powered by artificial intelligence <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="01:06:07">[01:06:07]</a>. The goal is to enable individuals to quickly assess potential health concerns and determine if professional medical attention is necessary <a class="yt-timestamp" data-t="05:21:07">[05:21:07]</a>.

## The "Dr. AI" Concept

The inspiration for Dr. AI stemmed from a friend's experience where a scraped knee led to an unexpected skin cancer diagnosis, highlighting the coincidental nature of discovering serious health issues <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>, <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This sparked the idea for a tool that could provide quick, initial assessments of skin marks or rashes, similar to how Cal AI uses AI for calorie tracking from a picture <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>, <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

The app aims to address significant healthcare access issues, particularly in regions like the US, where many are uninsured, or in countries like Canada, where healthcare systems are often bogged down, leaving millions without access to primary doctors <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Core Features

Dr. AI proposes three main features leveraging [[incorporating_ai_features_in_applications | AI features]]:
1.  **Skin Scan**: Users can take a picture of a skin mark or rash for identification, determining if it's potentially harmful or benign <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>, <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. The result would include a "danger level" (e.g., 0-5) and a diagnosis from the AI, advising whether to see a doctor or wait it out <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>, <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
2.  **Symptoms Quiz**: A conversational quiz where users input symptoms (e.g., "dry cough," "chills") to receive potential sickness possibilities, possibly ranked by likelihood <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>, <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
3.  **Chatbot**: A general AI chatbot for asking any health-related questions <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>, <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. Studies show that ChatGPT can be effective at diagnosing medical problems, even outperforming doctors in some areas <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>, <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>, <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

> [!WARNING] Disclaimers are crucial: The app's diagnoses would be heavily disclaimed as not 100% accurate, aiming to provide guidance on whether to consult a doctor, rather than definitive diagnoses <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>, <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

## Designing the User Experience (UX)

Zach Yagari emphasizes starting with basic framing for app design, typically doing the UX sketching oneself before hiring designers to refine it <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>, <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

Key design principles for Dr. AI:
*   **Simple Navigation**: A straightforward navigation bar with Home, Settings, and potentially a central feature <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>, <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.
*   **Feature Buttons**: Three prominent buttons for the main features: Scan, Chat, and Symptoms Quiz <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>, <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>.
*   **History Log**: A scrollable log, inspired by Cal AI, displaying previous chats, scans, and quiz results <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>, <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This history creates an investment in the product, making users less likely to switch to competitors <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>, <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. It can also be shared with a doctor <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Scanning Screen**: A simple camera screen with an upload option from the camera roll and visual scanning lines, similar to Cal AI or Photo Math <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>, <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>, <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
*   **Background Processing**: Instead of an "analyzing" screen, users are immediately returned to the home screen while the AI processes, with a loading indicator <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>, <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.
*   **Digestible Results**: Presenting information simply, such as a 0-5 "danger level" for scans, rather than verbose text <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>, <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>.
*   **Follow-up Options**: For scan results, an "Ask Question" button allows users to start a chat for deeper inquiries or follow up on changes over time <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>, <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.
*   **Gamification/Simplicity**: Design choices like danger levels or multiple-choice questions for quizzes make the app more digestible and engaging <a class="yt-timestamp" data-t="16:24:00">[16:24:00]</a>, <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>, <a class="yt-timestamp" data-t="21:35:00">[21:35:00]</a>.
*   **Referencing Existing "Primitives"**: When designing, looking at similar successful apps (like Cal AI or Riz GPT) for established UI elements and "primitives" (building blocks) can simplify the process <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>, <a class="yt-timestamp" data-t="10:18:00">[10:18:19]</a>.

## AI Prompting and Accuracy

To make the AI function effectively for diagnosis, careful prompting is essential to overcome standard disclaimers from models like ChatGPT <a class="yt-timestamp" data-t="29:53:00">[29:53:00]</a>.

*   **Role-Playing**: Instructing the AI to "take on the role of a doctor" or act as if it's for a "movie script" can bypass standard disclaimers and elicit more direct medical responses <a class="yt-timestamp" data-t="30:54:00">[30:54:00]</a>, <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.
*   **Scientific and Layman Terms**: Prompts should request diagnoses in both scientific terms (for potential doctor reference) and easy-to-understand language for the user <a class="yt-timestamp" data-t="29:18:00">[29:18:00]</a>, <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.
*   **API vs. Chatbot**: [[building_apps_with_ai_tools | Using the API directly]] offers more control over prompts compared to a general chatbot interface, allowing for precise output formatting <a class="yt-timestamp" data-t="32:29:00">[32:29:00]</a>.
*   **Function Calls**: Using function calls can direct the AI's response to specific variables, ensuring only the desired diagnostic text is captured <a class="yt-timestamp" data-t="32:38:00">[32:38:00]</a>, <a class="yt-timestamp" data-t="32:41:00">[32:41:00]</a>.
*   **Accuracy**: Crucially, like Cal AI, Dr. AI must prioritize accuracy through complex prompting pipelines, rather than simple GPT wrappers, to avoid potentially harmful misinformation <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>, <a class="yt-timestamp" data-t="47:18:00">[47:18:00]</a>.

## Go-to-Market Strategy: Influencer Marketing

The primary [[using_ai_tools_for_saas_development | marketing strategy]] for Dr. AI, given its low shareability (people may not want to share personal health issues), would be through paid ads and influencer marketing <a class="yt-timestamp" data-t="18:57:00">[18:57:00]</a>, <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>, <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.

*   **Design for Marketing**: The app's design should be simple and clear enough for quick comprehension in short influencer videos (e.g., 2 seconds) <a class="yt-timestamp" data-t="26:01:00">[26:01:00]</a>, <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a>.
*   **Branding Placement**: Displaying the app's name, "Dr. AI," prominently on the homepage and especially on the "wow factor" screens (like the scanning result screen) is vital for brand recognition in marketing content <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>, <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>, <a class="yt-timestamp" data-t="27:45:00">[27:45:00]</a>.
*   **Identify Target Audience**: For Dr. AI, concerned mothers are identified as a prime demographic <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>, <a class="yt-timestamp" data-t="37:26:00">[37:26:00]</a>.
*   **Find Influencers**: Search platforms like TikTok for influencers whose *audience* matches the target demographic, even if the influencer's niche differs <a class="yt-timestamp" data-t="35:18:00">[35:18:00]</a>, <a class="yt-timestamp" data-t="37:36:00">[37:36:00]</a>. Reading comments sections helps assess audience demographics <a class="yt-timestamp" data-t="35:32:00">[35:32:00]</a>.
*   **Create Compelling Angles**: Influencers should tell a relatable story, such as a parent using the app to quickly check a child's bump, alleviating fear and showing the app's utility <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>, <a class="yt-timestamp" data-t="39:19:00">[39:19:00]</a>.
*   **Pricing for Influencers**: Deals are structured based on CPM (cost per thousand views), ensuring RPM (revenue per thousand views) is higher than CPM for profitability <a class="yt-timestamp" data-t="41:16:00">[41:16:00]</a>, <a class="yt-timestamp" data-t="41:45:00">[41:45:00]</a>. This requires predicting likely views from the influencer's audience <a class="yt-timestamp" data-t="41:51:00">[41:51:00]</a>.

## Pricing Model

Dr. AI is well-suited for a weekly pricing model without a free trial, capitalizing on "repeat users" who subscribe on a need-basis <a class="yt-timestamp" data-t="43:06:00">[43:06:00]</a>, <a class="yt-timestamp" data-t="43:11:00">[43:11:00]</a>, <a class="yt-timestamp" data-t="43:52:00">[43:52:00]</a>.

*   **Need-Based Usage**: Users might download, subscribe for a quick scan, unsubscribe, and then resubscribe later when another problem arises <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>, <a class="yt-timestamp" data-t="43:30:00">[43:30:00]</a>, <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>, <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>.
*   **Pricing Sweet Spot**: Recommend testing weekly prices like $4 or $7, but also monthly and annual options <a class="yt-timestamp" data-t="45:18:00">[45:18:00]</a>, <a class="yt-timestamp" data-t="45:40:00">[45:40:00]</a>.
*   **AB Testing**: Use tools like Superwall to AB test different pricing points and free trial variations to determine the highest proceeds per download <a class="yt-timestamp" data-t="44:47:00">[44:47:00]</a>, <a class="yt-timestamp" data-t="45:36:00">[45:36:00]</a>, <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a>.

## Ethical Considerations and Call to Action

It is paramount that [[using_ai_in_mobile_apps | AI applications]] for health, like Dr. AI, include clear disclaimers, as giving medical advice without them is unethical and could lead to serious consequences if inaccurate <a class="yt-timestamp" data-t="46:52:00">[46:52:00]</a>. The accuracy of AI responses is critical, especially when dealing with health data; developers must ensure their AI models are highly accurate, not just simple wrappers <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>, <a class="yt-timestamp" data-t="47:22:00">[47:22:00]</a>.

Zach Yagari encourages aspiring entrepreneurs to take this idea and build it, emphasizing the potential to "make the world a better place with Dr. AI" <a class="yt-timestamp" data-t="46:45:00">[46:45:00]</a>, <a class="yt-timestamp" data-t="46:47:00">[46:47:00]</a>, <a class="yt-timestamp" data-t="46:49:00">[46:49:00]</a>.