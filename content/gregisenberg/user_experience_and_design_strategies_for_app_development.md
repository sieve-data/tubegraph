---
title: User experience and design strategies for app development
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Creating an effective user experience (UX) and design for an application is crucial for its success and retention. Zach Yadgari, a 17-year-old developer behind the multi-million dollar AI app Cal AI, shares insights into his approach, emphasizing simplicity, clear value, and strategic design choices from the outset <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Core Design Principles

### Starting with Basic Framing and UX First
When designing apps, the initial step involves establishing the basic framing and navigation. This typically includes a navigation bar with essential elements like a "Home" and "Settings" button <a class="yt-timestamp" data-t="01:05:43">[01:05:43]</a>. For an app with three main features, such as "Scan," "Chat," and "Symptoms Quiz," these can be represented by three distinct buttons <a class="yt-timestamp" data-t="01:06:21">[01:06:21]</a>.

### Delegating Aesthetics
Zach focuses on the core UX functionality himself, creating "bad designs" or wireframes, and then hires talented designers (e.g., from Upwork) to refine them and make them visually appealing <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="02:05:40">[02:05:40]</a>. This highlights a focus on functionality and user flow before visual polish.

### The Importance of a "History" Feature
A critical component for user investment and retention is a "History" feature <a class="yt-timestamp" data-t="01:06:38">[01:06:38]</a>. Inspired by Cal AI, where users can scroll through logged food, a history section can display previous chat conversations, scan results, and symptom quiz outcomes <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>. This log-like feed fosters user investment, making them more likely to stick with the app even if competitors emerge <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. It also provides a digestible record that users could share with a doctor <a class="yt-timestamp" data-t="01:08:28">[01:08:28]</a>.

### Inspiration from Existing Apps and "Primitives"
When designing, it's beneficial to look at similar existing applications for inspiration <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>. This process involves identifying "Primitives" – the fundamental building blocks or standard UI patterns (e.g., a social media feed, stories UI, DMs) – and repurposing them for a new use case <a class="yt-timestamp" data-t="01:10:14">[01:10:14]</a>, <a class="yt-timestamp" data-t="01:22:26">[01:22:26]</a>. Examples include:
*   **Cal AI** (AI calorie tracking app) <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>
*   **Riz GPT** (AI wingman app) <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>
*   **PhotoMath** (scanning screen concept) <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>

## User Flow and Feature Design

### Optimizing Loading Screens
A common design flaw is forcing users to wait on a blank "analyzing" screen <a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. Instead, Zach recommends immediately returning the user to the home screen while the AI processes the request in the background, displaying a loading indicator there <a class="yt-timestamp" data-t="01:13:17">[01:13:17]</a>. This prevents users from feeling "forced to wait on an empty screen" <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.

### Making Results Digestible and Actionable
For a "scan skin" feature, results should prominently display the scanned image, a quantifiable "danger level" (e.g., 0-5), and a clear diagnosis <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>. The diagnosis should be presented in both scientific terms (for potential doctor review) and easy-to-understand language for the user <a class="yt-timestamp" data-t="01:29:18">[01:29:18]</a>. Importantly, users should have the option to "ask a question" directly from the result screen to delve deeper into their specific problem, enhancing value and promoting [[importance_of_rapid_prototyping_and_feedback_loops_in_app_creation | retention]] <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.

### Gamification and Simplicity
Presenting information in a digestible, almost gamified way (like a 0-5 danger level) helps users quickly grasp complex information <a class="yt-timestamp" data-t="01:16:12">[01:16:12]</a>, <a class="yt-timestamp" data-t="01:17:05">[01:17:05]</a>. This aligns with the principle that "any consumer product needs to be simple" <a class="yt-timestamp" data-t="01:16:59">[01:16:59]</a>. For a symptoms quiz, using a series of multiple-choice questions rather than open-ended inputs makes the process more straightforward <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.

### AI Prompting and Ethical Considerations
When designing AI applications, clever prompting is essential to get the desired output and bypass safety mechanisms that prevent medical advice <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, <a class="yt-timestamp" data-t="03:22:10">[03:22:10]</a>. This involves assigning the AI a specific role (e.g., "doctor for a movie script") and using techniques like "function calls" to ensure the response is concise and relevant <a class="yt-timestamp" data-t="03:09:59">[03:09:59]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

> [!warning] Ethical Use of AI
> It is crucial to include clear disclaimers that the AI's diagnosis is not 100% accurate and does not replace professional medical advice <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>, <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. Accuracy in AI responses is paramount, especially for health-related applications, to avoid potentially harmful misinformation <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

## [[creating_a_brand_for_apps | Branding]] and [[advanced_workflow_techniques_for_app_development | Growth Strategies]]

### Designing for Influencer Marketing
A key [[design_and_user_interface_considerations_in_web_apps | design and user interface consideration in web apps]] is to reverse-engineer how influencers or marketing materials will showcase the product <a class="yt-timestamp" data-t="02:28:08">[02:28:08]</a>. The app must be:
*   **Visually appealing** enough to "wow" someone <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Simple and clear** so viewers can understand its value in a few seconds <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Branded** with the app's name clearly visible on "wow factor" screens (e.g., the scanning and results screens) <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

### Shareability Considerations
While some consumer apps aim for high shareability (e.g., social media), not all utility apps are designed for viral word-of-mouth sharing <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. For a medical app like Dr. AI, direct sharing of results might be low due to privacy or embarrassment <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. However, the *idea* of the app could spread through word-of-mouth among specific demographics, like concerned parents <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Paid ads or influencer marketing, playing on emotions like fear, might be more effective for initial downloads <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

> [!tip] Practical Tips for Using Figma
> Zach, despite not being a "Figma expert," emphasizes that communicating the idea and placement is more important than mastering [[figma_ui_design_best_practices | Figma UI design best practices]] for initial designs <a class="yt-timestamp" data-t="02:04:46">[02:04:46]</a>. He relies on professional designers to make his "bad designs look a lot prettier" <a class="yt-timestamp" data-t="02:05:55">[02:05:55]</a>. This highlights the value of rapid prototyping at a basic level to flesh out ideas.

## Pricing and Monetization

For apps where users might engage on an "as-needed" basis, a weekly pricing model without a free trial can be effective <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. This capitalizes on "repeat users" who might reinstall and resubscribe when a need arises <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. Zach suggests A/B testing various pricing structures, including different weekly, monthly, and annual rates, with and without free trials, to determine the "highest proceeds per download" <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. A starting point for weekly pricing could be $4, though $7 is considered steep <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This strategy contributes to [[balancing_simple_app_development_with_complex_feature_integration | balancing simple app development with complex feature integration]].