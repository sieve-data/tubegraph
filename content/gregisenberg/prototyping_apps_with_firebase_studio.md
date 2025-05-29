---
title: Prototyping apps with Firebase Studio
videoId: 1SbngfzEhbA
---

From: [[gregisenberg]] <br/> 

[[Firebase Studio features and capabilities | Firebase Studio]], newly launched by Google, is a free AI coding tool designed to help users take an idea, prototype it, and deploy it <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. It is tightly integrated with Google Firebase <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. As of its recording, the product was less than two weeks old <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Getting Started with Firebase Studio

Upon opening [[Firebase Studio features and capabilities | Firebase Studio]], users see their workspaces and any previous projects <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. A key feature is the inclusion of numerous project templates <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. These templates, available for React, Next.js, React Native, and Flutter applications, provide boilerplate code with built-in best practices, eliminating the need to start from scratch <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Target Audience

[[Firebase Studio features and capabilities | Firebase Studio]] is primarily aimed at a more technical user base <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Its interface, resembling an IDE with numerous files and configurations, assumes some familiarity with code <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. In contrast, tools like Lovable or Bolt are designed for users with little to no coding knowledge <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Prototyping Capabilities

### Using the Gemini Tab (Code Editor View)

[[Firebase Studio features and capabilities | Firebase Studio]] leverages Google's Gemini model for code generation <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Users can access a "Gemini" tab within the code editor view to generate code <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. While Gemini Pro 2.5 is the latest model, it may require a Gemini API key for free access <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

When generating a "Tinder for dogs" app as an example, [[Firebase Studio features and capabilities | Firebase Studio]] immediately displays a web preview <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. The images for the app were sourced by Gemini from a public API of dog images <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>, <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Using the App Prototyping Agent (Simplified View)

For a less overwhelming experience, [[Firebase Studio features and capabilities | Firebase Studio]] also offers an "app prototyping agent" accessible from the homepage <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This provides a text-based interaction, similar to what might be expected from Bolt or Lovable <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>, <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. It generates a plan for the app, which can be edited, before proceeding with the prototype <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>, <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This simplified view is only for the initial prototyping phase; further development requires switching to the more complex code editor view <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>, <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## [[Comparison between Firebase Studio and Lovable | Comparison with Lovable]]

A side-by-side [[comparison between Firebase Studio and Lovable | comparison]] using a prompt for a budgeting app reveals key differences:

*   **User Interface (UI)**: Lovable's interface is described as calmer and less overwhelming, while [[Firebase Studio features and capabilities | Firebase Studio]]'s UI, even in its prototyping view, presents a lot of buttons and files that can be daunting for non-developers <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>, <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Lovable's designs are also generally cleaner and include animations out of the box <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>, <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Code Visibility**: [[Firebase Studio features and capabilities | Firebase Studio]] shows the generated code directly as it works <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Lovable, conversely, hides the code by default, focusing on the interface, though the code can be viewed by clicking a button <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This reflects their different intended user bases <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Error Handling**: [[Firebase Studio features and capabilities | Firebase Studio]] surfaces issues and prompts the user to fix them <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>, <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. However, it can sometimes get into "death loops" of recurring errors <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
*   **Authentication Flow**: While [[Firebase Studio features and capabilities | Firebase Studio]] struggled with implementing a user sign-in flow and broke the app in the process <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>, <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>, Lovable was able to set up user authentication seamlessly, including integration with Superbase for confirmation emails <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>, <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

## [[Integration of Firebase Studio with Google ecosystem | Integration with the Google Ecosystem]]

[[Firebase Studio features and capabilities | Firebase Studio]] offers tight [[integration_of_firebase_studio_with_google_ecosystem | integrations]] with the broader Google ecosystem <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This includes:
*   One-click deployment to Firebase web hosting <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>, <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   Quick deployment to Google Cloud Platform (GCP) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   Connections to Google Maps and Secret Manager <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

These integrations make [[Firebase Studio features and capabilities | Firebase Studio]] particularly appealing to developers already familiar with and building on Google Cloud and Firebase <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. While Firebase offers more control over underlying Postgress SQL instances compared to Superbase, it is generally suited for more technical users <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

## Current State and Future Outlook

[[Firebase Studio features and capabilities | Firebase Studio]] is currently in an alpha or "preview" stage <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>, <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>, and as such, it is "far from perfect" and not yet ready for serious development <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>, <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>. Its launch was likely rushed due to market pressure from competing products like Lovable (formerly GPT Engineer) and [[building_ai_apps_with_cursor_firebase_and_vercel | Cursor]] <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>, <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>, <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

Despite its current limitations, there is strong optimism for the future of [[Firebase Studio features and capabilities | Firebase Studio]] <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>, <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>. Google's Gemini 2.5 Pro model is highly capable, especially for UI generation <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>, <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. It is expected to become a "mega competitor" to tools like Windsurf and [[building_ai_apps_with_cursor_firebase_and_vercel | Cursor]] as the models improve and potentially leverage private Google models <a class="yt-timestamp" data-t="00:28:39">[00:28:39]</a>, <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The product is also expected to attract more users into the Firebase ecosystem <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.

## Conclusion

[[Firebase Studio features and capabilities | Firebase Studio]] is a powerful, free tool for [[prototyping_and_interaction_design_in_figma | prototyping]] applications, particularly for those with a technical background and familiarity with the Google ecosystem <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>, <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>. While it's currently in an early, imperfect state, its potential for growth is significant, especially given the rapid advancements in AI models <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>, <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.

For less technical users, platforms like Lovable, Bolt, and [[prototyping_and_deployment_made_easy_with_replit | Replit]] offer more user-friendly approaches to app development <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>, <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. For advanced developers, tools like Windsurf, [[building_ai_apps_with_cursor_firebase_and_vercel | Cursor]], and Tempo Labs are also available <a class="yt-timestamp" data-t="00:32:49">[00:32:49]</a>. Regardless of the tool chosen, users are encouraged to experiment and recognize the potential to build real businesses from these prototypes <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>, <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>, <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.