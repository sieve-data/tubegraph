---
title: Designing user experience for AI apps
videoId: ZNIoIX0O-20
---

From: [[gregisenberg]] <br/> 

Designing a user experience (UX) for AI applications involves creating intuitive, digestible, and effective interfaces that leverage the power of artificial intelligence while addressing its unique challenges <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Zach Yagari, creator of the successful AI app Cal AI, shares his insights on building AI products, exemplified by a hypothetical app called Dr. AI <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Core Principles of AI App UX

### Simplicity and Digestibility
Apps should be designed to be very simple <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a> and digestible for the user <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This ensures that users can quickly grasp the app's value, especially when marketed through short-form videos <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. Presenting information, such as a danger level, as a numerical scale (0-5) or chart is more digestible than plain text <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

### Leveraging "Primitives" and Existing UI
When designing a new app's UX, it's beneficial to consider existing "Primitives" – the fundamental building blocks of apps that users are already familiar with <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. For example, social networking apps commonly use feeds, stories, and DMs <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. For AI apps, concepts like scanning screens are common across various applications, such as Cal AI and PhotoMath <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Rather than reinventing the wheel, existing UI patterns can be repurposed for new use cases <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

Zach typically starts with basic framing and sketches for the UX himself <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>, then hires a talented designer to make the designs look polished <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This allows for clear communication of the vision <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.

### User Investment and Retention
Incorporating a history or log feature helps users develop an investment in the product <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. This makes them more likely to stick with the app, even if competitors emerge <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. For Dr. AI, a history could include previous chats, scans, and symptoms quiz results <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This history could even be made digestible for sharing with a doctor <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Handling AI Processing
Instead of forcing users to wait on an "analyzing" or loading screen, especially for AI operations that can take 30-60 seconds, it's better to return the user to the home screen and show a loading indicator there <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This avoids making users feel like they're waiting on an empty screen <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

## Dr. AI: A Case Study in AI App UX

Dr. AI is conceived as an AI app for skin diagnosis and symptom assessment, offering an alternative to traditional doctor visits, especially in areas with healthcare access issues <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Main Features and Navigation
The app would feature a simple navigation bar with "Home" and "Settings" <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Its three main features would be:
1.  **Scan Skin**: Identify issues from a picture <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  **Symptoms Quiz**: Diagnose possibilities based on user-inputted symptoms <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Chatbot**: Answer general health questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

A "History" section would log previous interactions across all features <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Scan Skin Workflow
1.  **Capture/Upload**: Users are taken directly to a camera screen upon selecting "Scan Skin" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, with an option to upload from their camera roll <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Scanning lines visually indicate the AI's processing <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
2.  **Results Display**: After taking a picture, the user is returned to the home screen, and the analysis loads in the background <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. The results screen would prominently display:
    *   The image taken <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
    *   A "danger level" (e.g., 0-5) <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
    *   An AI-generated diagnosis in easy-to-understand terms <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>, with the option to "Ask Question" to delve deeper into the specific problem <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. This allows users to follow up on changes or specific concerns <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

### Symptoms Quiz Workflow
The symptoms quiz would ideally use a series of multiple-choice questions with limited answers (e.g., yes/no, then more specific options like "dry cough" or "wet cough") rather than open-ended input or checkboxes <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. The results would show a diagnosis with possibilities and potential likelihoods <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, possibly summarizing the user's responses <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Chatbot Workflow
The chatbot would function like a standard online chatbot interface <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>, with its history displaying the last message <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>.

## Key Considerations for AI App Design

### Gamification (Digestibility)
While not explicitly *gamified*, presenting information like a "danger level" as a 0-5 scale makes it highly digestible, similar to how video games present complex information clearly <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

### Shareability
The app's inherent shareability needs consideration. For a medical utility app like Dr. AI, direct sharing of sensitive results (e.g., a picture of a rash) is likely low <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. However, indirect word-of-mouth growth among target demographics (like concerned parents) can be significant <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

### [[using_ai_for_design_and_branding | Branding]] and Influencer Marketing
When designing for growth via influencer marketing, the app's UI must be clear and simple enough for viewers to understand its value within a 2-second phone screen appearance <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>. Key screens that will be heavily featured in marketing (like the scanning screen and results page) should prominently display the app's name (e.g., "Dr. AI") <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>. The app's "wow factor" feature (e.g., the skin scan and diagnosis) should be highlighted <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. Thinking about how an influencer will *show* the product and designing the product around that is a crucial insight <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.

### Prompting for Accuracy and Tone
A critical aspect of AI app design is crafting effective prompts for the underlying AI model. For Dr. AI, the AI needs to be specifically prompted to "take on the role of a doctor" and provide scientific yet understandable diagnoses <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>. To circumvent AI models' disclaimers about not providing medical advice, creative prompting techniques, such as framing the request as part of a "movie script," can be used to elicit the desired diagnostic output <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>. When [[using_apis_in_ai_app_development | using APIs]] directly, the prompt has full control, and function calls can be used to assign AI responses to specific variables for structured output <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

### Accuracy and Ethics
Despite the power of AI, it's paramount for medical-related apps to include strong disclaimers about accuracy and not to be taken as definitive medical advice <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>. Ensuring accuracy is crucial; unlike basic GPT wrappers, robust AI apps like Cal AI use complex pipelines with multiple prompts to achieve high accuracy <a class="yt-timestamp" data-t="00:47:18">[00:47:18]</a>. This is vital to avoid potentially harmful or misleading information <a class="yt-timestamp" data-t="00:47:25">[00:47:25]</a>.

In conclusion, effective UX design for AI apps prioritizes simplicity, leverages familiar design patterns, fosters user investment, strategically handles AI processing, and critically, ensures accuracy and ethical deployment of AI capabilities <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>.