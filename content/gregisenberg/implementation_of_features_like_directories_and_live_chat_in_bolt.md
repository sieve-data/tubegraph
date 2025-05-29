---
title: Implementation of features like directories and live chat in Bolt
videoId: 1SfUMQ1yTY8
---

From: [[gregisenberg]] <br/> 
[[introduction_to_boltnew | Bolt]] is presented as a powerful tool for quickly bringing ideas to market, even being dubbed a "[[comparison_between_boltnew_and_cursor_ai | Cursor AI]] killer" by some <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The co-founder of Stack Blitz, the maker of [[introduction_to_boltnew | Bolt]], Eric, demonstrated [[stepbystep_guidance_on_using_bolt_to_build_web_applications | how to use the product]] by building a directory and a live chat feature from scratch <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

## Building a Directory
The first project demonstrated was building a directory <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

### Initial Concept and Purpose
The idea was to create a directory similar to Product Hunt, focusing on products for founders, Indie hackers, and bootstrap founders <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. The goal was to attract SEO traffic and potentially evolve into a product with affiliate deals <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>, <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.

### Prompting Strategy
When prompting [[introduction_to_boltnew | Bolt]], it is helpful to describe the target audience and the desired "vibe" or "spiritual level" of the product, in addition to specific functionalities <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. For this directory, the prompt aimed for a site that provides "essential tools for Indie hackers" <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. The structure requested was one main page listing products and individual product pages for SEO optimization <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

### Initial Generation
[[building_a_prototype_with_boltnew | Bolt]] rapidly generated the initial codebase, including installing npm packages and writing files <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. The platform automatically pulls royalty-free images from sources like Unsplash to provide immediate visual content <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

### Handling Errors
When errors occur, a common troubleshooting step is to copy and paste the error message directly into [[introduction_to_boltnew | Bolt's]] chat interface, which will attempt to fix the issue <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.

### Adding Gamification and Design Enhancements
To enhance the directory, the following features were requested:
*   **Vertical listing** for products <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **Gamification**: Displaying product rankings (e.g., "number one, number two") and allowing users to upvote products, inspired by the Octalysis framework <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>, <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.
*   **Design**: Adding "pops of color" and "beautiful gradients" to make the site pop, drawing inspiration from sites like Arc Browser and Late Checkout Studio <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>, <a class="yt-timestamp" data-t="19:13:00">[19:13:00]</a>.

For complex functional changes, it's often better to break them into smaller, distinct prompts. For design changes, a single prompt can list multiple desired aesthetic improvements <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. The "undo" button allows rolling back changes if the result is not desired <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>. The final design successfully incorporated the requested color scheme and added subtle shadows <a class="yt-timestamp" data-t="22:15:00">[22:15:00]</a>, <a class="yt-timestamp" data-t="24:46:00">[24:46:00]</a>.

## Building a Live Chat Feature
To demonstrate more complex functionality, a live chat page was added to the directory site <a class="yt-timestamp" data-t="31:03:00">[31:03:00]</a>.

### Integration with Firebase
The live chat feature was implemented using Firebase for real-time communication and data storage <a class="yt-timestamp" data-t="32:23:00">[32:23:00]</a>. [[introduction_to_boltnew | Bolt]] recommends Firebase or Superbase due to their built-in authentication, real-time data storage, and synchronization capabilities <a class="yt-timestamp" data-t="32:03:00">[32:03:00]</a>. For prototyping, test mode can be used in Firebase to quickly get started without complex permission setup <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a>.

### Overcoming Challenges
During implementation, several challenges arose:
*   **AI Forgetting to Restart Dev Server**: Sometimes, the LLM forgets to restart the development server after making changes, requiring manual `npm run dev` <a class="yt-timestamp" data-t="36:16:00">[36:16:00]</a>.
*   **Locating Firebase Credentials**: Finding the necessary API keys in the Firebase dashboard was initially non-obvious, requiring creating a web app within Firebase project settings <a class="yt-timestamp" data-t="39:09:00">[39:09:00]</a>.
*   **Persistence Issues**: Messages were not persisting because the AI initially defaulted to Firebase Firestore, but the manual Firebase project was set up for Realtime Database. Specifying "use Firebase Realtime Database" resolved this <a class="yt-timestamp" data-t="42:52:00">[42:52:00]</a>.
*   **Login Requirement**: The initial chat implementation required signing in. To simplify the demonstration, the prompt was modified to remove the sign-in requirement <a class="yt-timestamp" data-t="40:33:00">[40:33:00]</a>.

A tutorial on [[stepbystep_guidance_on_using_bolt_to_build_web_applications | how to add a database to a Bolt.new app]] using Firebase is available for more detailed guidance <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>.

### Deployment and Live Chat
[[deployment_challenges_with_boltnew | Bolt]] allows direct deployment to production hosts like Netlify with a single click <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>. This generates a live URL that can be shared or linked to a custom domain for SEO <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>. After deployment, the live chat feature was successfully demonstrated with messages appearing in real-time across different locations <a class="yt-timestamp" data-t="45:51:00">[45:51:00]</a>.

## Comparison and Benefits
[[comparison_between_bolt_and_other_development_tools_like_cursor | Bolt]] is noted for its simplicity compared to traditional IDEs or tools like [[comparison_between_boltnew_and_cursor_ai | Cursor]], making it highly accessible for non-developers and entrepreneurs <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>. While [[comparison_between_boltnew_and_cursor_ai | Cursor]] excels in large, complex codebases for seasoned engineers, [[introduction_to_boltnew | Bolt]] is optimized for quickly building and launching full-stack web applications, including those with backend functionalities like authentication and payments <a class="yt-timestamp" data-t="29:08:00">[29:08:00]</a>.

### Real-life Examples
[[reallife_examples_of_products_built_using_bolt | Real-life examples of products built using Bolt]] include:
*   **Viral Hooks**: An app built by a PM from Thailand that helps create viral hooks for social media. It was built in about two weeks for $50/month using [[introduction_to_boltnew | Bolt]], compared to an Upwork quote of $3-5K over several months <a class="yt-timestamp" data-t="47:05:00">[47:05:00]</a>.
*   **CRM (e.g., CH Siam)**: Other users have built professional-looking CRMs <a class="yt-timestamp" data-t="49:02:00">[49:02:00]</a>.
*   **YC Startup Landing Pages**: Y Combinator startups have used [[introduction_to_boltnew | Bolt]] to quickly create professional landing pages, allowing their engineers to focus on core product development <a class="yt-timestamp" data-t="49:11:00">[49:11:00]</a>.

These examples highlight the significant time and cost savings offered by [[introduction_to_boltnew | Bolt]], enabling creative and entrepreneurial individuals to build and launch products rapidly <a class="yt-timestamp" data-t="48:24:00">[48:24:00]</a>, <a class="yt-timestamp" data-t="50:00:00">[50:00:00]</a>. The platform emphasizes the ability to build web apps directly in the browser, akin to creating documents or designs in cloud-based tools <a class="yt-timestamp" data-t="50:39:00">[50:39:00]</a>. To get started, users can visit bolt.new and input their ideas directly <a class="yt-timestamp" data-t="51:39:00">[51:39:00]</a>.