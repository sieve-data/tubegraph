---
title: Product management and AI prompting
videoId: mJwPvyc4-rk
---

From: [[gregisenberg]] <br/> 

This article, featuring Ras Mike, delves into how to effectively utilize [[leveraging_ai_in_product_and_marketing_development|AI tools]] and models to build a Software as a Service (SaaS) startup, specifically highlighting the tool Lovable <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core premise is that to get the most out of rapidly evolving [[sequential_prompting_ai_workflows|AI tools]], users need to improve their own approach, treating themselves as product managers <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## The Challenge with AI Tools

Many users struggle with [[leveraging_ai_in_product_and_marketing_development|AI tools]] generating incorrect outputs or "hallucinating" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This often stems from users providing insufficient or unclear prompts <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Expecting an AI model to build exactly what's in your mind from a single, vague prompt is described as "daydreaming" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## AI Prompts as Product Management

To overcome these challenges, users should frame themselves as product managers when interacting with [[sequential_prompting_ai_workflows|AI models]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Role of a Product Manager
In a traditional corporate tech environment, product managers define what needs to be built <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. They gather information from various stakeholders, such as UX teams and business strategists, and distill it into precise requirements for developers <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This includes creating a Product Requirement Document (PRD) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

A product manager's responsibilities include defining:
*   The market and customer <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
*   Launch timing, sales, and marketing collateral <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
*   The problem and value proposition <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>
*   Competitors, products, and capabilities <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>
*   Requirements and roadmaps (PRD) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
*   Internal and external stakeholder communication <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>
*   Being a product evangelist and champion <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>

Ultimately, a product manager sits at the intersection of UX, tech, and business <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. Their job involves significant documentation and note-taking to ensure clear communication <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Applying to AI Prompting
Users must collect all necessary information, defining flows, features, and the core product with extreme precision <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Just like developers can build the wrong thing if product managers don't communicate clearly, [[sequential_prompting_ai_workflows|AI models]] will fail if prompts are vague <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. AI models are "dumb" in that they predict based on training data but don't inherently know user intent <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Therefore, being a "product person" is crucial for getting the best out of [[leveraging_ai_in_product_and_marketing_development|AI tools]] <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

> "Don't assume the model knows. The models are dumb, they're trained on thousands of lines, millions of lines of code so they can sort of predict what you're exactly asking them, but they don't know, you are the one to know." <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

## Understanding Web Basics for AI Prompting
Beyond product management principles, a basic understanding of web architecture helps users prompt [[sequential_prompting_ai_workflows|AI tools]] more effectively <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

### Three Sections of the Web
A functional website or SaaS typically consists of three main sections:
1.  **Client-side (Frontend)**: What the user sees and interacts with, like a website's [[building_and_designing_the_user_interface_with_ai_assistance|user interface]] or landing page <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Tools like Bolt use React for the frontend <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>, and Vercel's v0 uses Next.js <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
2.  **Server-side (Backend)**: Where complex logic, APIs, and business rules are processed <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This is generally considered the more difficult part due to security and scalability concerns <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
3.  **Data Storage (Database)**: Where all application data is stored, ensuring persistence for user accounts and information <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Backend as a Service (BaaS)
Companies known as Backend as a Service (BaaS) providers handle the server and database infrastructure, allowing developers to focus on the frontend <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Examples include Superbase and Convex <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

*   **Superbase**: Excels with PostgreSQL databases and developer experience <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Convex**: Strong for real-time applications like chat or collaborative tools <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

Understanding these components helps users articulate precise needs when prompting [[sequential_prompting_ai_workflows|AI models]] <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. For instance, prompting an AI to "create a landing page" without specifying backend needs will only result in a frontend design <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

## Practical Application with Lovable
Lovable is a new [[leveraging_ai_in_product_and_marketing_development|AI developer tool]] that directly integrates with Superbase <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. This integration allows users to set up backend, database, and authentication with a single prompt <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

### Building a Note-Taking SaaS for Founders
A demonstration using Lovable to build a note-taking SaaS for founders illustrated the process:
1.  **Initial Prompt**: "I want to build a not taking SAS for Founders. There should be a user authentication, there should be a nice clean landing page explaining why founder need my SAS." <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>
2.  **Superbase Integration**: Lovable's direct integration with Superbase allows for one-click connection to handle authentication and database table setup <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This process involves complex SQL commands and security policies that would otherwise be difficult for non-developers <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.
3.  **Authentication**: After connecting Superbase, the AI can be prompted to implement sign-up and login functionality <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>. The system handles email verification and stores user data in the Superbase database <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.
4.  **Note-Taking Page**: The next step was to prompt for the note-taking page, specifying that only authenticated users should access it <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>. The AI creates the necessary database tables to store notes, linking them to specific user IDs <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.
5.  **User Experience and Flows**: Refinements, such as adding a navigation bar and directing signed-in users to the notes page, demonstrate the iterative process of product management through prompting <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>.
6.  **Deployment**: Lovable also supports public deployment, making the full SaaS application accessible online <a class="yt-timestamp" data-t="00:47:05">[00:47:05]</a>.

The ability of these tools to abstract away difficult tasks like authentication maintenance (e.g., when a service like Figma changes its API) is a significant advantage <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.

## Future of AI Building
The landscape of building applications with AI is rapidly changing. Ras Mike suggests that many current technical skills, such as manually integrating databases, will become redundant as [[sequential_prompting_ai_workflows|AI tools]] develop direct integrations and templates <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

The future "moat" or competitive advantage for builders will lie in:
*   **[[building_and_designing_the_user_interface_with_ai_assistance|Design]] and [[improving_content_engagement_with_aigenerated_insights|User Experience]]**: Creating a richer, better experience that solves user problems <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
*   **Distribution**: Attracting users to the product <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>.

The actual "building" of the product is becoming commoditized due to advanced [[leveraging_ai_in_product_and_marketing_development|AI tools]] <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. This shift empowers non-technical founders to build multi-million dollar businesses without needing a CTO <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.