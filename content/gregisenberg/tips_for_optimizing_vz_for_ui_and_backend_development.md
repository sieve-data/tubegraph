---
title: Tips for optimizing VZ for UI and backend development
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

VZ is an AI assistant developed by Vercel, specifically designed for [[using_vz_for_web_development_and_ui_design | web development]]. It helps with JavaScript, HTML, CSS, and integration with new frameworks and libraries, aiming to produce high-quality web products and simplify the coding and deployment process [01:06:03]. Lee, VP of Product at Vercel, shares insights on how to maximize VZ's potential for both user interface (UI) and backend development.

## Getting Started with VZ
[[introduction_to_vercels_vz | VZ]] acts as your personal [[vz_as_an_ai_tool_for_web_designers_and_developers | AI assistant]] for web development [01:08:11]. The goal is to make it as easy as possible to generate high-quality web components and ultimately, high-quality products [01:36:03].

### Starting Your Project
*   **Screenshot-Driven Design**: A highly effective way to start is by providing VZ with screenshots of designs you admire or want to emulate [02:57:07]. This gives VZ a clear visual starting point [03:16:09].
*   **Creative Modes**: You can approach VZ in two ways:
    *   **Opinionated Design**: If you have a specific vision, start with a screenshot or a clear idea of what you want [03:33:01].
    *   **AI-Driven Exploration**: If you don't know exactly what you want, let VZ generate initial ideas, and then iterate from there [03:40:02]. For example, you can ask it to "build a page where I can post a link, hit a button, and it'll send it to Slack," and VZ can provide a starting component [03:48:01].

## UI/Frontend Development Tips
Once you have an initial design, you can refine it through iterative prompting.

### Refining Design with Specificity
*   **Aesthetic Language**: Use descriptive terms to guide VZ's design output. Examples include:
    *   "Make it have warmer Grays" [04:56:04]
    *   "Use a Sanda font" [04:59:09]
    *   "Make the UI have a tighter information density" [05:12:05]
    *   "Less vertical spacing between the rows" [05:44:07]
    *   "Make the image it the album image Art smaller" [05:59:05]
    *   "Adjust the color scheme to be darker than the original but not full black" [10:03:08]
*   **Tailwind CSS Integration**: VZ "thinks" in Tailwind CSS [06:03:07]. If you're familiar with Tailwind, you can directly specify classes (e.g., "make it size four") for precise control [06:09:07].
*   **Incorporate Imagery**: Uploading or pasting images allows VZ to use them in the designs, significantly enhancing visual quality. Typography and imagery are crucial elements in web design [07:47:06].
*   **Natural Language Prompts**: You can speak to VZ as you would to a designer or a pair programmer [08:06:05]. Phrases like "that now playing bar is pretty wide like I would probably make that less" are effective [08:10:08].
*   **Mobile Responsiveness**: Request specific adjustments like "make the table mobile responsive" [08:47:09] or address issues such as "I can't see the table of songs because the image is so large, can you fix it?" [09:10:04].
*   **Animation Control**: VZ can fine-tune animations. If an animation feels slow, you can ask it to "make the sheet open up faster and make it have a better easing animation" [25:06:06]. VZ understands underlying animation properties like `cubic-bezier` easing functions [25:27:08].

### Learning and Inspiration
*   **Ask VZ for Advice**: Even if you're a novice designer, you can ask VZ for common design practices or patterns. For example, "I am a novice at design. I don't really know how to make my design look better but it's just lacking something like what do I have to do to make it look a little bit better?" [11:23:09]. VZ can provide fundamental advice on color schemes, white space, readable fonts, layout, and image quality [12:11:09].
*   **Understand Design Terminology**: If VZ uses terms you don't know (e.g., "sans-serif font"), ask it to explain them and their differences [12:39:07]. [[learning_web_design_basics_to_utilize_tools_like_vz | Learning web design basics]] helps you "go fast" after "going slow" to understand concepts [13:31:01].
*   **Seek External Inspiration**:
    *   **Godly.website**: This site offers design inspiration, allowing you to filter by categories like "startups" to see beautiful websites [14:17:09]. Screenshots from these sites can be used as starting points in VZ [14:43:08].
    *   **Patterns.dev**: Another resource for UI patterns that can be translated into VZ prompts [15:19:07].
*   **Leverage Shad CN UI**: [[introduction_to_vercels_vz | VZ]] is built on top of Shad CN UI, a system that allows building custom component libraries [16:11:00]. This means VZ can generate real React components for production websites, not throwaway code [16:19:09]. You can ask VZ for specific components like a "date picker" [17:11:00].

## Backend Development Tips
VZ isn't just for UI; it can also assist with backend logic and structure.

### Adding Interactivity and Logic
*   **Beyond UI**: You can use VZ for backend work, not just making UIs look nice [03:02:05]. After generating a UI, you can add interactivity and implement backend logic [03:09:07].
*   **Data Integration**:
    *   **API Calls**: VZ can help you swap out mock data with actual API calls by fetching external APIs or integrating with your database schema [21:00:09].
    *   **Database Schema Design**: You can provide VZ with your PostgreSQL schema and ask for the Object-Relational Mapping (ORM) for frameworks like Drizzle or Prisma (for JavaScript/TypeScript) or other languages like Rails or Laravel [21:25:00].
    *   **Schema Generation**: If you don't know the SQL code, you can describe your needs (e.g., "I need a table for users and emails") and VZ can help design the backend structure, including relationships [21:49:00].
*   **Performance Optimization**: Ask VZ to design the backend for speed. It might suggest using indexes on your database for faster common queries and provide the proper ORM schema incorporating these optimizations [23:18:00].

## General Workflow and Mindset
*   **Iterative Process**: VZ facilitates a rapid iterative process. Start with a basic idea or screenshot, then refine it through multiple versions, providing specific feedback and requests [04:30:08].
*   **Forking Projects**: You can "fork" existing VZ projects to experiment with different design directions (e.g., darker colors, new layouts) without losing your previous progress [09:34:04].
*   **AI as an Augmentation**: VZ and other AI tools are not replacements for developers; they are augmentations that act like a "knowledgeable super senior engineer" providing best practices and answering questions instantly [27:21:00]. This empowers builders to realize their ideas more efficiently than ever before [27:42:00].

To try VZ, visit VZ.dev, which offers a free tier [28:27:06].