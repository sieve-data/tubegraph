---
title: Live demonstration and building with Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 

Bolt, created by Stack Blitz, is highlighted as a powerful tool for rapidly developing and deploying applications. The platform's founder, Eric, provided a live, unprepared demonstration, showcasing its capabilities and how it simplifies the journey from idea to market <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This demonstration also involved troubleshooting and iterating in real-time, providing insight into the practical use of the tool <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Building a Product Directory

The first project undertaken was to build a product directory similar to Product Hunt, aimed at [[leveraging_replit_and_chatgpt_for_app_prototypes | Indie Hackers]] and Builders <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The goal was to create a trusted source for products that make their lives easier and more productive <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Initial Prompt and Philosophy
The initial prompt focused on the "spiritual level" of the product, describing the target audience and overall vibe rather than just functional requirements <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This approach helps Bolt's AI generate relevant marketing copy and aesthetics <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. The directory was planned to have a main page featuring the top five products and individual product pages for SEO benefits, with potential for affiliate deals <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Generation and Troubleshooting
Bolt rapidly generated the codebase, including installing dependencies and writing files <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. An initial error was encountered due to an unescaped quote in the AI-generated code <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. This was resolved by copying the error into the chat, allowing Bolt's AI to fix it <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The platform is also trained to pull royalty-free images from sources like Unsplash to provide immediate visuals <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

The generated directory, "Essential Tools for Indie Hackers," displayed products with marketing copy tailored to the audience <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Each product also had its own detailed page <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

### Enhancing the Directory
To improve the directory, the following changes were requested:
*   Vertical listing instead of horizontal <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   Gamification: displaying product rankings (e.g., "Product of the Day #1, #2") <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   User upvoting functionality <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

The design was further enhanced by requesting "pops of color" and "beautiful color gradients," using an image of the Arc browser's website as inspiration <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Bolt successfully applied the color palette and added icons, transforming the design <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

### Deployment
One of Bolt's key features is its [[deployment_and_practical_use_cases_of_applications_made_with_bolt | built-in deployment]] to production hosts like Netlify <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. By clicking a "deploy" button, Bolt performs a production build and provides a real URL for the application, allowing users to attach custom domains and benefit from SEO ranking <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. The process is done entirely in the browser, without requiring a login <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

## Building a Chat Application

To demonstrate Bolt's ability to create more complex applications, a live chat page was added to the existing directory site, allowing [[leveraging_replit_and_chatgpt_for_app_prototypes | Indie Hackers]] to communicate in real-time <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

### Firebase Integration
For backend functionality, Firebase was chosen as the database provider due to its compatibility with Bolt, built-in authentication, and real-time data storage <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. The chat functionality was built by first setting up a Firebase project and creating a Realtime Database in test mode <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.

### Challenges and Resolution
During the setup, locating Firebase API keys and understanding its project structure proved challenging, even for an experienced developer <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>. This highlighted areas for future improvement in Bolt's integration with third-party providers <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a>. The initial attempt to add chat functionality included a sign-in requirement, which was temporarily removed to simplify debugging <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. This iterative approach, adding one feature at a time, is recommended for complex functionalities <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.

After integrating the correct Firebase credentials and ensuring the Realtime Database was used, the chat functionality became live <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>. The chat successfully demonstrated real-time communication between users located in different parts of the country <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>.

## Bolt vs. [[comparisons_between_bolt_and_other_tools_like_cursor | Cursor]]

Bolt is positioned as a simpler, more intuitive tool compared to [[comparisons_between_bolt_and_other_tools_like_cursor | Cursor]], especially for non-developers or entrepreneurs focused on shipping products quickly <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. While [[comparisons_between_bolt_and_other_tools_like_cursor | Cursor]] is a powerful IDE designed for complex codebases and seasoned engineers, Bolt prioritizes a high-level, natural language discussion with the AI agent, minimizing direct code interaction <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>.

Bolt allows for [[creating_functional_applications_using_bolt | building full-stack web applications]] with backend features like authentication and payment processing (e.g., Stripe and Superbase integration) <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>. Although [[comparisons_between_bolt_and_other_tools_like_cursor | Cursor]] can build any type of software, Bolt excels in rapidly bringing web app ideas to production <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.

## Real-World Impact and Future of Bolt

Bolt empowers creative and entrepreneurial individuals to build and launch professional-looking products with unprecedented speed and cost-effectiveness <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>. An example shared was "Viral Hooks," an app built entirely with Bolt by a non-developer, which saved thousands of dollars and months of development time compared to hiring a contractor <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. Many users have already launched products and acquired their first customers using Bolt <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>. Even YC startups utilize Bolt for tasks like building landing pages, allowing their core engineering teams to focus on specialized backend work <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>.

The long-term vision for Bolt and Stack Blitz is to enable building web apps directly on the web, akin to creating documents in a browser or designs in Figma, without needing local downloads <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>.

## Getting Started

To get started with Bolt, visit bolt.new <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>. Users can type in their ideas into an input box to begin creating <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>. For tutorials and updates, follow @stackblitz on X (formerly Twitter) or join their Discord community at discord.gg/stackblitz <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>. A specific tutorial on how to add a database to a Bolt app using Firebase is also available <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.