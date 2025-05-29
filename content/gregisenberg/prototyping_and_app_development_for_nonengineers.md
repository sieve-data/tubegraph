---
title: Prototyping and app development for nonengineers
videoId: 4oNLQUznT8A
---

From: [[gregisenberg]] <br/> 

This episode aims to provide clarity on [[Building with AI]] and app development, specifically focusing on how business and marketing-oriented individuals can effectively communicate their app ideas for pitching to teams or as a guiding vision for building software <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The discussion emphasizes practical approaches to [[Prototyping and scaling startups using Replit | prototyping]] for those without a traditional engineering background <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Building with Code as a Non-Engineer

Despite not being a trained engineer or knowing how to write basic code like "hello world," it's possible to build full mockups for apps and deploy them to the web using templates <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This process fosters learning to code "in the opposite way": by building the thing first and then learning about it, rather than learning then building <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Prototyping iOS Apps with Xcode

Xcode is a powerful tool that allows for [[Prototyping and app development for nonengineers | prototyping]] iOS apps <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. iOS apps are built on Swift, and while the speaker doesn't write code, understanding generated Swift code for iOS apps is relatively easy <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Setup and Connection
To get started with Xcode and Cursor (an AI code generation tool):
1.  Create a new project in Xcode and save it to a specific location <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
2.  Open Cursor and select the same file via "open via file" to connect the two <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
This setup is quicker than configuring a web app <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Creating a Simple Notes App
Using Cursor's composer (accessed via `Command Shift I`), you can prompt it to create an app:
*   "Create a simple one-page app that lets me write my notes and save them to my phone" <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   iOS allows saving things locally to the phone's files, eliminating the need to set up Firebase, which can be time-consuming and error-prone <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   Once the code is generated, save all files and run the app on the iPhone simulator within Xcode <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This process is generally recommended as a starting point over web apps, especially for those who want a database <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

#### Iterating on the App
You can continue to refine the app with prompts, such as:
*   "Please make the top say 'Sip notes'" <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   "Make the top say 'Startup Ideas' and then make the button say 'Add Idea'" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   "Change the color theme" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
After each change, you save all and rerun the app on Xcode <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Deploying and Testing
While releasing apps to the App Store can be time-consuming due to Apple's strict monitoring and content regulations <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, testing is straightforward:
*   You can immediately deploy the app to your physical iPhone by putting it in developer mode <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The app lives on the phone for a maximum of seven days <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   It's easy to create a TestFlight account to share the app with others <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
This makes the app more tangible and fun to test, and it's not overly time-consuming if the goal isn't full deployment <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Building an app, even a simple one, can significantly stimulate new ideas and understanding <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

## Prototyping Web Apps with Vercel (Vzer)

[[Using Bolt for rapid prototyping and deployment | Vercel (Vzer)]] is useful for [[Prototyping and app development for nonengineers | prototyping]] web applications, particularly for front-end design <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Key Features of Vercel for Prototyping
*   **Project Feature**: Allows you to input information about your company or app (e.g., "Yap thread") so you don't have to re-enter it repeatedly <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. This enables prompts like "create a landing page for Yap thread" or "create an about us page with Yap thread" <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   **Creativity and Speed**: Vercel is highly creative compared to other AI tools like Claude Artifacts and generates original ideas quickly <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. It's also fast and shareable <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

### Example: VS Code-like App for Writers
An example prototype involved creating a "VS Code-like app but for writers," with specific panel layouts:
*   Left panel: Note titles <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   Middle panel: Markdown editor <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   Right panel: Custom presets (AI prompts) for editing the middle panel <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

#### Iterating for Content Creators
The app concept was refined to cater to internet writers and content creators:
*   Presets renamed to "Tweet thread," "TikTok script," "Podcast intro," "Outline," and "Newsletter," "Instagram Carousel" <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   Left panel titles to be "about posts on social media" <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
This iteration process helps define what each page should look like <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. If actually built, such an app would connect to a database like Firebase for data storage <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

### Sharing and Forging Prototypes
*   **Forking**: Recommended for iterating on a prototype to manage context and prevent performance degradation <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   **Public Links**: Prototypes can be shared via public links and organized in documents like Google Docs, where each page can be hyperlinked. This allows for mapping out the entire site vision for developers <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Whimsical Diagrams**: Can be used to show how buttons lead to different pages in the prototype <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

### Creating Landing Pages
Vercel is particularly effective for quickly creating landing pages <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
*   You can create a landing page from a single prompt, even incorporating elements like a logo generated by Midjourney and embedding a form from services like Tally for waitlist sign-ups <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>.
*   Tally offers a free tier and a low-cost premium tier without branding <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
*   These prototypes allow for immediate feedback collection, enabling rapid iteration and validation of ideas <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>.

## The "Creator Composer" Mindset

It's crucial to be a "prototype guy or gal" rather than just an "idea guy or gal" <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. Getting a prototype out quickly helps gather voice of customer feedback, which might reveal that a product isn't desired <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>. This rapid feedback loop is a significant advantage <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

Individuals who can [[Development and troubleshooting in app creation | build things]] with a community and quickly solicit feedback are considered "creator composers" and are "the most dangerous people" in terms of rapid innovation <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>. This contrasts with outsourced development, where basic features can take months to implement <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

There's a plan to release app code for "feature contests," where community members can fork the code and add features, fostering collaborative [[Innovative app development strategies | development]] <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.