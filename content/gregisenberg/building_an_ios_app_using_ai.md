---
title: Building an iOS app using AI
videoId: 4oNLQUznT8A
---

From: [[gregisenberg]] <br/> 

This article provides clarity around [[building_apps_using_ai_tools | building with AI]], focusing on how business-oriented and marketing-oriented individuals can effectively communicate their app ideas and prototype software <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. It highlights how non-engineers can [[building_apps_using_ai_tools | build things with code]] despite not knowing how to code, by building the product first and then learning about the underlying code <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

## Tools for Building iOS Apps with AI

The primary tools discussed for [[integrating_ai_features_in_ios_apps | building iOS apps with AI]] are:

*   **Xcode**: Apple's integrated development environment (IDE) for macOS, used to develop software for Apple's platforms. It's the environment for creating iOS apps <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Swift**: The programming language that iOS is built on <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. The generated Swift code is relatively easy to understand <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **[[using_ai_and_cursor_to_build_mobile_apps | Cursor]]**: An AI coding assistant used to generate the necessary code for the app <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Unlike web apps, [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] is used directly with Xcode, without needing [[building_apps_with_ai_using_replit | Replit]] as a codebase <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **iPhone Simulator**: An emulation of an iPhone within Xcode that allows for testing the app directly on the computer <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Process of Building an iOS App with AI

### Setting Up the Environment

1.  **Create a New Project in Xcode**: Start by creating a new project and saving it to a specific location <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  **Connect [[using_ai_and_cursor_to_build_mobile_apps | Cursor]]**: Open [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] and select "open via file," choosing the same project file to establish a connection <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This setup is quicker than for web apps <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Generating and Running the App

1.  **Prompt [[using_ai_and_cursor_to_build_mobile_apps | Cursor]]**: Use the composer in [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] (Command+Shift+I) to describe the desired app <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   **Example**: "Create a simple onepage app that lets me write my notes and save them to my phone" <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  **Local Storage**: For iOS apps, notes can be saved locally to the phone's files, eliminating the need to set up Firebase, which often leads to errors <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  **Run the App**: After [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] generates the code, save all files in Xcode and run the app on the iPhone simulator by hitting the play button <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. The build must succeed, otherwise it will display "build failed" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

### Iteration and Prototyping

*   **Modifying the App**: Users can go back to [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] to request changes, such as modifying text or colors <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. After each update, the app needs to be re-run in Xcode <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Deploying to a Device**: The app can be immediately deployed to a physical iPhone by enabling developer mode <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The app remains on the phone for a maximum of seven days <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **TestFlight**: For sharing with others, a TestFlight account can be set up, allowing users to test the app <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Advantages of Using AI for iOS App Development

*   **Rapid Prototyping**: It's possible to build a full mockup for an app and deploy it to the web for testing without knowing how to code <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Tangibility**: iOS apps feel more "tangible and fun" than websites <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Testing on a physical phone while on a walk is easy and convenient <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Empowerment**: Non-developers can gain "aha moments" by seeing their ideas come to life quickly, turning them from "idea guys" into "prototype guys" <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Fast Feedback Loop**: This process enables a rapid feedback loop, allowing creators to quickly build and test ideas with a community to determine demand, which is a "huge unlock" compared to traditional, months-long development cycles <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>.

## Considerations and Challenges

*   **App Store Release**: Releasing apps on the Apple App Store is time-consuming and annoying due to Apple's strict monitoring policies, content regulations, and 30% cut on sales <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. However, this is less of an issue if the goal is only testing and prototyping <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Xcode File Management**: Historically, anytime [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] added a new file, it needed to be manually added in Xcode, though this specific step appears to have improved <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Re-running the App**: Every time an update is made, the app must be re-run on Xcode, which can take a bit longer than with web apps <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

## Prototyping with Vercel (V0)

While Xcode and [[using_ai_and_cursor_to_build_mobile_apps | Cursor]] are for full app prototyping, Vercel (V0) is highlighted for rapid front-end design and mockups, particularly for web interfaces and landing pages <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

*   **Project Feature**: V0 allows users to input company and app information once, enabling the AI to consistently generate content for landing pages, "about us" pages, etc., without re-entering details <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Creative Generation**: V0 is noted for its creativity, coming up with original ideas, and its speed <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   **Prompting**: Users can be prescriptive (e.g., specific panels, features, themes like "VS Code-like app but for writers") or let the AI be more creative <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Sharing and Forking**: Designs can be forked to iterate on them without losing context or shared via public links <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. These links can be compiled into documents (e.g., Google Docs) to map out the entire site for developers <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Landing Page Creation**: V0 can generate highly effective landing pages with a single prompt, even embedding forms from services like Tally <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. This allows for collecting user sign-ups and feedback almost instantly <a class="yt-timestamp" data-t="00:29:59">[00:29:59]</a>.

## General AI App Development Strategies

*   **Focus on Good Examples**: When [[ai_app_development_strategies | building an AI app]], it's crucial to have really good examples and stay focused on a narrow scope, rather than trying to do everything <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   **Creator Composer Concept**: The ability to build things with a community and quickly get feedback (positive or negative) on features fosters a fast feedback loop, making such individuals "the most dangerous" in development <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.
*   **Put Ideas Out There**: Don't just be an "idea guy or gal"; become a "prototype guy or gal" and put your creations out there to gather voice-of-customer feedback, even if it means discovering that people don't want the product <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.