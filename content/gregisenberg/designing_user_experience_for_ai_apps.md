---
title: Designing user experience for AI apps
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Designing intuitive and effective user experiences is crucial for the success of artificial intelligence (AI) applications. This article explores key principles and strategies for [[ai_product_designers | designing AI apps]], drawing insights from the development of successful platforms like Cal AI and conceptualizing new ideas like Dr. AI.

## The Vision: Dr. AI
Zach Yagari, the 17-year-old founder of Cal AI, an [[using_ai_for_app_development | AI startup]] generating over $1 million a month in revenue, suggests an AI app concept called Dr. AI [00:00:06]. This app aims to offer quick preliminary diagnoses and advice based on user input, addressing issues such as lack of insurance or overwhelmed healthcare systems [00:03:22]. Dr. AI is envisioned as more than a simple GPT wrapper, designed for rapid development and launch within a month [00:01:28].

### Core Features
Dr. AI would include three main functionalities:
1.  **Skin Scan**: Users can take a picture of a skin mark or rash for identification, determining if it's harmful or benign [00:03:49].
2.  **Symptoms Quiz**: Users input symptoms (e.g., cough, chills) and receive a list of possible sicknesses, potentially ranked by likelihood [00:04:00].
3.  **Chatbot**: A general medical chatbot for answering user questions [00:04:18].

### Disclaimers and Accuracy
It's vital for such an app to include strong disclaimers, clarifying that diagnoses are not 100% accurate and are meant to guide users on whether a doctor's visit is necessary [00:03:09]. While AI models like ChatGPT are highly capable at diagnosing medical problems, they can still "hallucinate" [00:04:27]. Accuracy is paramount to avoid misleading users, unlike some basic GPT wrappers that may be inaccurate [00:46:58].

## UX Design Principles
When [[using_ai_tools_for_product_design | designing the UX]] for an AI app, several principles ensure clarity, user engagement, and value.

### 1. Simple Framing and Navigation
The initial design process involves creating a basic framework with clear navigation [00:05:43]. A typical structure might include a navigation bar with "Home" and "Settings," along with direct access to the app's core features [00:06:11]. For Dr. AI, this would be "Scan," "Chat," and "Symptoms Quiz" [00:06:26].

### 2. User Investment Through History
A "History" feature, similar to Cal AI's food logging, is essential for user retention and investment [00:06:47]. This section would log previous chats, scan results, and symptom quizzes, allowing users to track their health inquiries over time [00:07:06]. This historical data also serves as a digestible summary that users could share with actual doctors [00:08:28].

### 3. Leveraging "Primitives" for Inspiration
When designing a new AI app, it's beneficial to look at existing applications for inspiration, especially in areas where direct competitors are scarce [00:09:08]. The concept of "primitives"—the fundamental building blocks of an app—is key [00:10:18]. For example, the scanning screen or chatbot UI does not need to be reinvented; existing successful designs (like those in PhotoMath or general chatbots) can be repurposed and adapted to the specific use case [00:12:22].

### 4. Efficient Loading Experiences
Avoid making users wait on empty "analyzing" screens, especially when AI processing can take 30-60 seconds [00:13:03]. Instead, return the user to the home screen immediately, indicating that the process is loading in the background [00:13:17]. This prevents user frustration and improves the overall experience [00:13:27].

### 5. Presenting Results Clearly
Scan results should prioritize key information, such as a "danger level" (e.g., 0-5 scale) and a concise diagnosis [00:14:06]. The original image should be displayed alongside the AI's analysis [00:14:19]. The diagnosis should be presented in both scientific and easy-to-understand terms, allowing users to potentially show the information to medical professionals [00:29:18]. Users should also have the option to follow up with the chatbot directly from a result for deeper inquiry [00:15:22].

### 6. Gamification and Digestibility
Presenting information in a gamified or easily digestible format, such as a numerical "danger level," makes it more understandable for users [00:16:24]. This approach also benefits [[using_marketing_strategies_for_aibased_apps | marketing]], as it allows potential users to quickly grasp the app's value in short influencer videos [00:26:11].

## [[implementing_ai_in_app_development_processes | Implementing AI in App Development Processes]]
### AI Prompting
Effective prompting is crucial for accurate and helpful AI responses. Instead of simple requests, structure prompts to assign a specific "role" to the AI, such as "You are a doctor..." [00:29:02]. To bypass AI disclaimers (e.g., "I am not a medical doctor"), creative prompt engineering can be used, like framing the request as part of a "movie script" [00:31:16]. For direct API usage, function calls can be used to assign AI responses to specific variables, ensuring only the desired output is returned [00:32:38].

## Marketing and Growth Considerations
[[using_marketing_strategies_for_aibased_apps | Marketing strategies]] are intertwined with app design, especially for [[building_a_social_media_app_with_ai | consumer AI apps]].

### Sharability
While some AI apps might have high shareability (e.g., social media apps), a utility app like Dr. AI might have low direct shareability of results due to privacy concerns [00:18:16]. However, it could still spread through word-of-mouth among target demographics, such as concerned parents sharing the app's utility with friends [00:19:16].

### Influencer Marketing & "Wow Factor"
Designing with influencer marketing in mind involves thinking about what the "wow factor" of the app will be [00:27:07]. For Dr. AI, the "scan skin" feature with an immediate danger level and diagnosis is the most marketable aspect [00:27:36]. Branding (e.g., prominently displaying "Dr. AI" on key screens) ensures viewers instantly recognize the app [00:26:41].

When selecting influencers, it's crucial to analyze their audience, not just their niche [00:35:18]. For Dr. AI, targeting "mom" influencers whose audience is likely concerned parents would be effective [00:37:18]. Marketing narratives could leverage common fears and anxieties, presenting the app as a solution to quickly assess health concerns [00:36:30].

## Pricing Strategy for AI Apps
Pricing for AI apps, especially those serving intermittent needs, can be strategic. A weekly pricing model (e.g., $4-$7 per week) with no free trial can capitalize on "repeat users" who might subscribe on an as-needed basis [00:43:06]. This model has proven successful for other AI-based apps where users return only when they face a specific problem [00:44:00]. A/B testing various pricing structures (weekly, monthly, annual, with/without trials) is essential to find the optimal "proceeds per download" [00:45:57].

## [[challenges_and_solutions_in_ai_app_development | Challenges and Solutions in AI App Development]]
One of the primary [[challenges_and_solutions_in_ai_app_development | challenges]] in [[using_ai_for_app_development | building a SaaS app using AI]] is ensuring the accuracy of the AI model, especially in sensitive areas like medical diagnoses [00:47:01]. Developers must go beyond basic prompting, creating complex "pipelines" of prompts to refine responses and ensure reliability [00:47:20]. Ethical considerations, such as clear disclaimers, are non-negotiable [00:46:52].