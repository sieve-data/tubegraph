---
title: Live demonstration of building with Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

This article details a live demonstration of building web applications using [[overview_of_bolt_as_a_new_prototyping_tool | Bolt]], a new prototyping tool, conducted by its founder, Eric. The demonstration showcases [[challenges_and_advantages_in_using_bolt_for_nontechnical_users | Bolt's]] capabilities for non-technical users and entrepreneurs, highlighting its speed and simplicity in getting ideas to market <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The session was unplanned, reflecting a real-world building process <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The Demonstrator: Eric from Stack Blitz
Eric is the founder of Stack Blitz, the company behind [[overview_of_bolt_as_a_new_prototyping_tool | Bolt]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. He used this opportunity to actively build with the product, identify potential areas for improvement, and share debugging tips <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Building a Product Directory
The first project proposed was a product directory, inspired by platforms like Product Hunt, aimed at [[entrepreneurial_opportunities_and_success_stories_using_bolt | Indie hackers]], builders, and bootstrap founders <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The goal was to create a trusted source for products that make their lives easier and more productive <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Prompting Strategy
Eric emphasized describing the "vibe" or "spiritual level" of the desired product in the prompt, alongside concrete functionalities <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. For the directory, the prompt included:
*   **Audience:** Indie hackers, builders, bootstrap founders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Purpose:** A trusted source for productivity products <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Functionality:** A main page listing five "products of the day" and individual product pages for SEO <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Monetization Idea:** Potential for affiliate deals with listed products <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Initial Build and Challenges
After submitting the prompt, [[building_a_web_application_prototype_with_bolt | Bolt]] quickly generated a codebase, installing dependencies and writing files <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Error Handling:** An initial compilation error occurred due to an unescaped quote <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Eric demonstrated how to fix this by copying the error message into the chat, allowing [[overview_of_bolt_as_a_new_prototyping_tool | Bolt's]] AI to attempt a resolution <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Image Generation:** [[building_a_web_application_prototype_with_bolt | Bolt]] automatically pulled royalty-free images from Unsplash for the directory entries, providing a visually appealing initial output <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Marketing Copy:** The AI generated marketing copy that aligned with the described target audience <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### Enhancing the Directory with Gamification and Design
The next step was to enhance the directory with features similar to Product Hunt, focusing on gamification and visual design.
*   **Requested Features:**
    *   Vertical listing of products <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
    *   Displaying product rankings (e.g., #1, #2, #3) <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   User upvoting functionality <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **Design Feedback:** The demonstrator asked for "pops of color" and "color gradients," even providing a screenshot of the Arc Browser site as inspiration to capture a specific "vibe" <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. [[building_a_web_application_prototype_with_bolt | Bolt]] successfully incorporated the color palette and added icons from the reference image <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Iterative Building:** Eric explained that it's often better to break down changes into distinct blocks, especially for functionality, to maintain control and leverage [[overview_of_bolt_as_a_new_prototyping_tool | Bolt's]] undo feature <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

### Deployment to Production
[[building_a_web_application_prototype_with_bolt | Bolt]] offers built-in deployment to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. With a single click, the application is built in the browser and uploaded, providing a real URL for sharing and SEO <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

## Building a Live Chat Application
To demonstrate more complex functionality, the team decided to add a live chat page to the existing directory site for Indie hackers to communicate in real-time <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.

### Backend Integration
*   **Choice of Backend:** Eric recommended using [[firebase_studio_app_prototyping_features | Firebase]] or Superbase for their built-in authentication and real-time data synchronization capabilities <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. He explicitly prompted Bolt to use [[firebase_studio_app_prototyping_features | Firebase]] <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>.
*   **[[firebase_studio_app_prototyping_features | Firebase]] Setup:** Eric created a new [[firebase_studio_app_prototyping_features | Firebase]] project and set up a Realtime Database in test mode for quick prototyping <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.
*   **Challenges with API Keys:** Locating the [[firebase_studio_app_prototyping_features | Firebase]] API keys for integration proved challenging within the [[firebase_studio_app_prototyping_features | Firebase]] console <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. Eric used a tool like Claude to find instructions, highlighting the value of AI for technical support <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.
*   **Debugging Real-time Chat:** Initially, messages were not persisting, found to be due to Bolt using Firestore instead of the Realtime Database Eric intended <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>. After ensuring the correct [[firebase_studio_app_prototyping_features | Firebase]] configuration, the chat functionality worked <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.
*   **Authentication Removal:** To simplify the demonstration, the authentication requirement for chatting was temporarily removed <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.

The live chat was successfully implemented and demonstrated with messages appearing in real-time <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.

## Comparison and Use Cases
### [[comparison_of_bolt_with_other_coding_tools_like_cursor | Bolt vs. Cursor AI]]
Eric noted that [[overview_of_bolt_as_a_new_prototyping_tool | Bolt]] is much simpler than [[comparison_of_bolt_with_other_coding_tools_like_cursor | Cursor AI]] for non-developers <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. While [[comparison_of_bolt_with_other_coding_tools_like_cursor | Cursor AI]] is a powerful tool for working with complex codebases at companies like Fortune 500s, [[overview_of_bolt_as_a_product_for_entrepreneurs | Bolt]] excels at quickly building and deploying full-stack web applications <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>. [[overview_of_bolt_as_a_new_prototyping_tool | Bolt's]] focus is on a high-level discussion with the AI agent, minimizing direct interaction with code <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

### [[entrepreneurial_opportunities_and_success_stories_using_bolt | Entrepreneurial Opportunities]]
[[overview_of_bolt_as_a_product_for_entrepreneurs | Bolt]] allows users to build robust applications with back-end features like authentication and payment processing (e.g., Stripe) <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.

Several success stories were highlighted:
*   **Viral Hooks:** A product manager from Thailand, Pitch, built an app called Viral Hooks entirely with [[overview_of_bolt_as_a_new_prototyping_tool | Bolt]] for $50 a month in about a week and a half <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This contrasts sharply with an Upwork quote of $3-5K over several months <a class="yt-timestamp" data-t="00:47:52">[00:47:52]</a>.
*   **YC Startups:** Even Y Combinator-backed startups use [[overview_of_bolt_as_a_product_for_entrepreneurs | Bolt]] to quickly create professional-looking landing pages, allowing their engineers to focus on core product development <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>.
*   **First Customers:** Over a dozen [[overview_of_bolt_as_a_product_for_entrepreneurs | Bolt]] users have already acquired their first customers for products built using the tool <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>.

## Conclusion
The demonstration underscored [[overview_of_bolt_as_a_new_prototyping_tool | Bolt's]] power to enable rapid iteration from idea to production for web applications <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>. It significantly reduces the time and cost associated with [[building_a_web_application_prototype_with_bolt | web application prototyping]] and deployment, especially for non-technical individuals <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.

Users can get started by visiting Bolt.new <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Additional tutorials, including one on [[using_api_integration_with_bolt | adding databases]] to [[overview_of_bolt_as_a_new_prototyping_tool | Bolt]] apps, are available <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.