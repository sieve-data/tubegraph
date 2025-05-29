---
title: Building a successful AI startup
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Zach Yagari, a 17-year-old entrepreneur, has built an AI app called Cal AI that generates over $1 million a month in revenue <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. He shares insights into [[frameworks_for_ai_startup_success|building an AI startup]], including ideation, design, user experience, growth, and pricing, offering a free playbook for a similar idea <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Case Study: Dr AI

Zach presents an [[ai_in_startup_ideation_and_execution|AI startup idea]] called "Dr AI," an app designed to provide quick medical insights for skin issues and symptoms <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This app, unlike a mere GPT wrapper, could be built and launched as a full business in less than a month <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Problem Identification
The idea stemmed from a friend's experience where a scraped knee led to the discovery of skin cancer, highlighting the need for quick, accessible skin checks <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Many people, especially in countries like the US (where many are uninsured) or Canada (with bogged-down healthcare systems), lack immediate access to primary doctors <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The app aims to help users determine if a medical issue is safe to wait out or if a doctor should be seen immediately <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Proposed Features
Dr AI would have three main features <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>:
1.  **Skin Scan:** Users take a picture of something on their skin or body for identification, determining if it's harmful or benign <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  **Symptoms Quiz:** Users input symptoms (e.g., dry cough, chills) to receive possible sickness diagnoses, potentially with a likelihood percentage <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Chatbot:** A general Q&A feature for medical questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. ChatGPT has shown strong capabilities in diagnosing medical problems, even outperforming doctors in some studies <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Ethical Considerations
It is crucial that the app includes heavy disclaimers, stating that the diagnosis is not 100% accurate and should not be taken as definitive medical advice <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The goal is to provide an idea of whether a doctor's visit is necessary, not to replace professional medical care <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Accuracy is paramount, as an inaccurate diagnosis could have serious consequences <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

## Design and User Experience (UX)

Zach's approach to designing apps starts with basic framing and navigation <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. He typically sketches out the UX himself and then hires a designer (e.g., from Upwork) to refine the aesthetics <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Principles for App Design
*   **Simplicity and Digestibility:** Apps should be very simple and digestible for the user <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This means making information easy to understand, such as using a 0-5 danger level metric instead of vague text descriptions <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Gamification (Coincidental):** While not a primary goal, making elements like "danger level" gamified can enhance digestibility <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
*   **User Investment:** Building a history feature (e.g., previous chats, scans, quiz results) encourages user investment, making them more likely to stick with the app even if competitors emerge <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This history can also be shared with doctors <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Inspiration from Primitives:** When designing new apps, it's effective to look at existing "primitives" (building blocks) from other successful apps and repurpose them for the new use case <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Key App Elements (Dr AI Example)
*   **Navigation Bar:** Home, Settings, and three main feature buttons (Scan, Chat, Symptoms Quiz) <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **History Feed:** An "inscript feed" of past interactions, similar to Cal AI's food log <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Scan Skin Screen:** A simple camera interface with an upload option from the camera roll and scanning lines <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Result Screen:** Instead of a loading screen, immediately return the user to the home screen with a loading indicator, then display results <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. The results should include the scanned image, a danger level (e.g., 0-5), a diagnosis from the AI, and an option to "ask a question" for deeper follow-up <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. This follow-up capability aids retention <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Symptoms Quiz Flow:** A series of multiple-choice questions (e.g., "Do you have a cough? Yes/No") that adapt based on previous answers <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. The result could include a summary of responses and a diagnosis <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Optionally, sources could be displayed like on Perplexity <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.
*   **Chatbot Preview:** A simple preview of the last message in the history <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>.

## Technical Implementation

### Prompting Strategy
For [[building_ai_startup_using_ai_tools|AI startup using AI tools]] like Dr AI, it's critical to work around the AI's default disclaimers (e.g., "I am not a medical doctor") <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. Strategies include:
*   **Role Assignment:** Tell the AI to "take on the role of a doctor" <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
*   **Contextual Framing:** Frame the request as part of a movie script to bypass ethical filters <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>.
*   **Function Calls:** Using API features like function calls allows assigning the AI's response to a variable, ensuring only the desired output is received <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.

### Accuracy
Accuracy is paramount, especially for medical advice apps <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>. Unlike basic GPT wrappers, complex apps like Cal AI use multiple prompts in a pipeline to ensure high accuracy <a class="yt-timestamp" data-t="00:47:18">[00:47:18]</a>. Inaccurate information could be harmful <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>.

## Go-to-Market Strategy

The go-to-market strategy heavily relies on influencer marketing, particularly thinking about how influencers will showcase the product <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.

### Influencer Marketing
*   **Simplicity for Showcasing:** The app must be simple and clear enough for a viewer to understand its value within a 2-second glimpse in an influencer video <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
*   **Branding within the App:** Place the app's name ("Dr AI") prominently on the home screen and especially on "wow factor" screens (like the scan result screen) that influencers are most likely to show <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>.
*   **Identifying Target Audience:**
    *   **Low Shareability:** Apps like Dr AI (and Cal AI) have low natural shareability, as users typically don't share personal health or food data <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. Growth will likely come from paid ads or influencer marketing <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
    *   **Primary Target:** Concerned parents are the biggest audience for Dr AI <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>. Kids are less ideal as they are less willing to pay <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>.
    *   **Audience Research:** It's crucial to look at the *audience* of an influencer, not just their niche <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. This is done by manually reading comments on their posts <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>. For example, a "doctor" influencer might have an audience primarily of aspiring doctors, not concerned parents <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.
*   **Content Angle:** For Dr AI, an influencer could create a scenario where they were worried about a mark on their child, scanned it with the app, and found it was harmless, playing on parents' emotions <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>. The ad should "play on the emotions of a little bit of fearmongering on the idea that they might have some kind of disease or problem" <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
*   **Outreach:** Reach out to influencers via both email and direct message <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>.

## Pricing Strategy

For apps like Dr AI, a weekly pricing model often works well, especially for products that aren't needed daily but are frequently used on a "need basis" <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>.

*   **Weekly Pricing:** A suggested starting point is $4 a week, with no free trial <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>. The focus is on repeat users who subscribe, unsubscribe, and resubscribe when they need the service again <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>.
*   **AB Testing:** Utilize tools like Superwall to AB test different pricing tiers (e.g., $4/week vs. $7/week), monthly options ($10/month, $15/month), and annual options ($30/year, $70/year), as well as variations with and without free trials <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>. The goal is to find the highest "proceeds per download" <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
*   **Influencer Compensation:** To ensure profitability, compare RPM (revenue per thousand views) with CPM (cost per thousand views) <a class="yt-timestamp" data-t="00:41:16">[00:41:16]</a>. If an RPM of $5 is assumed, paying an influencer under $5,000 for 1 million views (e.g., four videos averaging 250k views each) would make the campaign profitable <a class="yt-timestamp" data-t="00:42:08">[00:42:08]</a>.

## Entrepreneurial Lessons from AI Startups

This detailed blueprint provides a solid roadmap for [[building a sustainable AI startup]], from initial design to market launch and growth <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>. The key is to prioritize clear communication of value, robust design, accurate AI implementation, and a well-researched [[growth_tactics_for_ai_startups|growth tactics for AI startups]] strategy <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. Zach Yagari openly shares this idea, hoping an audience member will take it and create a successful app, emphasizing the importance of disclaimers and accuracy <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a>.