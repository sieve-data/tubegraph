---
title: Healthcare apps with AI
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

The concept of "Dr. AI" is presented as an [[innovative_app_ideas_using_ai | innovative app idea using AI]] that could be rapidly built and launched as a full business in under a month <a class="yt-timestamp" data-t="01:32:41">[01:32:41]</a>. It is described as an [[ai_app_development | AI app development]] project that is more than a simple GPT wrapper <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>.

## Inspiration and Problem Solved
The idea for Dr. AI emerged from a personal anecdote where a friend discovered skin cancer due to a knee injury <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This highlighted the common concern about unidentified skin issues and the desire for quick, accessible diagnoses without needing a doctor's visit <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. The app aims to address challenges in healthcare systems, such as uninsured individuals in the US or bogged-down systems like Canada, where millions lack access to primary doctors <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. The primary goal is to help users determine if a condition is safe to wait out or if a doctor's visit is immediately necessary <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

## Core Features
Dr. AI proposes three main features:
*   **Skin Scan/Identification** <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>: Users can take a picture of something on their skin or body for identification, determining if it's harmful or benign <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This feature would include a "danger level" metric (e.g., 0-5) and a diagnosis based on the image <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Symptoms Quiz** <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>: Users input symptoms (e.g., cough, chills), and the app provides possible sicknesses, potentially with a likely percentage chance for each, ranked <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. The quiz would be structured with multiple-choice questions <a class="yt-timestamp" data-t="21:46:00">[01:46:00]</a>.
*   **Chatbot** <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>: A general AI chatbot for users to ask any health-related questions <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. This feature benefits from ChatGPT's capability in diagnosing medical problems, with studies showing its proficiency in various areas <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

## Design and User Experience (UX)
The design philosophy emphasizes simplicity and digestibility <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. Key elements include:
*   **Navigation Bar**: A basic navigation bar with "Home" and "Settings" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
*   **Feature Buttons**: Three prominent buttons for "Scan," "Chat," and "Symptoms Quiz" <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   **History Log**: A scrollable "in-script feed" similar to Cal AI, displaying previous chats, scans, and quiz results <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. This history also serves as a user investment, encouraging retention, and can be shared with actual doctors <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   **Scan Process**: A simple camera screen for scanning skin, including an upload option from the camera roll and scanning lines <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. To improve user experience, instead of a traditional analyzing screen, the app immediately returns the user to the home screen with a loading indicator, preventing forced waiting <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.
*   **Result Screen**: Displays the scanned image, a "danger level" (0-5) for easy understanding, and a diagnosis. A "Ask Question" button allows users to delve deeper into their specific problem, even after leaving the app and returning later <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>.
*   **Primitives**: The approach to UX design involves leveraging existing "Primitives" or building blocks from other successful apps (e.g., Cal AI, Riz GPT's three-feature popup, PhotoMath's scanning screens), repurposing them for the specific use case <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Gamification**: While not explicitly designed for gamification, the simple, digestible presentation (like the "danger level" metric) makes the app feel somewhat gamified, which is beneficial for user understanding and marketing <a class="yt-timestamp" data-t="16:24:00">[16:24:00]</a>.

## AI Implementation and Prompting
[[integrating_apis_in_ai_app_development | Integrating APIs in AI app development]], specifically with GPT models, requires strategic prompting:
*   **Role Assignment**: The AI should be prompted to "take on the role of a doctor" to guide its responses <a class="yt-timestamp" data-t="29:57:00">[29:57:00]</a>.
*   **Bypassing Disclaimers**: To circumvent common AI disclaimers ("I am not a medical doctor"), a workaround like asking the AI to respond "as part of a movie script" is suggested <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.
*   **Output Clarity**: The output should combine scientific terms (for doctors) with easily understandable language for regular users <a class="yt-timestamp" data-t="29:20:00">[29:20:00]</a>.
*   **Function Calls**: Using function calls in the API can ensure the AI assigns its response to a specific variable, providing only the desired output <a class="yt-timestamp" data-t="32:38:00">[32:38:00]</a>.
*   **Accuracy**: Crucially, the app must prioritize accuracy through detailed prompting pipelines to avoid inaccurate diagnoses, unlike some simpler GPT wrappers <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>.

## Go-to-Market Strategy and Marketing
The strategy for marketing Dr. AI focuses on [[opportunities_in_ai_and_consumer_mobile_applications | opportunities in AI and consumer mobile applications]], particularly through influencer marketing:
*   **Branding**: The app's name, "Dr. AI," should be prominently displayed on the homepage and especially on key "wow factor" screens like the scanning and results pages <a class="yt-timestamp" data-t="26:41:00">[26:41:00]</a>.
*   **Influencer Selection**:
    *   Focus on TikTok <a class="yt-timestamp" data-t="30:29:00">[30:29:00]</a>.
    *   Prioritize influencers whose audience aligns with the target demographic, even if the influencer's niche is different <a class="yt-timestamp" data-t="35:18:00">[35:18:00]</a>. For Dr. AI, concerned parents (specifically moms) are identified as the primary target audience <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>.
    *   Audience analysis is done by manually reading comments on influencer posts <a class="yt-timestamp" data-t="35:32:00">[35:32:00]</a>.
*   **Content Angle**: Influencer content should play on emotions, using "fear-mongering" tactics by presenting a scenario where a user (or their child) is scared about a mark, scans it with Dr. AI, and finds out it's harmless <a class="yt-timestamp" data-t="36:30:00">[36:30:00]</a>. This demonstrates the app's value proposition of alleviating worry or prompting necessary action <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>.
*   **Shareability**: While specific medical results may have low direct shareability (e.g., users won't post a bump on social media), the app's concept can spread through word-of-mouth among parents <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>.
*   **Influencer Compensation**:
    *   Compensation is typically upfront, not pay-per-view <a class="yt-timestamp" data-t="41:31:00">[41:31:00]</a>.
    *   Calculate potential profitability by ensuring Revenue Per Mille (RPM - revenue per thousand views) is greater than Cost Per Mille (CPM - cost per thousand views) <a class="yt-timestamp" data-t="41:45:00">[41:45:00]</a>.
    *   Estimate likely views based on past performance and set a deal (e.g., four posts a month averaging 250K views each for 1 million total views) <a class="yt-timestamp" data-t="41:59:00">[41:59:00]</a>.
    *   A starting RPM of $5 is suggested, meaning a cost under $5,000 for 1 million views is considered profitable <a class="yt-timestamp" data-t="42:19:00">[42:19:00]</a>.

## Pricing Strategy
For [[business_opportunities_using_ai_technologies | business opportunities using AI technologies]] like Dr. AI, a weekly pricing model is recommended <a class="yt-timestamp" data-t="43:06:00">[43:06:00]</a>:
*   **Rationale**: Since it's a utility app for infrequent, on-demand use, weekly pricing capitalizes on "repeat users" who might subscribe, unsubscribe, and resubscribe as needed <a class="yt-timestamp" data-t="43:13:00">[43:13:00]</a>. This is similar to [[innovative_ai_dating_apps | innovative AI dating apps]] like Riz GPT, where users subscribe only when they need specific advice <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.
*   **Price Points**: Suggested weekly prices are $4 or $7 <a class="yt-timestamp" data-t="45:18:00">[45:18:00]</a>.
*   **No Free Trial**: A crucial element is often no free trial, as this maximizes initial capitalization <a class="yt-timestamp" data-t="43:52:00">[43:52:00]</a>.
*   **A/B Testing**: Crucially, extensive A/B testing using tools like Superwall is vital to determine the optimal pricing, including weekly, monthly, and yearly options, with or without free trials, to find the highest "proceeds per download" <a class="yt-timestamp" data-t="44:47:00">[44:47:00]</a>.

## Best Practices for Development
*   **Rapid Prototyping**: Start with bare-bones UX sketches and then hire a designer (e.g., from Upwork) to refine them <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   **MVP Focus**: The initial design should be solid enough for a Minimum Viable Product (MVP) to be handed off to a designer <a class="yt-timestamp" data-t="28:29:00">[28:29:00]</a>.
*   **Ethical Considerations**: Always include clear disclaimers that the app's diagnosis is not 100% accurate and is not a substitute for professional medical advice <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This is a critical aspect of [[best_practices_for_utilizing_ai_tools_in_app_development | best practices for utilizing AI tools in app development]].
*   **Accuracy is Key**: Ensure the AI's responses are highly accurate, using complex prompting pipelines if necessary, to avoid misleading users, especially in a sensitive area like healthcare <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>.